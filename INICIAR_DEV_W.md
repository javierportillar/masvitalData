# INICIAR · Dev W (PC Windows MasVital)

> **Para vos.** Este documento es tu única fuente operativa para configurar el PC Windows de MasVital de cero a corriendo el pipeline automático. Si seguís estos pasos en orden, en ~3-5 horas el sistema está vivo.
>
> **Regla operativa.** Sos el ÚNICO rol que toca el PC físico. Ni el PO ni Dev Back ni Reviewer ingresan al PC. Si necesitás aclaraciones técnicas, pedilas en el PR donde el Dev Back te dejó el código — no toques nada por intuición.

---

## 0 · Pre-requisitos del PO antes de empezar

Antes de que empieces, el PO te tiene que haber dado:

- [ ] Acceso físico o remoto al PC Windows MasVital (Anydesk, RDP, presencial)
- [ ] Credenciales de administrador del Windows
- [ ] Credenciales root del MySQL local de MasVital (para crear usuario `api_read`)
- [ ] Confirmación de la ruta donde clonarás el repo (recomendado: `C:\Users\MasVital\Documents\masvitalData`)
- [ ] Acceso a las variables sensibles que vas a poner en `.env` (R2, HuggingFace, OpenCode, Telegram chat ID si aplica)

Si falta algo de esto, pausá y pedilo al PO. NO sigas.

---

## 1 · Instalar pre-requisitos del PC

### 1.1 Git

```powershell
# Verificar si ya está
git --version
# Si no, descargar desde https://git-scm.com/download/win e instalar
```

### 1.2 Python 3.11+

```powershell
python --version
# Si < 3.11, instalar desde https://www.python.org/downloads/
# Durante la instalación, marcar "Add Python to PATH"
```

### 1.3 Cliente MySQL (para backups + verificación)

```powershell
mysql --version
# Si no está, descargar MySQL Command Line Client desde https://dev.mysql.com/downloads/
```

### 1.4 PowerShell ExecutionPolicy

Para que los scripts `.ps1` corran:

```powershell
# Una vez, como Administrador
Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned
```

---

## 2 · Clonar el repo

```powershell
cd C:\Users\MasVital\Documents
git clone https://github.com/javierportillar/masvitalData.git
cd masvitalData
```

---

## 3 · Crear entorno virtual e instalar dependencias

```powershell
# Crear venv
python -m venv .venv

# Activar
.\.venv\Scripts\Activate.ps1

# Una vez que Dev Back haya poblado pipeline/ y pipeline/requirements.txt
pip install -r pipeline/requirements.txt
```

Validación rápida:

```powershell
python -c "import duckdb, pymysql, boto3, httpx; print('OK')"
```

---

## 4 · Configurar `.env`

```powershell
# Copiar plantilla
Copy-Item .env.example .env
notepad .env
```

Completá los valores. Las variables están documentadas en `.env.example` con un comentario al lado de cada una. **Las variables `R2_*`, `HF_API_TOKEN`, `OPENCODE_API_KEY` son las mismas que ya usás en MotoShop** (compartidas, mismo bucket). Las `MYSQL_*` son específicas del PC MasVital.

NUNCA pegues el `.env` a chat ni lo commits — el `.gitignore` lo protege pero verificá manual:

```powershell
git status   # .env NO debe aparecer
```

---

## 5 · Crear usuario MySQL `api_read` (SELECT-only)

Conectate al MySQL local con tu cliente preferido y ejecutá:

```sql
-- Reemplazar 'TU_PASSWORD_FUERTE' por la que vayas a usar
-- Reemplazar 'masvital_db' por el nombre real de la BD de MasVital
CREATE USER 'api_read'@'localhost' IDENTIFIED BY 'TU_PASSWORD_FUERTE';
GRANT SELECT ON masvital_db.* TO 'api_read'@'localhost';
FLUSH PRIVILEGES;
```

Verificá:

```sql
-- Como api_read, esto debe funcionar
SELECT COUNT(*) FROM productos;
-- Como api_read, esto debe fallar
INSERT INTO productos (cod) VALUES ('TEST');   -- ERROR 1142 expected
```

Actualizá `.env` con `MYSQL_USER=api_read` y `MYSQL_PASSWORD=TU_PASSWORD_FUERTE`.

---

## 6 · Documentar el esquema MySQL MasVital

> **Tarea crítica.** El pipeline genérico asume tablas estilo `sgHermes`. Si MasVital usa otro POS, las tablas serán distintas y Dev Back necesita saber para adaptar el mapeo bronze → silver.

Ejecutá:

```powershell
python pipeline/explore_mysql_schema.py > docs/mysql-schema-snapshot.md
git add docs/mysql-schema-snapshot.md
git commit -m "docs(dev-w): snapshot esquema MySQL MasVital para Dev Back"
git push origin main
```

Esto le da a Dev Back el insumo exacto para hacer M3.4 (adaptación del mapeo).

Si falta `explore_mysql_schema.py`, escribilo siguiendo el patrón documentado en `pipeline/README.md` (lista tablas, columnas, sample de 3 filas por tabla).

---

## 7 · Probar pipeline manual (primera corrida)

```powershell
# Activar venv si no está activo
.\.venv\Scripts\Activate.ps1

# Cargar variables
. .\infra\load_env.ps1   # creado por Dev Back en M3.5

# Correr pipeline VERBOSE
python pipeline\run_all.py
```

Esperá ~2-4 minutos. Salida esperada al final:

```
INFO Silver: 7/7 transformations complete
INFO Gold: 10/10 transformations complete   (o menos si MasVital arranca con subset)
INFO DuckDB written to .\masvital_gold.duckdb (XX MB)
```

Si hay error: capturá el log COMPLETO, abrí un issue en `masvitalData` y mencioná a Dev Back. NO sigas.

---

## 8 · Subir primer DuckDB a R2

```powershell
python scripts\upload_duckdb_to_r2.py
```

Salida esperada:

```
Uploading masvital_gold.duckdb to motoshop-gold/masvital_gold.duckdb
Upload successful (XX MB)
```

Verificá en el dashboard de Cloudflare R2 que el objeto `masvital_gold.duckdb` aparece en el bucket `motoshop-gold`.

---

## 9 · Validar en la PWA prod

1. Abrí `https://app.fragloesja.uk` en el navegador
2. Login con `admin` / `FG28`
3. En `/select-tenant` escogé MasVital
4. Home debe mostrar KPIs (aunque sean chicos — el negocio recién abrió)
5. `/products` debe listar el catálogo
6. `/dashboards/ventas` debe mostrar la curva de los días que hay

Si la PWA dice "Sin datos" en TODO: el DuckDB subió pero el backend no se enteró. Esperá 1 min (cold-start de Render) o disparar manual:

```powershell
# Endpoint admin que fuerza re-bootstrap del DuckDB
curl -X POST https://api.fragloesja.uk/api/admin/data/refresh `
  -H "Authorization: Bearer <TOKEN>" `
  -H "X-Tenant: masvital"
```

Si seguís sin ver datos: log al issue. NO sigas.

---

## 10 · Configurar Task Scheduler — Refresh cada 30 min

1. Abrí `Task Scheduler` (Programador de tareas)
2. Click "Create Task" (Crear tarea, NO "Crear tarea básica")
3. Pestaña **General**:
   - Name: `MasVitalRefresh`
   - "Run whether user is logged on or not"
   - "Run with highest privileges"
4. Pestaña **Triggers**: New → Daily
   - Start: hoy 07:00 hora Cali
   - Repeat task every: 30 minutes
   - For a duration of: 12 hours 30 minutes (07:00 → 19:30)
   - Enabled
5. Pestaña **Actions**: New
   - Program: `powershell.exe`
   - Arguments: `-ExecutionPolicy Bypass -File "C:\Users\MasVital\Documents\masvitalData\infra\refresh.ps1"`
   - Start in: `C:\Users\MasVital\Documents\masvitalData`
6. Pestaña **Conditions**: desmarcá "Start the task only if the computer is on AC power"
7. Pestaña **Settings**:
   - "Allow task to be run on demand"
   - "If the task fails, restart every": 5 minutes, up to 3 times
8. OK + ingresá credenciales del usuario Windows

Probá manual: click derecho sobre la tarea → Run. Mirá `infra\logs\refresh_YYYYMMDD.log`.

---

## 11 · Configurar Task Scheduler — Auto-Pull cada 5 min

Repetí el patrón pero con:

- Name: `MasVitalAutoPull`
- Triggers: Daily start 06:00, repeat every 5 minutes, duration 14 hours
- Action: `powershell.exe -ExecutionPolicy Bypass -File "C:\Users\MasVital\Documents\masvitalData\infra\auto_pull_and_apply.ps1"`

Validá tirando un commit dummy a `main` desde otro lado y viendo en `infra\logs\auto_pull.log` que el PC lo aplicó dentro de 5 min.

---

## 12 · Configurar backup diario MySQL

- Name: `MasVitalBackupMySQL`
- Trigger: Daily 02:00
- Action: `powershell.exe -ExecutionPolicy Bypass -File "C:\Users\MasVital\Documents\masvitalData\infra\backup_mysql.ps1"`
- Los backups van a una carpeta `C:\Backups\MasVital\` (gitignored, fuera del repo)

---

## 13 · Validación final — 24 horas de observación

Antes de dar el sprint por cerrado:

- [ ] 24 horas con runs cada 30 min sin fallar (mirar `infra\logs\refresh_*.log`)
- [ ] Auto-pull aplicado al menos un commit nuevo correctamente
- [ ] Backup MySQL del día anterior existe en `C:\Backups\MasVital\`
- [ ] PWA muestra datos frescos del día (badge "Actualizado hace X min" < 35 min)
- [ ] Cero entradas en R2 distintas a `motoshop_gold.duckdb` y `masvital_gold.duckdb`

Cuando los 5 estén ✅, actualizá `SEGUIMIENTO.md` y avisás al PO.

---

## 14 · Cómo pedir ayuda

| Problema | Acción |
|---|---|
| Pipeline rompe con SQL error | Issue con log COMPLETO y comando exacto que disparó |
| Esquema MySQL incompatible | Issue con tablas que faltan o columnas con nombre distinto |
| R2 upload falla | Verificar `.env` R2_* + intentar `aws s3 ls --endpoint-url $R2_ENDPOINT s3://motoshop-gold/` |
| PWA no ve datos | Verificar que `masvital_gold.duckdb` está en R2 + esperar 1 min Render cold-start |
| Task Scheduler no dispara | Verificar "Run whether user is logged on or not" + credenciales correctas |

**Regla de oro:** ante duda, NO inventes. Issue + ping al PO.

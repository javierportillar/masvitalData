# MySQL Schema Snapshot -- masvital

Generado: 2026-06-14 13:19:42
Host: localhost
Tablas encontradas: 179

---

## `ajustes` (0 filas)

| Campo | Tipo | Nulo | Key | Default | Extra |
|-------|------|------|-----|---------|-------|
| numaju | varchar(20) | NO | MUL |  |  |
| nomdoc | varchar(100) | NO |  | COMPROBANTE DE EGRESO |  |
| preaju | varchar(8) | NO |  | CE |  |
| fecaju | datetime | NO |  | 2000-01-20 00:00:00 |  |
| totdeb | double | NO |  | 0 |  |
| totcre | double | NO |  | 0 |  |
| obsaju | varchar(400) | NO |  |  |  |
| estaju | char(1) | NO |  |  |  |
| codemp | varchar(15) | NO | MUL |  |  |
| horaju | tinyint(3) | NO |  | 1 |  |
| codres | varchar(4) | NO | MUL |  |  |
| codclas | varchar(4) | NO | MUL |  |  |
| empcod | varchar(3) | NO | MUL |  |  |
| docext | varchar(20) | NO |  |  |  |
| numcru | varchar(20) | NO | MUL |  |  |
| clascru | varchar(4) | NO | MUL |  |  |
| nitter | varchar(15) | NO | MUL |  |  |
| codsuc | varchar(15) | NO | MUL |  |  |
| veridoc | tinyint(1) | NO |  | 0 |  |
| feccrea | datetime | NO |  | 2000-01-20 00:00:00 |  |

**Muestras (3 filas):**

```json
[]
```

---

## `archadjunto` (0 filas)

| Campo | Tipo | Nulo | Key | Default | Extra |
|-------|------|------|-----|---------|-------|
| numnum | varchar(20) | NO | MUL |  |  |
| codclas | varchar(4) | NO | MUL |  |  |
| tipdoc | char(1) | NO |  | 1 |  |
| numite | smallint(6) | NO | MUL | 1 |  |
| tiparch | varchar(6) | NO |  |  |  |
| urlarch | varchar(250) | NO |  |  |  |
| obsarch | varchar(250) | NO |  |  |  |
| tipclas | char(1) | NO |  | 0 |  |

**Muestras (3 filas):**

```json
[]
```

---

## `auxcompven` (0 filas)

| Campo | Tipo | Nulo | Key | Default | Extra |
|-------|------|------|-----|---------|-------|
| numdoc | varchar(20) | NO | MUL |  |  |
| codclas | varchar(4) | NO | MUL |  |  |
| nomdoc | varchar(100) | NO |  |  |  |
| predoc | varchar(8) | NO |  |  |  |
| fecdoc | datetime | NO |  | 2000-01-20 00:00:00 |  |
| nitter | varchar(15) | NO | MUL |  |  |
| digter | char(2) | NO |  |  |  |
| nomter | varchar(120) | NO |  |  |  |
| totcon | double | NO |  | 0 |  |
| totcre | double | NO |  | 0 |  |

**Muestras (3 filas):**

```json
[]
```

---

## `auxdetcompven` (0 filas)

| Campo | Tipo | Nulo | Key | Default | Extra |
|-------|------|------|-----|---------|-------|
| numdoc | varchar(20) | NO | MUL |  |  |
| codclas | varchar(4) | NO | MUL |  |  |
| valbas | double | NO |  | 0 |  |
| ivapor | float | NO |  | 0 |  |
| valiva | double | NO |  | 0 |  |
| ipopor | float | NO |  | 0 |  |
| valipo | double | NO |  | 0 |  |
| valexe | double | NO |  | 0 |  |
| auxnom1 | varchar(150) | NO |  |  |  |

**Muestras (3 filas):**

```json
[]
```

---

## `auxdetcue` (2 filas)

| Campo | Tipo | Nulo | Key | Default | Extra |
|-------|------|------|-----|---------|-------|
| numnum | varchar(20) | NO | MUL |  |  |
| prenum | varchar(8) | NO |  |  |  |
| codcue | varchar(35) | NO | MUL |  |  |
| detcue | varchar(300) | NO |  |  |  |
| valdeb | double | NO |  | 0 |  |
| valhab | double | NO |  | 0 |  |
| fecdoc | datetime | NO |  | 2000-01-20 00:00:00 |  |
| codcos | varchar(6) | NO | MUL |  |  |
| nitter | varchar(15) | NO | MUL |  |  |
| nomcom | varchar(150) | NO |  |  |  |
| estcue | char(1) | NO |  | B |  |
| codprod | varchar(20) | NO |  |  |  |
| candet | double | NO |  | 0 |  |
| sernum | varchar(40) | NO |  |  |  |
| codbod | varchar(4) | NO |  |  |  |
| codclas | varchar(4) | NO | MUL |  |  |
| numite | smallint(6) | NO |  | 1 |  |
| valdet | double | NO |  | 0 |  |
| docafe | varchar(20) | NO |  |  |  |
| preafe | varchar(4) | NO |  |  |  |
| clasafe | varchar(4) | NO |  |  |  |
| obsrev | varchar(400) | NO |  |  |  |
| tipo | char(1) | NO |  | C |  |

**Muestras (3 filas):**

```json
[
  {
    "numnum": "2",
    "prenum": "CE",
    "codcue": "519525",
    "detcue": "Elementos de aseo y cafeter├¡a",
    "valdeb": "52400.0",
    "valhab": "0.0",
    "fecdoc": "2000-01-20 00:00:00",
    "codcos": "",
    "nitter": "100",
    "nomcom": "",
    "estcue": "B",
    "codprod": "",
    "candet": "0.0",
    "sernum": "",
    "codbod": "",
    "codclas": "S02",
    "numite": "1",
    "valdet": "52400.0",
    "docafe": "",
    "preafe": "",
    "clasafe": "",
    "obsrev": "",
    "tipo": "2"
  },
  {
    "numnum": "2",
    "prenum": "CE",
    "codcue": "11050501",
    "detcue": "COMPRA UTENCILIOS DE CAFETERIA",
    "valdeb": "0.0",
    "valhab": "52400.0",
    "fecdoc": "2000-01-20 00:00:00",
    "codcos": "",
    "nitter": "100",
    "nomcom": "",
    "estcue": "B",
    "codprod": "",
    "candet": "0.0",
    "sernum": "",
    "codbod": "",
    "codclas": "S02",
    "numite": "2",
    "valdet": "52400.0",
    "docafe": "",
    "preafe": "",
    "clasafe": "",
    "obsrev": "",
    "tipo": "2"
  }
]
```

---

## `auxdetdoc` (6 filas)

| Campo | Tipo | Nulo | Key | Default | Extra |
|-------|------|------|-----|---------|-------|
| numcom | varchar(20) | NO | MUL |  |  |
| codprod | varchar(20) | NO |  |  |  |
| sernum | varchar(40) | NO |  |  |  |
| nomdet | varchar(300) | NO |  |  |  |
| presdet | varchar(100) | NO |  |  |  |
| valuni | double | NO |  | 0 |  |
| candet | double | NO |  | 0 |  |
| dctpor | float | NO |  | 0 |  |
| dctpes | double | NO |  | 0 |  |
| ivapor | float | NO |  | 0 |  |
| ivapes | double | NO |  | 0 |  |
| totdet | double | NO |  | 0 |  |
| obsdet | varchar(400) | NO |  |  |  |
| cosprod | double | NO |  | 0 |  |
| clase | varchar(4) | NO |  |  |  |
| tipdet | char(2) | NO |  | P |  |
| codcue | varchar(12) | NO |  |  |  |
| devcam | char(2) | NO |  | NO |  |
| codbod | varchar(4) | NO |  |  |  |
| numite | smallint(6) | NO |  | 1 |  |
| codclas | varchar(4) | NO | MUL |  |  |
| ipopor | float | NO |  | 0 |  |
| ipopes | double | NO |  | 0 |  |
| fecdet1 | datetime | NO |  | 2000-01-01 00:00:00 |  |
| codpor | varchar(4) | NO |  |  |  |
| codpor2 | varchar(4) | NO |  |  |  |
| codbar | varchar(40) | NO |  |  |  |
| pesodet | double | NO |  | 0 |  |
| tipipo | varchar(2) | NO |  |  |  |

**Muestras (3 filas):**

```json
[
  {
    "numcom": "47",
    "codprod": "SUBL009",
    "sernum": "",
    "nomdet": "SALSA TOMATE 200GR",
    "presdet": "UNIDAD",
    "valuni": "15000.0",
    "candet": "2.0",
    "dctpor": "0.0",
    "dctpes": "0.0",
    "ivapor": "0.0",
    "ivapes": "0.0",
    "totdet": "1.0",
    "obsdet": "",
    "cosprod": "15000.0",
    "clase": "",
    "tipdet": "P",
    "codcue": "",
    "devcam": "NO",
    "codbod": "",
    "numite": "1",
    "codclas": "S18",
    "ipopor": "0.0",
    "ipopes": "0.0",
    "fecdet1": "2000-01-01 00:00:00",
    "codpor": "IV2",
    "codpor2": " ",
    "codbar": "SUBL009",
    "pesodet": "0.0",
    "tipipo": ""
  },
  {
    "numcom": "47",
    "codprod": "SUBL010",
    "sernum": "",
    "nomdet": "PESTO 200GR",
    "presdet": "UNIDAD",
    "valuni": "16000.0",
    "candet": "2.0",
    "dctpor": "0.0",
    "dctpes": "0.0",
    "ivapor": "0.0",
    "ivapes": "0.0",
    "totdet": "1.0",
    "obsdet": "",
    "cosprod": "16000.0",
    "clase": "",
    "tipdet": "P",
    "codcue": "",
    "devcam": "NO",
    "codbod": "",
    "numite": "2",
    "codclas": "S18",
    "ipopor": "0.0",
    "ipopes": "0.0",
    "fecdet1": "2000-01-01 00:00:00",
    "codpor": "IV2",
    "codpor2": " ",
    "codbar": "SUBL010",
    "pesodet": "0.0",
    "tipipo": ""
  },
  {
    "numcom": "47",
    "codprod": "SUBL011",
    "sernum": "",
    "nomdet": "SAZONADOR 200GR",
    "presdet": "UNIDAD",
    "valuni": "15000.0",
    "candet": "2.0",
    "dctpor": "0.0",
    "dctpes": "0.0",
    "ivapor": "0.0",
    "ivapes": "0.0",
    "totdet": "1.0",
    "obsdet": "",
    "cosprod": "15000.0",
    "clase": "",
    "tipdet": "P",
    "codcue": "",
    "devcam": "NO",
    "codbod": "",
    "numite": "3",
    "codclas": "S18",
    "ipopor": "0.0",
    "ipopes": "0.0",
    "fecdet1": "2000-01-01 00:00:00",
    "codpor": "IV2",
    "codpor2": " ",
    "codbar": "SUBL011",
    "pesodet": "0.0",
    "tipipo": ""
  }
]
```

---

## `auxdetforpag` (0 filas)

| Campo | Tipo | Nulo | Key | Default | Extra |
|-------|------|------|-----|---------|-------|
| numnum | varchar(20) | NO | MUL |  |  |
| predoc | varchar(8) | NO |  |  |  |
| nomdoc | varchar(100) | NO |  |  |  |
| numcuo | smallint(6) | NO |  | 0 |  |
| fecdoc | datetime | NO |  | 2000-01-20 00:00:00 |  |
| nitter | varchar(15) | NO |  |  |  |
| nomter | varchar(120) | NO |  |  |  |
| valpag | double | NO |  | 0 |  |
| salant | double | NO |  | 0 |  |
| sanafe | double | NO |  | 0 |  |
| sanban | double | NO |  | 0 |  |
| sancaj | double | NO |  | 0 |  |
| santip | double | NO |  | 0 |  |
| debito | double | NO |  | 0 |  |
| credito | double | NO |  | 0 |  |
| valfondo | double | NO |  | 0 |  |
| entosal | char(1) | NO |  |  |  |
| clase | varchar(4) | NO |  |  |  |
| codpag | varchar(4) | NO | MUL |  |  |
| despag | varchar(100) | NO |  |  |  |
| afepag | tinyint(3) | NO | MUL | 0 |  |
| tippag | tinyint(3) | NO | MUL | 0 |  |
| codcaj | varchar(4) | NO | MUL |  |  |
| codban | varchar(8) | NO | MUL |  |  |
| cajoban | varchar(100) | NO |  |  |  |
| banotar | varchar(100) | NO |  |  |  |
| numpag | varchar(20) | NO |  |  |  |
| numapr | varchar(20) | NO |  |  |  |
| fecche | date | NO |  | 2000-01-20 |  |
| codcue | varchar(12) | NO |  |  |  |
| foncaj | char(1) | NO |  |  |  |
| codclas | varchar(4) | NO |  |  |  |

**Muestras (3 filas):**

```json
[]
```

---

## `auxdetrep` (0 filas)

| Campo | Tipo | Nulo | Key | Default | Extra |
|-------|------|------|-----|---------|-------|
| numord | int(9) | NO |  | 0 |  |
| Codigo | int(11) | NO | MUL | 0 |  |
| codigo2 | varchar(20) | NO |  |  |  |
| fecha1 | datetime | NO |  | 2000-01-20 00:00:00 |  |
| det1 | varchar(250) | NO |  |  |  |
| cant1 | double | NO |  | 0 |  |
| cant2 | double | NO |  | 0 |  |
| cant3 | double | NO |  | 0 |  |
| valor1 | double | NO |  | 0 |  |
| valor2 | double | NO |  | 0 |  |
| valor3 | double | NO |  | 0 |  |
| valor4 | double | NO |  | 0 |  |
| obsdet | varchar(250) | NO |  |  |  |

**Muestras (3 filas):**

```json
[]
```

---

## `auxdoc` (1 filas)

| Campo | Tipo | Nulo | Key | Default | Extra |
|-------|------|------|-----|---------|-------|
| numcom | varchar(20) | NO | MUL |  |  |
| nomdoc | varchar(100) | NO |  | COMPRA |  |
| precom | varchar(8) | NO |  | COM |  |
| feccom | datetime | NO |  | 2000-01-20 00:00:00 |  |
| faccom | varchar(20) | NO |  |  |  |
| nitter | varchar(15) | NO | MUL |  |  |
| digcom | char(2) | NO |  |  |  |
| procom | varchar(240) | NO |  |  |  |
| dircom | varchar(100) | NO |  |  |  |
| telcom | varchar(50) | NO |  |  |  |
| ciucom | varchar(100) | NO |  |  |  |
| tipcom | varchar(10) | NO |  |  |  |
| diascot | int(11) | NO |  | 0 |  |
| subcom | double | NO |  | 0 |  |
| totdct | double | NO |  | 0 |  |
| totiva | double | NO |  | 0 |  |
| totipo | double | NO |  | 0 |  |
| retfte | double | NO |  | 0 |  |
| retiva | double | NO |  | 0 |  |
| retica | double | NO |  | 0 |  |
| retcre | double | NO |  | 0 |  |
| ajuspe | double | NO |  | 0 |  |
| totcom | double | NO |  | 0 |  |
| obscom | varchar(600) | NO |  |  |  |
| estcom | char(1) | NO |  |  |  |
| clase | varchar(4) | NO |  |  |  |
| codemp | varchar(15) | NO |  |  |  |
| horcom | tinyint(3) | NO |  | 1 |  |
| venfven | varchar(120) | NO |  |  |  |
| Visible | char(2) | NO |  | NO |  |
| nomusu | varchar(150) | NO |  |  |  |
| cencos | varchar(50) | NO |  |  |  |
| pedrem | varchar(150) | NO |  |  |  |
| numped | varchar(20) | NO |  |  |  |
| nomzon | varchar(100) | NO |  |  |  |
| retsino | char(2) | NO |  | NO |  |
| codclas | varchar(4) | NO | MUL |  |  |
| dirdos | varchar(100) | NO |  |  |  |
| teldos | varchar(50) | NO |  |  |  |
| texres | varchar(250) | NO |  |  |  |
| vletras | varchar(250) | NO |  |  |  |
| fpconta | double | NO |  | 0 |  |
| fpcredi | double | NO |  | 0 |  |
| fpcheqe | double | NO |  | 0 |  |
| fpotros | double | NO |  | 0 |  |
| perdes | date | NO |  | 2000-01-01 |  |
| perhas | date | NO |  | 2000-01-01 |  |
| codsuc | varchar(15) | NO |  |  |  |
| nomrut | varchar(100) | NO |  |  |  |
| nomest | varchar(50) | NO |  |  |  |
| nomuso | varchar(50) | NO |  |  |  |
| salant | double | NO |  | 0 |  |
| numdeu | smallint(3) | NO |  | 0 |  |
| lectant | int(11) | NO |  | 0 |  |
| lectact | int(11) | NO |  | 0 |  |
| consumo | int(11) | NO |  | 0 |  |
| tiplect | char(1) | NO |  |  |  |
| totreca | double | NO |  | 0 |  |
| forpag | varchar(250) | NO |  |  |  |
| corele | varchar(100) | NO |  |  |  |
| tarimp1 | varchar(30) | NO |  |  |  |
| basimp1 | double | NO |  | 0 |  |
| valimp1 | double | NO |  | 0 |  |
| tarimp2 | varchar(30) | NO |  |  |  |
| basimp2 | double | NO |  | 0 |  |
| valimp2 | double | NO |  | 0 |  |
| tarimp3 | varchar(30) | NO |  |  |  |
| basimp3 | double | NO |  | 0 |  |
| valimp3 | double | NO |  | 0 |  |
| tarimp4 | varchar(100) | NO |  |  |  |
| basimp4 | double | NO |  | 0 |  |
| valimp4 | double | NO |  | 0 |  |
| metralc | smallint(6) | NO |  | 0 |  |
| metrase | double | NO |  | 0 |  |
| metprom | smallint(6) | NO |  | 0 |  |
| numpred | varchar(30) | NO |  |  |  |
| intmora | double | NO |  | 0 |  |
| cocufe | varchar(150) | NO |  |  |  |
| protec | char(1) | NO |  |  |  |
| otrimp | double | NO |  | 0 |  |
| dctglob | double | NO |  | 0 |  |
| tazacam | double | NO |  | 0 |  |
| moneda | varchar(4) | NO |  |  |  |
| salnue | double | NO |  | 0 |  |

**Muestras (3 filas):**

```json
[
  {
    "numcom": "47",
    "nomdoc": "COMPRA",
    "precom": "COM",
    "feccom": "2026-06-12 19:14:51",
    "faccom": "002",
    "nitter": "1015448634",
    "digcom": "",
    "procom": "SUBLIME",
    "dircom": "CLL 18 B 42 A 04 PASTO",
    "telcom": "3165818758",
    "ciucom": "PASTO - NARI├æO",
    "tipcom": "F07",
    "diascot": "0",
    "subcom": "188000.0",
    "totdct": "0.0",
    "totiva": "0.0",
    "totipo": "0.0",
    "retfte": "0.0",
    "retiva": "0.0",
    "retica": "0.0",
    "retcre": "0.0",
    "ajuspe": "0.0",
    "totcom": "188000.0",
    "obscom": " ",
    "estcom": "B",
    "clase": "",
    "codemp": "1151970853",
    "horcom": "1",
    "venfven": "",
    "Visible": "SI",
    "nomusu": "MAS VITAL MARKET",
    "cencos": "",
    "pedrem": "",
    "numped": "",
    "nomzon": "",
    "retsino": "NO",
    "codclas": "S18",
    "dirdos": "",
    "teldos": "",
    "texres": "",
    "vletras": "Ciento ochenta y ocho mil Pesos M/cte",
    "fpconta": "0.0",
    "fpcredi": "0.0",
    "fpcheqe": "0.0",
    "fpotros": "0.0",
    "perdes": "2000-01-01",
    "perhas": "2000-01-01",
    "codsuc": "",
    "nomrut": "",
    "nomest": "",
    "nomuso": "",
    "salant": "0.0",
    "numdeu": "0",
    "lectant": "0",
    "lectact": "0",
    "consumo": "0",
    "tiplect": "",
    "totreca": "0.0",
    "forpag": "                                  Contado TRANSFERENCIA BANCO.... ",
    "corele": "ventassublime@gmail.com",
    "tarimp1": "IVA 0 %",
    "basimp1": "188000.0",
    "valimp1": "0.0",
    "tarimp2": "",
    "basimp2": "0.0",
    "valimp2": "0.0",
    "tarimp3": "",
    "basimp3": "0.0",
    "valimp3": "0.0",
    "tarimp4": "",
    "basimp4": "0.0",
    "valimp4": "0.0",
    "metralc": "0",
    "metrase": "0.0",
    "metprom": "0",
    "numpred": "",
    "intmora": "0.0",
    "cocufe": "",
    "protec": "",
    "otrimp": "0.0",
    "dctglob": "0.0",
    "tazacam": "0.0",
    "moneda": "",
    "salnue": "0.0"
  }
]
```

---

## `auxfiscal1` (2 filas)

| Campo | Tipo | Nulo | Key | Default | Extra |
|-------|------|------|-----|---------|-------|
| tipinf | char(2) | NO | MUL |  |  |
| codclas | varchar(6) | NO |  |  |  |
| detalle | varchar(250) | NO |  |  |  |
| subtot | double | NO |  | 0 |  |
| valimp | double | NO |  | 0 |  |
| porimp | float | NO |  | 0 |  |
| valreca | double | NO |  | 0 |  |
| dctglob | double | NO |  | 0 |  |
| valrete | double | NO |  | 0 |  |
| tipdet | varchar(20) | NO |  |  |  |
| candet | double | NO |  | 0 |  |
| fecdoc | date | NO |  | 2000-01-01 |  |
| numreso | varchar(20) | NO |  |  |  |
| predoc | varchar(8) | NO |  |  |  |
| numdoc | varchar(20) | NO |  |  |  |
| docanu | smallint(6) | NO |  | 0 |  |
| numtran | int(10) | NO |  | 0 |  |
| numutil | varchar(50) | NO |  |  |  |
| nitter | varchar(15) | NO |  |  |  |
| nomter | varchar(150) | NO |  |  |  |
| fecres | date | NO |  | 2000-01-01 |  |
| freshas | date | NO |  | 2000-01-01 |  |
| numini | bigint(20) | NO |  | 0 |  |
| numfin | bigint(20) | NO |  | 0 |  |
| tippag | tinyint(3) | NO |  | 0 |  |

**Muestras (3 filas):**

```json
[
  {
    "tipinf": "6",
    "codclas": "S15",
    "detalle": "F. VENTA",
    "subtot": "36300.0",
    "valimp": "0.0",
    "porimp": "0.0",
    "valreca": "0.0",
    "dctglob": "0.0",
    "valrete": "0.0",
    "tipdet": "VENTA",
    "candet": "0.0",
    "fecdoc": "2026-06-14",
    "numreso": "",
    "predoc": "FVP",
    "numdoc": " ",
    "docanu": "0",
    "numtran": "3",
    "numutil": "86 - 88",
    "nitter": "",
    "nomter": " ",
    "fecres": "2000-01-01",
    "freshas": "2000-01-01",
    "numini": "0",
    "numfin": "0",
    "tippag": "0"
  },
  {
    "tipinf": "15",
    "codclas": "",
    "detalle": "Efectivo",
    "subtot": "36300.0",
    "valimp": "0.0",
    "porimp": "0.0",
    "valreca": "0.0",
    "dctglob": "0.0",
    "valrete": "0.0",
    "tipdet": "VENTA",
    "candet": "0.0",
    "fecdoc": "2026-06-14",
    "numreso": "",
    "predoc": " ",
    "numdoc": " ",
    "docanu": "0",
    "numtran": "3",
    "numutil": " ",
    "nitter": "",
    "nomter": " ",
    "fecres": "2000-01-01",
    "freshas": "2000-01-01",
    "numini": "0",
    "numfin": "0",
    "tippag": "1"
  }
]
```

---

## `auxinventario` (379 filas)

| Campo | Tipo | Nulo | Key | Default | Extra |
|-------|------|------|-----|---------|-------|
| codlis | char(3) | NO | MUL |  |  |
| nomlis | varchar(100) | NO |  |  |  |
| codlin1 | varchar(4) | NO |  |  |  |
| nomlin | varchar(100) | NO |  |  |  |
| codlin2 | varchar(4) | NO |  |  |  |
| nomlin2 | varchar(100) | NO |  |  |  |
| codlin3 | varchar(4) | NO |  |  |  |
| nomlin3 | varchar(100) | NO |  |  |  |
| codlin4 | varchar(4) | NO |  |  |  |
| nomlin4 | varchar(100) | NO |  |  |  |
| codlin5 | varchar(4) | NO |  |  |  |
| nomlin5 | varchar(100) | NO |  |  |  |
| codlin6 | varchar(4) | NO |  |  |  |
| nomlin6 | varchar(100) | NO |  |  |  |
| codbod | varchar(4) | NO |  |  |  |
| nombod | varchar(100) | NO |  |  |  |
| nitter | varchar(15) | NO |  |  |  |
| nomter | varchar(120) | NO |  |  |  |
| numdoc | varchar(20) | NO |  |  |  |
| nomdoc | varchar(100) | NO |  |  |  |
| codprod | varchar(20) | NO | MUL |  |  |
| sernum | varchar(40) | NO |  |  |  |
| nomprod | varchar(250) | NO |  |  |  |
| unimed | varchar(150) | NO |  |  |  |
| valor1 | double | NO |  | 0 |  |
| valor2 | double | NO |  | 0 |  |
| valor3 | double | NO |  | 0 |  |
| valor4 | double | NO |  | 0 |  |
| valor5 | double | NO |  | 0 |  |
| docfec | datetime | NO |  | 2000-01-20 00:00:00 |  |
| docnum | varchar(30) | NO |  |  |  |
| nomsub | varchar(30) | NO |  |  |  |
| multiplo | double | NO |  | 1 |  |
| codcos | varchar(6) | NO | MUL |  |  |
| nomcos | varchar(100) | NO |  |  |  |

**Muestras (3 filas):**

```json
[
  {
    "codlis": "",
    "nomlis": "",
    "codlin1": "",
    "nomlin": "",
    "codlin2": "",
    "nomlin2": "",
    "codlin3": "",
    "nomlin3": "",
    "codlin4": "",
    "nomlin4": "",
    "codlin5": "",
    "nomlin5": "",
    "codlin6": "",
    "nomlin6": "",
    "codbod": "",
    "nombod": "",
    "nitter": "",
    "nomter": "",
    "numdoc": "",
    "nomdoc": "1204",
    "codprod": "1204",
    "sernum": "N",
    "nomprod": "CM Natural 360g",
    "unimed": "",
    "valor1": "2.0",
    "valor2": "19501.0",
    "valor3": "24400.0",
    "valor4": "0.0",
    "valor5": "0.0",
    "docfec": "2000-01-20 00:00:00",
    "docnum": "",
    "nomsub": "",
    "multiplo": "1.0",
    "codcos": "",
    "nomcos": ""
  },
  {
    "codlis": "",
    "nomlis": "",
    "codlin1": "",
    "nomlin": "",
    "codlin2": "",
    "nomlin2": "",
    "codlin3": "",
    "nomlin3": "",
    "codlin4": "",
    "nomlin4": "",
    "codlin5": "",
    "nomlin5": "",
    "codlin6": "",
    "nomlin6": "",
    "codbod": "",
    "nombod": "",
    "nitter": "",
    "nomter": "",
    "numdoc": "",
    "nomdoc": "1205",
    "codprod": "1205",
    "sernum": "N",
    "nomprod": "CM Crunchy 360g",
    "unimed": "",
    "valor1": "2.0",
    "valor2": "19501.0",
    "valor3": "24400.0",
    "valor4": "0.0",
    "valor5": "0.0",
    "docfec": "2000-01-20 00:00:00",
    "docnum": "",
    "nomsub": "",
    "multiplo": "1.0",
    "codcos": "",
    "nomcos": ""
  },
  {
    "codlis": "",
    "nomlis": "",
    "codlin1": "",
    "nomlin": "",
    "codlin2": "",
    "nomlin2": "",
    "codlin3": "",
    "nomlin3": "",
    "codlin4": "",
    "nomlin4": "",
    "codlin5": "",
    "nomlin5": "",
    "codlin6": "",
    "nomlin6": "",
    "codbod": "",
    "nombod": "",
    "nitter": "",
    "nomter": "",
    "numdoc": "",
    "nomdoc": "1208",
    "codprod": "1208",
    "sernum": "N",
    "nomprod": "CM Con Chocolate 360g",
    "unimed": "",
    "valor1": "2.0",
    "valor2": "19501.0",
    "valor3": "24400.0",
    "valor4": "0.0",
    "valor5": "0.0",
    "docfec": "2000-01-20 00:00:00",
    "docnum": "",
    "nomsub": "",
    "multiplo": "1.0",
    "codcos": "",
    "nomcos": ""
  }
]
```

---

## `auxinvserial` (0 filas)

| Campo | Tipo | Nulo | Key | Default | Extra |
|-------|------|------|-----|---------|-------|
| codprod | varchar(20) | NO | MUL |  |  |
| sernum | varchar(250) | NO | MUL |  |  |
| candet | double | NO |  | 0 |  |
| canbod | double | NO |  | 0 |  |
| codbod | varchar(4) | NO |  |  |  |
| serfec | varchar(10) | NO |  |  |  |
| cosuni | double | NO |  | 0 |  |

**Muestras (3 filas):**

```json
[]
```

---

## `auxkardex` (0 filas)

| Campo | Tipo | Nulo | Key | Default | Extra |
|-------|------|------|-----|---------|-------|
| feckar | datetime | NO |  | 2000-01-20 00:00:00 |  |
| horkar | tinyint(3) | NO |  | 0 |  |
| entsal | tinyint(3) | NO |  | 0 |  |
| detkar | varchar(80) | NO |  |  |  |
| cankar | double | NO |  | 0 |  |
| coskar | double | NO |  | 0 |  |
| tipkar | char(1) | NO |  | 1 |  |
| clase | varchar(15) | NO |  |  |  |
| numdoc | varchar(20) | NO |  |  |  |
| reclase | varchar(15) | NO |  |  |  |
| renumdoc | varchar(20) | NO |  |  |  |
| codemp | varchar(15) | NO |  |  |  |
| codclas | varchar(4) | NO |  |  |  |
| codprod | varchar(20) | NO |  |  |  |
| codbod | varchar(4) | NO |  |  |  |
| codcos | varchar(6) | NO |  |  |  |

**Muestras (3 filas):**

```json
[]
```

---

## `auxmetafac` (0 filas)

| Campo | Tipo | Nulo | Key | Default | Extra |
|-------|------|------|-----|---------|-------|
| nitter | varchar(15) | NO | MUL |  |  |
| codprod | varchar(20) | NO | MUL |  |  |
| metven | double | NO |  | 0 |  |
| utiven | double | NO |  | 0 |  |
| cumpven | double | NO |  | 0 |  |
| canven | double | NO |  | 0 |  |
| metpun | double | NO |  | 0 |  |
| punacu | double | NO |  | 0 |  |
| cumppro | double | NO |  | 0 |  |
| nomdet | varchar(120) | NO |  |  |  |
| nitase | varchar(15) | NO | MUL |  |  |
| nomase | varchar(100) | NO |  |  |  |
| codcos | varchar(6) | NO | MUL |  |  |
| nomcos | varchar(50) | NO |  |  |  |

**Muestras (3 filas):**

```json
[]
```

---

## `auxpresupeje` (0 filas)

| Campo | Tipo | Nulo | Key | Default | Extra |
|-------|------|------|-----|---------|-------|
| codrub | varchar(35) | NO | MUL |  |  |
| nomdet | varchar(250) | NO |  |  |  |
| valdet | double | NO |  | 0 |  |
| codcos | varchar(6) | NO | MUL |  |  |
| valeje | double | NO |  | 0 |  |
| debcre | double | NO |  | 0 |  |
| valcdp | double | NO |  | 0 |  |
| valcrp | double | NO |  | 0 |  |
| vadici | double | NO |  | 0 |  |
| vreduc | double | NO |  | 0 |  |
| vcredi | double | NO |  | 0 |  |
| vcontr | double | NO |  | 0 |  |
| vaplaza | double | NO |  | 0 |  |
| vdespla | double | NO |  | 0 |  |
| totdisp | double | NO |  | 0 |  |
| afedisp | double | NO |  | 0 |  |
| totcom | double | NO |  | 0 |  |
| afecom | double | NO |  | 0 |  |
| totobli | double | NO |  | 0 |  |
| afeobli | double | NO |  | 0 |  |
| nomniv1 | varchar(250) | NO |  |  |  |
| nomniv2 | varchar(250) | NO |  |  |  |
| nomniv3 | varchar(250) | NO |  |  |  |
| nomniv4 | varchar(250) | NO |  |  |  |
| nomniv5 | varchar(250) | NO |  |  |  |
| nomniv6 | varchar(250) | NO |  |  |  |
| nomniv7 | varchar(250) | NO |  |  |  |
| nomniv8 | varchar(250) | NO |  |  |  |
| nomniv9 | varchar(250) | NO |  |  |  |
| nomni10 | varchar(250) | NO |  |  |  |

**Muestras (3 filas):**

```json
[]
```

---

## `auxrep` (0 filas)

| Campo | Tipo | Nulo | Key | Default | Extra |
|-------|------|------|-----|---------|-------|
| Codigo | int(11) | NO | PRI | 0 |  |
| codigo2 | varchar(20) | NO |  |  |  |
| fecha1 | datetime | NO |  | 2000-01-20 00:00:00 |  |
| fecha2 | datetime | NO |  | 2000-01-20 00:00:00 |  |
| det1 | varchar(80) | NO |  |  |  |
| det2 | varchar(200) | NO |  |  |  |
| det3 | varchar(80) | NO |  |  |  |
| cant1 | double | NO |  | 0 |  |
| cant2 | double | NO |  | 0 |  |
| cant3 | double | NO |  | 0 |  |
| valor1 | double | NO |  | 0 |  |
| valor2 | double | NO |  | 0 |  |
| valor3 | double | NO |  | 0 |  |
| codemp | varchar(15) | NO | MUL |  |  |

**Muestras (3 filas):**

```json
[]
```

---

## `auxrepcart` (0 filas)

| Campo | Tipo | Nulo | Key | Default | Extra |
|-------|------|------|-----|---------|-------|
| nitter | varchar(15) | NO | MUL |  |  |
| numdoc | varchar(20) | NO | MUL |  |  |
| predoc | varchar(20) | NO |  |  |  |
| numcuo | smallint(6) | NO |  | 0 |  |
| fecha | datetime | NO |  | 2000-01-20 00:00:00 |  |
| hordoc | tinyint(3) | NO |  | 0 |  |
| fecven | datetime | NO |  | 2000-01-20 00:00:00 |  |
| diasven | int(11) | NO |  | 0 |  |
| valor | double | NO |  | 0 |  |
| saldo | double | NO |  | 0 |  |
| sinven | double | NO |  | 0 |  |
| sal30 | double | NO |  | 0 |  |
| sal60 | double | NO |  | 0 |  |
| sal90 | double | NO |  | 0 |  |
| sal120 | double | NO |  | 0 |  |
| salsup120 | double | NO |  | 0 |  |
| tipo | tinyint(3) | NO |  | 0 |  |
| codclas | varchar(4) | NO | MUL |  |  |
| codcue | varchar(12) | NO | MUL |  |  |
| dias2 | tinyint(6) | NO |  | 0 |  |
| codcos | varchar(6) | NO | MUL |  |  |
| nomcos | varchar(50) | NO |  |  |  |
| nitvend | varchar(15) | NO |  |  |  |
| codsuc | varchar(15) | NO |  |  |  |
| nomsuc | varchar(120) | NO |  |  |  |
| dirsuc | varchar(100) | NO |  |  |  |
| docext | varchar(20) | NO |  |  |  |
| nomven | varchar(120) | NO |  |  |  |
| orden | int(11) | NO |  | 0 |  |

**Muestras (3 filas):**

```json
[]
```

---

## `auxrepconta` (2 filas)

| Campo | Tipo | Nulo | Key | Default | Extra |
|-------|------|------|-----|---------|-------|
| codcue | varchar(35) | NO | MUL |  |  |
| detcue | varchar(250) | NO |  |  |  |
| salant | double | NO |  | 0 |  |
| valdeb | double | NO |  | 0 |  |
| valhab | double | NO |  | 0 |  |
| nuesal | double | NO |  | 0 |  |
| nomcla | varchar(150) | NO |  |  |  |
| nomgru | varchar(150) | NO |  |  |  |
| nomcue | varchar(250) | NO |  |  |  |
| nomsub | varchar(150) | NO |  |  |  |
| nomaux | varchar(150) | NO |  |  |  |
| nitter | varchar(15) | NO | MUL |  |  |
| nomter | varchar(150) | NO |  |  |  |
| numnum | varchar(20) | NO | MUL |  |  |
| fecdoc | datetime | NO |  | 2000-01-20 00:00:00 |  |
| codprod | varchar(20) | NO |  |  |  |
| codclas | varchar(4) | NO |  |  |  |
| codcos | varchar(6) | NO |  |  |  |
| docext | varchar(20) | NO |  |  |  |
| detaux | varchar(150) | NO |  |  |  |
| nitnomi | varchar(15) | NO |  |  |  |
| nomnomi | varchar(150) | NO |  |  |  |
| nomcos | varchar(50) | NO |  |  |  |

**Muestras (3 filas):**

```json
[
  {
    "codcue": "41359501",
    "detcue": "Venta de otros productos",
    "salant": "0.0",
    "valdeb": "0.0",
    "valhab": "186600.0",
    "nuesal": "0.0",
    "nomcla": "INGRESOS",
    "nomgru": "Operacionales",
    "nomcue": "Comercio al por mayor y al por menor",
    "nomsub": "Venta de otros productos",
    "nomaux": "Venta de otros productos",
    "nitter": "",
    "nomter": "",
    "numnum": "",
    "fecdoc": "2000-01-20 00:00:00",
    "codprod": "",
    "codclas": "",
    "codcos": "",
    "docext": "",
    "detaux": "",
    "nitnomi": "",
    "nomnomi": "",
    "nomcos": ""
  },
  {
    "codcue": "61359501",
    "detcue": "Venta de otros productos",
    "salant": "0.0",
    "valdeb": "178914.0",
    "valhab": "0.0",
    "nuesal": "0.0",
    "nomcla": "COSTOS DE VENTAS",
    "nomgru": "Costo de ventas y de prestaci├│n de servicios",
    "nomcue": "Comercio al por mayor y al por menor",
    "nomsub": "Venta de otros productos",
    "nomaux": "Venta de otros productos",
    "nitter": "",
    "nomter": "",
    "numnum": "",
    "fecdoc": "2000-01-20 00:00:00",
    "codprod": "",
    "codclas": "",
    "codcos": "",
    "docext": "",
    "detaux": "",
    "nitnomi": "",
    "nomnomi": "",
    "nomcos": ""
  }
]
```

---

## `auxrepdim` (3 filas)

| Campo | Tipo | Nulo | Key | Default | Extra |
|-------|------|------|-----|---------|-------|
| numdoc | varchar(20) | NO | MUL |  |  |
| codclas | varchar(4) | NO |  |  |  |
| nomdoc | varchar(100) | NO |  | COMPRA |  |
| predoc | varchar(8) | NO |  | COM |  |
| fecdoc | datetime | NO |  | 2000-01-20 00:00:00 |  |
| nitter | varchar(15) | NO | MUL |  |  |
| digter | char(2) | NO |  |  |  |
| nomter | varchar(120) | NO |  |  |  |
| clase | varchar(4) | NO |  |  |  |
| agrfec | smallint(6) | NO |  | 0 |  |
| codcue | varchar(12) | NO |  |  |  |
| subdoc | double | NO |  | 0 |  |
| dctdoc | double | NO |  | 0 |  |
| valbas | double | NO |  | 0 |  |
| ivapor | float | NO |  | 0 |  |
| valiva | double | NO |  | 0 |  |
| valcon | double | NO |  | 0 |  |
| valcre | double | NO |  | 0 |  |
| cheque | double | NO |  | 0 |  |
| tardeb | double | NO |  | 0 |  |
| tarcre | double | NO |  | 0 |  |
| crucea | double | NO |  | 0 |  |
| valcmen | double | NO |  | 0 |  |
| entosal | varchar(8) | NO |  |  |  |
| docext | varchar(20) | NO |  |  |  |
| valcar | double | NO |  | 0 |  |
| dctglob | double | NO |  | 0 |  |

**Muestras (3 filas):**

```json
[
  {
    "numdoc": "86",
    "codclas": "S15",
    "nomdoc": "FACTURA DE VENTA POS",
    "predoc": "FVP",
    "fecdoc": "2026-06-14 00:00:00",
    "nitter": "222222222",
    "digter": "",
    "nomter": "CONSUMIDOR  FINAL",
    "clase": "",
    "agrfec": "0",
    "codcue": "",
    "subdoc": "7000.0",
    "dctdoc": "0.0",
    "valbas": "0.0",
    "ivapor": "0.0",
    "valiva": "0.0",
    "valcon": "7000.0",
    "valcre": "0.0",
    "cheque": "0.0",
    "tardeb": "0.0",
    "tarcre": "0.0",
    "crucea": "0.0",
    "valcmen": "0.0",
    "entosal": "",
    "docext": "",
    "valcar": "0.0",
    "dctglob": "0.0"
  },
  {
    "numdoc": "87",
    "codclas": "S15",
    "nomdoc": "FACTURA DE VENTA POS",
    "predoc": "FVP",
    "fecdoc": "2026-06-14 00:00:00",
    "nitter": "",
    "digter": "",
    "nomter": " ",
    "clase": "",
    "agrfec": "0",
    "codcue": "",
    "subdoc": "25300.0",
    "dctdoc": "0.0",
    "valbas": "0.0",
    "ivapor": "0.0",
    "valiva": "0.0",
    "valcon": "25300.0",
    "valcre": "0.0",
    "cheque": "0.0",
    "tardeb": "0.0",
    "tarcre": "0.0",
    "crucea": "0.0",
    "valcmen": "0.0",
    "entosal": "",
    "docext": "",
    "valcar": "0.0",
    "dctglob": "0.0"
  },
  {
    "numdoc": "88",
    "codclas": "S15",
    "nomdoc": "FACTURA DE VENTA POS",
    "predoc": "FVP",
    "fecdoc": "2026-06-14 00:00:00",
    "nitter": "",
    "digter": "",
    "nomter": " ",
    "clase": "",
    "agrfec": "0",
    "codcue": "",
    "subdoc": "4000.0",
    "dctdoc": "0.0",
    "valbas": "0.0",
    "ivapor": "0.0",
    "valiva": "0.0",
    "valcon": "4000.0",
    "valcre": "0.0",
    "cheque": "0.0",
    "tardeb": "0.0",
    "tarcre": "0.0",
    "crucea": "0.0",
    "valcmen": "0.0",
    "entosal": "",
    "docext": "",
    "valcar": "0.0",
    "dctglob": "0.0"
  }
]
```

---

## `bancos` (2 filas)

| Campo | Tipo | Nulo | Key | Default | Extra |
|-------|------|------|-----|---------|-------|
| codban | varchar(8) | NO | PRI |  |  |
| nomban | varchar(100) | NO |  |  |  |
| pucban | varchar(12) | NO |  |  |  |

**Muestras (3 filas):**

```json
[
  {
    "codban": "B02",
    "nomban": "BANCOLOMBIA",
    "pucban": "11100501"
  },
  {
    "codban": "B03",
    "nomban": "NEQUI",
    "pucban": ""
  }
]
```

---

## `bancosemp` (1 filas)

| Campo | Tipo | Nulo | Key | Default | Extra |
|-------|------|------|-----|---------|-------|
| codban | varchar(8) | NO | MUL |  |  |
| nitter | varchar(15) | NO | MUL |  |  |
| numcue | varchar(25) | NO |  |  |  |
| tipo | varchar(12) | NO |  | CORRIENTE |  |
| titular | varchar(100) | NO |  |  |  |

**Muestras (3 filas):**

```json
[
  {
    "codban": "B02",
    "nitter": "1151970853",
    "numcue": "",
    "tipo": "DE AHORROS",
    "titular": ""
  }
]
```

---

## `bodegas` (1 filas)

| Campo | Tipo | Nulo | Key | Default | Extra |
|-------|------|------|-----|---------|-------|
| codbod | varchar(4) | NO | PRI |  |  |
| nombod | varchar(100) | NO |  |  |  |
| telbod | varchar(30) | NO |  |  |  |
| ubibod | varchar(100) | NO |  |  |  |
| resbod | varchar(100) | NO |  |  |  |

**Muestras (3 filas):**

```json
[
  {
    "codbod": "BD01",
    "nombod": "BODEGA PRINCIPAL",
    "telbod": " ",
    "ubibod": " ",
    "resbod": " "
  }
]
```

---

## `cajaarqueo` (0 filas)

| Campo | Tipo | Nulo | Key | Default | Extra |
|-------|------|------|-----|---------|-------|
| numarq | varchar(20) | NO | MUL |  |  |
| codclas | varchar(4) | NO | MUL |  |  |
| nomdoc | varchar(100) | NO |  | ARQUEO DE CAJA |  |
| prearq | varchar(8) | NO |  |  |  |
| fecarq | datetime | NO |  | 2000-01-01 00:00:00 |  |
| nitter | varchar(15) | NO | MUL |  |  |
| codcue | varchar(12) | NO |  |  |  |
| salcaj | double | NO |  | 0 |  |
| obsarq | varchar(400) | NO |  |  |  |
| estarq | char(1) | NO |  |  |  |
| codemp | varchar(15) | NO | MUL |  |  |
| empcod | varchar(3) | NO | MUL |  |  |
| tiparq | char(1) | NO |  | C |  |
| veridoc | tinyint(1) | NO |  | 0 |  |
| feccrea | datetime | NO |  | 2000-01-20 00:00:00 |  |

**Muestras (3 filas):**

```json
[]
```

---

## `cajas` (1 filas)

| Campo | Tipo | Nulo | Key | Default | Extra |
|-------|------|------|-----|---------|-------|
| codcaj | varchar(4) | NO | PRI |  |  |
| descaj | varchar(50) | NO |  | CAJA UNO |  |
| indgen | char(3) | NO |  | GEN |  |
| titfac | varchar(50) | NO |  | FACTURA DE VENTA |  |
| codres | varchar(4) | NO | MUL |  |  |
| resdian | char(2) | NO |  | NO |  |
| numres | varchar(20) | NO |  |  |  |
| fecres | date | NO |  | 2000-01-01 |  |
| numini | bigint(20) | NO |  | 1 |  |
| numfin | bigint(20) | NO |  | 100 |  |
| numauto | char(2) | NO |  | SI |  |
| fecauto | char(2) | NO |  | NO |  |
| conres | bigint(20) | NO |  | 1 |  |
| avires | bigint(20) | NO |  | 0 |  |
| preres | varchar(8) | NO |  |  |  |
| imptiq | char(2) | NO |  | NO |  |
| codpag | varchar(4) | NO |  |  |  |
| empsino | char(1) | NO |  | N |  |
| maqnom | varchar(250) | NO |  |  |  |
| afeclas | varchar(4) | NO |  | S15 |  |
| prefgen | char(1) | NO |  | S |  |
| numplac | varchar(50) | NO |  |  |  |
| ubicaj | varchar(100) | NO |  |  |  |
| codiven | varchar(30) | NO |  |  |  |
| tipdomi | char(1) | NO |  |  |  |

**Muestras (3 filas):**

```json
[
  {
    "codcaj": "C1",
    "descaj": "CAJA UNO",
    "indgen": "GEN",
    "titfac": "FACTURA DE VENTA",
    "codres": " ",
    "resdian": "NO",
    "numres": " ",
    "fecres": "2000-01-01",
    "numini": "1",
    "numfin": "100",
    "numauto": "SI",
    "fecauto": "SI",
    "conres": "1",
    "avires": "0",
    "preres": "PFV",
    "imptiq": "NO",
    "codpag": "",
    "empsino": "N",
    "maqnom": "",
    "afeclas": "S15",
    "prefgen": "S",
    "numplac": "",
    "ubicaj": "",
    "codiven": "",
    "tipdomi": ""
  }
]
```

---

## `cajaspago` (1 filas)

| Campo | Tipo | Nulo | Key | Default | Extra |
|-------|------|------|-----|---------|-------|
| codcaj | varchar(4) | NO | PRI |  |  |
| nomcaj | varchar(100) | NO |  |  |  |
| puccaj | varchar(12) | NO |  |  |  |

**Muestras (3 filas):**

```json
[
  {
    "codcaj": "CA1",
    "nomcaj": "CAJA PRINCIPAL",
    "puccaj": "11050501"
  }
]
```

---

## `cargosemp` (4 filas)

| Campo | Tipo | Nulo | Key | Default | Extra |
|-------|------|------|-----|---------|-------|
| codcar | varchar(5) | NO | PRI |  |  |
| nomcar | varchar(50) | NO |  |  |  |

**Muestras (3 filas):**

```json
[
  {
    "codcar": "E1",
    "nomcar": "GERENTE"
  },
  {
    "codcar": "E2",
    "nomcar": "CONTADOR"
  },
  {
    "codcar": "E3",
    "nomcar": "SECRETARIA"
  }
]
```

---

## `cecostos` (1 filas)

| Campo | Tipo | Nulo | Key | Default | Extra |
|-------|------|------|-----|---------|-------|
| codcos | varchar(6) | NO | PRI |  |  |
| nomcos | varchar(50) | NO |  |  |  |
| codlis | char(3) | NO | MUL |  |  |

**Muestras (3 filas):**

```json
[
  {
    "codcos": "CC1",
    "nomcos": "CENTRO DE COSTO 1",
    "codlis": ""
  }
]
```

---

## `cierresper` (0 filas)

| Campo | Tipo | Nulo | Key | Default | Extra |
|-------|------|------|-----|---------|-------|
| codcie | int(11) | NO | PRI | 0 |  |
| fecdes | date | NO |  | 2000-01-20 |  |
| fechas | date | NO |  | 2000-01-20 |  |
| tipcie | char(1) | NO |  | P |  |
| numaju | varchar(20) | NO |  |  |  |
| codclas | varchar(4) | NO |  |  |  |
| numaju1 | varchar(20) | NO |  |  |  |
| codclas1 | varchar(4) | NO |  |  |  |

**Muestras (3 filas):**

```json
[]
```

---

## `ciudades` (1120 filas)

| Campo | Tipo | Nulo | Key | Default | Extra |
|-------|------|------|-----|---------|-------|
| codciu | varchar(6) | NO | PRI |  |  |
| codreg | varchar(4) | NO | MUL |  |  |
| nomciu | varchar(150) | NO |  |  |  |
| ciucod | varchar(4) | NO |  |  |  |
| codfel1 | varchar(6) | NO |  |  |  |

**Muestras (3 filas):**

```json
[
  {
    "codciu": "05001",
    "codreg": "05",
    "nomciu": "MEDELLIN",
    "ciucod": "001",
    "codfel1": "1"
  },
  {
    "codciu": "05002",
    "codreg": "05",
    "nomciu": "ABEJORRAL",
    "ciucod": "002",
    "codfel1": "2"
  },
  {
    "codciu": "05004",
    "codreg": "05",
    "nomciu": "ABRIAQUI",
    "ciucod": "004",
    "codfel1": "3"
  }
]
```

---

## `comevenrecep` (0 filas)

| Campo | Tipo | Nulo | Key | Default | Extra |
|-------|------|------|-----|---------|-------|
| numeve | varchar(20) | NO | MUL |  |  |
| codclas | varchar(4) | NO | MUL |  |  |
| preeve | varchar(8) | NO |  |  |  |
| nomdoc | varchar(100) | NO |  |  |  |
| feceve | datetime | NO |  | 2000-01-20 00:00:00 |  |
| docafe | varchar(20) | NO | MUL |  |  |
| clasafe | varchar(4) | NO | MUL |  |  |
| tipeve | char(1) | NO |  |  |  |
| facele | varchar(20) | NO |  |  |  |
| cocufe | varchar(150) | NO |  |  |  |
| nitter | varchar(15) | NO | MUL |  |  |
| codemp | varchar(15) | NO |  |  |  |
| esteve | char(1) | NO |  |  |  |
| nitprov | varchar(15) | NO |  |  |  |

**Muestras (3 filas):**

```json
[]
```

---

## `comicafe` (0 filas)

| Campo | Tipo | Nulo | Key | Default | Extra |
|-------|------|------|-----|---------|-------|
| numcom | varchar(20) | NO | MUL |  |  |
| codclas | varchar(4) | NO | MUL |  |  |
| feccom | date | NO |  | 2000-01-01 |  |
| nitter | varchar(15) | NO | MUL |  |  |
| totcom | double | NO |  | 0 |  |
| codcomi | varchar(20) | NO |  |  |  |
| valcomi | double | NO |  | 0 |  |
| comifec | date | NO |  | 2000-01-01 |  |
| numegr | varchar(20) | NO |  |  |  |
| clasegr | varchar(4) | NO |  |  |  |
| fecegr | date | NO |  | 2000-01-01 |  |
| estcomi | char(1) | NO |  | 1 |  |

**Muestras (3 filas):**

```json
[]
```

---

## `compdiario` (0 filas)

| Campo | Tipo | Nulo | Key | Default | Extra |
|-------|------|------|-----|---------|-------|
| numcom | int(11) | NO | MUL | 0 |  |
| titcom | varchar(50) | NO |  |  |  |
| fecdes | date | NO |  | 2000-01-20 |  |
| fechas | date | NO |  | 2000-01-20 |  |
| auxdoc | char(2) | NO |  | NO |  |

**Muestras (3 filas):**

```json
[]
```

---

## `compras` (56 filas)

| Campo | Tipo | Nulo | Key | Default | Extra |
|-------|------|------|-----|---------|-------|
| numcom | varchar(20) | NO | MUL |  |  |
| codclas | varchar(4) | NO | MUL |  |  |
| nomdoc | varchar(100) | NO |  | COMPRA |  |
| precom | varchar(8) | NO |  | COM |  |
| feccom | datetime | NO |  | 2000-01-20 00:00:00 |  |
| diascot | int(11) | NO |  | 0 |  |
| faccom | varchar(20) | NO |  |  |  |
| nitter | varchar(15) | NO | MUL |  |  |
| digcom | char(2) | NO |  |  |  |
| codsuc | varchar(15) | NO | MUL |  |  |
| procom | varchar(120) | NO |  |  |  |
| dircom | varchar(100) | NO |  |  |  |
| telcom | varchar(50) | NO |  |  |  |
| codpag | varchar(4) | NO |  |  |  |
| subcom | double | NO |  | 0 |  |
| totdct | double | NO |  | 0 |  |
| totiva | double | NO |  | 0 |  |
| totipo | double | NO |  | 0 |  |
| retfte | double | NO |  | 0 |  |
| retiva | double | NO |  | 0 |  |
| retica | double | NO |  | 0 |  |
| retcre | double | NO |  | 0 |  |
| ajuspe | double | NO |  | 0 |  |
| totcom | double | NO |  | 0 |  |
| obscom | varchar(400) | NO |  |  |  |
| estcom | char(1) | NO |  |  |  |
| codemp | varchar(15) | NO | MUL |  |  |
| horcom | tinyint(3) | NO |  | 1 |  |
| codres | varchar(4) | NO | MUL |  |  |
| numcru | varchar(20) | NO | MUL |  |  |
| clascru | varchar(4) | NO | MUL |  |  |
| codcos | varchar(6) | NO | MUL |  |  |
| codzon | varchar(4) | NO |  |  |  |
| empcod | varchar(3) | NO | MUL |  |  |
| nitvend | varchar(15) | NO | MUL |  |  |
| codpla | varchar(30) | NO |  |  |  |
| artsol | varchar(50) | NO |  |  |  |
| marsol | varchar(50) | NO |  |  |  |
| modsol | varchar(50) | NO |  |  |  |
| trarea | varchar(400) | NO |  |  |  |
| recesp | varchar(400) | NO |  |  |  |
| horini | datetime | NO |  | 2000-01-01 00:00:00 |  |
| horfin | datetime | NO |  | 2000-01-01 00:00:00 |  |
| codmes | varchar(4) | NO |  |   |  |
| estado | char(1) | NO |  | A |  |
| garfac | varchar(30) | NO |  |  |  |
| verifi | char(1) | NO |  |  |  |
| cauret | char(1) | NO |  |  |  |
| porrfte | float | NO |  | 0 |  |
| agrupa | char(1) | NO |  |  |  |
| corele | varchar(100) | NO |  |  |  |
| otrimp | double | NO |  | 0 |  |
| dctglob | double | NO |  | 0 |  |
| recglob | double | NO |  | 0 |  |
| tazacam | double | NO |  | 0 |  |
| moneda | varchar(4) | NO |  |  |  |
| salant | double | NO |  | 0 |  |
| salnue | double | NO |  | 0 |  |
| pendfac | char(1) | NO |  |  |  |
| veridoc | tinyint(1) | NO |  | 0 |  |
| feccrea | datetime | NO |  | 2000-01-20 00:00:00 |  |

**Muestras (3 filas):**

```json
[
  {
    "numcom": "1",
    "codclas": "S18",
    "nomdoc": "COMPRA",
    "precom": "COM",
    "feccom": "2026-05-17 18:57:50",
    "diascot": "0",
    "faccom": "62018",
    "nitter": "900778480",
    "digcom": "6",
    "codsuc": "",
    "procom": "A DE COCO",
    "dircom": "CL 84 15 45 OF 501",
    "telcom": "6165639",
    "codpag": "F07",
    "subcom": "668400.0",
    "totdct": "0.0",
    "totiva": "0.0",
    "totipo": "0.0",
    "retfte": "0.0",
    "retiva": "0.0",
    "retica": "0.0",
    "retcre": "0.0",
    "ajuspe": "0.0",
    "totcom": "668400.0",
    "obscom": " ",
    "estcom": "B",
    "codemp": "1151970853",
    "horcom": "18",
    "codres": "",
    "numcru": "",
    "clascru": "",
    "codcos": "",
    "codzon": "",
    "empcod": "",
    "nitvend": "",
    "codpla": "",
    "artsol": "",
    "marsol": "",
    "modsol": "",
    "trarea": "",
    "recesp": "",
    "horini": "2000-01-01 00:00:00",
    "horfin": "2000-01-01 00:00:00",
    "codmes": " ",
    "estado": "A",
    "garfac": "",
    "verifi": "",
    "cauret": "S",
    "porrfte": "0.0",
    "agrupa": "",
    "corele": "",
    "otrimp": "0.0",
    "dctglob": "0.0",
    "recglob": "0.0",
    "tazacam": "0.0",
    "moneda": "COP",
    "salant": "0.0",
    "salnue": "0.0",
    "pendfac": "",
    "veridoc": "0",
    "feccrea": "2000-01-20 00:00:00"
  },
  {
    "numcom": "2",
    "codclas": "S18",
    "nomdoc": "COMPRA",
    "precom": "COM",
    "feccom": "2026-05-20 19:52:42",
    "diascot": "0",
    "faccom": "1195",
    "nitter": "11111",
    "digcom": "",
    "codsuc": "",
    "procom": "KOMBUCHAS  DAR",
    "dircom": "CONOCIDA",
    "telcom": "3125555796",
    "codpag": "F07",
    "subcom": "288660.0",
    "totdct": "0.0",
    "totiva": "0.0",
    "totipo": "0.0",
    "retfte": "0.0",
    "retiva": "0.0",
    "retica": "0.0",
    "retcre": "0.0",
    "ajuspe": "0.0",
    "totcom": "288660.0",
    "obscom": " ",
    "estcom": "B",
    "codemp": "1151970853",
    "horcom": "19",
    "codres": "",
    "numcru": "",
    "clascru": "",
    "codcos": "",
    "codzon": "",
    "empcod": "",
    "nitvend": "",
    "codpla": "",
    "artsol": "",
    "marsol": "",
    "modsol": "",
    "trarea": "",
    "recesp": "",
    "horini": "2000-01-01 00:00:00",
    "horfin": "2000-01-01 00:00:00",
    "codmes": " ",
    "estado": "A",
    "garfac": "",
    "verifi": "",
    "cauret": "S",
    "porrfte": "0.0",
    "agrupa": "",
    "corele": "",
    "otrimp": "0.0",
    "dctglob": "0.0",
    "recglob": "0.0",
    "tazacam": "0.0",
    "moneda": "COP",
    "salant": "0.0",
    "salnue": "0.0",
    "pendfac": "",
    "veridoc": "0",
    "feccrea": "2000-01-20 00:00:00"
  },
  {
    "numcom": "3",
    "codclas": "S18",
    "nomdoc": "COMPRA",
    "precom": "COM",
    "feccom": "2026-05-17 20:29:04",
    "diascot": "0",
    "faccom": "418",
    "nitter": "901472390",
    "digcom": "",
    "codsuc": "",
    "procom": "CHONTAAREPA",
    "dircom": "Calle 7 # 28 - 35 - Cali",
    "telcom": "3046038920",
    "codpag": "F07",
    "subcom": "190010.0",
    "totdct": "0.0",
    "totiva": "0.0",
    "totipo": "0.0",
    "retfte": "0.0",
    "retiva": "0.0",
    "retica": "0.0",
    "retcre": "0.0",
    "ajuspe": "0.0",
    "totcom": "190010.0",
    "obscom": " ",
    "estcom": "B",
    "codemp": "1151970853",
    "horcom": "20",
    "codres": "",
    "numcru": "",
    "clascru": "",
    "codcos": "",
    "codzon": "",
    "empcod": "",
    "nitvend": "",
    "codpla": "",
    "artsol": "",
    "marsol": "",
    "modsol": "",
    "trarea": "",
    "recesp": "",
    "horini": "2000-01-01 00:00:00",
    "horfin": "2000-01-01 00:00:00",
    "codmes": " ",
    "estado": "A",
    "garfac": "",
    "verifi": "",
    "cauret": "S",
    "porrfte": "0.0",
    "agrupa": "",
    "corele": "",
    "otrimp": "0.0",
    "dctglob": "0.0",
    "recglob": "0.0",
    "tazacam": "0.0",
    "moneda": "COP",
    "salant": "0.0",
    "salnue": "0.0",
    "pendfac": "",
    "veridoc": "0",
    "feccrea": "2000-01-20 00:00:00"
  }
]
```

---

## `comprobantes` (3 filas)

| Campo | Tipo | Nulo | Key | Default | Extra |
|-------|------|------|-----|---------|-------|
| numegr | varchar(20) | NO | MUL |  |  |
| codclas | varchar(4) | NO | MUL |  |  |
| nomdoc | varchar(100) | NO |  | COMPROBANTE DE EGRESO |  |
| preegr | varchar(8) | NO |  | CE |  |
| fecegr | datetime | NO |  | 2000-01-20 00:00:00 |  |
| nitter | varchar(15) | NO | MUL |  |  |
| digver | char(2) | NO |  |  |  |
| codsuc | varchar(15) | NO | MUL |  |  |
| cliegr | varchar(120) | NO |  |  |  |
| diregr | varchar(100) | NO |  |  |  |
| telegr | varchar(50) | NO |  |  |  |
| codpag | varchar(4) | NO |  |  |  |
| subegr | double | NO |  | 0 |  |
| totdct | double | NO |  | 0 |  |
| ajuspe | double | NO |  | 0 |  |
| totegr | double | NO |  | 0 |  |
| obsegr | varchar(400) | NO |  |  |  |
| estegr | char(1) | NO |  |  |  |
| codemp | varchar(15) | NO | MUL |  |  |
| horegr | tinyint(3) | NO |  | 1 |  |
| codres | varchar(4) | NO | MUL |  |  |
| codcos | varchar(6) | NO | MUL |  |  |
| empcod | varchar(3) | NO | MUL |  |  |
| nitcob | varchar(15) | NO |  |  |  |
| docext | varchar(20) | NO |  |  |  |
| codcaj | varchar(4) | NO | MUL |  |  |
| turno1 | char(1) | NO |  | 0 |  |
| numcru | varchar(20) | NO | MUL |  |  |
| clascru | varchar(4) | NO | MUL |  |  |
| agrupa | char(1) | NO |  |  |  |
| cdtipag | varchar(4) | NO |  |  |  |
| veridoc | tinyint(1) | NO |  | 0 |  |
| feccrea | datetime | NO |  | 2000-01-20 00:00:00 |  |

**Muestras (3 filas):**

```json
[
  {
    "numegr": "1",
    "codclas": "S02",
    "nomdoc": "COMPROBANTE DE EGRESO",
    "preegr": "CE",
    "fecegr": "2026-06-12 12:19:37",
    "nitter": "100",
    "digver": "",
    "codsuc": "",
    "cliegr": "FAMILIA MASVITAL",
    "diregr": "CRA 41 315 B 64",
    "telegr": "3014128705",
    "codpag": "",
    "subegr": "83700.0",
    "totdct": "83700.0",
    "ajuspe": "0.0",
    "totegr": "83700.0",
    "obsegr": "PAGO FLETE ",
    "estegr": "B",
    "codemp": "1151970853",
    "horegr": "12",
    "codres": "",
    "codcos": "",
    "empcod": "",
    "nitcob": "",
    "docext": "",
    "codcaj": "",
    "turno1": "0",
    "numcru": "",
    "clascru": "",
    "agrupa": "",
    "cdtipag": "",
    "veridoc": "0",
    "feccrea": "2026-06-13 12:21:37"
  },
  {
    "numegr": "2",
    "codclas": "S02",
    "nomdoc": "COMPROBANTE DE EGRESO",
    "preegr": "CE",
    "fecegr": "2026-06-12 12:25:53",
    "nitter": "100",
    "digver": "",
    "codsuc": "",
    "cliegr": "FAMILIA MASVITAL",
    "diregr": "CRA 41 315 B 64",
    "telegr": "3014128705",
    "codpag": "",
    "subegr": "52400.0",
    "totdct": "52400.0",
    "ajuspe": "0.0",
    "totegr": "52400.0",
    "obsegr": "COMPRA UTENCILIOS DE CAFETERIA",
    "estegr": "B",
    "codemp": "1151970853",
    "horegr": "12",
    "codres": "",
    "codcos": "",
    "empcod": "",
    "nitcob": "",
    "docext": "",
    "codcaj": "",
    "turno1": "0",
    "numcru": "",
    "clascru": "",
    "agrupa": "",
    "cdtipag": "",
    "veridoc": "0",
    "feccrea": "2026-06-13 12:28:08"
  },
  {
    "numegr": "3",
    "codclas": "S02",
    "nomdoc": "COMPROBANTE DE EGRESO",
    "preegr": "CE",
    "fecegr": "2026-06-13 17:26:30",
    "nitter": "100",
    "digver": "",
    "codsuc": "",
    "cliegr": "FAMILIA MASVITAL",
    "diregr": "CRA 41 315 B 64",
    "telegr": "3014128705",
    "codpag": "",
    "subegr": "7020.0",
    "totdct": "7020.0",
    "ajuspe": "0.0",
    "totegr": "7020.0",
    "obsegr": "SUMINISTROS DE CAFETERIA",
    "estegr": "B",
    "codemp": "1151970853",
    "horegr": "17",
    "codres": "",
    "codcos": "",
    "empcod": "",
    "nitcob": "",
    "docext": "",
    "codcaj": "",
    "turno1": "0",
    "numcru": "",
    "clascru": "",
    "agrupa": "",
    "cdtipag": "",
    "veridoc": "0",
    "feccrea": "2026-06-13 17:30:42"
  }
]
```

---

## `concepingegr` (6 filas)

| Campo | Tipo | Nulo | Key | Default | Extra |
|-------|------|------|-----|---------|-------|
| codcon | varchar(12) | NO | PRI |  |  |
| nomcon | varchar(100) | NO |  |  |  |
| valcon | double | NO |  | 0 |  |
| tipcon | char(7) | NO |  | EGRESO |  |
| debcre | char(1) | NO |  | D |  |
| codcue | varchar(20) | NO | MUL |  |  |
| descon | varchar(400) | NO |  |  |  |
| codpor | varchar(4) | NO | MUL |  |  |

**Muestras (3 filas):**

```json
[
  {
    "codcon": "51353001",
    "nomcon": "Energ├¡a el├®ctrica",
    "valcon": "0.0",
    "tipcon": "EGRESO",
    "debcre": "D",
    "codcue": "51353001",
    "descon": " ",
    "codpor": ""
  },
  {
    "codcon": "51353501",
    "nomcon": "Tel├®fono",
    "valcon": "0.0",
    "tipcon": "EGRESO",
    "debcre": "D",
    "codcue": "51353501",
    "descon": " ",
    "codpor": ""
  },
  {
    "codcon": "51050601",
    "nomcon": "Pago de sueldos",
    "valcon": "0.0",
    "tipcon": "EGRESO",
    "debcre": "D",
    "codcue": "51050601",
    "descon": " ",
    "codpor": ""
  }
]
```

---

## `concibanper` (0 filas)

| Campo | Tipo | Nulo | Key | Default | Extra |
|-------|------|------|-----|---------|-------|
| codper | varchar(6) | NO | PRI |  |  |
| codcue | varchar(20) | NO | MUL |  |  |
| nomper | varchar(100) | NO |  |  |  |
| mesper | int(4) | NO |  | 0 |  |
| anoper | int(6) | NO |  | 0 |  |
| perdes | date | NO |  | 2000-01-01 |  |
| perhas | date | NO |  | 2000-01-01 |  |
| valext | double | NO |  | 0 |  |

**Muestras (3 filas):**

```json
[]
```

---

## `conimpdoc` (57 filas)

| Campo | Tipo | Nulo | Key | Default | Extra |
|-------|------|------|-----|---------|-------|
| codcon | varchar(4) | NO | MUL |  |  |
| tamimp | tinyint(3) | NO |  | 1 |  |
| cabimp | tinyint(3) | NO |  | 1 |  |
| detimp | varchar(15) | NO |  |  |  |
| pieimp | varchar(15) | NO |  |  |  |
| disdat | char(2) | NO |  | SI |  |
| relcer | tinyint(3) | NO |  | 0 |  |
| numdeci | varchar(4) | NO |  | 0 |  |
| implogtiq | char(2) | NO |  | NO |  |
| descab | varchar(800) | NO |  |  |  |
| despie | varchar(800) | NO |  |  |  |
| desadi | varchar(800) | NO |  |  |  |
| arcimg | varchar(255) | NO |  |  |  |
| impcod | char(2) | NO |  | SI |  |
| tipcon | char(1) | NO |  | S |  |
| codcaj | varchar(4) | NO |  |  |  |
| dettiq | varchar(6) | NO |  |  |  |
| letrimp | char(1) | NO |  | N |  |
| color1 | char(1) | NO |  | 0 |  |
| dobdes | char(1) | NO |  | 0 |  |
| imgfirma | varchar(255) | NO |  |  |  |
| topcar | varchar(10) | NO |  | 1.5 |  |
| botcar | varchar(10) | NO |  | 1 |  |
| topmed | varchar(10) | NO |  | .88 |  |
| botmed | varchar(10) | NO |  | 14 |  |
| codebar | char(1) | NO |  |  |  |
| tiqimg | varchar(255) | NO |  |  |  |
| oriimp | char(1) | NO |  | 0 |  |

**Muestras (3 filas):**

```json
[
  {
    "codcon": "S08",
    "tamimp": "1",
    "cabimp": "8",
    "detimp": ",1,4,6,8",
    "pieimp": ",2,3",
    "disdat": "SI",
    "relcer": "4",
    "numdeci": "0",
    "implogtiq": "NO",
    "descab": " ",
    "despie": "El presente documento se asimila en sus efectos a una letra de cambio. Art. 774 del C.C. El comprador y el aceptante declaran haber recibido real y materialmente las mercanc├¡as o servicios descritos en este t├¡tulo valor, la mora en el pago ocasiona intereses (%) a la taza autorizada legalmente.",
    "desadi": " ",
    "arcimg": " ",
    "impcod": "SI",
    "tipcon": "S",
    "codcaj": "",
    "dettiq": "",
    "letrimp": "N",
    "color1": "0",
    "dobdes": "0",
    "imgfirma": " ",
    "topcar": "1.5",
    "botcar": "1",
    "topmed": "0.88",
    "botmed": "14",
    "codebar": "0",
    "tiqimg": " ",
    "oriimp": "0"
  },
  {
    "codcon": "S23",
    "tamimp": "1",
    "cabimp": "8",
    "detimp": ",1",
    "pieimp": " ",
    "disdat": "SI",
    "relcer": "4",
    "numdeci": "0",
    "implogtiq": "NO",
    "descab": "",
    "despie": "",
    "desadi": "",
    "arcimg": "",
    "impcod": "SI",
    "tipcon": "S",
    "codcaj": "",
    "dettiq": "",
    "letrimp": "N",
    "color1": "0",
    "dobdes": "0",
    "imgfirma": "",
    "topcar": "1.5",
    "botcar": "1",
    "topmed": ".88",
    "botmed": "14",
    "codebar": "",
    "tiqimg": "",
    "oriimp": "0"
  },
  {
    "codcon": "S28",
    "tamimp": "1",
    "cabimp": "8",
    "detimp": ",1",
    "pieimp": " ",
    "disdat": "SI",
    "relcer": "4",
    "numdeci": "0",
    "implogtiq": "NO",
    "descab": "",
    "despie": "",
    "desadi": "",
    "arcimg": "",
    "impcod": "SI",
    "tipcon": "S",
    "codcaj": "",
    "dettiq": "",
    "letrimp": "N",
    "color1": "0",
    "dobdes": "0",
    "imgfirma": "",
    "topcar": "1.5",
    "botcar": "1",
    "topmed": ".88",
    "botmed": "14",
    "codebar": "",
    "tiqimg": "",
    "oriimp": "0"
  }
]
```

---

## `consbancab` (0 filas)

| Campo | Tipo | Nulo | Key | Default | Extra |
|-------|------|------|-----|---------|-------|
| numcon | varchar(20) | NO | MUL |  |  |
| nomdoc | varchar(100) | NO |  | RECIBO DE CAJA MENOR |  |
| precon | varchar(8) | NO |  | RC |  |
| feccon | datetime | NO |  | 2000-01-20 00:00:00 |  |
| codcue | varchar(20) | NO |  |  |  |
| codpag | varchar(4) | NO |  |  |  |
| detcon | varchar(300) | NO |  |  |  |
| totcon | double | NO |  | 0 |  |
| estcon | char(1) | NO |  |  |  |
| codemp | varchar(15) | NO | MUL |  |  |
| horcaj | tinyint(3) | NO |  | 1 |  |
| codres | varchar(4) | NO | MUL |  |  |
| tipret | char(8) | NO |  | DEPOSITO |  |
| codcos | varchar(6) | NO | MUL |  |  |
| codclas | varchar(4) | NO | MUL |  |  |
| empcod | varchar(3) | NO | MUL |  |  |
| cod2cos | varchar(6) | NO |  |  |  |
| veridoc | tinyint(1) | NO |  | 0 |  |
| feccrea | datetime | NO |  | 2000-01-20 00:00:00 |  |

**Muestras (3 filas):**

```json
[]
```

---

## `consbandet` (0 filas)

| Campo | Tipo | Nulo | Key | Default | Extra |
|-------|------|------|-----|---------|-------|
| numcon | varchar(20) | NO | MUL |  |  |
| codcue | varchar(20) | NO |  |  |  |
| detcue | varchar(150) | NO |  |  |  |
| valdet | double | NO |  | 0 |  |
| tipcaj | char(3) | NO |  | GEN |  |
| codpag | varchar(4) | NO | MUL |  |  |
| nitter | varchar(15) | NO | MUL |  |  |
| codclas | varchar(4) | NO | MUL |  |  |

**Muestras (3 filas):**

```json
[]
```

---

## `contadores` (57 filas)

| Campo | Tipo | Nulo | Key | Default | Extra |
|-------|------|------|-----|---------|-------|
| codcon | varchar(4) | NO | PRI |  |  |
| numcon | smallint(6) | NO |  | 0 |  |
| descon | varchar(100) | NO |  |  |  |
| actcon | char(2) | NO |  | NO |  |
| caucon | char(2) | NO |  | SI |  |
| resdian | char(2) | NO |  | NO |  |
| codres | varchar(4) | NO |  |  |  |
| numres | varchar(30) | NO |  |  |  |
| fecres | date | NO |  | 2000-01-01 |  |
| numini | bigint(20) | NO |  | 1 |  |
| numfin | bigint(20) | NO |  | 100 |  |
| numauto | char(2) | NO |  | SI |  |
| fecauto | char(2) | NO |  | NO |  |
| conres | bigint(20) | NO |  | 1 |  |
| avires | bigint(20) | NO |  | 0 |  |
| preres | varchar(8) | NO |  |  |  |
| imptiq | char(2) | NO |  | NO |  |
| impgra | char(2) | NO |  | NO |  |
| codpag | varchar(4) | NO |  |  |  |
| tipoher | char(1) | NO |  | 0 |  |
| tipclas | varchar(4) | NO |  |  |  |
| empsino | char(1) | NO |  | N |  |
| esfelec | char(1) | NO |  | N |  |
| freshas | date | NO |  | 2000-01-01 |  |
| codaux1 | varchar(10) | NO |  |  |  |
| colortit | char(2) | NO |  |  |  |
| inacon | char(1) | NO |  | N |  |
| envfele | char(1) | NO |  | N |  |
| establ | varchar(4) | NO |  |  |  |
| punemi | varchar(4) | NO |  |  |  |
| tipdoel | varchar(3) | NO |  |  |  |

**Muestras (3 filas):**

```json
[
  {
    "codcon": "S08",
    "numcon": "8",
    "descon": "FACTURA DE VENTA",
    "actcon": "SI",
    "caucon": "SI",
    "resdian": "NO",
    "codres": " ",
    "numres": " ",
    "fecres": "2016-08-13",
    "numini": "1",
    "numfin": "100",
    "numauto": "SI",
    "fecauto": "NO",
    "conres": "1",
    "avires": "0",
    "preres": "FV",
    "imptiq": "NO",
    "impgra": "NO",
    "codpag": " ",
    "tipoher": "0",
    "tipclas": "S08",
    "empsino": "N",
    "esfelec": "N",
    "freshas": "2000-01-01",
    "codaux1": "",
    "colortit": "",
    "inacon": "N",
    "envfele": "N",
    "establ": "",
    "punemi": "",
    "tipdoel": ""
  },
  {
    "codcon": "S23",
    "numcon": "23",
    "descon": "NOTA DE PRODUCCION",
    "actcon": "SI",
    "caucon": "SI",
    "resdian": "NO",
    "codres": " ",
    "numres": " ",
    "fecres": "2000-01-01",
    "numini": "1",
    "numfin": "100",
    "numauto": "SI",
    "fecauto": "NO",
    "conres": "1",
    "avires": "0",
    "preres": "NP",
    "imptiq": "NO",
    "impgra": "NO",
    "codpag": "",
    "tipoher": "0",
    "tipclas": "S23",
    "empsino": "N",
    "esfelec": "N",
    "freshas": "2000-01-01",
    "codaux1": "",
    "colortit": "",
    "inacon": "N",
    "envfele": "N",
    "establ": "",
    "punemi": "",
    "tipdoel": ""
  },
  {
    "codcon": "S28",
    "numcon": "28",
    "descon": "NOTA DE SALIDA",
    "actcon": "SI",
    "caucon": "SI",
    "resdian": "NO",
    "codres": " ",
    "numres": " ",
    "fecres": "2000-01-01",
    "numini": "1",
    "numfin": "100",
    "numauto": "SI",
    "fecauto": "NO",
    "conres": "1",
    "avires": "0",
    "preres": "SAL",
    "imptiq": "NO",
    "impgra": "NO",
    "codpag": "",
    "tipoher": "0",
    "tipclas": "S28",
    "empsino": "N",
    "esfelec": "N",
    "freshas": "2000-01-01",
    "codaux1": "",
    "colortit": "",
    "inacon": "N",
    "envfele": "N",
    "establ": "",
    "punemi": "",
    "tipdoel": ""
  }
]
```

---

## `conteoinv` (0 filas)

| Campo | Tipo | Nulo | Key | Default | Extra |
|-------|------|------|-----|---------|-------|
| numcon | varchar(20) | NO | MUL |  |  |
| codclas | varchar(4) | NO | MUL |  |  |
| nomdoc | varchar(100) | NO |  | CONTEO |  |
| precon | varchar(8) | NO |  | CON |  |
| feccon | datetime | NO |  | 2000-01-20 00:00:00 |  |
| nitter | varchar(15) | NO | MUL |  |  |
| rescon | varchar(120) | NO |  |  |  |
| obscon | varchar(400) | NO |  |  |  |
| estcon | char(1) | NO |  |  |  |
| codemp | varchar(15) | NO | MUL |  |  |
| horcon | tinyint(3) | NO |  | 1 |  |
| codres | varchar(4) | NO | MUL |  |  |
| codbod | varchar(4) | NO | MUL |  |  |
| codcos | varchar(6) | NO |  |   |  |
| veridoc | tinyint(1) | NO |  | 0 |  |
| feccrea | datetime | NO |  | 2000-01-20 00:00:00 |  |

**Muestras (3 filas):**

```json
[]
```

---

## `contperfiles` (0 filas)

| Campo | Tipo | Nulo | Key | Default | Extra |
|-------|------|------|-----|---------|-------|
| numdoc | varchar(20) | NO | MUL |  |  |
| codclas | varchar(4) | NO | MUL |  |  |
| nomdet | varchar(100) | NO |  |  |  |
| puntos | float | NO |  | 0 |  |
| orden | smallint(6) | NO |  | 0 |  |

**Muestras (3 filas):**

```json
[]
```

---

## `contratoemp` (0 filas)

| Campo | Tipo | Nulo | Key | Default | Extra |
|-------|------|------|-----|---------|-------|
| numcon | varchar(15) | NO | PRI |  |  |
| nitter | varchar(15) | NO | MUL |  |  |
| tipcon | char(1) | NO |  |  |  |
| fecini | date | NO |  | 2000-01-01 |  |
| fecfin | date | NO |  | 2000-01-01 |  |
| obscon | varchar(800) | NO |  |  |  |
| pernom | char(1) | NO |  |  |  |
| tiptrab | char(2) | NO |  |  |  |
| subtrab | char(2) | NO |  |  |  |
| altrie | char(1) | NO |  |  |  |
| salint | char(1) | NO |  |  |  |
| sueldo | double | NO |  | 0 |  |
| motret | varchar(150) | NO |  |  |  |
| nomban | varchar(150) | NO |  |  |  |
| cueban | varchar(30) | NO |  |  |  |
| tipcueb | char(1) | NO |  |  |  |
| codadm | char(3) | NO |  |  |  |
| codcar | varchar(5) | NO |  |  |  |
| nomcar | varchar(100) | NO |  |  |  |
| codcos | varchar(6) | NO |  |  |  |
| estcon | char(1) | NO |  |  |  |

**Muestras (3 filas):**

```json
[]
```

---

## `controlcafe` (0 filas)

| Campo | Tipo | Nulo | Key | Default | Extra |
|-------|------|------|-----|---------|-------|
| numdoc | varchar(20) | NO | MUL |  |  |
| codclas | varchar(4) | NO | MUL |  |  |
| nomdoc | varchar(100) | NO |  |  |  |
| predoc | varchar(8) | NO |  |  |  |
| fecdoc | date | NO |  | 2000-01-01 |  |
| estdoc | char(1) | NO |  | 1 |  |
| obsdoc | varchar(400) | NO |  |  |  |
| aprsino | char(1) | NO |  |  |  |
| sernum | varchar(40) | NO |  |  |  |
| codprod | varchar(20) | NO |  |  |  |
| nomdet | varchar(150) | NO |  |  |  |
| candet | double | NO |  | 0 |  |
| totcom | double | NO |  | 0 |  |
| numcom | varchar(20) | NO |  |  |  |
| tipclas | varchar(4) | NO |  |  |  |
| feccom | date | NO |  | 2000-01-01 |  |
| nombod | varchar(100) | NO |  |  |  |
| nitter | varchar(15) | NO | MUL |  |  |
| digter | char(2) | NO |  |  |  |
| nomter | varchar(120) | NO |  |  |  |
| telter | varchar(50) | NO |  |  |  |
| nitcat | varchar(15) | NO |  |  |  |
| nomcat | varchar(120) | NO |  |  |  |
| codemp | varchar(15) | NO |  |  |  |
| puntos | float | NO |  | 0 |  |
| muestra | double | NO |  | 0 |  |
| consfac | double | NO |  | 0 |  |
| valoat | double | NO |  | 0 |  |
| pmerma | double | NO |  | 0 |  |
| valoas | double | NO |  | 0 |  |
| valops | double | NO |  | 0 |  |
| valgr1 | double | NO |  | 0 |  |
| valgr2 | double | NO |  | 0 |  |
| broca | double | NO |  | 0 |  |
| mala15 | double | NO |  | 0 |  |
| mala14 | double | NO |  | 0 |  |
| mala13 | double | NO |  | 0 |  |
| mala00 | double | NO |  | 0 |  |
| valohp | double | NO |  | 0 |  |

**Muestras (3 filas):**

```json
[]
```

---

## `credclaves` (0 filas)

| Campo | Tipo | Nulo | Key | Default | Extra |
|-------|------|------|-----|---------|-------|
| nitter | varchar(15) | NO | MUL |  |  |
| numdes | varchar(20) | NO |  |  |  |
| numhas | varchar(20) | NO |  |  |  |
| numcon | varchar(20) | NO |  |  |  |

**Muestras (3 filas):**

```json
[]
```

---

## `cuentacobro` (0 filas)

| Campo | Tipo | Nulo | Key | Default | Extra |
|-------|------|------|-----|---------|-------|
| numcob | varchar(20) | NO | MUL |  |  |
| nomdoc | varchar(100) | NO |  | CUENTA DE COBRO |  |
| precob | varchar(8) | NO |  | CE |  |
| feccob | datetime | NO |  | 2000-01-20 00:00:00 |  |
| nitter | varchar(15) | NO | MUL |  |  |
| digver | char(2) | NO |  |  |  |
| nomter | varchar(120) | NO |  |  |  |
| dirter | varchar(100) | NO |  |  |  |
| telter | varchar(50) | NO |  |  |  |
| obscob | varchar(400) | NO |  |  |  |
| estcob | char(1) | NO |  |  |  |
| codemp | varchar(15) | NO | MUL |  |  |
| horcob | tinyint(3) | NO |  | 1 |  |
| codres | varchar(4) | NO | MUL |  |  |
| codclas | varchar(4) | NO | MUL |  |  |

**Muestras (3 filas):**

```json
[]
```

---

## `cuentaspuc` (2720 filas)

| Campo | Tipo | Nulo | Key | Default | Extra |
|-------|------|------|-----|---------|-------|
| codcue | varchar(20) | NO | PRI |  |  |
| nomcue | varchar(150) | NO |  |  |  |
| tipo | char(10) | NO |  |  |  |
| natcue | char(1) | NO |  |  |  |
| reqter | char(2) | NO |  |  |  |
| codtip | char(3) | NO | MUL |  |  |
| porimp | float | NO |  | 0 |  |
| codrub | varchar(35) | NO | MUL |  |  |
| nitter | varchar(15) | NO | MUL |  |  |
| tipniif | char(1) | NO |  |  |  |
| codniif | varchar(20) | NO |  |  |  |
| acusals | char(1) | NO |  |  |  |
| presud | char(1) | NO |  |  |  |
| presuc | char(1) | NO |  |  |  |
| codgru | char(2) | NO |  |  |  |
| corrie | char(1) | NO |  |  |  |
| codban | varchar(8) | NO |  |  |  |
| cueban | varchar(20) | NO |  |  |  |
| codfuen | varchar(4) | NO |  |  |  |

**Muestras (3 filas):**

```json
[
  {
    "codcue": "120510",
    "nomcue": "Pesca",
    "tipo": "DAUXILIAR",
    "natcue": "D",
    "reqter": "",
    "codtip": "",
    "porimp": "0.0",
    "codrub": "",
    "nitter": "",
    "tipniif": "",
    "codniif": "",
    "acusals": "",
    "presud": "",
    "presuc": "",
    "codgru": "",
    "corrie": "",
    "codban": "",
    "cueban": "",
    "codfuen": ""
  },
  {
    "codcue": "120505",
    "nomcue": "Agricultura, ganader├¡a, caza y silvicultura",
    "tipo": "DAUXILIAR",
    "natcue": "D",
    "reqter": "",
    "codtip": "",
    "porimp": "0.0",
    "codrub": "",
    "nitter": "",
    "tipniif": "",
    "codniif": "",
    "acusals": "",
    "presud": "",
    "presuc": "",
    "codgru": "",
    "corrie": "",
    "codban": "",
    "cueban": "",
    "codfuen": ""
  },
  {
    "codcue": "1205",
    "nomcue": "Acciones",
    "tipo": "CUENTA",
    "natcue": "D",
    "reqter": "",
    "codtip": "",
    "porimp": "0.0",
    "codrub": "",
    "nitter": "",
    "tipniif": "",
    "codniif": "",
    "acusals": "",
    "presud": "",
    "presuc": "",
    "codgru": "",
    "corrie": "",
    "codban": "",
    "cueban": "",
    "codfuen": ""
  }
]
```

---

## `cuentpresup` (0 filas)

| Campo | Tipo | Nulo | Key | Default | Extra |
|-------|------|------|-----|---------|-------|
| codrub | varchar(35) | NO | PRI |  |  |
| nomrub | varchar(250) | NO |  |  |  |
| tipcue | char(1) | NO |  | 1 |  |
| clascue | char(1) | NO |  |  |  |
| natcue | char(1) | NO |  |  |  |
| codsia | varchar(8) | NO |  |  |  |
| codfuen | varchar(4) | NO |  |  |  |

**Muestras (3 filas):**

```json
[]
```

---

## `despachos` (0 filas)

| Campo | Tipo | Nulo | Key | Default | Extra |
|-------|------|------|-----|---------|-------|
| numdes | varchar(20) | NO | MUL |  |  |
| codclas | varchar(4) | NO | MUL |  |  |
| nomdoc | varchar(100) | NO |  | DESPACHO |  |
| numfven | varchar(20) | NO | MUL |  |  |
| docafe | varchar(4) | NO |  |  |  |
| predes | varchar(8) | NO |  |  |  |
| fecdes | datetime | NO |  | 2000-01-20 00:00:00 |  |
| nitter | varchar(15) | NO | MUL |  |  |
| digter | char(2) | NO |  |  |  |
| nomter | varchar(120) | NO |  |  |  |
| dirter | varchar(100) | NO |  |  |  |
| telter | varchar(50) | NO |  |  |  |
| codciu | varchar(6) | NO | MUL |  |  |
| nitrec | varchar(15) | NO |  |  |  |
| obsdes | varchar(400) | NO |  |  |  |
| estdes | char(1) | NO |  |  |  |
| codemp | varchar(15) | NO | MUL |  |  |
| hordes | tinyint(3) | NO |  | 1 |  |
| codres | varchar(4) | NO | MUL |  |  |
| afebod | char(1) | NO |  | S |  |
| veides | varchar(50) | NO |  |  |  |
| plades | varchar(20) | NO |  |  |  |
| emptran | varchar(50) | NO |  |  |  |
| empcod | varchar(3) | NO |  |  |  |
| agrupa | char(1) | NO |  |  |  |
| veridoc | tinyint(1) | NO |  | 0 |  |
| feccrea | datetime | NO |  | 2000-01-20 00:00:00 |  |

**Muestras (3 filas):**

```json
[]
```

---

## `detajustes` (0 filas)

| Campo | Tipo | Nulo | Key | Default | Extra |
|-------|------|------|-----|---------|-------|
| numaju | varchar(20) | NO | MUL |  |  |
| numdoc | varchar(20) | NO | MUL |  |  |
| numcuo | tinyint(3) | NO |  | 0 |  |
| codcue | varchar(20) | NO | MUL |  |  |
| nomdet | varchar(150) | NO |  |  |  |
| valdeb | double | NO |  | 0 |  |
| valcre | double | NO |  | 0 |  |
| tipdet | varchar(10) | NO |  |  |  |
| nitter | varchar(15) | NO | MUL |  |  |
| codpag | varchar(4) | NO | MUL |  |  |
| basimp | double | NO |  | 0 |  |
| porimp | float | NO |  | 0 |  |
| valimp | double | NO |  | 0 |  |
| codcos | varchar(6) | NO | MUL |  |  |
| codprod | varchar(20) | NO | MUL |  |  |
| sernum | varchar(40) | NO |  |  |  |
| codclas | varchar(4) | NO | MUL |  |  |
| feccom | date | NO |  | 2000-01-01 |  |
| fecvence | date | NO |  | 2000-01-01 |  |
| valcom | double | NO |  | 0 |  |
| candet | double | NO |  | 0 |  |
| codbod | varchar(4) | NO |  |  |  |
| canbod | double | NO |  | 0 |  |

**Muestras (3 filas):**

```json
[]
```

---

## `detapago` (151 filas)

| Campo | Tipo | Nulo | Key | Default | Extra |
|-------|------|------|-----|---------|-------|
| numnum | varchar(20) | NO | MUL |  |  |
| codclas | varchar(4) | NO | MUL |  |  |
| predoc | varchar(8) | NO |  |  |  |
| numite | smallint(6) | NO |  | 0 |  |
| fecdoc | datetime | NO |  | 2000-01-20 00:00:00 |  |
| docodet | tinyint(3) | NO |  | 0 |  |
| valpag | double | NO |  | 0 |  |
| valefe | double | NO |  | 0 |  |
| despag | varchar(100) | NO |  |  |  |
| numpag | varchar(20) | NO |  |  |  |
| fecche | date | NO |  | 2000-01-20 |  |
| numapr | varchar(20) | NO |  |  |  |
| soldeb | double | NO |  | 0 |  |
| solcre | double | NO |  | 0 |  |
| codpag | varchar(4) | NO | MUL |  |  |
| afepag | tinyint(3) | NO |  | 0 |  |
| codban | varchar(8) | NO | MUL |  |  |
| codtar | varchar(4) | NO | MUL |  |  |
| estado | char(1) | NO |  | B |  |
| tipcmen | char(1) | NO |  |  |  |
| nitter | varchar(15) | NO | MUL |  |  |
| codemp | varchar(15) | NO |  |  |  |
| codcaj | varchar(4) | NO |  |  |  |
| turno1 | char(1) | NO |  | 0 |  |
| fecven | date | NO |  | 2000-01-01 |  |

**Muestras (3 filas):**

```json
[
  {
    "numnum": "1",
    "codclas": "S18",
    "predoc": "COM",
    "numite": "0",
    "fecdoc": "2026-05-17 18:57:50",
    "docodet": "0",
    "valpag": "668400.0",
    "valefe": "0.0",
    "despag": "",
    "numpag": "",
    "fecche": "2026-05-24",
    "numapr": " ",
    "soldeb": "0.0",
    "solcre": "668400.0",
    "codpag": "F07",
    "afepag": "21",
    "codban": "",
    "codtar": " ",
    "estado": "B",
    "tipcmen": "",
    "nitter": "900778480",
    "codemp": "1151970853",
    "codcaj": "",
    "turno1": "0",
    "fecven": "2026-05-17"
  },
  {
    "numnum": "2",
    "codclas": "S18",
    "predoc": "COM",
    "numite": "0",
    "fecdoc": "2026-05-20 19:52:42",
    "docodet": "0",
    "valpag": "288660.0",
    "valefe": "0.0",
    "despag": "",
    "numpag": "",
    "fecche": "2026-05-24",
    "numapr": " ",
    "soldeb": "0.0",
    "solcre": "288660.0",
    "codpag": "F07",
    "afepag": "21",
    "codban": "",
    "codtar": " ",
    "estado": "B",
    "tipcmen": "",
    "nitter": "11111",
    "codemp": "1151970853",
    "codcaj": "",
    "turno1": "0",
    "fecven": "2026-05-20"
  },
  {
    "numnum": "3",
    "codclas": "S18",
    "predoc": "COM",
    "numite": "0",
    "fecdoc": "2026-05-17 20:29:04",
    "docodet": "0",
    "valpag": "190010.0",
    "valefe": "0.0",
    "despag": "",
    "numpag": "",
    "fecche": "2026-05-24",
    "numapr": " ",
    "soldeb": "0.0",
    "solcre": "190010.0",
    "codpag": "F07",
    "afepag": "21",
    "codban": "",
    "codtar": " ",
    "estado": "B",
    "tipcmen": "",
    "nitter": "901472390",
    "codemp": "1151970853",
    "codcaj": "",
    "turno1": "0",
    "fecven": "2026-05-17"
  }
]
```

---

## `detbodegas` (0 filas)

| Campo | Tipo | Nulo | Key | Default | Extra |
|-------|------|------|-----|---------|-------|
| numnum | varchar(20) | NO | MUL |  |  |
| codclas | varchar(4) | NO | MUL |  |  |
| fecdoc | datetime | NO |  | 2000-01-20 00:00:00 |  |
| fecdet | datetime | NO |  | 2000-01-20 00:00:00 |  |
| codprod | varchar(20) | NO | MUL |  |  |
| nomdet | varchar(300) | NO |  |  |  |
| candet | double | NO |  | 0 |  |
| valuni | double | NO |  | 0 |  |
| sernum | varchar(40) | NO |  |  |  |
| serfec | varchar(10) | NO |  |  |  |
| obsdet | varchar(400) | NO |  |  |  |
| codbod | varchar(4) | NO | MUL |  |  |
| numite | smallint(6) | NO |  | 1 |  |
| estdoc | char(1) | NO |  |  |  |
| codmed | varchar(3) | NO | MUL |  |  |
| divmul | char(1) | NO |  | M |  |
| facumed | double | NO |  | 1 |  |
| tipdet | char(2) | NO |  |  |  |
| salant | double | NO |  | 0 |  |
| salnue | double | NO |  | 0 |  |
| iterel | smallint(6) | NO |  | 0 |  |
| cruclas | varchar(4) | NO |  |  |  |
| crunum | varchar(20) | NO |  |  |  |
| bodori | varchar(4) | NO | MUL |  |  |
| pesodet | double | NO |  | 0 |  |

**Muestras (3 filas):**

```json
[]
```

---

## `detcajarq` (0 filas)

| Campo | Tipo | Nulo | Key | Default | Extra |
|-------|------|------|-----|---------|-------|
| numarq | varchar(20) | NO | MUL |  |  |
| codclas | varchar(4) | NO | MUL |  |  |
| denarq | double | NO |  | 0 |  |
| cantden | smallint(6) | NO |  | 1 |  |
| tipdet | varchar(30) | NO |  |  |  |
| bandes | varchar(150) | NO |  |  |  |
| numche | varchar(30) | NO |  |  |  |
| tiparq | char(1) | NO |  |  |  |

**Muestras (3 filas):**

```json
[]
```

---

## `detcompras` (572 filas)

| Campo | Tipo | Nulo | Key | Default | Extra |
|-------|------|------|-----|---------|-------|
| numcom | varchar(20) | NO | MUL |  |  |
| codclas | varchar(4) | NO | MUL |  |  |
| codprod | varchar(20) | NO | MUL |  |  |
| nomdet | varchar(300) | NO |  |  |  |
| candet | double | NO |  | 0 |  |
| valuni | double | NO |  | 0 |  |
| dctpor | float | NO |  | 0 |  |
| dctpes | double | NO |  | 0 |  |
| ivapor | float | NO |  | 0 |  |
| ivapes | double | NO |  | 0 |  |
| ipopor | float | NO |  | 0 |  |
| ipopes | double | NO |  | 0 |  |
| totdet | double | NO |  | 0 |  |
| obsdet | varchar(400) | NO |  |  |  |
| cosprod | double | NO |  | 0 |  |
| sernum | varchar(40) | NO |  |  |  |
| serfec | varchar(10) | NO |  |  |  |
| tipdet | char(2) | NO |  | P |  |
| codpor | varchar(4) | NO | MUL | 0 |  |
| codpor2 | varchar(4) | NO |  | 0 |  |
| codbod | varchar(4) | NO | MUL |  |  |
| codcos | varchar(6) | NO | MUL |  |  |
| codmed | varchar(3) | NO | MUL |  |  |
| divmul | char(1) | NO |  | M |  |
| facumed | double | NO |  | 1 |  |
| numite | smallint(6) | NO |  | 1 |  |
| iterel | smallint(6) | NO |  | 0 |  |
| cruclas | varchar(4) | NO |  |   |  |
| crunum | varchar(20) | NO |  |   |  |
| tipipo | varchar(2) | NO |  |  |  |
| nitfor | varchar(15) | NO | MUL |  |  |
| horini | datetime | NO |  | 2000-01-01 00:00:00 |  |
| horfin | datetime | NO |  | 2000-01-01 00:00:00 |  |
| multiplo | double | NO |  | 1 |  |
| nomtec | varchar(120) | NO |  |  |  |
| factpor | float | NO |  | 0 |  |
| prbase | double | NO |  | 0 |  |
| tiesub | char(1) | NO |  |  |  |

**Muestras (3 filas):**

```json
[
  {
    "numcom": "1",
    "codclas": "S18",
    "codprod": "7503008669079",
    "nomdet": "ACEITE DE COCO VIRGEN ORG├üNICO X 300 ML",
    "candet": "3.0",
    "valuni": "56292.0",
    "dctpor": "0.0",
    "dctpes": "0.0",
    "ivapor": "0.0",
    "ivapes": "0.0",
    "ipopor": "0.0",
    "ipopes": "0.0",
    "totdet": "168876.0",
    "obsdet": "",
    "cosprod": "56292.0",
    "sernum": "",
    "serfec": "",
    "tipdet": "P",
    "codpor": "IV2",
    "codpor2": " ",
    "codbod": "BD01",
    "codcos": "",
    "codmed": "",
    "divmul": "",
    "facumed": "1.0",
    "numite": "1",
    "iterel": "0",
    "cruclas": "",
    "crunum": "",
    "tipipo": "",
    "nitfor": "",
    "horini": "2000-01-01 00:00:00",
    "horfin": "2000-01-01 00:00:00",
    "multiplo": "1.0",
    "nomtec": "",
    "factpor": "0.0",
    "prbase": "0.0",
    "tiesub": ""
  },
  {
    "numcom": "1",
    "codclas": "S18",
    "codprod": "7503008669062",
    "nomdet": "ACEITE DE COCO VIRGEN CONVENCIONAL X 300 ML",
    "candet": "3.0",
    "valuni": "44228.0",
    "dctpor": "0.0",
    "dctpes": "0.0",
    "ivapor": "0.0",
    "ivapes": "0.0",
    "ipopor": "0.0",
    "ipopes": "0.0",
    "totdet": "132684.0",
    "obsdet": "",
    "cosprod": "44228.0",
    "sernum": "",
    "serfec": "",
    "tipdet": "P",
    "codpor": "IV2",
    "codpor2": " ",
    "codbod": "BD01",
    "codcos": "",
    "codmed": "",
    "divmul": "",
    "facumed": "1.0",
    "numite": "2",
    "iterel": "0",
    "cruclas": "",
    "crunum": "",
    "tipipo": "",
    "nitfor": "",
    "horini": "2000-01-01 00:00:00",
    "horfin": "2000-01-01 00:00:00",
    "multiplo": "1.0",
    "nomtec": "",
    "factpor": "0.0",
    "prbase": "0.0",
    "tiesub": ""
  },
  {
    "numcom": "1",
    "codclas": "S18",
    "codprod": "7503008669147",
    "nomdet": "AGUA DE COCO 100% NATURAL X 1 L",
    "candet": "6.0",
    "valuni": "23130.0",
    "dctpor": "0.0",
    "dctpes": "0.0",
    "ivapor": "0.0",
    "ivapes": "0.0",
    "ipopor": "0.0",
    "ipopes": "0.0",
    "totdet": "138780.0",
    "obsdet": "",
    "cosprod": "23130.0",
    "sernum": "",
    "serfec": "",
    "tipdet": "P",
    "codpor": "IV2",
    "codpor2": " ",
    "codbod": "BD01",
    "codcos": "",
    "codmed": "",
    "divmul": "",
    "facumed": "1.0",
    "numite": "3",
    "iterel": "0",
    "cruclas": "",
    "crunum": "",
    "tipipo": "",
    "nitfor": "",
    "horini": "2000-01-01 00:00:00",
    "horfin": "2000-01-01 00:00:00",
    "multiplo": "1.0",
    "nomtec": "",
    "factpor": "0.0",
    "prbase": "0.0",
    "tiesub": ""
  }
]
```

---

## `detconteoinv` (0 filas)

| Campo | Tipo | Nulo | Key | Default | Extra |
|-------|------|------|-----|---------|-------|
| numcon | varchar(20) | NO | MUL |  |  |
| codprod | varchar(20) | NO | MUL |  |  |
| sernum | varchar(40) | NO |  |  |  |
| nomdet | varchar(300) | NO |  |  |  |
| cosuni | double | NO |  | 0 |  |
| exiant | double | NO |  | 0 |  |
| candet | double | NO |  | 0 |  |
| obsdet | varchar(300) | NO |  |  |  |
| codclas | varchar(4) | NO | MUL |  |  |

**Muestras (3 filas):**

```json
[]
```

---

## `detcuecobro` (0 filas)

| Campo | Tipo | Nulo | Key | Default | Extra |
|-------|------|------|-----|---------|-------|
| numcob | varchar(20) | NO | MUL |  |  |
| nomdet | varchar(300) | NO |  |  |  |
| valdet | double | NO |  | 0 |  |
| codclas | char(4) | NO | MUL |  |  |

**Muestras (3 filas):**

```json
[]
```

---

## `detcuentas` (2282 filas)

| Campo | Tipo | Nulo | Key | Default | Extra |
|-------|------|------|-----|---------|-------|
| numnum | varchar(20) | NO | MUL |  |  |
| codclas | varchar(4) | NO | MUL |  |  |
| prenum | varchar(8) | NO |  |  |  |
| codcue | varchar(20) | NO | MUL |  |  |
| detcue | varchar(150) | NO |  |  |  |
| valdeb | double | NO |  | 0 |  |
| valhab | double | NO |  | 0 |  |
| fecdoc | datetime | NO | MUL | 2000-01-20 00:00:00 |  |
| nitter | varchar(15) | NO | MUL |  |  |
| condoc | char(2) | NO |  | NO |  |
| codemp | varchar(15) | NO | MUL |  |  |
| codcos | varchar(6) | NO | MUL |  |  |
| numite | smallint(6) | NO |  | 1 |  |
| estcue | char(1) | NO |  | B |  |
| codbod | varchar(4) | NO | MUL |  |  |
| codprod | varchar(20) | NO | MUL |  |  |
| candet | double | NO |  | 0 |  |
| sernum | varchar(40) | NO | MUL |  |  |
| serfec | varchar(10) | NO |  |  |  |
| cansal | char(1) | NO |  |  |  |
| escost | char(1) | NO |  |  |  |
| empcod | varchar(3) | NO | MUL |  |  |
| valdet | double | NO |  | 0 |  |
| codpag | varchar(4) | NO | MUL |  |  |
| tipdet | char(2) | NO |  |  |  |
| codsuc | varchar(15) | NO | MUL |  |  |
| docafe | varchar(20) | NO | MUL |  |  |
| preafe | varchar(8) | NO |  |  |  |
| numcuo | smallint(6) | NO |  | 0 |  |
| clasafe | varchar(4) | NO | MUL |  |  |
| fecuno | date | NO |  | 2010-01-01 |  |
| fecves | date | NO |  | 2010-01-01 |  |
| docext | varchar(20) | NO |  |  |  |
| valafe | double | NO |  | 0 |  |
| nitaux | varchar(15) | NO |  |  |  |
| afepag | tinyint(3) | NO |  | 0 |  |
| valimp | double | NO |  | 0 |  |
| basimp | double | NO |  | 0 |  |
| porimp | float | NO |  | 0 |  |
| docodet | char(1) | NO |  |  |  |
| numit2 | smallint(6) | NO |  | 0 |  |
| banotar | varchar(100) | NO |  |  |  |
| numche | varchar(20) | NO |  |  |  |
| numapr | varchar(20) | NO |  |  |  |
| fecche | date | NO |  | 2000-01-01 |  |
| escrea | char(1) | NO |  |  |  |
| concili | char(1) | NO |  |  |  |
| ivacos | double | NO |  | 0 |  |
| verific | char(1) | NO |  |  |  |
| factpor | float | NO |  | 0 |  |
| agrupa | char(1) | NO |  |  |  |
| nitnomi | varchar(15) | NO |  |  |  |
| numcru | varchar(20) | NO | MUL |  |  |
| intmor | float | NO |  | 0 |  |
| pordct | float | NO |  | 0 |  |
| caufin | char(2) | NO |  | NO |  |
| valint | double | NO |  | 0 |  |
| valseg | double | NO |  | 0 |  |
| valotr | double | NO |  | 0 |  |
| tipdfac | char(2) | NO |  |  |  |

**Muestras (3 filas):**

```json
[
  {
    "numnum": "1",
    "codclas": "S18",
    "prenum": "COM",
    "codcue": "14350101",
    "detcue": "ACEITE DE COCO VIRGEN ORG├üNICO X 300 ML",
    "valdeb": "168876.0",
    "valhab": "0.0",
    "fecdoc": "2026-05-17 00:02:01",
    "nitter": "900778480",
    "condoc": "NO",
    "codemp": "1151970853",
    "codcos": "",
    "numite": "1",
    "estcue": "B",
    "codbod": "BD01",
    "codprod": "7503008669079",
    "candet": "3.0",
    "sernum": "",
    "serfec": "",
    "cansal": "",
    "escost": "",
    "empcod": "",
    "valdet": "56292.0",
    "codpag": " ",
    "tipdet": "",
    "codsuc": "",
    "docafe": " ",
    "preafe": " ",
    "numcuo": "0",
    "clasafe": "",
    "fecuno": "2026-05-17",
    "fecves": "2026-05-17",
    "docext": "62018",
    "valafe": "0.0",
    "nitaux": "",
    "afepag": "0",
    "valimp": "0.0",
    "basimp": "0.0",
    "porimp": "0.0",
    "docodet": "",
    "numit2": "0",
    "banotar": "",
    "numche": "",
    "numapr": "",
    "fecche": "2026-05-17",
    "escrea": "",
    "concili": "",
    "ivacos": "0.0",
    "verific": "",
    "factpor": "0.0",
    "agrupa": "",
    "nitnomi": "",
    "numcru": "",
    "intmor": "0.0",
    "pordct": "0.0",
    "caufin": "NO",
    "valint": "0.0",
    "valseg": "0.0",
    "valotr": "0.0",
    "tipdfac": ""
  },
  {
    "numnum": "1",
    "codclas": "S18",
    "prenum": "COM",
    "codcue": "24080202",
    "detcue": "IVA descontable excluido",
    "valdeb": "0.0",
    "valhab": "0.0",
    "fecdoc": "2026-05-17 18:57:50",
    "nitter": "900778480",
    "condoc": "NO",
    "codemp": "1151970853",
    "codcos": "",
    "numite": "2",
    "estcue": "B",
    "codbod": "",
    "codprod": "",
    "candet": "0.0",
    "sernum": "",
    "serfec": "",
    "cansal": "",
    "escost": "",
    "empcod": "",
    "valdet": "0.0",
    "codpag": "",
    "tipdet": "",
    "codsuc": "",
    "docafe": "",
    "preafe": "",
    "numcuo": "0",
    "clasafe": "",
    "fecuno": "2026-05-17",
    "fecves": "2026-05-17",
    "docext": "62018",
    "valafe": "0.0",
    "nitaux": "",
    "afepag": "0",
    "valimp": "0.0",
    "basimp": "168876.0",
    "porimp": "0.0",
    "docodet": "",
    "numit2": "0",
    "banotar": "",
    "numche": "",
    "numapr": "",
    "fecche": "2026-05-17",
    "escrea": "",
    "concili": "",
    "ivacos": "0.0",
    "verific": "",
    "factpor": "0.0",
    "agrupa": "",
    "nitnomi": "",
    "numcru": "",
    "intmor": "0.0",
    "pordct": "0.0",
    "caufin": "NO",
    "valint": "0.0",
    "valseg": "0.0",
    "valotr": "0.0",
    "tipdfac": ""
  },
  {
    "numnum": "1",
    "codclas": "S18",
    "prenum": "COM",
    "codcue": "14350101",
    "detcue": "ACEITE DE COCO VIRGEN CONVENCIONAL X 300 ML",
    "valdeb": "132684.0",
    "valhab": "0.0",
    "fecdoc": "2026-05-17 00:02:01",
    "nitter": "900778480",
    "condoc": "NO",
    "codemp": "1151970853",
    "codcos": "",
    "numite": "3",
    "estcue": "B",
    "codbod": "BD01",
    "codprod": "7503008669062",
    "candet": "3.0",
    "sernum": "",
    "serfec": "",
    "cansal": "",
    "escost": "",
    "empcod": "",
    "valdet": "44228.0",
    "codpag": " ",
    "tipdet": "",
    "codsuc": "",
    "docafe": " ",
    "preafe": " ",
    "numcuo": "0",
    "clasafe": "",
    "fecuno": "2026-05-17",
    "fecves": "2026-05-17",
    "docext": "62018",
    "valafe": "0.0",
    "nitaux": "",
    "afepag": "0",
    "valimp": "0.0",
    "basimp": "0.0",
    "porimp": "0.0",
    "docodet": "",
    "numit2": "0",
    "banotar": "",
    "numche": "",
    "numapr": "",
    "fecche": "2026-05-17",
    "escrea": "",
    "concili": "",
    "ivacos": "0.0",
    "verific": "",
    "factpor": "0.0",
    "agrupa": "",
    "nitnomi": "",
    "numcru": "",
    "intmor": "0.0",
    "pordct": "0.0",
    "caufin": "NO",
    "valint": "0.0",
    "valseg": "0.0",
    "valotr": "0.0",
    "tipdfac": ""
  }
]
```

---

## `detdespachos` (0 filas)

| Campo | Tipo | Nulo | Key | Default | Extra |
|-------|------|------|-----|---------|-------|
| numdes | varchar(20) | NO | MUL |  |  |
| codclas | varchar(4) | NO | MUL |  |  |
| codprod | varchar(20) | NO | MUL |  |  |
| iterel | smallint(6) | NO |  | 0 |  |
| sernum | varchar(40) | NO |  |  |  |
| nomdet | varchar(300) | NO |  |  |  |
| candet | double | NO |  | 0 |  |
| valuni | double | NO |  | 0 |  |
| codbod | varchar(4) | NO | MUL |  |  |
| numite | smallint(6) | NO |  | 1 |  |
| tiesub | char(1) | NO |  |  |  |
| serfec | varchar(10) | NO |  |  |  |
| codcos | varchar(6) | NO |  |   |  |
| cruclas | varchar(4) | NO |  |  |  |
| crunum | varchar(20) | NO |  |  |  |
| codmed | varchar(3) | NO | MUL |  |  |
| divmul | char(1) | NO |  | M |  |
| facumed | double | NO |  | 1 |  |
| canreal | double | NO |  | 0 |  |

**Muestras (3 filas):**

```json
[]
```

---

## `detentsalida` (0 filas)

| Campo | Tipo | Nulo | Key | Default | Extra |
|-------|------|------|-----|---------|-------|
| nument | varchar(20) | NO | MUL |  |  |
| codclas | varchar(4) | NO | MUL |  |  |
| codprod | varchar(20) | NO | MUL |  |  |
| sernum | varchar(40) | NO |  |  |  |
| nomdet | varchar(300) | NO |  |  |  |
| cosuni | double | NO |  | 0 |  |
| candet | double | NO |  | 0 |  |
| totdet | double | NO |  | 0 |  |
| obsdet | varchar(300) | NO |  |  |  |
| tipdet | char(1) | NO |  |  |  |
| codbod | varchar(4) | NO | MUL |  |  |
| numite | smallint(6) | NO |  | 1 |  |
| serfec | varchar(10) | NO |  |  |  |
| codcue | varchar(20) | NO | MUL |  |  |
| codcu2 | varchar(20) | NO |  |  |  |
| factpor | float | NO |  | 0 |  |
| codmed | varchar(3) | NO | MUL |  |  |
| divmul | char(1) | NO |  | M |  |
| facumed | double | NO |  | 1 |  |

**Muestras (3 filas):**

```json
[]
```

---

## `detfinancia` (0 filas)

| Campo | Tipo | Nulo | Key | Default | Extra |
|-------|------|------|-----|---------|-------|
| numfin | varchar(20) | NO | MUL |  |  |
| numcuo | tinyint(3) | NO |  | 0 |  |
| fecven | date | NO |  | 2000-01-20 |  |
| salcre | double | NO |  | 0 |  |
| intere | double | NO |  | 0 |  |
| capital | double | NO |  | 0 |  |
| nuesal | double | NO |  | 0 |  |
| valcuo | double | NO |  | 0 |  |
| valcomi | double | NO |  | 0 |  |
| ivacuo | float | NO |  | 0 |  |
| valiva | double | NO |  | 0 |  |
| valseg | double | NO |  | 0 |  |
| codclas | varchar(4) | NO | MUL |  |  |

**Muestras (3 filas):**

```json
[]
```

---

## `detfvensub` (0 filas)

| Campo | Tipo | Nulo | Key | Default | Extra |
|-------|------|------|-----|---------|-------|
| numnum | varchar(20) | NO | MUL |  |  |
| codclas | varchar(4) | NO | MUL |  |  |
| codprod | varchar(20) | NO | MUL |  |  |
| codbod | varchar(4) | NO | MUL |  |  |
| candet | double | NO |  | 0 |  |
| cosprod | double | NO |  | 0 |  |
| numite | smallint(6) | NO |  | 0 |  |
| codcos | varchar(6) | NO |  |   |  |
| codmed | varchar(3) | NO | MUL |  |  |
| divmul | char(1) | NO |  | M |  |
| facumed | double | NO |  | 1 |  |
| sernum | varchar(40) | NO |  |  |  |
| serfec | varchar(10) | NO |  |  |  |

**Muestras (3 filas):**

```json
[]
```

---

## `detfventas` (245 filas)

| Campo | Tipo | Nulo | Key | Default | Extra |
|-------|------|------|-----|---------|-------|
| numfven | varchar(20) | NO | MUL |  |  |
| codclas | varchar(4) | NO | MUL |  |  |
| codprod | varchar(20) | NO | MUL |  |  |
| nomdet | varchar(300) | NO |  |  |  |
| candet | double | NO |  | 0 |  |
| valuni | double | NO |  | 0 |  |
| dctpor | float | NO |  | 0 |  |
| dctpes | double | NO |  | 0 |  |
| ivapor | float | NO |  | 0 |  |
| ivapes | double | NO |  | 0 |  |
| ipopor | float | NO |  | 0 |  |
| ipopes | double | NO |  | 0 |  |
| totdet | double | NO |  | 0 |  |
| cosprod | double | NO |  | 0 |  |
| sernum | varchar(40) | NO |  |  |  |
| serfec | varchar(10) | NO |  |  |  |
| obsdet | varchar(200) | NO |  |  |  |
| tipdet | char(2) | NO |  | P |  |
| codpor | varchar(4) | NO | MUL | 0 |  |
| codpor2 | varchar(4) | NO |  | 0 |  |
| codcos | varchar(6) | NO | MUL |  |  |
| codbod | varchar(4) | NO | MUL |  |  |
| codmed | varchar(3) | NO | MUL |  |  |
| divmul | char(1) | NO |  | M |  |
| facumed | double | NO |  | 1 |  |
| presdet | varchar(100) | NO |  |  |  |
| devcam | char(2) | NO |  | NO |  |
| numite | smallint(6) | NO |  | 1 |  |
| iterel | smallint(6) | NO |  | 0 |  |
| cruclas | varchar(4) | NO | MUL |  |  |
| crunum | varchar(20) | NO | MUL |  |  |
| tipipo | varchar(2) | NO |  |  |  |
| tiesub | char(1) | NO |  |  |  |
| puntos | double | NO |  | 0 |  |
| grudet | varchar(1) | NO |  |  |  |
| nitfor | varchar(15) | NO | MUL |  |  |
| aplcomi | char(1) | NO |  | N |  |
| porcomi | float | NO |  | 0 |  |

**Muestras (3 filas):**

```json
[
  {
    "numfven": "1",
    "codclas": "S15",
    "codprod": "SANTO0007",
    "nomdet": "CHONAS ARTESANALES X 500 g",
    "candet": "1.0",
    "valuni": "34000.0",
    "dctpor": "0.0",
    "dctpes": "0.0",
    "ivapor": "0.0",
    "ivapes": "0.0",
    "ipopor": "0.0",
    "ipopes": "0.0",
    "totdet": "34000.0",
    "cosprod": "27420.0",
    "sernum": "",
    "serfec": "",
    "obsdet": "",
    "tipdet": "P",
    "codpor": "IV2",
    "codpor2": "",
    "codcos": "",
    "codbod": "BD01",
    "codmed": "001",
    "divmul": "",
    "facumed": "1.0",
    "presdet": "",
    "devcam": "NO",
    "numite": "1",
    "iterel": "0",
    "cruclas": "",
    "crunum": "",
    "tipipo": "NO",
    "tiesub": "A",
    "puntos": "0.0",
    "grudet": "",
    "nitfor": " ",
    "aplcomi": "N",
    "porcomi": "0.0"
  },
  {
    "numfven": "2",
    "codclas": "S15",
    "codprod": "MILDA0012",
    "nomdet": "MINI TORTA COCO",
    "candet": "1.0",
    "valuni": "5300.0",
    "dctpor": "0.0",
    "dctpes": "0.0",
    "ivapor": "0.0",
    "ivapes": "0.0",
    "ipopor": "0.0",
    "ipopes": "0.0",
    "totdet": "5300.0",
    "cosprod": "5000.0",
    "sernum": "",
    "serfec": "",
    "obsdet": "",
    "tipdet": "P",
    "codpor": "IV2",
    "codpor2": "",
    "codcos": "",
    "codbod": "BD01",
    "codmed": "001",
    "divmul": "",
    "facumed": "1.0",
    "presdet": "",
    "devcam": "NO",
    "numite": "1",
    "iterel": "0",
    "cruclas": "",
    "crunum": "",
    "tipipo": "NO",
    "tiesub": "A",
    "puntos": "0.0",
    "grudet": "",
    "nitfor": " ",
    "aplcomi": "N",
    "porcomi": "0.0"
  },
  {
    "numfven": "2",
    "codclas": "S15",
    "codprod": "MILDA0008",
    "nomdet": "MINI TORTA NARANJA",
    "candet": "1.0",
    "valuni": "5300.0",
    "dctpor": "0.0",
    "dctpes": "0.0",
    "ivapor": "0.0",
    "ivapes": "0.0",
    "ipopor": "0.0",
    "ipopes": "0.0",
    "totdet": "5300.0",
    "cosprod": "5000.0",
    "sernum": "",
    "serfec": "",
    "obsdet": "",
    "tipdet": "P",
    "codpor": "IV2",
    "codpor2": "",
    "codcos": "",
    "codbod": "BD01",
    "codmed": "001",
    "divmul": "",
    "facumed": "1.0",
    "presdet": "",
    "devcam": "NO",
    "numite": "2",
    "iterel": "0",
    "cruclas": "",
    "crunum": "",
    "tipipo": "NO",
    "tiesub": "A",
    "puntos": "0.0",
    "grudet": "",
    "nitfor": " ",
    "aplcomi": "N",
    "porcomi": "0.0"
  }
]
```

---

## `detimpuestos` (4 filas)

| Campo | Tipo | Nulo | Key | Default | Extra |
|-------|------|------|-----|---------|-------|
| codpor | varchar(4) | NO | PRI | 0 |  |
| codimp | char(3) | NO |  | 0 |  |
| poroval | varchar(2) | NO |  | SI |  |
| porimp | float | NO |  | 0 |  |
| valfij | double | NO |  | 0 |  |
| despor | varchar(50) | NO |  |  |  |
| codaux1 | varchar(10) | NO |  |  |  |
| sigla | varchar(4) | NO |  |  |  |
| inaimp | char(1) | NO |  | N |  |
| codele | char(2) | NO |  | 01 |  |
| tipimp | varchar(2) | NO |  | 01 |  |

**Muestras (3 filas):**

```json
[
  {
    "codpor": "IV1",
    "codimp": "IVA",
    "poroval": "SI",
    "porimp": "0.0",
    "valfij": "0.0",
    "despor": "EXENTO",
    "codaux1": "",
    "sigla": "IVA",
    "inaimp": "N",
    "codele": "01",
    "tipimp": "02"
  },
  {
    "codpor": "IV4",
    "codimp": "IVA",
    "poroval": "SI",
    "porimp": "0.0",
    "valfij": "0.0",
    "despor": "SIN IVA",
    "codaux1": "",
    "sigla": "IVA",
    "inaimp": "N",
    "codele": "01",
    "tipimp": "01"
  },
  {
    "codpor": "IV2",
    "codimp": "IVA",
    "poroval": "SI",
    "porimp": "0.0",
    "valfij": "0.0",
    "despor": "EXCLUIDO",
    "codaux1": "",
    "sigla": "IVA",
    "inaimp": "N",
    "codele": "01",
    "tipimp": "03"
  }
]
```

---

## `detlistempaq` (0 filas)

| Campo | Tipo | Nulo | Key | Default | Extra |
|-------|------|------|-----|---------|-------|
| numlis | varchar(20) | NO | MUL |  |  |
| codclas | varchar(4) | NO | MUL |  |  |
| tipguia | varchar(150) | NO |  |  |  |
| canguia | double | NO |  | 0 |  |
| numguia | varchar(20) | NO |  | 0 |  |
| conguia | varchar(150) | NO |  |  |  |
| dimguia | varchar(100) | NO |  |  |  |
| pesguia | float | NO |  | 0 |  |
| natguia | varchar(15) | NO |  |  |  |

**Muestras (3 filas):**

```json
[]
```

---

## `detnomiele` (0 filas)

| Campo | Tipo | Nulo | Key | Default | Extra |
|-------|------|------|-----|---------|-------|
| numnom | varchar(20) | NO | MUL |  |  |
| codclas | varchar(4) | NO | MUL |  |  |
| codcon | varchar(4) | NO | MUL |  |  |
| codnel1 | varchar(2) | NO |  |  |  |
| codnel2 | varchar(2) | NO |  |  |  |
| devded | char(1) | NO |  | 1 |  |
| nitter | varchar(15) | NO | MUL |  |  |
| codadm | char(3) | NO |  |  |  |
| nomcon | varchar(150) | NO |  |  |  |
| fecini | varchar(20) | NO |  |  |  |
| fecfin | varchar(20) | NO |  |  |  |
| candet | int(6) | NO |  | 0 |  |
| pordet | float | NO |  | 0 |  |
| valdve | double | NO |  | 0 |  |
| valddu | double | NO |  | 0 |  |
| valor1 | double | NO |  | 0 |  |
| valbas | double | NO |  | 0 |  |
| desdet | varchar(250) | NO |  |  |  |
| numite | smallint(6) | NO |  | 1 |  |
| codcue | varchar(20) | NO |  |  |  |
| docafe | varchar(20) | NO |  |  |  |
| numcuo | tinyint(3) | NO |  | 0 |  |
| clasafe | varchar(4) | NO |  |  |  |
| preafe | varchar(8) | NO |  |  |  |
| afepag | tinyint(3) | NO |  | 0 |  |
| codcos | varchar(6) | NO | MUL |  |  |

**Muestras (3 filas):**

```json
[]
```

---

## `detnomina` (0 filas)

| Campo | Tipo | Nulo | Key | Default | Extra |
|-------|------|------|-----|---------|-------|
| numnom | varchar(20) | NO | MUL |  |  |
| codcue | varchar(20) | NO | MUL |  |  |
| detdeb | varchar(150) | NO |  |  |  |
| cuecre | varchar(20) | NO | MUL |  |  |
| nomdet | varchar(150) | NO |  |  |  |
| nitter | varchar(15) | NO | MUL |  |  |
| suebas | double | NO |  | 0 |  |
| candet | int(11) | NO |  | 0 |  |
| meddet | varchar(5) | NO |  |  |  |
| valuni | double | NO |  | 0 |  |
| codtip | char(3) | NO | MUL |  |  |
| valdev | double | NO |  | 0 |  |
| valded | double | NO |  | 0 |  |
| codcos | varchar(6) | NO | MUL |  |  |
| tipdet | char(4) | NO |  | DEV |  |
| basimp | double | NO |  | 0 |  |
| porimp | float | NO |  | 0 |  |
| numcom | varchar(20) | NO |  |  |  |
| docafe | varchar(20) | NO |  |  |  |
| numcuo | tinyint(3) | NO |  | 0 |  |
| codclas | varchar(4) | NO | MUL |  |  |
| codadm | char(3) | NO |  |  |  |
| preafe | varchar(8) | NO |  |  |  |
| docext | varchar(20) | NO |  |  |  |
| afepag | tinyint(3) | NO |  | 0 |  |
| nitte1 | varchar(15) | NO | MUL |  |  |
| nitte2 | varchar(15) | NO | MUL |  |  |
| numite | smallint(6) | NO |  | 1 |  |

**Muestras (3 filas):**

```json
[]
```

---

## `detnotcxccxp` (1 filas)

| Campo | Tipo | Nulo | Key | Default | Extra |
|-------|------|------|-----|---------|-------|
| numnot | varchar(20) | NO | MUL |  |  |
| codclas | varchar(4) | NO | MUL |  |  |
| codprod | varchar(20) | NO | MUL |  |  |
| nomdet | varchar(300) | NO |  |  |  |
| candet | double | NO |  | 0 |  |
| valuni | double | NO |  | 0 |  |
| dctpor | float | NO |  | 0 |  |
| dctpes | double | NO |  | 0 |  |
| ivapor | float | NO |  | 0 |  |
| ivapes | double | NO |  | 0 |  |
| ipopor | float | NO |  | 0 |  |
| ipopes | double | NO |  | 0 |  |
| totdet | double | NO |  | 0 |  |
| cosprod | double | NO |  | 0 |  |
| sernum | varchar(40) | NO |  |  |  |
| serfec | varchar(10) | NO |  |  |  |
| tipdet | char(2) | NO |  |  |  |
| codpor | varchar(4) | NO | MUL | 0 |  |
| codpor2 | varchar(4) | NO |  | 0 |  |
| codcos | varchar(6) | NO | MUL |  |  |
| codbod | varchar(4) | NO | MUL |  |  |
| codmed | varchar(3) | NO | MUL |  |  |
| divmul | char(1) | NO |  | M |  |
| facumed | double | NO |  | 1 |  |
| numite | smallint(6) | NO |  | 1 |  |
| iterel | smallint(6) | NO |  | 0 |  |
| tipipo | varchar(2) | NO |  |  |  |
| tiesub | char(1) | NO |  |  |  |
| multiplo | double | NO |  | 1 |  |
| cruclas | varchar(4) | NO |  |  |  |
| crunum | varchar(20) | NO |  |  |  |

**Muestras (3 filas):**

```json
[
  {
    "numnot": "1",
    "codclas": "S16",
    "codprod": "KAROT050",
    "nomdet": "ACEITE DE COCO EN SPRAY x 150g",
    "candet": "1.0",
    "valuni": "24600.0",
    "dctpor": "0.0",
    "dctpes": "0.0",
    "ivapor": "0.0",
    "ivapes": "0.0",
    "ipopor": "0.0",
    "ipopes": "0.0",
    "totdet": "24600.0",
    "cosprod": "19687.0",
    "sernum": "",
    "serfec": "",
    "tipdet": "P",
    "codpor": "IV2",
    "codpor2": "",
    "codcos": "",
    "codbod": "BD01",
    "codmed": "001",
    "divmul": "",
    "facumed": "1.0",
    "numite": "1",
    "iterel": "1",
    "tipipo": "NO",
    "tiesub": "A",
    "multiplo": "1.0",
    "cruclas": "",
    "crunum": ""
  }
]
```

---

## `detpedires` (0 filas)

| Campo | Tipo | Nulo | Key | Default | Extra |
|-------|------|------|-----|---------|-------|
| numped | varchar(20) | NO | MUL |  |  |
| codmes | varchar(4) | NO | MUL |  |  |
| nitter | varchar(15) | NO | MUL |  |  |
| codprod | varchar(20) | NO | MUL |  |  |
| numite | smallint(6) | NO |  | 1 |  |
| sernum | varchar(40) | NO |  |  |  |
| nomdet | varchar(250) | NO |  |  |  |
| valuni | double | NO |  | 0 |  |
| candet | double | NO |  | 0 |  |
| cadesp | double | NO |  | 0 |  |
| dctpor | float | NO |  | 0 |  |
| dctpes | double | NO |  | 0 |  |
| ivapor | float | NO |  | 0 |  |
| ivapes | double | NO |  | 0 |  |
| totdet | double | NO |  | 0 |  |
| cosprod | double | NO |  | 0 |  |
| tipdet | char(2) | NO |  | P |  |
| codpor | varchar(4) | NO | MUL | 0 |  |
| presdet | varchar(100) | NO |  |  |  |
| codbod | varchar(4) | NO | MUL |  |  |
| ipopor | float | NO |  | 0 |  |
| ipopes | double | NO |  | 0 |  |
| tipipo | varchar(2) | NO |  |  |  |
| codpor2 | varchar(4) | NO |  | 0 |  |
| tiesub | char(1) | NO |  |  |  |
| puntos | double | NO |  | 0 |  |
| serfec | varchar(10) | NO |  |  |  |
| estado | char(1) | NO |  |  |  |
| horped | datetime | NO |  | 2000-01-01 00:00:00 |  |
| hordesp | datetime | NO |  | 2000-01-01 00:00:00 |  |
| codsuc | varchar(15) | NO |  |  |  |
| estdesp | varchar(1) | NO |  |  |  |
| obsdet | varchar(150) | NO |  |  |  |
| auxord | char(1) | NO |  |  |  |
| minuto | smallint(3) | NO |  | 0 |  |
| pidobs2 | char(1) | NO |  |  |  |
| lugimp | varchar(50) | NO |  |  |  |
| codmed | varchar(3) | NO | MUL |  |  |
| divmul | char(1) | NO |  | M |  |
| facumed | double | NO |  | 1 |  |
| codclas | varchar(4) | NO | MUL | P01 |  |

**Muestras (3 filas):**

```json
[]
```

---

## `detpedreseli` (0 filas)

| Campo | Tipo | Nulo | Key | Default | Extra |
|-------|------|------|-----|---------|-------|
| numped | varchar(20) | NO | MUL |  |  |
| codmes | varchar(4) | NO | MUL |  |  |
| nommes | varchar(50) | NO |  |  |  |
| nitter | varchar(15) | NO | MUL |  |  |
| codemp1 | varchar(15) | NO | MUL |  |  |
| codemp2 | varchar(15) | NO | MUL |  |  |
| codprod | varchar(20) | NO | MUL |  |  |
| numite | smallint(6) | NO |  | 1 |  |
| nomdet | varchar(250) | NO |  |  |  |
| valuni | double | NO |  | 0 |  |
| candet | double | NO |  | 0 |  |
| cadesp | double | NO |  | 0 |  |
| dctpor | float | NO |  | 0 |  |
| dctpes | double | NO |  | 0 |  |
| ivapor | float | NO |  | 0 |  |
| ivapes | double | NO |  | 0 |  |
| totdet | double | NO |  | 0 |  |
| tipdet | char(2) | NO |  | P |  |
| ipopor | float | NO |  | 0 |  |
| ipopes | double | NO |  | 0 |  |
| tipipo | varchar(2) | NO |  |  |  |
| estado | char(1) | NO |  |  |  |
| horped | datetime | NO |  | 2000-01-01 00:00:00 |  |
| hordesp | datetime | NO |  | 2000-01-01 00:00:00 |  |
| horeli | datetime | NO |  | 2000-01-01 00:00:00 |  |
| codsuc | varchar(15) | NO |  |  |  |
| estdesp | varchar(1) | NO |  |  |  |
| obsdet | varchar(150) | NO |  |  |  |
| minuto | smallint(3) | NO |  | 0 |  |
| codclas | varchar(4) | NO | MUL | P01 |  |

**Muestras (3 filas):**

```json
[]
```

---

## `detpresupues` (0 filas)

| Campo | Tipo | Nulo | Key | Default | Extra |
|-------|------|------|-----|---------|-------|
| numpre | varchar(20) | NO | MUL |  |  |
| codclas | varchar(4) | NO | MUL |  |  |
| codrub | varchar(35) | NO | MUL |  |  |
| nomdet | varchar(250) | NO |  |  |  |
| valdet | double | NO |  | 0 |  |
| numite | smallint(6) | NO |  | 1 |  |
| codcos | varchar(6) | NO | MUL |  |  |
| prenum | varchar(8) | NO |  |  |  |
| valdeb | double | NO |  | 0 |  |
| valhab | double | NO |  | 0 |  |
| codemp | varchar(15) | NO | MUL |  |  |
| fecdoc | datetime | NO |  | 2000-01-20 00:00:00 |  |
| nitter | varchar(15) | NO | MUL |  |  |
| estcue | char(1) | NO |  | B |  |
| empcod | varchar(3) | NO | MUL |  |  |
| docafe | varchar(20) | NO |  |  |  |
| preafe | varchar(8) | NO |  |  |  |
| clasafe | varchar(4) | NO |  |  |  |
| codsuc | varchar(15) | NO |  |  |  |
| tipodet | char(1) | NO |  |  |  |
| markav | char(1) | NO |  | X |  |
| tipafe | char(1) | NO |  |  |  |
| codano | smallint(6) | NO | MUL | 0 |  |

**Muestras (3 filas):**

```json
[]
```

---

## `detrecepmerca` (0 filas)

| Campo | Tipo | Nulo | Key | Default | Extra |
|-------|------|------|-----|---------|-------|
| numrec | varchar(20) | NO | MUL |  |  |
| codclas | varchar(4) | NO | MUL |  |  |
| codprod | varchar(20) | NO | MUL |  |  |
| sernum | varchar(40) | NO |  |  |  |
| nomdet | varchar(300) | NO |  |  |  |
| candet | double | NO |  | 0 |  |
| obsdet | varchar(300) | NO |  |  |  |
| numite | smallint(6) | NO |  | 1 |  |
| serfec | varchar(10) | NO |  |  |  |
| fecreci | datetime | NO |  | 2000-01-01 00:00:00 |  |
| multiplo | double | NO |  | 1 |  |
| codmed | varchar(3) | NO | MUL |  |  |
| divmul | char(1) | NO |  | M |  |
| facumed | double | NO |  | 1 |  |

**Muestras (3 filas):**

```json
[]
```

---

## `detreghabita` (0 filas)

| Campo | Tipo | Nulo | Key | Default | Extra |
|-------|------|------|-----|---------|-------|
| numreg | varchar(20) | NO | MUL |  |  |
| nitter | varchar(15) | NO |  |  |  |
| nomcli | varchar(120) | NO |  |  |  |
| fecnac | date | NO |  | 2000-01-20 |  |
| codclas | varchar(4) | NO | MUL |  |  |
| edad | tinyint(3) | NO |  | 0 |  |
| tipeda | varchar(10) | NO |  |  |  |

**Muestras (3 filas):**

```json
[]
```

---

## `detsolrepin` (0 filas)

| Campo | Tipo | Nulo | Key | Default | Extra |
|-------|------|------|-----|---------|-------|
| numcom | varchar(20) | NO | MUL |  |  |
| codclas | varchar(4) | NO | MUL |  |  |
| coddet | varchar(12) | NO |  |  |  |
| nomdet | varchar(150) | NO |  |  |  |
| candet | double | NO |  | 0 |  |
| valtot | double | NO |  | 0 |  |
| desinf | varchar(100) | NO |  |  |  |
| estsem | char(1) | NO |  |  |  |
| numite | smallint(6) | NO |  | 1 |  |
| tipo | char(1) | NO |  |  |  |
| obsdet | varchar(100) | NO |  |  |  |

**Muestras (3 filas):**

```json
[]
```

---

## `detsolser` (0 filas)

| Campo | Tipo | Nulo | Key | Default | Extra |
|-------|------|------|-----|---------|-------|
| numsol | varchar(20) | NO | MUL |  |  |
| nomdet | varchar(300) | NO |  |  |  |
| candet | double | NO |  | 0 |  |
| codclas | varchar(4) | NO | MUL |  |  |

**Muestras (3 filas):**

```json
[]
```

---

## `detsucursal` (0 filas)

| Campo | Tipo | Nulo | Key | Default | Extra |
|-------|------|------|-----|---------|-------|
| codsuc | varchar(20) | NO | MUL |  |  |
| codser | varchar(12) | NO | MUL |  |  |
| valuni | double | NO |  | 0 |  |
| candet | double | NO |  | 0 |  |
| ivapor | float | NO |  | 0 |  |
| ivapes | double | NO |  | 0 |  |
| totdet | double | NO |  | 0 |  |
| codpor | varchar(4) | NO | MUL | 0 |  |
| tiptip | char(1) | NO |  | M |  |
| devcam | char(2) | NO |  | NO |  |
| numite | smallint(6) | NO |  | 1 |  |
| tiecuo | char(1) | NO |  | N |  |
| numcuo | smallint(6) | NO |  | 0 |  |
| cuopag | smallint(6) | NO |  | 0 |  |
| fecdes | date | NO |  | 2000-01-01 |  |
| nomdet | varchar(100) | NO |  |  |  |

**Muestras (3 filas):**

```json
[]
```

---

## `dettraslado` (0 filas)

| Campo | Tipo | Nulo | Key | Default | Extra |
|-------|------|------|-----|---------|-------|
| numtra | varchar(20) | NO | MUL |  |  |
| codclas | varchar(4) | NO | MUL |  |  |
| codprod | varchar(20) | NO | MUL |  |  |
| sernum | varchar(40) | NO |  |  |  |
| nomdet | varchar(300) | NO |  |  |  |
| cosuni | double | NO |  | 0 |  |
| candet | double | NO |  | 0 |  |
| sanori | double | NO |  | 0 |  |
| snuori | double | NO |  | 0 |  |
| sandes | double | NO |  | 0 |  |
| snudes | double | NO |  | 0 |  |
| serfec | varchar(10) | NO |  |  |  |
| codmed | varchar(3) | NO | MUL |  |  |
| divmul | char(1) | NO |  | M |  |
| facumed | double | NO |  | 1 |  |
| numite | smallint(6) | NO |  | 1 |  |

**Muestras (3 filas):**

```json
[]
```

---

## `domicilios` (0 filas)

| Campo | Tipo | Nulo | Key | Default | Extra |
|-------|------|------|-----|---------|-------|
| numcom | varchar(20) | NO | MUL |  |  |
| codclas | varchar(4) | NO | MUL |  |  |
| predoc | varchar(8) | NO |  |  |  |
| nomdoc | varchar(100) | NO |  |  |  |
| fecdoc | datetime | NO |  | 2000-01-20 00:00:00 |  |
| fecent | datetime | NO |  | 2000-01-20 00:00:00 |  |
| nitter | varchar(15) | NO | MUL |  |  |
| nomcom | varchar(150) | NO |  |  |  |
| telter | varchar(30) | NO |  |  |  |
| nomter1 | varchar(30) | NO |  |  |  |
| nomter2 | varchar(30) | NO |  |  |  |
| apeter1 | varchar(30) | NO |  |  |  |
| apeter2 | varchar(30) | NO |  |  |  |
| dirter | varchar(100) | NO |  |  |  |
| dirdom | varchar(100) | NO |  |  |  |
| dirref | varchar(100) | NO |  |  |  |
| nitmen | varchar(15) | NO |  |  |  |
| nommen | varchar(150) | NO |  |  |  |
| subdoc | double | NO |  | 0 |  |
| totdct | double | NO |  | 0 |  |
| totiva | double | NO |  | 0 |  |
| totipo | double | NO |  | 0 |  |
| totdoc | double | NO |  | 0 |  |
| obsdoc | varchar(400) | NO |  |  |  |
| priorid | char(2) | NO |  |  |  |
| forped | varchar(30) | NO |  |  |  |
| codpag | varchar(4) | NO | MUL |  |  |
| codemp | varchar(15) | NO | MUL |  |  |
| estdoc | char(1) | NO |  |  |  |
| domfac | char(1) | NO |  |  |  |
| empcod | varchar(3) | NO | MUL |  |  |

**Muestras (3 filas):**

```json
[]
```

---

## `empfpago` (0 filas)

| Campo | Tipo | Nulo | Key | Default | Extra |
|-------|------|------|-----|---------|-------|
| nitter | varchar(15) | NO | MUL |  |  |
| codpag | varchar(4) | NO | MUL |  |  |
| codcaj | varchar(4) | NO | MUL |  |  |
| tipo | char(1) | NO |  | 1 |  |

**Muestras (3 filas):**

```json
[]
```

---

## `emplecoman` (0 filas)

| Campo | Tipo | Nulo | Key | Default | Extra |
|-------|------|------|-----|---------|-------|
| nitter | varchar(15) | NO | MUL |  |  |
| numdes | varchar(20) | NO |  |  |  |
| numhas | varchar(20) | NO |  |  |  |

**Muestras (3 filas):**

```json
[]
```

---

## `empresas` (1 filas)

| Campo | Tipo | Nulo | Key | Default | Extra |
|-------|------|------|-----|---------|-------|
| empcod | varchar(3) | NO | PRI |  |  |
| nomemp | varchar(120) | NO |  |  |  |
| dirsuc | varchar(100) | NO |  |  |  |
| telsuc | varchar(30) | NO |  |  |  |
| movsuc | varchar(30) | NO |  |  |  |
| codciu | varchar(6) | NO |  |  |  |
| obssuc | varchar(400) | NO |  |  |  |
| inasuc | char(2) | NO |  | NO |  |
| imptiq1 | varchar(150) | NO |  |  |  |
| imptiq2 | varchar(150) | NO |  |  |  |
| imptiq3 | varchar(150) | NO |  |  |  |
| imptiq4 | varchar(150) | NO |  |  |  |
| imptiq5 | varchar(150) | NO |  |  |  |

**Muestras (3 filas):**

```json
[
  {
    "empcod": "E01",
    "nomemp": "PRINCIPAL",
    "dirsuc": "",
    "telsuc": "",
    "movsuc": "",
    "codciu": "",
    "obssuc": "",
    "inasuc": "NO",
    "imptiq1": "Tienda Saludable y Funcional",
    "imptiq2": "Dir: CL 18 n25-94 esquina Centro",
    "imptiq3": "Pasto-Nari├▒o",
    "imptiq4": "Tel: 3116978695",
    "imptiq5": ""
  }
]
```

---

## `entsalida` (0 filas)

| Campo | Tipo | Nulo | Key | Default | Extra |
|-------|------|------|-----|---------|-------|
| nument | varchar(20) | NO | MUL |  |  |
| codclas | varchar(4) | NO | MUL |  |  |
| nomdoc | varchar(100) | NO |  | SALIDAS |  |
| preent | varchar(8) | NO |  | RC |  |
| fecent | datetime | NO |  | 2000-01-20 00:00:00 |  |
| obsent | varchar(400) | NO |  |  |  |
| estent | char(1) | NO |  |  |  |
| horent | tinyint(3) | NO |  | 1 |  |
| codres | varchar(4) | NO | MUL |  |  |
| codcos | varchar(6) | NO | MUL |  |  |
| nitter | varchar(15) | NO | MUL |  |  |
| nitres | varchar(15) | NO | MUL |  |  |
| codemp | varchar(15) | NO | MUL |  |  |
| codcue | varchar(20) | NO | MUL |  |  |
| empcod | varchar(3) | NO | MUL |  |  |
| agrupa | char(1) | NO |  |  |  |
| veridoc | tinyint(1) | NO |  | 0 |  |
| feccrea | datetime | NO |  | 2000-01-20 00:00:00 |  |

**Muestras (3 filas):**

```json
[]
```

---

## `facaprocre` (6 filas)

| Campo | Tipo | Nulo | Key | Default | Extra |
|-------|------|------|-----|---------|-------|
| numfven | varchar(20) | NO | MUL |  |  |
| codclas | varchar(4) | NO | MUL |  |  |
| nitter | varchar(15) | NO | MUL |  |  |
| obscre | varchar(250) | NO |  |  |  |
| valapro | double | NO |  | 0 |  |
| salante | double | NO |  | 0 |  |
| coddin | varchar(20) | NO |  |  |  |

**Muestras (3 filas):**

```json
[
  {
    "numfven": "4",
    "codclas": "S15",
    "nitter": "1151970853",
    "obscre": " ",
    "valapro": "59700.0",
    "salante": "0.0",
    "coddin": ""
  },
  {
    "numfven": "6",
    "codclas": "S15",
    "nitter": "1151970853",
    "obscre": " ",
    "valapro": "21950.0",
    "salante": "0.0",
    "coddin": ""
  },
  {
    "numfven": "8",
    "codclas": "S15",
    "nitter": "1151970853",
    "obscre": " ",
    "valapro": "13000.0",
    "salante": "0.0",
    "coddin": ""
  }
]
```

---

## `factorfin` (24 filas)

| Campo | Tipo | Nulo | Key | Default | Extra |
|-------|------|------|-----|---------|-------|
| codfac | varchar(4) | NO | PRI |  |  |
| desfac | varchar(50) | NO |  |  |  |
| valfac | double | NO |  | 0 |  |
| numcuo | tinyint(3) | NO |  | 0 |  |
| porfin | float | NO |  | 0 |  |

**Muestras (3 filas):**

```json
[
  {
    "codfac": "1",
    "desfac": "FACTOR 1 CUOTA",
    "valfac": "1.0125",
    "numcuo": "1",
    "porfin": "1.25"
  },
  {
    "codfac": "24",
    "desfac": "FACTOR 24 CUOTAS",
    "valfac": "0.048487",
    "numcuo": "24",
    "porfin": "1.25"
  },
  {
    "codfac": "2",
    "desfac": "FACTOR 2 CUOTAS",
    "valfac": "0.509394",
    "numcuo": "2",
    "porfin": "1.25"
  }
]
```

---

## `facventas` (91 filas)

| Campo | Tipo | Nulo | Key | Default | Extra |
|-------|------|------|-----|---------|-------|
| numfven | varchar(20) | NO | MUL |  |  |
| codclas | varchar(4) | NO | MUL |  |  |
| nomdoc | varchar(100) | NO |  | FACTURA DE VENTA |  |
| prefven | varchar(8) | NO |  | FV |  |
| fecfven | datetime | NO |  | 2000-01-20 00:00:00 |  |
| codciu | varchar(6) | NO | MUL |  |  |
| nitter | varchar(15) | NO | MUL |  |  |
| digfven | char(2) | NO |  |  |  |
| clifven | varchar(120) | NO |  |  |  |
| dirfven | varchar(100) | NO |  |  |  |
| telfven | varchar(50) | NO |  |  |  |
| nitvend | varchar(15) | NO | MUL |  |  |
| venfven | varchar(120) | NO |  |  |  |
| codpag | varchar(4) | NO |  |  |  |
| diasfven | smallint(6) | NO |  | 0 |  |
| subfven | double | NO |  | 0 |  |
| totdct | double | NO |  | 0 |  |
| totiva | double | NO |  | 0 |  |
| totipo | double | NO |  | 0 |  |
| retfte | double | NO |  | 0 |  |
| retiva | double | NO |  | 0 |  |
| retica | double | NO |  | 0 |  |
| retcre | double | NO |  | 0 |  |
| ajuspe | double | NO |  | 0 |  |
| totfven | double | NO |  | 0 |  |
| obsfven | varchar(400) | NO |  |  |  |
| estfven | char(1) | NO |  |  |  |
| codemp | varchar(15) | NO | MUL |  |  |
| horfven | tinyint(3) | NO |  | 1 |  |
| tipcre | char(1) | NO |  | N |  |
| codres | varchar(4) | NO | MUL |  |  |
| codcos | varchar(6) | NO | MUL |  |  |
| codzon | varchar(4) | NO |  |  |  |
| codcaj | varchar(4) | NO | MUL |  |  |
| comipor | float | NO |  | 0 |  |
| empcod | varchar(3) | NO | MUL |  |  |
| numcru | varchar(20) | NO | MUL |  |  |
| clascru | varchar(4) | NO | MUL |  |  |
| perdes | date | NO |  | 2010-01-01 |  |
| perhas | date | NO |  | 2010-01-01 |  |
| codsuc | varchar(15) | NO | MUL |  |  |
| nomest | varchar(2) | NO |  |  |  |
| nomuso | varchar(2) | NO |  |  |  |
| nomrut | varchar(100) | NO |  |  |  |
| nomzon | varchar(100) | NO |  |  |  |
| salant | double | NO |  | 0 |  |
| numdeu | smallint(3) | NO |  | 0 |  |
| texres | varchar(250) | NO |  |  |  |
| codpla | varchar(30) | NO |  |  |  |
| codmes | varchar(4) | NO |  |   |  |
| comanum | varchar(20) | NO |  |   |  |
| nomcos | varchar(50) | NO |  |  |  |
| cauret | char(1) | NO |  |  |  |
| turno1 | char(1) | NO |  | 0 |  |
| estfele | char(1) | NO |  | N |  |
| resfele | int(6) | NO |  | 0 |  |
| propina | double | NO |  | 0 |  |
| agrupa | char(1) | NO |  |  |  |
| tipdomi | char(1) | NO |  |  |  |
| lectant | int(11) | NO |  | 0 |  |
| lectact | int(11) | NO |  | 0 |  |
| consumo | int(11) | NO |  | 0 |  |
| tiplect | char(1) | NO |  |  |  |
| docext | varchar(20) | NO |  |  |  |
| corele | varchar(100) | NO |  |  |  |
| otrimp | double | NO |  | 0 |  |
| dctglob | double | NO |  | 0 |  |
| recglob | double | NO |  | 0 |  |
| tazacam | double | NO |  | 1 |  |
| moneda | varchar(4) | NO |  |  |  |
| veridoc | tinyint(1) | NO |  | 0 |  |
| fecdext | date | NO |  | 2010-01-01 |  |
| feccrea | datetime | NO |  | 2000-01-20 00:00:00 |  |
| tipofac | varchar(100) | NO |  |  |  |

**Muestras (3 filas):**

```json
[
  {
    "numfven": "1",
    "codclas": "S15",
    "nomdoc": "FACTURA DE VENTA POS",
    "prefven": "FVP",
    "fecfven": "2026-06-04 16:31:44",
    "codciu": "",
    "nitter": "",
    "digfven": "",
    "clifven": " ",
    "dirfven": " ",
    "telfven": " ",
    "nitvend": "",
    "venfven": " ",
    "codpag": "F01",
    "diasfven": "0",
    "subfven": "34000.0",
    "totdct": "0.0",
    "totiva": "0.0",
    "totipo": "0.0",
    "retfte": "0.0",
    "retiva": "0.0",
    "retica": "0.0",
    "retcre": "0.0",
    "ajuspe": "0.0",
    "totfven": "34000.0",
    "obsfven": "",
    "estfven": "B",
    "codemp": "1151970853",
    "horfven": "16",
    "tipcre": "N",
    "codres": "",
    "codcos": "",
    "codzon": "",
    "codcaj": "C1",
    "comipor": "0.0",
    "empcod": "",
    "numcru": "",
    "clascru": "",
    "perdes": "2010-01-01",
    "perhas": "2010-01-01",
    "codsuc": "",
    "nomest": "",
    "nomuso": "",
    "nomrut": "",
    "nomzon": "",
    "salant": "0.0",
    "numdeu": "0",
    "texres": "",
    "codpla": "",
    "codmes": "",
    "comanum": "",
    "nomcos": "",
    "cauret": "S",
    "turno1": "0",
    "estfele": "N",
    "resfele": "0",
    "propina": "0.0",
    "agrupa": "",
    "tipdomi": "",
    "lectant": "0",
    "lectact": "0",
    "consumo": "0",
    "tiplect": "",
    "docext": "",
    "corele": "",
    "otrimp": "0.0",
    "dctglob": "0.0",
    "recglob": "0.0",
    "tazacam": "1.0",
    "moneda": "",
    "veridoc": "0",
    "fecdext": "2010-01-01",
    "feccrea": "2026-06-04 16:33:58",
    "tipofac": ""
  },
  {
    "numfven": "2",
    "codclas": "S15",
    "nomdoc": "FACTURA DE VENTA POS",
    "prefven": "FVP",
    "fecfven": "2026-06-04 14:01:46",
    "codciu": "52001",
    "nitter": "222222222",
    "digfven": "",
    "clifven": "CONSUMIDOR  FINAL",
    "dirfven": "CONOCIDA",
    "telfven": " ",
    "nitvend": "",
    "venfven": " ",
    "codpag": "F01",
    "diasfven": "0",
    "subfven": "15900.0",
    "totdct": "0.0",
    "totiva": "0.0",
    "totipo": "0.0",
    "retfte": "0.0",
    "retiva": "0.0",
    "retica": "0.0",
    "retcre": "0.0",
    "ajuspe": "0.0",
    "totfven": "15900.0",
    "obsfven": "",
    "estfven": "B",
    "codemp": "1151970853",
    "horfven": "14",
    "tipcre": "N",
    "codres": "",
    "codcos": "",
    "codzon": "",
    "codcaj": "C1",
    "comipor": "0.0",
    "empcod": "",
    "numcru": "",
    "clascru": "",
    "perdes": "2010-01-01",
    "perhas": "2010-01-01",
    "codsuc": "",
    "nomest": "",
    "nomuso": "",
    "nomrut": "",
    "nomzon": "",
    "salant": "0.0",
    "numdeu": "0",
    "texres": "",
    "codpla": "",
    "codmes": "",
    "comanum": "",
    "nomcos": "",
    "cauret": "S",
    "turno1": "0",
    "estfele": "N",
    "resfele": "0",
    "propina": "0.0",
    "agrupa": "",
    "tipdomi": "",
    "lectant": "0",
    "lectact": "0",
    "consumo": "0",
    "tiplect": "",
    "docext": "",
    "corele": "",
    "otrimp": "0.0",
    "dctglob": "0.0",
    "recglob": "0.0",
    "tazacam": "1.0",
    "moneda": "",
    "veridoc": "0",
    "fecdext": "2010-01-01",
    "feccrea": "2026-06-08 14:06:10",
    "tipofac": ""
  },
  {
    "numfven": "3",
    "codclas": "S15",
    "nomdoc": "FACTURA DE VENTA POS",
    "prefven": "FVP",
    "fecfven": "2026-06-04 14:07:51",
    "codciu": "52001",
    "nitter": "222222222",
    "digfven": "",
    "clifven": "CONSUMIDOR  FINAL",
    "dirfven": "CONOCIDA",
    "telfven": " ",
    "nitvend": "",
    "venfven": " ",
    "codpag": "F01",
    "diasfven": "0",
    "subfven": "77000.0",
    "totdct": "0.0",
    "totiva": "0.0",
    "totipo": "0.0",
    "retfte": "0.0",
    "retiva": "0.0",
    "retica": "0.0",
    "retcre": "0.0",
    "ajuspe": "0.0",
    "totfven": "77000.0",
    "obsfven": "",
    "estfven": "B",
    "codemp": "1151970853",
    "horfven": "14",
    "tipcre": "N",
    "codres": "",
    "codcos": "",
    "codzon": "",
    "codcaj": "C1",
    "comipor": "0.0",
    "empcod": "",
    "numcru": "",
    "clascru": "",
    "perdes": "2010-01-01",
    "perhas": "2010-01-01",
    "codsuc": "",
    "nomest": "",
    "nomuso": "",
    "nomrut": "",
    "nomzon": "",
    "salant": "0.0",
    "numdeu": "0",
    "texres": "",
    "codpla": "",
    "codmes": "",
    "comanum": "",
    "nomcos": "",
    "cauret": "S",
    "turno1": "0",
    "estfele": "N",
    "resfele": "0",
    "propina": "0.0",
    "agrupa": "",
    "tipdomi": "",
    "lectant": "0",
    "lectact": "0",
    "consumo": "0",
    "tiplect": "",
    "docext": "",
    "corele": "",
    "otrimp": "0.0",
    "dctglob": "0.0",
    "recglob": "0.0",
    "tazacam": "1.0",
    "moneda": "",
    "veridoc": "0",
    "fecdext": "2010-01-01",
    "feccrea": "2026-06-08 14:31:14",
    "tipofac": ""
  }
]
```

---

## `financiacion` (0 filas)

| Campo | Tipo | Nulo | Key | Default | Extra |
|-------|------|------|-----|---------|-------|
| numfin | varchar(20) | NO | MUL |  |  |
| prefin | varchar(8) | NO |  |  |  |
| nomdoc | varchar(100) | NO |  |  |  |
| fecfin | datetime | NO |  | 2000-01-01 00:00:00 |  |
| nitter | varchar(15) | NO | MUL |  |  |
| tipgar | char(6) | NO |  | PAGARE |  |
| numgar | varchar(20) | NO |  |  |  |
| numsol | varchar(15) | NO | MUL |  |  |
| valnet | double | NO |  | 0 |  |
| cuoini | double | NO |  | 0 |  |
| salfin | double | NO |  | 0 |  |
| totint | double | NO |  | 0 |  |
| totcuo | tinyint(3) | NO |  | 0 |  |
| porfin | float | NO |  | 0 |  |
| facfin | double | NO |  | 0 |  |
| intmor | float | NO |  | 0 |  |
| valcomi | double | NO |  | 0 |  |
| tipiva | char(1) | NO |  | I |  |
| ivafin | float | NO |  | 0 |  |
| valseg | double | NO |  | 0 |  |
| fecini | date | NO |  | 2000-01-01 |  |
| valcuo | double | NO |  | 0 |  |
| obsfin | varchar(400) | NO |  |  |  |
| codpor | varchar(4) | NO | MUL |  |  |
| estfin | char(1) | NO |  |  |  |
| codemp | varchar(15) | NO | MUL |  |  |
| horfin | tinyint(3) | NO |  | 1 |  |
| codres | varchar(4) | NO | MUL |  |  |
| factor | char(2) | NO |  | NO |  |
| codfac | varchar(4) | NO |  |  |  |
| fpagdes | varchar(4) | NO |  |  |  |
| fpagcxc | varchar(4) | NO |  |  |  |
| codban | varchar(8) | NO | MUL |  |  |
| numche | varchar(20) | NO |  |  |  |
| fecche | date | NO |  | 2000-01-20 |  |
| perpag | varchar(10) | NO |  |  |  |
| codcos | varchar(6) | NO | MUL |  |  |
| pucint | varchar(12) | NO |  |  |  |
| pucvar | varchar(20) | NO |  |  |  |
| codclas | varchar(4) | NO | MUL |  |  |
| empcod | varchar(3) | NO | MUL |  |  |
| veridoc | tinyint(1) | NO |  | 0 |  |
| feccrea | datetime | NO |  | 2000-01-20 00:00:00 |  |

**Muestras (3 filas):**

```json
[]
```

---

## `fincas` (0 filas)

| Campo | Tipo | Nulo | Key | Default | Extra |
|-------|------|------|-----|---------|-------|
| nitter | varchar(15) | NO | MUL |  |  |
| fincod | varchar(30) | NO | MUL |  |  |
| finnom | varchar(50) | NO |  |  |  |

**Muestras (3 filas):**

```json
[]
```

---

## `formapago` (20 filas)

| Campo | Tipo | Nulo | Key | Default | Extra |
|-------|------|------|-----|---------|-------|
| codpag | varchar(4) | NO | PRI |  |  |
| forpag | varchar(100) | NO |  |  |  |
| afepag | tinyint(3) | NO |  | 0 |  |
| tippag | tinyint(3) | NO |  | 0 |  |
| codcaj | varchar(4) | NO | MUL |  |  |
| codban | varchar(8) | NO | MUL |  |  |
| codcue | varchar(20) | NO | MUL |  |  |
| facven | char(2) | NO |  | NO |  |
| venpos | char(2) | NO |  | NO |  |
| ndcxc | char(2) | NO |  | NO |  |
| nccxc | char(2) | NO |  | NO |  |
| compra | char(2) | NO |  | NO |  |
| ndcxp | char(2) | NO |  | NO |  |
| nccxp | char(2) | NO |  | NO |  |
| coming | char(2) | NO |  | NO |  |
| comegr | char(2) | NO |  | NO |  |
| devpos | char(2) | NO |  | NO |  |
| financ | char(2) | NO |  | NO |  |
| oblifin | char(2) | NO |  | NO |  |
| nomemp | char(2) | NO |  | NO |  |
| numcon | bigint(20) | NO |  | 0 |  |
| empsino | char(1) | NO |  | N |  |
| anting | char(2) | NO |  | SI |  |
| antegr | char(2) | NO |  | SI |  |
| codaux1 | varchar(10) | NO |  |  |  |
| codfele | varchar(3) | NO | MUL |  |  |

**Muestras (3 filas):**

```json
[
  {
    "codpag": "F04",
    "forpag": "TARJETA CREDITO",
    "afepag": "24",
    "tippag": "2",
    "codcaj": "CA1",
    "codban": " ",
    "codcue": "11100501",
    "facven": "SI",
    "venpos": "SI",
    "ndcxc": "SI",
    "nccxc": "NO",
    "compra": "NO",
    "ndcxp": "NO",
    "nccxp": "NO",
    "coming": "SI",
    "comegr": "NO",
    "devpos": "NO",
    "financ": "NO",
    "oblifin": "NO",
    "nomemp": "NO",
    "numcon": "0",
    "empsino": "N",
    "anting": "NO",
    "antegr": "NO",
    "codaux1": "",
    "codfele": "48"
  },
  {
    "codpag": "F05",
    "forpag": "CONSIGNACION BANCO....",
    "afepag": "21",
    "tippag": "2",
    "codcaj": "",
    "codban": " ",
    "codcue": "11100501",
    "facven": "SI",
    "venpos": "SI",
    "ndcxc": "SI",
    "nccxc": "NO",
    "compra": "NO",
    "ndcxp": "SI",
    "nccxp": "NO",
    "coming": "SI",
    "comegr": "NO",
    "devpos": "NO",
    "financ": "NO",
    "oblifin": "SI",
    "nomemp": "NO",
    "numcon": "0",
    "empsino": "N",
    "anting": "NO",
    "antegr": "NO",
    "codaux1": "",
    "codfele": "42"
  },
  {
    "codpag": "F06",
    "forpag": "CHEQUE BANCO....",
    "afepag": "22",
    "tippag": "2",
    "codcaj": "",
    "codban": " ",
    "codcue": "11100501",
    "facven": "NO",
    "venpos": "NO",
    "ndcxc": "NO",
    "nccxc": "NO",
    "compra": "SI",
    "ndcxp": "NO",
    "nccxp": "SI",
    "coming": "NO",
    "comegr": "SI",
    "devpos": "NO",
    "financ": "SI",
    "oblifin": "NO",
    "nomemp": "SI",
    "numcon": "1",
    "empsino": "N",
    "anting": "NO",
    "antegr": "NO",
    "codaux1": "",
    "codfele": "20"
  }
]
```

---

## `formapele` (75 filas)

| Campo | Tipo | Nulo | Key | Default | Extra |
|-------|------|------|-----|---------|-------|
| codfele | varchar(3) | NO | MUL |  |  |
| nomfpag | varchar(150) | NO |  |  |  |

**Muestras (3 filas):**

```json
[
  {
    "codfele": "1",
    "nomfpag": "Instrumento no definido"
  },
  {
    "codfele": "2",
    "nomfpag": "Cr├®dito ACH"
  },
  {
    "codfele": "3",
    "nomfpag": "D├®bito ACH"
  }
]
```

---

## `inmueblecab` (0 filas)

| Campo | Tipo | Nulo | Key | Default | Extra |
|-------|------|------|-----|---------|-------|
| codinm2 | varchar(4) | NO | PRI |  |  |
| nominm | varchar(150) | NO |  |  |  |
| tipinm | varchar(100) | NO |  |  |  |
| dirinm | varchar(100) | NO |  |  |  |
| codciu | varchar(6) | NO |  |  |  |
| obsinm | varchar(400) | NO |  |  |  |

**Muestras (3 filas):**

```json
[]
```

---

## `inmuebledet` (0 filas)

| Campo | Tipo | Nulo | Key | Default | Extra |
|-------|------|------|-----|---------|-------|
| codinm1 | varchar(4) | NO | PRI |  |  |
| codinm2 | varchar(4) | NO | MUL |  |  |
| tipinm | varchar(100) | NO |  |  |  |
| numinm | varchar(30) | NO |  |  |  |
| areinm | varchar(20) | NO |  |  |  |
| telinm | varchar(30) | NO |  |  |  |
| obsinm | varchar(400) | NO |  |  |  |

**Muestras (3 filas):**

```json
[]
```

---

## `lecturas` (0 filas)

| Campo | Tipo | Nulo | Key | Default | Extra |
|-------|------|------|-----|---------|-------|
| codsuc | varchar(20) | NO | MUL |  |  |
| anolec | int(11) | NO |  | 0 |  |
| perlec | varchar(2) | NO |  | 0 |  |
| lectant | int(11) | NO |  | 0 |  |
| lectact | int(11) | NO |  | 0 |  |
| consumo | int(11) | NO |  | 0 |  |

**Muestras (3 filas):**

```json
[]
```

---

## `linea1` (1 filas)

| Campo | Tipo | Nulo | Key | Default | Extra |
|-------|------|------|-----|---------|-------|
| codlin1 | char(4) | NO | PRI | L1 |  |
| nomlin | char(100) | NO |  |  |  |
| codcla | char(4) | NO |  | CL1 |  |
| codcue | varchar(20) | NO |  |  |  |
| autret | char(1) | NO |  | N |  |
| porret | float | NO |  | 0 |  |

**Muestras (3 filas):**

```json
[
  {
    "codlin1": "L01",
    "nomlin": "MERCANCIAS NO FABRICADAS POR LA EMPRESA",
    "codcla": "CL1",
    "codcue": "14350101",
    "autret": "N",
    "porret": "0.0"
  }
]
```

---

## `linea2` (0 filas)

| Campo | Tipo | Nulo | Key | Default | Extra |
|-------|------|------|-----|---------|-------|
| codlin2 | char(4) | NO | PRI | L1 |  |
| nomlin | char(100) | NO |  |  |  |
| pedmes | char(1) | NO |  | 1 |  |
| impmes | char(1) | NO |  | 1 |  |
| impped | char(1) | NO |  | 1 |  |
| lugimp | varchar(50) | NO |  |  |  |

**Muestras (3 filas):**

```json
[]
```

---

## `linea3` (0 filas)

| Campo | Tipo | Nulo | Key | Default | Extra |
|-------|------|------|-----|---------|-------|
| codlin3 | char(4) | NO | PRI | L1 |  |
| nomlin | char(100) | NO |  |  |  |

**Muestras (3 filas):**

```json
[]
```

---

## `linea4` (0 filas)

| Campo | Tipo | Nulo | Key | Default | Extra |
|-------|------|------|-----|---------|-------|
| codlin4 | char(4) | NO | PRI | L1 |  |
| nomlin | char(100) | NO |  |  |  |

**Muestras (3 filas):**

```json
[]
```

---

## `linea5` (0 filas)

| Campo | Tipo | Nulo | Key | Default | Extra |
|-------|------|------|-----|---------|-------|
| codlin5 | char(4) | NO | PRI | L1 |  |
| nomlin | char(100) | NO |  |  |  |

**Muestras (3 filas):**

```json
[]
```

---

## `linea6` (0 filas)

| Campo | Tipo | Nulo | Key | Default | Extra |
|-------|------|------|-----|---------|-------|
| codlin6 | char(4) | NO | PRI | L1 |  |
| nomlin | char(100) | NO |  |  |  |

**Muestras (3 filas):**

```json
[]
```

---

## `listapre` (2 filas)

| Campo | Tipo | Nulo | Key | Default | Extra |
|-------|------|------|-----|---------|-------|
| codlis | char(3) | NO | PRI |  |  |
| nomlis | varchar(100) | NO |  |  |  |
| fija | char(2) | NO |  | NO |  |

**Muestras (3 filas):**

```json
[
  {
    "codlis": "L1",
    "nomlis": "MAYORISTA",
    "fija": "SI"
  },
  {
    "codlis": "L2",
    "nomlis": "DISTRIBUIDOR",
    "fija": "NO"
  }
]
```

---

## `listempaques` (0 filas)

| Campo | Tipo | Nulo | Key | Default | Extra |
|-------|------|------|-----|---------|-------|
| numlis | varchar(20) | NO | MUL |  |  |
| docref | varchar(200) | NO |  |  |  |
| nomdoc | varchar(100) | NO |  | FACTURA DE VENTA |  |
| prelis | varchar(8) | NO |  | FV |  |
| feclis | datetime | NO |  | 2000-01-20 00:00:00 |  |
| obslis | varchar(800) | NO |  |  |  |
| voltot | varchar(100) | NO |  |  |  |
| pesnet | varchar(100) | NO |  |  |  |
| estlis | char(1) | NO |  |  |  |
| codemp | varchar(15) | NO | MUL |  |  |
| horlis | tinyint(3) | NO |  | 1 |  |
| codres | varchar(4) | NO | MUL |  |  |
| codclas | varchar(4) | NO | MUL |  |  |
| nitter | varchar(15) | NO | MUL |  |  |
| digter | char(2) | NO |  |  |  |
| nomter | varchar(120) | NO |  |  |  |
| dirter | varchar(100) | NO |  |  |  |
| telter | varchar(50) | NO |  |  |  |
| codciu | varchar(6) | NO | MUL |  |  |
| nomciu | varchar(1520) | NO |  |  |  |
| veridoc | tinyint(1) | NO |  | 0 |  |
| feccrea | datetime | NO |  | 2000-01-20 00:00:00 |  |

**Muestras (3 filas):**

```json
[]
```

---

## `mediomag` (0 filas)

| Campo | Tipo | Nulo | Key | Default | Extra |
|-------|------|------|-----|---------|-------|
| codfor | varchar(6) | NO | MUL |  |  |
| codcue | varchar(12) | NO | MUL |  |  |
| codmed | varchar(6) | NO |  |  |  |
| base | double | NO |  | 0 |  |
| tipcat | varchar(2) | NO |  |  |  |
| sumade | char(1) | NO |  |  |  |
| regimen | char(1) | NO |  |  |  |
| esmyiva | char(1) | NO |  |  |  |
| codigo | int(6) | NO | MUL | 0 |  |
| ester | char(1) | NO |  | S |  |

**Muestras (3 filas):**

```json
[]
```

---

## `mediomdet` (0 filas)

| Campo | Tipo | Nulo | Key | Default | Extra |
|-------|------|------|-----|---------|-------|
| codigo | int(4) | NO | MUL | 0 |  |
| codclas | varchar(4) | NO | MUL |  |  |
| descon | varchar(100) | NO |  |  |  |
| tipo | char(1) | NO |  | 1 |  |

**Muestras (3 filas):**

```json
[]
```

---

## `mesas` (0 filas)

| Campo | Tipo | Nulo | Key | Default | Extra |
|-------|------|------|-----|---------|-------|
| codmes | varchar(4) | NO | PRI |  |  |
| nommes | varchar(50) | NO |  |  |  |
| tipmes | varchar(1) | NO |  | 1 |  |
| actmes | char(1) | NO |  | A |  |
| posleft | int(11) | NO |  | 0 |  |
| postop | int(11) | NO |  | 0 |  |
| height | int(11) | NO |  | 0 |  |
| width | int(11) | NO |  | 0 |  |
| pisalon | varchar(50) | NO |  |  |  |
| codprod | varchar(20) | NO | MUL |  |  |
| tipdet | char(2) | NO |  | P |  |
| valser | double | NO |  | 0 |  |
| tipcob | char(1) | NO |  | 0 |  |
| valprom | double | NO |  | 0 |  |
| horini | tinyint(3) | NO |  | 0 |  |
| horfin | tinyint(3) | NO |  | 0 |  |
| aproxi | char(1) | NO |  |  |  |

**Muestras (3 filas):**

```json
[]
```

---

## `modifdoccab1` (0 filas)

| Campo | Tipo | Nulo | Key | Default | Extra |
|-------|------|------|-----|---------|-------|
| id_cabeza | int(11) | NO | PRI |  | auto_increment |
| numdoc | varchar(20) | NO | MUL |  |  |
| codclas | varchar(4) | NO | MUL |  |  |
| nomdoc | varchar(100) | NO |  |  |  |
| predoc | varchar(8) | NO |  |  |  |
| fecdoc | datetime | NO |  | 2000-01-20 00:00:00 |  |
| nitter | varchar(15) | NO | MUL |  |  |
| nomter | varchar(120) | NO |  |  |  |
| codpag | varchar(4) | NO |  |  |  |
| cantdoc | double | NO |  | 0 |  |
| itemdoc | double | NO |  | 0 |  |
| subdoc | double | NO |  | 0 |  |
| totdct | double | NO |  | 0 |  |
| totiva | double | NO |  | 0 |  |
| totipo | double | NO |  | 0 |  |
| retfte | double | NO |  | 0 |  |
| retiva | double | NO |  | 0 |  |
| retica | double | NO |  | 0 |  |
| retcre | double | NO |  | 0 |  |
| totcom | double | NO |  | 0 |  |
| otrimp | double | NO |  | 0 |  |
| dctglob | double | NO |  | 0 |  |
| recglob | double | NO |  | 0 |  |
| totdeb | double | NO |  | 0 |  |
| tothab | double | NO |  | 0 |  |
| obsdoc | varchar(400) | NO |  |  |  |
| codemp | varchar(15) | NO | MUL |  |  |
| codcos | varchar(6) | NO | MUL |  |  |
| empcod | varchar(3) | NO | MUL |  |  |
| nitvend | varchar(15) | NO |  |  |  |
| tazacam | double | NO |  | 0 |  |
| moneda | varchar(4) | NO |  |  |  |
| nitmod | varchar(15) | NO |  |  |  |
| nommod | varchar(120) | NO |  |  |  |
| fecmod | datetime | NO |  | 2000-01-20 00:00:00 |  |

**Muestras (3 filas):**

```json
[]
```

---

## `modifdoccab2` (0 filas)

| Campo | Tipo | Nulo | Key | Default | Extra |
|-------|------|------|-----|---------|-------|
| id_cabeza | int(11) | NO | PRI |  | auto_increment |
| numnum | varchar(20) | NO | MUL |  |  |
| codclas | varchar(4) | NO | MUL |  |  |
| prenum | varchar(8) | NO |  |  |  |
| codcue | varchar(20) | NO | MUL |  |  |
| detcue | varchar(150) | NO |  |  |  |
| valdeb | double | NO |  | 0 |  |
| valhab | double | NO |  | 0 |  |
| fecdoc | datetime | NO |  | 2000-01-20 00:00:00 |  |
| nitter | varchar(15) | NO | MUL |  |  |
| codemp | varchar(15) | NO | MUL |  |  |
| codcos | varchar(6) | NO | MUL |  |  |
| numite | smallint(6) | NO |  | 1 |  |
| codbod | varchar(4) | NO | MUL |  |  |
| empcod | varchar(3) | NO | MUL |  |  |
| codsuc | varchar(15) | NO |  |  |  |
| docafe | varchar(20) | NO |  |  |  |
| clasafe | varchar(4) | NO |  |  |  |
| nitmod | varchar(15) | NO |  |  |  |
| nommod | varchar(120) | NO |  |  |  |
| fecmod | datetime | NO |  | 2000-01-20 00:00:00 |  |

**Muestras (3 filas):**

```json
[]
```

---

## `modifdocdet1` (0 filas)

| Campo | Tipo | Nulo | Key | Default | Extra |
|-------|------|------|-----|---------|-------|
| id_detalle | int(11) | NO | PRI |  | auto_increment |
| id_cabeza | int(11) | NO | MUL | 0 |  |
| numdoc | varchar(20) | NO |  |  |  |
| codclas | varchar(4) | NO | MUL |  |  |
| codprod | varchar(20) | NO | MUL |  |  |
| nomdet | varchar(300) | NO |  |  |  |
| candet | double | NO |  | 0 |  |
| valuni | double | NO |  | 0 |  |
| dctpor | float | NO |  | 0 |  |
| dctpes | double | NO |  | 0 |  |
| ivapor | float | NO |  | 0 |  |
| ivapes | double | NO |  | 0 |  |
| ipopor | float | NO |  | 0 |  |
| ipopes | double | NO |  | 0 |  |
| totdet | double | NO |  | 0 |  |
| codcue | varchar(20) | NO |  |  |  |
| valdeb | double | NO |  | 0 |  |
| valhab | double | NO |  | 0 |  |
| nitter | varchar(15) | NO |  |  |  |
| obsdet | varchar(400) | NO |  |  |  |
| codbod | varchar(4) | NO | MUL |  |  |
| codcos | varchar(6) | NO | MUL |  |  |
| numite | smallint(6) | NO |  | 1 |  |

**Muestras (3 filas):**

```json
[]
```

---

## `motanudoc` (9 filas)

| Campo | Tipo | Nulo | Key | Default | Extra |
|-------|------|------|-----|---------|-------|
| numnum | varchar(20) | NO | MUL |  |  |
| fecanu | date | NO |  | 2000-01-20 |  |
| motanu | varchar(300) | NO |  |  |  |
| codemp | varchar(15) | NO | MUL |  |  |
| horanu | tinyint(3) | NO |  | 1 |  |
| codclas | varchar(4) | NO | MUL |  |  |
| fecdoc | date | NO |  | 2000-01-01 |  |
| tipo | char(1) | NO |  | A |  |
| codem2 | varchar(15) | NO |  |  |  |

**Muestras (3 filas):**

```json
[
  {
    "numnum": "16",
    "fecanu": "2026-06-04",
    "motanu": "ERROR",
    "codemp": "1151970853",
    "horanu": "16",
    "codclas": "S18",
    "fecdoc": "2026-05-17",
    "tipo": "M",
    "codem2": "1151970853"
  },
  {
    "numnum": "18",
    "fecanu": "2026-06-04",
    "motanu": "error",
    "codemp": "1151970853",
    "horanu": "17",
    "codclas": "S18",
    "fecdoc": "2026-06-04",
    "tipo": "A",
    "codem2": "1151970853"
  },
  {
    "numnum": "16",
    "fecanu": "2026-06-09",
    "motanu": "AGREGAR PRODUCTO",
    "codemp": "1151970853",
    "horanu": "19",
    "codclas": "S18",
    "fecdoc": "2026-05-17",
    "tipo": "M",
    "codem2": "1151970853"
  }
]
```

---

## `nomiconcep` (75 filas)

| Campo | Tipo | Nulo | Key | Default | Extra |
|-------|------|------|-----|---------|-------|
| codcon | varchar(4) | NO | MUL |  |  |
| nomcon | varchar(150) | NO |  |  |  |
| tipcon | char(1) | NO |  | 1 |  |
| tiptip | char(2) | NO |  | 1 |  |
| codnel1 | varchar(2) | NO |  |  |  |
| codnel2 | varchar(2) | NO |  |  |  |
| colexel | tinyint(3) | NO |  | 0 |  |
| porfac | float | NO |  | 0 |  |
| actcon | char(1) | NO |  | N |  |

**Muestras (3 filas):**

```json
[
  {
    "codcon": "001",
    "nomcon": "SUELDOS",
    "tipcon": "1",
    "tiptip": "1",
    "codnel1": "01",
    "codnel2": "1",
    "colexel": "1",
    "porfac": "0.0",
    "actcon": "S"
  },
  {
    "codcon": "002",
    "nomcon": "AUXILIO DE TRANSPORTE",
    "tipcon": "1",
    "tiptip": "5",
    "codnel1": "02",
    "codnel2": "1",
    "colexel": "4",
    "porfac": "0.0",
    "actcon": "S"
  },
  {
    "codcon": "003",
    "nomcon": "VIATICOS",
    "tipcon": "1",
    "tiptip": "5",
    "codnel1": "02",
    "codnel2": "2",
    "colexel": "0",
    "porfac": "0.0",
    "actcon": "N"
  }
]
```

---

## `nomiconcuf` (64 filas)

| Campo | Tipo | Nulo | Key | Default | Extra |
|-------|------|------|-----|---------|-------|
| codadm | char(3) | NO | MUL |  |  |
| codcon | varchar(4) | NO | MUL |  |  |
| tippar | char(1) | NO |  | G |  |
| nitter | varchar(15) | NO | MUL |  |  |
| cuedeb | varchar(20) | NO | MUL |  |  |
| cuecre | varchar(20) | NO | MUL |  |  |
| nitdeb | varchar(15) | NO |  |  |  |
| nitcre | varchar(15) | NO |  |  |  |
| tipfij | char(1) | NO |  | S |  |
| codsum | char(3) | NO | MUL |  |  |
| valopf | double | NO |  | 0 |  |

**Muestras (3 filas):**

```json
[
  {
    "codadm": "C1",
    "codcon": "001",
    "tippar": "G",
    "nitter": "",
    "cuedeb": "51050601",
    "cuecre": "",
    "nitdeb": "",
    "nitcre": "",
    "tipfij": "S",
    "codsum": "",
    "valopf": "0.0"
  },
  {
    "codadm": "C1",
    "codcon": "002",
    "tippar": "G",
    "nitter": "",
    "cuedeb": "51052701",
    "cuecre": "",
    "nitdeb": "",
    "nitcre": "",
    "tipfij": "S",
    "codsum": "",
    "valopf": "0.0"
  },
  {
    "codadm": "C1",
    "codcon": "005",
    "tippar": "G",
    "nitter": "",
    "cuedeb": "51051501",
    "cuecre": "",
    "nitdeb": "",
    "nitcre": "",
    "tipfij": "S",
    "codsum": "",
    "valopf": "0.0"
  }
]
```

---

## `nomiconempl` (0 filas)

| Campo | Tipo | Nulo | Key | Default | Extra |
|-------|------|------|-----|---------|-------|
| codcon | varchar(4) | NO | MUL |  |  |
| nitter | varchar(15) | NO | MUL |  |  |
| tippar | char(1) | NO |  |  |  |

**Muestras (3 filas):**

```json
[]
```

---

## `nominas` (0 filas)

| Campo | Tipo | Nulo | Key | Default | Extra |
|-------|------|------|-----|---------|-------|
| numnom | varchar(20) | NO | MUL |  |  |
| nomdoc | varchar(100) | NO |  | NOMINA EMPLEADOS |  |
| prenom | varchar(8) | NO |  | NOM |  |
| fecnom | datetime | NO |  | 2000-01-20 00:00:00 |  |
| inifec | date | NO |  | 2000-01-20 |  |
| finfec | date | NO |  | 2000-01-20 |  |
| nitter | varchar(15) | NO | MUL |  |  |
| ternom | varchar(120) | NO |  |  |  |
| totdev | double | NO |  | 0 |  |
| totded | double | NO |  | 0 |  |
| tottot | double | NO |  | 0 |  |
| totapro | double | NO |  | 0 |  |
| obsnom | varchar(2000) | NO |  |  |  |
| estnom | char(1) | NO |  |  |  |
| codemp | varchar(15) | NO | MUL |  |  |
| hornom | tinyint(3) | NO |  | 1 |  |
| codres | varchar(4) | NO | MUL |  |  |
| codclas | varchar(4) | NO | MUL |  |  |
| cienom | char(1) | NO |  | S |  |
| codcos | varchar(6) | NO | MUL |  |  |
| empcod | varchar(3) | NO | MUL |  |  |
| agrupa | char(1) | NO |  |  |  |
| numcon | varchar(15) | NO | MUL |  |  |
| tipnom | char(1) | NO |  | 3 |  |
| tpajus | char(1) | NO |  | P |  |
| cruclas | varchar(4) | NO |  |  |  |
| crunum | varchar(20) | NO |  |  |  |
| veridoc | tinyint(1) | NO |  | 0 |  |
| feccrea | datetime | NO |  | 2000-01-20 00:00:00 |  |

**Muestras (3 filas):**

```json
[]
```

---

## `nomisumcab` (4 filas)

| Campo | Tipo | Nulo | Key | Default | Extra |
|-------|------|------|-----|---------|-------|
| codsum | char(3) | NO | PRI |  |  |
| nomsum | varchar(100) | NO |  |  |  |
| sumtdv | char(1) | NO |  | T |  |
| baseval | double | NO |  | 0 |  |

**Muestras (3 filas):**

```json
[
  {
    "codsum": "001",
    "nomsum": "IBC - SEGURIDAD SOCIAL",
    "sumtdv": "T",
    "baseval": "0.0"
  },
  {
    "codsum": "002",
    "nomsum": "IBC - PARAFISCALES",
    "sumtdv": "T",
    "baseval": "0.0"
  },
  {
    "codsum": "003",
    "nomsum": "IBC - PRESTACIONES SOCIALES",
    "sumtdv": "T",
    "baseval": "0.0"
  }
]
```

---

## `nomisumdet` (3 filas)

| Campo | Tipo | Nulo | Key | Default | Extra |
|-------|------|------|-----|---------|-------|
| codsum | char(3) | NO | MUL |  |  |
| codcon | varchar(4) | NO | MUL |  |  |
| sumres | int(4) | NO |  | 1 |  |

**Muestras (3 filas):**

```json
[
  {
    "codsum": "001",
    "codcon": "002",
    "sumres": "-1"
  },
  {
    "codsum": "002",
    "codcon": "002",
    "sumres": "-1"
  },
  {
    "codsum": "004",
    "codcon": "001",
    "sumres": "1"
  }
]
```

---

## `notabodegas` (0 filas)

| Campo | Tipo | Nulo | Key | Default | Extra |
|-------|------|------|-----|---------|-------|
| numnum | varchar(20) | NO | MUL | 0 |  |
| codclas | varchar(4) | NO | MUL |  |  |
| predoc | varchar(8) | NO |  |  |  |
| nomdoc | varchar(100) | NO |  | NOTA DE AJUSTE DE BODEGAS |  |
| fecdoc | datetime | NO |  | 2000-01-20 00:00:00 |  |
| nitter | varchar(15) | NO | MUL |  |  |
| docext | varchar(20) | NO |  |  |  |
| concep | varchar(200) | NO |  |  |  |
| obsdoc | varchar(400) | NO |  |  |  |
| estdoc | char(1) | NO |  |  |  |
| codemp | varchar(15) | NO | MUL |  |  |
| codres | varchar(4) | NO |  |  |  |
| afebod | char(1) | NO |  | S |  |
| dirter | varchar(100) | NO |  |  |  |
| telter | varchar(50) | NO |  |  |  |
| codciu | varchar(6) | NO |  |  |  |
| empcod | varchar(3) | NO |  |  |  |
| agrupa | char(1) | NO |  |  |  |
| auxtex1 | varchar(100) | NO |  |  |  |
| auxtex2 | varchar(100) | NO |  |  |  |
| nittra | varchar(15) | NO | MUL |  |  |
| nomtra | varchar(120) | NO |  |  |  |
| veridoc | tinyint(1) | NO |  | 0 |  |
| feccrea | datetime | NO |  | 2000-01-20 00:00:00 |  |

**Muestras (3 filas):**

```json
[]
```

---

## `notascxccxp` (1 filas)

| Campo | Tipo | Nulo | Key | Default | Extra |
|-------|------|------|-----|---------|-------|
| numnot | varchar(20) | NO | MUL |  |  |
| codclas | varchar(4) | NO | MUL |  |  |
| nomdoc | varchar(100) | NO |  | NOTA DEBITO |  |
| prenot | varchar(8) | NO |  | NC |  |
| fecnot | datetime | NO |  | 2000-01-20 00:00:00 |  |
| nitter | varchar(15) | NO | MUL |  |  |
| digver | char(2) | NO |  |  |  |
| codsuc | varchar(15) | NO | MUL |  |  |
| clinot | varchar(120) | NO |  |  |  |
| dirnot | varchar(100) | NO |  |  |  |
| telnot | varchar(50) | NO |  |  |  |
| codpag | varchar(4) | NO |  |  |  |
| afeclas | varchar(4) | NO |  |  |  |
| numfac | varchar(20) | NO | MUL |  |  |
| numcuo | tinyint(3) | NO |  | 0 |  |
| docafe | varchar(5) | NO |  |  |  |
| diasnot | int(11) | NO |  | 0 |  |
| subnot | double | NO |  | 0 |  |
| totdct | double | NO |  | 0 |  |
| totiva | double | NO |  | 0 |  |
| totipo | double | NO |  | 0 |  |
| retfte | double | NO |  | 0 |  |
| retiva | double | NO |  | 0 |  |
| retica | double | NO |  | 0 |  |
| retcre | double | NO |  | 0 |  |
| ajuspe | double | NO |  | 0 |  |
| totnot | double | NO |  | 0 |  |
| obsnot | varchar(400) | NO |  |  |  |
| estnot | char(1) | NO |  |  |  |
| codemp | varchar(15) | NO | MUL |  |  |
| hornot | tinyint(3) | NO |  | 1 |  |
| codres | varchar(4) | NO | MUL |  |  |
| codcos | varchar(6) | NO | MUL |  |  |
| codzon | varchar(4) | NO |  |  |  |
| codcaj | varchar(4) | NO | MUL |  |  |
| empcod | varchar(3) | NO | MUL |  |  |
| cauret | char(1) | NO |  |  |  |
| turno1 | char(1) | NO |  | 0 |  |
| agrupa | char(1) | NO |  |  |  |
| estfele | char(1) | NO |  | N |  |
| resfele | int(6) | NO |  | 0 |  |
| motivor | char(1) | NO |  |  |  |
| perdes | date | NO |  | 2010-01-01 |  |
| perhas | date | NO |  | 2010-01-01 |  |
| corele | varchar(100) | NO |  |  |  |
| otrimp | double | NO |  | 0 |  |
| dctglob | double | NO |  | 0 |  |
| recglob | double | NO |  | 0 |  |
| tazacam | double | NO |  | 0 |  |
| moneda | varchar(4) | NO |  |  |  |
| veridoc | tinyint(1) | NO |  | 0 |  |
| feccrea | datetime | NO |  | 2000-01-20 00:00:00 |  |

**Muestras (3 filas):**

```json
[
  {
    "numnot": "1",
    "codclas": "S16",
    "nomdoc": "DEVOLUCION POS",
    "prenot": "DP",
    "fecnot": "2026-06-09 11:12:12",
    "nitter": "",
    "digver": "",
    "codsuc": "",
    "clinot": "",
    "dirnot": "",
    "telnot": "",
    "codpag": "F01",
    "afeclas": "S15",
    "numfac": "5",
    "numcuo": "0",
    "docafe": "",
    "diasnot": "0",
    "subnot": "24600.0",
    "totdct": "0.0",
    "totiva": "0.0",
    "totipo": "0.0",
    "retfte": "0.0",
    "retiva": "0.0",
    "retica": "0.0",
    "retcre": "0.0",
    "ajuspe": "0.0",
    "totnot": "24600.0",
    "obsnot": " ",
    "estnot": "B",
    "codemp": "1151970853",
    "hornot": "11",
    "codres": "",
    "codcos": "",
    "codzon": "",
    "codcaj": "C1",
    "empcod": "",
    "cauret": "S",
    "turno1": "0",
    "agrupa": "",
    "estfele": "N",
    "resfele": "0",
    "motivor": "5",
    "perdes": "2026-06-09",
    "perhas": "2026-06-09",
    "corele": "",
    "otrimp": "0.0",
    "dctglob": "0.0",
    "recglob": "0.0",
    "tazacam": "0.0",
    "moneda": "COP",
    "veridoc": "0",
    "feccrea": "2026-06-09 11:12:53"
  }
]
```

---

## `paises` (9 filas)

| Campo | Tipo | Nulo | Key | Default | Extra |
|-------|------|------|-----|---------|-------|
| codpais | varchar(3) | NO | PRI |  |  |
| nompais | varchar(150) | NO |  |  |  |
| codfel1 | varchar(6) | NO | MUL |  |  |

**Muestras (3 filas):**

```json
[
  {
    "codpais": "CO",
    "nompais": "Colombia",
    "codfel1": "46"
  },
  {
    "codpais": "EC",
    "nompais": "Ecuador",
    "codfel1": "57"
  },
  {
    "codpais": "PE",
    "nompais": "Peru",
    "codfel1": "178"
  }
]
```

---

## `paraciecue` (0 filas)

| Campo | Tipo | Nulo | Key | Default | Extra |
|-------|------|------|-----|---------|-------|
| codper | varchar(4) | NO | MUL |  |  |
| cuedes | varchar(12) | NO |  |  |  |
| cuehas | varchar(12) | NO |  |  |  |
| cuefin | varchar(12) | NO |  |  |  |

**Muestras (3 filas):**

```json
[]
```

---

## `parametros` (88 filas)

| Campo | Tipo | Nulo | Key | Default | Extra |
|-------|------|------|-----|---------|-------|
| tipo | varchar(12) | NO |  |  |  |
| valor | varchar(15) | NO |  |  |  |
| codcon | varchar(4) | NO | MUL |  |  |
| codcaj | varchar(4) | NO | MUL |  |  |
| desadi | varchar(400) | NO |  |  |  |
| desad2 | varchar(50) | NO |  |  |  |
| empcod | varchar(3) | NO | MUL |  |  |

**Muestras (3 filas):**

```json
[
  {
    "tipo": "DECIGEN",
    "valor": "2",
    "codcon": "",
    "codcaj": "",
    "desadi": "",
    "desad2": "",
    "empcod": ""
  },
  {
    "tipo": "STOCKMIN",
    "valor": "NO",
    "codcon": "",
    "codcaj": "",
    "desadi": "",
    "desad2": "",
    "empcod": ""
  },
  {
    "tipo": "STOCKMAX",
    "valor": "NO",
    "codcon": "",
    "codcaj": "",
    "desadi": "",
    "desad2": "",
    "empcod": ""
  }
]
```

---

## `paranomicos` (2 filas)

| Campo | Tipo | Nulo | Key | Default | Extra |
|-------|------|------|-----|---------|-------|
| codadm | char(3) | NO | PRI |  |  |
| desadm | varchar(50) | NO |  |  |  |

**Muestras (3 filas):**

```json
[
  {
    "codadm": "C1",
    "desadm": "ADMINISTRACION"
  },
  {
    "codadm": "C2",
    "desadm": "VENTAS"
  }
]
```

---

## `pararepcxcp` (5 filas)

| Campo | Tipo | Nulo | Key | Default | Extra |
|-------|------|------|-----|---------|-------|
| codcue | varchar(12) | NO | MUL |  |  |
| tipcar | char(1) | NO |  |  |  |

**Muestras (3 filas):**

```json
[
  {
    "codcue": "28050501",
    "tipcar": "1"
  },
  {
    "codcue": "13659501",
    "tipcar": "1"
  },
  {
    "codcue": "22050101",
    "tipcar": "2"
  }
]
```

---

## `parinfcabniif` (0 filas)

| Campo | Tipo | Nulo | Key | Default | Extra |
|-------|------|------|-----|---------|-------|
| codigo | smallint(6) | NO | MUL | 0 |  |
| orden | smallint(4) | NO |  | 0 |  |
| descon | varchar(250) | NO |  |  |  |
| codper | varchar(2) | NO |  |  |  |
| tipo1 | char(1) | NO |  |  |  |
| valor1 | double | NO |  | 0 |  |
| valor2 | double | NO |  | 0 |  |
| somlet | char(1) | NO |  |  |  |
| codcue | varchar(12) | NO |  |  |  |
| nomcue | varchar(150) | NO |  |  |  |
| grurev | char(1) | NO |  | 1 |  |
| numrev | int(4) | NO |  | 0 |  |
| tiprev | char(1) | NO |  |  |  |
| obsrev | varchar(2000) | NO |  |  |  |

**Muestras (3 filas):**

```json
[]
```

---

## `parinfcontab` (25 filas)

| Campo | Tipo | Nulo | Key | Default | Extra |
|-------|------|------|-----|---------|-------|
| codper | varchar(4) | NO | MUL |  |  |
| codcue | varchar(20) | NO | MUL |  |  |
| sumres | int(4) | NO |  | 1 |  |
| natprin | char(1) | NO |  |  |  |
| tipo | smallint(3) | NO |  | 1 |  |

**Muestras (3 filas):**

```json
[
  {
    "codper": "LINB",
    "codcue": "9",
    "sumres": "1",
    "natprin": "C",
    "tipo": "1"
  },
  {
    "codper": "LINB",
    "codcue": "8",
    "sumres": "1",
    "natprin": "D",
    "tipo": "1"
  },
  {
    "codper": "LINB",
    "codcue": "7",
    "sumres": "1",
    "natprin": "D",
    "tipo": "1"
  }
]
```

---

## `parinfdetniif` (0 filas)

| Campo | Tipo | Nulo | Key | Default | Extra |
|-------|------|------|-----|---------|-------|
| codigo | smallint(6) | NO | MUL | 0 |  |
| codcue | varchar(12) | NO |  |  |  |
| tipo2 | char(1) | NO |  |  |  |
| codcod | smallint(6) | NO | MUL | 0 |  |
| sumres | int(4) | NO |  | 1 |  |

**Muestras (3 filas):**

```json
[]
```

---

## `pedidores` (0 filas)

| Campo | Tipo | Nulo | Key | Default | Extra |
|-------|------|------|-----|---------|-------|
| numped | varchar(20) | NO | MUL |  |  |
| codmes | varchar(4) | NO | MUL |  |  |
| nitter | varchar(15) | NO | MUL |  |  |
| nitmes | varchar(15) | NO | MUL |  |  |
| fecped | datetime | NO |  | 2000-01-01 00:00:00 |  |
| fecdesp | datetime | NO |  | 2000-01-01 00:00:00 |  |
| estado | char(1) | NO |  |  |  |
| codsuc | varchar(15) | NO |  |  |  |
| numreg | varchar(20) | NO |  |  |  |
| estimp | char(1) | NO |  |  |  |
| estiemp | char(1) | NO |  | 0 |  |
| horini | datetime | NO |  | 2000-01-01 00:00:00 |  |
| comanum | varchar(20) | NO |  |  |  |
| codclas | varchar(4) | NO | MUL | P01 |  |
| predoc | varchar(8) | NO |  |  |  |
| nomdoc | varchar(100) | NO |  |  |  |
| nomcli | varchar(150) | NO |  |  |  |
| telter | varchar(30) | NO |  |  |  |
| dirter | varchar(100) | NO |  |  |  |
| dirzon | varchar(100) | NO |  |  |  |
| dirref | varchar(100) | NO |  |  |  |
| obsdoc | varchar(400) | NO |  |  |  |
| priorid | char(2) | NO |  |  |  |
| valdom | double | NO |  | 0 |  |
| codpag | varchar(4) | NO | MUL |  |  |
| codemp | varchar(15) | NO | MUL |  |  |
| empdomi | varchar(30) | NO |  |  |  |
| tipdomi | char(1) | NO |  |  |  |
| estdoc | char(1) | NO |  |  |  |
| empcod | varchar(3) | NO | MUL |  |  |
| horfin | datetime | NO |  | 2000-01-01 00:00:00 |  |

**Muestras (3 filas):**

```json
[]
```

---

## `permisoscab` (128 filas)

| Campo | Tipo | Nulo | Key | Default | Extra |
|-------|------|------|-----|---------|-------|
| codper | varchar(4) | NO | PRI |  |  |
| nommen | varchar(100) | NO |  |  |  |
| nuevo | char(2) | NO |  | NO |  |
| editar | char(2) | NO |  | NO |  |
| eliminar | char(2) | NO |  | NO |  |
| buscar | char(2) | NO |  | NO |  |
| desplazar | char(2) | NO |  | NO |  |
| imprimir | char(2) | NO |  | NO |  |
| causacion | char(2) | NO |  | NO |  |
| aditer | char(2) | NO |  | NO |  |
| traer | char(2) | NO |  | NO |  |
| todo | char(2) | NO |  | NO |  |
| numord | smallint(4) | NO |  | 1 |  |
| tipo | char(1) | NO |  | 1 |  |
| menu | char(2) | NO |  | 0 |  |
| adjuntar | char(2) | NO |  | NO |  |
| deshacer | char(2) | NO |  | NO |  |

**Muestras (3 filas):**

```json
[
  {
    "codper": "O051",
    "nommen": "Documentos electr├│nicos",
    "nuevo": "NO",
    "editar": "NO",
    "eliminar": "NO",
    "buscar": "NO",
    "desplazar": "NO",
    "imprimir": "NO",
    "causacion": "NO",
    "aditer": "NO",
    "traer": "NO",
    "todo": "SI",
    "numord": "105",
    "tipo": "1",
    "menu": "3",
    "adjuntar": "NO",
    "deshacer": "NO"
  },
  {
    "codper": "N002",
    "nommen": "Empresa",
    "nuevo": "NO",
    "editar": "SI",
    "eliminar": "NO",
    "buscar": "NO",
    "desplazar": "NO",
    "imprimir": "NO",
    "causacion": "NO",
    "aditer": "NO",
    "traer": "NO",
    "todo": "NO",
    "numord": "2",
    "tipo": "1",
    "menu": "1",
    "adjuntar": "NO",
    "deshacer": "NO"
  },
  {
    "codper": "N003",
    "nommen": "Cat├ílogo de productos",
    "nuevo": "SI",
    "editar": "SI",
    "eliminar": "SI",
    "buscar": "SI",
    "desplazar": "SI",
    "imprimir": "NO",
    "causacion": "NO",
    "aditer": "NO",
    "traer": "NO",
    "todo": "NO",
    "numord": "3",
    "tipo": "1",
    "menu": "1",
    "adjuntar": "NO",
    "deshacer": "NO"
  }
]
```

---

## `permisosfac` (2 filas)

| Campo | Tipo | Nulo | Key | Default | Extra |
|-------|------|------|-----|---------|-------|
| modpre | char(2) | NO |  | NO |  |
| aplidct | char(2) | NO |  | NO |  |
| modiva | char(2) | NO |  | NO |  |
| modipo | char(2) | NO |  |  |  |
| vercup | char(2) | NO |  | NO |  |
| devcam | char(2) | NO |  | NO |  |
| nitter | varchar(15) | NO | MUL |  |  |
| modcau | char(2) | NO |  | NO |  |
| valcup | double | NO |  | 0 |  |
| vercos | char(2) | NO |  | NO |  |
| arqcaj | char(2) | NO |  | NO |  |
| borite | char(2) | NO |  | SI |  |
| modcup | char(2) | NO |  | SI |  |
| maxdia | smallint(6) | NO |  | 0 |  |
| apli2dct | char(2) | NO |  | NO |  |
| facele | char(2) | NO |  | NO |  |
| mosdisp | char(2) | NO |  | SI |  |
| numatr | smallint(6) | NO |  | 0 |  |
| modkit | char(2) | NO |  | NO |  |
| arcaj2 | char(2) | NO |  | NO |  |
| camclav | char(2) | NO |  | SI |  |
| bsprod1 | char(2) | NO |  | SI |  |
| crudoc | char(2) | NO |  | SI |  |

**Muestras (3 filas):**

```json
[
  {
    "modpre": "NO",
    "aplidct": "NO",
    "modiva": "NO",
    "modipo": "NO",
    "vercup": "0",
    "devcam": "NO",
    "nitter": "1085343471",
    "modcau": "NO",
    "valcup": "0.0",
    "vercos": "NO",
    "arqcaj": "SI",
    "borite": "NO",
    "modcup": "NO",
    "maxdia": "0",
    "apli2dct": "NO",
    "facele": "NO",
    "mosdisp": "NO",
    "numatr": "0",
    "modkit": "NO",
    "arcaj2": "NO",
    "camclav": "SI",
    "bsprod1": "SI",
    "crudoc": "NO"
  },
  {
    "modpre": "NO",
    "aplidct": "NO",
    "modiva": "NO",
    "modipo": "NO",
    "vercup": "0",
    "devcam": "NO",
    "nitter": "29121236",
    "modcau": "NO",
    "valcup": "0.0",
    "vercos": "NO",
    "arqcaj": "SI",
    "borite": "NO",
    "modcup": "NO",
    "maxdia": "0",
    "apli2dct": "NO",
    "facele": "NO",
    "mosdisp": "NO",
    "numatr": "0",
    "modkit": "NO",
    "arcaj2": "NO",
    "camclav": "SI",
    "bsprod1": "SI",
    "crudoc": "NO"
  }
]
```

---

## `permisosusu` (0 filas)

| Campo | Tipo | Nulo | Key | Default | Extra |
|-------|------|------|-----|---------|-------|
| codper | varchar(4) | NO | MUL |  |  |
| nuevo | char(2) | NO |  | NO |  |
| editar | char(2) | NO |  | NO |  |
| eliminar | char(2) | NO |  | NO |  |
| buscar | char(2) | NO |  | NO |  |
| desplazar | char(2) | NO |  | NO |  |
| imprimir | char(2) | NO |  | NO |  |
| causacion | char(2) | NO |  | NO |  |
| aditer | char(2) | NO |  | NO |  |
| traer | char(2) | NO |  | NO |  |
| todo | char(2) | NO |  | NO |  |
| nitter | varchar(15) | NO | MUL |  |  |
| adjuntar | char(2) | NO |  | NO |  |
| deshacer | char(2) | NO |  | SI |  |

**Muestras (3 filas):**

```json
[]
```

---

## `preciosxdct` (0 filas)

| Campo | Tipo | Nulo | Key | Default | Extra |
|-------|------|------|-----|---------|-------|
| codprod | varchar(20) | NO | MUL |  |  |
| nivlin | smallint(6) | NO |  | 0 |  |
| codlin | varchar(4) | NO |  |  |  |
| cansin | char(2) | NO |  | NO |  |
| valcan | double | NO |  | 0 |  |
| fecsin | char(2) | NO |  | NO |  |
| fecdes | datetime | NO |  | 2000-01-02 00:00:00 |  |
| fechas | datetime | NO |  | 2000-01-01 00:00:00 |  |
| pordct | float | NO |  | 0 |  |
| codlin1 | char(4) | NO |  |  |  |
| codlin2 | char(4) | NO |  |  |  |
| codlin3 | char(4) | NO |  |  |  |
| codlin4 | char(4) | NO |  |  |  |
| codlin5 | char(4) | NO |  |  |  |
| codlin6 | char(4) | NO |  |  |  |

**Muestras (3 filas):**

```json
[]
```

---

## `preciosxpro` (13 filas)

| Campo | Tipo | Nulo | Key | Default | Extra |
|-------|------|------|-----|---------|-------|
| codprod | varchar(20) | NO | MUL |  |  |
| codlis | char(3) | NO | MUL |  |  |
| venprod | double | NO |  | 0 |  |
| veniva | double | NO |  | 0 |  |
| porutil | float | NO |  | 0 |  |
| actupr | char(1) | NO |  | N |  |
| pvtipo | char(1) | NO |  |  |  |

**Muestras (3 filas):**

```json
[
  {
    "codprod": "MILDA0012",
    "codlis": "L2",
    "venprod": "6300.0",
    "veniva": "0.0",
    "porutil": "0.0",
    "actupr": "",
    "pvtipo": "2"
  },
  {
    "codprod": "2344",
    "codlis": "L2",
    "venprod": "16100.0",
    "veniva": "0.0",
    "porutil": "0.0",
    "actupr": "",
    "pvtipo": "2"
  },
  {
    "codprod": "LATIT001",
    "codlis": "L2",
    "venprod": "40000.0",
    "veniva": "0.0",
    "porutil": "0.0",
    "actupr": "",
    "pvtipo": "2"
  }
]
```

---

## `presupanos` (0 filas)

| Campo | Tipo | Nulo | Key | Default | Extra |
|-------|------|------|-----|---------|-------|
| codano | smallint(6) | NO | PRI | 0 |  |
| estado | char(1) | NO |  |  |  |

**Muestras (3 filas):**

```json
[]
```

---

## `presupuesto` (0 filas)

| Campo | Tipo | Nulo | Key | Default | Extra |
|-------|------|------|-----|---------|-------|
| numpre | varchar(20) | NO | MUL |  |  |
| codclas | varchar(4) | NO | MUL |  |  |
| nomdoc | varchar(100) | NO |  | PRESUPUESTO |  |
| prepre | varchar(8) | NO |  |  |  |
| fecpre | datetime | NO |  | 2000-01-01 00:00:00 |  |
| fechas | date | NO |  | 2000-01-01 |  |
| nitter | varchar(15) | NO | MUL |  |  |
| conpre | varchar(300) | NO |  |  |  |
| estpre | char(1) | NO |  |  |  |
| codemp | varchar(15) | NO | MUL |  |  |
| empcod | varchar(3) | NO | MUL |  |  |
| digter | char(2) | NO |  |  |  |
| nomter | varchar(100) | NO |  |  |  |
| dirter | varchar(100) | NO |  |  |  |
| telter | varchar(50) | NO |  |  |  |
| numcru | varchar(20) | NO |  |  |  |
| clascru | varchar(4) | NO |  |  |  |
| conpr2 | varchar(300) | NO |  |  |  |
| tippre | char(2) | NO |  |  |  |
| codano | smallint(6) | NO | MUL | 0 |  |
| veridoc | tinyint(1) | NO |  | 0 |  |
| feccrea | datetime | NO |  | 2000-01-20 00:00:00 |  |

**Muestras (3 filas):**

```json
[]
```

---

## `prodactfij` (0 filas)

| Campo | Tipo | Nulo | Key | Default | Extra |
|-------|------|------|-----|---------|-------|
| codprod | varchar(20) | NO | MUL |  |  |
| numpla | varchar(20) | NO |  |  |  |
| nommar | varchar(50) | NO |  |  |  |
| numser | varchar(30) | NO |  |  |  |
| feccom | date | NO |  | 2000-01-20 |  |
| preadq | double | NO |  | 0 |  |
| vidutil | int(8) | NO |  | 0 |  |
| tipvid | char(1) | NO |  |  |  |
| codcos | varchar(6) | NO | MUL |  |  |
| fecdep | date | NO |  | 2000-01-20 |  |
| nitter | varchar(15) | NO | MUL |  |  |
| numcom | varchar(20) | NO | MUL |  |  |
| pordep | float | NO |  | 0 |  |
| ubiact | varchar(50) | NO |  |  |  |
| nitres | varchar(15) | NO | MUL |  |  |
| tieseg | char(2) | NO |  | NO |  |
| venseg | date | NO |  | 2000-01-20 |  |
| tiegar | char(2) | NO |  | NO |  |
| vengar | date | NO |  | 2000-01-20 |  |
| detgar | varchar(100) | NO |  |  |  |

**Muestras (3 filas):**

```json
[]
```

---

## `prodacttar` (0 filas)

| Campo | Tipo | Nulo | Key | Default | Extra |
|-------|------|------|-----|---------|-------|
| codprod | varchar(20) | NO | MUL |  |  |
| numano | int(8) | NO |  | 0 |  |
| nummes | tinyint(3) | NO |  | 0 |  |
| valdep1 | double | NO |  | 0 |  |
| valdep2 | double | NO |  | 0 |  |
| valdep3 | double | NO |  | 0 |  |

**Muestras (3 filas):**

```json
[]
```

---

## `prodcamposad` (0 filas)

| Campo | Tipo | Nulo | Key | Default | Extra |
|-------|------|------|-----|---------|-------|
| codprod | varchar(20) | NO | MUL |  |  |
| nomgen | varchar(100) | NO |  |  |  |
| concent | varchar(30) | NO |  |  |  |
| forfarm | varchar(30) | NO |  |  |  |
| labora | varchar(50) | NO |  |  |  |
| titufab | varchar(100) | NO |  |  |  |
| presen | varchar(30) | NO |  |  |  |
| priact | varchar(150) | NO |  |  |  |

**Muestras (3 filas):**

```json
[]
```

---

## `prodcodbars` (0 filas)

| Campo | Tipo | Nulo | Key | Default | Extra |
|-------|------|------|-----|---------|-------|
| codprod | varchar(20) | NO | MUL |  |  |
| codbar | varchar(30) | NO | MUL |  |  |

**Muestras (3 filas):**

```json
[]
```

---

## `prodserlotes` (0 filas)

| Campo | Tipo | Nulo | Key | Default | Extra |
|-------|------|------|-----|---------|-------|
| codprod | varchar(20) | NO | MUL |  |  |
| sernum | varchar(40) | NO | MUL |  |  |
| serfec | varchar(10) | NO |  |  |  |
| feccrea | date | NO |  | 2020-01-01 |  |
| candet | double | NO |  | 0 |  |
| cosuni | double | NO |  | 0 |  |
| inaser | char(1) | NO |  | N |  |

**Muestras (3 filas):**

```json
[]
```

---

## `productos` (496 filas)

| Campo | Tipo | Nulo | Key | Default | Extra |
|-------|------|------|-----|---------|-------|
| codprod | varchar(20) | NO | PRI |  |  |
| codbar | varchar(40) | NO | MUL |  |  |
| nomprod | varchar(200) | NO |  |  |  |
| codmed | varchar(3) | NO | MUL |  |  |
| valmed | double | NO |  | 0 |  |
| presen | varchar(30) | NO |  |  |  |
| incserl | char(2) | NO |  | SI |  |
| inccum | char(2) | NO |  | NO |  |
| stockmin | double | NO |  | 0 |  |
| stockmax | double | NO |  | 0 |  |
| exiprod | double | NO |  | 0 |  |
| cosprod | double | NO |  | 0 |  |
| cosman | double | NO |  | 0 |  |
| cosulc | double | NO |  | 0 |  |
| cosant | double | NO |  | 0 |  |
| coskar | double | NO |  | 0 |  |
| tipcos | char(2) | NO |  | NO |  |
| pvsini | double | NO |  | 0 |  |
| pvconi | double | NO |  | 0 |  |
| pvtipo | char(1) | NO |  | 1 |  |
| menopre | double | NO |  | 0 |  |
| codpor | varchar(4) | NO | MUL |  |  |
| codpor2 | varchar(4) | NO |  |  |  |
| codpor3 | varchar(4) | NO |  |  |  |
| codlin1 | varchar(4) | NO | MUL |  |  |
| codlin2 | char(4) | NO |  |  |  |
| codlin3 | char(4) | NO |  |  |  |
| codlin4 | char(4) | NO |  |  |  |
| codlin5 | char(4) | NO |  |  |  |
| codlin6 | char(4) | NO |  |  |  |
| actprod | char(1) | NO |  | A |  |
| reginvi | varchar(30) | NO |  |  |  |
| regcum | varchar(30) | NO |  | NO |  |
| desprod | varchar(800) | NO |  |  |  |
| fotprod | varchar(255) | NO |  |  |  |
| fecapa | date | NO |  | 2013-01-01 |  |
| manser | char(1) | NO |  | N |  |
| moddet | char(1) | NO |  | N |  |
| pidfor | char(1) | NO |  |  |  |
| masiva | char(1) | NO |  |  |  |
| pidecos | char(1) | NO |  |  |  |
| fsinex | char(1) | NO |  |  |  |
| impinvi | char(2) | NO |  | NO |  |
| modipre | char(1) | NO |  | S |  |
| calcuni | char(1) | NO |  | N |  |
| noesven | char(1) | NO |  | N |  |
| infmin | char(1) | NO |  | N |  |
| tipsub | char(1) | NO |  |  |  |
| tipser | varchar(30) | NO |  |  |  |
| nitter | varchar(15) | NO | MUL |  |  |
| refprov | varchar(50) | NO |  |  |  |
| regica | varchar(30) | NO |  |  |  |
| titufab | varchar(100) | NO |  |  |  |
| valform | double | NO |  | 1 |  |
| actfij | char(1) | NO |  |  |  |
| nominv | char(1) | NO |  | N |  |
| actupr | char(1) | NO |  | N |  |
| aproxi | char(1) | NO |  | 0 |  |
| aplcomi | char(1) | NO |  | N |  |
| porcomi | float | NO |  | 0 |  |
| porutil | float | NO |  | 0 |  |
| factobs | float | NO |  | 0 |  |
| prbase | double | NO |  | 0 |  |
| minuto | smallint(3) | NO |  | 0 |  |
| puntos | double | NO |  | 0 |  |
| codcos | varchar(6) | NO | MUL |  |  |
| auxdet | varchar(150) | NO |  |  |  |
| multiplo | double | NO |  | 1 |  |
| inviica | char(1) | NO |  | 1 |  |
| lugimp | varchar(50) | NO |  |  |  |
| pesopro | double | NO |  | 0 |  |
| valpor2 | double | NO |  | 0 |  |
| pidobs1 | char(1) | NO |  |  |  |
| pidobs2 | char(1) | NO |  |  |  |
| lotcos | char(1) | NO |  |  |  |
| lotobl | char(1) | NO |  |  |  |
| codbod | varchar(4) | NO |  |  |  |
| incpres | char(2) | NO |  | NO |  |

**Muestras (3 filas):**

```json
[
  {
    "codprod": "7503008669079",
    "codbar": "7503008669079",
    "nomprod": "ACEITE DE COCO VIRGEN ORG├üNICO X 300 ML",
    "codmed": "001",
    "valmed": "0.0",
    "presen": "UNIDAD",
    "incserl": "SI",
    "inccum": "NO",
    "stockmin": "0.0",
    "stockmax": "0.0",
    "exiprod": "3.0",
    "cosprod": "0.0",
    "cosman": "0.0",
    "cosulc": "56292.0",
    "cosant": "0.0",
    "coskar": "56292.0",
    "tipcos": "AK",
    "pvsini": "70400.0",
    "pvconi": "70400.0",
    "pvtipo": "1",
    "menopre": "0.0",
    "codpor": "IV2",
    "codpor2": "",
    "codpor3": "IV2",
    "codlin1": "L01",
    "codlin2": "",
    "codlin3": "",
    "codlin4": "",
    "codlin5": "",
    "codlin6": "",
    "actprod": "A",
    "reginvi": "",
    "regcum": "",
    "desprod": "",
    "fotprod": "",
    "fecapa": "2026-05-24",
    "manser": "N",
    "moddet": "N",
    "pidfor": "N",
    "masiva": "N",
    "pidecos": "N",
    "fsinex": "N",
    "impinvi": "NO",
    "modipre": "S",
    "calcuni": "N",
    "noesven": "N",
    "infmin": "N",
    "tipsub": "",
    "tipser": "",
    "nitter": "",
    "refprov": "",
    "regica": "",
    "titufab": "",
    "valform": "1.0",
    "actfij": "",
    "nominv": "N",
    "actupr": "4",
    "aproxi": "0",
    "aplcomi": "N",
    "porcomi": "0.0",
    "porutil": "20.0",
    "factobs": "0.0",
    "prbase": "0.0",
    "minuto": "0",
    "puntos": "0.0",
    "codcos": "",
    "auxdet": "",
    "multiplo": "1.0",
    "inviica": "1",
    "lugimp": "",
    "pesopro": "0.0",
    "valpor2": "0.0",
    "pidobs1": "",
    "pidobs2": "",
    "lotcos": "",
    "lotobl": "",
    "codbod": "",
    "incpres": "NO"
  },
  {
    "codprod": "7503008669062",
    "codbar": "7503008669062",
    "nomprod": "ACEITE DE COCO VIRGEN CONVENCIONAL X 300 ML",
    "codmed": "001",
    "valmed": "0.0",
    "presen": "UNIDAD",
    "incserl": "SI",
    "inccum": "NO",
    "stockmin": "0.0",
    "stockmax": "0.0",
    "exiprod": "3.0",
    "cosprod": "0.0",
    "cosman": "0.0",
    "cosulc": "44228.0",
    "cosant": "0.0",
    "coskar": "44228.0",
    "tipcos": "AK",
    "pvsini": "55300.0",
    "pvconi": "55300.0",
    "pvtipo": "1",
    "menopre": "0.0",
    "codpor": "IV2",
    "codpor2": "",
    "codpor3": "IV2",
    "codlin1": "L01",
    "codlin2": "",
    "codlin3": "",
    "codlin4": "",
    "codlin5": "",
    "codlin6": "",
    "actprod": "A",
    "reginvi": "",
    "regcum": "",
    "desprod": "",
    "fotprod": "",
    "fecapa": "2026-05-24",
    "manser": "N",
    "moddet": "N",
    "pidfor": "N",
    "masiva": "N",
    "pidecos": "N",
    "fsinex": "N",
    "impinvi": "NO",
    "modipre": "S",
    "calcuni": "N",
    "noesven": "N",
    "infmin": "N",
    "tipsub": "",
    "tipser": "",
    "nitter": "",
    "refprov": "",
    "regica": "",
    "titufab": "",
    "valform": "1.0",
    "actfij": "",
    "nominv": "N",
    "actupr": "4",
    "aproxi": "0",
    "aplcomi": "N",
    "porcomi": "0.0",
    "porutil": "20.0",
    "factobs": "0.0",
    "prbase": "0.0",
    "minuto": "0",
    "puntos": "0.0",
    "codcos": "",
    "auxdet": "",
    "multiplo": "1.0",
    "inviica": "1",
    "lugimp": "",
    "pesopro": "0.0",
    "valpor2": "0.0",
    "pidobs1": "",
    "pidobs2": "",
    "lotcos": "",
    "lotobl": "",
    "codbod": "",
    "incpres": "NO"
  },
  {
    "codprod": "7503008669147",
    "codbar": "7503008669147",
    "nomprod": "AGUA DE COCO 100% NATURAL X 1 L",
    "codmed": "001",
    "valmed": "0.0",
    "presen": "UNIDAD",
    "incserl": "SI",
    "inccum": "NO",
    "stockmin": "0.0",
    "stockmax": "0.0",
    "exiprod": "6.0",
    "cosprod": "0.0",
    "cosman": "0.0",
    "cosulc": "23130.0",
    "cosant": "0.0",
    "coskar": "23130.0",
    "tipcos": "AK",
    "pvsini": "28900.0",
    "pvconi": "28900.0",
    "pvtipo": "1",
    "menopre": "0.0",
    "codpor": "IV2",
    "codpor2": "",
    "codpor3": "IV2",
    "codlin1": "L01",
    "codlin2": "",
    "codlin3": "",
    "codlin4": "",
    "codlin5": "",
    "codlin6": "",
    "actprod": "A",
    "reginvi": "",
    "regcum": "",
    "desprod": "",
    "fotprod": "",
    "fecapa": "2026-05-24",
    "manser": "N",
    "moddet": "N",
    "pidfor": "N",
    "masiva": "N",
    "pidecos": "N",
    "fsinex": "N",
    "impinvi": "NO",
    "modipre": "S",
    "calcuni": "N",
    "noesven": "N",
    "infmin": "N",
    "tipsub": "",
    "tipser": "",
    "nitter": "",
    "refprov": "",
    "regica": "",
    "titufab": "",
    "valform": "1.0",
    "actfij": "",
    "nominv": "N",
    "actupr": "4",
    "aproxi": "0",
    "aplcomi": "N",
    "porcomi": "0.0",
    "porutil": "20.0",
    "factobs": "0.0",
    "prbase": "0.0",
    "minuto": "0",
    "puntos": "0.0",
    "codcos": "",
    "auxdet": "",
    "multiplo": "1.0",
    "inviica": "1",
    "lugimp": "",
    "pesopro": "0.0",
    "valpor2": "0.0",
    "pidobs1": "",
    "pidobs2": "",
    "lotcos": "",
    "lotobl": "",
    "codbod": "",
    "incpres": "NO"
  }
]
```

---

## `produndmeds` (0 filas)

| Campo | Tipo | Nulo | Key | Default | Extra |
|-------|------|------|-----|---------|-------|
| codprod | varchar(20) | NO | MUL |  |  |
| codmed | varchar(3) | NO | MUL |  |  |
| divmul | char(1) | NO |  | M |  |
| facumed | double | NO |  | 1 |  |
| pventa | double | NO |  | 0 |  |
| tipovc | char(1) | NO |  | 0 |  |
| presen | varchar(30) | NO |  |  |  |

**Muestras (3 filas):**

```json
[]
```

---

## `provetecno` (0 filas)

| Campo | Tipo | Nulo | Key | Default | Extra |
|-------|------|------|-----|---------|-------|
| codpro | varchar(2) | NO | MUL |  |  |
| activo | varchar(1) | NO |  |  |  |
| token1 | varchar(150) | NO |  |  |  |
| token2 | varchar(300) | NO |  |  |  |
| token3 | varchar(150) | NO |  |  |  |
| token4 | varchar(1200) | NO |  |  |  |
| urlarch | varchar(250) | NO |  |  |  |
| msgfele | char(1) | NO |  | N |  |
| flexnum | char(1) | NO |  | N |  |
| profac | char(1) | NO |  | 1 |  |
| procom | char(1) | NO |  | 1 |  |
| prorad | char(1) | NO |  | 1 |  |
| pronom | char(1) | NO |  | 1 |  |
| pruebas | char(1) | NO |  | N |  |
| tiemres | smallint(3) | NO |  | 60 |  |
| idsoft1 | varchar(150) | NO |  |  |  |

**Muestras (3 filas):**

```json
[]
```

---

## `recepmerca` (0 filas)

| Campo | Tipo | Nulo | Key | Default | Extra |
|-------|------|------|-----|---------|-------|
| numrec | varchar(20) | NO | MUL |  |  |
| codclas | varchar(4) | NO | MUL |  |  |
| nomdoc | varchar(100) | NO |  | RECEPCION DE MERCACIA |  |
| prerec | varchar(8) | NO |  |  |  |
| fecrec | datetime | NO |  | 2000-01-20 00:00:00 |  |
| nitter | varchar(15) | NO | MUL |  |  |
| obsrec | varchar(400) | NO |  |  |  |
| estrec | char(1) | NO |  |  |  |
| codemp | varchar(15) | NO | MUL |  |  |
| horrec | tinyint(3) | NO |  | 1 |  |
| codres | varchar(4) | NO | MUL |  |  |
| codbod | varchar(4) | NO |  |  |  |
| codcos | varchar(6) | NO |  |   |  |
| empcod | varchar(3) | NO |  |  |  |
| agrupa | char(1) | NO |  |  |  |
| veridoc | tinyint(1) | NO |  | 0 |  |
| feccrea | datetime | NO |  | 2000-01-20 00:00:00 |  |

**Muestras (3 filas):**

```json
[]
```

---

## `regiones` (33 filas)

| Campo | Tipo | Nulo | Key | Default | Extra |
|-------|------|------|-----|---------|-------|
| codreg | varchar(4) | NO | PRI |  |  |
| nomdep | varchar(100) | NO |  |  |  |
| codpais | varchar(3) | NO | MUL |  |  |

**Muestras (3 filas):**

```json
[
  {
    "codreg": "91",
    "nomdep": "AMAZONAS",
    "codpais": "CO"
  },
  {
    "codreg": "05",
    "nomdep": "ANTIOQUIA",
    "codpais": "CO"
  },
  {
    "codreg": "81",
    "nomdep": "ARAUCA",
    "codpais": "CO"
  }
]
```

---

## `regishabita` (0 filas)

| Campo | Tipo | Nulo | Key | Default | Extra |
|-------|------|------|-----|---------|-------|
| numreg | varchar(20) | NO | MUL |  |  |
| nomdoc | varchar(100) | NO |  | TARJETA DE REGISTRO |  |
| prereg | varchar(8) | NO |  |  |  |
| fecing | datetime | NO |  | 2000-01-20 00:00:00 |  |
| fecret | datetime | NO |  | 2000-01-20 00:00:00 |  |
| nitter | varchar(15) | NO | MUL |  |  |
| lugexp | varchar(50) | NO |  |  |  |
| tipnit | char(2) | NO |  |  |  |
| nacion | varchar(50) | NO |  |  |  |
| nomcli | varchar(120) | NO |  |  |  |
| dircli | varchar(100) | NO |  |  |  |
| telcli | varchar(50) | NO |  |  |  |
| fecnac | date | NO |  | 2000-01-20 |  |
| ciucli | varchar(50) | NO |  |  |  |
| oficli | varchar(50) | NO |  |  |  |
| tipveh | varchar(50) | NO |  |  |  |
| plaveh | varchar(30) | NO |  |  |  |
| marveh | varchar(50) | NO |  |  |  |
| motvia | varchar(50) | NO |  |  |  |
| ciupro | varchar(50) | NO |  |  |  |
| paipro | varchar(50) | NO |  |  |  |
| ciudes | varchar(100) | NO |  |  |  |
| paides | varchar(50) | NO |  |  |  |
| numper | tinyint(6) | NO |  | 1 |  |
| codmes | varchar(4) | NO | MUL |  |  |
| codser | varchar(12) | NO | MUL |  |  |
| valser | double | NO |  | 0 |  |
| tipcob | char(1) | NO |  | P |  |
| calpor | char(1) | NO |  | D |  |
| obsreg | varchar(400) | NO |  |  |  |
| estreg | char(1) | NO |  |  |  |
| codemp | varchar(15) | NO | MUL |  |  |
| horreg | tinyint(3) | NO |  | 1 |  |
| codres | varchar(4) | NO | MUL |  |  |
| codclas | varchar(4) | NO | MUL |  |  |
| estado | char(1) | NO |  | A |  |

**Muestras (3 filas):**

```json
[]
```

---

## `registro` (1 filas)

| Campo | Tipo | Nulo | Key | Default | Extra |
|-------|------|------|-----|---------|-------|
| nitemp | varchar(15) | NO |  |  |  |
| digver | char(2) | NO |  |  |  |
| nomcom | varchar(100) | NO |  |  |  |
| codreg | varchar(50) | NO |  | x |  |
| codent1 | varchar(50) | NO |  |  |  |
| codent2 | varchar(50) | NO |  |  |  |
| fecent | date | NO |  | 0000-00-00 |  |
| fecdia | date | NO |  | 0000-00-00 |  |
| horreg | tinyint(3) | NO |  | 1 |  |
| diater | smallint(5) | NO |  | 20 |  |
| verher | varchar(12) | NO |  |  |  |
| nitem2 | varchar(20) | NO |  |  |  |
| nomem2 | varchar(120) | NO |  |  |  |
| tipreg | char(1) | NO |  | 1 |  |

**Muestras (3 filas):**

```json
[
  {
    "nitemp": "1151970853",
    "digver": "6",
    "nomcom": "MAS VITAL MARKET",
    "codreg": "HXHBRDFH99GR7-880F8YPS91T",
    "codent1": "DWFO3N-A4T",
    "codent2": "DWFG3N-X4T",
    "fecent": "2026-05-09",
    "fecdia": "2026-04-09",
    "horreg": "9",
    "diater": "30",
    "verher": "10.0.0.3",
    "nitem2": "1151970853",
    "nomem2": "MAS VITAL MARKET",
    "tipreg": "1"
  }
]
```

---

## `resdian` (0 filas)

| Campo | Tipo | Nulo | Key | Default | Extra |
|-------|------|------|-----|---------|-------|
| codres | varchar(4) | NO | PRI |  |  |
| codcon | varchar(4) | NO | MUL |  |  |
| numres | varchar(20) | NO |  |  |  |
| fecres | date | NO |  | 2000-01-01 |  |
| numini | bigint(20) | NO |  | 1 |  |
| numfin | bigint(20) | NO |  | 100 |  |
| preres | varchar(8) | NO |  |  |  |
| actres | char(2) | NO |  | NO |  |
| texres | varchar(400) | NO |  |   |  |
| freshas | date | NO |  | 2000-01-01 |  |
| nmeses | smallint(5) | NO |  | 0 |  |
| aplvig | char(1) | NO |  | S |  |

**Muestras (3 filas):**

```json
[]
```

---

## `reservaciones` (0 filas)

| Campo | Tipo | Nulo | Key | Default | Extra |
|-------|------|------|-----|---------|-------|
| numres | varchar(20) | NO | MUL |  |  |
| nomdoc | varchar(100) | NO |  |   |  |
| preres | varchar(8) | NO |  |  |  |
| fecres | datetime | NO |  | 2000-01-20 00:00:00 |  |
| fecing | datetime | NO |  | 2000-01-20 00:00:00 |  |
| fecret | datetime | NO |  | 2000-01-20 00:00:00 |  |
| nitter | varchar(15) | NO | MUL |  |  |
| codmes | varchar(4) | NO | MUL |  |  |
| obsres | varchar(400) | NO |  |  |  |
| estres | char(1) | NO |  |  |  |
| codemp | varchar(15) | NO | MUL |  |  |
| horres | tinyint(3) | NO |  | 1 |  |
| codres | varchar(4) | NO | MUL |  |  |
| codclas | varchar(4) | NO | MUL |  |  |
| estado | char(1) | NO |  | A |  |
| tipo | char(1) | NO |  | R |  |

**Muestras (3 filas):**

```json
[]
```

---

## `resolpuc` (80 filas)

| Campo | Tipo | Nulo | Key | Default | Extra |
|-------|------|------|-----|---------|-------|
| codcon | varchar(20) | NO | MUL |  |  |
| tipo | varchar(15) | NO |  |  |  |
| codcue | varchar(20) | NO | MUL |  |  |
| clasres | varchar(15) | NO |  | CONTADORES |  |
| desadi | varchar(150) | NO |  |  |  |
| nitter | varchar(15) | NO |  |  |  |

**Muestras (3 filas):**

```json
[
  {
    "codcon": "L01",
    "tipo": "DEVOLCOMPRA",
    "codcue": "14350101",
    "clasres": "LINEA",
    "desadi": "",
    "nitter": ""
  },
  {
    "codcon": "L01",
    "tipo": "DEVOLUCIONES",
    "codcue": "41750101",
    "clasres": "LINEA",
    "desadi": "",
    "nitter": ""
  },
  {
    "codcon": "L01",
    "tipo": "VENTAS",
    "codcue": "41359501",
    "clasres": "LINEA",
    "desadi": "",
    "nitter": ""
  }
]
```

---

## `respdocfele` (0 filas)

| Campo | Tipo | Nulo | Key | Default | Extra |
|-------|------|------|-----|---------|-------|
| numnum | varchar(20) | NO | MUL |  |  |
| codclas | varchar(4) | NO | MUL |  |  |
| cocufe | varchar(150) | NO |  |  |  |
| cuuid | varchar(100) | NO |  |  |  |
| qrcode | varchar(800) | NO |  |  |  |
| respcod | int(6) | NO |  | 0 |  |
| estfele | char(1) | NO |  | 2 |  |
| estcli | char(1) | NO |  |  |  |
| fecgen | datetime | NO |  | 2000-01-20 00:00:00 |  |
| fecvlid | datetime | NO |  | 2000-01-20 00:00:00 |  |
| resptxt | varchar(800) | NO |  |  |  |
| protec | char(1) | NO |  | 0 |  |
| codpro | varchar(2) | NO |  | 0 |  |
| fecenv | datetime | NO |  | 2000-01-01 00:00:00 |  |
| respori | varchar(800) | NO |  |  |  |
| numenv | int(6) | NO |  | 1 |  |

**Muestras (3 filas):**

```json
[]
```

---

## `retenciones` (0 filas)

| Campo | Tipo | Nulo | Key | Default | Extra |
|-------|------|------|-----|---------|-------|
| numnum | varchar(20) | NO | MUL |  |  |
| codclas | varchar(4) | NO | MUL |  |  |
| tipret | varchar(12) | NO |  |  |  |
| basret | double | NO |  | 0 |  |
| porret | float | NO |  | 0 |  |
| valret | double | NO |  | 0 |  |
| codcue | varchar(20) | NO | MUL |  |  |
| detcue | varchar(150) | NO |  |  |  |
| numite | smallint(6) | NO |  | 1 |  |

**Muestras (3 filas):**

```json
[]
```

---

## `retftenomina` (66 filas)

| Campo | Tipo | Nulo | Key | Default | Extra |
|-------|------|------|-----|---------|-------|
| codtab | varchar(6) | NO | MUL | 0 |  |
| valdes | double | NO |  | 0 |  |
| valhas | double | NO |  | 0 |  |
| porimp | float | NO |  | 0 |  |
| valuvt1 | double | NO |  | 0 |  |

**Muestras (3 filas):**

```json
[
  {
    "codtab": "1",
    "valdes": "360.0",
    "valhas": "0.0",
    "porimp": "33.0",
    "valuvt1": "69.0"
  },
  {
    "codtab": "1",
    "valdes": "150.0",
    "valhas": "360.0",
    "porimp": "28.0",
    "valuvt1": "10.0"
  },
  {
    "codtab": "1",
    "valdes": "95.0",
    "valhas": "150.0",
    "porimp": "19.0",
    "valuvt1": "0.0"
  }
]
```

---

## `revelaciones` (0 filas)

| Campo | Tipo | Nulo | Key | Default | Extra |
|-------|------|------|-----|---------|-------|
| numnum | varchar(20) | NO | MUL |  |  |
| codclas | varchar(4) | NO | MUL |  |  |
| obsrev | varchar(2000) | NO |  |  |  |
| numrev | int(4) | NO |  | 0 |  |
| anorev | int(4) | NO |  | 0 |  |
| codigo | smallint(6) | NO | MUL | 0 |  |
| codper | varchar(2) | NO |  |  |  |
| tiprev | char(1) | NO |  |  |  |
| titurev | varchar(150) | NO |  |  |  |
| codcue | varchar(12) | NO |  |  |  |

**Muestras (3 filas):**

```json
[]
```

---

## `seguimcli` (0 filas)

| Campo | Tipo | Nulo | Key | Default | Extra |
|-------|------|------|-----|---------|-------|
| nitter | varchar(15) | NO | MUL |  |  |
| fecfec | date | NO | MUL | 2000-01-01 |  |
| numseg | smallint(6) | NO |  | 0 |  |
| numite | smallint(4) | NO |  | 0 |  |
| fecseg | datetime | NO |  | 2000-01-01 00:00:00 |  |
| tipseg | varchar(100) | NO |  |  |  |
| nomenc | varchar(100) | NO |  |  |  |
| nomusu | varchar(100) | NO |  |  |  |
| fecfin | varchar(25) | NO |  |  |  |
| obsseg | varchar(250) | NO |  |  |  |
| nuefec | datetime | NO |  | 2000-01-01 00:00:00 |  |
| tiptip | char(1) | NO |  | M |  |

**Muestras (3 filas):**

```json
[]
```

---

## `servicios` (0 filas)

| Campo | Tipo | Nulo | Key | Default | Extra |
|-------|------|------|-----|---------|-------|
| codser | varchar(12) | NO | PRI |  |  |
| detser | varchar(200) | NO |  |  |  |
| valser | double | NO |  | 0 |  |
| vconiva | double | NO |  | 0 |  |
| porimp | double | NO |  | 0 |  |
| codpor | varchar(4) | NO | MUL | 0 |  |
| codcue | varchar(12) | NO |  |  |  |
| serdct | char(2) | NO |  |  |  |
| grudet | varchar(1) | NO |  |  |  |
| moddet | char(1) | NO |  | N |  |
| codcos | varchar(6) | NO | MUL |  |  |
| autret | char(1) | NO |  | N |  |
| porret | float | NO |  | 0 |  |
| aplcomi | char(1) | NO |  | N |  |
| porcomi | float | NO |  | 0 |  |
| modipre | char(1) | NO |  | N |  |
| actser | char(1) | NO |  | A |  |

**Muestras (3 filas):**

```json
[]
```

---

## `solcreapro` (0 filas)

| Campo | Tipo | Nulo | Key | Default | Extra |
|-------|------|------|-----|---------|-------|
| numsol | varchar(15) | NO | MUL | 0 |  |
| fecapr | date | NO |  | 2000-01-20 |  |
| solapr | char(2) | NO |  | NO |  |
| obsapr | tinytext | NO |  |  |  |
| codemp | varchar(15) | NO | MUL |  |  |

**Muestras (3 filas):**

```json
[]
```

---

## `solcreditos` (0 filas)

| Campo | Tipo | Nulo | Key | Default | Extra |
|-------|------|------|-----|---------|-------|
| numsol | varchar(15) | NO | PRI | 0 |  |
| fecsol | date | NO |  | 2000-01-20 |  |
| nitter | varchar(15) | NO | MUL |  |  |
| valsol | double | NO |  | 0 |  |
| nitfia1 | varchar(15) | NO |  |  |  |
| nomfia1 | varchar(120) | NO |  |  |  |
| dirfia1 | varchar(100) | NO |  |  |  |
| telfia1 | varchar(50) | NO |  |  |  |
| obsfia1 | varchar(800) | NO |  |  |  |
| nitfia2 | varchar(15) | NO |  |  |  |
| nomfia2 | varchar(120) | NO |  |  |  |
| dirfia2 | varchar(100) | NO |  |  |  |
| telfia2 | varchar(50) | NO |  |  |  |
| obsfia2 | varchar(800) | NO |  |  |  |
| obssol | varchar(800) | NO |  |  |  |

**Muestras (3 filas):**

```json
[]
```

---

## `solservicios` (0 filas)

| Campo | Tipo | Nulo | Key | Default | Extra |
|-------|------|------|-----|---------|-------|
| numsol | varchar(20) | NO | MUL |  |  |
| codclas | varchar(4) | NO | MUL |  |  |
| nomdoc | varchar(100) | NO |  | SOLICITUD DE SERVICIO |  |
| presol | varchar(8) | NO |  | SS |  |
| fecsol | datetime | NO |  | 2000-01-20 00:00:00 |  |
| nitter | varchar(15) | NO | MUL |  |  |
| digver | char(2) | NO |  |  |  |
| clisol | varchar(120) | NO |  |  |  |
| dirsol | varchar(100) | NO |  |  |  |
| telsol | varchar(50) | NO |  |  |  |
| nitsol | varchar(15) | NO | MUL |  |  |
| diassol | int(11) | NO |  | 0 |  |
| obssol | varchar(400) | NO |  |  |  |
| estsol | char(1) | NO |  |  |  |
| codemp | varchar(15) | NO | MUL |  |  |
| horsol | tinyint(3) | NO |  | 1 |  |
| codres | varchar(4) | NO | MUL |  |  |
| codpla | varchar(30) | NO |  |  |  |
| artsol | varchar(50) | NO |  |  |  |
| marsol | varchar(50) | NO |  |  |  |
| modsol | varchar(50) | NO |  |  |  |
| marcrep | char(1) | NO |  |  |  |
| garfac | varchar(30) | NO |  |  |  |
| empcod | varchar(3) | NO |  |  |  |
| agrupa | char(1) | NO |  |  |  |
| veridoc | tinyint(1) | NO |  | 0 |  |
| feccrea | datetime | NO |  | 2000-01-20 00:00:00 |  |

**Muestras (3 filas):**

```json
[]
```

---

## `subinventa` (4 filas)

| Campo | Tipo | Nulo | Key | Default | Extra |
|-------|------|------|-----|---------|-------|
| codsub | varchar(3) | NO | MUL |  |  |
| nomsub | varchar(30) | NO |  |  |  |
| tiefec | char(1) | NO |  |  |  |

**Muestras (3 filas):**

```json
[
  {
    "codsub": "",
    "nomsub": "Serial",
    "tiefec": ""
  },
  {
    "codsub": "",
    "nomsub": "Lote",
    "tiefec": ""
  },
  {
    "codsub": "",
    "nomsub": "Vencimiento",
    "tiefec": ""
  }
]
```

---

## `subproduct` (0 filas)

| Campo | Tipo | Nulo | Key | Default | Extra |
|-------|------|------|-----|---------|-------|
| codprod | varchar(20) | NO | MUL |  |  |
| codsubp | varchar(20) | NO | MUL |  |  |
| cansub | double | NO |  | 0 |  |
| tipsub | char(1) | NO |  |  |  |
| codmed | varchar(3) | NO | MUL |  |  |
| divmul | char(1) | NO |  | M |  |
| facumed | double | NO |  | 1 |  |

**Muestras (3 filas):**

```json
[]
```

---

## `sucbloqcab` (0 filas)

| Campo | Tipo | Nulo | Key | Default | Extra |
|-------|------|------|-----|---------|-------|
| codbloq | varchar(4) | NO | PRI |  |  |
| nombloq | varchar(100) | NO |  |  |  |

**Muestras (3 filas):**

```json
[]
```

---

## `sucbloqdet` (0 filas)

| Campo | Tipo | Nulo | Key | Default | Extra |
|-------|------|------|-----|---------|-------|
| codbloq | varchar(4) | NO | MUL |  |  |
| codtip | char(1) | NO |  |  |  |
| tipbloq | char(1) | NO |  |  |  |
| codser | varchar(12) | NO | MUL |  |  |
| valser | double | NO |  | 0 |  |
| porser | float | NO |  | 0 |  |
| tippor | char(1) | NO |  | 1 |  |

**Muestras (3 filas):**

```json
[]
```

---

## `succategoria` (0 filas)

| Campo | Tipo | Nulo | Key | Default | Extra |
|-------|------|------|-----|---------|-------|
| codcat | varchar(2) | NO | PRI |  |  |
| nomcat | varchar(30) | NO |  |  |  |

**Muestras (3 filas):**

```json
[]
```

---

## `sucestratos` (0 filas)

| Campo | Tipo | Nulo | Key | Default | Extra |
|-------|------|------|-----|---------|-------|
| codest | varchar(2) | NO | PRI |  |  |
| nomest | varchar(30) | NO |  |  |  |

**Muestras (3 filas):**

```json
[]
```

---

## `sucretencion` (0 filas)

| Campo | Tipo | Nulo | Key | Default | Extra |
|-------|------|------|-----|---------|-------|
| codsuc | varchar(20) | NO | MUL |  |  |
| tipret | varchar(12) | NO |  |  |  |
| basret | double | NO |  | 0 |  |
| porret | float | NO |  | 0 |  |
| valret | double | NO |  | 0 |  |
| cauret | char(1) | NO |  |  |  |

**Muestras (3 filas):**

```json
[]
```

---

## `sucursales` (0 filas)

| Campo | Tipo | Nulo | Key | Default | Extra |
|-------|------|------|-----|---------|-------|
| codsuc | varchar(15) | NO | PRI |  |  |
| nitter | varchar(15) | NO | MUL |  |  |
| nomsuc | varchar(120) | NO |  |  |  |
| dirsuc | varchar(100) | NO |  |  |  |
| telsuc | varchar(30) | NO |  |  |  |
| movsuc | varchar(30) | NO |  |  |  |
| nomrut | varchar(30) | NO |  |  |  |
| obssuc | varchar(400) | NO |  |  |  |
| nomzon | varchar(100) | NO |  |  |  |
| inasuc | char(2) | NO |  | NO |  |
| codciu | varchar(6) | NO |  |  |  |
| suscod | varchar(30) | NO |  |  |  |
| impcod | varchar(10) | NO |  |  |  |
| codest | varchar(2) | NO | MUL |  |  |
| codcat | varchar(2) | NO | MUL |  |  |
| tieacue | char(1) | NO |  | 0 |  |
| tiealca | char(1) | NO |  | 0 |  |
| tieaseo | char(1) | NO |  | 0 |  |
| metrfij | smallint(6) | NO |  | 0 |  |
| tiposuc | char(1) | NO |  |  |  |
| corele | varchar(100) | NO |  |  |  |
| tiparre | char(1) | NO |  | 0 |  |
| metralc | smallint(6) | NO |  | 0 |  |
| metrase | double | NO |  | 0 |  |
| numpred | varchar(20) | NO |  |  |  |
| codbloq | varchar(4) | NO | MUL |  |  |
| codinm1 | varchar(4) | NO | MUL |  |  |
| nitpro | varchar(15) | NO | MUL |  |  |
| fecini | date | NO |  | 2000-01-01 |  |
| fecfin | date | NO |  | 2000-01-01 |  |
| meses | int(11) | NO |  | 0 |  |

**Muestras (3 filas):**

```json
[]
```

---

## `sucvalbloque` (0 filas)

| Campo | Tipo | Nulo | Key | Default | Extra |
|-------|------|------|-----|---------|-------|
| tipo | char(1) | NO |  |  |  |
| codest | varchar(2) | NO | MUL |  |  |
| codcat | varchar(2) | NO | MUL |  |  |
| valser1 | double | NO |  | 0 |  |
| vrmetro | double | NO |  | 0 |  |
| codser1 | varchar(12) | NO | MUL |  |  |
| codser2 | varchar(12) | NO | MUL |  |  |
| porser2 | float | NO |  | 0 |  |
| valser2 | double | NO |  | 0 |  |
| topesr2 | smallint(6) | NO |  | 0 |  |
| codser3 | varchar(12) | NO | MUL |  |  |
| codbloq | varchar(4) | NO | MUL |  |  |

**Muestras (3 filas):**

```json
[]
```

---

## `sucvehimasc` (0 filas)

| Campo | Tipo | Nulo | Key | Default | Extra |
|-------|------|------|-----|---------|-------|
| codsuc | varchar(15) | NO | MUL |  |  |
| numite | smallint(6) | NO |  | 1 |  |
| planom | varchar(30) | NO |  |  |  |
| marraz | varchar(50) | NO |  |  |  |
| coltam | varchar(30) | NO |  |  |  |
| modveh | varchar(30) | NO |  |  |  |
| tipvhm | char(1) | NO |  | 1 |  |
| tipmas | char(1) | NO |  | 0 |  |

**Muestras (3 filas):**

```json
[]
```

---

## `tarjetas` (4 filas)

| Campo | Tipo | Nulo | Key | Default | Extra |
|-------|------|------|-----|---------|-------|
| codtar | varchar(4) | NO | PRI |  |  |
| nomtar | varchar(100) | NO |  |  |  |

**Muestras (3 filas):**

```json
[
  {
    "codtar": "T01",
    "nomtar": "AMERICAN EXPRESS"
  },
  {
    "codtar": "T02",
    "nomtar": "MASTERD CARD"
  },
  {
    "codtar": "T03",
    "nomtar": "VISA"
  }
]
```

---

## `temdetalles` (0 filas)

| Campo | Tipo | Nulo | Key | Default | Extra |
|-------|------|------|-----|---------|-------|
| numtem | varchar(20) | NO | MUL |  |  |
| codclas | varchar(4) | NO | MUL |  |  |
| nitter | varchar(15) | NO | MUL |  |  |
| numite | smallint(6) | NO |  | 1 |  |
| codprod | varchar(20) | NO | MUL |  |  |
| iterel | smallint(6) | NO |  | 0 |  |
| sernum | varchar(40) | NO |  |  |  |
| nomdet | varchar(300) | NO |  |  |  |
| valuni | double | NO |  | 0 |  |
| candet | double | NO |  | 0 |  |
| exiant | double | NO |  | 0 |  |
| dctpor | float | NO |  | 0 |  |
| dctpes | double | NO |  | 0 |  |
| ivapor | float | NO |  | 0 |  |
| ivapes | double | NO |  | 0 |  |
| totdet | double | NO |  | 0 |  |
| obsdet | varchar(400) | NO |  |  |  |
| cosprod | double | NO |  | 0 |  |
| tipdet | char(2) | NO |  | P |  |
| codpor | varchar(4) | NO | MUL | 0 |  |
| codbod | varchar(4) | NO | MUL |  |  |
| ipopor | float | NO |  | 0 |  |
| ipopes | double | NO |  | 0 |  |
| tipipo | varchar(2) | NO |  |  |  |
| codpor2 | varchar(4) | NO |  | 0 |  |
| nitfor | varchar(12) | NO |  |  |  |
| serfec | varchar(10) | NO |  |  |  |
| multiplo | double | NO |  | 1 |  |
| cruclas | varchar(4) | NO |  |   |  |
| crunum | varchar(20) | NO |  |   |  |
| nomtec | varchar(12) | NO |  |  |  |
| factpor | float | NO |  | 0 |  |
| prbase | double | NO |  | 0 |  |
| codcos | varchar(6) | NO |  |  |  |
| codmed | varchar(3) | NO | MUL |  |  |
| divmul | char(1) | NO |  | M |  |
| facumed | double | NO |  | 1 |  |

**Muestras (3 filas):**

```json
[]
```

---

## `tercecorreo` (0 filas)

| Campo | Tipo | Nulo | Key | Default | Extra |
|-------|------|------|-----|---------|-------|
| nitter | varchar(15) | NO | MUL |  |  |
| corele | varchar(100) | NO |  |  |  |

**Muestras (3 filas):**

```json
[]
```

---

## `terceepsasi` (0 filas)

| Campo | Tipo | Nulo | Key | Default | Extra |
|-------|------|------|-----|---------|-------|
| nitter | varchar(15) | NO | MUL |  |  |
| codtip | varchar(3) | NO | MUL |  |  |
| niteps | varchar(15) | NO | MUL |  |  |

**Muestras (3 filas):**

```json
[]
```

---

## `terceros` (73 filas)

| Campo | Tipo | Nulo | Key | Default | Extra |
|-------|------|------|-----|---------|-------|
| nitter | varchar(15) | NO | PRI |  |  |
| tipnit | varchar(2) | NO |  |  |  |
| digter | char(2) | NO |  |  |  |
| perjur | varchar(1) | NO |  |  |  |
| razsoc | varchar(100) | NO |  |  |  |
| apeter | varchar(30) | NO |  |  |  |
| apeter2 | varchar(30) | NO |  |  |  |
| nomter | varchar(30) | NO |  |  |  |
| nomter2 | varchar(30) | NO |  |  |  |
| nomcom | varchar(120) | NO |  |  |  |
| dirter | varchar(100) | NO |  |  |  |
| telter | varchar(50) | NO |  |  |  |
| faxter | varchar(15) | NO |  |  |  |
| movter | varchar(15) | NO |  |  |  |
| codciu | varchar(6) | NO | MUL |  |  |
| corele | varchar(100) | NO |  |  |  |
| corel2 | varchar(100) | NO |  |  |  |
| cupcar | double | NO |  | 0 |  |
| calter | char(1) | NO |  |  |  |
| cupblo | char(1) | NO |  | R |  |
| codban | varchar(8) | NO | MUL |  |  |
| cuenum | varchar(20) | NO |  |  |  |
| nomban | varchar(100) | NO |  |  |  |
| regven | varchar(1) | NO |  |  |  |
| fecnac | date | NO |  | 2000-01-01 |  |
| arcimg | varchar(255) | NO |  |  |  |
| tipimg | tinyint(3) | NO |  | 1 |  |
| obster | varchar(800) | NO |  |  |  |
| emppro | char(2) | NO |  |  |  |
| codlis | char(3) | NO | MUL |  |  |
| cliter | char(2) | NO |  | NO |  |
| proter | char(2) | NO |  | NO |  |
| empter | char(2) | NO |  | NO |  |
| venter | char(2) | NO |  | NO |  |
| inater | char(2) | NO |  | NO |  |
| tipemp | varchar(1) | NO |  |  |  |
| cedrep | varchar(15) | NO |  |  |  |
| repleg | varchar(100) | NO |  |  |  |
| cedcon | varchar(15) | NO |  |  |  |
| connom | varchar(100) | NO |  |  |  |
| gracon | char(2) | NO |  | NO |  |
| ageret | char(2) | NO |  | NO |  |
| ageaut | char(2) | NO |  | NO |  |
| regsimp | char(2) | NO |  | NO |  |
| tiecli | char(2) | NO |  | NO |  |
| tiepro | char(2) | NO |  | NO |  |
| suebas | double | NO |  | 0 |  |
| codcar | varchar(5) | NO |  |  |  |
| codadm | char(3) | NO |  |  |  |
| feccrea | date | NO |  | 2010-01-01 |  |
| tarpro | varchar(40) | NO |  |  |  |
| acteco | varchar(6) | NO |  |  |  |
| diaven | smallint(4) | NO |  | 0 |  |
| tipocli | char(1) | NO |  | 0 |  |
| feccup | date | NO |  | 2000-01-01 |  |
| agedet | varchar(100) | NO |  |  |  |
| vencod | varchar(4) | NO |  |  |  |
| codzon | varchar(4) | NO |  |  |  |
| codpost | varchar(12) | NO |  |  |  |
| nitvend | varchar(15) | NO |  |  |  |
| fijvend | char(1) | NO |  | 0 |  |
| impnatu | char(1) | NO |  | 0 |  |
| codpais | varchar(3) | NO |  | CO |  |
| resinc | char(1) | NO |  | N |  |
| otrter | char(2) | NO |  | NO |  |

**Muestras (3 filas):**

```json
[
  {
    "nitter": "1151970853",
    "tipnit": "13",
    "digter": "6",
    "perjur": "N",
    "razsoc": "MAS VITAL MARKET",
    "apeter": "PORTILLA",
    "apeter2": "ROSERO",
    "nomter": "JAVIER",
    "nomter2": "ANDRES",
    "nomcom": "MAS VITAL MARKET",
    "dirter": "CALLE 18 N 25-94",
    "telter": "3116978695",
    "faxter": " ",
    "movter": " ",
    "codciu": "52001",
    "corele": "masvitalmarket@gmail.com",
    "corel2": "",
    "cupcar": "0.0",
    "calter": "",
    "cupblo": "R",
    "codban": "",
    "cuenum": "",
    "nomban": "",
    "regven": "2",
    "fecnac": "2000-01-01",
    "arcimg": " ",
    "tipimg": "2",
    "obster": "",
    "emppro": "SI",
    "codlis": "",
    "cliter": "NO",
    "proter": "NO",
    "empter": "NO",
    "venter": "NO",
    "inater": "NO",
    "tipemp": "2",
    "cedrep": " 1151970853",
    "repleg": "JAVIER ANDRES PORTILLA ROSERO",
    "cedcon": "12963457",
    "connom": "FRANCISCO PORTILLA",
    "gracon": "NO",
    "ageret": "NO",
    "ageaut": "NO",
    "regsimp": "NO",
    "tiecli": "NO",
    "tiepro": "NO",
    "suebas": "0.0",
    "codcar": "",
    "codadm": "",
    "feccrea": "2010-01-01",
    "tarpro": "",
    "acteco": "4729",
    "diaven": "0",
    "tipocli": "0",
    "feccup": "2000-01-01",
    "agedet": "",
    "vencod": "",
    "codzon": "",
    "codpost": "",
    "nitvend": "",
    "fijvend": "0",
    "impnatu": "0",
    "codpais": "CO",
    "resinc": "N",
    "otrter": "NO"
  },
  {
    "nitter": "12963457",
    "tipnit": "13",
    "digter": "2",
    "perjur": "N",
    "razsoc": "",
    "apeter": "PORTILLA",
    "apeter2": "ERAZO",
    "nomter": "FRANCISCO ",
    "nomter2": "JAVIER",
    "nomcom": "FRANCISCO  JAVIER PORTILLA ERAZO",
    "dirter": "CRA 41  15B-64 BARRIO SAN JUAN DE DIOS",
    "telter": "3105830555",
    "faxter": "",
    "movter": "",
    "codciu": "52001",
    "corele": "franjapo1@hotmail.com",
    "corel2": "",
    "cupcar": "500000.0",
    "calter": "A",
    "cupblo": "V",
    "codban": "",
    "cuenum": "",
    "nomban": "",
    "regven": "2",
    "fecnac": "2000-01-01",
    "arcimg": "",
    "tipimg": "1",
    "obster": "",
    "emppro": "NO",
    "codlis": "L2",
    "cliter": "SI",
    "proter": "SI",
    "empter": "SI",
    "venter": "SI",
    "inater": "NO",
    "tipemp": "",
    "cedrep": "",
    "repleg": "",
    "cedcon": "",
    "connom": "",
    "gracon": "NO",
    "ageret": "NO",
    "ageaut": "SI",
    "regsimp": "NO",
    "tiecli": "NO",
    "tiepro": "NO",
    "suebas": "0.0",
    "codcar": "",
    "codadm": "C1",
    "feccrea": "2026-05-20",
    "tarpro": "173477-T",
    "acteco": "",
    "diaven": "0",
    "tipocli": "0",
    "feccup": "2026-05-20",
    "agedet": "",
    "vencod": "1",
    "codzon": "1",
    "codpost": "520001",
    "nitvend": "",
    "fijvend": "0",
    "impnatu": "0",
    "codpais": "CO",
    "resinc": "N",
    "otrter": "SI"
  },
  {
    "nitter": "29121236",
    "tipnit": "13",
    "digter": "",
    "perjur": "N",
    "razsoc": "",
    "apeter": "SUAREZ",
    "apeter2": "MONTOYA",
    "nomter": "FRANCIA",
    "nomter2": "NURY",
    "nomcom": "FRANCIA NURY SUAREZ MONTOYA",
    "dirter": "CALLE 8 No 20A-81 B/ VILLA LUCIA",
    "telter": "3104100513",
    "faxter": "",
    "movter": "",
    "codciu": "52001",
    "corele": "",
    "corel2": "",
    "cupcar": "500000.0",
    "calter": "A",
    "cupblo": "R",
    "codban": "",
    "cuenum": "",
    "nomban": "",
    "regven": "",
    "fecnac": "2000-01-01",
    "arcimg": "",
    "tipimg": "1",
    "obster": "",
    "emppro": "NO",
    "codlis": "",
    "cliter": "SI",
    "proter": "SI",
    "empter": "SI",
    "venter": "SI",
    "inater": "NO",
    "tipemp": "",
    "cedrep": "",
    "repleg": "",
    "cedcon": "",
    "connom": "",
    "gracon": "NO",
    "ageret": "NO",
    "ageaut": "NO",
    "regsimp": "NO",
    "tiecli": "NO",
    "tiepro": "NO",
    "suebas": "0.0",
    "codcar": "",
    "codadm": "",
    "feccrea": "2026-05-20",
    "tarpro": "",
    "acteco": "",
    "diaven": "0",
    "tipocli": "0",
    "feccup": "2026-05-20",
    "agedet": "",
    "vencod": "",
    "codzon": "2",
    "codpost": "520001",
    "nitvend": "12963457",
    "fijvend": "0",
    "impnatu": "0",
    "codpais": "CO",
    "resinc": "N",
    "otrter": "NO"
  }
]
```

---

## `traslados` (0 filas)

| Campo | Tipo | Nulo | Key | Default | Extra |
|-------|------|------|-----|---------|-------|
| numtra | varchar(20) | NO | MUL | 00 |  |
| nomdoc | varchar(100) | NO |  | SALIDAS |  |
| pretra | varchar(8) | NO |  | RC |  |
| fectra | datetime | NO |  | 2000-01-20 00:00:00 |  |
| obstra | varchar(400) | NO |  |  |  |
| esttra | char(1) | NO |  |  |  |
| codemp | varchar(15) | NO | MUL |  |  |
| hortra | tinyint(3) | NO |  | 1 |  |
| codres | varchar(4) | NO | MUL |  |  |
| codbod | varchar(4) | NO | MUL |  |  |
| boddes | varchar(4) | NO | MUL |  |  |
| codclas | varchar(4) | NO | MUL |  |  |
| cosori | varchar(6) | NO |  |   |  |
| cosdes | varchar(6) | NO |  |   |  |
| nitter | varchar(15) | NO | MUL |  |  |
| verifi | char(1) | NO |  |  |  |
| veridoc | tinyint(1) | NO |  | 0 |  |
| feccrea | datetime | NO |  | 2000-01-20 00:00:00 |  |

**Muestras (3 filas):**

```json
[]
```

---

## `ubiprodbod` (0 filas)

| Campo | Tipo | Nulo | Key | Default | Extra |
|-------|------|------|-----|---------|-------|
| codbod | varchar(4) | NO | MUL |  |  |
| codprod | varchar(20) | NO | MUL |  |  |
| desubi | varchar(150) | NO |  |  |  |
| stockmin | double | NO |  | 0 |  |
| stockmax | double | NO |  | 0 |  |

**Muestras (3 filas):**

```json
[]
```

---

## `undmedidas` (8 filas)

| Campo | Tipo | Nulo | Key | Default | Extra |
|-------|------|------|-----|---------|-------|
| codmed | varchar(3) | NO | MUL |  |  |
| nommed | varchar(50) | NO |  |  |  |
| medpres | varchar(15) | NO |  |  |  |
| codele | varchar(3) | NO |  |  |  |

**Muestras (3 filas):**

```json
[
  {
    "codmed": "001",
    "nommed": "UNIDAD",
    "medpres": "UND",
    "codele": "94"
  },
  {
    "codmed": "002",
    "nommed": "CAJA",
    "medpres": "CAJA",
    "codele": "BX"
  },
  {
    "codmed": "003",
    "nommed": "GRAMO",
    "medpres": "GRAMO",
    "codele": "GRM"
  }
]
```

---

## `usuapermiso` (0 filas)

| Campo | Tipo | Nulo | Key | Default | Extra |
|-------|------|------|-----|---------|-------|
| nitter | varchar(15) | NO | MUL |  |  |
| pesino | char(2) | NO |  | NO |  |
| codclas | varchar(6) | NO |  | NO |  |

**Muestras (3 filas):**

```json
[]
```

---

## `usuarios` (4 filas)

| Campo | Tipo | Nulo | Key | Default | Extra |
|-------|------|------|-----|---------|-------|
| nomusu | varchar(25) | NO | MUL |  |  |
| clausu | varchar(30) | NO |  |  |  |
| nitter | varchar(15) | NO | MUL |  |  |
| nivusu | tinyint(3) | NO |  | 1 |  |
| estusu | char(2) | NO |  | NO |  |
| codcos | varchar(6) | NO | MUL |  |  |
| cosfij | char(1) | NO |  | S |  |
| codbod | varchar(4) | NO | MUL |  |  |
| bodfij | char(1) | NO |  | S |  |
| bodtra | char(1) | NO |  |  |  |
| agefij | char(1) | NO |  |  |  |
| empcod | varchar(3) | NO |  |  |  |
| claweb | varchar(250) | NO |  |  |  |

**Muestras (3 filas):**

```json
[
  {
    "nomusu": "ADMIN",
    "clausu": "xtd4",
    "nitter": "1151970853",
    "nivusu": "1",
    "estusu": "NO",
    "codcos": "",
    "cosfij": "S",
    "codbod": "",
    "bodfij": "S",
    "bodtra": "",
    "agefij": "",
    "empcod": "",
    "claweb": ""
  },
  {
    "nomusu": "VALERIA",
    "clausu": "dfcd",
    "nitter": "1085343471",
    "nivusu": "2",
    "estusu": "NO",
    "codcos": "",
    "cosfij": "S",
    "codbod": "",
    "bodfij": "S",
    "bodtra": "O",
    "agefij": "N",
    "empcod": "",
    "claweb": ""
  },
  {
    "nomusu": "FRANCIA",
    "clausu": "qqc4",
    "nitter": "29121236",
    "nivusu": "2",
    "estusu": "NO",
    "codcos": "",
    "cosfij": "S",
    "codbod": "",
    "bodfij": "S",
    "bodtra": "O",
    "agefij": "N",
    "empcod": "",
    "claweb": ""
  }
]
```

---

## `usuauditoria` (817 filas)

| Campo | Tipo | Nulo | Key | Default | Extra |
|-------|------|------|-----|---------|-------|
| id_auditoria | int(11) | NO | PRI |  | auto_increment |
| tokenses | varchar(100) | SI |  |  |  |
| nomusu | varchar(25) | NO | MUL |  |  |
| codemp | varchar(15) | NO | MUL |  |  |
| nomemp | varchar(120) | NO |  |  |  |
| equipo | varchar(100) | NO |  |  |  |
| accion | varchar(50) | NO |  |  |  |
| fecha | datetime | NO |  |  |  |
| modulo | varchar(100) | NO |  |  |  |
| codcod | varchar(20) | NO | MUL |  |  |
| numdoc | varchar(20) | NO | MUL |  |  |
| codclas | varchar(4) | NO | MUL |  |  |
| nitter | varchar(15) | NO | MUL |  |  |
| detalle | text | SI |  |  |  |

**Muestras (3 filas):**

```json
[
  {
    "id_auditoria": "1",
    "tokenses": "11070fcd-6816-4c72-93e4-5b941eb3488c",
    "nomusu": "ADMIN",
    "codemp": "1151970853",
    "nomemp": "MAS VITAL MARKET",
    "equipo": "DESKTOP-LDJR4PC",
    "accion": "MODIFICAR",
    "fecha": "2026-05-25 12:06:31",
    "modulo": "CATALOGO DE TERCEROS",
    "codcod": "",
    "numdoc": "",
    "codclas": "",
    "nitter": "12963457",
    "detalle": "Tercero: 12963457 FRANCISCO  JAVIER PORTILLA ERAZO"
  },
  {
    "id_auditoria": "2",
    "tokenses": "57c6eb7a-5197-4daf-8e94-d9a066fd1c72",
    "nomusu": "ADMIN",
    "codemp": "1151970853",
    "nomemp": "MAS VITAL MARKET",
    "equipo": "CU19881",
    "accion": "INSERTAR",
    "fecha": "2026-06-03 19:10:46",
    "modulo": "CATALOGO DE PRODUCTOS",
    "codcod": "7709841861223",
    "numdoc": "",
    "codclas": "",
    "nitter": "",
    "detalle": "producto: 7709841861223 Galletas de Almendras Naranja"
  },
  {
    "id_auditoria": "3",
    "tokenses": "57c6eb7a-5197-4daf-8e94-d9a066fd1c72",
    "nomusu": "ADMIN",
    "codemp": "1151970853",
    "nomemp": "MAS VITAL MARKET",
    "equipo": "CU19881",
    "accion": "INSERTAR",
    "fecha": "2026-06-03 19:10:46",
    "modulo": "CATALOGO DE PRODUCTOS",
    "codcod": "7709841861216",
    "numdoc": "",
    "codclas": "",
    "nitter": "",
    "detalle": "producto: 7709841861216 Galletas de Almendras Cinnamon"
  }
]
```

---

## `usubtfavorito` (0 filas)

| Campo | Tipo | Nulo | Key | Default | Extra |
|-------|------|------|-----|---------|-------|
| codfav | int(11) | NO | PRI |  | auto_increment |
| nomusu | varchar(25) | NO | MUL |  |  |
| nommenu | varchar(100) | NO |  |  |  |
| nitter | varchar(15) | NO | MUL |  |  |

**Muestras (3 filas):**

```json
[]
```

---

## `usuingre` (59 filas)

| Campo | Tipo | Nulo | Key | Default | Extra |
|-------|------|------|-----|---------|-------|
| id_ingreso | int(11) | NO | PRI |  | auto_increment |
| tokenses | varchar(100) | SI |  |  |  |
| nomusu | varchar(25) | NO | MUL |  |  |
| nitter | varchar(15) | NO | MUL |  |  |
| nomter | varchar(120) | NO |  |  |  |
| verherm | varchar(20) | NO |  |  |  |
| equipo | varchar(100) | NO |  |  |  |
| fecing | datetime | NO |  |  |  |
| fecactiv | datetime | NO |  |  |  |
| fecsal | datetime | SI |  |  |  |
| estado | tinyint(3) unsigned | NO |  | 0 |  |

**Muestras (3 filas):**

```json
[
  {
    "id_ingreso": "1",
    "tokenses": "b64a8de2-3e5f-4a0a-892b-eeb8427c7734",
    "nomusu": "ADMIN",
    "nitter": "1151970853",
    "nomter": "MAS VITAL MARKET",
    "verherm": "10.0.0.2",
    "equipo": "FRANCISCO",
    "fecing": "2026-05-25 10:46:53",
    "fecactiv": "2026-05-25 10:48:53",
    "fecsal": "2026-05-25 10:49:42",
    "estado": "1"
  },
  {
    "id_ingreso": "2",
    "tokenses": "11070fcd-6816-4c72-93e4-5b941eb3488c",
    "nomusu": "ADMIN",
    "nitter": "1151970853",
    "nomter": "MAS VITAL MARKET",
    "verherm": "10.0.0.2",
    "equipo": "DESKTOP-LDJR4PC",
    "fecing": "2026-05-25 11:00:51",
    "fecactiv": "2026-05-25 16:21:10",
    "fecsal": "2026-05-25 16:21:21",
    "estado": "1"
  },
  {
    "id_ingreso": "3",
    "tokenses": "25e08dec-7376-4e2d-bd93-f507d798f029",
    "nomusu": "ADMIN",
    "nitter": "1151970853",
    "nomter": "MAS VITAL MARKET",
    "verherm": "10.0.0.2",
    "equipo": "DESKTOP-LDJR4PC",
    "fecing": "2026-05-29 09:32:21",
    "fecactiv": "2026-05-29 10:59:22",
    "fecsal": "2026-05-29 10:59:40",
    "estado": "1"
  }
]
```

---

## `variosdet` (17 filas)

| Campo | Tipo | Nulo | Key | Default | Extra |
|-------|------|------|-----|---------|-------|
| codvar | varchar(6) | NO | MUL |  |  |
| desvar | varchar(100) | NO |  |  |  |
| adivar | varchar(50) | NO |  |  |  |
| tipvar | char(3) | NO |  |  |  |
| codcue | varchar(20) | NO |  |  |  |
| valor1 | double | NO |  | 0 |  |
| empcod | varchar(3) | NO | MUL |  |  |
| codprod | varchar(20) | NO | MUL |  |  |
| tipmes | varchar(1) | NO |  | 1 |  |

**Muestras (3 filas):**

```json
[
  {
    "codvar": "F01",
    "desvar": "SALIDA POR PERDIDA",
    "adivar": "",
    "tipvar": "NSA",
    "codcue": " ",
    "valor1": "0.0",
    "empcod": "",
    "codprod": "",
    "tipmes": "1"
  },
  {
    "codvar": "F02",
    "desvar": "SALIDA POR DETERIORO",
    "adivar": "",
    "tipvar": "NSA",
    "codcue": " ",
    "valor1": "0.0",
    "empcod": "",
    "codprod": "",
    "tipmes": "1"
  },
  {
    "codvar": "F03",
    "desvar": "SALIDA A PRODUCCION",
    "adivar": "",
    "tipvar": "NSA",
    "codcue": "14100101",
    "valor1": "0.0",
    "empcod": "",
    "codprod": "",
    "tipmes": "1"
  }
]
```

---

## `zonas` (3 filas)

| Campo | Tipo | Nulo | Key | Default | Extra |
|-------|------|------|-----|---------|-------|
| codzon | varchar(4) | NO | PRI |  |  |
| nomzon | varchar(100) | NO |  |  |  |
| codciu | varchar(5) | NO | MUL |  |  |

**Muestras (3 filas):**

```json
[
  {
    "codzon": "1",
    "nomzon": "NORTE",
    "codciu": ""
  },
  {
    "codzon": "2",
    "nomzon": "CENTRO",
    "codciu": ""
  },
  {
    "codzon": "3",
    "nomzon": "SUR",
    "codciu": ""
  }
]
```

---


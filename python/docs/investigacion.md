# Investigación DataCook

## ZIP principal

- Contiene una carpeta con la fecha.
- Dentro existen 17 ZIP correspondientes a comercios.
- Los ZIP internos pueden abrirse directamente desde memoria (sin extraerlos).

## ZIP de comercio

Cada ZIP contiene exactamente tres archivos CSV:

- comercio.csv
- sucursales.csv
- productos.csv

### Observaciones

- Es posible abrir los ZIP internos completamente en memoria.
- No es necesario descomprimir archivos en el disco para procesarlos.

## productos.csv

- Separador: `|`
- Codificación: UTF-8 con BOM (`utf-8-sig`)
- Cantidad de columnas: 17
- Cantidad de registros (primer ZIP analizado): 955.145

### Observaciones

- El archivo contiene información de productos y precios.
- Incluye referencias a comercio, bandera y sucursal.
- Existen campos de promociones que pueden estar vacíos.
- Codigo para la Provincia de Buenos Aires: AR-B

## Hallazgos

### ZIP interno corrupto

En las bases analizadas (`sepa_viernes` y `sepa_miercoles`) se detectó que el archivo:

`sepa_2_comercio-sepa-36_*.zip`

está vacío (0 bytes) y no puede abrirse como un archivo ZIP.

La aplicación deberá ignorar estos archivos, registrar el incidente y continuar con el procesamiento del resto de la información.

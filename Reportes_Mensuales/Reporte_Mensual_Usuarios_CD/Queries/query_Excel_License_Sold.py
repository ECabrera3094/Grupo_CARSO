from google.cloud import bigquery

def query_Excel_License_Sold(date):
    # Crea un cliente de BigQuery
    #client = bigquery.Client(project="amco-cv-prod") # Solo aplica a Proyectos en la Nube.

    # Crea un cliente de BigQuery
    client = bigquery.Client()

    # Ejecuta la consulta
    query_job = client.query(
    f"""
    --- EXCEL LICENCIAS ASIGNADAS
    --- licencias_vencidas_asignadas_suscripciones = SUSCRIPCIONES
    --- licencias_vencidas_asignadas_licencias = LICENCIAS VENDIDAS
    --- licencias_vencidas_asignadas_buzones = LICENCIAS OCUPADAS
select sum(licencias_vencidas_asignadas_suscripciones), SUM(licencias_vencidas_asignadas_licencias), SUM(licencias_vencidas_asignadas_buzones)
from(
WITH licencias_vencidas_asignadas AS (with  filtro_m as (
        Select distinct last_day(date(id_fecha), month) as fecha,
                cast (cast(last_day(date(id_fecha), month) as date)as string) fecha_String,
                CAST(CONCAT(CAST(extract(year from last_day(date(id_fecha), month)) AS STRING),
                LPAD(CAST(extract(month from date_trunc(date(id_fecha), month)) AS STRING),2,'00'),
                LPAD(CAST(extract(day from date_trunc(date(id_fecha), month)) AS STRING),2,'00')) AS INTEGER)*-1 ORDEN_FECHA,
                concat(extract(year from date_trunc(date(id_fecha), month)),' ',FORMAT_DATETIME("%h", DATETIME(date_trunc(date(id_fecha), month))) )as Fecha_Nombre
        from amco-cd-qa.GRAL_N.LOGIN_ACTIVIDAD_CDN order by 3 asc
),
login as(
SELECT    case when pais is null then 'SIN VENDOR' else pais end completo,
case when pais is null then 'SIN VENDOR'
WHEN pais like 'MEXICO%' THEN 'MEXICO' else pais  end as pais ,
count(activo) as activo, count(Login) as sum_login, ID_FECHA as fecha_login
FROM `amco-cd-qa.GRAL_N.LOGIN_ACTIVIDAD_CDN`
--where ID_FECHA= '2022-05-31'-- and pais ='SIN VENDOR'
group by 1,pais,ID_FECHA
),
licencias as (
SELECT  case when vendor is null then 'SIN VENDOR' when vendor like 'MEXICO%' THEN vendor else replace(vendor,' ','') end completo,
--sum(SUSCRIPCIONES) as suscripciones ,sum(l.LICENCIAS) as lic_vendidas, sum(BUZONES) as buzones ,
ID_FECHA as fecha_lic,
ACCOUNTID,VENDOR,SUSCRIPCIONES,LICENCIAS, BUZONES
FROM  amco-cd-qa.GRAL_N.LICENCIAS_VENDIDAS_ASIGNADAS_CDN  l
--where ID_FECHA= '2022-05-31'-- and vendor is null
group by ID_FECHA,l.ACCOUNTID,l.VENDOR,l.SUSCRIPCIONES,l.LICENCIAS, l.BUZONES
)
select lic.ACCOUNTID,
case when vendor is null then 'SIN VENDOR'
WHEN vendor like 'MEXICO%' THEN 'MEXICO' else replace(vendor,' ','')  end as vendor, lic.SUSCRIPCIONES, lic.LICENCIAS, lic.BUZONES,
SPLIT(lo.pais, ' ')[OFFSET(0)] as pais_filtro
--lo.completo, lo.pais, lo.activo, lo.sum_login, lic.suscripciones, lic.lic_vendidas, lic.buzones
from login as lo
left join licencias lic on lo.completo=lic.completo   and lo.fecha_login=lic.fecha_lic
left join filtro_m f on  last_day(date(f.fecha), month) =last_day(date(lo.fecha_login), month)
where   (f.Fecha_Nombre = '{date}')
group by lic.ACCOUNTID,vendor,lic.SUSCRIPCIONES,lic.LICENCIAS, lic.BUZONES,pais_filtro
)
SELECT
    licencias_vencidas_asignadas.ACCOUNTID  AS licencias_vencidas_asignadas_accountid,
    licencias_vencidas_asignadas.VENDOR  AS licencias_vencidas_asignadas_vendor,
    licencias_vencidas_asignadas.SUSCRIPCIONES  AS licencias_vencidas_asignadas_suscripciones,
    licencias_vencidas_asignadas.LICENCIAS  AS licencias_vencidas_asignadas_licencias,
    licencias_vencidas_asignadas.BUZONES  AS licencias_vencidas_asignadas_buzones
FROM licencias_vencidas_asignadas
WHERE (licencias_vencidas_asignadas.pais_filtro ) IS NOT NULL
GROUP BY
    1,
    2,
    3,
    4,
    5
ORDER BY
    1
)

"""
    )

    # Espera a que la consulta termine
    results = query_job.result()

    row = next(results)

    # Acceder al valor del número en la primera fila
    suscripcioners = row[0]
    # Mostrar el valor
    print("Excel Suscripciones: ", suscripcioners)  # Esto imprimirá: 140163

    # Acceder al valor del número en la Segunda fila
    licencias_vendidas = row[1]
    # Mostrar el valor
    print("Excel Licencias Vendidas: ", licencias_vendidas) 

    # Acceder al valor del número en la Tercera fila
    licencias_ocupadas = row[2]
    # Mostrar el valor
    print("Excel Licencias Ocupadas: ", licencias_ocupadas)

    return suscripcioners, licencias_vendidas, licencias_ocupadas
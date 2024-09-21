from google.cloud import bigquery

def query_Excel_Login_Activity_Detail(date):
    # Crea un cliente de BigQuery
    client = bigquery.Client()

    # Ejecuta la consulta
    query_job = client.query(
    f'''
    --- EXCEL LOGIN
    -- Login
    SELECT SUM(reporte_mensual_2_login), COUNT(reporte_mensual_2_ac)
    FROM(
    WITH reporte_mensual_2 AS (with  filtro_m as (
            Select distinct date_trunc(date(id_fecha), month) as fecha,
                    cast (cast(date_trunc(date(id_fecha), month) as date)as string) fecha_String,
                    CAST(CONCAT(CAST(extract(year from date_trunc(date(id_fecha), month)) AS STRING),
                    LPAD(CAST(extract(month from date_trunc(date(id_fecha), month)) AS STRING),2,'00'),
                    LPAD(CAST(extract(day from date_trunc(date(id_fecha), month)) AS STRING),2,'00')) AS INTEGER)*-1 ORDEN_FECHA,
                    concat(extract(year from date_trunc(date(id_fecha), month)),' ',FORMAT_DATETIME("%h", DATETIME(date_trunc(date(id_fecha), month))) )as Fecha_Nombre
            from amco-cd-qa.GRAL_N.LOGIN_ACTIVIDAD_CDN order by 3 asc
        ),
    login as(
    SELECT  pais ,ID_SUSCRIPCION_ODIN,ID_ACCOUNT_ODIN,ACTIVO as ac, plan,login ,ID_FECHA as fecha_login
    FROM `amco-cd-qa.GRAL_N.LOGIN_ACTIVIDAD_CDN`
    group by pais,ID_FECHA,ID_ACCOUNT_ODIN,ID_SUSCRIPCION_ODIN,plan,ac,login
    ),
    licencias as (
    SELECT vendor,sum(SUSCRIPCIONES) as suscripciones_s ,sum(l.LICENCIAS) as lic_vendidas, sum(BUZONES) as buzones ,ID_FECHA as fecha_lic
    FROM `amco-cd-qa.GRAL_N.LICENCIAS_VENDIDAS_ASIGNADAS_CDN` l
    group by vendor,ID_FECHA
    )
    select lo.pais, lo.ID_SUSCRIPCION_ODIN, lo.ac, lo.ID_ACCOUNT_ODIN, lo.plan,SPLIT(lo.pais, ' ')[OFFSET(0)] as pais_filtro,  lo.login,lic.suscripciones_s, lic.lic_vendidas, lic.buzones from login as lo
    left join licencias lic on lo.pais=lic.vendor and lo.fecha_login=lic.fecha_lic
    left join filtro_m f on  last_day(date(f.fecha), month) =last_day(date(lo.fecha_login), month)
    where   (f.Fecha_Nombre = '{date}')
    group by lo.pais, lo.ID_SUSCRIPCION_ODIN, lo.ID_ACCOUNT_ODIN,lo.plan, lo.ac, pais_filtro, lo.login, lic.suscripciones_s, lic.lic_vendidas, lic.buzones
    )
    SELECT
        reporte_mensual_2.ID_ACCOUNT_ODIN  AS reporte_mensual_2_id_account_odin_1,
        reporte_mensual_2.ID_SUSCRIPCION_ODIN  AS reporte_mensual_2_id_suscripcion_odin_1,
        reporte_mensual_2.pais  AS reporte_mensual_2_pais,
        reporte_mensual_2.plan  AS reporte_mensual_2_plan,
        reporte_mensual_2.ac  AS reporte_mensual_2_ac,
        reporte_mensual_2.login  AS reporte_mensual_2_login
    FROM reporte_mensual_2
    WHERE (reporte_mensual_2.pais) IS NOT NULL
    GROUP BY ALL
    ORDER BY
        1
    )
    '''

    )

    # Espera a que la consulta termine
    results = query_job.result()

    row = next(results)

    # Acceder al valor del número en la primera fila
    login = row[0]
    # Mostrar el valor
    print("Excel Login: ", login)  # Esto imprimirá: 140163

    # Acceder al valor del número en la Segunda fila
    activos = row[1]
    # Mostrar el valor
    print("Excel Activos: ", activos)

    return login, activos
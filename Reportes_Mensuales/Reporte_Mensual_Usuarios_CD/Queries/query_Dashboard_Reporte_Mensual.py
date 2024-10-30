from google.cloud import bigquery

def query_Dashboard(date):
    # Crea un cliente de BigQuery
    #client = bigquery.Client(project="amco-cv-prod") # Solo aplica a Proyectos en la Nube.

    # Crea un cliente de BigQuery
    client = bigquery.Client()

    # Ejecuta la consulta
    query_job = client.query(
    f"""
    WITH reporte_3 AS (with  filtro_m as (
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
    count(activo) as activo, sum(Login) as sum_login ,ID_FECHA as fecha_login
    FROM `amco-cd-qa.GRAL_N.LOGIN_ACTIVIDAD_CDN`
    where
    pais !='NOASIGANDO'
    group by 1,pais,ID_FECHA
    ),
    licencias as (
    SELECT  case when vendor is null then 'SIN VENDOR' when vendor like 'MEXICO%' THEN vendor else replace(vendor,' ','') end completo,
    case when vendor is null then 'SIN VENDOR'
    WHEN vendor like 'MEXICO%' THEN 'MEXICO' else replace(vendor,' ','')  end as vendor  ,
    sum(SUSCRIPCIONES) as suscripciones ,sum(l.LICENCIAS) as lic_vendidas, sum(BUZONES) as buzones ,ID_FECHA as fecha_lic
    FROM  amco-cd-qa.GRAL_N.LICENCIAS_VENDIDAS_ASIGNADAS_CDN  l
    group by 1,vendor,ID_FECHA
    )
    select lo.completo, lo.pais, lo.activo, lo.sum_login, lic.suscripciones, lic.lic_vendidas, lic.buzones
    from login as lo
    left join licencias lic on lo.completo=lic.completo   and lo.fecha_login=lic.fecha_lic
    left join filtro_m f on  last_day(date(f.fecha), month) =last_day(date(lo.fecha_login), month)
    where   (f.Fecha_Nombre = '{date}') -- '2024 Aug'
    group by completo, lo.pais,  lo.activo, lo.sum_login, lic.suscripciones, lic.lic_vendidas, lic.buzones,lic.vendor
    )
    SELECT
        COALESCE(SUM(CAST( reporte_3.suscripciones   AS NUMERIC)), 0) AS t_sus,
        COALESCE(SUM(CAST( reporte_3.lic_vendidas   AS NUMERIC)), 0) AS t_lic_vendidas,
        COALESCE(SUM(CAST( reporte_3.buzones   AS NUMERIC)), 0) AS t_con_login,
        COALESCE(SUM(CAST( reporte_3.sum_login   AS NUMERIC)), 0) AS t_lic_ocupa,
        COALESCE(SUM(CAST( reporte_3.activo   AS NUMERIC)), 0) AS t_activos
    FROM reporte_3
    WHERE (reporte_3.pais ) IS NOT NULL
    """
    )

    # Espera a que la consulta termine
    results = query_job.result()

    row = next(results)

    # Acceder al valor del número en la primera fila
    suscripcioners = row[0]
    # Mostrar el valor
    print("Suscripciones: ", suscripcioners)  # Esto imprimirá: 140163

    # Acceder al valor del número en la Segunda fila
    licencias_vendidas = row[1]
    # Mostrar el valor
    print("Licencias Vendidas: ", licencias_vendidas) 

    # Acceder al valor del número en la Tercera fila
    licencias_ocupadas = row[2]
    # Mostrar el valor
    print("Licencias Ocupadas: ", licencias_ocupadas) 

    # Acceder al valor del número en la Cuarta Fila
    login = row[3]
    print("Login: ", login)

    # Acceder al valor del número en la Quinta Fila
    activos = row[4]
    print("Activos: ", activos)

    return suscripcioners, licencias_vendidas, licencias_ocupadas, login, activos
from google.cloud import bigquery
from datetime import date, timedelta

def query_Dashboard(country):
    # Crea un cliente de BigQuery
    #client = bigquery.Client(project="amco-cv-prod") # Solo aplica a Proyectos en la Nube.

    # Crea un cliente de BigQuery
    client = bigquery.Client()

    # Creamos la Fecha de consulta: N - 1
    yesterday = str(date.today() - timedelta(days=1))

    #yesterday = '2024-12-24' # La fecha fue 25

    # Ejecuta la consulta
    query_job = client.query(
    f"""
        SELECT 
            COALESCE(SUM(bi_ca_fac_login_registro_looker.NUM_EVENTOS), 0) AS total_eventos
        FROM `amco-cv-des.BI.BI_CA_FAC_LOGIN_REGISTRO_LOOKER` AS bi_ca_fac_login_registro_looker
        JOIN `amco-cv-des.BQ.BQ_CA_DIM_PAIS` AS bq_ca_dim_pais
            ON bi_ca_fac_login_registro_looker.ID_PAIS = bq_ca_dim_pais.ID_PAIS
        LEFT JOIN `amco-cv-des.BI.BI_CA_DIM_MENSAJE_ERROR` AS bi_ca_dim_mensaje_error
            ON bi_ca_fac_login_registro_looker.ID_MENSAJE_ERROR = bi_ca_dim_mensaje_error.ID_MENSAJE_ERROR
        WHERE 
            (bi_ca_fac_login_registro_looker.ID_PAIS IS NULL OR bi_ca_fac_login_registro_looker.ID_PAIS NOT IN (759, 760))
            AND NOT (bi_ca_fac_login_registro_looker.ID_RESULTADO = 0 
                AND bi_ca_fac_login_registro_looker.ID_TIPO_EVENTO = 2 
                AND bi_ca_fac_login_registro_looker.ID_ORIGEN_EVENTO = 17)
            AND bi_ca_fac_login_registro_looker.PAIS IS NOT NULL
            AND bq_ca_dim_pais.PAIS = '{country}'
            AND bi_ca_fac_login_registro_looker.ID_FECHA = '{yesterday}'
    """
    )

    # Espera a que la consulta termine
    results = query_job.result()

    row = next(results)

    # Acceder al valor del número en la primera fila
    value = row[0]

    return value
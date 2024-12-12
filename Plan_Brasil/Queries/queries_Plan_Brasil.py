from google.cloud import bigquery

def query_Brasil(table, var_country, country, var_date, date):
    
    alias = table.split('.')[-1]
    
    # Crea un cliente de BigQuery
    #client = bigquery.Client(project="amco-cv-prod") # Solo aplica a Proyectos en la Nube.

    # Crea un cliente de BigQuery
    client = bigquery.Client()

    # Ejecuta la consulta
    query_job = client.query(
        f"""
        SELECT 
            CASE 
                WHEN EXISTS (
                    SELECT 1 
                    FROM {table}
                    WHERE {var_country} = '{country}'
                    AND {var_date} <= '{date}'
                ) THEN 1 
                ELSE 0 
            END AS {alias}_BRASIL;
        """
    )

    # Espera a que la consulta termine
    results = query_job.result()

    row = next(results)

    print(row)

    valor = row[0]

    # Mostrar valor
    print("Valor: ", valor ) 
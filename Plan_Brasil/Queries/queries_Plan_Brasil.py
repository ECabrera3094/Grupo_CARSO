from google.cloud import bigquery

def query_Brasil(table, var_country, country, var_date, date):
    
    alias = table.split('.')[-1]

    # Estas variables se encargan de formatear los valores de country y date según su tipo (str o int) antes de incluirlos en la consulta SQL.
    # verifica si las variables country y date son cadenas de texto (str). Si lo son, se envuelven entre comillas simples. 
    # Si no lo son (por ejemplo, son enteros), se convierten a cadenas sin envolverlas.
    # isinstance(country, str): Esta función verifica si country es una cadena (str).
    formatted_country = f"'{country}'" if isinstance(country, str) else str(country)
    formatted_date = f"'{date}'" if isinstance(date, str) else str(date)

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
                    WHERE {var_country} = {formatted_country}
                    AND {var_date} <= {formatted_date}
                ) THEN 1 
                ELSE 0 
            END AS {alias}_BRASIL;
        """
    )

    # Espera a que la consulta termine
    results = query_job.result()

    row = next(results)

    print("Row: ", row)

    valor = row[0]

    # Mostrar Resultado
    print("Resultado: ", valor) 
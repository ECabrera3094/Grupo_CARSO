
import pytest
import sys
from datetime import datetime

class TestClaro():

    #@classmethod
    @pytest.fixture(autouse=True, scope="class")
    def setUpClass(cls):
        pass
    
    def validate_data(self, date, countries):
        print("VALIDACION FECHA")
        fecha_str = date
        try:
            # Formatear solo la fecha
            fecha_ingresada = datetime.strptime(fecha_str, "%Y%m%d").strftime('%Y%m%d')  
            print(f"Fecha ingresada: {fecha_ingresada}")

            fecha_hoy = datetime.today().strftime("%Y%m%d") 
            print("Fecha de Hoy:", fecha_hoy)

            if fecha_ingresada > fecha_hoy:
                print("No pueden se puede ingresar una fecha mayor al día de hoy.")
                sys.exit(1)
            elif  fecha_ingresada == fecha_hoy:
                print("La fecha ingresada es igual a la fecha actual")
            elif fecha_ingresada < fecha_hoy:
                diferencia_dias = (int(fecha_hoy) - int(fecha_ingresada))
                # La diferencia no puede ser mayor a 89 días
                print(f"La fecha ingresada es menor y la diferencia es de {diferencia_dias} días.")
            
        except ValueError:
            print(f"Error: La fecha '{fecha_str}' no tiene el formato correcto. Debe ser YYYYMMDD.")
            sys.exit(1)
        
        print("VALIDACION PAIS")
        # Captura de la lista de países (esperamos una cadena separada por comas)
        paises_str = countries.upper()
        paises = [pais.strip() for pais in paises_str.split(",")]
        print(f"Paises ingresados: {paises}")
        print(len(paises))

        list_Countries = ['ARGENTINA',
                    'BRASIL',
                    'CHILE',
                    'COLOMBIA',
                    'COSTARICA',
                    'DOMINICANA',
                    'ECUADOR',
                    'ELSALVADOR',
                    'GUATEMALA',
                    'HONDURAS',
                    'MEXICO',
                    'NICARAGUA',
                    'PANAMA',
                    'PARAGUAY',
                    'PERU',
                    'URUGUAY']

        if paises == ["ALL"]:
            print("Es un Pais ALL")
            # Se ejecuta normal
        for pais in paises:
            if pais not in list_Countries:
                print(f"Error: El país '{pais}' no se encuentra en la lista permitida.")
                break
        else:
            print("Todos los países ingresados son válidos.")

    def test_ClaroVideo(self,test_params):
        date, countries = test_params
        print("\n=====> Inicio del TestCase <=====")
        print(f"Parámetro 'date': {date}")
        print(f"Parámetro 'countries': {countries}")

        self.validate_data(date, countries)

        print("=====> Fin del TestCase <=====")


    #@classmethod
    @pytest.fixture(autouse=True, scope="class")
    def tearDownClass(cls):
        pass

if __name__ == '__main__':
    pytest.main()

# pytest test_reproceso.py --param1=HOLA --param2=Hola --capture=no
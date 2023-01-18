import pyodbc 
import requests 
import pandas as pd 

conn = pyodbc.connect('Driver={SQL Server};'
                        'Server=zzzz;'
                        'Database=zzzz;'
                        'UID=zzz;'
                        'PWD=z8#_;'
                        'Trusted_Connection=no;')

try:
    cursor = conn.cursor()
    cursor.execute('SELECT top 20 * FROM Table')

    for i in cursor:
        print(i)
except Exception as e:
    print("Erro: ", e)


r = requests.get("http://phd-data-service.aws.api.com.br/funds/positions?reference_date=2022-10-27")  


print(type(r))



data = "2022-10-27"
r = requests.get(f"http://phd-data-service.aws.api.com.br/funds/positions?reference_date={data}")

objeto_resposta = r.json()
data = objeto_resposta["data"]

listagem_obj = []

for data_obj in data:
    try:
        obj = {}
        obj["type"] = data_obj["type"]
        obj["id"] = data_obj["id"]
        for key in data_obj["attributes"].keys():
            obj[key] = data_obj["attributes"][key]
        
        listagem_obj.append(obj)
    except:
        print("Não foi possível tratar o objeto:", data_obj)

df = pd.DataFrame(listagem_obj)

df.to_sql()
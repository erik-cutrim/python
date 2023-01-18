# para abrir o jupyter rode o comando:
# python -m jupyterlab
# pasta: E:\Lista\Python>
# ir para pasta: cd E:\Lista\Python>

import pyodbc 

conn = pyodbc.connect('Driver={SQL Server};'
                        'Server=D3HWDBSQL001;'
                        'Database=FIRACmt;'
                        'UID=fira;'
                        'PWD=f1ra#hm1#2o18#_;'
                        'Trusted_Connection=no;')

try:
    cursor = conn.cursor()
    cursor.execute('SELECT top 20 * FROM ListaAtencao')

    for i in cursor:
        print(i)
except Exception as e:
    print("Erro: ", e)


# lista_objetos = [
# {
# coluna1: valor
# coluna2: valor
# },
# {
# coluna1: valor
# coluna2: valor
# }
# ]


# df = pd.DataFrame(lista_objetos)

# df.to_sql(cursor,)


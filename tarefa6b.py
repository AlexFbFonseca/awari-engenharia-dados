from minio import Minio
from minio.error import S3Error

# Configure as informações de conexão com o servidor MinIO
minio_client = Minio(
    "localhost:9000",  # Endereço e porta do servidor MinIO
    access_key="VAj4RYCd7Jf2aR7t",
    secret_key="AWDM9UHhJuzLHEQNP419maSWFSDuueXR",
    region="sa-east-1",
    secure=False  # Defina como True se você estiver usando HTTPS
)

def remove_special_characters(input_string):
    # Remove all characters that are not alphanumeric or spaces
    return re.sub(r'[^a-zA-Z0-9\s]', '', input_string)

# Nome do seu bucket
bucket_name = 'tarefa-06'
sub_bucket_name = ''
# minio_client.make_bucket(bucket_name)

import re
import csv

# Abra o arquivo CSV em modo de leitura
with open(r'C:\Users\alxfo\Desktop\awari-engenharia-de-dados-docker-main\exercicios\municipios-estados\csv\estados.csv', newline='') as arquivo_csv:
    # Crie um objeto leitor CSV
    leitor_csv = csv.reader(arquivo_csv)
    
    # Itere pelas linhas do arquivo CSV
    for linha in leitor_csv:

        # Acesse os valores das colunas pelo índice
        coluna1 = linha[0]
        coluna2 = linha[1]
        coluna3 = linha[2]
        coluna4 = linha[3]
        coluna5 = linha[4]
        coluna6 = linha[5]

        string2a = coluna2.lower() 
        string2b = remove_special_characters( string2a )

        print( string2b )
        # ... faça algo com os valores das colunas

        # Nome da pasta que você deseja criar
        sub_bucket_name = bucket_name + '-' + string2b 
        print( sub_bucket_name )

        try:
            # Crie a pasta dentro do bucket
            # minio_client.make_bucket( bucket_name )
            minio_client.make_bucket( sub_bucket_name )
            # minio_client.put_object(bucket_name, f"{pasta}/", "")
            # print(f"Pasta '{pasta}' criada com sucesso no bucket '{bucket_name}'.")
        except S3Error as e:
            print(f"Erro ao criar a pasta: {e}")


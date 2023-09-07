import os
import io
import minio
import json
import pandas as pd
import pyarrow as pa

# Configuração do cliente MinIO
minio_endpoint = 'localhost:9000'  # Substitua pelo endpoint do seu servidor MinIO
access_key = "VAj4RYCd7Jf2aR7t"
secret_key = "AWDM9UHhJuzLHEQNP419maSWFSDuueXR"
minio_bucket = "tarefa-08"  # Nome do balde no MinIO
secure=False  # Defina como True se você estiver usando HTTPS
local_folder_path = r'C:\users\alxfo\Desktop\awari-engenharia-de-dados-docker-main\exercicios\municipios-estados\csv'  # Caminho da pasta com arquivos CSV
folder_path = os.path.join( local_folder_path )
minio_path = "tarefa-08"  # Caminho da pasta no MinIO onde os arquivos JSON serão armazenados

# Conexão com o servidor MinIO
client = minio.Minio(minio_endpoint, access_key, secret_key, secure=False)

# Listar todos os arquivos CSV na pasta local
csv_files = [f for f in os.listdir(local_folder_path) if f.endswith('.csv')]

# Para cada arquivo CSV, faça a conversão para JSON e faça o upload no MinIO
for csv_file in csv_files:

    ################## GENÉRICO
    csv_path = os.path.join( folder_path, csv_file)
    df = pd.read_csv( csv_path )

    ################### CSV

    # Read the CSV file as bytes
    with open( csv_path , 'rb' ) as csv_file_open:
        csv_data = csv_file_open.read()

    # Calculate the length (size) of the data in bytes
    data_length = len(csv_data)
    
    # client.put_object(minio_bucket, minio_path, csv_file )
    # client.put_object( minio_bucket, csv_file , io.BytesIO(csv_data), data_length )
    # print(f'O arquivo CSV {csv_file} foi feito upload no MinIO.')

    
    ################### JSON
   
    ###  Converter o DataFrame para JSON
    json_data = df.to_json(orient='records')

    ###  Definir o nome do arquivo JSON no MinIO
    json_file = os.path.splitext(csv_file)[0] + '.json'
    minio_json_path = os.path.join(minio_path, json_file)

    # Fazer upload do arquivo JSON para o MinIO
    #client.put_object( minio_bucket, json_file , io.BytesIO(json_data.encode()), len(json_data))
    #print(f'O arquivo CSV {csv_file} foi convertido para JSON e feito upload como {minio_json_path} no MinIO.')

    ################### PARQUET

    # Definir o nome do arquivo Parquet no MinIO
    parquet_file = os.path.splitext(csv_file)[0] + '.parquet'
    minio_parquet_path = os.path.join(minio_path, parquet_file)

    # Converter o DataFrame para Parquet
    table = pa.Table.from_pandas(df)

    # Converter o DataFrame para o formato Parquet e salvar no MinIO
    ## with pa.OSFile(minio_parquet_path, 'wb') as f:
    ##    pa.write_table(table, f)
    ##    print(f'O arquivo CSV {csv_file} foi convertido para PARQUET e feito upload como { minio_parquet_path } no MinIO.')

    # variaveis do processo
    print( folder_path )
    print( csv_file )
    print( csv_path )
    print( data_length )
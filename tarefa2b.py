import os
import subprocess

# Substitua "<seu_username>/<seu_conjunto_de_dados>" pelo seu nome de usuário e nome do conjunto de dados no Kaggle.
dataset_id = "alexfbfonseca/global-youtube-statistics-2023"

# Certifique-se de configurar a variável de ambiente 'KAGGLE_USERNAME' e 'KAGGLE_KEY'
# com seu nome de usuário e chave da API do Kaggle, respectivamente.
# Você pode encontrá-los na página de configuração da sua conta do Kaggle.
os.environ['KAGGLE_USERNAME'] = 'alexfbfonseca'
os.environ['KAGGLE_KEY'] = 'da3dcb53f21705609525f01bdd81702e'

# Comando de download gerado pelo Kaggle.
download_command = f'kaggle datasets download -d {dataset_id}'

# Execute o comando para baixar o conjunto de dados.
subprocess.call(download_command, shell=True)

# Verifique se o arquivo foi baixado com sucesso.
if os.path.exists(f'{dataset_id.split("/")[1]}.zip'):
    print(f'O conjunto de dados {dataset_id} foi baixado com sucesso.')
else:
    print(f'Houve um erro ao baixar o conjunto de dados {dataset_id}.')

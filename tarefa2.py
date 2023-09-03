import os

# Define as credenciais da API do Kaggle (você pode encontrar essas informações na sua conta do Kaggle)
os.environ['KAGGLE_USERNAME'] = 'alexfbfonseca'
os.environ['KAGGLE_KEY'] = 'da3dcb53f21705609525f01bdd81702e'

# Comando para baixar o conjunto de dados (substitua pelo comando copiado da página do conjunto de dados)
kaggle_command = 'kaggle datasets download -d alexfbfonseca/global-youtube-statistics-2023'

# Execute o comando usando a função `os.system`
os.system(kaggle_command)

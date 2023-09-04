import csv

# Abra o arquivo CSV em modo de leitura
with open(r'C:\Users\alxfo\Desktop\awari-engenharia-de-dados-docker-main\exercicios\municipios-estados\csv\estados.csv', newline='') as arquivo_csv:
    # Crie um objeto leitor de dicionário CSV
    leitor_csv = csv.DictReader(arquivo_csv)
    
    # Itere pelas linhas do arquivo CSV
    for linha in leitor_csv:
        # Acesse os valores das colunas pelo nome
        coluna1 = linha['codigo_uf']
        coluna2 = linha['uf']
        coluna3 = linha['nome']
        coluna4 = linha['latitude']
        coluna5 = linha['longitude']
        coluna6 = linha['regiao']
        # ... faça algo com os valores das colunas

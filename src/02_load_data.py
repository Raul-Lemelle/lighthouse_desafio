import os
import pandas as pd
from dotenv import load_dotenv

def load_and_display_data(directory):
    # Dicionário para armazenar os DataFrames
    dataframes = {}

    # Percorrer todos os arquivos na pasta especificada
    for filename in os.listdir(directory):
        if filename.endswith(".csv"):
            # Caminho completo do arquivo
            file_path = os.path.join(directory, filename)
            # Nome do DataFrame com base no nome do arquivo
            df_name = "DF_" + filename.split('.')[0].upper()
            # Carregar o CSV em um DataFrame
            dataframes[df_name] = pd.read_csv(file_path)
            # Exibir as primeiras linhas do DataFrame
            print(f"{filename}:")
            print(dataframes[df_name].head(), "\n")

    return dataframes

if __name__ == "__main__":
    
    # Carregar variáveis de ambiente do arquivo .env
    load_dotenv()

    # Caminho para a pasta que contém os arquivos CSV
    silver_path = os.getenv('SILVER_PATH')
    
    # Chamada da função para visualizar os dataframes 
    DATAFRAMES = load_and_display_data(silver_path)
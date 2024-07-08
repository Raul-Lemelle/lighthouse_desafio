import zipfile
import os
from dotenv import load_dotenv

def extract_zip_file(zip_path, extract_path):
    """
    Extrai um arquivo zip para um diretório específico se os arquivos ainda não foram extraídos.

    Args:
    - zip_path (str): Caminho para o arquivo zip a ser extraído.
    - extract_path (str): Caminho para o diretório onde o arquivo zip será extraído.
    """
    # Verificar se o arquivo zip existe
    if not os.path.exists(zip_path):
        raise FileNotFoundError(f"O arquivo {zip_path} não foi encontrado. Verifique o caminho e a existência do arquivo.")

    # Verificar se o diretório de extração existe, caso contrário, criá-lo
    if not os.path.exists(extract_path):
        os.makedirs(extract_path)

    # Verificar quais arquivos já existem no diretório de extração
    existing_files = set(os.listdir(extract_path))

    # Tentar abrir o arquivo zip e extrair apenas arquivos que não foram extraídos ainda
    try:
        with zipfile.ZipFile(zip_path, 'r') as zip_ref:
            zip_files = set(zip_ref.namelist())
            files_to_extract = zip_files - existing_files
            
            if not files_to_extract:
                print(f"Todos os arquivos do zip já foram extraídos em {extract_path}.")
            else:
                for file in files_to_extract:
                    zip_ref.extract(file, extract_path)
                print(f"Arquivos extraídos com sucesso em {extract_path}: {files_to_extract}")
    except zipfile.BadZipFile:
        raise zipfile.BadZipFile(f"O arquivo {zip_path} não é um arquivo zip válido.")
    except Exception as e:
        raise Exception(f"Ocorreu um erro ao extrair o arquivo: {e}")

if __name__ == "__main__":
    # Carregar variáveis de ambiente do arquivo .env
    load_dotenv()

    # Obter caminhos do arquivo zip e do diretório de extração das variáveis de ambiente
    zip_path = os.getenv('BRONZE_PATH')
    extract_path = os.getenv('SILVER_PATH')

    # Verificar se as variáveis de ambiente foram carregadas corretamente
    if not zip_path:
        raise ValueError("A variável de ambiente BRONZE_PATH não está definida.")
    if not extract_path:
        raise ValueError("A variável de ambiente SILVER_PATH não está definida.")

    # Chamar a função para extrair o arquivo zip
    extract_zip_file(zip_path, extract_path)

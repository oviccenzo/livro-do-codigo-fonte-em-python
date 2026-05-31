##5.3 Montando o dicionário de metadados

# import os
#
# for meta_files in os.listdir('data/meta-data'):
#   print(meta_files)


####Criando os arquivos de metadados

####Vamos criar os arquivos `empreendimento.txt`, `execucaoFinanceira.txt`, `instituicao.txt` e `licitação.txt`
# dentro do diretório `data/meta-data` para que `os.listdir` possa encontrá-los.

import os

directory_path = 'data/meta-data'

# Lista de nomes de arquivos a serem criados
file_names = ['Empreendimento.txt', 'execucaoFinanceira.txt', 'instituicao.txt', 'licitacao.txt']

for file_name in file_names:
    file_path = os.path.join(directory_path, file_name)
    try:
        with open(file_path, 'w') as f:
            f.write(f'Conteúdo de teste para {file_name}\n')
        print(f"Arquivo '{file_name}' criado com sucesso.")
    except Exception as e:
        print(f"Erro ao criar o arquivo '{file_name}': {e}")

import os

directory_path = 'data/meta-data'

# files_names

### Verificando novamente os arquivos no diretório

# Agora que os arquivos foram criados, vamos listar o conteúdo do diretório `data/meta-data`
# novamente para confirmar que eles aparecem.

import os

for meta_files in os.listdir('data/meta-data'):
  print(meta_files)
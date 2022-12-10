from time import sleep
import os.path
from random import randint
import requests
from unidecode import unidecode

from models import Cep, CepRange, create_tables
from settings import CEP_MIN, CEP_MAX, DATABASE_FILE


if not (os.path.isfile(DATABASE_FILE)):
    create_tables()
    
    cep_range = CepRange(
        min_cep = CEP_MIN,
        max_cep = CEP_MAX
    )
    cep_range.save()

# url api
base_url = "https://viacep.com.br/ws/"
  
# formato da resposta
response_format = "/json/"

# obtem cep inicial
get_cep = CepRange.get().last_cep
if get_cep < CEP_MIN:
    get_cep = CEP_MIN

print('Iniciando consultas!')
  
while get_cep <= CEP_MAX:
    URL = base_url + str(get_cep) + response_format
    try:
        r = requests.get(url = URL)
    except Exception as e:
        print('Erro ao realizar consulta API!')
        break
    
    # extrai resposta
    data = r.json()
    
    # codigo status da resposta
    status_code = r.status_code
    
    # verifica se retornou erro
    erro = 'erro' in data.keys()
    
    if not erro and status_code == 200:
        cep = data['cep']
        logradouro = data['logradouro']
        complemento = data['complemento']
        bairro = data['bairro']
        localidade = data['localidade']
        uf = data['uf']
        ibge = data['ibge']
        gia = data['gia']
        ddd = data['ddd']
        siafi = data['siafi']
        
        #tratamento dos dados
        cep = int(cep.replace('-',''))
        logradouro = unidecode(logradouro.upper()).strip()
        complemento = unidecode(complemento.upper()).strip()
        bairro = unidecode(bairro.upper()).strip()
        localidade = unidecode(localidade.upper()).strip()
        uf = unidecode(uf.upper()).strip()
        ibge = int(ibge)
        gia = int(gia)
        ddd = int(ddd)
        siafi = int(siafi)
        
        # grava cep no banco de dados
        Cep.create(
            cep = cep,
            logradouro = logradouro,
            complemento = complemento,
            bairro = bairro,
            localidade = localidade,
            uf = uf,
            ibge = ibge,
            gia = gia,
            ddd = ddd,
            siafi = siafi
        )
        
        # atualiza ultimo cep consultado
        cep_range = CepRange.get()
        cep_range.last_cep = cep
        cep_range.save()
    
        print(f'{Cep.get(cep = cep).cep}... OK!')
        sleep(randint(0,4))
    elif erro and status_code == 200:
        print(f'{get_cep}... CEP não encontrado.')
    else:
        print('Erro inesperado, tente novamente')
        break

    get_cep += 1
    
print('Fim das consultas!')
    
import requests
import re

from acesso_cep import BuscaEndereco
from CPF_CNPJ import CpfCnpj, Documentos
from validate_docbr import CPF, CNPJ
from telefonesbr import TelefonesBr
from datetime import datetime, timedelta
from datas_br import DatasBr

# cep = 72146206
# objeto_cep = BuscaEndereco(cep)
# print(objeto_cep)

# r = requests.get("https://viacep.com.br/ws/01001000/json/")

# print(type(r.text))

# a = objeto_cep.acessa_via_cep()

# print(type(a))
# print()
# print(dir(a))

# print(a.text)
# print()
# print(a.json())

# bairro, cidade, uf = objeto_cep.acessa_via_cep()

# print(bairro, cidade, uf)

# cpf = 25632258157
# objeto_cpf = Cpf(cpf)

# format_cpf = Cpf(cpf)
# print(format_cpf)

# cpf_um = Cpf("05632258157")
# print(cpf_um)

# exemplo_cnpj = "35379838000112"
# exemplo_cpf = "05632258157"
# cnpj = CNPJ()
# print(cnpj.validate(exemplo_cnpj))

# documento = CpfCnpj(exemplo_cpf, 'cpf')
# print(documento)

# documento = Documentos.cria_documento(exemplo_cpf)
# print(documento)

# padrao = "\w{5,50}@[a-z]\w{3,10}.com.br"
# texto = "aaabbbcc rodrigo123@gmail.com.br ffsfsfsfsdfs qweqweqeqweqd"
# resposta = re.search(padrao, texto)
# print(resposta.group())

# padrao_mole = "(xx)aaaa-wwww"
# padrao = "[0-9]{2}[0-9]{4,5}[0-9]{4}"

# texto = "eu gosto do numero 2126451234 e gosto também do 2136431234"
# resposta = re.search(padrao, texto) 
# print(resposta.group())

# telefone = "2126481234"

# telefone_objeto = TelefonesBr(telefone)

# padrao = "([0-9]{2,3})?([0-9]{2})([0-9]{4,5})([0-9]{4})"
# resposta = re.search(padrao, telefone)

# print(resposta.group())

# print(telefone_objeto)
# cadastro = DatasBr()
# print(cadastro.mes_cadastro())
# print(cadastro.dia_semana())

# hoje = datetime.today()
# hoje_formatado = hoje.strftime("%d/%m/%Y %H:%M")
# print(hoje)
# print(hoje_formatado)
# print(type(hoje_formatado))

# cadastro = DatasBr()
# print(cadastro)

hoje = DatasBr()

print(hoje.tempo_cadastro())


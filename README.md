# totverprm
API para acesso aos Webservices do TOTVS ERP RM.

## Instalação

pip install totverprm

### Exemplo para criação de um aluno:
```python
from datetime import datetime
from totvserprm.educational import Student

server = '192.168.1.100:8051'
username = 'admin'
password = 'admin'

stundet = Student(server, username, password)
stundet.create(
  codcoligada=1,
  codtipocurso=1,
  data_nascimento=datetime(1992, 2, 3, 4, 5),
  estado_natal='MG',
  naturalidade='Belo Horizonte',
  nome='Fulano de tal',
  ra=35
)
```

### Exemplo para criação de um cliente:
```python
from datetime import datetime
from totvserprm.financial import Client

server = '192.168.1.100:8051'
username = 'admin'
password = 'admin'

client = Client(server, username, password)
client.create(
  ativo=True,
  codexterno=1,
  codcoligada=0,
  codcoligada_contexto=1,
  cpf_cnpj='11781328110', # Sem formatação
  tipo_rua=1, # RUA = 1 / AVENIDA = 6
  tipo_bairro=1, # BAIRRO = 1
  bairro='Belvedere',
  rua='Rua Professor Pedro Aleixo',
  numero=695,
  estado='MG', # EX = Exterior
  cidade='Belo Horizonte',
  codigo_municipio=06200, # Ultimos 5 digitos do codigo do ibge do município
  pais=1, # 1 = Brasil, 2 = Portugal, 11 = Angola
  data_nascimento=datetime(1990,5,14),
  nome='Cliente Teste Vetrol',
  classificacao=1, # 1 = Cliente, 2 = Fornecedor, 3 = Ambos
  categoria='F', # F = Pessoa Física, J = Pessoa Jurídica
  cep='30320-300'
)
```

### Exemplo para criação de um boleto:
```python
from datetime import datetime
from totvserprm.financial import Billet

server = '192.168.1.100:8051'
username = 'admin'
password = 'admin'

boleto = Billet(server, username, password)
boleto.create(
  codcoligada=1,
  codcoligada_contexto=1,
  codcoligada_cfo=0,
  data_vencimento=datetime(2017,10,30),
  valor='100,55', # Enviar string com separação por vírgula
  codcliente='0000470',
  codfilial=1,
  classificacao=1, # 1 = Receber, 2 = Pagar
  tipo_documento='999', # 999 = Taxa de adesão
  conta=1,
  historico='Teste', # Descrição
  centro_custo='01.019'
)
```


### Exemplo de consulta SQL:
```python
from totvserprm.retrieve import ConsultSQL

server = '192.168.1.100:8051'
username = 'admin'
password = 'admin'

consultsql = ConsultSQL(server, username, password)
consultsql.get(
  codcoligada=0,
  codsistema='F',
  codsentenca='CODIGO_CONSULTA',
  parameters={'PARAMETRO_1': 'VALOR_1', 'PARAMETRO_2': 'VALOR_1'}
)
```

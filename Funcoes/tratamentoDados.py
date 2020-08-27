
import json 
from unicodedata import normalize

estados = '{"AC": "Acre","AL": "Alagoas","AP": "Amapá","AM": "Amazonas","BA": "Bahia","CE": "Ceará","DF": "Distrito Federal","ES": "Espírito Santo","GO": "Goiás","MA": "Maranhão","MT": "Mato Grosso","MS": "Mato Grosso do Sul","MG": "Minas Gerais","PA": "Pará","PB": "Paraíba","PR": "Paraná","PE": "Pernambuco","PI": "Piauí","RJ": "Rio de Janeiro","RN": "Rio Grande do Norte","RS": "Rio Grande do Sul","RO": "Rondônia","RR": "Roraima","SC": "Santa Catarina","SP": "São Paulo","SE": "Sergipe","TO": "Tocantins"}'
estados_json = json.loads(estados)

# Funcao para converter uma UF no nome do respectivo estado 
def converter_sigla2nome (sigla):
    
    sigla = sigla.upper()

    try:
        resultado = estados_json [sigla]
    except:
        resultado = 0
    finally:
        return resultado

# Teste
estado = converter_sigla2nome ('CE')
print(estado)

# Funcao que retira a acentuacao das palavras
def remover_acentos(txt):
    return normalize('NFKD', txt).encode('ASCII', 'ignore').decode('ASCII')

#Teste
texto = remover_acentos('Raíssâáó') 
print(texto)

# Funcao que padroniza textos para facilitar o tramento de entradas
def padronizar_texto (texto): 

    texto = remover_acentos(texto)
    texto = texto.replace(" ","_")
    texto = texto.replace("-","_")
    texto = texto.lower()
    return texto 

# Teste
texto = padronizar_texto('Raíssa-Ellen')
print(texto)
from nltk import word_tokenize
from biblioteca import *


with open('dados/artigo_100_palavras.txt', 'r', encoding="utf8") as f: # f = file
    texto_fonte = f.read()


tokens_texto = word_tokenize(texto_fonte) # Cria token para palavras e símbolos

tokens_alpha = tokens_sem_pontuacao(tokens_texto)

tokens_normalizados = normalizacao(tokens_alpha)

tokens_sem_repeticao = set(tokens_normalizados)# Quantidade de palavras sem repetições


palavra_teste = 'lgica'
palavras = gerador_palavras(palavra_teste) # Fatia e coloca cada letra do alfabeto concatenado entre as fatias
print(len(palavras))

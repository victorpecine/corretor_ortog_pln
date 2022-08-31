from nltk import word_tokenize, FreqDist
from biblioteca import *


with open('dados/artigo_100_palavras.txt', 'r', encoding="utf8") as f: # f = file
    texto_fonte = f.read()


tokens_texto = word_tokenize(texto_fonte) # Cria token para palavras e símbolos

tokens_alpha = tokens_sem_pontuacao(tokens_texto)

tokens_normalizados = normalizacao(tokens_alpha) # Palavras em lower case

# tokens_sem_repeticao = set(tokens_normalizados) # Quantidade de palavras sem repetições


frequencia = FreqDist(tokens_normalizados) # Calcula a frequência de cada palavra no texto_fonte
total_palavras = len(tokens_normalizados)


def probabilidade(palavra):
    return frequencia[palavra]/total_palavras


def corretor(palavra):
    palavras_geradas = gerador_palavras(palavra.lower())
    palavra_correta = max(palavras_geradas, key=probabilidade) # A palavra com maior probabilidade será considerada a correção
    return palavra_correta


palavra_buscada = 'lorem' # lorem 3% de probabilidade

prob = probabilidade(palavra_buscada)
print(prob)

correcao = corretor(palavra_buscada)
print(correcao)

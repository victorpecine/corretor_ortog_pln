from nltk import word_tokenize
from biblioteca import tokens_sem_pontuacao, normalizacao

with open('dados/artigo_100_palavras.txt', 'r', encoding="utf8") as f: # f = file
    artigo = f.read()


tokens_artigo = word_tokenize(artigo) # Cria token para palavras e símbolos

tokens_alpha = tokens_sem_pontuacao(tokens_artigo)


tokens_normalizados = normalizacao(tokens_alpha)
print(tokens_normalizados)

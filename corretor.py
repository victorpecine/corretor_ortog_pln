from enum import unique
from nltk import word_tokenize
from biblioteca import tokens_sem_pontuacao

with open('dados/artigos.txt', 'r', encoding="utf8") as f: # f = file
    artigos = f.read()


tokens_artigos = word_tokenize(artigos) # Cria token para palavras e símbolos

tokens_alpha = tokens_sem_pontuacao(tokens_artigos) # 403031

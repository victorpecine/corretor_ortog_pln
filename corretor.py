from nltk import word_tokenize
from biblioteca import tokens_sem_pontuacao, normalizacao


with open('dados/artigo_100_palavras.txt', 'r', encoding="utf8") as f: # f = file
    texto_fonte = f.read()


tokens_texto = word_tokenize(texto_fonte) # Cria token para palavras e símbolos

tokens_alpha = tokens_sem_pontuacao(tokens_texto)


tokens_normalizados = normalizacao(tokens_alpha)


# Quantidade de palavras sem repetições
tokens_sem_repeticao = set(tokens_normalizados)

print(len(tokens_sem_repeticao))

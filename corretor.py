from nltk import word_tokenize, FreqDist
from biblioteca import *


with open('dados/artigos.txt', 'r', encoding="utf8") as f: # f = file
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


def novo_corretor(palavra):
    palavras_geradas = gerador_palavras(palavra.lower())
    palavras_geradas_turbinado = gerador_turbinado(palavra.lower())
    todas_palavras = set(palavras_geradas + palavras_geradas_turbinado)
    possiveis_palavras = [palavra]
    for palavra in todas_palavras:
        if palavra in vocabulario:
            possiveis_palavras.append(palavra)
    palavra_correta = max(possiveis_palavras, key=probabilidade) # A palavra com maior probabilidade será considerada a correção
    return palavra_correta


# Cálculo da taxa de acerto do corretor
def avaliador(lista_palavras_teste, vocabulario):
    numero_palavras = len(lista_palavras_teste)
    acertos = 0
    desconhecidas = 0
    for correta, errada in lista_palavras_teste:
        palavra_corrigida = corretor(errada)
        desconhecidas += (correta not in vocabulario)
        if palavra_corrigida == correta:
            acertos += 1       
    taxa_acerto = (acertos / numero_palavras) * 100
    taxa_palavras_desconhecidas = (desconhecidas / numero_palavras) * 100
    print('Taxa de acerto: {:.2f}% no total de {} palavras'.format(taxa_acerto, numero_palavras))
    print('Taxa de palavras desconhecidas: {:.2f}% no total de {} palavras'.format(taxa_palavras_desconhecidas, numero_palavras))


palavra_buscada = 'lóogica'

palavras_geradas_turbinado = gerador_turbinado(gerador_palavras(palavra_buscada))

vocabulario = set(tokens_normalizados)

# texto_avaliado = avaliador(teste, vocabulario)

print(corretor(palavra_buscada))
print(novo_corretor(palavra_buscada))

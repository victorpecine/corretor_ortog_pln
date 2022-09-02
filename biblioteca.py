from nltk import FreqDist

def tokens_sem_pontuacao(lista_tokens):
    lista_palavras = []
    for token in lista_tokens:
        if token.isalpha():
            lista_palavras.append(token)    
    return lista_palavras


def normalizacao(lista_palavras):
    lista_normalizada = []
    for palavra in lista_palavras:
        lista_normalizada.append(palavra.lower())
    return lista_normalizada


def insere_letra(fatias):
    novas_palavras = []
    letras = 'abcdefghijklmnopqrstuvwxyzàáâãèéêìíîòóôõùúûç'
    for E, D in fatias:
        for letra in letras:
            novas_palavras.append(E + letra + D) # Testa todas as possibilidades
    return novas_palavras


def gerador_palavras(palavra):
    fatias = []
    for i in range(len(palavra) + 1):
        fatias.append((palavra[:i], palavra[i:]))
    palavras_geradas = insere_letra(fatias)
    palavras_geradas += deleta_caractere(fatias)
    palavras_geradas += troca_letra(fatias)
    palavras_geradas += inverte_letra(fatias)
    return palavras_geradas


# def corretor(palavra):
#     palavras_geradas = gerador_palavras(palavra.lower())
#     palavra_correta = max(palavras_geradas, key=probabilidade)
#     return palavra_correta


# def frequencia(lista_normalizada):
#     frequencia_palavras = FreqDist(lista_normalizada)
#     return frequencia_palavras


# def total_palavras(lista_normalizada):
#     total_palavras = len(lista_normalizada)
#     return total_palavras


# def probabilidade(frequencia_palavras, palavra_buscada):
#     probabilidade_palavra = frequencia_palavras[palavra_buscada] / total_palavras
#     return probabilidade_palavra


def cria_dados_teste(nome_arquivo):
    lista_palavras_teste = []
    f =  open(nome_arquivo, 'r', encoding="utf8") 
    for linha in f:
        correta, errada = linha.split()
        lista_palavras_teste.append((correta, errada))
    f.close()
    return lista_palavras_teste


# def avaliador(lista_palavras_teste):
#     numero_palavras = len(lista_palavras_teste)
#     acertos = 0
#     for correta, errada in lista_palavras_teste:
#         palavra_corrigida = corretor(errada)
#         if palavra_corrigida == correta:
#             acertos += 1
#     taxa_acerto = acertos / numero_palavras
#     print('Taxa de acerto: {}'format(taxa_acerto))


def deleta_caractere(fatias):
    novas_palavras = []
    for E, D in fatias:
        novas_palavras.append(E + D[1:])
    return novas_palavras


def troca_letra(fatias):
    novas_palavras = []
    letras = 'abcdefghijklmnopqrstuvwxyzàáâãèéêìíîòóôõùúûç'
    for E, D in fatias:
        for letra in letras:
            novas_palavras.append(E + letra + D[1:]) # Testa todas as possibilidades
    return novas_palavras


def inverte_letra(fatias):
    novas_palavras = []
    for E, D in fatias:
        if len(D) > 1:
            novas_palavras.append(E + D[1] + D[0] + D[2:])
    return novas_palavras

def tokens_sem_pontuacao(lista_tokens):
    lista_palavras = []
    for token in lista_tokens:
        if token.isalpha():
            lista_palavras.append(token)    
    return lista_palavras

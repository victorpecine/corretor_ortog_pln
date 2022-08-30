with open('dados/artigos.txt', 'r', encoding="utf8") as f: # f = file
    artigos = f.read()

# Quantidade de palavras
tokes_artigos = len(artigos.split()) # 416903 tokens
print(tokes_artigos)

import re


def le_assinatura():
    """A funcao le os valores dos tracos linguisticos do modelo e devolve uma assinatura a ser comparada com os textos fornecidos"""
    print("Bem-vindo ao detector automático de COH-PIAH.")
    print("Informe a assinatura típica de um aluno infectado:")

    wal = float(input("Entre o tamanho médio de palavra:"))
    ttr = float(input("Entre a relação Type-Token:"))
    hlr = float(input("Entre a Razão Hapax Legomana:"))
    sal = float(input("Entre o tamanho médio de sentença:"))
    sac = float(input("Entre a complexidade média da sentença:"))
    pal = float(input("Entre o tamanho medio de frase:"))

    return [wal, ttr, hlr, sal, sac, pal]


def le_textos():
    """A funcao le todos os textos a serem comparados e devolve uma lista contendo cada texto como um elemento"""
    i = 1
    textos = []
    texto = input("Digite o texto " + str(i) + " (aperte enter para sair):")
    while texto:
        textos.append(texto)
        i += 1
        texto = input("Digite o texto " + str(i) + " (aperte enter para sair):")

    return textos


def separa_sentencas(texto):
    """A funcao recebe um texto e devolve uma lista das sentencas dentro do texto"""
    sentencas = re.split(r'[.!?]+', texto)
    if sentencas[-1] == '':
        del sentencas[-1]
    return sentencas


def separa_frases(sentenca):
    """A funcao recebe uma sentenca e devolve uma lista das frases dentro da sentenca"""
    return re.split(r'[,:;]+', sentenca)


def separa_palavras(frase):
    """A funcao recebe uma frase e devolve uma lista das palavras dentro da frase"""
    return frase.split()


def n_palavras_unicas(lista_palavras):
    """Essa funcao recebe uma lista de palavras e devolve o numero de palavras que aparecem uma unica vez"""
    freq = dict()
    unicas = 0
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            if freq[p] == 1:
                unicas -= 1
            freq[p] += 1
        else:
            freq[p] = 1
            unicas += 1

    return unicas


def n_palavras_diferentes(lista_palavras):
    """Essa funcao recebe uma lista de palavras e devolve o numero de palavras diferentes utilizadas"""
    freq = dict()
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            freq[p] += 1
        else:
            freq[p] = 1

    return len(freq)


def compara_assinatura(as_a, as_b):
    """IMPLEMENTAR. Essa funcao recebe duas assinaturas de texto e deve devolver o grau de similaridade nas assinaturas."""
    print("este é a", as_a)
    print("este é b", as_b)
    i = 0
    soma = 0
    while i < len(as_b):
        soma = as_a[i] + as_b[i]
        i = i + 1
    grau_similaridade = (soma//6)
    return grau_similaridade


def calcula_assinatura(texto):
    """IMPLEMENTAR. Essa funcao recebe um texto e deve devolver a assinatura do texto."""
    i = 0
    caracter_per_sentence = 0
    caracter_per_frases = 0
    soma = 0
    soma_caract = 0
    sentencas = separa_sentencas(texto)
    frases = []
    palavras = []
    caracteres = []
    for sent in sentencas:
        frases += separa_frases(sent)
    for fr in frases:
        palavras += separa_palavras(fr)
    for i in texto:
        soma_caract = soma_caract + len(i)
    for i in palavras:
        soma = soma + len(i)
    for i in sentencas:
        caracter_per_sentence = caracter_per_sentence + len(i)
    for i in frases:
        caracter_per_frases = caracter_per_frases + len(i)

    wal = soma/len(palavras)
    ttr = n_palavras_diferentes(palavras)/len(palavras)
    hlr = n_palavras_unicas(palavras)/len(palavras)
    sal = caracter_per_sentence/len(sentencas)
    sac = len(frases)/len(sentencas)
    pal = caracter_per_frases/len(frases)
    return [wal, ttr, hlr, sal, sac, pal]


def avalia_textos(textos, ass_cp):
    """IMPLEMENTAR. Essa funcao recebe uma lista de textos e uma assinatura ass_cp e deve devolver o numero (1 a n) do texto com maior probabilidade de ter sido infectado por COH-PIAH."""
    pass


def conta_caracteres(texto):
    soma = 0
    for i in re.split(r'\W+', texto):
        soma = soma + len(i)
    return soma


def main():
    as_b = (le_assinatura())
    textos = le_textos()
    print(type(textos))
    i = 0
    while i < len(textos):
        print("Este é o texto", i+1)
        as_a = calcula_assinatura(textos[i])
        print(compara_assinatura(as_a, as_b))
        i = i + 1


main()
# print("frases",len(frases))
# print("palavras",len(palavras))
# print(n_palavras_unicas(palavras))
# print(n_palavras_diferentes(palavras))

# wal = total_caracteres/len(palavras)
# ttr = n_palavras_diferentes(palavras)/len(palavras)
# hlr = n_palavras_unicas(palavras)/len(palavras)
# sal = total_caracteres/len(sentencas)
# sac = len(frases)/len(sentencas)


# print("valor de wal é: ", wal)
# print("valor de ttr é: ", ttr)
# print("valor de hlr é: ", hlr)
# print("valor de sal é: ", sal)
# print("valor de sac é: ", sac)

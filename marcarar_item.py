def mascarar(item):
    s = str(item)
    p = ''
    lista_de_caracteres = []
    if len(s) <= 4:
        return s
    else:
        for i in range(len(s)):
            lista_de_caracteres.append(s[i])
    for j in range(len(lista_de_caracteres)-4):
        lista_de_caracteres[j]='#'
    for elem in lista_de_caracteres:
        p+=elem
    return p

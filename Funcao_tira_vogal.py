def tira_vogal(string):
    lista_vogais=['a','e','i','o','u','A','E','I','O','U']
    lista_consoante=[]
    s = ''
    for j in string:
        if j not in lista_vogais:
            lista_consoante.append(j)
    for i in lista_consoante:
        s= s+i
    return s


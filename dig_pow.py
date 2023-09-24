def dig_pow(n,p):
    s = str(n) #Transforma n em string
    m = 0
    digitos_de_n=[]
    for i in range(len(s)):
        digitos_de_n.append(int(s[i])) #transforma cada digito de s em int e adiciona na lista digitos_de_n
    for j in range(len(digitos_de_n)): #para cada elemento na lista digitos_de_n
        m+=digitos_de_n[j]**(p+j) #somar com m
    if m%n==0: #Se n divide m, então existe um k tal que k*n=m
        return m//n
    else:
        return -1


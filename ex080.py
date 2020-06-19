numList = []

for cont in range(0, 5):
    num = int(input(f'Informe o {cont+1}º valor: '))
    if cont == 0:
        numList.append(num)
    elif num > numList[-1]: # se o número informado for maior que o último da lista.
        numList.append(num)
    else:
        pos = 0
        while pos < len(numList): # do ínicio até o final
            if num <= numList[pos]:
                numList.insert(pos, num)
                # se o número for menor ou igual ao número anterior da lista, troca suas posições.
                break
            pos += 1
        
print(numList)
print(f'Maior: {numMaior} \nMenor: {numMenor}')
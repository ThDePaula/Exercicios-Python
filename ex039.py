from datetime import date #Importação para pegar o ano atual.
ano = int(input('Informe o ano de seu nascimento: '))
hoje = str(date.today())
atual = int(hoje[:4]) #Transformação de String para Int e pegando apenas os 4 primeiro digitos, no caso, o ano atual.
idade = atual - ano
if idade < 18:
   temp_falta = 18 - idade
   if temp_falta > 1:
       print('Ainda faltam {} anos para você se alistar!'.format(temp_falta))
   else:
       print('Você deverá se apresentar ano que vem, fique atento!')
elif idade == 18:
   print('Esta é a hora de se alistar!!')
else:
   temp_passou = idade - 18
   resp = int(input(('Você já se alistou? \n[ 1 ] Sim - [ 2 ] Não\n')))
   if resp == 1:
       print('Ótimo, então não se preocupe!')
   elif temp_passou == 1:
       print('Seu tempo de alistamento foi ano passado... \nVá se alistar, jovem!')
   else:
       print('Já passaram {} anos do tempo de se alistar \nVá se alistar!!!!!'.format(temp_passou))

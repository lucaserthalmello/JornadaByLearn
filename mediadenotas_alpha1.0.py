#Calcular média para n termos:
#Ed. Alpha_1.0

#Primeiro definimos a rotina calcular_media(notas):
def calcular_media(notas):
  quantidade=len(notas)
  soma=sum(notas)
  media=soma/quantidade
  return media
#Depois definimos a rotina verificar_aprovacao(media):
def verificar_aprovacao(media):
  if media >=5:
    print('O aluno foi Aprovado')
  else:
    print('o aluno foi Reprovado')
#Por último, definimos a nota através de uma lista:
notas=[10,9.1,8.5,7.75]
print('As Notas foram:')
print(notas)
media=calcular_media(notas)
verificar_aprovacao(media)
print('aperte ENTER para sair do programa')

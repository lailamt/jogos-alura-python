import adivinhacao
import forca

print("*********************************")
print("Bem vindo ao menu!")
print("Escolha seu jogo!")
print("1 - Adivinhação")
print("2 - Forca")
print("*********************************")

jogo = int(input("Escolha o jogo: "))

if(jogo == 1):
  print("Jogo de adivinhação!")
  adivinhacao.jogar()
elif(jogo == 2):
  print("Jogo da forca!")
  forca.jogar()

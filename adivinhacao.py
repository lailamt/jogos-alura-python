import random

def jogar():
  print("*********************************")
  print("Bem vindo ao jogo de adivinhação!")
  print("Tente adivinhar o número escolhido pela máquina!")
  print("Você acha que consegue?")
  print("O valor do chute deve ser um inteiro entre 0 e 100")
  print("*********************************")

  numero_rand = random.randrange(0,101)
  #numero = 42
  tentativas = 0
  pontos = 1000
  #print(numero_rand)

  print("Qual o núvel de dificuldade?")
  print("1 - Fácil")
  print("2 - Intermediário")
  print("3 - Difícil")
  print("666 - Impossível")

  nivel = int(input("Defina o nível: "))

  if(nivel == 1):
    tentativas = 20
  elif(nivel == 2):
    tentativas = 10
  elif(nivel == 3):
    tentativas = 5
  elif(nivel == 666):
    print("Você perdeu!")
  else:
    print("Nível inválido!")

  for rodada in range(1,tentativas+1):
    # Interpolação de string
    # formata a string, substituindo o valor de {} com as variáveis
    print("Tentativa {} de {}".format(rodada, tentativas))
    chute = int(input("Digite o seu numero: "))

    if (chute < 0 or chute > 100):
      print("Digite um número válido (entre 0 e 100)")
      continue

    acertou = chute == numero_rand
    menor   = chute < numero_rand
    maior   = chute > numero_rand

    if (acertou):
      print("Você acertou e fez {} pontos!".format(pontos))
      break
    else:
      if(menor):
        print("Seu chute foi baixo!")
        if (rodada == tentativas):
          print("O número secreto era {}. Você fez {}".format(numero_rand, pontos))
      elif(maior):
        print("Seu chute foi alto!")
        if (rodada == tentativas):
          print("O número secreto era {}. Você fez {}".format(numero_rand, pontos))
      pontos_perdidos = abs(numero_rand - chute)
      pontos = pontos - pontos_perdidos


  print("Fim de jogo!")

if(__name__ == "__main__"):
  jogar()
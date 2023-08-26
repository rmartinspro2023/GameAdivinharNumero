import random

def jogo_adivinhacao():
  numero_secreto = random.randint(1, 20)
  tentativas = 0
   
  print("Bem-vindo ao jogo de adivinhação!")
   
  while tentativas < 5:
    try:
      palpite = int(input("Tente adivinhar o número secreto (entre 1 e 20): "))
      tentativas += 1
      
      if palpite < numero_secreto:
        print("Tente um número maior!")
      elif palpite > numero_secreto:
        print("Tente um número menor!")
      else:
        print(f"Parabéns! Você acertou o número secreto {numero_secreto} em {tentativas} tentativas.")
        break
    except ValueError:
        print("Error::: Por favor, insira um numero")
        continue
    
  if palpite != numero_secreto:
    print(f"Você excedeu o número de tentativas. O número secreto era {numero_secreto}.")

jogo_adivinhacao()

from random import randint
# radint serve para gerar numeros inteiros
secreto = randint(1, 50)
# o radint coloca os numeros inteiros que você seleciona dentro do parenteses, depois de atribuir em uma variavel
total_de_tentativas = 5

print('que dificuldade você deseja jogar?')
print('(1) Fácil (2) Médio (3) Difícil (4) impossível', secreto)

nivel = int(input (" eu escolho o nivel "))

pontos = 100

if nivel == 1:
    total_de_tentativas = 10
    print("você escolheu o nível fácil, começando o jogo")

elif nivel == 2:

    total_de_tentativas = 5
    print("você escolheu o nível médio, começando o jogo")

elif nivel == 3:
    total_de_tentativas = 2

    print("você escolheu o nível difícil, começando o jogo")

else:
    total_de_tentativas = 1
    print ("você escolheu o nível impossível. boa sorte.")

while (total_de_tentativas > 0):
    print("você tem {} tentativas".format(total_de_tentativas))


    chute = int(input("tente acertar um numero entre 1 e 50. "
                      "A sua escolha é: "))

    if chute <1 or chute>50:
        print ("digitie um numero ENTRE 1(UM) E 50(CINQUENTA)")
        #total_de_tentativas +=1
        continue
        #continue pula a interação dita no if, então nesse caso faz a mesma coisa do "total_de_tentativas +=1"

    if chute == secreto:
        print (f"você acertou! a sua pontuação foi {pontos} de 100")
        print ("fim de jogo!")
        break
    else:
        if chute > secreto:
            print("o seu chute foi muito alto!")
            pontos -= abs(secreto - chute)#abs serve para fazer tipo: se o numero for -20, o abs faz virar 20, mostrando
            #quanto falta pro numero chegar a 0, assim o numero nunca vai ser negativo.
            #e essa conta vai subtrair o valor do secreto pelo chute, dando o resultado de pontos


        elif chute < secreto:

            print("o seu chute foi muito baixo!")
            pontos -= abs(secreto - chute)

    total_de_tentativas -=1


    if total_de_tentativas == 0:
        print (f"você perdeu, o numero secreto era {secreto}" )
# tem que colocar ultima linha pq se n vai ficar rodando infinitamente
# o -1 é pra cada vez que errar tirar um ponto, serve para diminuir um ponto do total, que é atualiazdo

import discord
import emoji
from deep_translator import GoogleTranslator
from discord.ext import commands
import random
import asyncio
import time

client = commands.Bot(command_prefix = "$", case_insensitive = True)

@client.event
async def on_ready():
    print(' "Humanos são como oceanos, e não há ondas que eu não possa superar!" '.format(client))

@client.command()
async def sinbad(x):
    await x.send(emoji.emojize('''
===============
    SINBAD BOT :sailboat:
===============
                            
"Humanos são como oceanos!! 
   E não há ondas que eu não 
            possa superar!!!"

$ajuda para ver os comandos
'''))

@client.command()
async def ajuda(x):
    await x.send('''==============$$COMANDOS:computer:$$==============

============================================================

$ajuda => abre essa aba aqui :wink:

============================================================

$translate => o tradutor mais eficaz dos sete mares :earth_africa:!! Para traduzir uma palavra basta utilizar essa sintaxe:

    $translate oceano en => ocean (para palavras)

    $translate "O mundo nos espera!" en => The world awaits us (para frases)

=============================================================

$sort => para fazer sorteios rápidos para algum jogo :stuck_out_tongue_winking_eye:

    ex: $sort 10 => algum número aleatório entre 1 e 10

=============================================================

$super_flood => mete um numero se aloprar na potenciação :persevere:

    ex: $super_flood 2 100 => um mega numero imprimido

=============================================================

$velhinha => jogo da velha entre os djinns mais inteligentes do server :older_woman:

    ex: $velhinha @jogador1 @jogador2

=============================================================

$calcula => Uma calculadorinha simples, mas bastante eficaz!! Para fazer operações utilize:

    ex: $calcula 2 + 3

    símbolos para realizar as operações presentes na calculadora:

    "+" -> adição
    "-" -> subtração
    "x" -> multiplicação
    "p" -> potenciação
    "/" -> divisão
    "r" -> radiciação

==============================================================
    ''')

#função ola
@client.command()
async def ola(x):
    await x.send(f'Olá, {x.author}')

#função sorteio
@client.command()
async def sort(x, numero):
    sorteio = random.randint(1, int(numero))
    await x.send(f'O número sorteado foi: {sorteio}')

#função super_flood
@client.command()
async def super_flood(x, i, j):
    s = int(i) ** int(j)
    await x.send(f'{s}')

# função tradutor de palavras para o bot
@client.command()
async def translate(x, palavra, lingua):
    trad = GoogleTranslator(source = 'auto', target = lingua).translate(palavra)
    await x.send("Pode confiar! Já estive por todos os 4 cantos do mundo e posso traduzir sua mensagem com facilidade!")
    time.sleep(2)
    await x.send(f"{trad}")

#função adivinha
@client.command()
async def adivinha(x, numero: int):
    """Adivinhe o numero de 1 a 6"""
    valor = random.randint(1, 6)
    if numero == valor:
        await x.send("Acertou")
    else:
        await x.send("Errou")

#função calculadora
@client.command()
async def calcula(x, number1: float, operador, number2: float):
  
  operador = operador.lower()

  await x.send('''Uma calculadorinha simples, mas bastante eficaz!!
  
  Para fazer operações utilize:
  
    ex: $calcula 2 + 3 
    
    resultado esperado: 5.
    
  funções presentes nessa calculadora para realizar:
  
  - "+" - adição
  - "x" - multiplicação
  - "-" - subtração
  - "/" - divisão
  - "p" - potenciação
  - "r" - radiciação''')

  if operador == "adição" or operador == "+":
    await x.send("Ta aqui a soma meu chapa.")
    resultado = number1 + number2
    await x.send(f"O resultado é: {resultado}")
  elif operador == "subtração" or operador == "-":
    await x.send("Tá aqui a subtração meu chapa.")
    resultado = number1 - number2
    await x.send(f"O resultado é: {resultado}")
  elif operador == "multiplicação" or operador == "x":
    await x.send("Tá aqui a multiplicação meu chapa.")
    resultado = number1 * number2
    await x.send(f"O resultado é: {resultado}")
  elif operador == "potenciação" or operador == "p":
    await x.send("Tá aqui a potenciação meu chapa.")
    resultado = number1 ** number2
    await x.send(f"O resultado é: {resultado}")
  elif operador == "raiz quadrada" or operador == "r":
    await x.send("Tá aqui a sua raiz meu chapa.")
    resultado = number2 ** (1/number1)
    await x.send(f"O resultado é: {resultado:.2f}")
  elif operador == "divisão" or operador == "/":
    await x.send("Tá aqui a sua divisão meu chapa.")
    resultado = number1 / number2
    await x.send(f"O resultado é: {resultado}")

#jogo da velha para o bot
jogador1 = ""
jogador2 = ""
turno = ""
gameOver = True

condVitoria = [
    [0, 1, 2],
    [3, 4, 5],
    [6, 7, 8],
    [0, 3, 6],
    [1, 4, 7],
    [2, 5, 8],
    [0, 4, 8],
    [2, 4, 6]
]

@client.command()
async def velhinha(x, p1 : discord.Member, p2 : discord.Member):

    await x.send('''Bem-vindos ao duelo de djinns do jogo da velha!! Aqui está um pequeno tutorial pra que este duelo seja realizado:
    
    Primeiramente, olhe para as letras q/ w/ e/ a/ s/ d/ z/ x/ c. Notou algo interessante? Elas foram setadas como botões para esse jogo para que vc consiga visualizar melhor o tabuleiro no seu teclado! insira uma dessas letras que será referente a sua posição no tabuleiro!!!

    Para realizar uma ação no seu turno, utilize o comando $jogar. Por exemplo, ao digitar:

        $jogar s
    
        A jogada se dará na seguinte posição do tabuleiro:

        :white_large_square: :white_large_square: :white_large_square:

        :white_large_square: :regional_indicator_x: :white_large_square:

        :white_large_square: :white_large_square: :white_large_square:
        
       
        Bora jogar???''')

    global jogador1
    global jogador2
    global turno
    global gameOver
    global count

    if gameOver:
        global board
        board = [':black_large_square:', ':black_large_square:', ':black_large_square:',
                 ':black_large_square:', ':black_large_square:', ':black_large_square:',
                 ':black_large_square:', ':black_large_square:', ':black_large_square:']
        turno = ""
        gameOver = False
        count = 0

        jogador1 = p1
        jogador2 = p2

        #printando o tabuleiro
        linha = ""
        for i in range(len(board)):
            if i == 2 or i == 5 or i == 8:
                linha +=  " " + board[i]
                await x.send(linha)
                linha = ""
            else:
                linha += " " + board[i]

        #determinando turno

        num = random.randint(1, 2)
        if num == 1:
            turno = jogador1
            await x.send(f"É a vez de <@{str(jogador1.id)}>!!")
        elif num == 2:
            turno = jogador2
            await x.send(f"É a vez de <@{str(jogador2.id)}>!!")
    
    else:
        await x.send("Um jogo está rolando amigo, acabe primeiro para jogar outro :smile:")

@client.command()
async def jogar(x, pos):
    global turno
    global jogador1
    global jogador2
    global board
    global count
    global gameOver

    letras = ['237375428518523125738', 'q', 'w', 'e', 'a', 's', 'd', 'z', 'x', 'c']
    
    if gameOver == False:
        mark = ""
        if turno == x.author:
            if turno == jogador1:
                mark = ":regional_indicator_x:"
            elif turno == jogador2:
                mark = ":o2:"
            if pos in letras and board[letras.index(pos) - 1] == ":black_large_square:":
                board[letras.index(pos) - 1] = mark
                count += 1

                #imprime o tabuleiro:
                linha = ""
                for i in range(len(board)):
                    if i == 2 or i == 5 or i == 8:
                        linha +=  " " + board[i]
                        await x.send(linha)
                        linha = ""
                    else:
                        linha += " " + board[i]
                
                checkVencedor(condVitoria, mark)
                print(count)
                if gameOver == True:
                    await x.send(mark + " venceu!!")
                if count >= 9:
                    gameOver = True
                    await x.send("É um empate")

                #trocando turno
                if turno == jogador1:
                    turno = jogador2
                elif turno == jogador2:
                    turno = jogador1
            else:
                await x.send("Amigo para jogar use as letras q/ w/ e/ a/ s/ d/ z/ x/ c. Com elas vc poderá visualizar um tabuleiro de jogo da velha ;) ")

        else:
            await x.send("Não é sua vez amigo")
    else:
        await x.send("Comece um novo jogo usando $velhinha!!")

def checkVencedor(condVitoria, mark):
    global gameOver
    for cond in condVitoria:
        if board[cond[0]] == mark and board[cond[1]] == mark and board[cond[2]] == mark:
            gameOver = True

@velhinha.error
async def velhinha_error(x, error):
    print(error)
    if isinstance(error, commands.MissingRequiredArgument):
        await x.send("Onde está o outro jogador?? Você deve colocar o seu nome e o do jogador que deseja desafiar para esse duelo de djinns do jogo da velha :smile:")
    elif isinstance(error, commands.BadArgument):
        await x.send("Para desafiar e iniciar um jogo cite um jogador dessa maneira: (<@jogador>).")

@jogar.error
async def jogar_error(x, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await x.send("Ei amigo, insira a letra referente a posição que deseja jogar.")
    elif isinstance(error, commands.BadArgument):
        await x.send("Não se esqueça: As letras usadas nesse jogo são q/ w/ e/ a/ s/ d/ z/ x/ c.")


client.run('tokenHere')
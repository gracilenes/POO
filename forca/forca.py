
'''
Jogo da Forca
- O jogo da forca é um jogo de adivinhação de palavras.
- O jogador deve adivinhar uma palavra secreta, letra por letra.
- A cada letra errada, uma parte do corpo do boneco da forca é desenhada.
- O jogador tem um número limitado de tentativas para adivinhar a palavra.
- Se o jogador adivinhar a palavra antes de esgotar as tentativas, ele vence.
- Se o jogador esgotar as tentativas, ele perde e a palavra secreta é revelada.
- O jogo pode ser jogado com palavras de diferentes categorias, como animais, frutas, etc.
- O jogo vai ter um registro das palavras já jogadas, para evitar repetições e registra as vitórias.
'''
#https://pastebin.com/2BPjVvTV
 
import os
 
 
palavra = "morango"
# 7 letras, 6 letras diferentes
 
letras_erradas = []
letras_certas = []
tentativas = 6
palavra_adivinhada = False
print("Bem-vindo ao Jogo da Forca!")
 
def limpar_tela():
    # Verifica o sistema operacional
    if os.name == 'nt': # Para Windows
        os.system('cls')
    else: # Para macOS e Linux
        os.system('clear')
 
def atualizar_tela():
    limpar_tela()
    print(f"{tentativas-len(letras_erradas)} tentativas restantes.")
    for letra in palavra:
        if letra in letras_certas:
            print(letra, end=" ")
        else:
            print("_", end=" ")
 
atualizar_tela()
while not palavra_adivinhada and len(letras_erradas) < tentativas:
    print()
    for i in range(97, 123):
        if chr(i) in letras_certas or chr(i) in letras_erradas:
            pass
        else:
            print(chr(i), end=" ")
 
    letra = input("\nDigite uma letra: ").lower()
 
    if letra in letras_certas or letra in letras_erradas: # letra já foi
        print("Você já tentou essa letra. Tente outra.")
    elif letra in palavra: # letra certa
        letras_certas.append(letra)
    else: # letra errada
        letras_erradas.append(letra)
 
 
    qtd_letras_certas = 0
    for letra in palavra:
        if letra in letras_certas:
            qtd_letras_certas += 1
 
    if qtd_letras_certas == len(palavra):
        print("Parabéns! Você adivinhou a palavra!")
        palavra_adivinhada = True
    elif len(letras_erradas) == tentativas:
        print("Você perdeu! A palavra era:", palavra)
 
    input("Pressione uma tecla para continuar...")
    atualizar_tela()
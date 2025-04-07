class Jogo:
    def iniciar(self):
        print("O jogo começou!")
Jogo = Jogo()
Jogo.iniciar()

class Personagem:
    def pular(self):
        print("O Personagem pulou!")
Personagem = Personagem()
Personagem.pular()

class Inimigo:
    def atacar(self):
        print("O inimigo atacou!")
Inimigo = Inimigo()
Inimigo.atacar()

class Pontuacao:
    def zerar_pontos(self):
        print("Pontuação zerada")
Pontuacao = Pontuacao()
Pontuacao.zerar_pontos()

class Menu:
    def iniciar_jogo(self):
        print("O jogo está começando!")

    def mostrar_opcoes(self):
        print("1. Iniciar Jogo")
        print("2. Mostrar Opções")
        print("3. Sair")

    def sair(self):
        print("Saindo do jogo, até logo!")
Menu = Menu()

Menu.iniciar_jogo()
Menu.mostrar_opcoes()
Menu.sair()

class Personagem:
    def __init__(self, nome):
        self.nome = nome
    
    def dizer_nome(self):
        print(f"Meu nome é {self.nome}")
Personagem = Personagem("Gracilene")
Personagem.dizer_nome()

class Pontuacao:
    def __init__(self):
        self.pontos = 0

    def adicionar_pontos(self, quantidade):
        self.pontos += quantidade

    def mostrar_pontos(self):
        print(f"Pontuação atual {self.pontos}")
Pontuacao = Pontuacao()
Pontuacao.adicionar_pontos(25)
Pontuacao.adicionar_pontos(35)
Pontuacao.mostrar_pontos()

class Personagem:
    def __init__(self):
        self.vida = 100
    
    def tomar_dano(self,dano):
        self.vida -= dano
        if self.vida <= 0:
            print("Gamer Over!")
        else:
            print(f"vida restante: {self.vida}")
Personagem = Personagem()
Personagem.tomar_dano(45)
Personagem.tomar_dano(75)
Personagem.tomar_dano(28)

class Jogador:
    def __init__(self):
        self.energia = 50
    
    def recuperar_energia(self, quantidade):
        self.energia += quantidade
        print(f"Energia recuperada! Energia atual: {self.energia}")

    def usar_energia(self, quantidade):
        if self.energia - quantidade < 0:
            print("Sem energia suficiente!")
        else:
            self.energia -= quantidade
            print(f"Energia usada! Energia atual: {self.energia}")
Jogador = Jogador()
Jogador.usar_energia(40)
Jogador.recuperar_energia(30)
Jogador.usar_energia(60)

class Personagem:
    def __init__(self, nome, vida=100):
        self.nome = nome
        self.vida = vida

    def exibir_status(self):
        print(f'{self.nome} - Vida: {self.vida}')

class Inimigo:
    def __init__(self, nome):
        self.nome = nome
        self.vida = 100  # Inicializa a vida do inimigo com 100

    def atacar(self, alvo):
        if isinstance(alvo, Personagem):
            alvo.vida -= 10  # Reduz a vida do personagem alvo em 10 pontos
            print(f'{self.nome} atacou {alvo.nome}. A vida de {alvo.nome} agora é {alvo.vida}.')
        else:
            print('O alvo não é um personagem válido.')

personagem1 = Personagem("Herói")
inimigo1 = Inimigo("Goblin")

personagem1.exibir_status()
inimigo1.atacar(personagem1)
personagem1.exibir_status()

import random
class Personagem:
    def __init__(self, nome, vida=100):
        self.nome = nome
        self.vida = vida

    def exibir_status(self):
        print(f'{self.nome} - Vida: {self.vida}')

    def atacar(self, alvo):
        if isinstance(alvo, (Personagem, Inimigo)):  # O alvo pode ser um Personagem ou um Inimigo
            dano = random.randint(5, 20)
            alvo.vida -= dano  # Reduz a vida do alvo pelo valor do dano
            print(f'{self.nome} atacou {alvo.nome} causando {dano} de dano. Vida restante de {alvo.nome}: {alvo.vida}')

class Inimigo:
    def __init__(self, nome, vida=100):
        self.nome = nome
        self.vida = vida

    def exibir_status(self):
        print(f'{self.nome} - Vida: {self.vida}')

    def atacar(self, alvo):
        if isinstance(alvo, (Personagem, Inimigo)):  # O alvo pode ser um Personagem ou um Inimigo
            dano = random.randint(5, 20)
            alvo.vida -= dano  # Reduz a vida do alvo pelo valor do dano
            print(f'{self.nome} atacou {alvo.nome} causando {dano} de dano. Vida restante de {alvo.nome}: {alvo.vida}')

def combate(personagem, inimigo):
    while personagem.vida > 0 and inimigo.vida > 0:
        personagem.atacar(inimigo)  # Personagem ataca primeiro
        if inimigo.vida <= 0:
            print(f'{inimigo.nome} foi derrotado! {personagem.nome} venceu a batalha!')
            break
        inimigo.atacar(personagem)  # Inimigo ataca depois
        if personagem.vida <= 0:
            print(f'{personagem.nome} foi derrotado! {inimigo.nome} venceu a batalha!')
            break

personagem = Personagem("Herói")
inimigo = Inimigo("Goblin")

combate(personagem, inimigo)

import random
class Inimigo:
    def __init__(self, nome, vida=50):
        self.nome = nome
        self.vida = vida

    def atacar(self, alvo):
        if isinstance(alvo, Jogador):
            dano = random.randint(5, 20)
            alvo.energia -= dano
            print(f'{self.nome} atacou {alvo.nome} causando {dano} de dano à energia. Energia restante de {alvo.nome}: {alvo.energia}')

class Jogador:
    def __init__(self, nome):
        self.nome = nome
        self.energia = 100  # Energia inicial do jogador
        self.pontos = 0  # Pontos iniciais do jogador
        self.pontuacao = Pontuacao()  # Cria a instância de Pontuacao associada ao jogador

    def atacar(self, inimigo):
        if self.energia <= 0:
            print(f'{self.nome} não tem energia suficiente para atacar. É hora de descansar!')
            return
        if isinstance(inimigo, Inimigo):
            dano = random.randint(5, 20)
            inimigo.vida -= dano
            self.energia -= 10  # Perde 10 de energia a cada ataque
            print(f'{self.nome} atacou {inimigo.nome} causando {dano} de dano. Energia restante de {self.nome}: {self.energia}')

            if inimigo.vida <= 0:
                self.pontos += 10  # Ganha 10 pontos ao derrotar o inimigo
                print(f'{inimigo.nome} foi derrotado! {self.nome} ganhou 10 pontos. Pontuação total: {self.pontos}')

    def descansar(self):
        if self.energia < 100:
            energia_recuperada = 20
            self.energia += energia_recuperada
            if self.energia > 100:
                self.energia = 100  # Energia não pode ultrapassar 100
            print(f'{self.nome} descansou e recuperou {energia_recuperada} de energia. Energia atual: {self.energia}')
        else:
            print(f'{self.nome} já está com energia cheia!')

class Pontuacao:
    def __init__(self):
        self.pontos = 0

    def atualizar_pontos(self, pontos):
        self.pontos += pontos

    def mostrar_pontos(self):
        print(f'Pontuação atual: {self.pontos}')

def combate(jogador, inimigo):
    while jogador.energia > 0 and inimigo.vida > 0:
        # Jogador ataca
        jogador.atacar(inimigo)
        if inimigo.vida <= 0:
            print(f'{jogador.nome} venceu a batalha!')
            break
        # Inimigo ataca
        inimigo.atacar(jogador)
        if jogador.energia <= 0:
            print(f'{jogador.nome} ficou sem energia! {inimigo.nome} venceu a batalha!')
            break

jogador = Jogador("Herói")
inimigo1 = Inimigo("Goblin")
inimigo2 = Inimigo("Orc")

combate(jogador, inimigo1)
jogador.descansar()
combate(jogador, inimigo2)


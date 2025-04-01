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

class Inimigo:
    def __init__(self, nome):
        self.nome = nome
        self.vida = 100

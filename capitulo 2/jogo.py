class Personagem:
    def __init__(self, nome, vida):
        self.nome = nome
        self.__vida = vida  # atributo privado
    def mostrar_vida(self):
        return self.__vida  # método público para acessar o valor de __vida
heroi = Personagem("Maria", 100)
print(heroi.mostrar_vida())  # Saída: 100

class Pontuacao:
    def __init__(self):
        self.__pontos = 0  # atributo privado
    def adicionar_pontos(self, valor):
        if isinstance(valor, int) and valor > 0:
            self.__pontos += valor
        else:
            print("Valor inválido. Só é possível adicionar pontos inteiros positivos.")
    def mostrar_pontos(self):
        return self.__pontos  # método adicional para consultar os pontos, se necessário
pontuacao = Pontuacao()
pontuacao.adicionar_pontos(10)
print(pontuacao.mostrar_pontos())  # Saída: 10
pontuacao.adicionar_pontos(-5)     # Saída: Valor inválido...

class Inimigo:
    def __init__(self, nome, forca):
        self.nome = nome
        self.__forca = forca  # atributo privado
    def atacar(self):
        print(f"{self.nome} ataca com força {self.__forca}!")  # usa o atributo privado internamente
orc = Inimigo("Orc Guerreiro", 25)
orc.atacar()  # Saída: Orc Guerreiro ataca com força 25!

class Jogador:
    def __init__(self, nome, energia):
        self.nome = nome
        self.__energia = max(0, min(energia, 100))  # Garante valor inicial entre 0 e 100
    def usar_energia(self, valor):
        if isinstance(valor, int) and valor > 0:
            self.__energia = max(0, self.__energia - valor)
        else:
            print("Valor inválido. Informe um número inteiro positivo.")
    def recuperar_energia(self, valor):
        if isinstance(valor, int) and valor > 0:
            self.__energia = min(100, self.__energia + valor)
        else:
            print("Valor inválido. Informe um número inteiro positivo.")
    def mostrar_energia(self):
        return self.__energia
jogador = Jogador("Gaby", 80)
print(jogador.mostrar_energia())  # Saída: 80
jogador.usar_energia(30)
print(jogador.mostrar_energia())  # Saída: 50
jogador.recuperar_energia(70)
print(jogador.mostrar_energia())  # Saída: 10

class Personagem:
    def __init__(self, nome, vida):
        self.nome = nome
        self.__vida = vida  # atributo privado
    @property
    def vida(self):
        return self.__vida  # getter com @property
heroi = Personagem("Maria", 100)
print(heroi.vida)  # Saída: 100 (acesso como se fosse um atributo público)

class Pontuacao:
    def __init__(self):
        self.__pontos = 0  # atributo privado
    @property
    def pontos(self):
        return self.__pontos  # getter
    @pontos.setter
    def pontos(self, valor):
        if isinstance(valor, int) and valor >= 0:
            self.__pontos = valor
        else:
            print("Valor inválido. Pontos não podem ser negativos.")
p = Pontuacao()
print(p.pontos)  # Saída: 0
p.pontos = 50
print(p.pontos)  # Saída: 50
p.pontos = -10   # Saída: Valor inválido...
print(p.pontos)  # Saída: 50 (valor anterior mantido)

class Jogo:
    def __init__(self, dificuldade):
        self.__dificuldade = 1  # valor padrão
        self.dificuldade = dificuldade  # usa o setter para validação
    @property
    def dificuldade(self):
        return self.__dificuldade  # getter
    @dificuldade.setter
    def dificuldade(self, valor):
        if isinstance(valor, int) and 1 <= valor <= 3:
            self.__dificuldade = valor
        else:
            print("Dificuldade inválida. Escolha um valor entre 1 e 3.")
jogo = Jogo(2)
print(jogo.dificuldade)  # Saída: 2
jogo.dificuldade = 4     # Saída: Dificuldade inválida...
print(jogo.dificuldade)  # Saída: 2 (valor anterior mantido)

class Personagem:
    def __init__(self, nome, vida, defesa):
        self.nome = nome
        self.__vida = vida  # já privado
        self.__defesa = 0   # valor padrão
        self.defesa = defesa  # usa o setter para validação
    @property
    def vida(self):
        return self.__vida
    @property
    def defesa(self):
        return self.__defesa
    @defesa.setter
    def defesa(self, valor):
        if isinstance(valor, int) and 0 <= valor <= 100:
            self.__defesa = valor
        else:
            print("Valor inválido. A defesa deve estar entre 0 e 100.")
p = Personagem("João", 100, 80)
print(p.defesa)  # Saída: 80

p.defesa = 110   # Saída: Valor inválido...
print(p.defesa)  # Saída: 80

class Personagem:
    def __init__(self, nome, vida):
        self.nome = nome
        self.__vida = vida  # valor inicial recebido por parâmetro
        self.__defesa = 0   # valor padrão de defesa
    @property
    def vida(self):
        return self.__vida
    @property
    def defesa(self):
        return self.__defesa
    @defesa.setter
    def defesa(self, valor):
        if isinstance(valor, int) and 0 <= valor <= 100:
            self.__defesa = valor
        else:
            print("Valor inválido. A defesa deve estar entre 0 e 100.")
heroi = Personagem("Maria", 150)
print(heroi.nome)      # Saída: Aragorn
print(heroi.vida)      # Saída: 150
print(heroi.defesa)    # Saída: 0 (valor padrão)
heroi.defesa = 50
print(heroi.defesa)    # Saída: 50

class Inimigo:
    def __init__(self, nome, vida, forca):
        self.nome = nome
        self.__vida = vida  # valor recebido por parâmetro
        self.__forca = forca  # valor recebido por parâmetro
    @property
    def vida(self):
        return self.__vida
    @property
    def forca(self):
        return self.__forca
    def atacar(self):
        print(f"{self.nome} ataca com força {self.__forca}!")
inimigo = Inimigo("Luís", 200, 50)
print(inimigo.nome)      # Saída: Luís
print(inimigo.vida)      # Saída: 200
print(inimigo.forca)     # Saída: 50
inimigo.atacar()         # Saída: Luís ataca com força 50!

class Jogador:
    def __init__(self, nome, energia, pontos):
        self.nome = nome
        self.__energia = max(0, min(energia, 100))  # Garantindo que a energia esteja entre 0 e 100
        self.__pontos = max(0, pontos)  # Garantindo que pontos não sejam negativos
    @property
    def energia(self):
        return self.__energia
    @property
    def pontos(self):
        return self.__pontos
    def usar_energia(self, valor):
        if isinstance(valor, int) and valor > 0:
            self.__energia = max(0, self.__energia - valor)
        else:
            print("Valor inválido. Informe um número inteiro positivo.")
    def recuperar_energia(self, valor):
        if isinstance(valor, int) and valor > 0:
            self.__energia = min(100, self.__energia + valor)
        else:
            print("Valor inválido. Informe um número inteiro positivo.")
    def adicionar_pontos(self, valor):
        if isinstance(valor, int) and valor >= 0:
            self.__pontos += valor
        else:
            print("Valor inválido. Pontos não podem ser negativos.")
jogador = Jogador("Gaby", 80, 50)
print(jogador.nome)      # Saída: Gaby
print(jogador.energia)   # Saída: 80
print(jogador.pontos)    # Saída: 50
jogador.usar_energia(20)
print(jogador.energia)   # Saída: 60
jogador.recuperar_energia(30)
print(jogador.energia)   # Saída: 90
jogador.adicionar_pontos(10)
print(jogador.pontos)    # Saída: 60

class Menu:
    def __init__(self, titulo):
        self.titulo = titulo  # título do menu
        self.exibir_titulo()  # Exibe o título assim que o menu for criado
    def exibir_titulo(self):
        print(f"--- {self.titulo} ---")  # Exibe o título do menu
    def exibir_opcoes(self):
        print("1. Iniciar Jogo")
        print("2. Sair") # Você pode adicionar outras opções aqui
menu = Menu("Menu Principal") # Saída: --- Menu Principal ---
menu.exibir_opcoes() # Saída: # 1. Iniciar Jogo # 2. Sair

class Personagem:
    def __init__(self, nome, vida):
        self.nome = nome
        self.__vida = vida  # valor inicial recebido por parâmetro
    @property
    def vida(self):
        return self.__vida
    def atacar(self):
        print(f"{self.nome} está atacando!")
class NPC(Personagem):
    def __init__(self, nome, vida):
        super().__init__(nome, vida)  # Chama o __init__ da classe base Personagem
    # Sobrescreve o método atacar para não fazer nada, pois NPC não ataca
    def atacar(self):
        print(f"{self.nome} não pode atacar.")  # Comportamento específico para NPCs
# Criando um personagem normal
heroi = Personagem("Gaby", 100)
heroi.atacar()  # Saída: Gaby está atacando!
# Criando um NPC
npc = NPC("Murilo", 50)
npc.atacar()  # Saída: Merlin não pode atacar.

class Inimigo:
    def __init__(self, nome, vida, forca):
        self.nome = nome
        self.__vida = vida  # valor recebido por parâmetro
        self.__forca = forca  # valor recebido por parâmetro
    @property
    def vida(self):
        return self.__vida
    @property
    def forca(self):
        return self.__forca
    def atacar(self):
        print(f"{self.nome} ataca com força {self.__forca}!")
class Chefe(Inimigo):
    def __init__(self, nome, vida, forca):
        super().__init__(nome, vida * 2, forca * 2)  # Chefe tem o dobro de vida e força
chefe = Chefe("Luís supremo", 200, 50)
print(chefe.nome)     # Saída: Luís Supremo
print(chefe.vida)     # Saída: 400 (dobro de vida)
print(chefe.forca)    # Saída: 100 (dobro de força)
chefe.atacar()        # Saída: Luís Supremo ataca com força 100!

class Jogador:
    def __init__(self, nome, energia, pontos):
        self.nome = nome
        self.__energia = max(0, min(energia, 100))  # Garantindo que a energia esteja entre 0 e 100
        self.__pontos = max(0, pontos)  # Garantindo que pontos não sejam negativos
    @property
    def energia(self):
        return self.__energia
    @property
    def pontos(self):
        return self.__pontos
    def usar_energia(self, valor):
        if isinstance(valor, int) and valor > 0:
            self.__energia = max(0, self.__energia - valor)
        else:
            print("Valor inválido. Informe um número inteiro positivo.")
    def recuperar_energia(self, valor):
        if isinstance(valor, int) and valor > 0:
            self.__energia = min(100, self.__energia + valor)
        else:
            print("Valor inválido. Informe um número inteiro positivo.")
    def adicionar_pontos(self, valor):
        if isinstance(valor, int) and valor >= 0:
            self.__pontos += valor
        else:
            print("Valor inválido. Pontos não podem ser negativos.")
class JogadorPremium(Jogador):
    def __init__(self, nome, energia, pontos):
        super().__init__(nome, energia, pontos)  # Inicializa a classe base (Jogador)
    def adicionar_pontos(self, valor):
        bonus = valor * 0.2  # Bônus de 20% a mais para Jogadores Premium
        super().adicionar_pontos(valor + int(bonus))  # Adiciona o valor original + bônus
        print(f"Bônus de {int(bonus)} pontos aplicados! Pontuação total: {self.pontos}")
# Criando um jogador normal
jogador_comum = Jogador("Gaby", 80, 50)
jogador_comum.adicionar_pontos(20)  # Pontuação total: 70
# Criando um jogador premium
jogador_premium = JogadorPremium("Anna", 100, 80)
jogador_premium.adicionar_pontos(20)  # Bônus de 4 pontos aplicados! Pontuação total: 104

class JogoMultiplayer(Jogo):
    def __init__(self, titulo):
        super().__init__(titulo)  # Chama o __init__ da classe base (Jogo)
        self.jogadores = []  # Lista para armazenar os jogadores
    def adicionar_jogador(self, jogador):
        self.jogadores.append(jogador)  # Adiciona um jogador à lista
    def listar_jogadores(self):
        if self.jogadores:
            print("Jogadores no jogo:")
            for jogador in self.jogadores:
                print(f"- {jogador.nome}")
        else:
            print("Nenhum jogador adicionado ainda.")
class Jogador:
    def __init__(self, nome):
        self.nome = nome
# Criando a instância do JogoMultiplayer
jogo_mp = JogoMultiplayer("Super Aventura Multiplayer")
# Criando jogadores
jogador1 = Jogador("Gaby")
jogador2 = Jogador("Anna")
jogador3 = Jogador("Mario")
# Adicionando jogadores ao jogo
jogo_mp.adicionar_jogador(jogador1)
jogo_mp.adicionar_jogador(jogador2)
jogo_mp.adicionar_jogador(jogador3)
# Exibindo os jogadores no jogo
jogo_mp.listar_jogadores()

class Menu:
    def __init__(self, titulo):
        self.titulo = titulo  # Título do menu
        self.exibir_titulo()  # Exibe o título assim que o menu for criado
    def exibir_titulo(self):
        print(f"--- {self.titulo} ---")  # Exibe o título do menu
    def exibir_opcoes(self):
        print("1. Iniciar Jogo")
        print("2. Sair")
        # Você pode adicionar outras opções aqui
import json
class MenuAvancado(Menu):
    def __init__(self, titulo):
        super().__init__(titulo)  # Chama o __init__ da classe base (Menu)
        self.configuracoes = {}  # Dicionário para armazenar as configurações personalizadas
    def exibir_opcoes(self):
        super().exibir_opcoes()  # Exibe as opções do Menu base
        print("3. Salvar Configurações")
        print("4. Carregar Configurações")
    def salvar_configuracoes(self, nome_arquivo="configuracoes.json"):
        """Salva as configurações em um arquivo JSON"""
        try:
            with open(nome_arquivo, 'w') as arquivo:
                json.dump(self.configuracoes, arquivo)
            print("Configurações salvas com sucesso!")
        except Exception as e:
            print(f"Erro ao salvar configurações: {e}")
    def carregar_configuracoes(self, nome_arquivo="configuracoes.json"):
        """Carrega as configurações de um arquivo JSON"""
        try:
            with open(nome_arquivo, 'r') as arquivo:
                self.configuracoes = json.load(arquivo)
            print("Configurações carregadas com sucesso!")
        except FileNotFoundError:
            print("Arquivo de configurações não encontrado.")
        except Exception as e:
            print(f"Erro ao carregar configurações: {e}")
    def alterar_configuracao(self, chave, valor):
        """Altera uma configuração específica"""
        self.configuracoes[chave] = valor
        print(f"Configuração '{chave}' alterada para '{valor}'")
# Criando o Menu Avançado
menu_avancado = MenuAvancado("Menu Avançado")
# Exibindo opções do menu
menu_avancado.exibir_opcoes()
# Alterando e salvando configurações personalizadas
menu_avancado.alterar_configuracao("dificuldade", "média")
menu_avancado.alterar_configuracao("musica", "desligada")
menu_avancado.salvar_configuracoes()
# Carregando configurações salvas
menu_avancado.carregar_configuracoes()
# Exibindo configurações carregadas
print(menu_avancado.configuracoes)

class Arma:
    def __init__(self, nome):
        self.nome = nome  # Nome da arma
    def atacar(self):
        """Método genérico de ataque. Será sobrescrito nas subclasses."""
        raise NotImplementedError("Este método deve ser sobrescrito nas subclasses!")
class Espada(Arma):
    def __init__(self, nome, comprimento):
        super().__init__(nome)  # Chama o __init__ da classe base (Arma)
        self.comprimento = comprimento  # Comprimento da espada em centímetros
    def atacar(self):
        """Ataque específico da espada: corte"""
        print(f"{self.nome} faz um corte rápido com {self.comprimento} cm de lâmina!")
class Arco(Arma):
    def __init__(self, nome, alcance):
        super().__init__(nome)  # Chama o __init__ da classe base (Arma)
        self.alcance = alcance  # Alcance do arco em metros
    def atacar(self):
        """Ataque específico do arco: disparo de flecha"""
        print(f"{self.nome} dispara uma flecha com alcance de {self.alcance} metros!")
class Arma:
    def __init__(self, nome):
        self.nome = nome  # Nome da arma
    def atacar(self):
        """Método genérico de ataque. Será sobrescrito nas subclasses."""
        raise NotImplementedError("Este método deve ser sobrescrito nas subclasses!")
class Espada(Arma):
    def __init__(self, nome, comprimento):
        super().__init__(nome)  # Chama o __init__ da classe base (Arma)
        self.comprimento = comprimento  # Comprimento da espada em centímetros
    def atacar(self):
        """Ataque específico da espada: corte"""
        print(f"{self.nome} faz um corte rápido com {self.comprimento} cm de lâmina!")
class Arco(Arma):
    def __init__(self, nome, alcance):
        super().__init__(nome)  # Chama o __init__ da classe base (Arma)
        self.alcance = alcance  # Alcance do arco em metros
    def atacar(self):
        """Ataque específico do arco: disparo de flecha"""
        print(f"{self.nome} dispara uma flecha com alcance de {self.alcance} metros!")

class Missao:
    def __init__(self, nome, descricao):
        self.nome = nome
        self.descricao = descricao
    def recompensar(self):
        """Método genérico para recompensar. Será sobrescrito nas subclasses."""
        raise NotImplementedError("Este método deve ser sobrescrito nas subclasses!")
class MissaoPrincipal(Missao):
    def __init__(self, nome, descricao, recompensa):
        super().__init__(nome, descricao)
        self.recompensa = recompensa  # Recompensa da missão principal
    def recompensar(self):
        """Recompensa específica da missão principal"""
        print(f"Missão Principal: {self.nome} - {self.descricao}")
        print(f"Recompensa: {self.recompensa} (Recompensa significativa!)")
class MissaoSecundaria(Missao):
    def __init__(self, nome, descricao, recompensa):
        super().__init__(nome, descricao)
        self.recompensa = recompensa  # Recompensa da missão secundária
    def recompensar(self):
        """Recompensa específica da missão secundária"""
        print(f"Missão Secundária: {self.nome} - {self.descricao}")
        print(f"Recompensa: {self.recompensa} (Recompensa menor!)")
# Criando missões principais e secundárias
missao_principal = MissaoPrincipal("Salvar o Reino", "Defender o castelo contra os invasores", "Espada Mágica e 500 de Ouro")
missao_secundaria = MissaoSecundaria("Caçar Animais", "Caçar 10 lobos na floresta", "50 de Ouro")
# Recompensando as missões
missao_principal.recompensar()
missao_secundaria.recompensar()

class Item:
    def __init__(self, nome, descricao):
        self.nome = nome  # Nome do item
        self.descricao = descricao  # Descrição do item
    def usar(self):
        """Método genérico de uso do item. Será sobrescrito nas subclasses."""
        raise NotImplementedError("Este método deve ser sobrescrito nas subclasses!")
class Pocao(Item):
    def __init__(self, nome, descricao, efeito):
        super().__init__(nome, descricao)
        self.efeito = efeito  # Efeito da poção, como cura ou aumento de energia
    def usar(self):
        """Usar a poção, aplicando seu efeito"""
        print(f"Você usou a {self.nome}: {self.descricao}")
        print(f"Efeito: {self.efeito}!")
class Equipamento(Item):
    def __init__(self, nome, descricao, tipo_efeito):
        super().__init__(nome, descricao)
        self.tipo_efeito = tipo_efeito  # Tipo de efeito do equipamento (ex: aumento de defesa)
    def usar(self):
        """Usar o equipamento, aplicando seu efeito"""
        print(f"Você equipou o {self.nome}: {self.descricao}")
        print(f"Efeito: {self.tipo_efeito}!")
# Criando poções e equipamentos
pocao_de_cura = Pocao("Poção de Cura", "Recupera 50 de vida", "Cura 50 pontos de vida")
pocao_de_energia = Pocao("Poção de Energia", "Aumenta a energia em 30", "Aumenta 30 de energia")
espada_magica = Equipamento("Espada Mágica", "Aumenta o ataque em 20", "Aumento de ataque")
escudo_defensivo = Equipamento("Escudo Defensivo", "Aumenta a defesa em 15", "Aumento de defesa")
# Usando os itens
pocao_de_cura.usar()
pocao_de_energia.usar()
espada_magica.usar()
escudo_defensivo.usar()

class Fase:
    def __init__(self, nome, descricao):
        self.nome = nome  # Nome da fase
        self.descricao = descricao  # Descrição da fase
    def entrar(self):
        """Método genérico para entrar em uma fase. Será sobrescrito nas subclasses."""
        raise NotImplementedError("Este método deve ser sobrescrito nas subclasses!")
class FaseFloresta(Fase):
    def __init__(self, nome, descricao, vegetacao, criaturas):
        super().__init__(nome, descricao)
        self.vegetacao = vegetacao  # Tipo de vegetação
        self.criaturas = criaturas  # Tipos de criaturas presentes
    def entrar(self):
        """Entrar na fase floresta"""
        print(f"Você entrou na fase {self.nome}: {self.descricao}")
        print(f"Vegetação predominante: {self.vegetacao}")
        print(f"Cuidado com as criaturas selvagens: {', '.join(self.criaturas)}")

class FaseDeserto(Fase):
    def __init__(self, nome, descricao, temperatura, recursos_agua):
        super().__init__(nome, descricao)
        self.temperatura = temperatura  # Temperatura da fase
        self.recursos_agua = recursos_agua  # Quantidade de água disponível
    def entrar(self):
        """Entrar na fase deserto"""
        print(f"Você entrou na fase {self.nome}: {self.descricao}")
        print(f"Temperatura extrema: {self.temperatura}°C")
        print(f"Recursos de água disponíveis: {self.recursos_agua} litros")
# Criando fases
floresta = FaseFloresta("Floresta Densa", "Uma floresta cheia de árvores altas e escuras", "Vegetação densa", ["Lobo", "Pantera", "Águia"])
deserto = FaseDeserto("Deserto Ardente", "Uma vasta extensão de areia quente e seca", 45, 5)
# Entrando nas fases
floresta.entrar()
print("\n")  # Quebra de linha para separar as fases
deserto.entrar()

class Aliado:
    def __init__(self, nome, tipo):
        self.nome = nome  # Nome do aliado
        self.tipo = tipo  # Tipo de aliado (ex: Mago, Guerreiro)
    def habilidade_especial(self):
        """Método genérico para habilidade especial, será sobrescrito nas subclasses."""
        raise NotImplementedError("Este método deve ser sobrescrito nas subclasses!")
class Mago(Aliado):
    def __init__(self, nome):
        super().__init__(nome, "Mago")  # Define o tipo como "Mago"
    def habilidade_especial(self):
        """Habilidade especial do Mago: Feitiço de Fogo"""
        print(f"{self.nome} conjura um Feitiço de Fogo! Causa dano massivo em área!")
class Guerreiro(Aliado):
    def __init__(self, nome):
        super().__init__(nome, "Guerreiro")  # Define o tipo como "Guerreiro"
    def habilidade_especial(self):
        """Habilidade especial do Guerreiro: Golpe de Espada"""
        print(f"{self.nome} realiza um Golpe de Espada poderoso! Causa dano crítico no inimigo!")
# Criando aliados
mago = Mago("Gandalf")
guerreiro = Guerreiro("Gaby")
# Usando as habilidades especiais
mago.habilidade_especial()
guerreiro.habilidade_especial()

class Veículo:
    def mover(self):
        print("O veículo está se movendo.")

class Bicicleta(Veículo):
    def pedalar(self):
        print("A bicicleta está sendo pedalada.")
    
class Ônibus(Veículo):
    def embancar_passageiros(self):
        print("Os passageiros estão embarcando no Ônibus.")

Veículo = Veículo()
Bicicleta = Bicicleta()
Ônibus = Ônibus()

print("Objeto Veículo:")
Veículo.mover()

print("Objeto Bicicleta:")
Bicicleta.mover()
Bicicleta.pedalar()

print("Objeto Ônibus:")
Ônibus.mover()
Ônibus.embancar_passageiros()
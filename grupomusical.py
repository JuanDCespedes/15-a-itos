import random
from enum import Enum
from datetime import date
from abc import ABC, abstractmethod


# -------------------------
# ENUM TIPO EVENTO
# -------------------------
class TipoEvento(Enum):

    FIESTA_15 = "Fiesta de 15"
    BODA = "Boda"
    CONCIERTO = "Concierto"


# -------------------------
# CLASE ABSTRACTA INSTRUMENTO
# -------------------------
class Instrumento(ABC):

    def __init__(self, nombre):
        self.nombre = nombre

    @abstractmethod
    def afinar(self):
        pass

    @abstractmethod
    def tocar(self):
        pass


# -------------------------
# INSTRUMENTOS
# -------------------------
class Guitarra(Instrumento):

    def __init__(self):
        super().__init__("Guitarra")

    def afinar(self):
        print("Afinando Guitarra (E A D G B E)")

    def tocar(self):
        print("Tocando Guitarra con rasgueo")


class Flauta(Instrumento):

    def __init__(self):
        super().__init__("Flauta")

    def afinar(self):
        print("Ajustando Flauta")

    def tocar(self):
        print("Tocando Flauta soplando")


class Ukelele(Instrumento):

    def __init__(self):
        super().__init__("Ukelele")

    def afinar(self):
        print("Afinando Ukelele (G C E A)")

    def tocar(self):
        print("Tocando Ukelele con rasgueo")


class Piano(Instrumento):

    def __init__(self):
        super().__init__("Piano")

    def afinar(self):
        print("Afinando Piano")

    def tocar(self):
        print("Tocando Piano con teclas")


# -------------------------
# CLASE MUSICO
# -------------------------
class Musico:

    def __init__(self, nombre, instrumento):

        self.nombre = nombre
        self.instrumento = instrumento
        self.asistira = False

    def confirmar_asistencia(self):
        self.asistira = True


# -------------------------
# CLASE EVENTO
# -------------------------
class Evento:

    def __init__(self, tipo, fecha, lugar, asistentes):

        if not (3 <= len(asistentes) <= 15):
            raise ValueError("El evento debe tener entre 3 y 15 músicos")

        self.tipo = tipo
        self.fecha = fecha
        self.lugar = lugar
        self.asistentes = asistentes

    def iniciar_evento(self):

        print("\n============================")
        print("INICIANDO EVENTO")
        print("============================")

        print("Tipo de evento:", self.tipo.value)
        print("Lugar:", self.lugar)
        print("Fecha:", self.fecha)
        print("Músicos asistentes:", len(self.asistentes))

        print("\n--- PRESENTACIÓN ---\n")

        for musico in self.asistentes:

            print("Músico:", musico.nombre)

            musico.instrumento.afinar()
            musico.instrumento.tocar()

            print()


# -------------------------
# PROGRAMA PRINCIPAL
# -------------------------

instrumentos_disponibles = {
    1: Guitarra,
    2: Flauta,
    3: Ukelele,
    4: Piano
}

# Número aleatorio de músicos
cantidad_musicos = random.randint(3, 15)

# Tipo de evento aleatorio
tipo_evento = random.choice(list(TipoEvento))

print("Número de músicos para el evento:", cantidad_musicos)
print("Tipo de evento elegido:", tipo_evento.value)

musicos = []

for i in range(cantidad_musicos):

    print("\n----------------------------")

    nombre = input(f"Nombre del músico {i+1}: ")

    while True:

        print("\nInstrumentos disponibles")
        print("1. Guitarra")
        print("2. Flauta")
        print("3. Ukelele")
        print("4. Piano")

        try:
            opcion = int(input("Seleccione instrumento (1-4): "))
        except:
            print("Ingrese un número válido")
            continue

        if opcion not in instrumentos_disponibles:
            print("Instrumento no válido")
            continue

        instrumento = instrumentos_disponibles[opcion]()
        break

    musico = Musico(nombre, instrumento)
    musico.confirmar_asistencia()

    musicos.append(musico)


# Crear evento
evento = Evento(
    tipo_evento,
    date.today(),
    "Salón principal",
    musicos
)

# Iniciar evento
evento.iniciar_evento()

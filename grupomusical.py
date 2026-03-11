from enum import Enum
from datetime import date
from abc import ABC, abstractmethod
from typing import List

# ---------------------------------------------------------
# Enumeración (Enum)
# ---------------------------------------------------------
class TipoEvento(Enum):
    """
    Representa el tipo de evento.
    Corresponde al <<Enum>> TipoEvento del diagrama.
    """
    FIESTA_15 = "FIESTA_15"
    BODA = "BODA"
    CONCIERTO = "CONCIERTO"

# ---------------------------------------------------------
# Clases de Instrumentos (Herencia y Abstracción)
# ---------------------------------------------------------
class Instrumento(ABC):
    """
    Clase abstracta (indicado por la 'A' y letra cursiva).
    Define la estructura base para cualquier instrumento.
    """
    def __init__(self, nombre: str):
        # Atributo privado indicado por el signo '-'
        self.__nombre = nombre

    @property
    def nombre(self) -> str:
        return self.__nombre

    # Métodos públicos indicados por el signo '+'
    @abstractmethod
    def afinar(self) -> None:
        """Método abstracto para afinar el instrumento."""
        pass

    @abstractmethod
    def tocar(self) -> None:
        """Método abstracto para tocar el instrumento."""
        pass

# Clases concretas que heredan de Instrumento (Relación de Generalización)
class Guitarra(Instrumento):
    def afinar(self) -> None:
        print(f"Afinando la {self.nombre} (cuerdas)...")

    def tocar(self) -> None:
        print(f"Tocando la {self.nombre}...")

class Flauta(Instrumento):
    def afinar(self) -> None:
        print(f"Afinando la {self.nombre} (viento)...")

    def tocar(self) -> None:
        print(f"Tocando la {self.nombre}...")

class Ukelele(Instrumento):
    def afinar(self) -> None:
        print(f"Afinando el {self.nombre} (cuerdas)...")

    def tocar(self) -> None:
        print(f"Tocando el {self.nombre}...")

class Piano(Instrumento):
    def afinar(self) -> None:
        print(f"Afinando el {self.nombre} (teclas/cuerdas)...")

    def tocar(self) -> None:
        print(f"Tocando el {self.nombre}...")

# ---------------------------------------------------------
# Clase Musico
# ---------------------------------------------------------
class Musico:
    """
    Representa a un músico del grupo.
    """
    def __init__(self, nombre: str, instrumentos: List[Instrumento]):
        self.__nombre = nombre
        self.__asistira = False
        
        # Relación "toca": Un músico toca de 1 a muchos (1..*) instrumentos.
        if not instrumentos:
            raise ValueError("Un músico debe tocar al menos un instrumento (1..*)")
        self.__instrumento = instrumentos 

    @property
    def asistira(self) -> bool:
        """Propiedad para acceder al estado de asistencia de forma segura."""
        return self.__asistira

    def confirmarAsistencia(self) -> None:
        """Confirma la asistencia del músico."""
        self.__asistira = True
        print(f"{self.__nombre} ha confirmado su asistencia.")

    def cancelarAsistencia(self) -> None:
        """Cancela la asistencia del músico."""
        self.__asistira = False
        print(f"{self.__nombre} ha cancelado su asistencia.")

# ---------------------------------------------------------
# Clase Evento
# ---------------------------------------------------------
class Evento:
    """
    Representa un evento en el que participa el grupo.
    """
    def __init__(self, tipo: TipoEvento, fecha: date, lugar: str, asistentes: List[Musico]):
        self.__tipo = tipo
        self.__fecha = fecha
        self.__lugar = lugar
        
        # Relación "asistentes": Un evento tiene entre 3 y 15 músicos asistentes (3..15)
        if not (3 <= len(asistentes) <= 15):
            raise ValueError("Un evento debe tener entre 3 y 15 músicos asistentes.")
        self.__asistentes = asistentes

    def iniciarEvento(self) -> None:
        """Inicia el evento musical."""
        print(f"Iniciando el evento de tipo {self.__tipo.value} en {self.__lugar} para la fecha {self.__fecha}.")

# ---------------------------------------------------------
# Clase GrupoMusical
# ---------------------------------------------------------
class GrupoMusical:
    """
    Representa al grupo musical principal.
    """
    def __init__(self, nombre: str, musicos: List[Musico]):
        self.__nombre = nombre
        self.__totalIntegrantes = 15 # Valor por defecto según el diagrama
        
        # Relación "tiene": Un grupo tiene exactamente 15 músicos
        if len(musicos) != 15:
            raise ValueError("El grupo musical debe tener exactamente 15 integrantes.")
        self.__musicos = musicos
        
        # Relación "participa en": Un grupo participa en 0 o muchos eventos (0..*)
        self.__eventos_participados: List[Evento] = []

    def agregar_evento(self, evento: Evento) -> None:
        """Añade un evento a la lista de participaciones del grupo."""
        self.__eventos_participados.append(evento)

    def contarMusicosPresentes(self) -> int:
        """
        Cuenta cuántos músicos de la lista tienen el atributo 'asistira' en True.
        """
        presentes = sum(1 for musico in self.__musicos if musico.asistira)
        return presentes
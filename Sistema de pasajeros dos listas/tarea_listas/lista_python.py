from bisect import bisect_left
from pasajero import Pasajero


class ListaPython:
    """Las mismas operaciones usando los métodos del list de Python."""

    def __init__(self):
        self.pasajeros = []

    def añadir(self, pasajero):                      # ✅ resuelto
        self.pasajeros.append(pasajero)
        return True

    def listar(self):                                 # ✅ resuelto
        if not self.pasajeros:
            print("  (lista vacía)")
            return
        for i, p in enumerate(self.pasajeros):
            print(f"  [{i}] {p}")

    # ---------------- ✍ IMPLEMENTA (tabla 3.2 de la guía) ----------------
    def insertar(self, posicion, pasajero):
        if posicion < 0 or posicion > len(self.pasajeros):
            print("Posición inválida")
            return False

        self.pasajeros.insert(posicion, pasajero)

        return True
    def buscar(self, numero):
        posiciones = [
            i for i, pasajero in enumerate(self.pasajeros)
            if pasajero.numero == numero
        ]

        if posiciones:
            return posiciones[0]

        return -1

    def buscar_binaria(self, numero):
        numeros = [pasajero.numero for pasajero in self.pasajeros]

        posicion = bisect_left(numeros, numero)

        if posicion < len(numeros) and numeros[posicion] == numero:
            return posicion

        return -1

    def modificar(self, numero, nuevo_destino, nuevo_asiento):
        posicion = self.buscar(numero)

        if posicion == -1:
            print("Pasajero no encontrado")
            return False

        self.pasajeros[posicion].destino = nuevo_destino
        self.pasajeros[posicion].asiento = nuevo_asiento

        return True

    def eliminar_por_posicion(self, posicion):
        if posicion < 0 or posicion >= len(self.pasajeros):
            print("Posición inválida")
            return False

        self.pasajeros.pop(posicion)

        return True

    def eliminar_por_valor(self, numero):
        posicion = self.buscar(numero)

        if posicion == -1:
            print("Pasajero no encontrado")
            return False

        self.pasajeros.pop(posicion)

        return True

    def ordenar_asc(self):
        self.pasajeros.sort(key=lambda pasajero: pasajero.numero)

    def ordenar_desc(self):
        self.pasajeros.sort(key=lambda pasajero: pasajero.numero, reverse=True)

    def reversar(self):
        self.pasajeros.reverse()

    def copiar(self):
        nueva_lista = ListaPython()
        nueva_lista.pasajeros = self.pasajeros.copy()
        return nueva_lista

    def longitud(self):
        return len(self.pasajeros)

    def filtrar_por_destino(self, destino):
        resultado = [
            pasajero for pasajero in self.pasajeros
            if pasajero.destino == destino
        ]

        return resultado

    def mayores_de_edad(self):
        resultado = [
            pasajero for pasajero in self.pasajeros
            if pasajero.es_mayor_de_edad()
        ]

        return resultado
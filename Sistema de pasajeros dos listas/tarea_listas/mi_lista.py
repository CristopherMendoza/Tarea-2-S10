from pasajero import Pasajero


class MiLista:
    """Lista construida a mano sobre un arreglo de tamaño fijo.
    datos     -> [p1, p2, p3, None, None, ...]
    capacidad -> total de cajones     cantidad -> cajones ocupados
    ⛔ Sin append, insert, pop, remove, sort, reverse, copy, len, in, slicing.
    """

    def __init__(self, capacidad=10):
        self.datos = [None] * capacidad
        self.capacidad = capacidad
        self.cantidad = 0

    def añadir(self, pasajero):                      # ✅ resuelto
        if self.cantidad == self.capacidad:
            print("  ⚠ La lista está llena")
            return False
        self.datos[self.cantidad] = pasajero          # primer cajón libre
        self.cantidad = self.cantidad + 1
        return True

    def listar(self):                                 # ✅ resuelto
        if self.cantidad == 0:
            print("  (lista vacía)")
            return
        for i in range(self.cantidad):
            print(f"  [{i}] {self.datos[i]}")

    # ---------------- ✍ IMPLEMENTA (tabla 3.1 de la guía) ----------------
    def insertar(self, posicion, pasajero):
        if self.cantidad == self.capacidad:
            print("La lista está llena")
            return False

        if posicion < 0 or posicion > self.cantidad:
            print("Posición inválida")
            return False

        i = self.cantidad

        while i > posicion:
            self.datos[i] = self.datos[i - 1]
            i = i - 1

        self.datos[posicion] = pasajero
        self.cantidad = self.cantidad + 1

        return True

    def buscar(self, numero):
        for i in range(self.cantidad):
            if self.datos[i].numero == numero:
                return i

        return -1

    def buscar_binaria(self, numero):
        inicio = 0
        fin = self.cantidad - 1

        while inicio <= fin:
            medio = (inicio + fin) // 2

            if self.datos[medio].numero == numero:
                return medio

            elif self.datos[medio].numero < numero:
                inicio = medio + 1

            else:
                fin = medio - 1

            return -1

    def modificar(self, numero, nuevo_destino, nuevo_asiento):
        posicion = self.buscar(numero)

        if posicion == -1:
            print("Pasajero no encontrado")
            return False

        self.datos[posicion].destino = nuevo_destino
        self.datos[posicion].asiento = nuevo_asiento

        return True

    def eliminar_por_posicion(self, posicion):
        if posicion < 0 or posicion >= self.cantidad:
            print("Posición inválida")
            return False

        i = posicion

        while i < self.cantidad - 1:
            self.datos[i] = self.datos[i + 1]
            i = i + 1

        self.datos[self.cantidad - 1] = None
        self.cantidad = self.cantidad - 1

        return True

    def eliminar_por_valor(self, numero):
        posicion = self.buscar(numero)

        if posicion == -1:
            print("Pasajero no encontrado")
            return False

        return self.eliminar_por_posicion(posicion)

    def ordenar_asc(self):
        for i in range(self.cantidad - 1):
            for j in range(self.cantidad - 1 - i):
                if self.datos[j].numero > self.datos[j + 1].numero:
                    aux = self.datos[j]
                    self.datos[j] = self.datos[j + 1]
                    self.datos[j + 1] = aux

    def ordenar_desc(self):
        for i in range(self.cantidad - 1):
            for j in range(self.cantidad - 1 - i):
                if self.datos[j].numero < self.datos[j + 1].numero:
                    aux = self.datos[j]
                    self.datos[j] = self.datos[j + 1]
                    self.datos[j + 1] = aux

    def reversar(self):
        inicio = 0
        fin = self.cantidad - 1

        while inicio < fin:
            aux = self.datos[inicio]
            self.datos[inicio] = self.datos[fin]
            self.datos[fin] = aux

            inicio = inicio + 1
            fin = fin - 1

    def copiar(self):
        nueva_lista = MiLista(self.capacidad)

        for i in range(self.cantidad):
            nueva_lista.añadir(self.datos[i])

        return nueva_lista

    def longitud(self):
        return self.cantidad
class NodoTorre:
    def __init__(self, valor, siguiente=None):
        self.valor = valor
        self.siguiente = siguiente

class Torre:
    def __init__(self):
        self.cima = None

    def push(self, valor):
        nuevo_nodo = NodoTorre(valor, self.cima)
        self.cima = nuevo_nodo

    def pop(self):
        if self.cima is not None:
            valor = self.cima.valor
            self.cima = self.cima.siguiente
            return valor
        else:
            return None

    def __str__(self):
        valores = []
        actual = self.cima
        while actual:
            valores.append(actual.valor)
            actual = actual.siguiente
        return str(valores)
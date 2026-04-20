from graphviz import Digraph

# Nodo del árbol
class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izq = None
        self.der = None

# Crear árbol de: 3*(9-3*4)
def crear_arbol():
    raiz = Nodo('*')
    raiz.izq = Nodo('3')

    raiz.der = Nodo('-')
    raiz.der.izq = Nodo('9')

    raiz.der.der = Nodo('*')
    raiz.der.der.izq = Nodo('3')
    raiz.der.der.der = Nodo('4')

    return raiz

# Dibujar árbol con Graphviz
def dibujar(nodo, dot=None):
    if dot is None:
        dot = Digraph()
    
    if nodo:
        dot.node(str(id(nodo)), nodo.valor)

        if nodo.izq:
            dot.edge(str(id(nodo)), str(id(nodo.izq)))
            dibujar(nodo.izq, dot)

        if nodo.der:
            dot.edge(str(id(nodo)), str(id(nodo.der)))
            dibujar(nodo.der, dot)

    return dot

# MAIN
raiz = crear_arbol()
dot = dibujar(raiz)

dot.render('arbol', format='png', view=True)

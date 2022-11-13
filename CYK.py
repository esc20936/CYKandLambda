# Clase arbol para representar el arbol de derivacion
class Tree:
    def __init__(self, label, children=None):
        self.label = label
        self.children = children or []

    def __repr__(self):
        if self.children:
            return '%s(%s)' % (self.label, ', '.join(map(str, self.children)))
        else:
            return self.label

    def __str__(self):
        return self.__repr__()

# Funcion para obtener el arbol de derivacion
# table: tabla CYK
# sentence: lista de palabras
# i: indice de la palabra inicial
# j: indice de la palabra final
# A: variable no terminal inicial
def construct_tree(table, sentence, i, j, A):
    for rule in R[A]:
        if len(rule) == 1:
            if rule[0] == sentence[i]:
                return Tree(A, [Tree(rule[0])])
        else:
            B = rule[0]
            C = rule[1]
            for k in range(i, j):
                if B in table[i][k] and C in table[k+1][j]:
                    return Tree(A, [construct_tree(table, sentence, i, k, B), construct_tree(table, sentence, k+1, j, C)])
    return None

# Lista de variables no terminales
non_terminals = ["S","VP", "PP", "NP", "V","P", "N", "Det"]
# Lista de variables terminales
terminals = ["cooks", "drinks", "eats","cuts",
			"he", "she",
			"in", "with",
            "cat","dog",
            "beer","cake","juice","meat","soup",
            "fork","knife","spoon","oven",
            "the","a"]
# diccionario de reglas
R = {
    "S": [["NP", "VP"]],
    "VP": [["VP", "PP"],["V", "NP"],["cooks"], ["drinks"], ["eats"], ["cuts"]],
    "PP": [["P", "NP"]],
    "NP": [["Det", "N"],["he"], ["she"]],
    "V" : [["cooks"], ["drinks"], ["eats"], ["cuts"]],
    "P" : [["in"], ["with"]],
    "N": [["cat"], ["dog"],["beer"], ["cake"], ["juice"], ["meat"], ["soup"],["fork"], ["knife"], ["spoon"], ["oven"]],
    "Det": [["a"], ["the"]]
	}

# Funcion para obtener la tabla CYK
# Recibe una lista de palabras
# Devuelve una tabla CYK
# la manera en la que funciona es la siguiente:
# se recorre la tabla de izquierda a derecha y de arriba hacia abajo
# en cada celda se revisa si la palabra en esa posicion es una variable terminal
# si lo es, se agrega a la lista de variables en esa celda
# si no lo es, se revisa si la celda es una union de dos variables no terminales
# si lo es, se agrega a la lista de variables en esa celda
# se repite el proceso hasta que se recorre toda la tabla
# se devuelve la tabla
def CYK(sentence):
    n = len(sentence)
    table = [[[] for i in range(n)] for j in range(n)]
    for i in range(n):
        for A in non_terminals:
            for rule in R[A]:
                if sentence[i] in rule:
                    table[i][i].append(A)
    for l in range(1, n):
        for i in range(n-l):
            j = i + l
            for k in range(i, j):
                for A in non_terminals:
                    for rule in R[A]:
                        if len(rule) == 2:
                            B = rule[0]
                            C = rule[1]
                            if B in table[i][k] and C in table[k+1][j]:
                                table[i][j].append(A)
    return table


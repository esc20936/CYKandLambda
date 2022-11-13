import CYK

def test(oracion):
    w = oracion.split()
    table = CYK.CYK(w)
    if "S" in table[0][len(w)-1]:
        print("Accepted")
    else:
        print("Not Accepted")


    tree = CYK.construct_tree(table, w, 0, len(w)-1, "S")
    print(tree)

# Oraciones con resultados correctos
sentences = ["he cuts the cake with a knife",
            "she drinks the soup with a fork",
            "she eats a cake with a fork",
            "the cat drinks the beer"]


# Oraciones con resultados incorrectos
sentences2 =["he plays soccer",
            "she laughs",
            "the cat loves the dog"]


for sentence in sentences:
    test(sentence)
    print("")
print("\nCASOS INCORRECTOS\n")
for sentence in sentences2:
    test(sentence)
    print("")
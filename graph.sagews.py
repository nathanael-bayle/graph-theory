def evaluation( formule ):
    i = 0
    res = 0
    for clause in formule:
        if valeurs.get(clause[0])==None:
            valeurs[clause[0]] = int(not(valeurs.get(clause[0][1:])))
        if valeurs.get(clause[1])==None:
            valeurs[clause[1]] = int(not(valeurs.get(clause[1][1:])))
        formule[i][0] = valeurs.get(clause[0])
        formule[i][1] = valeurs.get(clause[1])
        formule[i] = clause[0] or clause[1]
        i += 1

    for index in range(0,len(formule)-1):
        res = formule[index] and formule[index+1]
    return res

def graphe_oriente( formule ):
    aretes = []
    graphe = DiGraph()
    for clause in formule:
        aretes.append(["!" + clause[0], clause[1]])
        aretes.append(["!" + clause[1], clause[0]])
    for arete in aretes:
        if arete[0][:2]=="!!":
            arete[0] = arete[0][2:]
        if arete[1][:2]=="!!":
            arete[1] = arete[1][2:]
    graphe.add_edges(aretes)
    return graphe

def pp( graphe ):
    for noeud in graphe:
        visite[noeud] = "blanc"
    for noeud in graphe:
        if visite[noeud] == "blanc":
            visiterpp( noeud )

def visiterpp( noeud ):
    visite[noeud] = "gris"
    if len(graphe.outgoing_edges([noeud])) > 0:
        for v in graphe.outgoing_edges([noeud]):
            if visite[v[1]] == "blanc":
                visite[v[1]] = "gris"
                visiterpp(v[1])
    visite[noeud] = "noir"
    etape.append(noeud)

def reverse( graphe ):
    D = DiGraph()
    for v in graphe.edges():
        D.add_edge(v[1],v[0])
    return D

def trajan( graphe ):
    visite = {}
    etape = []
    pp( graphe )
    etape.reverse()
    graphe = reverse( graphe)
    return graphe
valeurs = {'x1': 1, 'x2': 0, 'x3': 0}
formule = [['x1','!x2'],['!x1','x2'],['!x1','!x2'],['x1','!x3']]


G = graphe_oriente( formule )

trajan( G )
#G.show()

#print formule
#print evaluation( formule )

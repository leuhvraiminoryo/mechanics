class Tree:
    def __init__(self, value, nodes=[]):
        ''' constructeur'''
        self.value = value
        self.nodes = nodes


    def add_node(self, value):
        self.nodes.append(value)
    
    def taille(self):
        ''' retourne la taille de l'arbre avec méthode récursive'''
        TailleG = 0
        TailleD = 0
        if self.left is not None :
                TailleG = self.left.taille()
        if self.right is not None :
                TailleD = self.right.taille()
        return 1 + TailleG + TailleD

    def hauteur(self):
        ''' retourne la hauteur de l'arbre avec méthode récursive'''
        HauteurG = 0
        HauteurD = 0
        if self.nodes != []:
            for arbre in self.nodes:
                pass
        if self.right != None :
                HauteurD = self.right.hauteur()
        return 1 + max( HauteurG , HauteurD)
    
    def est_feuille(self):
        ''' retourne booléen si le noeud (sous arbre) est une feuille'''
        return self.nodes == []

    def compte_feuilles(self):
        ''' Retourne le nombre de feuilles'''
        cpt = 0
        if self.est_feuille():
            return 1
        if self.nodes != []:
            for arbre in self.nodes:
                cpt += arbre.compte_feuilles()
        return cpt

salle0 = Tree(0)
salle1 = Tree(0)
salle2 = Tree(0)
salle3 = Tree(0)
salle4 = Tree(0)
salle5 = Tree(2,[salle1,salle2])
salle6 = Tree(6,[salle5,salle3,salle4,salle0])
print(salle6.compte_feuilles())

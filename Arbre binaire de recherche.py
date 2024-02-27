from binarytree import Node  # librairie pour la méthode "graphique"
from random import shuffle  # fonction de mélange des listes

class Noeud:
    def __init__(self, valeur=None):
        """initialisation du noeud"""
        self.valeur = valeur
        self.gauche = None
        self.droit = None
        
    def graphique(self):
        """affichage du noeud et de l'arbre des descendants par binarytree
        avec un joli affichage pour __str__"""
        def ajout_noeud(noeud):
            n = Node(noeud.valeur)
            if noeud.a_un_fils_gauche():
                n.left = ajout_noeud(noeud.gauche)
            if noeud.a_un_fils_droit():
                n.right = ajout_noeud(noeud.droit)
            return n
        
        return ajout_noeud(self)
        
    def __str__(self):
        """affichage du noeud"""
        return f"{self.graphique()}"
    
    __repr__ = __str__  # affichage identique par __repr__
    
    def a_un_fils_gauche(self):
        """renvoie True si le noeud a un fils gauche"""
        return self.gauche is not None
    
    def a_un_fils_droit(self):
        """renvoie True si le noeud a un fils droit"""
        return self.droit is not None
    
    def est_une_feuille(self):
        """renvoie True si le noeud est une feuille"""
        return not self.a_un_fils_gauche() and not self.a_un_fils_droit()
        
    def inserer(self, val):
        """insère par appel récursif, la valeur au bon endroit"""    
        if self.valeur == None or self.valeur == val:  # rien dans le noeud ou doublon
            self.valeur = val
            return  # travail terminé
        if val > self.valeur:  # si val est trop grande
            if self.a_un_fils_droit() :  # si le noeud a un fils à droite
                self.droit.inserer(val) 
            else :# le noeud n'a pas de fils à droite
                 self.droit = Noeud(val)
        if self.valeur > val :  # si val est trop petite
            if self.a_un_fils_gauche() :  # si le noeud a un fils à gauche
                self.gauche.inserer(val)
            else:  # le noeud n'a pas de fils à gauche
                self.gauche = Noeud(val)
                
    def recherche(self, val):
        """fonction de recherche qui renvoie True si l'élément est trouvé et False sinon"""
        if val == self.valeur:
            return True
        elif self.valeur == None:
            return False
        elif val > self.valeur: 
            if self.a_un_fils_droit():
                return self.droit.recherche(val)
            else:
                return False
        else:
            if self.a_un_fils_gauche():
                return self.gauche.recherche(val)
            

racine = Noeud()

liste = [12,23,13,55,61,58,39]
shuffle(liste)  # mélangeons la liste pour créer un meilleur arbre...

# inserons les valeurs de la liste
for e in liste:
    racine.inserer(e)
    
print(racine)

# Tests de la recherche
# assert ...
assert racine.recherche(12) == True
assert racine.recherche(9) == False
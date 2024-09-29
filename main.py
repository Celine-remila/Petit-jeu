import random

class Jeu:
    """
    La Classe représentative du jeu.

    Attributs:
        m (int): Le nombre m reçois en paramètre.
        k (int): Un nombre tiré au hasard entre 0 et m.
        n (int): Le nombre maximum d'essais qu'on a à faire.
    Example:
        >>> j = Jeu(10, 4)
        >>> 0 <= j.k <= 10
        True
    """

    def __init__(self, m, n):
        """
        Constructeur de la classe Jeu.

        Arguments:
            m (int): Le nombre pour le tirage aléatoire.
            n (int): Le nombre maximum d'essais qu'on a à faire.
   
        Examples:
            >>> j = Jeu(10,4)
            >>> j.n
            4
        """
        self.m = m
        self.k = random.randint(0, m)
        self.n = n 
        
        
    def test(self, k):
        """
        Comparer le nombre k avec le nombre donné m à deviner.

        Arguments:
            k (int): Le nombre proposé par le joueur.

        Returns:
            bool: True si le joueur a gagné, False sinon.
  
        Examples:
            >>> j = Jeu(10, 4)
            >>> j.test(j.k)  #On doit gagner si on propose le bon nombre
            Bravo, tu as gagné !
            True 
        """

        if k < self.k:
            print("Trop petit !")
            self.n -=1 #Pour décrémenter le nombre d'essais
            return False
        elif k > self.k:
            print("Trop grand !")
            self.n -=1 #Pour décrémenter le nombre d'essais
            return False
        else:
            print("Bravo, tu as gagné !")
            return True
            

    def jouer(self):
        while self.n > 0:
            try:
                k = int(input("Entre un nombre : "))
                if self.test(k):
                    print("Bravo, tu as gagné !")
                    break
            except ValueError:
                print("Ceci n’est pas un entier !")
        else:
            print("Tu as perdu !")
            
            

if __name__ == '__main__':
    import doctest
    doctest.testmod()

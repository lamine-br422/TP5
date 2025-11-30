#!/usr/bin/env python
# -*- coding: utf-8 -*-

from abc import ABC, abstractmethod

class Compte(ABC):
    @abstractmethod
    def stock(self):
        pass

    @abstractmethod
    def achat(self):
        pass

    @abstractmethod
    def commande(self):
        pass


class Vendeur(Compte):
    def stock(self):
        print("Vendeur: consultation du stock")

    def achat(self):
        print("Vendeur: effectue un achat")

    def commande(self):
        print("Vendeur: enregistre une commande")


class Visiteur(Compte):
    def stock(self):
        print("Visiteur: visualise le stock")

    def achat(self):
        print("Visiteur: effectue un achat")

    def commande(self):
        print("Visiteur: passe une commande")


class Gestionnaire(Compte):
    def stock(self):
        print("Gestionnaire: gère le stock")

    def achat(self):
        print("Gestionnaire: valide un achat")

    def commande(self):
        print("Gestionnaire: gère les commandes")


class CompteFactory(ABC):
    @abstractmethod
    def createCompte(self, type_compte):
        pass


class ConcreteCompteFactory(CompteFactory):
    def createCompte(self, type_compte):
        if type_compte == "vendeur":
            return Vendeur()
        elif type_compte == "visiteur":
            return Visiteur()
        elif type_compte == "gestionnaire":
            return Gestionnaire()
        else:
            raise ValueError("Type de compte inconnu: " + type_compte)


if __name__ == "__main__":
    factory = ConcreteCompteFactory()
    for t in ("gestionnaire", "vendeur", "visiteur"):
        compte = factory.createCompte(t)
        compte.stock()
        compte.achat()
        compte.commande()

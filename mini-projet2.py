#définition des fonctions
def afficher_menu():
    print("--------------------------------------------------------------------------------")
    print("(1) entrer/modifier informations")
    print("(2) calculs du besoin en calorie et en nutriments")
    print("(3) afficher les aliments disponibles")
    print("(4) Ajouter un aliment à ma journée")
    print("(5) Afficher mon bilan de la journée")
    print("(6) Simuler la progression (poids)")
    print("--------------------------------------------------------------------------------")
  
#déclaration des variables 
informations = {}
aliments_du_jour = []
programme = True

#liste des aliments disponibles
aliments = [
    {'aliment': 'Poulet grillé', 'calories': 165, 'protéines': 31, 'glucides': 0, 'lipides': 3.6},
    {'aliment': 'Saumon', 'calories': 206, 'protéines': 22, 'glucides': 0, 'lipides': 13},
    {'aliment': 'Quinoa', 'calories': 120, 'protéines': 4.1, 'glucides': 21, 'lipides': 1.9},
    {'aliment': 'Riz brun', 'calories': 111, 'protéines': 2.6, 'glucides': 23, 'lipides': 0.9},
    {'aliment': 'Pâtes', 'calories': 131, 'protéines': 5, 'glucides': 25, 'lipides': 1.1},
    {'aliment': 'Brocoli', 'calories': 55, 'protéines': 3.7, 'glucides': 11, 'lipides': 0.6},
    {'aliment': 'Oeuf', 'calories': 155, 'protéines': 13, 'glucides': 1.1, 'lipides': 11},
    {'aliment': 'Amandes', 'calories': 576, 'protéines': 21, 'glucides': 22, 'lipides': 49},
    {'aliment': 'Banane', 'calories': 89, 'protéines': 1.1, 'glucides': 23, 'lipides': 0.3},
    {'aliment': 'Pomme', 'calories': 52, 'protéines': 0.3, 'glucides': 14, 'lipides': 0.2},
    {'aliment': 'Yaourt nature', 'calories': 59, 'protéines': 10, 'glucides': 3.6, 'lipides': 0.4},
    {'aliment': 'Fromage', 'calories': 402, 'protéines': 25, 'glucides': 1.3, 'lipides': 33},
    {'aliment': 'Pain complet', 'calories': 69, 'protéines': 3.6, 'glucides': 12, 'lipides': 1.1},
    {'aliment': 'Tomate', 'calories': 18, 'protéines': 0.9, 'glucides': 3.9, 'lipides': 0.2},
    {'aliment': 'Carotte', 'calories': 41, 'protéines': 0.9, 'glucides': 10, 'lipides': 0.2},
    {'aliment': 'Epinard', 'calories': 23, 'protéines': 2.9, 'glucides': 3.6, 'lipides': 0.4},
    {'aliment': 'Avocat', 'calories': 160, 'protéines': 2, 'glucides': 9, 'lipides': 15},
    {'aliment': 'Chocolat noir', 'calories': 546, 'protéines': 4.9, 'glucides': 61, 'lipides': 31},
    {'aliment': 'Miel', 'calories': 304, 'protéines': 0.3, 'glucides': 82, 'lipides': 0},
    {'aliment': 'Poivron', 'calories': 20, 'protéines': 0.9, 'glucides': 4.7, 'lipides': 0.2},
    {'aliment': 'Haricot rouge', 'calories': 127, 'protéines': 8.7, 'glucides': 22.8, 'lipides': 0.5},
    {'aliment': 'Pêche', 'calories': 39, 'protéines': 0.9, 'glucides': 10, 'lipides': 0.3},
    {'aliment': 'Poire', 'calories': 57, 'protéines': 0.4, 'glucides': 15, 'lipides': 0.1},
    {'aliment': 'Sardine', 'calories': 208, 'protéines': 25, 'glucides': 0, 'lipides': 11},
    {'aliment': 'Céréales', 'calories': 100, 'protéines': 3, 'glucides': 21, 'lipides': 1},
    {'aliment': 'Lait', 'calories': 42, 'protéines': 3.4, 'glucides': 5, 'lipides': 1},
    {'aliment': 'Cacahuète', 'calories': 567, 'protéines': 25.8, 'glucides': 16.1, 'lipides': 49.2},
    {'aliment': 'Gingembre', 'calories': 80, 'protéines': 1.8, 'glucides': 18, 'lipides': 0.4},
    {'aliment': 'Kiwi', 'calories': 61, 'protéines': 1.1, 'glucides': 15, 'lipides': 0.5},
    {'aliment': 'Pâté', 'calories': 330, 'protéines': 20, 'glucides': 2, 'lipides': 28},
]


#programme principal

while programme:
    afficher_menu()
    choix = int(input("votre choix : "))
    
    match choix:
        case 1:
            #recolte des informations de l'utilisateur
            pass
        case 2:
            #calculer les beosin en calories et nutriments selon les objectifs
            pass
        case 3:
            #afficher les aliements
            pass
        case 4:
            #ajouter un(des) aliments à ma journée
            pass
        case 5:
            #afficher le bilan du jours
            pass
        case 6:
            #simuler la progression du poids
            pass
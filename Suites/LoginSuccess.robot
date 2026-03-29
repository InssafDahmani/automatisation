*** Settings ***
Resource         ../Conf/ImportRessource.robot
Suite Setup      Ouvrir Navigateur
Suite Teardown   Fermer Navigateur
Test Teardown   Capturer Screenshot En Cas D Echec

*** Test Cases ***
Login Success And Product Management
    [Documentation]    Login with valid credentials, add Sauce Labs Bike Light to cart and remove it

    # Étape 1 : Se connecter avec identifiants corrects
    Login    standard_user    secret_sauce

    # Étape 2 : Vérifier qu'on est sur la page produits
    Verify Inventory Page

    # Étape 3 : Récupérer et afficher prix et description du produit
    Get Bike Light Info

    # Étape 4 : Ajouter le produit au panier
    Add Bike Light To Cart

    # Étape 5 : Cliquer sur le panier
    View Cart

    # Étape 6 : Vérifier qu'on est sur la page panier
    Verify Cart Page

    # Étape 7 : Vérifier que le produit est dans le panier
    Verify Product In Cart    Sauce Labs Bike Light

    # Étape 8 : Cliquer sur Remove
    Click Remove

    # Étape 9 : Vérifier que le produit a disparu
    Verify Product Not In Cart    Sauce Labs Bike Light
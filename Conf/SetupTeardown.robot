*** Settings ***
Library    SeleniumLibrary

*** Keywords ***
#the keyword that i'm gonna reuse 
Ouvrir Navigateur 
#keywords built-in or Step / Action
    Open Browser    https://www.saucedemo.com/    chrome
    Maximize Browser Window

Fermer Navigateur
    Close Browser

Capturer Screenshot En Cas D Echec
    Run Keyword If Test Failed    Capture Page Screenshot
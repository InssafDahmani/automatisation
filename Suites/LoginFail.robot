*** Settings ***
Resource         ../Conf/ImportRessource.robot
Suite Setup      Ouvrir Navigateur
Suite Teardown   Fermer Navigateur
Test Teardown   Capturer Screenshot En Cas D Echec
*** Test Cases ***
Login with invalid credentials
    [Documentation]    This test case verifies that a user cannot login
    ${invalid_user}=    Set Variable    standard_user
    ${invalid_pass}=    Set Variable    123456
    Input Invalid Credentials    ${invalid_user}    ${invalid_pass}
    Verify Login Failed Message






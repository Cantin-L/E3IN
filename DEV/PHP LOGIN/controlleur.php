<?php

require_once('compte.php');
require_once('compteDAO.php');


$identifiant = $_POST['identifiant'];
$mot_passe = $_POST['mot_passe'];

//Création de l'objet CompteDAO pour effectuer les opérations de base de données.
$compteDAO = new CompteDAO();

//Recherche du compte dans la base de données à partir des identifiants et mots de passe fournis
$compte = $compteDAO->existe($identifiant, $mot_passe);

//Test si compte existe 
if ($compte) {
    //redirection vers la page accueil
    header('Location: accueil.php');
} else {
    //création d'un nouveau compte en utilisant les identifiant et mots de passe fourni
    $compte = new Compte($identifiant, $mot_passe);
    //insertion du nouveau compte dans la base de données
    $compteDAO->ajout($compte);
    //redirection vers la page login pour une nouvelle connection
    header('Location: login.php');
}

?>


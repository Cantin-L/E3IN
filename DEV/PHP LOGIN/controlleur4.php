<?php

require_once('compte.php');
require_once('compteDAO.php');

$compteDAO = new CompteDAO();

$identifiant = $_POST['identifiant'];
$mot_passe = $_POST['mot_passe'];
$id = $_POST['id'];

$compteDAO->modif($identifiant,$mot_passe,$id);


//redirection vers la page accueil
header('Location: accueil.php');
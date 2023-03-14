<?php

require_once('compte.php');
require_once('compteDAO.php');

$compteDAO = new CompteDAO();

$id = $_GET['id'];

$compteDAO->suppr($id);

echo ($id);
//redirection vers la page accueil
header('Location: accueil.php');





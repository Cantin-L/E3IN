<?php
require_once('compte.php');
require_once('compteDAO.php');

$compteDAO = new CompteDAO();

$id = $_GET['id'];

$compte = $compteDAO->listingID($id);

$ident = $compte['identifiant'];
$pass = $compte['mot_passe'];
?>

<html>
<head>
    <title>Page de Modification</title>
    <style>
      table, th, td {
        border: 1px solid black;
        border-collapse: collapse;
      }
      th, td {
        padding: 5px;
        text-align: center;
      }
    </style>
</head>
<body>
    <center>
    <h1 style="padding-top : 6em">Modification</h1>
    <form action="controlleur4.php" method="POST">
        <!--création du champ pour l'identifiant-->
        <input type="hidden" id="id" name="id" value="<?php echo($id)?>" required>
        <label for="identifiant"> Identifiant </label>
        <!--récupération du contenu dans la variable identifiant-->
        <input type="text" id="identifiant" name="identifiant" value="<?php echo($ident)?>" required>
        <br>
        <br>
        <!--création du champ pour le mot de passe-->
        <label for="mot_passe"> Mot de passe </label>
        <!--récupération du contenu dans la variable mot de passe-->
        <input type="text" id="mot_passe" name="mot_passe" value="<?php echo($pass)?>" required>
        <br>
        <br>
        <!--création du boutton pour se connecter-->
        <input type="submit" value="Modifier">
    </form>
</body>
</html>
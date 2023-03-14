<?php
require_once('compte.php');
require_once('compteDAO.php');
if (isset($_GET["afaire"]) && $_GET["afaire"] === "deconnexion") {
    header("Location: login.php");
    exit();
}

if (isset($_GET["afaire"]) && $_GET["afaire"] === "creation") {
    header("Location: CreationCompte.php");
    exit();
}
$compteDAO = new CompteDAO();

?>

<html>
<head>
    <title>Page d'accueil</title>
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
    <h1 style="padding-top : 6em">Liste des comptes</h1>
    <br>
    <table>
        <thead>
            <tr>
                <th>Identifiant</th>
                <th>Mot de passe</th>
                <th>Suppression</th>
                <th>Modification</th>
            </tr>
        </thead>
        <tbody>
            <?php
            //Connexion à la base de données
            $db = new SQLite3('Compte.db');
            //Récupération de la liste des comptes
            $result = $compteDAO->listing();
            //boucle pour afficher la liste des comptes 
            foreach ($result as $row){                
                echo "<tr>";
                echo "<td>" . $row['identifiant'] . "</td>";
                $id = $row['id'];
                echo "<td>" . $row['mot_passe'] . "</td>";
                echo "<td><a href='suppr.php?id=$id'>Supprimer</a></td>";
                echo "<td><a href='modif.php?id=$id'>Modifier</a></td>";
                echo "</tr>";
            }
            ?>
        </tbody>
    </table>
    <br>
    <br>
    <!--Boutton de deconnexion-->
    <a href="accueil.php?afaire=deconnexion">Deconnexion</a>
    <br>
    <br>
    <!--Boutton pour ajouter un compte-->
    <a href="accueil.php?afaire=creation">Ajouter un compte</a>
    </center>   
</body>
</html>

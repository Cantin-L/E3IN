<html>
<head>
    <title>Page de Connexion</title>
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
    <h1 style="padding-top : 6em">Connexion</h1>
    <form action="controlleur.php" method="post">
        <!--création du champ pour l'identifiant-->
        <label for="identifiant">Identifiant </label>
        <!--récupération du contenu dans la variable identifiant-->
        <input type="text" id="identifiant" name="identifiant" required>
        <br>
        <br>
        <!--création du champ pour le mot de passe-->
        <label for="mot_passe">Mot de passe </label>
        <!--récupération du contenu dans la variable mot de passe-->
        <input type="password" id="mot_passe" name="mot_passe" required>
        <br>
        <br>
        <!--création du boutton pour se connecter-->
        <input type="submit" value="Se connecter">
    </form>
</body>
</html>

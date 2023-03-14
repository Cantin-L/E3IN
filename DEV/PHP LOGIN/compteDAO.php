<?php

require_once('compte.php');

//création de la classe CompteDAO
class CompteDAO {

    //initialisation de l'attribut db pour la connexion à la base de données 
    private $db;

    //Constructeur de la classe CompteDAO
    public function __construct() {
        $this->db = new PDO('sqlite:compte.db');
    }

    //Methode pour trouver un compte avec un identifiant et un mot de passe saisie 
    public function listing() {
        //requete sql de la recherche 
        $stmt = $this->db->prepare('SELECT * FROM Compte');
        $stmt->execute();
        return $stmt->fetchAll();
    }

    //Methode pour trouver un compte avec un identifiant et un mot de passe saisie 
    public function listingID($id) {
        //requete sql de la recherche 
        $stmt = $this->db->prepare('SELECT * FROM Compte WHERE id = :id');
        $stmt->bindParam(':id', $id);
        $stmt->execute();
        return $stmt->fetch();
    }

    //Methode pour trouver un compte avec un identifiant et un mot de passe saisie 
    public function modif($identifiant, $mot_passe, $id) {
        //requete sql de la recherche 
        $stmt = $this->db->prepare('UPDATE Compte SET identifiant = :identifiant, mot_passe = :mot_passe WHERE id = :id');
        $stmt->bindParam(':identifiant', $identifiant);
        $stmt->bindParam(':mot_passe', $mot_passe);
        $stmt->bindParam(':id', $id);
        $stmt->execute();

        return $stmt->fetch();
    }    

    //Methode pour trouver un compte avec un identifiant et un mot de passe saisie 
    public function existe($identifiant, $mot_passe) {
        //requete sql de la recherche 
        $stmt = $this->db->prepare('SELECT * FROM Compte WHERE identifiant = :identifiant AND mot_passe = :mot_passe');
        $stmt->bindParam(':identifiant', $identifiant);
        $stmt->bindParam(':mot_passe', $mot_passe);
        $stmt->execute();

        return $stmt->fetch();
    }

    //Methode pour ajouter un compte dans la base de données 
    public function ajout(Compte $compte) {
        //requete pour ajouter l'identifiant et le mot de passe du nouveau compte dans la base de donées
        $stmt = $this->db->prepare('INSERT INTO Compte (identifiant, mot_passe) VALUES (:identifiant, :mot_passe)');
        $stmt->bindParam(':identifiant', $compte->getIdentifiant());
        $stmt->bindParam(':mot_passe', $compte->getMotPasse());
        $stmt->execute();
    }

    //Methode pour supprimer un compte
    public function suppr($id) {
        //requet pour supprimer le compte affilier à l'id donné
        $stmt = $this->db->prepare('DELETE FROM Compte WHERE id = :id');
        $stmt->bindParam(':id', $id);
        $stmt->execute();
    }
}

?>

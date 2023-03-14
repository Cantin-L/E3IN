<?php

//création de la classe Compte
class Compte {

    //initialisation des attributs identifiant et mot_passe
    private $identifiant;
    private $mot_passe;

    //Constructeur de la classe Compte 
    public function __construct($identifiant, $mot_passe) {
        $this->identifiant = $identifiant;
        $this->mot_passe = $mot_passe;
    }

    //fonction getter et setter
    public function getIdentifiant() {
        return $this->identifiant;
    }
    public function setIdentifiant($identifiant) {
        $this->identifiant = $identifiant;
    }
    public function getMotPasse() {
        return $this->mot_passe;
    }
    public function setMotPasse($mot_passe) {
        $this->mot_passe = $mot_passe;
    }

}

?>


## Introduction
Un **générateur de mots de passe complexes** qui prend en compte, selon le choix de l'utilisateur, les lettres majuscules, minuscules, les chiffres et les caractères spéciaux.</br></br>

##  Langages de programmation
- L'application a été développée en *Python* via *Django* avec frontEnd *HTML/CSS/JQuery*</br></br>


## Captures d'écran
<img src="https://raw.githubusercontent.com/umut-dag/Projet07-Django-Generateur-de-mots-de-passe/main/screenshots/2021-09-04_042436.jpg" alt="Capture d'écran"/>

<img src="https://raw.githubusercontent.com/umut-dag/Projet07-Django-Generateur-de-mots-de-passe/main/screenshots/2021-09-04_042449.jpg" alt="Capture d'écran"/>

<img src="https://raw.githubusercontent.com/umut-dag/Projet07-Django-Generateur-de-mots-de-passe/main/screenshots/2021-09-04_042727.jpg" alt="Capture d'écran"/>

</br>

## Les règles à respecter pour créer un bon mot de passe

#### Règle n°1 : 12 caractères
> Un mot de passe sécurisé doit comporter au moins 12 caractères. Il peut être éventuellement plus court si le compte propose des sécurités complémentaires comme le verrouillage du compte après plusieurs échecs, un test de reconnaissance de caractères ou d’images (« captcha »), la nécessité d’entrer des informations complémentaires communiquées par un autre moyen qu’internet (exemple : un identifiant administratif envoyé par La Poste), etc.

#### Règle n°2 : des chiffres, des lettres, des caractères spéciaux
> Votre mot de passe doit se composer de 4 types de caractères différents : majuscules, minuscules, chiffres, et signes de ponctuation ou caractères spéciaux (€, #...).

#### Règle n°3 : un mot de passe anonyme
> Votre mot de passe doit être anonyme : il est très risqué d’utiliser un mot de passe avec votre date de naissance, le nom de votre chien etc., car il serait facilement devinable.

#### Règle n°4 : la double authentification
> Certains sites proposent de vous informer par mail ou par téléphone si quelqu’un se connecte à votre compte depuis un terminal nouveau. Vous pouvez ainsi accepter ou refuser la connexion. N'hésitez pas à utiliser cette option.

#### Règle n°5 : renouvellement des mots de passe
> Sur les sites où vous avez stocké des données sensibles, pensez à changer votre mot de passe régulièrement : tous les 3 mois parait être une fréquence raisonnable.


---


# Installation

#### Cloner le projet :
```
git clone https://github.com/umut-dag/Projet07-Django-Generateur-de-mots-de-passe.git
```

#### Il est conseillé de travailler dans un environnement virtuel :
```
python -m venv venv
.\venv\Scripts\activate
```

#### Installation des dépendances :
```
pip install -r requirements.txt
```

#### Création des tables dans la base de données :
```
python manage.py migrate
```

#### Lancement du serveur :
```
python manage.py runserver
```

# Emulation

#### Entrer l'adresse suivante dans la barre d'adresse de votre navigateur Web :
```
http://localhost:8000/
```

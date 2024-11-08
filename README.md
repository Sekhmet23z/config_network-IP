Network Setup Tool

Ce script est conçu pour calculer les informations réseau essentielles en fonction du nombre d'hôtes souhaité. Il détermine l'adresse réseau, les IP utilisables, l'adresse de diffusion (broadcast), et le masque de sous-réseau.

Fonctionnalités

Détection de classe : sélection automatique des classes de réseau A, B ou C en fonction du nombre d'hôtes.
Calcul du masque de sous-réseau : ajustement dynamique pour adapter le réseau au nombre d'hôtes.
Affichage des adresses : première et dernière IP utilisable, adresse de diffusion, passerelle (gateway) et prochain réseau.
Interface interactive : menu simple en ligne de commande pour une expérience conviviale.

Lancer le script

python3 network_setup.py
 or
./network_setup.py

Installation:

- Cloner le dépôt :

git clone https://github.com/votre-utilisateur/network-setup.git

cd network-setup

- Installer les dépendances :

pip install -r requirements.txt

Détails Techniques

Langage : Python 3
Bibliothèques utilisées : ipaddress, math, pyfiglet

Auteurs

Sekhmet.23z - Créateur du script

Licence

Ce projet est sous licence MIT - consultez le fichier LICENSE pour plus d’informations.

Notes
Assurez-vous d’utiliser Python 3.8 ou plus pour éviter tout problème de compatibilité.

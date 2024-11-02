# MorpionUI
Un morpion avancé comme sur le sujet mais avec des fonctionnalités en plus.
## Installation
Utiliser python pour faire un environnement virtuel.
```bash
cd <chemin_du_dossier_MorpionUI>
python -m pip install virtualenv
virtualenv --python <chemin_vers_python.exe> venv
.\venv\Scripts\activate.bat
```
Puis utilisez [pip](https://pip.pypa.io/en/stable/) pour installer la dépendance nécéssaire :
```bash
pip install -r requirements.txt
```
ou installez directement flet dans la bonne version :
```bash
pip install flet==0.12.0
```
Pour lancer le jeu, executez
```bash
flet run ./src/morpion.py
```
en espérant que vous ayez un écran 1920x1080 car il n'y a pas de responsive.
## Github
https://github.com/blueskin8/MorpionUI
# Testeur d'orthogrape vocal pour travailler le français en ligne de commande

## Principe
L'apprentissage de l'orthographe française s'accompagne traditionnellement de liste de mots à apprendre.  
Ce programme permet à l'élève de tester son orthographe de manière autonome, à partir d'une liste de mots prédéfinie (sans faute d'orthographe).  
L'ordinateur guide l'élève par la voix et des instructions écrites. Il fournit la réponse attendue en cas d'erreur et calcule le score.
Les mots mal orthographiés sont à nouveau demandés, ce qui permet à l'élève de se corriger et d'améliorer son score.

## Prérequis
- ordinateur doté d'une sortie audio (carte son et casque audio ou autre)
- OS Linux
- mplayer (avec une configuration audio opérationnelle)
- libttspico0 (Small Footpring Text To Speech library)
- Python 3
Testé sous Linux Ubuntu 20.04 amd64 avec pulseaudio

## Utilisation
1. préparer la liste de mots à tester en modifiant le début du programme
1. exécuter le programme depuis un terminal pour tester l'orthographe des mots.

### Exemple
Voici un exemple.  
(Les messages d'erreur *Audio device got stuck!* peuvent être ignorés en attendant un éventuel correctif ultérieur...)
```
$ python3 testeur_orthographe.py                                            
Ecris ton prénom : Laure                                                                                                                
Bonjour Laure ! Bienvenue dans le testeur d'orthographe ! J'espère que tu es en forme aujourd'hui... Tu démarres avec un score de zéro e
t peux gagner des points en écrivants des mots avec la bonne orthographe ! Tu peux aussi tenter d'avoir le moins de fautes possible ! At
tention c'est parti !!!                                                                                                                 
Tu peux choisir 1 pour répéter, 2 pour arrêter ou 
écris ici la réponse : chaque
Bravo !
Ton score est 1

Audio device got stuck!
Tu peux choisir 1 pour répéter, 2 pour arrêter ou 
écris ici la réponse : 1

Audio device got stuck!
Tu peux choisir 1 pour répéter, 2 pour arrêter ou 
écris ici la réponse : 1

Audio device got stuck!
Tu peux choisir 1 pour répéter, 2 pour arrêter ou 
écris ici la réponse : gnetille
Désolé la bonne réponse était g . E . n . t . i . l . l . E . 
Ton score est 1

Audio device got stuck!
Tu peux choisir 1 pour répéter, 2 pour arrêter ou 
écris ici la réponse : gentil
Bravo !
Ton score est 2
Tu peux choisir 1 pour répéter, 2 pour arrêter ou 
écris ici la réponse : un avion
Bravo !
Ton score est 3
Tu peux choisir 1 pour répéter, 2 pour arrêter ou 
écris ici la réponse : mardi
Bravo !
Ton score est 4
Tu peux choisir 1 pour répéter, 2 pour arrêter ou 
écris ici la réponse : chez
Bravo !
Ton score est 5

Audio device got stuck!
Tu peux choisir 1 pour répéter, 2 pour arrêter ou 
écris ici la réponse : gentille
Bravo !
Ton score est 6

Audio device got stuck!
Tu peux choisir 1 pour répéter, 2 pour arrêter ou 
écris ici la réponse : chercher
Bravo !
Ton score est 7
Tu peux choisir 1 pour répéter, 2 pour arrêter ou 
écris ici la réponse : jeudi
Bravo !
Ton score est 8
Tu peux choisir 1 pour répéter, 2 pour arrêter ou 
écris ici la réponse : 1
Tu peux choisir 1 pour répéter, 2 pour arrêter ou 
écris ici la réponse : compte
Désolé la bonne réponse était c . o . n . t . r . E . 
Ton score est 8
Tu peux choisir 1 pour répéter, 2 pour arrêter ou 
écris ici la réponse : contre
Bravo !
Ton score est 9
Tu peux choisir 1 pour répéter, 2 pour arrêter ou 
écris ici la réponse : à côté de
Bravo !
Ton score est 10
Le test est terminé ! Tu as été jusqu'au bout : BRAVO !

Tu as répondu à 12 mots.
Tu as 83.33 sur cent de réussite ! (16.67 sur 20)
Ton score est 10
Tu as fait 2 fautes
Au revoir et à bientôt Laure.

```

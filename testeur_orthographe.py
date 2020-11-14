import os
import random
import sys
import readline

# liste de mots à tester et variables globales ##############
# prénom de test
prenom = "Jean"

# séries à tester avec précision / aide si nécessaire dans un tableau de deux strings
serie0 = ["lundi", "mardi", "mercredi",
          "jeudi", "vendredi", "samedi", "dimanche"]
serie1 = ["il a", "un accent", "beau", ["elle", "comme elle a faim"], "alors"]
serie2 = ["acheter", "mes affaires", "belle",
          ["elles", "comme elles sont parties"], "après"]
serie3 = ["aimer", "un album", "blanc", ["en", "comme en avant"], "assez"]
serie4 = ["aller", "un ami", "bleu", [
    "il", "comme il va à la piscine"], "aujourd'hui"]
serie5 = ["appeler", "je m'appelle", "un animal", "blond", "aussi"]
serie6 = ["apporter", "une année", "bon", "bonne", "je", "autour"]
serie7 = ["attraper", "l'anniversaire", "chaud", [
    "leur", "comme dans je leur donne à manger"], "avant"]
serie8 = ["avoir", "l'anorak", "content", "lui", "avec"]
serie9 = [["c'est", "comme cela est"], [
    "ans", "comme j'ai 5 ans"], "droite", "moi", "beaucoup"]
serie10 = ["casser", "l'après-midi", "fort", "nous", "bien"]
serie11 = ["chanter", "un arbre", "froid", ["on", "comme dans on y va"], "car"]
serie12 = ["chercher", "une armoire", "gauche", "qui", "chez"]
serie13 = ["couper", "l'assiette", [
    "gentil", "comme il est gentil"], "vous", "contre"]
serie14 = ["crier", "un avion", ["gentille",
                                 "comme elle est gentille"], "à côté de", "dans"]
serie15 = ["danser", "une balle", "grand", "dehors", "chaque"]

serie_xa1 = ["une", "un", "le", "la", "des", "les", "est-t-il",
             "est-elle", "et", "sur", "dans", "avec", "pour"]
serie_xa2 = ["une pie", "une pomme", "un biberon", "une barbe", "une botte", "une balle", "elle se balade",
             "bientôt"]
serie_xa3 = ["une tarte", "une table", "la route", "une tortue", "elle termine", "tard",
             "une dame", "la date", "une dictée", "le dos", "il dessine", "dehors"]
serie_xa4 = ["un faucon", "une femme", "l'affiche", "une photo", "il souffle",
             "parfois", "un vélo", "le vent", "une olive", "la voiture", "il ouvre", "vite"]
serie_xa5 = ["le tépéphone", "l'école", "une année", "une fée", "vous réparez",
             "déjà", "du papier", "le boulanger", "un cahier", "un nez", "assez", "un pied"]
serie_xa6 = ["une chèvre", "mon frère", "une fête", "l'hiver", "il reste",
             "même", "du lait", "une semaine", "elle aime", "une reine", "la neige", "un jouet"]
serie_xa7 = ["le soir", "un voyage", "elle voit", "il boit", "pourquoi", "un oiseau", "le roi",
             "le mois", "le doigt", "le bois", "voici", "le toit", "un hibou", "une souris", "la soupe", "un trou", "elle ouvre", "aujourd'hui"]
serie_xa8 = ["un loup", "la cour", "une poupée", "il joue", "toujours", "sous"]

# séries à tester
# series = serie0 + serie1 + serie2 + serie3 + \
#     serie4 + serie5 + serie6 + serie7 + serie8
# series += serie9 + serie10 + serie11 + serie12 + serie13 + serie14 + serie15
# series = serie13 + serie14 + serie15
# series = serie_xa1+serie_xa2+serie_xa3+serie_xa4+serie_xa5+
# series = serie_xa6+serie_xa7
series = serie0 + serie12+serie13 + serie14 + serie15

score = 0
nb_fautes = 0
nb_mots_testes = 0

#### fonctions utilisées par le programme principal ##########


def lit(txt):
    """ utilise pico2wave et mplayer pour lire du texte en français"""
    cmd = 'pico2wave -l fr-FR -w test.wav "'+txt+'"'
    cmd += ' 2>&1 >/dev/null'
    res = os.system(cmd)
    if res == 0:
        cmd = "mplayer test.wav"
        cmd += ' 2>&1 >/dev/null'
        os.system(cmd)


def affiche_et_lit(txt):
    """affiche du texte dans la console et le lit"""
    print(txt)
    lit(txt)


def informe_score():
    """informe du score courant"""
    global score
    annonce_score = "Ton score est " + str(score)
    affiche_et_lit(annonce_score)


def mot_accueil():
    """Mot d'accueil"""
    global prenom
    accueil = "Bonjour "+prenom+" ! Bienvenue dans le testeur d'orthographe ! "
    accueil += "J'espère que tu es en forme aujourd'hui... "
    accueil += "Tu démarres avec un score de zéro et peux gagner des points en écrivants des mots avec la bonne orthographe ! "
    accueil += "Tu peux aussi tenter d'avoir le moins de fautes possible ! Attention c'est parti !!! "
    affiche_et_lit(accueil)


def teste_mot(mot):
    """demande la saisie au clavier d'un mot et traite la réponse"""

    lit("Voici un nouveau mot à écrire.")
    bonne_reponse = litMot(mot)
    print("Tu peux choisir 1 pour répéter, 2 pour arrêter ou ")

    # saisie de la réponse au clavier
    reponse = input("écris ici la réponse : ").lower().strip()

    traite_reponse(reponse, bonne_reponse, mot)


def litMot(mot):
    """lit le mot et extrait la réponse attendue"""
    bonne_reponse = ""
    # mot seul sans précision / aide
    if (type(mot) is str):
        bonne_reponse = mot.lower()
        lit(mot)
    # mot suivi d'une précision / aide
    else:
        bonne_reponse = mot[0].lower()
        lit(mot[0])
        lit(mot[1])
    return bonne_reponse


def traite_reponse(reponse, bonne_reponse, mot):
    """traite la réponse 
    1 : répète le mot
    2 : quitte le programme
    autre : compare la réponse avec le résultat attendu et actualise le score"""
    global score, nb_mots_testes, series
    if reponse.find("1") != -1:
        teste_mot(mot)
        return
    elif reponse == "2":
        affiche_et_lit("Tu as interrompu le test avant la fin !")
        message_fin()
        exit()
    elif reponse == bonne_reponse:
        encouragement = "Bravo !"
        affiche_et_lit(encouragement)
        score += 1
    else:
        series.append(mot)
        random.shuffle(series)
        corrige_erreur(bonne_reponse)

    nb_mots_testes += 1
    informe_score()


def corrige_erreur(mot):
    """annonce l'erreur, le résultat qui était attendu et actualise le score"""
    global nb_fautes
    nb_fautes += 1

    # décompose le mot en lettres épelées pour la correction
    lettres = ""
    for i in range(len(mot)):
        if (mot[i] == "'"):
            lettres += "apostrophe . "
        elif (mot[i] == " "):
            lettres += "espace . "
        elif (mot[i] == "e"):
            lettres += "E . "
        else:
            lettres += mot[i]+" . "
    correction = "Désolé la bonne réponse était " + str(lettres)
    affiche_et_lit(correction)


def message_fin():
    """donne le score de fin et précise la taux de réussite"""
    global nb_fautes, nb_mots_testes
    if (nb_mots_testes > 0):
        donne_avancement()
        informe_score()
        fautes = ""
        if nb_fautes == 0:
            fautes += "Tu as fait zéro faute"
        elif nb_fautes == 1:
            fautes += "Tu as fait une faute"
        else:
            fautes += "Tu as fait "+str(nb_fautes)+" fautes"
        affiche_et_lit(fautes)
        if(nb_fautes == 0 and score > 0):
            felicitations = "Bravo pour ce sans faute !"
            affiche_et_lit(felicitations)
    affiche_et_lit("Au revoir et à bientôt "+prenom+".")


def donne_avancement():
    """précise le nombre de mots testés, le nombre de fautes et le taux de réussite"""
    global nb_mots_testes, nb_fautes
    if (nb_mots_testes > 0):
        taux_succes = (nb_mots_testes-nb_fautes)*100/float(nb_mots_testes)
        avancement = "\nTu as répondu à "+str(nb_mots_testes)+" mots."
        avancement += "\nTu as "+str(round(taux_succes, 2)
                                     )+" sur cent de réussite ! ("
        avancement += str(round(taux_succes/5, 2))+" sur 20)"
        affiche_et_lit(avancement)


def demande_prenom():
    """demande le prénom de l'utilisateur"""
    global prenom
    prenom = input("Ecris ton prénom : ")


########  Programme principal ##############
demande_prenom()
mot_accueil()
# mélange les mots à tester
random.shuffle(series)
# extrait un sous-ensemble de mots à tester
series = series[:10]
# teste les mots un par un
while len(series) > 0:
    mot = series.pop(0)
    # donne le résultat intermédiaire tous les 5 mots
    # if (nb_mots_testes % 5 == 0 and nb_mots_testes > 0):
    #     donne_avancement()
    teste_mot(mot)

affiche_et_lit("Le test est terminé ! Tu as été jusqu'au bout : BRAVO !")
message_fin()

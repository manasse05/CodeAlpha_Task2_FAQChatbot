import re
import nltk
from nltk.corpus import stopwords
from nltk.stem.snowball import SnowballStemmer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

from faq import FAQ

# Télécharge la liste des mots inutiles (le, la, de, est...) une seule fois
nltk.download("stopwords", quiet=True)

# Mots inutiles de NLTK + mots de questions qui ne portent pas de sens
mots_inutiles = set(stopwords.words("french"))
mots_inutiles.update({"quel", "quels", "quelle", "quelles", "comment", "puis", "peux", "peut"})

# Outil pour ramener les mots à leur racine (livrez, livraison -> livr)
racinisateur = SnowballStemmer("french")

# En dessous de ce score, le chatbot considère qu'il n'a pas compris
SEUIL = 0.3


def nettoyer(texte):
    # Met en minuscules
    texte = texte.lower()
    # Découpe la phrase en mots (on garde uniquement lettres et chiffres)
    mots = re.findall(r"\w+", texte)
    # Enlève les mots inutiles et garde la racine des autres
    mots = [racinisateur.stem(m) for m in mots if m not in mots_inutiles]
    return " ".join(mots)


# Prépare les questions de la FAQ : on les nettoie une fois au démarrage
questions_faq = [element["question"] for element in FAQ]
questions_nettoyees = [nettoyer(q) for q in questions_faq]

# Transforme les questions en nombres (TF-IDF) pour pouvoir les comparer
vectoriseur = TfidfVectorizer()
matrice_faq = vectoriseur.fit_transform(questions_nettoyees)


def repondre(question_utilisateur):
    # Nettoie la question de l'utilisateur de la même façon
    question_nettoyee = nettoyer(question_utilisateur)

    # Si rien ne reste après nettoyage, on ne peut pas comparer
    if not question_nettoyee:
        return "Je n'ai pas compris, peux-tu reformuler ta question ?"

    # Transforme la question en nombres, puis calcule la ressemblance avec chaque question de la FAQ
    vecteur = vectoriseur.transform([question_nettoyee])
    scores = cosine_similarity(vecteur, matrice_faq)[0]

    # Trouve la question la plus proche
    meilleur_index = scores.argmax()

    # Si la ressemblance est trop faible, on l'admet honnêtement
    if scores[meilleur_index] < SEUIL:
        return "Désolé, je n'ai pas la réponse. Contacte notre service client."

    return FAQ[meilleur_index]["reponse"]


# Boucle de discussion dans le terminal
if __name__ == "__main__":
    print("Chatbot FAQ - tape 'quitter' pour arrêter")
    while True:
        question = input("Toi : ")
        if question.lower().strip() in ("quitter", "exit", "quit"):
            print("Bot : À bientôt !")
            break
        print("Bot :", repondre(question))
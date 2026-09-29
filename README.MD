# CodeAlpha - Chatbot for FAQs

Projet réalisé dans le cadre du stage virtuel **Artificial Intelligence** chez CodeAlpha (Tâche 2 : Chatbot for FAQs).

## Objectif

Créer un chatbot capable de répondre aux questions fréquentes d'une boutique en ligne. Le chatbot comprend la question de l'utilisateur, même si elle est écrite avec d'autres mots, et affiche la réponse la plus adaptée.

## Thème de la FAQ

Boutique en ligne en Côte d'Ivoire : livraison, paiement, retours, remboursement, annulation, service client (10 questions/réponses dans `faq.py`).

## Comment ça marche

1. **Collecte** : les questions et réponses sont stockées dans `faq.py`.
2. **Prétraitement (NLTK)** : le texte est mis en minuscules, découpé en mots, débarrassé des mots inutiles (le, la, de, est...), puis chaque mot est ramené à sa racine (livrez, livraison -> livr).
3. **Comparaison (scikit-learn)** : les questions sont transformées en nombres avec TF-IDF, puis la **similarité cosinus** mesure à quel point la question de l'utilisateur ressemble à chaque question de la FAQ.
4. **Réponse** : le chatbot affiche la réponse de la question la plus proche. Si la ressemblance est trop faible (seuil de 0,3), il répond qu'il n'a pas la réponse au lieu de répondre n'importe quoi.

## Outils utilisés

- Python 3
- NLTK (nettoyage du texte)
- scikit-learn (TF-IDF et similarité cosinus)

## Structure du projet

```
CodeAlpha_FAQChatbot/
├── faq.py
├── chatbot.py
├── requirements.txt
├── .gitignore
└── README.md
```

## Installation et lancement

1. Créer et activer un environnement virtuel :
```
python -m venv venv
venv\Scripts\activate
```
2. Installer les bibliothèques :
```
pip install -r requirements.txt
```
3. Lancer le chatbot :
```
python chatbot.py
```
4. Poser une question, puis taper `quitter` pour arrêter.

## Exemples

```
Toi : c'est combien la livraison ?
Bot : La livraison coûte 2000 FCFA et elle est gratuite à partir de 50000 FCFA d'achat.

Toi : je peux payer avec wave ?
Bot : Nous acceptons Orange Money, MTN Money, Moov Money, Wave et le paiement à la livraison.

Toi : quelle est la capitale de la France ?
Bot : Désolé, je n'ai pas la réponse. Contacte notre service client.
```

## Limites et améliorations possibles

- La FAQ ne contient que 10 questions : plus il y en a, meilleur est le chatbot.
- Le chatbot compare des mots, il ne comprend pas le sens profond des phrases.
- Le seuil de 0,3 peut être ajusté dans `chatbot.py` (variable `SEUIL`).
- Ajout possible d'une interface de chat graphique (Tkinter ou web).

## Auteur

Doou - Stagiaire Artificial Intelligence chez CodeAlpha.
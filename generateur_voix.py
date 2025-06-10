from gtts import gTTS
import os

def generer_voix_depuis_texte(texte, fichier_sortie="voix.mp3", langue="fr"):
    try:
        tts = gTTS(text=texte, lang= langue)
        tts.save(fichier_sortie)
        print(f"Voix enregistrée dans : {fichier_sortie}")
        return fichier_sortie
    except Exception as e:
        print("Erreur lors de la génération de la voix : ", e)
        return None
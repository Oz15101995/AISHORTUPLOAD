from moviepy.editor import *
import os

def generer_video(voix_path, texte_affiche="Bonjour, ceci est une vidéo IA", fichier_sortie="video_finale.mp4"):
    try:
        clip = TextClip(texte_affiche, fontsize=70, color='white', size=(1280, 720), method='caption', bg_color='black', align='center', font="Arial-bold")
        clip = clip.set_duration(5)

        audio = AudioFileClip(voix_path)
        audio = audio.set_duration(5)

        clip = clip.set_audio(audio)

        clip.write_videofile(fichier_sortie, fps=24)
        print(f"Vidéo générée : {fichier_sortie}")

        return fichier_sortie
    except Exception as e:
        print("Erreur lors de la génération de la vidéo : ", e)
        return None
from generateur_texte import generer_texte
from generateur_voix import generer_voix_depuis_texte
from generateur_video import generer_video
from youtube_uploader import uploader_video




def main():
    texte = generer_texte()
    if texte:
        print("Script généré :", texte)
    else:
        print("Echec de génération du texte.")
    
    voix_path = generer_voix_depuis_texte(texte)
    video_path = generer_video(voix_path, texte) 
    uploader_video(video_path, "Titre IA généré", "Une vidéo courte générée automatiquement.")



if __name__ == "__main__":
    main()
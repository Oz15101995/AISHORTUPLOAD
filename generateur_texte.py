import openai

openai.api_key = "" #ICI INSERER MON API
def generer_texte(prompt="Crée un prompte pour video de 5 secondes."):
    try:
        reponse = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content" : "faire des scripts très courts pour correspondre à des youtubes shorts de 5 secondes "}
                {"role": "user", "content": prompt}
            ],
            max_tokens=60
        )
        texte = reponse['choices'][0]['message']['content'].strip()
        return texte
    except Exception as e:
        print("Erreir lors de la génération du texte : ", e)
        return None
    
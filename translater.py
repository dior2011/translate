from googletrans import Translator, constants

def google_translate(word):
    translator = Translator()
    translation = translator.translate(word, dest="uz")
    return f"{translation.text}"

# print(google_translate("Привет"))


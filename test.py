import deepl 


auth_key="d014492b-c188-dd4d-0d35-391ec72f1c44:fx"

text = "Salut à tous"



translator = deepl.Translator(auth_key) 
result = translator.translate_text(text, target_lang="EN-US") 
translated_text = result.text

print(translated_text)
import spacy

def find_last_name(line:str) -> str:
    nlp = spacy.load('en_core_web_sm')
    text = line
    doc = nlp(text)
    last_place_name = ""
    for ent in doc.ents:
        if ent.label_ in ["GPE", "LOC"]:
            last_place_name = ent.text
    return last_place_name


nlp = spacy.load('en_core_web_sm')
print(nlp)



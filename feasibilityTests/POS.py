import spacy

nlp = spacy.load('en_core_web_sm')

doc = nlp("The Selwyn River flows through North Canterbury, near the bridge on Springston-Leeston Rd.")

# for token in doc:
#     if token.pos_ == 'ADP':  # Check if the token is a preposition
#         prepositional_phrase = ''
#         for child in token.children:
#             print(token.text)
#             print(child.text)
#             print()
#             if child.pos_ in ['NOUN', 'PROPN', 'PRON']:  # Check if the child of the preposition is a noun phrase or a pronoun
#                 prepositional_phrase += ' ' + child.text
#         if prepositional_phrase != '':
#             print(token.text + prepositional_phrase)
#
# for token in doc:
#     print (token.pos_ , token.text)

prepositional_phrase = ''
preposition = ''
adp_encountered = False

for i,token in enumerate(doc):
    if adp_encountered:
        if token.pos_ in ['NOUN', 'PROPN', 'PRON', 'DET']:
            prepositional_phrase += ' ' + token.text
        elif token.text == "-":
            prepositional_phrase += token.text
        else:
            print(preposition + prepositional_phrase)
            prepositional_phrase = ''
            adp_encountered = False

    if token.pos_ == 'ADP':
        adp_encountered = True
        preposition = token.text


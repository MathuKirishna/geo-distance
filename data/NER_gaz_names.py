import spacy
import pandas as pd

# Load a blank spaCy model or an existing one
nlp = spacy.blank('en')

# Create a new EntityRecognizer in the spaCy model pipeline
entity_ruler = nlp.create_pipe('entity_ruler')

df = pd.read_csv("gazzette/gaz_names.csv", sep=",", header=0)

place_names = df[['name','feat_type']]
print(place_names.shape)
patterns=[]
for index,rows in place_names.iterrows():
    patterns.append({'label': rows['feat_type'], 'pattern': rows['name']})
print(len(patterns))

entity_ruler.add_patterns(patterns)

# Add the EntityRecognizer to the spaCy model pipeline
nlp.add_pipe(entity_ruler)

# # Test the model
doc = nlp('1 mile S. of Okari River, between Charleston and Westport, Westland')
for ent in doc.ents:
    print(ent.text, ent.label_)



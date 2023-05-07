import spacy
from spacy_lookup import Entity
import pandas as pd

# Load a blank spaCy model or an existing one
nlp = spacy.blank('en')

# Create a new EntityRecognizer in the spaCy model pipeline
entity_ruler = nlp.create_pipe('entity_ruler')

df = pd.read_csv("gazzette/NZ_geo_names.txt", sep="\t", header=None)

place_names = df.iloc[:, 1].tolist()   # assuming the column you want to extract is the second column (index 1)

patterns=[]
for rows in place_names:
    patterns.append({'label': 'LOC', 'pattern': rows})
print(len(patterns))

entity_ruler.add_patterns(patterns)

# Add the EntityRecognizer to the spaCy model pipeline
nlp.add_pipe(entity_ruler)

# # Test the model
doc = nlp('The Selwyn River flows through North Canterbury.')
for ent in doc.ents:
    print(ent.text, ent.label_)



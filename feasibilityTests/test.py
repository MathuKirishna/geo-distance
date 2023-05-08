# import geoCoding
# import NER
# import distance
#
# data = ["1 mile S. of Okari River, between Charleston and Westport, Westland",-41.845,171.556]
# location = NER.find_last_name(data[0])
# print(location)
# coordinates = geoCoding.getGeoCoding(location)
# print(coordinates)
# distance = distance.distance(float(coordinates[0]), float(coordinates[1]), float(data[1]), float(data[2]))
# print(distance)


import spacy
# from spacy.language import Language
# from spacy.pipeline import EntityRuler


data = ["1 mile S. of Okari River, between Charleston and Westport, Westland",-41.845,171.556]
# nlp = spacy.blank('en')
nlp=spacy.load("en_core_web_sm")
ruler = nlp.add_pipe("entity_ruler")

patterns = [{"label": "ORG", "pattern": "Westland"}, {"label": "GPE", "pattern": "Westport"}, {"label": "river", "pattern": "Okari River"}]

ruler.add_patterns(patterns)

doc = nlp(data[0])

print([(ent.text, ent.label_) for ent in doc.ents])
# @Language.component("add_entity_patterns")
# def add_entity_patterns(nlp):
#     patterns = [{"label": "ORG", "pattern": "Apple"},
#                 {"label": "GPE", "pattern": [{"LOWER": "san"}, {"LOWER": "francisco"}]}]
#     ruler = EntityRuler(nlp, overwrite_ents=True)
#     ruler.add_patterns(patterns)
#     nlp.add_pipe(ruler, before="ner")
#     return nlp

# nlp = spacy.load("en_core_web_sm")
# nlp = add_entity_patterns(nlp)

# doc = nlp("Apple is headquartered in Cupertino, but also has offices in San Francisco.")
# print([(ent.text, ent.label_) for ent in doc.ents])



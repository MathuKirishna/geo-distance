import spacy
import pandas as pd

df = pd.read_csv("../data/preprocessed_200.csv", header=0, sep=",")

patterns_df = pd.read_csv("../data/gazzette/gaz_names.csv")

place_names_dict = patterns_df[['name', 'feat_type']]
patterns=[]
for index,rows in place_names_dict.iterrows():
    patterns.append({'label': rows['feat_type'], 'pattern': rows['name'].lower()})

nlp = spacy.blank('en')
# nlp=spacy.load("en_core_web_sm")
ruler = nlp.add_pipe("entity_ruler")

ruler.add_patterns(patterns)
null_data=0
null_data_index=[]
df['place_names']=0
df['last_place_name']=0
df['last_place_name_feature_type']=0

for index, rows in df.iterrows():
    place_names=[]
    doc = nlp(rows['Locality'])
    if len(doc.ents) == 0:
        # print(rows['Locality'])
        null_data+=1
        null_data_index.append(index)
    else:
        for ent in doc.ents:
            place_names.append({'place_name': ent.text, 'feature_type': ent.label_})
        if len(place_names)>1:
            df.at[index,'place_names']=place_names[:-1]
        else:
            df.at[index,'place_names']=place_names
        df.at[index,'last_place_name']=place_names[-1]['place_name']
        df.at[index,'last_place_name_feature_type']=place_names[-1]['feature_type']

    # print([(ent.text, ent.label_) for ent in doc.ents])
for index in null_data_index:
    df=df.drop(index)
print(df.head)

df.to_csv('../data/ner_feature_extracted_200.csv', header=True, sep=',', index=False)

# for index, row in df.iterrows():
#     last_place_name = find_last_name(row['Locality'])
#     print(last_place_name)
#     # if last_place_name == "":
#     #     print(row)
#     break
# data = ["1 mile S. of Okari River, between Charleston and Westport, Westland",-41.845,171.556]
# location = find_last_name(data[0])
# print(location)
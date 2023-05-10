import pandas as pd

df = pd.read_csv("data/BioGeoRef cleaned data all.csv", header=0, sep=",")
print(df.head)

# Iterate over the rows of the DataFrame and expand cardinal data and change the data to lowercase
# Need to loop to find iterative conditions
for index, row in df.iterrows():
    description = row['Locality'].lower()
    locality = description.replace(" n.e.", " north east")
    locality = locality.replace(" n.w.", " north west")
    locality = locality.replace(" s.e.", " south east")
    locality = locality.replace(" s.w.", " south west")
    locality = locality.replace(" e.", " east")
    locality = locality.replace(" s.", " south")
    locality = locality.replace(" n.", " north")
    locality = locality.replace(" w.", " west")
    if locality.startswith("n."):
        locality = locality.replace("n.", "north")
    elif locality.startswith("e."):
        locality = locality.replace("e.", "east")
    elif locality.startswith("w."):
        locality = locality.replace("w.", "west")
    elif locality.startswith("s."):
        locality = locality.replace("s.", "south")
    df.at[index, 'Locality'] = locality
df.to_csv('data/preprocessed_all.csv', header=True, sep=',', index=False)

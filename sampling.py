import pandas as pd

# Load the original dataset
df = pd.read_csv('data/BioGeoRef cleaned data all.csv')

# Select 200 random rows from the dataset
df_random = df.sample(n=200, random_state=42)

# Write the random subset to a csv file
df_random.to_csv('data/sample_200.csv', index=False)

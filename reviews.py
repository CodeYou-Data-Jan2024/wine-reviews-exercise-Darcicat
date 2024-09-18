import pandas as pd

wine_reviews = pd.read_csv('data/winemag-data-130k-v2.csv.zip')
summary = (
    wine_reviews.groupby('country')
    .agg(
        reviews=('title','count'), # counts the number of reviews
        points=('points', 'mean') # calculate avg
    )
    .reset_index()
)
print(summary)


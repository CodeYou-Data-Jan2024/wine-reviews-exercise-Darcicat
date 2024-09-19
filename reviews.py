import pandas as pd

wine_reviews = pd.read_csv('data/winemag-data-130k-v2.csv.zip')
#print(wine_reviews.columns)

summary = (
    wine_reviews.groupby('country')
    .agg(
        count=('title','count'), # counts the number of reviews
        points=('points', 'mean') # calculate avg
    )
    .reset_index()
)
summary.sort_values(by=["count"], inplace=True, ascending=False)
summary["points"] = summary["points"].round(1)
print(summary)
summary.to_csv("data/reviews-per-country.csv", index=True)



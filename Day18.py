#MOVIE DATASET ANALYSIS
import pandas as pd
import matplotlib.pyplot as plt
data = {
    "Movie_Name": ["Inception","Avengers: Endgame","Interstellar","Joker",
                   "Titanic","3 Idiots","Bahubali 2","Dangal"],

    "Rating": [8.8, 8.4, 8.7,8.3,7.9,8.4,8.2,8.3],

    "Genre": ["Sci-Fi","Action","Sci-Fi","Thriller",
              "Romance","Comedy/Drama","Action","Sports/Drama"
    ],

    "Revenue": [836000000, 2798000000,701000000,1074000000,2200000000,40000000,250000000,310000000]
}
df = pd.DataFrame(data)

#highest rated movie
highest = df.sort_values(by="Rating", ascending=False)
print(highest[["Movie_Name", "Rating"]])

#most profitable genres
most_profit = df.groupby("Genre")["Revenue"].sum()
print(most_profit.sort_values(ascending=False))

#Genre vs Revenue
plt.bar(most_profit.index,most_profit.values)
plt.title("GENRE VS REVENUE")
plt.xlabel("genre")
plt.ylabel("revenue")
plt.tight_layout()
plt.show()

#Rating Distribution
plt.hist(df["Rating"],bins = 5 )
plt.title("RATING DISTRIBUTION")
plt.xlabel("rating")
plt.ylabel("frequency")
plt.show()

#correlation between rating and revenue
print("Correlation between Rating and Revenue:",df["Rating"].corr(df["Revenue"]))

#Top 5 movies
top5 = df.sort_values(by = "Revenue", ascending=False).head(5)
print(top5[["Movie_Name","Revenue"]])

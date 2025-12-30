import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("CAvideos.csv", encoding="latin1")

# removing the removed videos
df = df[df["video_error_or_removed"] == False]

# converting to numeric
cols = ["views", "likes", "dislikes", "comment_count"]
df[cols] = df[cols].apply(pd.to_numeric, errors="coerce")

sns.set_theme(style="darkgrid")

#Count Plot 
plt.figure(figsize=(8,5))
sns.countplot(y="category_id", data=df)
plt.title("Trending Videos by Category")
plt.show()

#Scatter Plot 
plt.figure(figsize=(6,4))
sns.scatterplot(x="views", y="likes", data=df, alpha=0.3)
plt.title("Likes vs Views")

plt.savefig("likes_vs_views.png")  # SAVE BEFORE SHOW
plt.show()

# Top 10 Videos 
top10 = df.sort_values(by="views", ascending=False).head(10)
print("\nTOP 10 MOST VIEWED VIDEOS:")
print(top10[["title", "views"]])


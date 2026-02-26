"""
Nihar patel
lab 8, APIs
Feb 24,2026
"""

#-----------------------------------
#Example 1: data frame using pandas
#-----------------------------------

import pandas as pd

# step 1 Dict_ as the. static tamplatee of our API
dict_ = {
    'a' : [11,21,31],
    'b' : [12,22,32]
}
# step 2 create a dataframe using pandas
df = pd.DataFrame(dict_)

#head mehtod of the dataframe communicates with the API displaying the first few row of the dataframe
print("\n Example 1: simple API")
print(df.head())

#mean mehtod calculates and returns the mean valuse of a df
print (f"the mean valuse is = \n{df.mean()}")

#-----------------------------------
#Example 2: get NBA team form static.py file
#-----------------------------------
    #step 1, data collection
from static import get_teams

nba_teams = get_teams()
#testing

print(f"the first two teams: {nba_teams[:2]}")

#step 2, creat dataframe
df_teams = pd.DataFrame(nba_teams)
print ("\n All teams")
print (df_teams.head())

#step 3 , working with the data in df_teams
df_worriors = df_teams[df_teams['nickname'] == 'Warriors']
print ('\nwarriors')
print(df_worriors)

#-----------------------------------
#Example 3: working with external APIs
#-----------------------------------
#step 1, data collection
#download the pickle file
import requests

url = "https://s3-api.us-geo.objectstorage.softlayer.net/cf-courses-data/CognitiveClass/PY0101EN/Chapter%205/Labs/Golden_State.pkl"

# save download file
file_name = "Golden_state.pkl"

print(f"\nDownloading external file!...")
response = requests.get(url)
if response.status_code == 200: 
    with open(file_name, "wb") as f:
        f.write(response.content)
    print("Download complete!")
else: 
    print("Download failed!")

#step 2, create dataframe
#b. load dataframe from a pickle file
games = pd.read_pickle(file_name)
print(f"\n Games from pickle file")
print(games.head())

#step 3, working with the data in the dataframe 
#c. filter GSW v Raptors 
warriors_vs_raptors = games[games['MATCHUP'].str.contains('TOR')]

#testing 
print ("\n GSW vs raptors games")
print (warriors_vs_raptors)

gsw_home_vs_raptors = warriors_vs_raptors[warriors_vs_raptors['MATCHUP'].str.contains(' vs ')]
gsw_away_vs_raptors = warriors_vs_raptors[warriors_vs_raptors['MATCHUP'].str.contains(' @ ')]

#testing 
print("\n GSW home games")
print(gsw_home_vs_raptors)

#d. calculate the average of the home and away matches
home_avg_plus = gsw_home_vs_raptors['PLUS_MINUS'].mean()
away_avg_plus = gsw_away_vs_raptors['PLUS_MINUS'].mean()
home_avg_pts = gsw_home_vs_raptors['PTS'].mean()
away_avg_pts = gsw_away_vs_raptors['PTS'].mean()

print(f"GSW home average = {home_avg_plus}")
print(f"GSW away average = {away_avg_plus}")

#e. visualization of data analysis
import matplotlib.pyplot as plt

metrics = ["PLUS_MINUS", "PTS"]
home_values = [home_avg_plus, home_avg_pts]
away_values = [away_avg_plus, away_avg_pts]

x = range(len(metrics))
bar_width = 0.35

plt.figure(figsize=(8,5))
plt.bar([i - bar_width/2 for i in x],home_values, width= bar_width, label = 'Home' , color='skyblue')
plt.bar([i - bar_width/2 for i in x],away_values, width= bar_width, label = 'Away' , color='orange')

plt.xticks(x, metrics)
plt.title("GSW vs Raptors")

plt.ylabel("Average value")
plt.legend()
plt.show(block=True)

input ("Press Enter to close...")


# -----------------------------------
# Example 4: Working with another external API
# -----------------------------------


# Step 1 – Data Collection
print("\nDownloading data from new API...")

url = "https://jsonplaceholder.typicode.com/posts"

response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    print("Download complete!")
else:
    print("Download failed!")

# Step 2 – Create DataFrame
df_posts = pd.DataFrame(data)

print("\nAll Posts")
print(df_posts.head())

# Step 3 – Working with the data
# Filter posts from userId = 1
user1_posts = df_posts[df_posts["userId"] == 1]

print("\nPosts from User 1")
print(user1_posts)

# Step 4 – Calculate averages
# Example: average title length
df_posts["title_length"] = df_posts["title"].str.len()

avg_title_length = df_posts["title_length"].mean()
avg_body_length = df_posts["body"].str.len().mean()

print(f"\nAverage title length = {avg_title_length}")
print(f"Average body length = {avg_body_length}")

# Step 5 – Visualization
metrics = ["Title Length", "Body Length"]
values = [avg_title_length, avg_body_length]

plt.figure(figsize=(8,5))
plt.bar(metrics, values)

plt.title("Post Length Analysis")
plt.ylabel("Average Characters")
plt.show()

input("Press Enter to close...")
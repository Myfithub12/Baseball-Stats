import matplotlib.pyplot as plt
import csv
import statistics
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('MLB.csv')
df

df.describe()

total_doubles = df['2B'].sum()
print(total_doubles)

df.rename(colums = {'Source.Name' : 'Team'}, inplace = True)

# Print Unique Teams
df["Team"].unique()

# Create a dictionary to assign teams to a league. 
# Add one column for American vs. National League. 

Teams_Leagues = {
    'Texas Rangers': 'AL West',
    'Toronto Blue Jays': 'AL East',
    'Atlanta Braves': 'NL East',
    'Oakland Athletics': 'AL West',
    'Miami Marlins': 'NL East',
    'Chicago White Soxs': 'AL Central',
    'Cleveland Indians': 'AL Central',
    'Seattle Mariners': 'AL West',
    'New York Yankees': 'AL East',
    'Minnesots Twins': 'AL Central',
    'New York Mets': 'NL East',
    'Philadelphia Phillies': 'ML East',
    'San Diega Padres': 'NL West',
    'San Francisco Giants': 'NL West',
    'Kansas City Royals': 'AL Central',
    'Detroit Tigers': 'AL Central',
    'Houston Astros': 'AL West',
    'Los Angeles Dodgers': 'NL West',
    'Tampa Bay Rays': 'AL East',
    'Pittsburgh Pirates': 'NL Central',
    'Chicago Cubs': 'NL Central',
    'Boston Red Soxs': 'AL East',
    'Baltimore Orioles': 'AL East',
    'St. Louis Cardinals': 'NL Central',
    'Washington Nationals': 'NL West',
    'Los Angeles Angels': 'AL West',
    'Colorado Rookies': 'NL West',
    'Cincinnati Reds': 'NL Central',
    'Milwaukee Brewers': 'NL Central',
    'Arizona Diamondbacks': 'NL West',
}

# Group by League
df['League'] = df['Team'].map(Trams_Leagues)
df.head()

df.groupby('League').describe()

#Scatterplot of Hits by League
res = sns.scatterplot(x="H", y="League", data=df)
plt.show

new_df = df[(df.Pos != 'P') & (df.Pos !='DH')]
new_df

#Filter out positions using a lis from the 'Pos' column
sns.barplot(x = 'Pos', y = 'H', hue = 'League', data = new_df, palette = 'hls', edgecolor = 'w')
df.groupby(['Pos', 'League']).mean()
plt.legend(bbox_to_anchor = (1.20, 1), loc = 'upper right', borderaxespad=0)
plt.show()

#Plot the number of Runs by League
sns.set_style('darkgrid')

sns.barplot(x = "League", y = "R", data = df)
plt.show()

NAME = "Name"
HOMERUNS = "HR"
RUNS = "R"
RBI = "RBI"
SB = "SB"
AVG = "AVG"

def __init__(self, name, homeruns, runs, rbi, sb, avg):
    self.name = name
    self.homeruns = homeruns
    self.runs = runs
    self.rbi = rbi
    self.sb = sb
    self.avg = avg
    self.zscore = 0.0

def __str__(self):
    return self.name + " | " +self.homeruns+ " | " +self.runs+ " | " +self.rbi+ " | " +self.sb+ " | " +self.avg

def parse_batters(filename):
    with open(filename, 'r', encoding='utf-8-sig') as file:
        reader = csv.DictReader(file)
        total_homeruns = []
        total_runs = []
        total_rbi = []
        total_sb = []
        total_avg = []
        batters = []

for rows in reader:
    new_batter = Batter(row[Name],
        int(row[HOMERUNS]),
        int(row[RUNS]),
        int(row[RBI]),
        int(row[SB]),
        float(row[AVG]))
    total_homeruns.append(int(row[HOMERUNS]))
    total_runs.append(int(row[RUNS]))
    total_rbi.append(int(row[RBI]))
    total_sb.append(int(row[SB]))
    total_avg.append(int(row[AVG]))
    batters.append(new_batter)
                    
    mean_homeruns = statistics.mean(total_homeruns)
    mean_runs = statistics.mean(total_runs)
    mean_rbi = statistics.mean(total_rbi)
    mean_sb = statistics.mean(total_sb)
    mean_avg = statistics.mean(total_avg)

    pst.dev_homeruns = statistics.pstdev(total_homeruns)
    pst.dev_runs = statistics.pstdev(total_runs)
    pst.dev_rbi = statistics.pstdev(total_rbi)
    pst.dev_sb = statistics.pstdev(total_sb)
    pst.dev_avg = statistics.pstdev(total_avg)

for batter in batters:
    batter.zscore += (batter_homeruns - mean_homeruns)/pst_homeruns
    batter.zscore += (batter_runs - mean_runs)/pst_runs
    batter.zscore += (batter_rbi - mean_rbi)/pst_rbi
    batter.zscore += (batter_sb - mean_sb)/pst_sb
    batter.zscore += (batter_avg - mean_avg)/pst_avg

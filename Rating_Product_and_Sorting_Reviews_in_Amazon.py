###################################################
# Calculation of Average Rating Based on Recent Reviews and Comparison with Existing Average Rating
###################################################

# In the given dataset, users have provided ratings and written reviews for a product.
# Our goal is to evaluate the ratings by weighting them according to time.
# The initial average rating should be compared with the time-weighted average rating.


###################################################
# Loading the Dataset and Calculating the Product’s Average Rating
###################################################

import pandas as pd
import math
import scipy.stats as st
from sklearn.preprocessing import MinMaxScaler
pd.set_option('display.max_columns', None)
pd.set_option('display.expand_frame_repr', False)
pd.set_option('display.max_rows', 10)
pd.set_option('display.float_format', lambda x: '%.2f' % x)

df = pd.read_csv("amazon_review.csv")
df.head()
df.info()
df.describe().T
df.shape


df["overall"].mean()


###################################################
# Calculation of Time-Weighted Average Rating
###################################################

df.info()
df.head()
df["day_diff"].value_counts()

df.groupby("day_diff")["overall"].mean()

(df.loc[(df["day_diff"] <= 30), "overall"].mean()) * 0.40 + \
(df.loc[(df["day_diff"] > 30) & (df["day_diff"] <= 90), "overall"].mean()) * 0.30 + \
(df.loc[(df["day_diff"] > 90) & (df["day_diff"] <= 180), "overall"].mean()) * 0.20 + \
(df.loc[(df["day_diff"] > 180), "overall"].mean()) * 0.10

df["weighted_rating"] = (df.loc[(df["day_diff"] <= 30), "overall"].mean()) * 0.40 + \
                        (df.loc[(df["day_diff"] > 30) & (df["day_diff"] <= 90), "overall"].mean()) * 0.30 + \
                        (df.loc[(df["day_diff"] > 90) & (df["day_diff"] <= 180), "overall"].mean()) * 0.20 + \
                        (df.loc[(df["day_diff"] > 180), "overall"].mean()) * 0.10

(df.loc[(df["day_diff"] <= 30), "overall"].mean()) * 0.40
(df.loc[(df["day_diff"] > 30) & (df["day_diff"] <= 90), "overall"].mean()) * 0.30
(df.loc[(df["day_diff"] > 90) & (df["day_diff"] <= 180), "overall"].mean()) * 0.20
(df.loc[(df["day_diff"] > 180), "overall"].mean()) * 0.10

bins = [0, 30, 90, 180, df["day_diff"].max()]
labels = ["0-30", "31-90", "91-180", "180+"]

df["days"] = pd.cut(df["day_diff"], bins, labels=labels, include_lowest=True)

group_means = df.groupby("days")["overall"].mean()

weights = {"0-30" : 0.40, "31-90": 0.30, "91-180": 0.20, "180+": 0.10}

weighted_contributions = group_means * pd.Series(weights)

pd.DataFrame({"mean": group_means, "weights": weighted_contributions})


###################################################
# Determining the Top 20 Reviews to Be Displayed on the Product Detail Page
###################################################

###################################################
# Generating the "helpful_no" Variable
###################################################

# total_vote represents the total number of up and down votes given to a review.
# up means helpful.
# The dataset does not contain the helpful_no variable; it needs to be derived from existing variables.

df.head()
df["helpful"].value_counts()

df["helpful_no"] = df["total_vote"] - df["helpful_yes"]


###################################################
# Calculating score_pos_neg_diff, score_average_rating, and wilson_lower_bound Scores and Adding Them to the Dataset
###################################################

def score_pos_neg_diff(up, down):
    return up - down

df["score_pos_neg_diff"] = df.apply(lambda x: score_pos_neg_diff(x["helpful_yes"], x["helpful_no"]), axis=1)


def score_average_rating(up, down):
    if up + down == 0:
        return 0
    return up / (up + down)


df["score_average_rating"] = df.apply(lambda x: score_average_rating(x["helpful_yes"], x["helpful_no"]), axis=1)


def wilson_lower_bound(up, down, confidence=0.95):
    n = up + down
    if n == 0:
        return 0
    z = st.norm.ppf(1 - (1 - confidence) / 2)
    phat = 1.0 * up / n
    return (phat + z * z / (2 * n) - z * math.sqrt((phat * (1 - phat) + z * z / (4 * n)) / n)) / (1 + z * z / n)

df["wilson_lower_bound"] = df.apply(lambda x: wilson_lower_bound(x["helpful_yes"], x["helpful_no"]), axis=1)

df.sort_values("wilson_lower_bound", ascending=False).head(20)







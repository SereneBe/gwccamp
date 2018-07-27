import matplotlib.pyplot as plt
import school_scores

list_of_report = school_scores.get_all()
print(list_of_report)

# list of what will be in data set
math = []
ScoreRanges = []

scores = school_scores.get_all()

for score in scores:
    if score["State"]["Code"] == "AL":
        ScoreRanges.append(score["Total"]["Math"])
        math.append(score["Year"])

plt.plot(math, ScoreRanges)
plt.legend(['AL'], loc='upper left')

# Set the x and y labels
plt.xlabel("Math")
plt.ylabel("Score Ranges")

plt.title("Math Total in Alabama")

plt.show()

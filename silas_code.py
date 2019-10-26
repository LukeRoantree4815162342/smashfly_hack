job_dfs = [successful_df[successful_df[j]==True] for j in jobs]

age_stats = {jobs_unique[i]: {"kurtosis":df["Age"].kurtosis(), "skew":df["Age"].skew()} for i,df in enumerate(job_dfs)}

#print(age_stats)
#plt.figure()

statistics = ["skew", "kurtosis"]
fig, ax = plt.subplots(len(statistics), sharex=True)

for row in range(len(statistics)):
    ax[row].bar(range(len(jobs)), [age_stats[j][statistics[row]] for j in jobs_unique])
    ax[row].set_xticks(range(len(jobs)))
    ax[row].set_xticklabels([j.replace(' ','\n') for j in jobs_unique], rotation=45, size=9)
    ax[row].set_ylabel(statistics[row])
fig.suptitle("Description of Interviewed Applicant Age by Job Type", size=10)

"""
and;
"""

job_dfs = [successful_df[successful_df[j]==True] for j in jobs]

age_stats = {jobs_unique[i]: df["Age"].describe() for i,df in enumerate(job_dfs)}

#print(age_stats)
#plt.figure()

statistics = ["mean", "std", "50%", "25%", "75%"]
fig, ax = plt.subplots(len(statistics), sharex=True)

for row in range(len(statistics)):
    ax[row].bar(range(len(jobs)), [age_stats[j][statistics[row]] for j in jobs_unique])
    ax[row].set_xticks(range(len(jobs)))
    ax[row].set_xticklabels([j.replace(' ','\n') for j in jobs_unique], rotation=45, size=9)
    ax[row].set_ylabel(statistics[row])
fig.suptitle("Description of Interviewed Applicant Age by Job Type", size=10)



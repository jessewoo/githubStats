import requests

# DOC: https://docs.github.com/en/rest/metrics/statistics#get-the-last-year-of-commit-activity

print("---- FEATURE - GIT COMMITS IN THE LAST YEAR ----\n")


def chunks(lst, n):
    """Yield successive n-sized chunks from lst."""
    for i in range(0, len(lst), n):
        yield lst[i:i + n]


# Returns the total commit counts for the owner and total commit counts in all in the last 52 weeks.
commit_response = requests.get(
    "https://api.github.com/repos/hubzero/hubzero-cms/stats/participation")
commit_data = commit_response.json()

print("Output: ", commit_data)

each_week_data = commit_data["all"]
number_of_weeks = len(each_week_data)
# print("Number of weeks: ", number_of_weeks)

chunk = list(chunks(each_week_data, 4))
print("** Commits in the last 52 weeks, segmented by months")
print(chunk, "\n")

print("** Commits in the last 12 months")
chunk_by_month = [sum(l) for l in chunk]
print(chunk_by_month)

# NOTE: Will this be stored on a database, will need to note the first time cron job ran, to indicate the 1st week

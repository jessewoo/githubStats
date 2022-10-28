import requests

# NOTE: GIT API DOCUMENTION - https://docs.github.com/en/rest/issues/issues#list-repository-issues

# Open Issues
open_response = requests.get("https://api.github.com/repos/hubzero/hubzero-cms/issues?state=open&per_page=100&since=2022-01-01")
open_data = open_response.json()
number_of_open_issues = len(open_data)
print("Number of open issues since 2022: ", number_of_open_issues)

# Closed Issues / Can segment by year, months
closed_response = requests.get("https://api.github.com/repos/hubzero/hubzero-cms/issues?state=closed&per_page=100&since=2022-01-01")
closed_data = closed_response.json()
number_of_closed_issues = len(closed_data)
print("Number of closed issues since 2022: ", number_of_closed_issues)

# NOTE: Will this be stored on a database, will need to update the number as issues get closed in recent months

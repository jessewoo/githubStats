import requests
response = requests.get("https://api.github.com/repos/hubzero/hubzero-cms/contributors")
data = response.json()

number_of_contributors = len(data)
print("Number of contributors: ", number_of_contributors)
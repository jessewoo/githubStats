import requests

response = requests.get("https://api.github.com/repos/hubzero/hubzero-cms/releases")
data = response.json()

number_of_releases = len(data)
print("Number of releases: ", number_of_releases, "\n")

# list_of_logins = [obj['login'] for obj in data]

list_of_releases = []
for obj in data:
    x = {}

    x['tag_name'] = obj['tag_name']
    x['author'] = obj['author']['login']
    x['created_at'] = obj['created_at']
    
    list_of_releases.append(x)

print("List of Releases:\n", list_of_releases, "\n")
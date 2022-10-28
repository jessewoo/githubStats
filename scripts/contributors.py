import requests

# NOTE: https://geodynamics.org/resources/jupyter/gitstats utilized https://gitstats.sourceforge.net/, 3rd party code

# https://docs.github.com/en/rest/repos/repos#list-repository-contributors

response = requests.get("https://api.github.com/repos/hubzero/hubzero-cms/contributors")
data = response.json()

number_of_contributors = len(data)
print("Number of contributors: ", number_of_contributors, "\n")

# list_of_logins = [obj['login'] for obj in data]

list_of_logins = []
list_of_contributions = []
for obj in data:
    x = {}

    if 'login' in obj:
        x['login'] = obj['login']
        x['contributions'] = obj['contributions']
        list_of_logins.append(x['login'])
    else:
        x['login'] = "anon"
        x['contributions'] = 0
    
    list_of_contributions.append(x)

print("List of Logins:\n", list_of_logins, "\n")

list_of_contributions_numbers = [obj['contributions'] for obj in list_of_contributions]

print("Number contributions by contributor:")
print(list_of_contributions, "\n")
print("List of contributions by author:", list_of_contributions_numbers, "\n")
print("Sum of the number of contributions:", sum(list_of_contributions_numbers), "\n")
import requests
from datetime import datetime
pixela_endpoint = "https://pixe.la/v1/users"
TOKEN = "hsktu2lslop8mahoptrwenm"
USERNAME = "mahdi12"
GRAPH_ID = "graph1"
today = datetime(year=2025, month=10, day=28)
# parameter = {
#     "token": "hsktu2lslop8mahoptrwenm",
#     "username": "mahdi12",
#     "agreeTermsOfService": "yes",
#     "notMinor": "yes"
# }

# response = requests.post(url=pixela_endpoint, json=parameter)
# print(response.text)

# graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
#
# graph_config = {
#     "id": "graph1",
#     "name": "coding",
#     "unit": "hour",
#     "type": "float",
#     "color": "sora"
# }
header = {
    "X-USER-TOKEN": TOKEN
}



# response = requests.post(url=graph_endpoint, json=graph_config, headers=header)
# print(response.text)
# pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"

# response =requests.post(url=pixel_endpoint, json=parameter, headers=header)
# update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"
# parameter = {
#     "quantity": "4.5"
# }

# response = requests.put(url=update_endpoint, json=parameter, headers=header)

delete_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"
response = requests.delete(url=delete_endpoint, headers=header)
print(response.text)


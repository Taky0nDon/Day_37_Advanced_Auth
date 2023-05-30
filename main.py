### HABIT TRACKER ###
import os

import requests
import dotenv
import html
import datetime
import json

dotenv.load_dotenv("environment.env")
now = datetime.datetime.now()
TODAY = now.strftime("%Y%m%d")
PIXELA_ENDPOINT = "https://pixe.la/v1/users"
PIXELA_TOKEN = os.environ.get("PIXELA_TOKEN")
PIXELA_USERNAME = os.environ.get("PIXELA_USERNAME")
GRAPH_ID = "my-first-graph"

GRAPH_HEADERS = {
    "X-USER-TOKEN": PIXELA_TOKEN
}



## CREATING PIXELA ACCOUNT
# pixela_params = {
#     "token": PIXELA_TOKEN,
#     "username": PIXELA_USERNAME,
#     "agreeTermsOfService": "yes",
#     "notMinor": "yes"
# }
# pixela_create_account = requests.post(url=PIXELA_ENDPOINT, json=pixela_params)
# print(pixela_create_account.text)
# print(pixela_create_account)

def create_graph(graph_id: str, graph_name: str) -> str:
    """ Create a pixela graph with the id and name as arguments, returns a string containing the response message
    from the pixela api"""
    GRAPH_CREATE_ENDPOINT = f"{PIXELA_ENDPOINT}/{PIXELA_USERNAME}/graphs"
    GRAPH_DATA = {"id": graph_id,
                  "name": graph_name,
                  "unit": "minutes",
                  "type": "int",
                  "color": "shibafu",
                  "timezone": "Asia/Tokyo"
                  }
    graph_response = requests.post(url=GRAPH_CREATE_ENDPOINT,
                                   headers=GRAPH_HEADERS,
                                   json=GRAPH_DATA)
    response = graph_response.text
    return response


def update_graph(graph_id: str, date: str) -> None:
    """Post a value to the graph for the ID provided as an argument. Quantity (in minutes) is taken as user input.
    Returns API status response"""
    time_spent = input("How many minutes did you spend learning to code today? \n")
    GRAPH_UPDATE_ENDPOINT = f"{PIXELA_ENDPOINT}/{PIXELA_USERNAME}/graphs/{graph_id}"
    graph_update_data = {
        "date": date,
        "quantity": time_spent
    }
    update_post = requests.post(url=GRAPH_UPDATE_ENDPOINT, headers=GRAPH_HEADERS, json=graph_update_data)
    status_dict = json.loads(update_post.text)
    print(status_dict["message"])

def update_pixel(quantity: str, id: str, date) -> None:
    update_endpoint = f"{PIXELA_ENDPOINT}/{PIXELA_USERNAME}/graphs/{id}/{date}"
    put_request = requests.put(url=update_endpoint, json={"quantity": quantity}, headers=GRAPH_HEADERS)
    response = json.loads(put_request.text)
    print(response["message"])

def delete_pixel(graph_id: str, date: str) -> None:
    delete_endpoint = f"{PIXELA_ENDPOINT}/{PIXELA_USERNAME}/graphs/{graph_id}/{date}"
    delete_request = requests.delete(url=delete_endpoint, headers=GRAPH_HEADERS)
    response = json.loads(delete_request.text)
    print(response["message"])
# create_graph("coding-graph", "Minutes Learning to Code")
yesterday = datetime.datetime(year=2023, month=5, day=28).strftime("%Y%m%d")
# add_pixel = update_graph("coding-graph", date=yesterday)
delete_pixel(graph_id="coding-graph", date=yesterday)
# update = update_pixel(quantity="105", id="coding-graph", date=TODAY)

# display_graph = requests.get(url=f"{PIXELA_ENDPOINT}/{PIXELA_USERNAME}/graphs/{GRAPH_DATA['id']}")
# display_graph.raise_for_status()
#
## WRITE HTML RESPONSE TO FILE
# response = requests.get("https://facebook.com")
# with open("test.html", "w", encoding="utf-8") as graph_output:
#     sanitized_text = html.unescape(response.text)
#     graph_output.write(sanitized_text)

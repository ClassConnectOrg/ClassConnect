import requests
import json
from bs4 import BeautifulSoup

def read(file_name : str):
    file_name = f"JSON/{file_name}.json"

    with open(file_name, 'r') as f:
        dict_obj = json.load(f)
        return dict_obj



def write(dict_obj : object, file_name : str, json_indent=2):
    file_name = f"JSON/{file_name}.json"

    with open(file_name, 'w') as f:
        json.dump(dict_obj, f, indent=json_indent)


'''
r = requests.get("https://catalog.drexel.edu/coursedescriptions/quarter/undergrad/bio/")
with open("./python/req.html", "w+") as f:
    f.write(r.text)
'''

with open("./python/req.html", "r") as f:
    soup = BeautifulSoup(f, features="html.parser")
    class_data = soup.find_all("span", "cdspacing")




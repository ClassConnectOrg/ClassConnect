import requests
import json
from bs4 import BeautifulSoup

def json_read(file_name : str):
    file_name = f"JSON/{file_name}.json"

    with open(file_name, 'r') as f:
        dict_obj = json.load(f)
        return dict_obj



def json_write(dict_obj : object, file_name : str, json_indent=2):
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
    soup.prettify()
    data = soup.find_all("div", "courseblock")

#print(soup.get_text())

#print(data)
idx = 0
classes = json_read("class_BIO")

with open("./python/temp.html", "w+") as f:
    f.write(str(data[0]))

with open("./python/temp.html", "r") as f:
    soup = BeautifulSoup(f, features="html.parser")
    soup.prettify()
    temp_class = []
    #class_data = soup.find("span", "cdspacing")
    for item in soup.find_all("span", "cdspacing"):
        temp_class.append(item.get_text())
    
    print(temp_class)
    classes.append[{"Course": temp_class[0], "Title": temp_class[1]}]

print(classes)
json_write(classes, "class_BIO")
'''
for item in data:
    print(item)
'''




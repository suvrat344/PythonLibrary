import json
from urllib.request import urlopen

people_string = '''
{
    "people" : [
        {
            "name" : "John Smith",
            "phone" : "615-555-7164",
            "emails" : ["johnsmith@boguseemail.com","john.smith@work-place.com"],
            "has_license" : false
        },
        {
            "name" : "Jane Doe",
            "phone" : "560-555-5153",
            "emails" : null,
            "has_license" : true
        }
    ]
}
'''

# Convert from JSON to Python
data = json.loads(people_string)
print(data)
print(type(data))

for person in data["people"]:
    print(person["name"])


for person in data["people"]:
    del person["phone"]


# Convert from Python to JSON:
new_string = json.dumps(data,indent=2,sort_keys=True)
print(new_string)


with open("states.json","r") as f:
    data = json.load(f)

for state in data["states"]:
    print(state["name"],state["abbreviation"])
    del state["area_codes"]

with open("new_state.json","w") as f:
    json.dump(data,f,indent=2)


with urlopen("https://finance.yahoo.com/webservice/v1/symbols/allcurrencies/quote?format=json") as response:
    source = response.read()
data = json.loads(source)
print(json.dumps(data,indent=2))

usd_rate = {}
for item in data["list"]["resources"]:
    name = item["resource"]["fields"]["name"]
    price = item["resource"]["fields"]["price"]
    usd_rate[name] = price

print(usd_rate["USD/EUR"])
data = {"name":'Kamlesh',"city": "New York","population": 8000}
if "city" in data.keys():
    a = data.pop("city")
    data["location"] = a
print("dictionary after desired changes is:",data)
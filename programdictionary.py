marks={"Harry":100,
        "Darshan":200,
        "Rohan":300}
print(marks,type(marks))

print(marks["Darshan"])
print(marks.items())
print(marks.keys())
print(marks.values())
print(marks.get("Darshan")) 
print(marks.update({"Darshan":400}))
print(marks)

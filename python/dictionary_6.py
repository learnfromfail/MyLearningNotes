monthConversions = {
    "Jan": "January",
    "Feb": "February",
    "KeyMustBeUnquie" : "ValueNVM",
    123 : "hahah"
}

print(monthConversions["Feb"])
print(monthConversions["Jan"])
#print(monthConversions["notExisted"])
print(monthConversions.get("notExisted")) #none
print(monthConversions.get("notExisted", "Default Value")) 
print(monthConversions[123])
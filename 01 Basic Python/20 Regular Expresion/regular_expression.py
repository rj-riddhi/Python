import re

result = re.search("inform", "We need to inform him the latet informations.")
if result:
    print("There is inform")


result = re.findall("inform", "We need to inform him the latet informations.")
print(result)
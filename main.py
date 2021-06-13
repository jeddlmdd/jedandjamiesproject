 
import json
  
# Opening JSON file
f = open('matehi.json',)
  
# returns JSON object as 
# a dictionary
data = json.load(f)

print("I've imported some data")

# Closing file
f.close()

response = input("do you want to display data?")


jarman_height = data["jarman"]
print(jarman_height)

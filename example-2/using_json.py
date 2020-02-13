#%%
import json

#%%
with open("people.json") as input_file:
    content = json.load(input_file)
	
    print(content)
	
 
#%%
ramones = ["Johnny", "Joey", "Markee", "Dee dee"]

with open("ramones.json", "w") as output_file:
    json.dump(ramones, output_file)

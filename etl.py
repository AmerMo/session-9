#%%

import csv
import json


def load(filepath):
    
    result = []
    
    with open(filepath) as file:
        
        reader = csv.DictReader(file)

        for row in reader:
            
            result.append(row)
            
    return result


def transform(data):
    
    balances = {}
    
    for element in data:
        
        if element['state'] in balances:
            
            balances[element['state']].append(float(element['balance']))
            
        else:
            
            balances[element['state']] = [float(element['balance'])]
            
    for state in balances:
        balances[state] = sum(balances[state]) / len(balances[state])
    
    return balances


def sink(data):
    with open("output.json" , "w") as file:
        json.dump(data, file)


sink(transform(load("balances.csv")))
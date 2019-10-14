import json
with open('inventory.json') as f:
    data = json.load(f)

for inventory in data['inventory']:
    total = inventory['weight']*inventory['price_per_kg']
    print(inventory['name'],inventory['weight'] ,inventory['price_per_kg'],total)

# with open('new_inventory.json', 'w') as f:
#     json.dump(data,f, indent=2)
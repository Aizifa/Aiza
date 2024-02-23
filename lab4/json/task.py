import json
print('Interface Status')
print("================================================================================")
print(f'{'DN':<50} {'Description':<20} {'Speed':<10} {'MTU':<6}')
print('-------------------------------------------------- --------------------  ------  ------')
with open("sample", 'r') as obj:
    data = json.load(obj)
    for object in data['imdata']:
        dn = object["l1PhysIf"]["attributes"]["dn"]
        descr = object['l1PhysIf']['attributes']['descr']
        speed = object['l1PhysIf']['attributes']["speed"]
        mtu = object['l1PhysIf']['attributes']['mtu']
        
        print(f"{dn:<50}{descr:<20}{speed:<10}{mtu:<6}")
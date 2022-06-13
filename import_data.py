import json
f = open('seed_factory_data.json')
data = json.load(f)
print("INSERT INTO db.facotry_data \n(factory_id, sprocket_production_actual, sprocket_production_goal, `time`) VALUES")
count = 0
for i in data['factories']:
    count += 1
    x = i['factory']['chart_data']
    for u in range(len(x["sprocket_production_actual"])):
        print('(', count, ",")
        print(x["sprocket_production_actual"][u], ",")
        print(x["sprocket_production_goal"][u], ",")
        print(x["time"][u], "),")

f.close()

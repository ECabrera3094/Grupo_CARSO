
import datetime
import json
import pandas as pd

today = datetime.date.today() - datetime.timedelta(days=5)

print(today)



with open("test_data.json") as json_file:
    json_data = json.load(json_file)

    for i in json_data["a"]:
        print(i)


    print(json_data["a"])


#df = pd.read_json('test_data.json', lines=True, orient="columns") #, lines=True
#print(df)

#/html/body/div[2]/div/div/div/div/section/div/div[2]/div[1]/div/div[2]/div/section/div/div[2]/div/div/div/div/div[2]/div[2]/div[3]/div[1]/div[13]
#/html/body/div[2]/div/div/div/div/section/div/div[2]/div[1]/div/div[2]/div/section/div/div[2]/div/div/div/div/div[2]/div[2]/div[3]/div[1]/div[2]/div
#/html/body/div[2]/div/div/div/div/section/div/div[2]/div[1]/div/div[2]/div/section/div/div[2]/div/div/div/div/div[2]/div[2]/div[3]/div[2]/div/div/div[2]/div[4]/div/span/div/div/span/span/a/button
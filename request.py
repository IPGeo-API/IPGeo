import requests
import json
import ast
import pandas as pd

def flatten_json(nested_json):
    """
        Flatten json object with nested keys into a single level.
        Args:
            nested_json: A nested json object.
        Returns:
            The flattened json object if successful, None otherwise.
    """
    out = {}

    def flatten(x, name=''):
        if type(x) is dict:
            for a in x:
                flatten(x[a], name + a + '_')
        elif type(x) is list:
            i = 0
            for a in x:
                flatten(a, name + str(i) + '_')
                i += 1
        else:
            out[name[:-1]] = x

    flatten(nested_json)
    return out

url = 'https://ipgeo.azurewebsites.net/try'

with open('ipList.txt', 'r') as f:
    ipList = [line.strip() for line in f]
    f.close() 
"""
ipList = []
numberInput = int(input("How many IP searches would you like to make? "))
for x in range(numberInput):
    ip = input("Please Enter IPv4 request in x.x.x.x format. ")
    ipList.append(ip)
"""
for ip in ipList:
    ipsearch = "{\n\t\"ip\":\""+ip+"\"\n}"
    res = requests.post(url, data=ipsearch)
    res = res.text
    with open("results/json/result-ip-"+ip+".json", 'w') as result:
        result.write(res)
        result.close()
        with open("results/json/result-ip-"+ip+".json", 'r') as result:
            data = json.load(result)
            data = flatten_json(data)
            ipAddress = [""+ip+""]
            df = pd.Series(data).to_frame().T
            df['ip'] = ipAddress
            if set(['city_names_en','subdivisions_0_names_en']).issubset(df.columns):
                df = df[['ip','city_names_en','subdivisions_0_names_en','country_names_en','continent_names_en','location_latitude','location_longitude']]
                df = df.rename(columns={'city_names_en':'City','subdivisions_0_names_en':'State/Province','country_names_en':'Country','continent_names_en':'Continent',
                'location_latitude':'Latitude','location_longitude':'Longitude'})
            elif 'city_names_en' in df:
                df = df[['ip','city_names_en','country_names_en','continent_names_en','location_latitude','location_longitude']]
                df = df.rename(columns={'city_names_en':'City','country_names_en':'Country','continent_names_en':'Continent',
                'location_latitude':'Latitude','location_longitude':'Longitude'})
            elif 'subdivisions_0_names_en' in df:
                df = df[['ip','subdivisions_0_names_en','country_names_en','continent_names_en','location_latitude','location_longitude']]
                df = df.rename(columns={'subdivisions_0_names_en':'State/Province','country_names_en':'Country','continent_names_en':'Continent',
                'location_latitude':'Latitude','location_longitude':'Longitude'})
            else:
                df = df[['ip','country_names_en','continent_names_en','location_latitude','location_longitude']]
                df = df.rename(columns={'country_names_en':'Country','continent_names_en':'Continent',
                'location_latitude':'Latitude','location_longitude':'Longitude'})
            #df = df.dropna()
            df.to_csv(path_or_buf="results/csv/result-ip-"+ip+".csv", sep =',', index = False)
            result.close()


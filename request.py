import requests
import json
import ast
import pandas as pd
import time

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
#Sets Post URL
url = 'https://ipgeo.azurewebsites.net/try'

#opening list of IP's
with open('ipList.txt', 'r') as f:
    ipList = [line.strip() for line in f]
    f.close()
#checking if IP List is compatible with version
if len(ipList) > 10:
    print("Your IP List is longer than 10 entires, which is more than alloted for your version. Sending it would result in an error from the server.")
    print("Please shorten your list so that all your IP's may be processed.")
    time.sleep(5)
    exit()

#Recursively sending requests to the server
for ip in ipList:
    ipsearch = "{\n\t\"ip\":\""+ip+"\"\n}"
    authentication = {'Content-Type': "application/json"}
    res = requests.post(url, data=ipsearch, headers=authentication)
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
            #processing and removing unnecessary fields from the result
            if set(['city_names_en','subdivisions_0_names_en']).issubset(df.columns):
                df = df[['ip','city_names_en','subdivisions_0_names_en','country_names_en','continent_names_en','location_latitude','location_longitude',
                'autonomous_system_number','autonomous_system_organization','isp','organization','organization_type','isic_code','naics_code','connection_type'
                ,'ip_routing_type', 'line_speed']]
                df = df.rename(columns={'city_names_en':'City','subdivisions_0_names_en':'State/Province','country_names_en':'Country','continent_names_en':'Continent',
                'location_latitude':'Latitude','location_longitude':'Longitude','autonomous_system_number':'ASN','autonomous_system_organization':'ASO',
                'isp':'ISP', 'organization':'Organization','organization_type':'Organization Type','isic_code':'ISIC','naics_code':'NAICS'
                ,'connection_type':'Connection Type','ip_routing_type':'IP Routing Type','line_speed':'Line Speed'})
            elif 'city_names_en' in df:
                df = df[['ip','city_names_en','country_names_en','continent_names_en','location_latitude','location_longitude',
                'autonomous_system_number','autonomous_system_organization','isp','organization','organization_type','isic_code','naics_code','connection_type',
                'ip_routing_type','line_speed']]
                df = df.rename(columns={'city_names_en':'City','country_names_en':'Country','continent_names_en':'Continent',
                'location_latitude':'Latitude','location_longitude':'Longitude','autonomous_system_number':'ASN','autonomous_system_organization':'ASO',
                'isp':'ISP', 'organization':'Organization','organization_type':'Organization Type','isic_code':'ISIC','naics_code':'NAICS'
                ,'connection_type':'Connection Type','ip_routing_type':'IP Routing Type','line_speed':'Line Speed'})
            elif 'subdivisions_0_names_en' in df:
                df = df[['ip','subdivisions_0_names_en','country_names_en','continent_names_en','location_latitude','location_longitude',
                'autonomous_system_number','autonomous_system_organization','isp','organization','organization_type','isic_code','naics_code','connection_type',
                'ip_routing_type','line_speed']]
                df = df.rename(columns={'subdivisions_0_names_en':'State/Province','country_names_en':'Country','continent_names_en':'Continent',
                'location_latitude':'Latitude','location_longitude':'Longitude','autonomous_system_number':'ASN','autonomous_system_organization':'ASO',
                'isp':'ISP', 'organization':'Organization','organization_type':'Organization Type','isic_code':'ISIC','naics_code':'NAICS'
                ,'connection_type':'Connection Type','ip_routing_type':'IP Routing Type','line_speed':'Line Speed'})
            else:
                df = df[['ip','country_names_en','continent_names_en','location_latitude','location_longitude',
                'autonomous_system_number','autonomous_system_organization','isp','organization','organization_type','isic_code','naics_code','connection_type',
                'ip_routing_type','line_speed']]
                df = df.rename(columns={'country_names_en':'Country','continent_names_en':'Continent',
                'location_latitude':'Latitude','location_longitude':'Longitude','autonomous_system_number':'ASN','autonomous_system_organization':'ASO',
                'isp':'ISP', 'organization':'Organization','organization_type':'Organization Type','isic_code':'ISIC','naics_code':'NAICS'
                ,'connection_type':'Connection Type','ip_routing_type':'IP Routing Type','line_speed':'Line Speed'})
            df.to_csv(path_or_buf="results/csv/result-ip-"+ip+".csv", sep =',', index = False)
            result.close()


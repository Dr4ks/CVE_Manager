import json
import requests


def get_last_5_vulnerabilities(system_type,system_name,system_version):
    url=f"https://services.nvd.nist.gov/rest/json/cves/2.0?cpeName=cpe:2.3:{system_type}:{system_name}:{system_version}:*:*:*:*:*:*:*&resultsPerPage=5"

    response=requests.get(url=url)

    if response.status_code==200:
       data=response.json()
       return data["vulnerabilities"]
    else:
       return f"Error: {response.status_code}"


def read_systems_data(filename):
    with open('systems.json', 'r') as f:
        data = json.load(f)
    return data
         

def main():
    data=read_systems_data("systems.json")
    for item in data:

        vulnerabilities=get_last_5_vulnerabilities(item["type"],item["name"],item["version"])

        if len(vulnerabilities)>0:
            for vulnerability in vulnerabilities:
                print(f"Your system {item['type']}:{item['name']}:{item['version']} is vulnerable to {vulnerability['cve']['id']}")
        else:
            print(f"Your system {item['type']}:{item['name']}:{item['version']} is up2date, no worries!")
                
        
main()

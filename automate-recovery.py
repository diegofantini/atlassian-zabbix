import requests
import sys


authorization_token = "OAuth d0a2c12f14664f679a9249a05a104b59"

list_url = "https://api.statuspage.io/v1/pages/srf6g2y5xrnc/incidents"

headers = {
    "Authorization": authorization_token
}

def find_incident_id(name):
    response = requests.get(list_url, headers=headers)

    if response.status_code == 200:
        data = response.json()

        for incident in data:
            if incident["name"] == name and incident["status"] != "resolved":
                incident_id = incident["id"]
                return incident_id

        return None
    else:
        return None
    
def update_incident_status(incident_id, product_id):
    if incident_id:
        update_url = f"https://api.statuspage.io/v1/pages/srf6g2y5xrnc/incidents/{incident_id}"

        data = {
            "incident[status]": "resolved",
            f"incident[components][{product_id}]": "operational"
        }

        response = requests.patch(update_url, headers=headers, data=data)

name_tag = sys.argv[1] if len(sys.argv) > 1 else None
product_id_tag = sys.argv[2] if len(sys.argv) > 2 else None

incident_id = find_incident_id(name_tag)


if incident_id:
    update_incident_status(incident_id, product_id_tag)
else:
    print("Incidente não encontrado.")

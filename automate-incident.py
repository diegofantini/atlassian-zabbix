import requests
import sys

def create_incident(name, status, body, impact_override, client_id, product_id, damage):
    url = "https://api.statuspage.io/v1/pages/srf6g2y5xrnc/incidents"
    authorization_token = "OAuth d0a2c12f14664f679a9249a05a104b59"

    data = {
        "incident[name]": name,
        "incident[status]": status,
        "incident[body]": body,
        "incident[impact_override]": impact_override,
        "incident[component_ids]": client_id,
        f"incident[components][{product_id}]": damage
    }

    headers = {
        "Authorization": authorization_token
    }

    response = requests.post(url, headers=headers, data=data)


name_tag = sys.argv[1] if len(sys.argv) > 1 else None
status_tag = sys.argv[2] if len(sys.argv) > 2 else None
body_tag = sys.argv[3] if len(sys.argv) > 3 else None
impact_override_tag = sys.argv[4] if len(sys.argv) > 4 else None
client_id_tag = sys.argv[5] if len(sys.argv) > 5 else None
product_id_tag = sys.argv[6] if len(sys.argv) > 6 else None
damage_tag = sys.argv[7] if len(sys.argv) > 7 else None


if name_tag and status_tag and body_tag and impact_override_tag and product_id_tag:
    create_incident(name_tag, status_tag, body_tag, impact_override_tag, client_id_tag, product_id_tag, damage_tag)
else:
    print("Tags não fornecidas como argumentos.")

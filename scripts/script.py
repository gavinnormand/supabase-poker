import requests
import json

with open("sites.json", "r", encoding="utf-8") as file:
    sites = json.load(file)

for site in sites:
    url = f"https://{site['project_id']}.supabase.co/rest/v1/{site['table_name']}"

    headers = {
        "apikey": site["publishable_key"],
        "Authorization": f"Bearer {site['publishable_key']}",
        "Content-Type": "application/json",
    }

    response = requests.post(
        url,
        headers=headers,
        json={}
    )

    print(response.status_code)
    print(response.text)

    response.raise_for_status()

    print(f"Successfully posted to Supabase for {site['project_id']}!")
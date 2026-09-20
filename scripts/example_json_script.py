# 0 */4 * * * cd path_to_repo/supabase-poker && path_to_repo/supabase-poker/.venv/bin/python scripts/example_json_script.py >> path_to_repo/supabase-poker/cron.log 2>&1

import requests
import json

json_file_path = ... # INSERT YOUR JSON FILE PATH HERE

with open(json_file_path, "r", encoding="utf-8") as file:
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
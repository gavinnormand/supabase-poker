import requests

project_id = ... # INSERT YOUR PROJECT ID HERE
table_name = ... # INSERT YOUR LOGGING TABLE'S NAME HERE (IT MUST HAVE ONLY ID AND CREATED_AT)
publishable_key = ... # INSERT YOUR PUBLISHABLE API KEY HERE

url = f"https://{project_id}.supabase.co/rest/v1/{table_name}"

headers = {
    "apikey": publishable_key,
    "Authorization": f"Bearer {publishable_key}",
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

print("Successfully posted to Supabase!")
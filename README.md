# Supabase Poker

A lightweight Python script that periodically posts to multiple Supabase projects. Each site is configured in a local `sites.json` file, allowing a single cron job to update multiple Supabase tables on a schedule.

## How It Works

1. `sites.json` contains the Supabase project and table information for each site.
2. `json_script.py` loops through every configured site.
3. It sends a POST request to each site's Supabase REST API.
4. A cron job runs the script periodically.

## Setup

### 1. Clone the repository

```bash
git clone <your-repository-url>
cd supabase-poker
```

### 2. Create a virtual environment

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install requests
```

### 3. Configure `sites.json`

Create a `sites.json` file in the project root:

```json
[
  {
    "project_id": "your-project-id",
    "table_name": "logs",
    "publishable_key": "your-publishable-key"
  }
]
```

Multiple sites can be added:

```json
[
  {
    "project_id": "project-one",
    "table_name": "logs",
    "publishable_key": "key-one"
  },
  {
    "project_id": "project-two",
    "table_name": "logs",
    "publishable_key": "key-two"
  }
]
```

Do not use a Supabase secret or service-role key. This script is designed to use publishable keys.

Add `sites.json` to `.gitignore`:

```gitignore
.venv/
sites.json
```

### 4. Test the script

From the project root:

```bash
python scripts/json_script.py
```

## Running with Cron

Open your crontab:

```bash
crontab -e
```

To run the script every 4 hours:

```cron
0 */4 * * * cd /home/ubuntu/supabase-poker && /home/ubuntu/supabase-poker/.venv/bin/python scripts/json_script.py >> /home/ubuntu/supabase-poker/cron.log 2>&1
```

View your cron jobs:

```bash
crontab -l
```

View the script output:

```bash
cat ~/supabase-poker/cron.log
```
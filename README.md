# DeadlyRBot

DeadlyRBot is a Telegram bot that provides lecture timetables, reminders, and automated daily notifications. It is built using Python and integrates with the Telegram Bot API.

## Features
-  Fetch and display lecture timetables for specific days
-  Sends reminders 10 minutes before each lecture
-  Daily notification with the day's timetable
-  Built-in error handling and scheduling using APScheduler

## Installation

### Prerequisites
Ensure you have Python installed (>=3.9) and install required dependencies:

```sh
pip install -r requirements.txt
```

### Setting Up
1. Clone the repository:
   ```sh
   git clone https://github.com/rupak1005/deadlyBot.git
   cd deadlyBot
   ```

2. Create a `timetable.json` file in the project root with your schedule:
   ```json
   {
       "Monday": [
           { "time": "10:00 AM", "subject": "Math", "location": "Room 101" },
           { "time": "2:00 PM", "subject": "Physics", "location": "Room 202" }
       ],
       "Tuesday": [
           { "time": "11:00 AM", "subject": "Chemistry", "location": "Room 103" }
       ]
   }
   ```

3. Set your Telegram bot token as an environment variable:
   ```sh
   export TOKEN='your_telegram_bot_token'
   ```

4. Run the bot:
   ```sh
   python main.py
   ```

## Usage

### Commands:
- `/start` - Displays a welcome message
- `/timetable <day>` - Get the timetable for a specific day (e.g., `/timetable Monday`)
- `/help` - Shows available commands

## Deployment

### Deploy on Railway (Recommended)
1. Install Railway CLI:
   ```sh
   curl -fsSL https://railway.app/install.sh | sh
   ```
2. Login and initialize:
   ```sh
   railway login
   railway init
   ```
3. Deploy:
   ```sh
   railway up
   ```

### Deploy on Render.com
1. Connect your GitHub repo on [Render](https://render.com/)
2. Set the **Start Command** to:
   ```sh
   python main.py
   ```
3. Add an **environment variable** `TOKEN`
4. Click **Deploy**

## CI/CD Setup (GitHub Actions)
DeadlyRBot uses GitHub Actions to automate testing. Add the following workflow at `.github/workflows/test.yml`:

```yaml
name: CI/CD for DeadlyRBot

on: [push, pull_request]

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout Repository
        uses: actions/checkout@v2
      
      - name: Set up Python
        uses: actions/setup-python@v2
        with:
          python-version: '3.9'
      
      - name: Install Dependencies
        run: pip install -r requirements.txt
      
      - name: Run Unit Tests
        run: python -m unittest discover tests
```

## Contributing
Feel free to open issues or submit pull requests to improve DeadlyRBot!

## License
This project is licensed under the MIT License.


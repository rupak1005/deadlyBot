import json
import telebot
from datetime import datetime, timedelta
from apscheduler.schedulers.background import BackgroundScheduler

# Replace with your actual bot token
TOKEN = "7518216322:AAHfBgQhmJiL3NxBPv7B6wCPylL3c8h8Ov4"
bot = telebot.TeleBot(TOKEN)

# Scheduler for background tasks
scheduler = BackgroundScheduler()

def load_timetable():
    with open('timetable.json', 'r') as file:
        return json.load(file)

def send_daily_timetable(chat_id):
    today = datetime.now().strftime('%A')
    timetable = load_timetable()
    
    if today in timetable:
        response_message = f"Today's timetable for {today}:\n"
        for lecture in timetable[today]:
            response_message += f"{lecture['time']} - {lecture['subject']} ({lecture['location']})\n"
    else:
        response_message = f"Today is {today}, but there are no lectures scheduled."

    bot.send_message(chat_id, response_message)

def schedule_daily_notifications():
    # Set the time for daily notifications (e.g., 8 AM)
    scheduler.add_job(send_daily_timetable, 'cron', hour=8, minute=0, args=[5104491160])

@bot.message_handler(commands=['start', 'hello'])
def send_welcome(message):
    bot.reply_to(message, """It's deadlyR, deadlyR always deadly. 
    Available commands:
    
    /start - Welcome message
    /timetable - Get the timetable
    /help - Show this message
    """)

@bot.message_handler(commands=['help'])
def send_help(message):
    help_text = """
    Available commands:
    /start - Welcome message
    /timetable <day> - Get the timetable for a specific day (e.g., /timetable 21)
    /help - Show this message
    """
    bot.send_message(message.chat.id, help_text)

@bot.message_handler(commands=['timetable'])
def timetable(message):
    args = message.text.split()[1:]  # Get command arguments
    timetable = load_timetable()

    if args:
        try:
            day = int(args[0])  # Get the first argument as an integer
            date = datetime.now().replace(day=day)  # Set the current month and year
            day_name = date.strftime('%A')  # Get the name of the day
        except ValueError:
            bot.reply_to(message, "Invalid day format. Please use: /timetable <day>")
            return
        except Exception as e:
            bot.reply_to(message, str(e))
            return
    else:
        date = datetime.now()  # Default to today if no date provided
        day_name = date.strftime('%A')

    if day_name in timetable:
        response_message = f"Here’s the timetable for {day_name}, {date.strftime('%Y-%m-%d')}:\n"
        for lecture in timetable[day_name]:
            response_message += f"{lecture['time']} - {lecture['subject']} ({lecture['location']})\n"
            # Schedule a reminder 10 minutes before the lecture
            lecture_time = datetime.strptime(lecture['time'], '%I:%M %p')  # Adjust format as necessary
            reminder_time = (lecture_time - timedelta(minutes=10)).time()
            scheduler.add_job(send_reminder, 'cron', hour=reminder_time.hour, minute=reminder_time.minute, args=[message.chat.id, lecture])
    else:
        response_message = f"{day_name} is not a valid day, or there are no lectures scheduled."
    
    bot.reply_to(message, response_message)

def send_reminder(chat_id, lecture):
    message = f"Reminder: You have {lecture['subject']} at {lecture['time']} in {lecture['location']}."
    bot.send_message(chat_id, message)

# Start the scheduler
scheduler.start()

# Start polling
bot.polling(none_stop=True)

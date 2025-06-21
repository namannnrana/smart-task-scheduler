from datetime import datetime, timedelta
from plyer import notification
import os
import time

def schedule(task, days=0, hours=0, minutes=0, seconds=0):
    total_seconds = (days * 86400) + (hours * 3600) + (minutes * 60) + seconds
    target_time = datetime.now() + timedelta(seconds=total_seconds)

    if total_seconds <= 300:
        print(f"⏰ Setting notification for '{task}' at {target_time.strftime('%Y-%m-%d %H:%M:%S')}")
        time.sleep(total_seconds)
        notification.notify(
            title='Reminder',
            message=task,
            timeout=10
        )
    else:
        print(f"📅 Adding calendar event for '{task}' at {target_time.strftime('%Y-%m-%d %H:%M:%S')}")
        create_text_reminder(task, target_time)

def create_text_reminder(task, target_time):
    reminder_dir = os.path.expanduser("~/Reminders")
    if not os.path.exists(reminder_dir):
        os.makedirs(reminder_dir)
    
    filename = f"Reminder_{target_time.strftime('%Y-%m-%d_%H-%M')}.txt"
    filepath = os.path.join(reminder_dir, filename)

    with open(filepath, 'w') as f:
        f.write(f"REMINDER: {task}\n")
        f.write(f"TIME: {target_time.strftime('%Y-%m-%d %H:%M:%S')}\n")
        f.write("\nCreated by Python Reminder System\n")
    
    print(f"📝 Created text reminder at: {filepath}")
    print("Please check your reminders folder at:", reminder_dir)

from voice_input import get_voice_input
from whatsapp_messenger import send_whatsapp_message
from scheduler import schedule

def main():
    print("PRESS 1 FOR WHATSAPP MESSAGE \nPRESS 2 FOR SCHEDULING TASK")
    try:
        key = int(input("Enter your choice (1 or 2): "))
        if key == 1:
            number = input("ENTER YOUR NUMBER (with country code): ")
            message = get_voice_input()
            if not message:
                message = input("Voice failed. Please type your message: ")
            send_whatsapp_message(number, message)
        elif key == 2:
            task = input("ENTER THE TASK YOU WANT TO SCHEDULE: ")
            days = int(input("Enter number of days from now: "))
            hours = int(input("Enter number of hours from now: "))
            minutes = int(input("Enter number of minutes from now: "))
            seconds = int(input("Enter number of seconds from now: "))
            schedule(task, days, hours, minutes, seconds)
        else:
            print("INVALID CHOICE.")
    except ValueError:
        print("Please enter a valid number (1 or 2).")

if __name__ == "__main__":
    main()

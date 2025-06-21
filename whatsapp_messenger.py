import pywhatkit as wp

def send_whatsapp_message(phone_number, message):
    try:
        wp.sendwhatmsg_instantly(
            phone_no=phone_number,
            message=message,
            tab_close=True,
            close_time=3
        )
        print(f"Message sent to {phone_number}: {message}")
    except Exception as e:
        print(f"An error occurred: {e}")

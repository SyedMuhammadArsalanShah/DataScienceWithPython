import pywhatkit as kit
import pandas as pd
import time

# Load Excel File
df = pd.read_excel("Contacts.xlsx")  # Ensure contacts.xlsx has a column 'Phone'

# WhatsApp Group Invite Link
group_invite_link = ("https://chat.whatsapp.com/JJULI8qF7KyJesuxuYL1vH")



# Loop through each phone number and send the message
for index, row in df.iterrows():
    phone_number = f"+{row['Phone']}"  # Ensure phone numbers are in international format (e.g., +923001234567)
    message = f"""📢📢 Welcome to Your Official Batch Group!
    imp mujhy t nhi krni ap logon sse 
👉 Join the group now: {group_invite_link}
"""


    try:
        kit.sendwhatmsg_instantly(phone_number, message, wait_time=10)
        print(f"Message sent to {phone_number}")
        time.sleep(5)  # Add delay to avoid being flagged as spam
    except Exception as e:
        print(f"Failed to send message to {phone_number}: {e}")

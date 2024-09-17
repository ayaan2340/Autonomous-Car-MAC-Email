import smtplib
import uuid
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Function to get the MAC address
def get_mac_address():
    mac = hex(uuid.getnode()).replace('0x', '').upper()
    mac_address = ':'.join(mac[i:i+2] for i in range(0, 12, 2))
    return mac_address

# Function to send an email
def send_email(mac_address, sender_email, sender_password, receiver_email):
    try:
        # Create the email
        message = MIMEMultipart()
        message['From'] = sender_email
        message['To'] = receiver_email
        message['Subject'] = 'MAC Address'
        
        # Email body
        body = f'The MAC address of your system is: {mac_address}'
        message.attach(MIMEText(body, 'plain'))
        
        # Setting up the SMTP server
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()  # Start TLS encryption
        server.login(sender_email, sender_password)
        
        # Send the email
        server.sendmail(sender_email, receiver_email, message.as_string())
        server.quit()
        print("Email sent successfully!")
    
    except Exception as e:
        print(f"Failed to send email. Error: {str(e)}")

# Main function
def main():
    mac_address = get_mac_address()
    print(f"Your MAC address is: {mac_address}")

    # Sender's email credentials
    sender_email = 'ayaansunesara123@gmail.com'
    sender_password = 'qoxi wcix iuhu xnhg'  # Use app password if using Gmail

    # Receiver's email
    receiver_email = 'sahanagana@utexas.edu'  # You can send it to yourself

    # Send the email
    send_email(mac_address, sender_email, sender_password, receiver_email)

if __name__ == '__main__':
    main()

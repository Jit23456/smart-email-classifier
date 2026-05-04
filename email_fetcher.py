import imaplib
import email

def fetch_emails(username, password):
    mail = imaplib.IMAP4_SSL("imap.gmail.com")
    mail.login(username, password)
    mail.select("inbox")

    _, messages = mail.search(None, "ALL")
    email_list = []

    for num in messages[0].split()[-10:]:  # last 10 emails
        _, data = mail.fetch(num, "(RFC822)")
        msg = email.message_from_bytes(data[0][1])

        subject = msg["subject"]
        sender = msg["from"]

        email_list.append({
            "subject": subject,
            "sender": sender
        })

    return email_list
from django.core.mail import EmailMessage


def send_mail():
    email = EmailMessage('Subject', 'Body', to=['dkumar@ce.iitr.ac.in'])
    email.send()

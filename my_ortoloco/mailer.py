# -*- coding: utf-8 -*-

from django.conf import settings
from django.core import mail
from django.template.loader import get_template
from django.template import Context
from django.core.mail import EmailMultiAlternatives
import re


# sends mail only to specified email-addresses if dev mode
def send_mail(subject, message, from_email, to_emails, sendername):
    okmails = []
    if settings.DEBUG is False:
        okmails = to_emails
    else:
        for email in to_emails:
            sent = False
            for entry in settings.WHITELIST_EMAILS:
                if sent is False and re.match(entry, email):
                    sent = True
                    okmails.append(email)
            if not sent:
                print("Mail not sent to " + ", " + email + ", not in whitelist")

    if len(okmails) > 0:
        # only SERVER_EMAIL is allowed as sender. Workaround:
        if from_email == settings.SERVER_EMAIL:
            sender = settings.SERVER_EMAIL
        else:
            sender = sendername +' via my.mehalsgmues.ch <'+settings.SERVER_EMAIL+'>'
        # connect to server and send emails
        connection = mail.get_connection()
        connection.open()
        email = mail.EmailMessage(
            subject,
            message,
            sender,
            headers = {'Reply-To': from_email},
            connection = connection
        )
        for amail in okmails:
            email.to = [amail]
            email.send()
        connection.close()
        print("Mail sent to " + ", ".join(okmails) + (", on whitelist" if settings.DEBUG else ""))

    return None


def send_mail_multi(email_multi_message):
    okmails = []
    if settings.DEBUG is False:
        okmails = email_multi_message.to
    else:
        for email in email_multi_message.to:
            sent = False
            for entry in settings.WHITELIST_EMAILS:
                if sent is False and re.match(entry, email):
                    sent = True
                    okmails.append(email)
            if not sent:
                print("Mail not sent to " + email + ", not in whitelist")

    if len(okmails) > 0:
        # only SERVER_EMAIL is allowed as sender. Workaround:
        if email_multi_message.from_email != settings.SERVER_EMAIL:
            email_multi_message.headers = {'Reply-To': email_multi_message.from_email},
            email_multi_message.from_email = email_multi_message.from_email.replace('@',' at ') +' via my.mehalsgmues.ch <'+settings.SERVER_EMAIL+'>'
        email_multi_message.to = []
        email_multi_message.bcc = okmails
        email_multi_message.send()
        print("Mail sent to " + ", ".join(okmails) + (", on whitelist" if settings.DEBUG else ""))
    return None


def send_new_loco_in_taetigkeitsbereich_to_bg(area, loco):
    print( "new_loco_in_taetigkeitsbereich_to_bg emails are disabled for now" )
    return
    send_mail('Neues Mitglied im Taetigkeitsbereich ' + area.name,
              'Soeben hat sich ' + loco.first_name + " " + loco.last_name + ' in den Taetigkeitsbereich ' + area.name + ' eingetragen', settings.SERVER_EMAIL, [area.coordinator.email])


def send_contact_form(subject, message, loco, copy_to_loco):
    send_mail('Anfrage per my.mehalsgmues: ' + subject, message, loco.email, [settings.SERVER_EMAIL], loco.first_name + ' ' + loco.last_name)
    if copy_to_loco:
        send_mail('Anfrage per my.mehalsgmues: ' + subject, message, loco.email, [loco.email], loco.first_name + ' ' + loco.last_name)

def send_contact_loco_form(subject, message, loco, contact_loco, copy_to_loco):
    send_mail('Nachricht per my.mehalsgmues: ' + subject, message, loco.email, [contact_loco.email], loco.first_name + ' ' + loco.last_name)
    if copy_to_loco:
        send_mail('Nachricht per my.mehalsgmues: ' + subject, message, loco.email, [loco.email], loco.first_name + ' ' + loco.last_name)


def send_welcome_mail(email, password, server):
    print( "welcome emails are disabled for now" )
    return
    plaintext = get_template('mails/welcome_mail.txt')
    htmly = get_template('mails/welcome_mail.html')

    # reset password so we can send it to him
    d = Context({
        'subject': 'Willkommen bei meh als gmues',
        'username': email,
        'password': password,
        'serverurl': "http://" + server
    })

    text_content = plaintext.render(d)
    html_content = htmly.render(d)

    msg = EmailMultiAlternatives('Willkommen bei meh als gmues', text_content, settings.SERVER_EMAIL, [email])
    msg.attach_alternative(html_content, "text/html")
    send_mail_multi(msg)


def send_been_added_to_abo(email, password, name, anteilsscheine, hash, server):
    print( "been_added_to_abo emails are disabled for now" )
    return
    plaintext = get_template('mails/welcome_added_mail.txt')
    htmly = get_template('mails/welcome_added_mail.html')

    # reset password so we can send it to him
    d = Context({
        'subject': 'Willkommen bei meh als gmues',
        'username': email,
        'name': name,
        'password': password,
        'hash': hash,
        'anteilsscheine': anteilsscheine,
        'serverurl': "http://" + server
    })

    text_content = plaintext.render(d)
    html_content = htmly.render(d)

    msg = EmailMultiAlternatives('Willkommen bei meh als gmues', text_content, settings.SERVER_EMAIL, [email])
    msg.attach_alternative(html_content, "text/html")
    send_mail_multi(msg)


def send_filtered_mail(subject, message, text_message, emails, server, attachments, sender):
    plaintext = get_template('mails/filtered_mail.txt')
    htmly = get_template('mails/filtered_mail.html')

    htmld = Context({
        'subject': subject,
        'content': message,
        'serverurl': "http://" + server
    })
    textd = Context({
        'subject': subject,
        'content': text_message,
        'serverurl': "http://" + server
    })

    text_content = plaintext.render(textd)
    html_content = htmly.render(htmld)

    msg = EmailMultiAlternatives(subject, text_content, sender, emails, headers={'Reply-To': sender})
    msg.attach_alternative(html_content, "text/html")
    for attachment in attachments:
        msg.attach(attachment.name, attachment.read())
    send_mail_multi(msg)
    

def send_mail_password_reset(email, password, server):
    plaintext = get_template('mails/password_reset_mail.txt')
    htmly = get_template('mails/password_reset_mail.html')
    subject = 'Dein neues meh als gmues Passwort'

    htmld = Context({
        'subject': subject,
        'email': email,
        'password': password,
        'serverurl': "http://" + server
    })
    textd = Context({
        'subject': subject,
        'email': email,
        'password': password,
        'serverurl': "http://" + server
    })

    text_content = plaintext.render(textd)
    html_content = htmly.render(htmld)

    msg = EmailMultiAlternatives(subject, text_content, settings.SERVER_EMAIL, [email])
    msg.attach_alternative(html_content, "text/html")
    send_mail_multi(msg)


def send_job_reminder(emails, job, participants, server):
    print( "Job reminder emails are disabled for now" )
    return
    plaintext = get_template('mails/job_reminder_mail.txt')
    htmly = get_template('mails/job_reminder_mail.html')

    d = Context({
        'job': job,
        'participants': participants,
        'serverurl': "http://" + server
    })

    text_content = plaintext.render(d)
    html_content = htmly.render(d)

    msg = EmailMultiAlternatives("meh als gmües - Job-Erinnerung", text_content, settings.SERVER_EMAIL, emails)
    msg.attach_alternative(html_content, "text/html")
    send_mail_multi(msg)

def send_job_canceled(emails, job):
    print( "Job canceled emails are disabled for now" )
    return
    plaintext = get_template('mails/job_canceled_mail.txt')
    htmly = get_template('mails/job_canceled_mail.html')

    d = Context({
        'job': job
    })

    text_content = plaintext.render(d)
    html_content = htmly.render(d)

    msg = EmailMultiAlternatives("meh als gmües - Job-Abgesagt", text_content, settings.SERVER_EMAIL, emails)
    msg.attach_alternative(html_content, "text/html")
    send_mail_multi(msg)

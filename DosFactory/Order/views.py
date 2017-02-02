from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import json
import smtplib
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

# Create your views here.
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import View
from DosFactory.settings import SMTP_SERVER, SMTP_PORT


class PlaceOrder(View):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super(PlaceOrder, self).dispatch(request, *args, **kwargs)

    def post(self, request):
        data = {}
        request_data = request.body
        self.send_mail("request_data", request_data, ['kokku2chiranjeevi@gmail.com', 'adithya.raju7@gmail.com'])
        data["fulifilments"] = {"speech": "sadagshdgajsgd"}
        return JsonResponse(data)

    def send_mail(self, subject, body, receiver_list):
        mail_user = "kokku2chiranjeevi"
        mail_pwd = "aLLisweLL"
        from_id = mail_user
        to_ids = receiver_list
        message = MIMEMultipart('alternative')
        message['Subject'] = subject
        message['From'] = 'CustomFurnish <'+from_id+'>'
        message['To'] = to_ids[0]
        part2 = MIMEText(body, 'html')
        message.attach(part2)
        smtp_server = SMTP_SERVER
        smtp_port = SMTP_PORT
        try:
            server = smtplib.SMTP(smtp_server, smtp_port)
            server.ehlo()
            server.starttls()
            server.login(mail_user, mail_pwd)
            server.sendmail(from_id, to_ids, message.as_string())
            server.quit()
            return "Success fully mail sent"
        except Exception as e:
            return "Failed sending mail to {0} Exception {1}".format(receiver_list,str(e))
import base64
import inspect
import logging
import smtplib
import os

import pytest

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build


@pytest.mark.usefixtures("setup")
class TestUtilities:
    # Defining the logging mechanism
    def get_logger(self):
        logger_name = inspect.stack()[1][3]
        logger = logging.getLogger(logger_name)

        file_handler = logging.FileHandler("reports/logs/logfile.log")

        formatter = logging.Formatter("%(asctime)s : %(levelname)s : %(name)s : %(message)s")

        file_handler.setFormatter(formatter)

        logger.addHandler(file_handler)

        logger.setLevel(logging.INFO)

        return logger

    def send_email_with_html_report(self):
        credentials = Credentials.from_authorized_user_info(info={
            "client_id": "486964041533-59lr2j1ekopci9t81cnbi5lvn9aj3b3u.apps.googleusercontent.com",
            "client_secret": "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",
            "token_uri": "https://oauth2.googleapis.com/token",
            "scopes": ["https://www.googleapis.com/auth/gmail.send"]
        })

        receiver_address = "eghitta@mozilla.org"
        message = MIMEMultipart()
        message['To'] = receiver_address
        message['Subject'] = 'Selenium Test Execution - Report'
        body = "Please take a look at the attached Selenium Test Report for details"

        try:
            service = build("gmail", "v1", credentials=credentials)
            message.attach(MIMEText(body, 'plain'))

            # report_dir = os.environ['GITHUB_WORKSPACE'] + '/reports'
            report_dir = "reports/"
            report_filename = 'report.html'
            report_path = os.path.join(report_dir, report_filename)
            with open(report_path, 'rb') as f:
                attach_report = MIMEApplication(f.read(), _subtype='html')
                attach_report.add_header('Content-Disposition', 'attachment', filename=report_filename)
            message.attach(attach_report)
            create_message = {'raw': base64.urlsafe_b64encode(message.as_bytes()).decode()}
            send_message = service.users().messages().send(userId='me', body = create_message).execute()
        except Exception as e:
            print("An error has occurred while sending the email")


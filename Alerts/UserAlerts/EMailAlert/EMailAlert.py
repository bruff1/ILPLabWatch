from Alerts.AbstractAlert import AbstractAlert
import datetime, smtplib
from email.mime.text import MIMEText
from email.header import Header

class EMailAlert(AbstractAlert):
    """Diese Klasse gibt eine Nachricht auf der Konsole aus, sobald der Alert aufgerufen wird."""

    lastCalled = 0

    def __init__(self, alertID, settings):
        self.lastCalled = datetime.datetime.now() + datetime.timedelta(minutes=-5)
        super().__init__(alertID, settings)

    # erzeugt einen neuen Alert in der Command Line.
    def throwAlert(self, port, trigger):
        td = datetime.timedelta(minutes=-5)
        if self.lastCalled < datetime.datetime.now() + td:
            smtp = smtplib.SMTP()
            smtp.connect(host=self.getSetting('SMTPServerAddress'), port=self.getSetting('SMTPServerPort'))
            if self.getSetting('SMTPUsername') != "":
                smtp.login(user=self.getSetting('SMTPUsername'), password=self.getSetting('SMTPPassword'))

            for address in self.getSetting('sendTo').split(';'):
                to = address.strip()
                self.sendMail(to, port, smtp)
            self.lastCalled = datetime.datetime.now()
            smtp.quit()

    # gibt die Beschreibung des Alerts aus.
    def getDescription(self):
        return "Ein E-Mail-Alert sendet eine E-Mail an einen oder mehre Empfänger, wenn der Trigger das erste Mal auslöst."

    def sendMail(self, to, port, smtp):
        """Sendet eine Email an einen Empfänger"""
        content = "Alert vom Port "+port.getName()+" ausgelöst \n Der Wert vom Port betrug: "+port.getStateWithUnit()+" \n Zusätzliche Nachricht: "+self.getSetting('message')+" \n Zeitpunkt: " + datetime.datetime.now().strftime("%d.%m.%Y %H:%M:%S")
        message = MIMEText(content.encode('utf-8'), 'plain', 'utf-8')
        message['From'] = 'ILPLabWatch'
        message['To'] = to
        message['Subject'] = Header("ILPLabWatch Alert ausgelöst", 'utf-8')

        try:
            smtp.sendmail('noReply@ILPLabWatch.uni-hamburg.de', to, message.as_string())
        except:
            print("Senden der E-Mails fehlgeschlagen!")
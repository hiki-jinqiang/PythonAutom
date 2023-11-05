from email.mime.text import MIMEText
import smtplib

def mailToME(Title,EmailText):
    #Sendemail information
    SendEmail = "SendEemail@163.com"
    SendEmailPassword = 'PeimitCode'
    #Send content information
    Subject = Title
    Content = EmailText
    message = MIMEText(Content,"plain","utf-8")  #context style translate utf-8
    #Receive email information
    ReceiveEmail = "ReceiveEmail@qq.com"

    #give real email value
    message['Subject'] = Subject
    message['To'] = ReceiveEmail
    message['From'] = SendEmail

    #start a smtp server
    smtp = smtplib.SMTP_SSL("smtp.163.com",994)
    smtp.login(SendEmail,SendEmailPassword)
   
    smtp.sendmail(SendEmail,[ReceiveEmail],message.as_string())
    smtp.close()
    print("send email success")
    return 1
if __name__ == "__main__":
   mailToME('Test','success')
import win32com.client as win32


# criar a integração com o outlook
outlook = win32.Dispatch("outlook.application") 

#criar email
email = outlook.CreateItem(0)

email.To = "email que queira enviar"
email.Subject = "Email automático do Python"
email.HTMLBody = """

<p-----</p>

<p>-----</p>
<p>------<p>

<p>--------</p>
<p>---------</p>
"""

email.Send()

print("Email enviado!")


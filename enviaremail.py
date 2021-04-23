import win32com.client as win32


# criar a integração com o outlook
outlook = win32.Dispatch("outlook.application") 

#criar email
email = outlook.CreateItem(0)

email.To = "antonio.lima@ibyte.com.br; ealves@ibyte.com.br"
email.Subject = "Email automático do Python"
email.HTMLBody = """

<p>Olá Igor, aqui é o código python!</p>

<p>Se liga nesse email automa tizado</p>
<p>EAI MEU CHAPA<p>

<p>Atenciosamente,</p>
<p>DEVigor</p>
"""

email.Send()

print("Email enviado!")


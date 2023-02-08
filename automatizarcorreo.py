
#Importar librerías
from email.message import EmailMessage
import ssl
import smtplib


#Definir email
email_emisor = 'ced.villalbaag@gmail.com'
email_contrasena = 'ixpobiitxnqalqgj'

email_receptor = 'carlosv2806@gmail.com'


#Crear el correo 
asunto = 'Correo Prueba - Python'
cuerpo = 'He desarrollado este nuevo codigo desde YT'


#Crear una instancia para email message
em = EmailMessage()
em['From'] = email_emisor
em['To'] = email_receptor
em['Subject'] = asunto
em.set_content(cuerpo)



#Agregar seguridad
contexto = ssl.create_default_context()


with smtplib.SMTP_SSL('smtp.gmail.com', 465, context = contexto) as smtp:
	smtp.login(email_emisor, email_contrasena)
	smtp.sendmail(email_emisor, email_receptor, em.as_string())
    

print('Correo enviado exitosamente')
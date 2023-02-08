#Importar librerías
from email.message import EmailMessage
import ssl
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email import encoders
from email.mime.base import MIMEBase


#Definir email
email_emisor = 'ced.villalbaag@gmail.com'
email_contrasena = 'ixpobiitxnqalqgj'

email_receptor = 'carlosv2806@gmail.com'


#Crear el correo 
asunto = 'Correo Prueba - Python'

cuerpo = MIMEMultipart('Alternative')
#Definir el mensaje
html = f"""
<html>
<body>
<b>Titulo del correo</b> <br>

<p>Hola esta es una prueba<p>
</body>
</html>

"""


# Definir el contenido del mensaje como html
parte_html = MIMEText(html,"html")


# Agregar ese contenido al mensaje
cuerpo.attach(parte_html)


#Agregar archivo adjunto
archivo = "descarga.png"

with open(archivo, "rb") as adjunto:
	contenido_adjunto = MIMEBase("application", "octet-stream")
contenido_adjunto.set_payload(adjunto.read())

encoders.encode_base64(contenido_adjunto)

contenido_adjunto.add_header(
    "Content_Disposition",
	f"attachment; filename= {archivo}",
    )

mensaje.attach(contenido_adjunto)


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
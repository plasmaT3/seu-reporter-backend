import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

EMAIL_ORIGEM = "newsletter@seuredator.com.br"
SENHA = "P3p3cud0@@@"  # substitua aqui pela senha que você criou

SMTP_SERVER = "smtp.seuredator.com.br"  # ou smtp.hostgator.com, confirme no painel
SMTP_PORT = 587  # Porta TLS padrão

def enviar_email(destinatario, assunto, corpo_html):
    msg = MIMEMultipart()
    msg['From'] = EMAIL_ORIGEM
    msg['To'] = destinatario
    msg['Subject'] = assunto

    msg.attach(MIMEText(corpo_html, 'html'))

    try:
        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        server.starttls()  # ativa TLS
        server.login(EMAIL_ORIGEM, SENHA)
        server.sendmail(EMAIL_ORIGEM, destinatario, msg.as_string())
        server.quit()
        print("E-mail enviado com sucesso!")
    except Exception as e:
        print(f"Erro ao enviar e-mail: {e}")

# Exemplo de uso:
# enviar_email("destino@exemplo.com", "Teste Newsletter", "<h1>Olá, leitor!</h1><p>Este é um teste.</p>")


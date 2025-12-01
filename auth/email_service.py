#!/usr/bin/env python3
"""
Serviço de Email para Sistema de Autenticação
Envia notificações por email quando eventos importantes acontecem
"""

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from datetime import datetime
from typing import Optional
import os


class EmailConfig:
    """Configurações de email"""

    # Configurações SMTP (Gmail como exemplo)
    # Para usar Gmail, você precisa:
    # 1. Habilitar autenticação de dois fatores
    # 2. Gerar uma "Senha de App" em https://myaccount.google.com/apppasswords
    SMTP_SERVER = os.environ.get('SMTP_SERVER', 'smtp.gmail.com')
    SMTP_PORT = int(os.environ.get('SMTP_PORT', 587))
    SMTP_USERNAME = os.environ.get('SMTP_USERNAME', 'seu_email@gmail.com')
    SMTP_PASSWORD = os.environ.get('SMTP_PASSWORD', 'sua_senha_de_app')

    # Email do remetente
    FROM_EMAIL = os.environ.get('FROM_EMAIL', SMTP_USERNAME)
    FROM_NAME = os.environ.get('FROM_NAME', 'Sistema de Autenticação')

    # Email do administrador (para receber notificações)
    ADMIN_EMAIL = os.environ.get('ADMIN_EMAIL', 'admin@example.com')

    # Habilitar/desabilitar envio de emails
    EMAIL_ENABLED = os.environ.get('EMAIL_ENABLED', 'false').lower() == 'true'


class EmailService:
    """Serviço para envio de emails"""

    def __init__(self, config: EmailConfig = EmailConfig()):
        self.config = config

    def _create_message(self, to_email: str, subject: str, html_content: str, text_content: Optional[str] = None) -> MIMEMultipart:
        """
        Cria uma mensagem de email

        Args:
            to_email: Email do destinatário
            subject: Assunto do email
            html_content: Conteúdo HTML do email
            text_content: Conteúdo em texto plano (opcional)

        Returns:
            Mensagem MIME configurada
        """
        message = MIMEMultipart('alternative')
        message['From'] = f"{self.config.FROM_NAME} <{self.config.FROM_EMAIL}>"
        message['To'] = to_email
        message['Subject'] = subject

        # Adicionar versão em texto plano
        if text_content:
            part1 = MIMEText(text_content, 'plain')
            message.attach(part1)

        # Adicionar versão HTML
        part2 = MIMEText(html_content, 'html')
        message.attach(part2)

        return message

    def _send_email(self, message: MIMEMultipart) -> bool:
        """
        Envia um email via SMTP

        Args:
            message: Mensagem MIME a ser enviada

        Returns:
            True se o email foi enviado com sucesso, False caso contrário
        """
        if not self.config.EMAIL_ENABLED:
            print(f"[EMAIL] Envio de emails desabilitado. Email para {message['To']} não foi enviado.")
            print(f"[EMAIL] Assunto: {message['Subject']}")
            return False

        try:
            # Conectar ao servidor SMTP
            with smtplib.SMTP(self.config.SMTP_SERVER, self.config.SMTP_PORT) as server:
                server.starttls()  # Habilitar TLS
                server.login(self.config.SMTP_USERNAME, self.config.SMTP_PASSWORD)

                # Enviar email
                server.send_message(message)

            print(f"[EMAIL] Email enviado com sucesso para {message['To']}")
            return True

        except smtplib.SMTPAuthenticationError:
            print(f"[EMAIL] Erro de autenticação SMTP. Verifique suas credenciais.")
            return False
        except smtplib.SMTPException as e:
            print(f"[EMAIL] Erro ao enviar email: {e}")
            return False
        except Exception as e:
            print(f"[EMAIL] Erro inesperado: {e}")
            return False

    def send_registration_notification_to_admin(self, username: str, email: str, role: str) -> bool:
        """
        Envia notificação para o admin quando um novo usuário se cadastra

        Args:
            username: Nome de usuário do novo cadastro
            email: Email do novo usuário
            role: Papel/função do novo usuário

        Returns:
            True se o email foi enviado com sucesso, False caso contrário
        """
        subject = f"Novo Cadastro: {username}"

        # Conteúdo HTML
        html_content = f"""
        <!DOCTYPE html>
        <html>
        <head>
            <style>
                body {{
                    font-family: Arial, sans-serif;
                    line-height: 1.6;
                    color: #333;
                }}
                .container {{
                    max-width: 600px;
                    margin: 0 auto;
                    padding: 20px;
                    background-color: #f4f4f4;
                }}
                .content {{
                    background-color: white;
                    padding: 30px;
                    border-radius: 5px;
                    box-shadow: 0 2px 5px rgba(0,0,0,0.1);
                }}
                .header {{
                    background-color: #4CAF50;
                    color: white;
                    padding: 20px;
                    text-align: center;
                    border-radius: 5px 5px 0 0;
                }}
                .info-box {{
                    background-color: #f9f9f9;
                    border-left: 4px solid #4CAF50;
                    padding: 15px;
                    margin: 20px 0;
                }}
                .footer {{
                    text-align: center;
                    margin-top: 20px;
                    color: #666;
                    font-size: 12px;
                }}
            </style>
        </head>
        <body>
            <div class="container">
                <div class="content">
                    <div class="header">
                        <h1>Novo Usuário Cadastrado</h1>
                    </div>

                    <p>Olá Administrador,</p>

                    <p>Um novo usuário acabou de se cadastrar no sistema.</p>

                    <div class="info-box">
                        <h3>Detalhes do Cadastro:</h3>
                        <p><strong>Nome de usuário:</strong> {username}</p>
                        <p><strong>Email:</strong> {email}</p>
                        <p><strong>Papel/Função:</strong> {role}</p>
                        <p><strong>Data/Hora:</strong> {datetime.now().strftime('%d/%m/%Y às %H:%M:%S')}</p>
                    </div>

                    <p>Este é um email automático de notificação. Você pode revisar o novo cadastro no painel administrativo.</p>

                    <div class="footer">
                        <p>Sistema de Autenticação via Token JWT</p>
                        <p>Este é um email automático, não responda.</p>
                    </div>
                </div>
            </div>
        </body>
        </html>
        """

        # Conteúdo em texto plano
        text_content = f"""
        Novo Usuário Cadastrado

        Olá Administrador,

        Um novo usuário acabou de se cadastrar no sistema.

        Detalhes do Cadastro:
        - Nome de usuário: {username}
        - Email: {email}
        - Papel/Função: {role}
        - Data/Hora: {datetime.now().strftime('%d/%m/%Y às %H:%M:%S')}

        Este é um email automático de notificação.

        Sistema de Autenticação via Token JWT
        """

        message = self._create_message(
            to_email=self.config.ADMIN_EMAIL,
            subject=subject,
            html_content=html_content,
            text_content=text_content
        )

        return self._send_email(message)

    def send_welcome_email(self, username: str, email: str) -> bool:
        """
        Envia email de boas-vindas para o novo usuário

        Args:
            username: Nome de usuário
            email: Email do usuário

        Returns:
            True se o email foi enviado com sucesso, False caso contrário
        """
        subject = f"Bem-vindo ao Sistema, {username}!"

        # Conteúdo HTML
        html_content = f"""
        <!DOCTYPE html>
        <html>
        <head>
            <style>
                body {{
                    font-family: Arial, sans-serif;
                    line-height: 1.6;
                    color: #333;
                }}
                .container {{
                    max-width: 600px;
                    margin: 0 auto;
                    padding: 20px;
                    background-color: #f4f4f4;
                }}
                .content {{
                    background-color: white;
                    padding: 30px;
                    border-radius: 5px;
                    box-shadow: 0 2px 5px rgba(0,0,0,0.1);
                }}
                .header {{
                    background-color: #2196F3;
                    color: white;
                    padding: 20px;
                    text-align: center;
                    border-radius: 5px 5px 0 0;
                }}
                .button {{
                    display: inline-block;
                    padding: 12px 24px;
                    background-color: #2196F3;
                    color: white;
                    text-decoration: none;
                    border-radius: 5px;
                    margin: 20px 0;
                }}
                .footer {{
                    text-align: center;
                    margin-top: 20px;
                    color: #666;
                    font-size: 12px;
                }}
            </style>
        </head>
        <body>
            <div class="container">
                <div class="content">
                    <div class="header">
                        <h1>Bem-vindo!</h1>
                    </div>

                    <p>Olá {username},</p>

                    <p>Seja muito bem-vindo ao nosso sistema! Seu cadastro foi realizado com sucesso.</p>

                    <p>Agora você já pode fazer login e começar a usar todas as funcionalidades disponíveis.</p>

                    <p><strong>Seus dados de acesso:</strong></p>
                    <ul>
                        <li><strong>Nome de usuário:</strong> {username}</li>
                        <li><strong>Email:</strong> {email}</li>
                    </ul>

                    <p>Se você não realizou este cadastro, por favor entre em contato conosco imediatamente.</p>

                    <div class="footer">
                        <p>Sistema de Autenticação via Token JWT</p>
                        <p>Este é um email automático, não responda.</p>
                    </div>
                </div>
            </div>
        </body>
        </html>
        """

        # Conteúdo em texto plano
        text_content = f"""
        Bem-vindo!

        Olá {username},

        Seja muito bem-vindo ao nosso sistema! Seu cadastro foi realizado com sucesso.

        Agora você já pode fazer login e começar a usar todas as funcionalidades disponíveis.

        Seus dados de acesso:
        - Nome de usuário: {username}
        - Email: {email}

        Se você não realizou este cadastro, por favor entre em contato conosco imediatamente.

        Sistema de Autenticação via Token JWT
        """

        message = self._create_message(
            to_email=email,
            subject=subject,
            html_content=html_content,
            text_content=text_content
        )

        return self._send_email(message)

    def send_login_notification(self, username: str, email: str, ip_address: str = "N/A") -> bool:
        """
        Envia notificação de login para o usuário

        Args:
            username: Nome de usuário
            email: Email do usuário
            ip_address: Endereço IP do login

        Returns:
            True se o email foi enviado com sucesso, False caso contrário
        """
        subject = f"Novo login detectado - {username}"

        # Conteúdo HTML
        html_content = f"""
        <!DOCTYPE html>
        <html>
        <head>
            <style>
                body {{
                    font-family: Arial, sans-serif;
                    line-height: 1.6;
                    color: #333;
                }}
                .container {{
                    max-width: 600px;
                    margin: 0 auto;
                    padding: 20px;
                    background-color: #f4f4f4;
                }}
                .content {{
                    background-color: white;
                    padding: 30px;
                    border-radius: 5px;
                    box-shadow: 0 2px 5px rgba(0,0,0,0.1);
                }}
                .header {{
                    background-color: #FF9800;
                    color: white;
                    padding: 20px;
                    text-align: center;
                    border-radius: 5px 5px 0 0;
                }}
                .warning {{
                    background-color: #fff3cd;
                    border-left: 4px solid #ffc107;
                    padding: 15px;
                    margin: 20px 0;
                }}
                .footer {{
                    text-align: center;
                    margin-top: 20px;
                    color: #666;
                    font-size: 12px;
                }}
            </style>
        </head>
        <body>
            <div class="container">
                <div class="content">
                    <div class="header">
                        <h1>Novo Login Detectado</h1>
                    </div>

                    <p>Olá {username},</p>

                    <p>Detectamos um novo login em sua conta.</p>

                    <p><strong>Detalhes do Login:</strong></p>
                    <ul>
                        <li><strong>Data/Hora:</strong> {datetime.now().strftime('%d/%m/%Y às %H:%M:%S')}</li>
                        <li><strong>Endereço IP:</strong> {ip_address}</li>
                    </ul>

                    <div class="warning">
                        <strong>Não foi você?</strong>
                        <p>Se você não reconhece este login, recomendamos que altere sua senha imediatamente e entre em contato conosco.</p>
                    </div>

                    <div class="footer">
                        <p>Sistema de Autenticação via Token JWT</p>
                        <p>Este é um email automático, não responda.</p>
                    </div>
                </div>
            </div>
        </body>
        </html>
        """

        # Conteúdo em texto plano
        text_content = f"""
        Novo Login Detectado

        Olá {username},

        Detectamos um novo login em sua conta.

        Detalhes do Login:
        - Data/Hora: {datetime.now().strftime('%d/%m/%Y às %H:%M:%S')}
        - Endereço IP: {ip_address}

        Não foi você?
        Se você não reconhece este login, recomendamos que altere sua senha imediatamente e entre em contato conosco.

        Sistema de Autenticação via Token JWT
        """

        message = self._create_message(
            to_email=email,
            subject=subject,
            html_content=html_content,
            text_content=text_content
        )

        return self._send_email(message)


# Instância global do serviço de email
email_service = EmailService()


if __name__ == "__main__":
    """Demonstração do serviço de email"""
    print("=" * 80)
    print("Serviço de Email - Demonstração")
    print("=" * 80)

    print("\nConfigurações atuais:")
    print(f"  SMTP Server: {EmailConfig.SMTP_SERVER}:{EmailConfig.SMTP_PORT}")
    print(f"  From Email: {EmailConfig.FROM_EMAIL}")
    print(f"  Admin Email: {EmailConfig.ADMIN_EMAIL}")
    print(f"  Email Enabled: {EmailConfig.EMAIL_ENABLED}")

    if not EmailConfig.EMAIL_ENABLED:
        print("\n" + "!" * 80)
        print("AVISO: Envio de emails está DESABILITADO")
        print("Para habilitar, configure EMAIL_ENABLED=true nas variáveis de ambiente")
        print("!" * 80)

    print("\n--- Teste 1: Notificação de Cadastro para Admin ---")
    email_service.send_registration_notification_to_admin(
        username="teste_usuario",
        email="teste@example.com",
        role="user"
    )

    print("\n--- Teste 2: Email de Boas-vindas ---")
    email_service.send_welcome_email(
        username="teste_usuario",
        email="teste@example.com"
    )

    print("\n--- Teste 3: Notificação de Login ---")
    email_service.send_login_notification(
        username="teste_usuario",
        email="teste@example.com",
        ip_address="192.168.1.1"
    )

    print("\n" + "=" * 80)
    print("Demonstração concluída!")
    print("=" * 80)

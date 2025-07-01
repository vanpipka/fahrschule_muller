from fahrschule_muller.models import Message, Anmeldung

class Notification:
    
    form_name: str = ""
    author: str = ""
    phone_number: str = ""
    connection_type: str = ""
    additional_info: str = ""
    url: str = ""
    text: str = ""
    
    def __init__(self, form_name: str, author: str, phone_number: str, connection_type: str, url: str, text: str, additional_info: str = ""):
        self.form_name = form_name
        self.author = author
        self.phone_number = phone_number
        self.connection_type = connection_type
        self.url = url
        self.text = text
        self.additional_info = additional_info
  
    def build_admin_notification_message(self) -> str:
    
        text = f"""
        📨 Новое сообщение с сайта!\n
        🧾 Форма: {self.form_name}
        👤 Автор: {self.author or 'Не указано'}
        📞 Контакт: {self.phone_number or 'Не указано'}
        ➡️ Как связаться: {self.connection_type or 'Не указано'}
        🌐 Страница: {self.url or 'Не указано'}
        💬 Сообщение:\n{self.text}"""

        if self.additional_info:
            text += f"\nℹ️ Дополнительная информация: {self.additional_info}"

        return text

    def from_message(message: Message) -> 'Notification':
        return Notification(
            form_name=message.form_name,
            author=message.author,
            phone_number=message.phone_number,
            connection_type=message.connection_type,
            url=message.url,
            text=message.text
        )
    
    def from_anmeldung(annmeldung: Anmeldung) -> 'Notification':
        return Notification(
            form_name=annmeldung.form_name,
            author=annmeldung.vorname + " " + annmeldung.nachname,
            phone_number=annmeldung.phone + " " + annmeldung.email,
            connection_type="",
            url=annmeldung.url,
            text=annmeldung.form_message,
            additional_info=annmeldung.course
        )

    def __repr__(self):
        return f"Notification(title={self.title}, message={self.message}, icon={self.icon})"
from smtp import Email
from action import Action
from typing import List


class EmailWork:
    def __init__(self, name: str, email: Email, actions: list, to_user: str, to_email: str, subject: str):
        self.name = name
        self.email = email
        self.actions: List[Action] = actions
        self.to_user = to_user
        self.to_email = to_email
        self.subject = subject

    def send(self):
        text = ""
        for i in self.actions:
            text += i.to_text() + "\n"
        return self.email.send_email(self.name, self.to_user, self.to_email, self.subject, text)

    def quit(self):
        self.email.quit()
from smtp import Email
from action import Action
from typing import List
from logging import Logger


class EmailWork:
    def __init__(self, name: str, email: Email, actions: list,
                 to_user: str, to_email: str, subject: str, logger: Logger):
        self.name = name
        self.email = email
        self.actions: List[Action] = actions
        self.to_user = to_user
        self.to_email = to_email
        self.subject = subject
        self.logger = logger

    def send(self):
        text = ""
        for i in self.actions:
            text += i.to_text(self.logger) + "\n"
        return self.email.send_email(self.name, self.to_user, self.to_email, self.subject, text, logger=self.logger)

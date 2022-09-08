from abc import ABCMeta, abstractmethod
import os


class Action(metaclass=ABCMeta):
    def __init__(self, action_id, job, **kwargs):
        self.id = action_id
        self.job = job

    @abstractmethod
    def to_text(self) -> str:
        pass


class TextAction(Action):
    def __init__(self, action_id, job, **kwargs):
        super(TextAction, self).__init__(action_id, job)
        self.text = kwargs.get("text", "今天又是元气满满的一天")

    def to_text(self) -> str:
        return self.text


class CommandAction(Action):
    def __init__(self, action_id, job, **kwargs):
        super(CommandAction, self).__init__(action_id, job)
        self.command = kwargs.get("command", "echo Hello")

    def to_text(self) -> str:
        result = os.popen(self.command)
        context = result.read()
        result.close()
        return context

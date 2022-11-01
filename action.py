from abc import ABCMeta, abstractmethod
import subprocess
import io
from logging import Logger


class Action(metaclass=ABCMeta):
    def __init__(self, action_id, job, **kwargs):
        self.id = action_id
        self.job = job

    @abstractmethod
    def to_text(self, logger: Logger) -> str:
        pass


class TextAction(Action):
    def __init__(self, action_id, job, **kwargs):
        super(TextAction, self).__init__(action_id, job)
        self.text = kwargs.get("text", "今天又是元气满满的一天")

    def to_text(self, loger: Logger) -> str:
        loger.info(f"Text to text Length: {len(self.text)}")
        return self.text


class CommandAction(Action):
    def __init__(self, action_id, job, **kwargs):
        super(CommandAction, self).__init__(action_id, job)
        self.command = kwargs.get("command", "echo Hello")

    def to_text(self, loger: Logger) -> str:
        proc = subprocess.Popen(self.command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, bufsize=-1)
        proc.wait()
        stream_stdout = io.TextIOWrapper(proc.stdout, encoding='utf-8')
        stream_stderr = io.TextIOWrapper(proc.stderr, encoding='utf-8')
        str_stdout = str(stream_stdout.read()).strip()
        str_stderr = str(stream_stderr.read()).strip()

        loger.info(f"Command to text Command {self.command} stdout: {str_stdout}")
        loger.info(f"Command to text Command {self.command} stdout: {str_stderr}")

        if len(str_stdout) == 0:
            return str_stdout
        else:
            return str_stdout + "\n" + str_stderr

import json
import action
from email_work import EmailWork, Email
from time import strftime, localtime

def configure(file):
    with open(file, "r", encoding="utf-8") as f:
        return json.loads(f.read())


def load_action(conf: dict):
    actions = {}
    for i in conf["action"]:
        if i.get("job") == "Text":
            actions[i.get("action_id", "default")] = action.TextAction(**i)
        elif i.get("job") == "Command":
            actions[i.get("action_id", "default")] = action.CommandAction(**i)
    return actions


def load_email(conf: dict, actions: dict):
    emails = []
    for i in conf["email"]:
        email_actions = []
        for a in i["content"]:
            email_action = actions.get(a)
            if email_action:
                email_actions.append(email_action)
        email = EmailWork(i["from"],
                          Email(i["user"], i["passwd"], i["smtp"], port=i["post"], ssl=i["is_ssl"]),
                          email_actions,
                          i["to"].split(" ")[0],
                          i["to"].split(" ")[1],
                          i["subject"] + " - " + strftime('%Y-%b-%d', localtime()))
        emails.append(email)
    return emails

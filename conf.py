import json
import action
from email_work import EmailWork, Email
from time import strftime, localtime
import logging



def configure(file, logger: logging.Logger):
    logger.info(f"Configure File: {file}")
    with open(file, "r", encoding="utf-8") as f:
        content = json.loads(f.read())
        logger.info(f"Configure Content: {content}")
        return content


def load_action(conf: dict, logger: logging.Logger):
    actions = {}
    for i in conf["action"]:
        action_id = i.get("action_id", "default")
        if i.get("job") == "Text":
            job = action.TextAction(**i)
            actions[action_id] = job
            logger.info(f"Add text job ID: {action_id} Length: {len(job.text)}")
        elif i.get("job") == "Command":
            job = action.CommandAction(**i)
            actions[action_id] = job
            logger.info(f"Add command job ID: {action_id} CMD: {job.command}")
    return actions


def load_email(conf: dict, actions: dict, logger: logging.Logger):
    emails = []
    for i in conf["email"]:
        email_actions = []
        for a in i["content"]:
            email_action = actions.get(a)
            if email_action:
                email_actions.append(email_action)
            logger.info(f"Add content for {i['to']} Content: {a}")
        email = EmailWork(i["from"],
                          Email(i["user"], i["passwd"], i["smtp"], port=i["post"], ssl=i["is_ssl"]),
                          email_actions,
                          i["to"].split(" ")[0],
                          i["to"].split(" ")[1],
                          i["subject"] + " - " + strftime('%Y-%b-%d', localtime()),
                          logger=logger)
        emails.append(email)
    return emails

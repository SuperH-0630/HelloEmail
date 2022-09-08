from conf import configure, load_action, load_email
import sys


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Tell me the conf file.")
        exit(1)

    conf = configure(sys.argv[1])
    actions = load_action(conf)
    emails = load_email(conf, actions)
    for i in emails:
        i.send()

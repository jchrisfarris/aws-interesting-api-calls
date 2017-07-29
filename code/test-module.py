#!/usr/bin/env python3

import yaml
from pprint import pprint
from InterestingAwsActions import *
from sys import argv

if len(argv) < 2:
    filename = "https://raw.githubusercontent.com/jchrisfarris/aws-interesting-api-calls/master/actions.yaml"
else:
    filename = argv[1]

try:
    action_db = ActionDatabase(filename)
    # action_db = ActionDatabase("https://raw.githubusercontent.com/jchrisfarris/aws-interesting-api-calls/master/actions.yaml")
except ActionFileParseError as e:
    print(e)
    print("Aborting....")
    exit(1)
except NotImplementedError as e:
    print(e)
    print("Aborting....")
    exit(1)

print("Services: {}".format(action_db.list_services()))
print("Severities: {}".format(action_db.list_severities()))
print("Categories: {}".format(action_db.list_categories()))
print("Risk Types: {}".format(action_db.list_risks()))

print("All AccessControl Calls: {}".format(action_db.by_category("AccessControl")))

print("API Calls resulting in AccountTakeOver: {}".format(action_db.by_risk("AccountTakeOver")))

print("----------------------\n\n")

try: 
    action = action_db.get_action("organizations:DeletePolicy")
    pprint(action.__dict__)
    print(action.URL)
except ActionLookupError as e:
    print(e)


print("----------------------\n\n")


high = action_db.by_severity("high")
print("Got {} high severity actions".format(len(high)))
for name in high:
    a = action_db.get_action(name)
    print("{}\t\t{}".format(name,a.Description))
print("----------------------\n\n")


ec2 = action_db.by_service('ec2')
print("Got {} ec2 actions".format(len(ec2)))
for name in ec2:
    a = action_db.get_action(name)
    print("{}\t\t{}".format(name,a.Description))

print("----------------------\n\n")
print("Summary Report:")
for service in action_db.list_services():
    print("Service {} has {} actions".format(service, len(action_db.by_service(service))))

for severity in action_db.list_severities():
    print("Severity {} has {} actions".format(severity, len(action_db.by_severity(severity))))

for category in action_db.list_categories():
    print("Category {} has {} actions".format(category, len(action_db.by_category(category))))

for risk in action_db.list_risks():
    print("Risk {} has {} actions".format(risk, len(action_db.by_risk(risk))))



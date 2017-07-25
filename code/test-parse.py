#!/usr/bin/env python

import yaml

with open("actions.yaml", 'r') as stream:
    try:
        actions = yaml.load(stream)

        print("{} Critical Actions".format(len(actions['Critical'])))
        print("{} High Actions".format(len(actions['High'])))
        print("{} Medium Actions".format(len(actions['Medium'])))
        print("{} Low Actions".format(len(actions['Low'])))

    except yaml.YAMLError as exc:
        print(exc)
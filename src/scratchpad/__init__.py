from src.definitions import ROOT_DIR
import os
import getpass
from importlib import import_module

TEMPLATE = """
def main():
    print("Running scratchpad for user {}")
"""


def set_up():
    user = getpass.getuser()
    route = f"src.scratchpad.scratchpad-{user}"
    scratchpad_file = os.path.join(ROOT_DIR, *route.split(".")) + ".py"
    if not os.path.exists(scratchpad_file):
        with open(scratchpad_file, "w") as f:
            f.write(TEMPLATE.format(user))

    return import_module(route)


scratchpad = set_up()

from src.definitions import ROOT_DIR
import os
import getpass
from importlib import import_module

TEMPLATE = """
def main():
    print("Running workbench for user {}")
"""


def user_workbench_set_up():
    user = getpass.getuser()
    route = f"src.workbench.station-{user}"
    user_file = os.path.join(ROOT_DIR, *route.split(".")) + ".py"
    if not os.path.exists(user_file):
        with open(user_file, "w") as f:
            f.write(TEMPLATE.format(user))

    return import_module(route)


workbench = user_workbench_set_up()

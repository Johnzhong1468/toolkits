import os
import datetime

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LOCAL_TZ = datetime.datetime.now(datetime.timezone(datetime.timedelta(0))).astimezone().tzinfo

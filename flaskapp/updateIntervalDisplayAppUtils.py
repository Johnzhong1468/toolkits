from wtforms import Form, SelectField
import pandas as pd
import numpy as np

# form
class table_select_form(Form):
    # For example, "A" correspond to option A from get_data function, UI will display "Display Option A" in the dropdown menu
    selected_table = SelectField(label="Select Table ", choices=[("A", "Display Option A"), ("B", "Display Option B"), ("C", "Display Option C")])

def get_data(choice=None):
    _n = 12
    _size = (_n, _n)
    _cols = [chr(i) for i in range(ord("A"), ord("A") + _n)]
    if choice == "A":
        df = pd.DataFrame(np.random.randint(0, 100, size=_size), columns=_cols)
    elif choice == "B":
        df = pd.DataFrame(np.random.randint(-100, 0, size=_size), columns=_cols)
    elif choice == "C":
        df = pd.DataFrame(np.random.randint(1000, 2000, size=_size), columns=_cols)
    else:
        # default
        df = pd.DataFrame()
    return df
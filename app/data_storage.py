import json
import pandas as pd
from datetime import datetime
import os

def save_to_json(data):
    filename = f"data_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
    filepath = os.path.join('/app/data', filename)
    with open(filepath, 'w') as f:
        json.dump(data, f)
    return filename

def save_to_excel(data):
    filename = f"data_{datetime.now().strftime('%Y%m%d_%H%M%S')}.xlsx"
    filepath = os.path.join('/app/data', filename)
    df = pd.DataFrame(data)
    df.to_excel(filepath, index=False)
    return filename
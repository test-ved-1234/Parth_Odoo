from datetime import datetime
import pytz
date_from = str(datetime.now(pytz.timezone('Asia/Kolkata')).strftime("%Y-%m-%d %H:%M:%S"))
print(date_from)

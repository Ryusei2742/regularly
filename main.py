# スケジュール実行

import datetime
import pandas as pd

dt_now = str(datetime.datetime.now().strftime('%Y%m%d-%H%M%S'))

df = pd.DataFrame(
    [[dt_now, 'test', 'Hello cron']],
    columns = ['datetime', 'name', 'greet'])

df.to_csv('場所' + dt_now + '.csv')
print(dt_now, 'Hello world from cron')
















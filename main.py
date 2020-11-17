# スケジュール実行

import datetime
import pandas as pd

dt_now = str(datetime.datetime.now().strftime('%Y%m%d-%H%M%S'))

df = pd.DataFrame(
    [[dt_now, 'kinocode', 'Hello cron']],
    columns = ['datetime', 'name', 'greet'])

df.to_csv('/Users/asd2f/Python/to_excel/' + dt_now + '.csv')
print(dt_now, 'Hello world from cron')


# /Library/Frameworks/Python.framework/Versions/3.8/bin:/usr/local/bin:/bin:/usr/local/sbin:/usr/sbin:/sbin:/usr/bin

















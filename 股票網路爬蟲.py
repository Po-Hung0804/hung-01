from email import header
import urllib.request as req
from wsgiref import headers
url="https://tw.stock.yahoo.com/_td-stock/api/resource/FinanceChartService.ApacLibraCharts;autoRefresh=1644727004808;symbols=%5B%222330.TW%22%5D;type=tick?bkt=&device=desktop&ecma=modern&feature=ecmaModern%2CuseVersionSwitch%2CuseNewQuoteTabColor&intl=tw&lang=zh-Hant-TW&partner=none&prid=cbg5jj9h0h2j3&region=TW&site=finance&tz=Asia%2FTaipei&ver=1.2.1217&returnMeta=true"

request=req.Request( url ,headers={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36 Edg/97.0.1072.76"
})

with req.urlopen(request) as response:
    data=response.read().decode("utf-8")


import json
jd=json.loads(data)


close=jd['data'][0]['chart']['indicators']['quote'][0]['close']
high=jd['data'][0]['chart']['indicators']['quote'][0]['high']
low=jd['data'][0]['chart']['indicators']['quote'][0]['low']
timestamp=jd['data'][0]['chart']['timestamp']
import pandas as pd
df=pd.DataFrame({'close':close, 'high':high, 'low':low, 'timestamp':timestamp})
df['timestamp']=pd.to_datetime(df['timestamp'] +3600*8,unit='s')

print(df)


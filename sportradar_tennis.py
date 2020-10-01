
#Request URL: http://api.sportradar.us/tennis-t2/en/matches/sr:match:21531459/summary.json?api_key=gnsdu63tj8cjmtdtdavygwfd




import http.client

conn = http.client.HTTPSConnection("api.sportradar.us")

conn.request("GET", "/tennis-t2/en/matches/sr:match:21531459/summary.json?api_key=gnsdu63tj8cjmtdtdavygwfd")

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))
# coding: utf-8

import httplib, urllib2, json

kintoneDomain = "lambda-handson.cybozu.com"
appId = "15"
apiToken = "ecQg5zQw7OqAiY1QAllU0siV972PsoQICq682pm0"

summary = "kintone & AWS ハンズオン秋祭り 2015 スライド作成"
description = "kintone & AWS ハンズオン秋祭り 2015 スライド作成（詳細）"
link = ""

record = {"summary":{"value":summary}, "description":{"value":description}, "link":{"value":link}}
request = {"app":appId,"record":record}
requestJson = json.dumps(request)
headers = {"X-Cybozu-API-Token": apiToken, "Content-Type" : "application/json"}
connect = httplib.HTTPSConnection(kintoneDomain + ":443")
connect.request("POST", "/k/v1/record.json", requestJson, headers)
response = connect.getresponse()
print(response.read())

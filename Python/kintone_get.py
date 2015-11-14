# coding: utf-8

import httplib, urllib2, json

kintoneDomain = "lambda-handson.cybozu.com"
appId = "15"
apiToken = "ecQg5zQw7OqAiY1QAllU0siV972PsoQICq682pm0"

query = "?app=" + appId
headers = {"X-Cybozu-API-Token": apiToken}
connect = httplib.HTTPSConnection(kintoneDomain + ":443")
connect.request("GET", "/k/v1/records.json" + query, {}, headers)
response = connect.getresponse()
print(response.read())

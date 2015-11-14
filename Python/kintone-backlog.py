import httplib, urllib2, json

print('Loading function')

backlogSubdomain = "kintone-c2"
projectKey = "PRIV_TEST"
backlogPath = "https://" + backlogSubdomain + ".backlog.jp/view/" + projectKey
kintoneDomain = "lambda-handson.cybozu.com"
appId = "15"
apiToken = "ecQg5zQw7OqAiY1QAllU0siV972PsoQICq682pm0"

def lambda_handler(event, context):
    #print("Received event: " + json.dumps(event, indent=2))
    summary = event['requestParameters']['content']['summary']
    description = event['requestParameters']['content']['description']
    link = backlogPath + "-" + str(event['requestParameters']['content']['key_id'])
    query = "&query=" + urllib2.quote("link=\"" + link + "\"") + "&totalCount=true"
    query = "?app=" + appId + query
    print(query);
    headers = {"X-Cybozu-API-Token": apiToken}
    connect = httplib.HTTPSConnection(kintoneDomain + ":443")
    connect.request("GET", "/k/v1/records.json" + query, {}, headers)
    response = connect.getresponse()
    res = response.read()
    print(res)
    res = json.loads(res)
    if(int(res["totalCount"]) == 0):
        record = {"summary":{"value":summary}, "description":{"value":description}, "link":{"value":link}}
        request = {"app":appId,"record":record}
        requestJson = json.dumps(request)
        headers = {"X-Cybozu-API-Token": apiToken, "Content-Type" : "application/json"}
        connect = httplib.HTTPSConnection(kintoneDomain + ":443")
        connect.request("POST", "/k/v1/record.json", requestJson, headers)
        response = connect.getresponse()
        print(response.read())
    return event['requestParameters']['content']['key_id']

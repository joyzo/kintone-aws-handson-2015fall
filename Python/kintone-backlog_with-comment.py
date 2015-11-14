import httplib, urllib2, json

print('Loading function')
##
#Backlogとkintoneの情報
##
backlogSubdomain = "kintone-c2" #Backlogのサブドメイン
projectKey = "PRIV_TEST" #プロジェクトキー
backlogPath = "https://" + backlogSubdomain + ".backlog.jp/view/" + projectKey #Backlogの課題閲覧パス
kintoneDomain = "lambda-handson.cybozu.com" #kintoneのドメイン
appId = "15" #課題管理アプリのID
apiToken = "cSDCvGfBtEI7kYZtCJYkg2Tl5TUjta2dp3wVcjCO" #課題管理アプリのAPIトークン

def lambda_handler(event, context):
    ##
    #API Gatewayをトリガーにしたevent（Webhook）の値をセット
    ##
    #print("Received event: " + json.dumps(event, indent=2))
    summary = event['requestParameters']['content']['summary'] #Backlogに追加された課題の「概要」
    description = event['requestParameters']['content']['description'] #Backlogに追加された課題の「詳細」
    link = backlogPath + "-" + str(event['requestParameters']['content']['key_id']) #Backlogに追加された課題の「ID」を用いてリンクを作成
    ##
    #kintone課題管理アプリに登録しようとしているBacklogの課題が既にkintone側から登録済みでないかチェック
    ##
    query = "&query=" + urllib2.quote("link=\"" + link + "\"") + "&totalCount=true" #クエリの作成
    query = "?app=" + appId + query #クエリにアプリIDを追加
    print(query);
    headers = {"X-Cybozu-API-Token": apiToken} #ヘッダ
    connect = httplib.HTTPSConnection(kintoneDomain + ":443") #HTTPSリクエスト用の接続
    connect.request("GET", "/k/v1/records.json" + query, {}, headers) #GETリクエスト
    response = connect.getresponse() #レスポンス
    res = response.read()
    print(res)
    res = json.loads(res)
    ##
    #kintoneへの課題が未登録の際には登録を進める
    ##
    if(int(res["totalCount"]) == 0):
        record = {"summary":{"value":summary}, "description":{"value":description}, "link":{"value":link}} #recordの作成
        request = {"app":appId,"record":record} #アプリIDを足して、リクエストボディ完成
        requestJson = json.dumps(request)
        headers = {"X-Cybozu-API-Token": apiToken, "Content-Type" : "application/json"} #ヘッダ
        connect = httplib.HTTPSConnection(kintoneDomain + ":443") #HTTPSリクエスト用の接続
        connect.request("POST", "/k/v1/record.json", requestJson, headers) #POSTリクエスト
        response = connect.getresponse() #レスポンス
        print(response.read())
    return event['requestParameters']['content']['key_id']  # 終了

![handsonFestivalTitle](image/handson-banner.png)

## Contents
* **handson-festival-2015fall-B2-pack.zip**：「課題管理」アプリのテンプレートです。Backlogチケットプラグインが連携（未設定）されています。

* **./kintone-plugin/**：kintoneプラグイン群です。

* **./kintone-plugin/backlog.zip**：[Backlogチケット連携のプラグイン](https://www.joyzo.co.jp/plugin/backlog/)です。今回はテンプレート中の「課題管理アプリ」に連携済みです。（[設定方法](https://www.joyzo.co.jp/plugin/backlog/)）

* **./json**：AWSの設定に用いるファイル群です。

* **./json/sample_event.json**：Lambdaのテスト用eventに使うJSONファイルです。

* **./json/mapping_template.json**：API GatewayのMapping Templateに使うJSONファイルです。

* **./Python/**：Python.jsによるLamda関数のサンプルのファイル群です。

* **./Python/kintone_get.py**：PythonでkintoneのREST API（records/GET）をコールするサンプルです。

* **./Python/kintone_post.py**：PythonでkintoneのREST API（record/POST）をコールするサンプルです。

* **./Python/kintone-backlog.py**：Backlogで課題追加されたら、API Gateway経由でLambdaを起動し、kintoneアプリにレコード登録を行うLambda関数サンプルです。

* **./Python/kintone-backlog.py**：`kintone-backlog.py`に日本語コメントを追加したサンプルです。Lambdaにインラインで貼ると文字化けしますので、今回は利用しません。

## Reference
* [AWS Lambdaによるサーバレス
アーキテクチャの基本に触れてみよう！-kintone & AWS ハンズオン祭り2015秋【B-2】-](https://www.slideshare.net/yamaryu0508b/kintone-caf-vol4-kintone-aws-api-gatewaylambdamachine-learning-52406500)（slideshare）
* [Amazon Web Services](http://aws.amazon.com/jp/)
* [kintone](https://kintone.cybozu.com/jp/)
* [kintone API リファレンス](https://cybozudev.zendesk.com/hc/ja/categories/200147600)（cybozu.com developer network内）
* [kintone JavaScript APIサンプル](https://cybozudev.zendesk.com/hc/ja/sections/200263970)（cybozu.com developer network内）
* [AWS利用無料枠](http://aws.amazon.com/jp/free/)（[FAQ](http://aws.amazon.com/jp/free/faqs/)）
* [kintone30日間無料お試し](https://kintone.cybozu.com/jp/trial/)
* [kintone無償開発者ライセンス](https://cybozudev.zendesk.com/hc/ja/articles/200720464)

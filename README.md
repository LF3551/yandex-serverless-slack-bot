# yandex-serverless-slack-bot
[![Supported python versions](https://img.shields.io/badge/Python-3.8%20%7C%203.9-blue?style=flat-square&logo=python)](https://www.python.org/)
[![Yandex.Cloud](https://img.shields.io/badge/Yandex.Cloud-functions-9cf?style=flat-square&logo=data:image/png;base64,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)](https://cloud.yandex.ru/)

Simple Slack bot example using Yandex Cloud 

## Steps 

1. First you need to [Create your App](https://api.slack.com/apps):
    - Click `Create New App`
    - In the `Name field`, enter the app name, in our case: `MY_SLACK_BOT`
    - Select the workspace and click `Create app`
    - Grant permissions to the `MY_SLACK_BOT` app:
      - go to Features -> OAuth@Permissions -> Scopes -> Bot Token Scopes:
      - add:
        `chat:write`
        `commands`
        `im:history`
      - go to Features -> OAuth@Permissions:
        - click `Install to Workspace`
        - click `Allow`
        - at the top you will see pop-up `Success!`
        - below you can see `Bot User OAuth Token`. Copy to your notes
      - go to Settings -> Basic Information:
        - copy `Signing Secret` to your notes

2. Go to [Yandex Cloud Console](https://console.cloud.yandex.ru/)

3. Create `Yandex Service account` in Yandex Cloud:
    - click `Create service account`
    - add name, in our case `for-slack-bot`
    - add role `editor`
    - click `Create`
    - copy `Service Account ID` to your notes

4. Create `Yandex API-Gateway` in Yandex Cloud:
    - add name, in our case `api-python-slack-bot` 
    - click `Create`
    - after publication in spec you can see `servers` section:
    - Copy `Server Url` to your notes 
      `https://d5dtglrhssdfgvms1i.apigw.yandexcloud.net` (url example from spec)

5. Create  `Yandex Cloud Function` in Yandex Cloud:
   - add name, in our case `function-for-api-python-slack-bot`
   - click `Create`
   - choose programming language, in our case it will be `Python`:
   - create `index.py` file (If is not created as template):
     - add temp data in `index.py` file:
      ```
      import json
      def handler(event, context):
          print(f"Received event:\n{event}\nWith context:\n{context}")

          slack_body = event.get("body")
          slack_event = json.loads(slack_body)
          challenge_answer = slack_event.get("challenge")

          return {
              'statusCode': 200,
              'body': challenge_answer
          }
      ```
   - select below `Yandex Service account` you created earlier
   - set `timeout settings` to 5 sec
   - set variable `SLACK_BOT_TOKEN`, with key `Bot User OAuth Token` from your notes
   - set variable `SLACK_SIGNING_SECRET`, with key `Signing Secret` from your notes
   - click `Create version`
   - copy `Function ID` to your notes

6. Go back to `Yandex API-Gateway` Settings in Yandex Cloud with name `for-slack-bot`:
   - add `POST` spec below:
      ```
      paths:
        /:
          get:
            x-yc-apigateway-integration:
                type: dummy
                content:
                  '*': Hello, World!
                http_code: 200
                http_headers:
                  Content-Type: text/plain
          post:
            x-yc-apigateway-integration:
                type: cloud_functions
                function_id: `Function ID`
                service_account_id: `Service Account ID`
            operationId: slack-challenge
      ```
    
7. Go back to `API Slack settings`:
   - go to Basic Information -> Add features and functionality -> 
   -> Event Subscribtions -> Enable Events
   - click `On`
   - paste `Server Url` from your API Gateway here
   - if it is `ok` you will see message `Verified` 
   - below click `Subscribe to bot events`
   - then click  `Add Bot User Event` and add event called `message.im`
   - click `Save Changes`
   - you will see pop-up `Success!` 
   - go to Features -> App Home and select `Your App’s Presence in Slack`
    - click `Always Show My Bot as Online`
    - select `Show Tabs`
    - click `Allow users to send Slash commands and messages from the messages tab`

8. Go back to `Yandex Cloud Function` in Yandex Cloud:
    - delete old temp code from `index.py` file
    - copy and paste code from `index.py` to file `index.py` 
      in `Yandex Cloud Function` Editor
    - create file `requirements.txt` in `Yandex Cloud Function` Editor
    - copy and paste data from `requirements.txt` to file `requirements.txt` 
      in `Yandex Cloud Function` Editor
    - click `Create Version`

8. Reopen Your Slack APP on your Windows\Linux OS

9. Everything should work 🙂

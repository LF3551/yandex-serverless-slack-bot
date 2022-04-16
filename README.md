# yandex-serverless-slack-bot
Simple Slack bot example using Yandex Cloud 

## Steps 

1. First you need to [Create your App](https://api.slack.com/apps):
  - Click **Create New App** 
  - In the **Name field**, enter the app name, in our case: `MY_SLACK_BOT`
  - Select the workspace and click **Create app**
  - Grant permissions to the **MY_SLACK_BOT** app:
    - go to Features -> OAuth@Permissions -> Scopes -> Bot Token Scopes:
    - add:
      `chat:write`
      `commands`
      `im:history`
    - go to Features -> OAuth@Permissions:
      - click **Install to Workspace**
      - click **Allow**
      - at the top you will see pop-up `Success!`
      - below we can see `Bot User OAuth Token`. Copy to your notes
    - go to Settings -> Basic Information:
      - copy `Signing Secret` to your notes

2. Go to [Yandex Cloud Console](https://console.cloud.yandex.ru/)

3. Create **Yandex Service account** in Yandex Cloud:
  - click `Create service account`
  - add name, in our case `for-slack-bot`
  - add role `editor`
  - click **Create**
  - copy `Service Account ID` to your notes

4. Create **Yandex API-Gateway** in Yandex Cloud:
  - add name, in our case `api-python-slack-bot` 
  - click **Create**
  - after publication in spec you can see `servers` section:
  - Copy **Server Url** to your notes 
    `https://d5dtglrhssdfgvms1i.apigw.yandexcloud.net` (url example from spec)

6. Create  **Yandex Cloud Function** in Yandex Cloud:
   - add name, in our case `function-for-api-python-slack-bot`
   - click **Create**
   - choose programming language, in our case it will be **Python**:
   - create `index.py` file (If is not created as template):
     - add temp data in `index.py` file:
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
   - select below **Yandex Service account** you created earlier
   - set `timeout settings` to 5 sec
   - set variable `SLACK_BOT_TOKEN`, with key `Bot User OAuth Token` from our notes
   - set variable `SLACK_SIGNING_SECRET`, with key `Signing Secret` from our notes
   - click **Create version**
   - copy `Function ID` to your notes

7. Go back to **Yandex API-Gateway** Settings in Yandex Cloud with name `for-slack-bot`:
   - add POST spec below:
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
    

6. Go back to **API Slack settings**:
   - go to Basic Information -> Add features and functionality -> 
   -> Event Subscribtions -> Enable Events
   - click `On`
   - paste **Server Url** from your API Gateway here
   - if it is `ok` you will see message **Verified** 
   - below click `Subscribe to bot events`
   - and `Add Bot User Event` called `message.im`
   - click `Save Changes`
   - you will see message **Success** 
   - go to Features -> App Home and select **Your App’s Presence in Slack**
    - click `Always Show My Bot as Online`
   - select **Show Tabs** 
    - click `Allow users to send Slash commands and messages from the messages tab`

7. Go back to **Yandex Cloud Function** in Yandex Cloud:
  - delete old temp code from `index.py` file
  - copy and paste the code from `index.py` to file `index.py` 
    in **Yandex Cloud Function** Editor
  - create file `requirements.txt` in **Yandex Cloud Function** Editor
  - copy and paste data from `requirements.txt` to file `requirements.txt` 
    in **Yandex Cloud Function** Editor
  - click `Create Version`

8. Reopen Your Slack APP on your Windows\Linux OS

9. All should work correctly

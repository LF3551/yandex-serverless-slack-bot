from slack_bolt import App
from slack_bolt.adapter.aws_lambda import SlackRequestHandler

app = App(process_before_response=True)

@app.message("hello")
def say_hello(message, say):
    user = message['user']
    say(f"Hello my friend, <@{user}>!") 

def handler(event, context):
    slack_handler = SlackRequestHandler(app=app)
    return slack_handler.handle(event, context)
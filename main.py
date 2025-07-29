import boto3

# Input
print("What is your question?")
question = input()

# LexV2 client uses 'lexv2-runtime'
client = boto3.client('lexv2-runtime', region_name='us-east-1')

# Submit the text 'What can I expense?'
response = client.recognize_text(
    botId='53ZDFY3LHZ',
    botAliasId='TSTALIASID',
    localeId='en_US',
    sessionId="test_session",
    text=question
)

# Extract the messages object
messages = response.get('messages', [])

if not messages:
    print("No response from Lex.")
    print(response)
else:
    # Print the first message content
    print(messages[0].get('content'))
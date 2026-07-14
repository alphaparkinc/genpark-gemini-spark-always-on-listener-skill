from client import GeminiSparkAlwaysOnListenerClient
client = GeminiSparkAlwaysOnListenerClient()
print(client.check_event("new_email"))
class GeminiSparkAlwaysOnListenerClient:
    def check_event(self, event_type: str) -> dict:
        return {"notification_triggered": event_type == "new_email"}
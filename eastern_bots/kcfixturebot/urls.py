from django.urls import path

from .views import bot_webhook, heartbeat, poll_bot_updates, setup_bot

urlpatterns = [
    path("heartbeat/", heartbeat, name="heartbeat"),
    path("webhook/<str:token>/", bot_webhook, name="webhook"),
    path("poll/<str:token>/", poll_bot_updates, name="polling"),
    path("setup/<str:token>/", setup_bot, name="setup_bot")
]

from django.db import models


class Schedule(models.Model):
    class Days(models.TextChoices):
        mon = "MONDAY"
        tue = "TUESDAY"
        wed = "WEDNESDAY"
        thu = "THURSDAY"
        fri = "FRIDAY"
        sat = "SATURDAY"
        sun = "SUNDAY"

    user_id = models.IntegerField()
    channel_username = models.CharField(max_length=30)
    fixture_schedule = models.CharField(choices=Days.choices, max_length=15)

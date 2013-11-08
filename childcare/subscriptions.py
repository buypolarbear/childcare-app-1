from django.db import models


SUBSCRIPTION_CHOICES = (
    ('A', 'A package'),
    ('B', 'B package'),
    ('C', 'C package'),
)


class SubscriptionField(models.CharField):
    def __init__(self, *args, **kwargs):
        kwargs.setdefault('max_length', 100)
        kwargs.setdefault('choices', SUBSCRIPTION_CHOICES)

        super(SubscriptionField, self).__init__(*args, **kwargs)

    def get_internal_type(self):
        return "CharField"
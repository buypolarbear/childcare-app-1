from django.db import models


THEME_CHOICES = (
    ('default', 'Default'),
    ('yc', 'Y Combinator'),
)


class ThemeField(models.CharField):
    def __init__(self, *args, **kwargs):
        kwargs.setdefault('max_length', 100)
        kwargs.setdefault('choices', THEME_CHOICES)

        super(ThemeField, self).__init__(*args, **kwargs)

    def get_internal_type(self):
        return "CharField"
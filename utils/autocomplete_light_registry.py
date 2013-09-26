from django.contrib.auth.models import User
from django.core import urlresolvers

import autocomplete_light

from child.models import Child


class UserAutocomplete(autocomplete_light.AutocompleteModelBase):
    search_fields = ['^username']

autocomplete_light.register(User, UserAutocomplete)
from django.contrib import admin
from typing import Any, List, Optional, Tuple, Union

from django.http.request import HttpRequest

from .models import Sport , Country , Team, Player, Author , Game, Stat,News, Analysis


admin.site.register(Sport)
admin.site.register(Country)
admin.site.register(Team)
admin.site.register(Player)
admin.site.register(Author)
admin.site.register(Game)
admin.site.register(Stat)
admin.site.register(News)
admin.site.register(Analysis)

from django.contrib import admin

# Register your models here.
from .models import Team, Game, Player, GoalEvent

admin.site.register(Team)
admin.site.register(Game)
admin.site.register(Player)
admin.site.register(GoalEvent)

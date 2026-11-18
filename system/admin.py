from django.contrib import admin
from .models import FacultyTeam, Player, Venue, Match, MatchResults


@admin.register(FacultyTeam)
class FacultyAdmin(admin.ModelAdmin):
    list_display = ("Faculty_name", "sport_type", "team_manager", "no_of_registered_players")


@admin.register(Player)
class PlayerAdmin(admin.ModelAdmin):
    list_display = ("student_reg_no", "student_name", "gender", "Faculty", "sport_type", "player_position")


@admin.register(Venue)
class VenueAdmin(admin.ModelAdmin):
    list_display = ("venue_name", "venue_type", "capacity")


@admin.register(Match)
class MatchAdmin(admin.ModelAdmin):
    list_display = ("match_day", "sport_type", "home_team", "away_team", "assigned_offical", "venue_start_time", "end_time", "venue")

@admin.register(MatchResults)
class MatchResultsAdmin(admin.ModelAdmin):
    list_display = ("match_date", "match", "team", "team_score", "match_outcome")

    
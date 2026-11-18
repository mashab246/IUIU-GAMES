from django.forms import ModelForm
from .models import FacultyTeam, Player, Venue, Match, MatchResults

class FacultyTeamForm(ModelForm):
    class Meta:
        model = FacultyTeam
        fields = '__all__'

class PlayerForm(ModelForm):
    class Meta:
        model = Player
        fields = '__all__'

class VenueForm(ModelForm):
    class Meta:
        model = Venue
        fields = '__all__'

class MatchForm(ModelForm):
    class Meta:
        model = Match
        fields = '__all__'      

class MatchResultsForm(ModelForm):
    class Meta:
        model = MatchResults
        fields = '__all__'
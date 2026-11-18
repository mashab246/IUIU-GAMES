from django.shortcuts import render
from .models import *
from .forms import *

def home_view(request):
    return render(request, "home.html")

def add_faculty_team_view(request):
    message = ""
    if request.method == "POST":
        facultyteamform = FacultyTeamForm(request.POST)

        if facultyteamform.is_valid():
            facultyteamform.save()
            message = "Form created successfully"
    else:
        facultyteamform = FacultyTeamForm()

    facultyteams = FacultyTeam.objects.all()

    context = {
        'form': facultyteamform,
        'msg': message,
        'facultyteams': facultyteams

    }

    return render(request, "add_faculty_team.html", context)


def add_player_view(request):
    message = ""
    if request.method == "POST":
        player_form = PlayerForm(request.POST)

        if player_form.is_valid():
            player_form.save()
            message = "Player added successfully"
    else:
        player_form = PlayerForm()

    players = PlayerForm.objects.all()

    context = {
        'form': PlayerForm,
        'msg': message,
        'players': players
    }

    return render(request, "add_player.html", context)


def add_venue_view(request):
    message = ""
    if request.method == "POST":
        venue_form = VenueForm(request.POST)

        if venue_form.is_valid():
            venue_form.save()
            message = "Venue added successfully"
    else:
        venue_form = VenueForm()

    venues = VenueForm.objects.all()

    context = {
        'form': VenueForm,
        'msg': message,
        'venues': venues
    }

    return render(request, "add_venue.html", context)


def add_match_view(request):
    message = ""
    if request.method == "POST":
        match_form = MatchForm(request.POST)

        if match_form.is_valid():
            match_form.save()
            message = "Match added successfully"
    else:
        match_form = MatchForm()

    matches = MatchForm.objects.all()

    context = {
        'form': MatchForm,
        'msg': message,
        'matches': matches
    }

    return render(request, "add_match.html", context)

def add_match_results_view(request):
    message = ""
    if request.method == "POST":
        match_result_form = MatchResults(request.POST)
    
        if match_result_form.is_valid():
            match_result_form.save()
            message = "Match added successfully"
    else:
        match_result_form = MatchResults()
    
    results = MatchResults.objects.all()
    
    context = {
        'form': MatchResults,
        'msg': message,
        'results': results
    }
    
    return render(request, "add_results.html", context)


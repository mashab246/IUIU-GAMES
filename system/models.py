from django.db import models

class FacultyTeam(models.Model):
    sports = [
        ("Football", "Football"),
        ("Netball","Netaball"),
        ("Volleyball","Volleyball"),
        ("Basketball","Basketball"),
        ("Athletics","Athletics")
    ]

    Faculty_name = models.CharField(max_length=100)
    sport_type = models.CharField(max_length=100, choices=sports)
    team_manager = models.CharField(max_length=100)
    no_of_registered_players = models.PositiveBigIntegerField(verbose_name="Registered Players")

    def __str__(self):
        return f"{self.faculty_name} - {self.sport_type}"


class Player(models.Model):
    Gender_Options = [
        ("Male","M"),
        ("Female","F")
    ]

    student_reg_no = models.CharField(max_length=100)
    student_name = models.CharField(max_length=100)
    gender = models.CharField(max_length=50, choices=Gender_Options)

    Faculty = models.ForeignKey(
        FacultyTeam,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

    sport_type = models.ForeignKey(
        FacultyTeam,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="sporttype"
    )
    player_position = models.CharField(max_length=100, help_text=("e.g, Goalkeeper, Striker, Setter, Center"))

    def __str__(self):
        return f"{self.student_name} ({self.student_reg_no})"


class Venue(models.Model):
    venues = [
        ("Football Pitch","Football Pitch"),
        ("Indoor Court","Indoor Court"),
        ("Netball Court","Netball Court"),
        ("Track Field","Track Field")
    ]

    venue_name = models.CharField(max_length=100)
    venue_type = models.CharField(max_length=100, choices=venues)
    capacity = models.PositiveBigIntegerField(verbose_name="Venue Capacity")

    def __str__(self):
        return f"{self.venue_name} - {self.venue_type} - {self.capacity}"


class Match(models.Model):
    days = [
        ("Mon","Monday"),
        ("Tue","Tuesday"),
        ("Wed","Wednesday"),
        ("Thur","Thursday"),
        ("Fri","Friday"),
        ("Sat","Saturday"),
        ("Sun","Sunday")
    ]

    match_day = models.CharField(max_length=50, choices=days)
    sport_type = models.ForeignKey(
        FacultyTeam,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

    home_team = models.ForeignKey(
        FacultyTeam,
        on_delete=models.CASCADE,
        related_name='hometeam'
    )

    away_team = models.ForeignKey(
        FacultyTeam,
        on_delete=models.CASCADE,
        related_name='Awayteam'
    )

    assigned_offical = models.CharField(max_length=100)
    venue_start_time = models.DateTimeField(max_length=100)
    end_time = models.DateTimeField(max_length=100)

    venue = models.ForeignKey(
        Venue,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

    class Meta:
        unique_together = ('venue', 'match_day', 'sport_type', 'venue_start_time', 'end_time')

    def __str__(self):
        return f"{self.home_team.faculty_name} vs {self.away_team.Faculty_name} on {self.match_day} by {self.assigned_offical}"


class MatchResults(models.Model):
    match_date = models.DateField(auto_now_add=True)
    match = models.ForeignKey(
        Match,
        on_delete=models.SET_NULL,
        null=True
    )

    team = models.ForeignKey(
        FacultyTeam,
        on_delete=models.SET_NULL,
        null=True
    )

    team_score = models.IntegerField(max_length=50)
    match_outcome = models.CharField(max_length=100, help_text=("Winner", "Second Runners up", "others"))

    def __str__(self):
        return f"{self.match_date} - {self.match} - {self.team} - {self.team_score} - {self.match_outcome}"


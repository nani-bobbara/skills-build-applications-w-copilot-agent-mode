from djongo import models

class User(models.Model):
    _id = models.ObjectIdField()
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=100)
    password = models.CharField(max_length=128)
    def __str__(self):
        return self.email

class Team(models.Model):
    _id = models.ObjectIdField()
    name = models.CharField(max_length=100)
    members = models.ArrayField(model_container=User)
    def __str__(self):
        return self.name

class Activity(models.Model):
    _id = models.ObjectIdField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    type = models.CharField(max_length=50)
    duration = models.IntegerField()
    date = models.DateTimeField()
    def __str__(self):
        return f"{self.user.email} - {self.type}"

class Leaderboard(models.Model):
    _id = models.ObjectIdField()
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    points = models.IntegerField()
    def __str__(self):
        return f"{self.team.name} - {self.points}"

class Workout(models.Model):
    _id = models.ObjectIdField()
    name = models.CharField(max_length=100)
    description = models.TextField()
    def __str__(self):
        return self.name

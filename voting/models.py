from django.db import models

class Voter(models.Model):
    name = models.CharField(max_length=100)
    mobile = models.CharField(max_length=10, unique=True)
    password = models.CharField(max_length=100)

class FamilyMember(models.Model):
    voter = models.ForeignKey(Voter, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    member_voter_id = models.CharField(max_length=20)  # ✅ Renamed to avoid conflict
    has_voted = models.BooleanField(default=False)


class Vote(models.Model):
    family_member = models.ForeignKey(FamilyMember, on_delete=models.CASCADE)
    candidate = models.CharField(max_length=100)
    vote_time = models.DateTimeField(auto_now_add=True)

from django.contrib import admin
from .models import Voter, FamilyMember, Vote
from django.db.models import Count


@admin.register(Vote)
class VoteAdmin(admin.ModelAdmin):
    change_list_template = "admin/voting/vote_changelist.html"

    def changelist_view(self, request, extra_context=None):
        vote_data = Vote.objects.values('candidate').annotate(count=Count('candidate'))
        extra_context = {'vote_data': vote_data}
        return super().changelist_view(request, extra_context=extra_context)

@admin.register(Voter)
class VoterAdmin(admin.ModelAdmin):
    list_display = ['name', 'mobile']

@admin.register(FamilyMember)
class FamilyMemberAdmin(admin.ModelAdmin):
    list_display = ['name', 'member_voter_id', 'has_voted']

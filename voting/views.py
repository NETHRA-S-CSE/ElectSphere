import random
from django.shortcuts import render, redirect
from .models import FamilyMember, Voter, Vote
from datetime import datetime


def index(request):
    return render(request, 'voting/index.html')

def login_view(request):
    if request.method == 'POST':
        mobile = request.POST.get('mobile')
        password = request.POST.get('password')

        try:
            voter = Voter.objects.get(mobile=mobile, password=password)
            request.session['voter_id'] = voter.id  # Save to session
            return redirect('dashboard')
        except Voter.DoesNotExist:
            return render(request, 'voting/login.html', {'error': 'Invalid credentials'})

    return render(request, 'voting/login.html')

def register(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        mobile = request.POST.get('mobile')
        password = request.POST.get('password')
        confirm = request.POST.get('confirm')

        if password != confirm:
            return render(request, 'voting/register.html', {'error': 'Passwords do not match'})

        if Voter.objects.filter(mobile=mobile).exists():
            return render(request, 'voting/register.html', {'error': 'Mobile number already exists'})

        # Save to MongoDB
        Voter.objects.create(name=name, mobile=mobile, password=password)
        return redirect('login')  # go to login page after registration

    return render(request, 'voting/register.html')
def dashboard(request):
    voter_id = request.session.get('voter_id')
    if not voter_id:
        return redirect('login')

    voter = Voter.objects.get(id=voter_id)

    if request.method == 'POST':
        name = request.POST.get('name')
        voterid = request.POST.get('voterid')
        FamilyMember.objects.create(
            voter=voter,
            name=name,
            member_voter_id=voterid,
            has_voted=False
        )
        return redirect('dashboard')

    family_members = FamilyMember.objects.filter(voter=voter)

    return render(request, 'voting/dashboard.html', {
        'voter': voter,
        'members': family_members
    })


otp_storage = {}

def otp_verify(request):
    member_id = request.GET.get('id')
    print("👉 Reached OTP view")
    print("📌 member_id from GET:", member_id)

    if request.method == 'POST':
        print("🔄 POST request - verifying OTP")
        entered_otp = request.POST.get('otp')
        if otp_storage.get(member_id) == entered_otp:
            del otp_storage[member_id]
            request.session['member_id'] = member_id
            return redirect('finalVote')
        else:
            member = FamilyMember.objects.get(id=member_id)
            return render(request, 'voting/otp_verify.html', {
                'member': member,
                'error': 'Invalid OTP'
            })

    # 🆕 GET request
    print("🆕 GET request - generating OTP")

    member = FamilyMember.objects.get(id=member_id)  # ✅ Place it here for GET
    generated_otp = str(random.randint(1000, 9999))
    otp_storage[member_id] = generated_otp
    print(f"🔐 OTP for {member.name}: {generated_otp}")

    return render(request, 'voting/otp_verify.html', {'member': member})



def finalVote(request):
    member_id = request.session.get('member_id')
    if not member_id:
        return redirect('dashboard')

    member = FamilyMember.objects.get(id=member_id)

    # ✅ Prevent re-voting
    if member.has_voted:
        return redirect('dashboard')

    if request.method == 'POST':
        candidate = request.POST.get('candidate')
        Vote.objects.create(family_member=member, candidate=candidate)

        member.has_voted = True
        member.save()

        del request.session['member_id']

        current_time = datetime.now().strftime("%B %d, %Y – %I:%M %p")
        

        return render(request, 'voting/voteSuccess.html', {
            'member': member,
            'candidate': candidate,
            'time': current_time
        })

    return render(request, 'voting/finalVote.html', {'member': member})

#def voteSuccess(request):
 #   return render(request, 'voting/voteSuccess.html')

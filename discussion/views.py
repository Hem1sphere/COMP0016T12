from django.shortcuts import render
# Create your views here.
from django.contrib.auth.mixins import UserPassesTestMixin
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from django import forms
from django.http import HttpResponse
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from .models import Discussion

# from .models import Discussion

def discussion(request):
    context = {
        'discussion': Discussion.objects.all()
    }
    return render(request, 'discussion/discussion_list.html', context)


# def user_is_discussing(discussionid, userid):
#     current_discussion = Discussion.objects.get(pk=discussionid)
#     for devs in current_discussion.discussion_developer.all():
#         if devs.pk == userid:
#             return True
#     return False

# def participateInDiscussion(request, discussionid):
#     user = Developer.objects.get(user=request.user)
#     if not user_is_participating(challengeid, user.pk):
#         Challenge.objects.get(pk=challengeid).developers.add(user)
#         # return render(request, 'challenges/challenge_list.html')
#     return HttpResponseRedirect(reverse('challenges_detail', args=[challengeid]))

class DiscussionMainView(ListView):
    model = Discussion
    template_name = 'discussion/discussion_list.html'
    context_object_name = 'discussion'
    # ordering = ['-date_created']
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
from django.http import HttpResponse,HttpRequest
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from .models import Discussion,Each_discussion



def discussion(request):
    context = {
        'discussion': Discussion.objects.all()
    }
    return render(request, 'discussion/discussion_list.html', context)



# All Forms

class DiscussionCreateForm(forms.ModelForm):
    class Meta:
        model= Discussion
        fields=['title', 'content']


class CommentCreateForm(forms.ModelForm):
    class Meta:
        model= Each_discussion
        fields=['comment']



# All Views

class DiscussionMainView(ListView):
    model = Discussion
    template_name = 'discussion/discussion_list.html'
    context_object_name = 'discussion'
    ordering = ['-date_posted']



class DiscussionDetailView(DetailView):
    model = Discussion
    template_name = 'discussion/discussion_detail.html'

    def get_context_data(self, **kwargs):
        context = super(DiscussionDetailView,self).get_context_data(**kwargs)
        context['each_discussion'] = Each_discussion.objects.all()
        return context



class DiscussionCreateView(SuccessMessageMixin, CreateView):
    model = Discussion
    template_name = 'discussion/discussion_form.html'
    fields = ['title', 'content']
    success_message = "Your discussion has been successfully created."
    
    def form_valid(self,form):
        form.instance.author = self.request.user.developer
        return super().form_valid(form)



def add_comment_to_discussion(request,pk):
        discussion = get_object_or_404(Discussion,pk=pk)
        if request.method == 'POST':
            form = CommentCreateForm(request.POST)
            if form.is_valid():
                comment = form.save(commit=False)
                comment.post = post
                comment.commenter = request.user
                comment.save()
                
        else:
            form =  CommentCreateForm()
        return render(request,'discussion/comment_success.html',{'form':form})







from datetime import datetime
from django.db.models import Q
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView, DetailView

from .models import QuestionModel, CommentModel
from .forms import QuestionForm, CommentForm

# Create your views here.


@login_required(login_url='login')
def all_questions(request):
    questions = QuestionModel.objects.all().order_by('-datetime')
    return render(request, 'pages/quest.html', {'questions': questions})


class DetailQuestion(LoginRequiredMixin, DetailView):
    model = QuestionModel
    template_name = 'pages/detail.html'
    context_object_name = 'question'


class CreateQuestion(LoginRequiredMixin, CreateView):
    model = QuestionModel
    form_class = QuestionForm
    template_name = 'pages/posts.html'
    success_url = 'ques'
    login_url = 'login'


@login_required(login_url='login')
def add_comment(request, pk):
    questions_var = QuestionModel.objects.get(id=pk)
    if request.method == 'POST':
        form = CommentForm(request.POST, instance=questions_var)
        if form.is_valid():
            name = request.user
            question = form.cleaned_data['question']
            data = CommentModel(the_question=questions_var, username=name, question=question, created_at=datetime.now())
            data.save()
            return redirect('question')
        else:
            print('form is invalid')
    else:
        form = CommentForm()

    return render(request, 'pages/add_comment.html', {'form': form})


def search(request):
    query = request.GET.get('q')
    page_search = QuestionModel.objects.filter(Q(hashtag__icontains=query))

    return render(request, 'secret_app/search.html', {'search': page_search})


@login_required(login_url='login')
def LikeView(request, pk):
    like = get_object_or_404(QuestionModel, id=pk)
    like.likes.add(request.user)
    return HttpResponseRedirect('question')


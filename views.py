from typing import Any
from django.db import models
from .models import Choice, Question 
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import get_object_or_404, render
from django.views import generic
from django.utils import timezone
from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import InputForm
from django.shortcuts import redirect
from django.template import loader
from .models import Member



class IndexView(generic.ListView):
    template_name = "polls/index.html"
    context_object_name = "latest_question_list"

    def get_queryset(self):
        """Return the last five published questions."""
        return Question.objects.order_by("-pub_date")[:5]


class DetailView(generic.DetailView):
    model = Question
    template_name = "polls/question_detail.html"

    def get_queryset(self):
        return Question.objects.filter(pub_date__lte=timezone.now())


class ResultsView(generic.DetailView):
    model = Question
    template_name = "polls/results.html"

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST["choice"])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(
            request,
            "polls/detail.html",
            {
                "question": question,
                "error_message": "You didn't select a choice.",
            },
        )
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse("polls:results", args=(question.id,)))




class DetailView(generic.DetailView):
    ...

    def get_queryset(self):
     
        return Question.objects.filter(pub_date__lte=timezone.now())
    


# Create your views here.
def home_view(request):

    
    
    if request.method == "POST":
        form = InputForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            q=Question()
            q.question_text=form.cleaned_data["question"]
            q.pub_date=timezone.now()
            q.save()
            c1=Choice(question=q)
            c1.choice_text=form.cleaned_data["choice1"]
            c1.save()
            c2=Choice(question=q)
            c2.choice_text=form.cleaned_data["choice2"]
            c2.save()
            return redirect("polls:index")

    else:
        form = InputForm()        
    return render(request, "polls/name.html",{'form': form})

# def deleteView(request,pk):
#     Question.objects.get(id=pk).delete()
#     return redirect("polls:index")

def delete_items(request, pk):
	queryset = Question.objects.get(id=pk)
	if request.method == 'POST':
		queryset.delete()
		return redirect('polls:index')
	return render(request, 'polls/delete_items.html')

def update_items(request,pk):
    queryset = Question.objects.get(id=pk)
    if request.method == "POST":
        form = InputForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            q=Question.objects.get(id=pk)
            q.question_text=form.cleaned_data["question"]
            q.pub_date=timezone.now()
            q.save()
            c1=Choice.objects.get(question=q)
            c1.choice_text=form.cleaned_data["choice1"]
            c1.save()
            c2=Choice.objects.get(question=q)
            c2.choice_text=form.cleaned_data["choice2"]
            c2.save()
            return redirect("polls:index")

    else:
        form = InputForm()        
    return render(request, "polls/name.html",{'form': form})




   








   

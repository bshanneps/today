from question.models import Question
from question.forms import QuestionForm
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
# Create your views here.

def create(request):
    if request.method == "POST":
        form = QuestionForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('/show/')
            except:
                pass
    else:
        form = QuestionForm()
    return render(request, 'question/index.html', {'form': form})

def show(request):
    question = Question.objects.all()
    return render(request, "question/show.html", {'question': question})

def edit(request,id):
    question = Question.objects.get(id = id)
    return render(request, 'question/edit.html', {'question': question})

def update(request, id):
    question = Question.objects.get(id=id)
    form = QuestionForm(request.POST, instance = question)
    # print(id)
    if form.is_valid():
        form.save()
        # print("Hello")
        return redirect("/show/")
    return render(request, 'question/edit.html', {'question': question})

def delete(request,id):
    question = Question.objects.get(id = id)

    if request.method == "POST":
        question.delete()
        return redirect("/show")
    return render(request, 'question/delete.html', {'question': question})
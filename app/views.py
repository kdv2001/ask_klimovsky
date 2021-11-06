from django.shortcuts import render
from django.core.paginator import Paginator
from django.http import HttpResponse


# Create your views here


def index(request):
    return render(request, "index.html", {})


questions = [
    {
        "title": f"Title {i}",
        "text": f"This is text for {i} question."
    } for i in range(100)
]


def hot(request):
    paginator = Paginator(questions, 5)
    page = request.GET.get('page')
    content = paginator.get_page(page)
    return render(request, "hot.html", {'questions': content})


def question(request):
    return render(request, "question.html", {})

# def index(request):
#     return render(request, "base.html", {})

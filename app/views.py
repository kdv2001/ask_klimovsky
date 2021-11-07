from django.shortcuts import render
from django.core.paginator import Paginator
from django.http import HttpResponse

# Create your views here
questions_hot = [
    {
        "title": f"Title_hot {i}",
        "text": f"This is for {i} question_base.",
        "number": i
    } for i in range(100)
]

questions_base = [
    {
        "title": f"Title_base {i}",
        "text": f"This is text for {i} question_base.",
        "number": i
    } for i in range(100)
]

questions_tag = [
    {
        "title": f"Title_tag {i}",
        "text": f"This is text for {i} question_tag.",
        "number": i
    } for i in range(100)
]

question_num = [
    {
        "title": f"Title_question",
        "text": f"This is text for  question_question.",
        "number": 1
    }
]

answers = [
    {
        "title": f"Title_tag {i} answer_title",
        "text": f"This is text for {i} answer_text.",
        "number": i
    } for i in range(100)
]



def index(request):
    paginator = Paginator(questions_base, 5)
    page = request.GET.get('page')
    content_base = paginator.get_page(page)
    return render(request, "index.html", {'questions': content_base})


def hot(request):
    paginator = Paginator(questions_hot, 5)
    page = request.GET.get('page')
    content = paginator.get_page(page)
    return render(request, "hot.html", {'questions': content})


def tag(request):
    paginator = Paginator(questions_tag, 5)
    page = request.GET.get('page')
    content_tag = paginator.get_page(page)
    return render(request, "base.html", {'questions': content_tag})


def question(request, number):
    paginator = Paginator(answers, 5)
    page = request.GET.get('page')
    content_answer = paginator.get_page(page)
    return render(request, "question.html", {'questions': questions_base[number], 'answers': content_answer})


def ask(request):
    return render(request, "ask.html", {})


def login(request):
    return render(request, "login.html", {})


def signup(request):
    return render(request, "signup.html", {})


def settings(request):
    return render(request, "settings.html", {})

from django.shortcuts import render
from django.http import HttpResponseNotFound
from django.core.paginator import Paginator
from app.models import Question, Answer, Profile
from django.http import HttpResponse

# Create your views here

questions_hot = [
    {
        "user": f"user {i}",
        "title": f"Title_hot {i}",
        "text": f"This is for {i} question_base.",
        "number": i,
        "like": i,
        "answers": f"Answers ({100})",
        "tags": [{
            "tag": f"tag_h{j}"
        } for j in range(3)]
    } for i in range(100)
]

popular_tags = [
    {
        "tag": f"tag {i}"
    } for i in range(40)
]


def index(request):
    questions_new = Question.objects.get_questions()
    best_members = Profile.objects.get_best_members()
    return render(request, "index.html",
                  {'questions': my_paginator(request, questions_new), 'tags_block': popular_tags,
                   'best_members_block': best_members})


def hot(request):
    best_members = Profile.objects.get_best_members()
    return render(request, "hot.html",
                  {'questions': my_paginator(request, questions_hot), 'tags_block': popular_tags,
                   'best_members_block': best_members})


def tag(request, choose_tag):
    questions_tag = Question.objects.get_question_tag(choose_tag)
    if questions_tag == 0:
        return HttpResponseNotFound('<h1>Page not found</h1>')

    best_members = Profile.objects.get_best_members()
    return render(request, "base.html",
                  {'questions': my_paginator(request, questions_tag), 'tags_block': popular_tags,
                   'best_members_block': best_members,
                   'shoose_tag': choose_tag})


def question(request, number):
    question = Question.objects.get_question(number)
    answer = Answer.objects.get_answers(number)
    best_members = Profile.objects.get_best_members()


    return render(request, "question.html",
                  {'questions': question, 'answers': my_paginator(request, answer), 'tags_block': popular_tags,
                   'best_members_block': best_members})


def ask(request):
    best_members = Profile.objects.get_best_members()
    return render(request, "ask.html", {'tags_block': popular_tags, 'best_members_block': best_members})


def login(request):
    best_members = Profile.objects.get_best_members()

    return render(request, "login.html", {'tags_block': popular_tags, 'best_members_block': best_members})


def signup(request):
    best_members = Profile.objects.get_best_members()

    return render(request, "signup.html", {'tags_block': popular_tags, 'best_members_block': best_members})


def settings(request):
    best_members = Profile.objects.get_best_members()
    return render(request, "settings.html", {'tags_block': popular_tags, 'best_members_block': best_members})


def my_paginator(request, object_to_pag):
    paginator = Paginator(object_to_pag, 5)
    page = request.GET.get('page')
    content_paginate = paginator.get_page(page)
    return content_paginate

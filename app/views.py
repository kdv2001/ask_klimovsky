from django.shortcuts import render
from django.core.paginator import Paginator
from app.models import Question, Answer, Like
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

questions_base = [
    {
        "user": f"user {i}",
        "title": f"Title_base {i}",
        "text": f"This is text for {i} question_base.",
        "number": i,
        "like": i,
        "answers": f"Answers ({100})",
        "tags": [{
            "tag": f"tag_b{j}"
        } for j in range(3)]
    } for i in range(100)
]

questions_tag = [
    {
        "user": f"user {i}",
        "title": f"Title_tag {i}",
        "text": f"This is text for {i} question_tag.",
        "number": i,
        "like": i,
        "answers": f"Answers ({100})",

    } for i in range(100)
]

question_num = [
    {
        "title": f"Title_question",
        "text": f"This is text for question_question.",
        "number": 1,
    }
]

answers = [
    {
        "title": f"Title_tag {i} answer_title",
        "text": f"This is text for {i} answer_text.",
        "number": i,
        "like": i
    } for i in range(100)
]

popular_tags = [
    {
        "tag": f"tag {i}"
    } for i in range(40)
]

best_members = [
    {
        "member": f"member {i}"
    } for i in range(40)
]


def index(request):
    questions_new = Question.objects.get_questions()

    paginator = Paginator(questions_new, 5)
    page = request.GET.get('page')
    content_base = paginator.get_page(page)
    return render(request, "index.html",
                  {'questions': content_base, 'tags_block': popular_tags, 'best_members_block': best_members})


def hot(request):
    paginator = Paginator(questions_hot, 5)
    page = request.GET.get('page')
    content = paginator.get_page(page)
    return render(request, "hot.html",
                  {'questions': content, 'tags_block': popular_tags, 'best_members_block': best_members})


def tag(request, choose_tag):
    questions_tag = Question.objects.get_question_tag(choose_tag)

    paginator = Paginator(questions_tag, 5)
    page = request.GET.get('page')
    content_tag = paginator.get_page(page)
    return render(request, "base.html",
                  {'questions': content_tag, 'tags_block': popular_tags, 'best_members_block': best_members,
                   'shoose_tag': choose_tag})


def question(request, number):
    question = Question.objects.get_question(number)
    answer = Answer.objects.get_answers(number)
    paginator = Paginator(answer, 5)
    page = request.GET.get('page')
    content_answer = paginator.get_page(page)
    return render(request, "question.html",
                  {'questions': question, 'answers': content_answer, 'tags_block': popular_tags,
                   'best_members_block': best_members})


def ask(request):
    return render(request, "ask.html", {'tags_block': popular_tags, 'best_members_block': best_members})


def login(request):
    return render(request, "login.html", {'tags_block': popular_tags, 'best_members_block': best_members})


def signup(request):
    return render(request, "signup.html", {'tags_block': popular_tags, 'best_members_block': best_members})


def settings(request):
    return render(request, "settings.html", {'tags_block': popular_tags, 'best_members_block': best_members})

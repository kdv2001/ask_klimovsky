from django.contrib.auth.models import User
from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey

class ProfileManager(models.Manager):
    def get_best_members(self):
        data = self.all()
        best_members = [
            {
                "member": i.name
            }for i in data
        ]
        return best_members

class Profile(models.Model):
    avatar = models.ImageField(max_length=64, default='/static/img/chaplin.jpg')
    name = models.CharField(max_length=64)

    # user = models.OneToOneField(User, on_delete=models.CASCADE)

    objects = ProfileManager()

    def __str__(self):
        return ''.join([self.name])


class Tag(models.Model):
    tag = models.CharField(max_length=64)

    def __str__(self):
        return ''.join([self.tag])


class QuestionManager(models.Manager):
    def get_questions(self):
        data = self.order_by('-id')
        questions_base = [
            {
                "user": i.author.name,
                "title": i.title,
                "text": i.text,
                "number": i.pk,
                "like": 100,
                "answers": f"Answers {Answer.objects.filter(answer=i.pk).count()}",
                "tags": [{
                    "tag": f"{j}"
                } for j in i.tag.all()]
            } for i in data
        ]
        return questions_base

    def get_question(self, number):
        data = self.all()
        question_base = {
            "user": self.get(pk=number).author.name,
            "title": self.get(pk=number).title,
            "text": self.get(pk=number).text,
            "number": self.get(pk=number).pk,
            "like": 100,
            "tags": [{
                "tag": f"{j}"
            } for j in self.get(pk=number).tag.all()]
        }
        return question_base

    def get_question_tag(self, choose_tag):
        data = self.filter(tag__tag__icontains=choose_tag)
        if not data:
            return 0;

        questions_tag = [
            {
                "user": i.author.name,
                "title": i.title,
                "text": i.text,
                "number": i.pk,
                "like": 100,
                "answers": f"Answers {Answer.objects.filter(answer=i.pk).count()}",
                "tags": [{
                    "tag": f"{j}"
                } for j in i.tag.all()]
            } for i in data.order_by('-id')
        ]
        return questions_tag


class Question(models.Model):
    title = models.CharField(max_length=32)
    text = models.TextField()
    author = models.ForeignKey(Profile, on_delete=models.CASCADE)
    tag = models.ManyToManyField(Tag)

    objects = QuestionManager()

    def __str__(self):
        return ''.join([self.title])

    # str(self.tag.pk), str(self.author.pk)


class AnswerManager(models.Manager):
    def get_answers(self, number):
        data = self.filter(answer=number)
        answers_base = [
            {
                "user": i.author.name,
                "title": f"answer {i.pk}",
                "text": i.Text,
                "number": i.pk,
                "like": 100,
            } for i in data.order_by('-id')
        ]
        return answers_base


class Answer(models.Model):
    author = models.ForeignKey(Profile, on_delete=models.CASCADE)
    answer = models.ForeignKey(Question, on_delete=models.CASCADE)
    Text = models.TextField()

    objects = AnswerManager()
    # def __str__(self):
    #     return ''.join([self.Text, str(self.author.pk)])


class Like(models.Model):
    likeNumber = models.IntegerField(default=0)
    author = models.ForeignKey(Profile, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer = models.ForeignKey(Answer, on_delete=models.CASCADE)


class 
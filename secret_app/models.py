from django.db import models
from django.contrib.auth.models import User


class QuestionModel(models.Model):
    username = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user')
    question = models.TextField()
    hashtag = models.CharField(max_length=50)
    liked = models.ManyToManyField(User, default=None, blank=True, related_name='like')
    updated = models.DateTimeField(auto_now=True)
    datetime = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-datetime"]

    def __str__(self):
        return self.question

    @property
    def num_likes(self):
        return self.liked.all().count()


class CommentModel(models.Model):
    the_question = models.ForeignKey(QuestionModel, related_name='comments', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.TextField()
    datetime = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-datetime"]

    def __str__(self):
        return self.comment


CHOICE_LIKE = (
    ('Like', 'Like'),
    ('Unlike', 'Unlike')
)


class LikeModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(QuestionModel, on_delete=models.CASCADE)
    value = models.CharField(choices=CHOICE_LIKE, default='Like', max_length=10)

    def __str__(self):
        return self.user


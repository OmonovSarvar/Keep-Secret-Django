from django.db import models
from django.contrib.auth.models import User


class QuestionModel(models.Model):
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    question = models.TextField()
    hashtag = models.CharField(max_length=50)
    likes = models.ManyToManyField(User, related_name='tweet_like')
    datetime = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-datetime"]

    def __str__(self):
        return self.question


class CommentModel(models.Model):
    question = models.ForeignKey(QuestionModel, related_name='comments', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.TextField()
    datetime = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-datetime"]

    def __str__(self):
        return self.comment

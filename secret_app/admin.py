from django.contrib import admin

from secret_app.models import QuestionModel, CommentModel

# Register your models here.
admin.site.register(QuestionModel)
admin.site.register(CommentModel)

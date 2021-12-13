from django.db import models

class Topic(models.Model):

    document    = models.FileField(verbose_name="ドキュメントファイル",upload_to="document/")


from django.db import models


class User(models.Model):
    # id は書かなくても自動で作成されるので、name だけ書く
    # CharField(max_length=20) が、 VARCHAR(20) に相当する
    name = models.CharField(max_length=20)

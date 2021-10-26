from django.db import models
import uuid


class BaseModel(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    class Meta:
       abstract = True


class Project(BaseModel):
    title = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    url = models.URLField(null=True, blank=True)
    tags = models.ManyToManyField('Tag', blank=True)

    def __str__(self):
        return self.title


class Comment(BaseModel):
    VOTE_TYPE = (
        (1, 'up'),
        (2, 'down')
    )
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    body = models.TextField(null=True, blank=True)
    value = models.IntegerField(choices=VOTE_TYPE)

    def __str__(self):
        return self.body


class Tag(BaseModel):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name
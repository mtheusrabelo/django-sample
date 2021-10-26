from django.db import models
import uuid


class BaseModel(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    class Meta:
       abstract = True


class Project(BaseModel):
    title = models.CharField(max_length=180)
    description = models.TextField(null=True, blank=True)
    url = models.URLField(null=True, blank=True)

    def __str__(self):
        return self.title

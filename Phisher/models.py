from datetime import datetime
from django.db import models

# Create your models here.
class SignIn(models.Model):
    email = models.EmailField()
    password = models.CharField(max_length=32)
    date_time = models.DateTimeField(auto_now_add=True)
    client_ip = models.CharField(max_length=32, null=True)
    
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def __str__(self) -> str:
        return self.email
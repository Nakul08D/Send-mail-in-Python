from django.db import models

#admin name=admin
#admin password=1234
# Create your models here.
class contact_info(models.Model):
    name=models.CharField(max_length=20)
    number=models.IntegerField()
    email=models.EmailField(max_length = 254)
    message=models.TextField()

    def __str__(self) -> str:
        return self.name

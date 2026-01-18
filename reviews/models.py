from django.db import models

# Create your models here.

class Review(models.Model):
    user_name = models.CharField(max_length=100)
    review_text = models.TextField()
    rating = models.IntegerField()

    # def __str__(self):
    #     return f"Username: {self.user_name}, Review_text: {self.review_text}, Rating: {self.rating}"
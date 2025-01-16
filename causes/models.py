from django.db import models

class Cause(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    image_url = models.URLField()

    def __str__(self):
        return self.title

class Contribution(models.Model):
    cause = models.ForeignKey(Cause, related_name='contributions', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    email = models.EmailField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.name} contributed {self.amount} to {self.cause.title}"


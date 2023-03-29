from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
# Create your models here.

class UploadImage(models.Model):
    caption = models.CharField(max_length=300)
    image = models.ImageField(upload_to='images')

    def __str__(self):
        return self.caption

# class Person(models.Model):
#     last_name = models.TextField()
#     first_name = models.TextField()
#     courses = models.ManyToManyField("Course", blank=True)

# class Course(models.Model):
#     name = models.TextField()
#     year = models.IntegerField()

#     class Meta:
#         unique_together = ("name", "year", )

# class Grade(models.Model):
#     person = models.ForeignKey(Person, on_delete=models.CASCADE)
#     grade = models.PositiveSmallIntegerField(
#         validators=[MinValueValidator(0), MaxValueValidator(100)])
#     course = models.ForeignKey(Course, on_delete=models.CASCADE)
from django.db import models
from django.core.validators import MaxValueValidator
# Create your models here.
class Students(models.Model):
    name = models.CharField(max_length=255)
    date_of_birth = models.DateTimeField()
    physics_marks = models.IntegerField(validators=[MaxValueValidator(100)])
    chemistry_marks = models.IntegerField(validators=[MaxValueValidator(100)])
    maths_marks = models.IntegerField(validators=[MaxValueValidator(100)])
    computer_science_marks = models.IntegerField(validators=[MaxValueValidator(100)])
    percentage_marks = models.FloatField(blank=True,null=True)

    def save(self,*args,**kwargs):
        total_marks = self.physics_marks + self.chemistry_marks + self.maths_marks + self.computer_science_marks
        self.percentage_marks = (total_marks /400)*100
        super().save(*args,**kwargs)

    def __str__(self):
        return self.name


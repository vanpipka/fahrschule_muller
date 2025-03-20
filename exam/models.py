import uuid
from django.db import models
from django.conf import settings


class Type(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return self.name
    
    
class Thema(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name    
    
    
class Category(models.Model):
    
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Question(models.Model):
    
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)  
    description = models.TextField()
    file = models.FileField(upload_to="exam_files/", verbose_name="file", blank=True)
    type = models.ForeignKey(Type, null=True, on_delete=models.CASCADE, related_name="drivers_category")
    thema = models.ForeignKey(Thema, null=True, on_delete=models.CASCADE, related_name="questions_thema")
    category = models.ForeignKey(Category, null=True, on_delete=models.CASCADE, related_name="questions_category")
    answer_description = models.TextField(blank=True)
    penalty_points = models.IntegerField(default=0)
    answer_1 = models.TextField(blank=True)
    answer_2 = models.TextField(blank=True)
    answer_3 = models.TextField(blank=True)
    answer_4 = models.TextField(blank=True)   
    right_answers = models.CharField(max_length=200)

    def __str__(self):
        return self.description
    
    def to_question_dto(self):
        
        answers = []
        for i in range(1, 5):
            val = getattr(self, f"answer_{i}")
            if val:
                answers.append(val)
        
        question_dto = {
            'id': self.id,
            'penalty_points': self.penalty_points,
            'img': "",
            'video': "",
            'description': self.description,
            'answer_description': self.answer_description,
            'right_answers': self.right_answers,
            'answers': answers,
            'thema': { 'name': self.thema.name, 'id': self.thema.id },
            'category': { 'name': self.category.name, 'id': self.category.id }
        }
        
        if "mp4" in self.file.name:
            question_dto["video"] = f"{settings.MEDIA_URL}{self.file}"
        elif self.file:
            question_dto["img"] = f"{settings.MEDIA_URL}{self.file}"
            
        return question_dto
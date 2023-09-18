from django.db import models

class UserInfo(models.Model):
    user_name = models.CharField(max_length=100)
    job_title = models.CharField(max_length=200)
    salary = models.IntegerField()
    city = models.CharField(max_length=100)
    required_experience = models.BooleanField(default=False) #требуется ли опыт работы в вакансии
    request_date = models.DateField(auto_now=True) 
        
    
    def __set__(self):
        return self.job_title
    
    class Meta:
        verbose_name = "Запрос пользователя"
        verbose_name_plural = 'Запросы пользователей'

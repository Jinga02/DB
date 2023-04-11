from django.db import models

# Create your models here.
class Doctor(models.Model):
    name = models.TextField()

    def __str__(self):
        return f'{self.name} 전문의'

class Patient(models.Model):
    # Reservation테이블을 통해서 ManyToManyField를 맺을거야.
    doctors = models.ManyToManyField(Doctor, through='Reservation') 
    name = models.TextField()

    def __str__(self):
        return f'{self.pk}번 환자 {self.name}'

# 중개모델 : 관계를 가지는 두 테이블을 각각 참조하는 외래키 필드
# 예약 모델은 의사와 환자에 각각 N:1 관계를 가진다.
class Reservation(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)

    symptom = models.TextField()
    reserved_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f'{self.doctor_id}번 의사의 {self.patient_id}번 환자'




from django.db import models

# Create your models here.
class Doctor(models.Model):
    name = models.CharField(max_length=50)
    modile = models.IntegerField()
    special = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name
    
    
class Patient(models.Model):
    name = models.CharField(max_length=50)
    mobile = models.IntegerField(null=True)
    gender = models.CharField(max_length=20)
    address = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name
    
    
class Appiontment(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)#doctor table se data delete to yaha se vi delete hoga
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)#patient table se data delete to yaha se vi delete hoga
    date = models.DateField()
    time = models.TimeField()    
    
    def __str__(self):
        return self.doctor.name+"--"+self.patient.name  #doctor and patient ko jodana

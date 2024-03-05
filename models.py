from django.db import models

# Create your models here.
class register_table(models.Model):
    first_name=models.CharField(max_length=100)
    Last_name=models.CharField(max_length=100)
    email_id=models.EmailField()
    phone_number=models.CharField(max_length=100)
    appointment_time=models.CharField(max_length=100)
    reason_for_the_appointment=models.CharField(max_length=100)
    otp_number=models.CharField(max_length=20)


    

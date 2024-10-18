from django.db import models

class Lead(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(blank=True, null=True)
    phone = models.CharField(max_length=15)
    course = models.CharField(max_length=100)

    CONSULTOR_CHOICES = [
        ('Marisa Rodrigues', 'Marisa Rodrigues'),
        ('Jacob Ambrósio', 'Jacob Ambrósio'),
        ('Vito Leal', 'Vito Leal'),
        ('Larissa Lari', 'Larissa Lari'),
        ('Thiago Gomes', 'Thiago Gomes'),
    ]

    consultores = models.CharField(
        max_length=50,
        choices=CONSULTOR_CHOICES,
        default='-------------------'
    )

    def __str__(self):
        return self.name

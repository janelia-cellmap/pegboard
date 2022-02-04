from django.db import models

class Tissue(models.Model):
    type = models.CharField(max_length=300)
    short_name = models.CharField(max_length=300)

    def __str__(self):
        return self.type

class Record(models.Model):
    tissue = models.ForeignKey(Tissue, on_delete=models.CASCADE)
    last_updated = models.DateField(auto_now=True)
    created = models.DateField(auto_now_add=True)
    double_check = models.DateField()
    raw_data = models.CharField(max_length=300)
    predicition = models.CharField(max_length=300)

class Crop(models.Model):
    record = models.OneToOneField(Record, on_delete=models.CASCADE)
    number = models.IntegerField()
    short_name = models.CharField(max_length=300)

    def __str__(self):
        return self.short_name

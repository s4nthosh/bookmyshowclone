from django.db import models
from django.core.validators import MaxValueValidator
from django.urls import reverse
import datetime
import os




class movies(models.Model):
    name=models.CharField(max_length=50)
    banner_1=models.ImageField(null=True,blank=True)
    banner_2=models.ImageField(null=True,blank=True)
    banner_3=models.ImageField(null=True,blank=True)
    banner_4=models.ImageField(null=True,blank=True)

    def __str__(self):
        return self.name

class list_mov(models.Model):
    movie=models.ForeignKey(movies,on_delete=models.CASCADE)
    name=models.CharField(max_length=100,null=False)
    img = models.ImageField()
    Description=models.CharField(max_length=50)

    def __str__(self):
        return self.name


class main(models.Model):
    movie=models.ForeignKey(list_mov,on_delete=models.CASCADE)
    name=models.CharField(max_length=100)
    background=models.ImageField()
    image=models.ImageField()
    Description=models.TextField(max_length=200)
    About=models.TextField(max_length=500)
    
    def __str__(self):
        return self.name


class theater(models.Model):
    theater_name=models.CharField(max_length=200,null=False)
    location=models.CharField(max_length=200,null=False)    

    def __str__(self):
        return self.theater_name

class theaters(models.Model):
    movie=models.ForeignKey(main,on_delete=models.CASCADE)
    theater_name=models.ForeignKey(theater,on_delete=models.CASCADE)
    
    def __str__(self):
        return self.movie.name


    

class date_time(models.Model):
    movie=models.ForeignKey(main,on_delete=models.CASCADE)
    theater_name=models.ForeignKey(theater,on_delete=models.CASCADE)
    date=models.CharField(max_length=200,null=False)
    time=models.CharField(max_length=200,null=False)

    def __str__(self):
        return self.theater_name.theater_name
    

    

class cast_crew(models.Model):
    options=(('cast','cast'),('crew','crew'))
    movie=models.ForeignKey(main,on_delete=models.CASCADE)
    name=models.CharField(max_length=200)
    category=models.CharField(max_length=200,null=False,choices=options)
    profile=models.ImageField()

    def __str__(self):
        return self.name


class seats(models.Model):
    name=models.CharField(max_length=1,null=False)
    seat_type=models.CharField(max_length=100,null=True,blank=True)
    row_num = models.PositiveSmallIntegerField(null=False, blank=False)
    price = models.IntegerField(null=False,blank=False)



    def __str__(self):
        return self.name


class save_details(models.Model):
    row=models.CharField(max_length=50,null=False,blank=False)
    

  
    
from django.db import models

# Create your models here.

class Pol(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title

class Student_parent(models.Model):
    title = models.CharField(max_length=100,blank=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    middle_name = models.CharField(max_length=100,blank=True)
    iin = models.IntegerField(default=0, max_length=12)
    number = models.CharField(max_length=15)
    number2 = models.CharField(max_length=15, blank=True)
    # birth_day = models.DateField()
    status = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.title} >>>{self.first_name} {self.last_name} {self.middle_name}'

class Doljnost(models.Model):
    title = models.CharField(max_length=300)

    def __str__(self):
        return self.title


class InfoTeacher(models.Model):
    first_name = models.CharField(max_length=300)
    last_name = models.CharField(max_length=300)
    middle_name = models.CharField(max_length=300,blank=True)
    iin = models.IntegerField(default=0)
    birth_day = models.DateField()
    doljnost = models.ForeignKey(Doljnost, on_delete=models.CASCADE ,blank=True, null=True )
    photo = models.ImageField(upload_to='upload')
    address = models.TextField()
    number = models.CharField(max_length=15)
    number2 = models.CharField(max_length=15,blank=True,default=0)
    email = models.CharField(max_length=60)
    id_prikaz = models.CharField(max_length=60)
    data_prikaz = models.DateField()
    status = models.IntegerField(default=0)


    def __str__(self):
        return f'{self.first_name} {self.last_name} {self.middle_name} {self.doljnost}'





class  Sinf(models.Model):
    title = models.CharField(max_length=300,blank=True)
    stage = models.IntegerField(max_length=2)
    symbol = models.CharField(max_length=2)
    leader = models.ForeignKey(InfoTeacher,related_name='rahbar', on_delete=models.CASCADE,limit_choices_to={'doljnost': 1})
    tar1 = models.ForeignKey(InfoTeacher,related_name='tarbiyachi1', on_delete=models.CASCADE,limit_choices_to={'doljnost': 2})
    tar2 = models.ForeignKey(InfoTeacher,related_name='tarbiyachi2', on_delete=models.CASCADE,limit_choices_to={'doljnost': 2})
    amount_student = models.IntegerField(max_length=2)


    def __str__(self):
        return f'{self.stage} - {self.symbol}'

class Diagnoz(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return self.title

class Student(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    middle_name = models.CharField(max_length=100,blank=True)
    iin = models.IntegerField(default=0)
    birth_day = models.DateField()
    diagnoz = models.ForeignKey(Diagnoz,on_delete=models.CASCADE,blank=True)
    sinf = models.ForeignKey(Sinf,on_delete=models.CASCADE,blank=True)
    pol = models.ForeignKey(Pol, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='upload')
    address = models.TextField()
    # parent = models.ManyToManyField(Student_parent,null=True,blank=True)
    parents = models.ManyToManyField(Student_parent,null=True,blank=True)
    status = models.IntegerField(default=0)
    status = models.IntegerField

    def __str__(self):
        return f'{self.first_name} {self.last_name} {self.middle_name}'



class Subject(models.Model):
    title = models.CharField(max_length=300)
    status = models.IntegerField(default=0)

    def __str__(self):
        return self.title


class Corpus(models.Model):
    title = models.CharField(max_length=300)
    status = models.IntegerField(default=0)

    def __str__(self):
        return self.title


class Cabinet(models.Model):
    title = models.CharField(max_length=300)
    floor = models.IntegerField(default=0)
    corpus = models.ForeignKey(Corpus, on_delete=models.CASCADE)
    status = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.title}-каб {self.floor}-этаж {self.corpus}'


class Lesson(models.Model):
    title = models.CharField(max_length=300,blank=True)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE,blank=True,null=True)
    cabinet = models.ForeignKey(Cabinet, on_delete=models.CASCADE)
    teacher = models.ForeignKey(InfoTeacher, on_delete=models.CASCADE)
    sinf = models.ForeignKey(Sinf, on_delete=models.CASCADE)
    status = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.title} > {self.sinf}'

class Week(models.Model):
    title = models.CharField(max_length=300)

    def __str__(self):
        return self.title

class LessonTime(models.Model):
    title = models.CharField(max_length=300)
    lesson_id = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    week_day = models.ForeignKey(Week, on_delete=models.CASCADE)
    start_time = models.TimeField()
    stop_time = models.TimeField()
    status = models.IntegerField(default=0)


    def __str__(self):
        return f'{self.lesson_id.subject} {self.lesson_id.sinf} {self.start_time} {self.stop_time}'
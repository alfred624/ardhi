from django.db import models
# Create your models here.
class Department(models.Model):
    DEPARTMENT_CHOICES=[
        ('Department of Building Economics','Department of Building Economics'),
        ('Department of Interior Designs','Department of Interior Designs'),
        ('Department of Bussiness studies','Department of Bussiness studies'),
        ('Department of Environmental Science and Management','Department of Environmental Science and Management'),
        ('Department of Architecture','Department of Architecture'),
        ('Department of Land Management and Valuation','Department of Land Management and Valuation'),
        ('Department of Geospatial Sciences and Technology','Department of Geospatial Sciences and Technology'),
        ('Department of Urban and Regional Planning','Department of  Urban and Regional Planning'),
        ('Department of Civil and Environmental Engineering','Department of Civil and Environmental Engineering'),
        ('Department of Computer Systems and Mathematics','Department of Computer Systems and Mathematics'),
        ('Department of Economics and Social Studies','Department of Economics and Social Studies'),  
    ]
    department_name=models.CharField(max_length=255,choices=DEPARTMENT_CHOICES)
    def __str__(self):
        return self.department_name

class Course(models.Model):
    department=models.ForeignKey(Department,on_delete=models.CASCADE,null=True, blank=True)
    COURSE_CHOICES=[
        ('cs','cs'),
        ('cnice','cnice'),
        ('',''),
        ('',''),
        ('',''),
        ('',''),
        ('',''),
        ('',''),
        ('',''),
        ('',''),
    ]
    course_name=models.CharField(max_length=255,choices=COURSE_CHOICES,default='unknown')
    code=models.CharField(max_length=255)
    credits=models.IntegerField()
    def __str__(self):
        return f"{self.code}-{self.course_name}-{self.credits}"
    
class Programme(models.Model):
    course=models.ForeignKey(Course,on_delete=models.CASCADE,null=True, blank=True)
    department=models.OneToOneField(Department,on_delete=models.CASCADE,null=True, blank=True)
    name=models.CharField(max_length=255)
    def __str__(self):
        return f"{self.name}"

class Lecturer(models.Model):
    programme=models.ForeignKey(Programme,on_delete=models.CASCADE,null=True, blank=True)
    course=models.ForeignKey(Course,on_delete=models.CASCADE,null=True, blank=True)
    department=models.ForeignKey(Department,on_delete=models.CASCADE,null=True, blank=True)
    name=models.CharField(max_length=255)
    email=models.EmailField()
    type=models.CharField(max_length=255)
    def __str__(self):
        return f"{self.name}-{self.email}-{self.type}"
    
class Room(models.Model):
    lecturer=models.ForeignKey(Lecturer,on_delete=models.CASCADE,null=True, blank=True)
    programme=models.ForeignKey(Programme,on_delete=models.CASCADE,null=True, blank=True)
    course=models.ForeignKey(Course,on_delete=models.CASCADE,null=True, blank=True)
    department=models.ForeignKey(Department,on_delete=models.CASCADE,null=True, blank=True)
    name=models.CharField(max_length=255)
    CAPACITY_CHOICES=[
        ('R1(#120)','R1(#120)'),
        ('R3(#120)','R3(#120)'),
        ('R4(#120)','R4(#120)'),
        ('R5(#35)','R5(#35)'),
        ('R11(#84)','R11(#84)'),
        ('R12(#81)','R12(#81)'),
        ('R13(#84)','R13(#84)'),
        ('R14(#84)','R14(#84)'),
        ('R15(#50)','R15(#50)'),
        ('R17(#48)','R17(#48)'),
        ('R18(#80)','R18(#80)'),
        ('R19(#80)','R19(#80)'),
        ('R20(#70)','R20(#70)'),
        ('R21(#48)','R21(#48)'),
        ('R22(#48)','R22(#48)'),
        ('R23(#70)','R23(#70)'),
        ('R24(#70)','R24(#70)'),
        ('R25(#24)','R25(#24)'),
        ('R29(#104)','R29(#104)'),
        ('R38 + 39(#120)','R38 + 39(#120)'),
        ('R44(#64)','R44(#64)'),
        ('R45(#80)','R45(#80)'),
        ('R46(#72)','R46(#72)'),
        ('R51(#60)','R51(#60)'),
        ('R52(#60)','R52(#60)'),
        ('R53(#70)','R53(#70)'),
        ('R54(#60)','R54(#60)'),
        ('R55(#130)','R55(#130)'),
        ('R56(#130)','R56(#130)'),
        ('57(#130)','57(#130)'),
        ('R58(#130)','R58(#130)'),
        ('R59(#50)','R59(#50)'),
        ('R60(#50)','R60(#50)'),
        ('R61(#80)','R61(#80)'),
        ('R62(#130)','R62(#130)'),
        ('R63(#130)','R63(#130)'),
        ('R64(#50)','R64(#50)'),
        ('R65(#50)','R65(#50)'),
        ('R66(#80)','R66(#80)'),
        ('R67(#130)','R67(#130)'),
        ('R68(#130)','R68(#130)'),
        ('R69(#50)','R69(#50)'),
        ('R70(#50)','R70(#50)'),
        ('R71(#82)','R71(#82)'),
        ('R72Venue(#82)','R72Venue(#82)'),
        ('R73(#82)','R73(#82)'),
        ('R74(#82)','R74(#82)'),
        ('R75(#82)','R75(#82)'),
        ('R76(#313)','R76(#313)'),
        ('R50-LAB','R50-LAB'),
        ('R49-LAB','R49-LAB'),
        ('R31-LAB','R31-LAB'),
        ('EE LAB - LAB2','EE LAB - LAB2'),
        ('R32-LAB','R32-LAB'),
        ('R33-LAB','R33-LAB'),
        ('R34-LAB','R34-LAB'),
        ('Experimental Hall - Hall','Experimental Hall - Hall'),
        ('ARCH WORKSHOP - WORKSHOP','ARCH WORKSHOP - WORKSHOP'),
    ]
    capacity=models.CharField(max_length=255,choices=CAPACITY_CHOICES)
    def __str__(self):
        return f"{self.name}-{self.capacity}"
    
class Timetable(models.Model):
    lecturer=models.OneToOneField(Lecturer,on_delete=models.CASCADE)
    programme=models.OneToOneField(Programme,on_delete=models.CASCADE)
    course=models.OneToOneField(Course,on_delete=models.CASCADE)
    department=models.OneToOneField(Department,on_delete=models.CASCADE)
    room=models.ForeignKey(Room,on_delete=models.CASCADE)
    year=models.PositiveIntegerField()
    TYPE_CHOICES=[
        ('Teaching Timetable','Teaching Timetable'),
        ('Examination Timetable','Examination Timetable'),
    ]
    type=models.CharField(max_length=255,choices=TYPE_CHOICES)
    SEMISTER_CHOICES=[
        ('Teaching Timetable','Teaching Timetable'),
        ('Examination Timetable','Examination Timetable'),
    ]
    semister=models.CharField(max_length=255,choices=SEMISTER_CHOICES)
    DAY_CHOICES=[
        ('Monday', 'Monday'),
        ('Tuesday', 'Tuesday'),
        ('Wednesday', 'Wednesday'),
        ('Thursday', 'Thursday'),
        ('Friday', 'Friday'),
    ]
    date=models.DateField()
    day=models.CharField(max_length=255,choices=DAY_CHOICES)
    start_time=models.TimeField()
    end_time=models.TimeField()
    updated_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.year}-{self.type}-{self.semister}-{self.date}-{self.day}-{self.start_time}-{self.end_time}-{self.updated_at}"

class Approval(models.Model):
    approved_by=models.CharField(max_length=200)
    approved_date=models.DateTimeField(auto_created=True)
    
    def __str__(self):
        return f"{self.approved_by}-{self.approved_date}"

    
    
from django.db import models

from django.utils import timezone
#from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.contrib.auth.models import User

#------------------------------
#------ USERS
#------------------------------

"""
class CustomUserManager(BaseUserManager):

    def _create_user(self, email, password,
       is_staff, is_superuser, **extra_fields):

        ""
        Creates and saves a User with the given email and password.
        ""

        now = timezone.now()
        if not email:
            raise ValueError('The given email must be set')
            email = self.normalize_email(email)
            user = self.model(email=email,
              is_staff=is_staff, is_active=True,
              is_superuser=is_superuser, last_login=now,
              date_joined=now, **extra_fields)
            user.set_password(password)
            user.save(using=self._db)
            return user

        def create_user(self, email, password=None, **extra_fields):
            return self._create_user(email, password, False, False,
                   **extra_fields)

        def create_superuser(self, email, password, **extra_fields):
            return self._create_user(email, password, True, True,
                       **extra_fields)


class InvestigaUser(AbstractBaseUser, PermissionsMixin):
    first_name = models.CharField('First Name', max_length=200)
    last_name = models.CharField('Last Name', max_length=200)
    email = models.EmailField('Email', max_length=254, unique=True)
    is_staff = models.BooleanField('staff', default=False,
        help_text='Designates whether the user can log into this admin '
        )
    is_active = models.BooleanField('active', default=True,
        help_text='Designates whether this user should be treated as '
        'active. Unselect this instead of deleting accounts.')
    date_joined = models.DateTimeField('Fecha de inscripcion', default=timezone.now)
    objects = CustomUserManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name','last_name']

    def get_full_name(self):
        full_name = '%s %s' % (self.first_name, self.last_name)
        return full_name.strip()
    
    def get_short_name(self):
        return self.first_name
    
    def __str__(self):
        return self.email
"""

#------------------------------
#------------------------------

#------ START class Scientist
class Scientist(models.Model):

    ACADEMIC_DEGREES = (
        ('MAG','Master'),
        ('PHD','PhD'),
        ('MD','MD'),
        )

    OCCUPATION = (
        ('PHD_EST','PhD Student'),
        ('REAS_ASS','Research Assistant'),
        ('POST_DOC','Postdoctoral Researcher'),
        ('REAS_DIR','Research Lab. Director'),
        ('REAS','Researcher'),
        ('PROF','Professor'),
        ('R&D_ENG','R&D Engineer'),
        ('IND','Independent Researcher'),
        )


    user = models.OneToOneField(User)

    academic_degree = models.CharField(max_length=10,choices=ACADEMIC_DEGREES,verbose_name='Academic Degree',blank=False)
    academic_field = models.ForeignKey('AcademicDiscipline')

    country_residence = models.ForeignKey('Country')
    
    current_occupation = models.CharField(max_length=40,verbose_name='Occupation',blank=False)
    working_place = models.CharField(max_length=40,verbose_name='Working Place',blank=False)
    languages = models.CharField(max_length=50,verbose_name='Languages', blank=True)

    personal_website = models.CharField(max_length=30, verbose_name='Website', blank=True)
    researchgate_profile = models.CharField(max_length=30, verbose_name='ResearchGate', blank=True)
    linkedin_profile = models.CharField(max_length=30, verbose_name='LinkedIn', blank=True)
    twitter_username = models.CharField(max_length=15, verbose_name='Twitter', blank=True)
    facebook_profile = models.CharField(max_length=30, verbose_name='Facebook', blank=True)

    referenced_by = models.CharField(max_length=150,verbose_name='Referenced by',blank=False)
    
    is_verified = models.BooleanField(verbose_name="Verified Researcher?")


    def __str__(self):
        return '%s %s' % self.user.first_name, self.user.last_name

#------ END class Scientist

#------------------------------
#------------------------------

#------ START class SchoolTeacher
class SchoolTeacher(models.Model):

    user = models.OneToOneField(User)
    school = models.ForeignKey('School')

    degree = models.CharField(max_length=20,verbose_name='Degree',blank=False)
    subjects = models.CharField(max_length=40,verbose_name='Subjects',blank=False)    
    
    telephone = models.CharField(max_length=25, verbose_name='Telephone')

    twitter_username = models.CharField(max_length=15, verbose_name='Twitter', blank=True)
    facebook_profile = models.CharField(max_length=30, verbose_name='Facebook', blank=True)
    
    has_IT_training = models.BooleanField(verbose_name="Has IT training?")


    def __str__(self):
        return '%s %s' % self.user.first_name, self.user.last_name

#------ END class SchoolTeacher

#------------------------------
#------------------------------

#------ START class Moderator
class Moderator(models.Model):

    user = models.OneToOneField(User)    
    report = models.CharField(max_length=500,verbose_name='Report',blank=False)    
    
    def __str__(self):
        return '%s %s' % self.user.first_name, self.user.last_name

#------ END class Moderator

#------------------------------
#------ SCIENCE
#------------------------------


#------ START class ScienceField 

class ScienceField(models.Model):

    SCIENCE_FIELD = (
        ('LIFE','Life Sciences'),
        ('APPL','Applied Sciences'),
        ('SOCIAL','Social Sciences'),
        ('PHYS','Physical Sciences'),
        )

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30, choices=SCIENCE_FIELD, verbose_name='Science Field')
    description = models.CharField(max_length=300,verbose_name='Description')

    def __str__(self):
        return self.name
        
#------ END class ScienceField

#------------------------------
#------------------------------

#------ START class AcademicDiscipline 

class AcademicDiscipline(models.Model):

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50,  verbose_name='Academic Discipline')
    academic_discipline = models.ForeignKey('ScienceField')

    def __str__(self):
        return self.name
        
#------ END class AcademicDiscipline

#------------------------------
#------------------------------

#------ START class Country 
class Country(models.Model):

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50,  verbose_name='Country')

    def __str__(self):
        return self.name
        
#------ END class Country

#------------------------------
#------------------------------

#------------------------------
#------ SCHOOLS
#------------------------------

#------ START class School
class School(models.Model):

    SCHOOL_LEVELS = (
        ('ELEMS','Elementary School'),
        ('PRIMS','Primary School'),
        ('SECUS','Secondary School'),
        )

    # Location
    department = models.CharField(max_length=30,verbose_name='Department')
    # Town
    town = models.CharField(max_length=30,verbose_name='Town')
    
    max_level = models.CharField(max_length=20,choices=SCHOOL_LEVELS,verbose_name='Max. level')

    director_fullname = models.CharField(max_length=25, verbose_name='Full name School director')
    address = models.CharField(max_length=300,verbose_name='Address')
    telephone = models.CharField(max_length=25, verbose_name='Telephone')
    email = models.EmailField(max_length=254, verbose_name='School email')

    facebook_url = models.CharField(max_length=20, verbose_name='Facebook', blank=True)
    school_website = models.CharField(max_length=20, verbose_name='Website', blank=True)

    has_projector = models.BooleanField(verbose_name="Has projector?")
    has_screen = models.BooleanField(verbose_name="Has screen?")
    has_webcam = models.BooleanField(verbose_name="Has webcam?")
    has_videoconf_room = models.BooleanField(verbose_name="Has videoconf room?")
    has_microphone = models.BooleanField(verbose_name="Has microphone?")
    has_speakers = models.BooleanField(verbose_name="Has speakers?")

    def __str__(self):
        return self.user.username

#------ END class School

#------------------------------
#------------------------------

#------------------------------
#------ SESSIONS
#------------------------------

#------ START class VideoconfSession 
class VideoconfSession(models.Model):
    STATUS_SCHOOL = (
        ('CANCEL','Cancelled'),
        ('VER_REQ','To verify requirements'),
        ('TO_SCH','To be scheduled'),
        ('SCHED','Scheduled'),
        ('IN_PROG','In progress'),
        ('COMPLET','Completed'),
        )
    STATUS_SCIENTIST = (
        ('CANCEL','Cancelled'),
        ('READING','Preparing reading'),
        ('TRAIN','Training'),
        ('TO_SCH','To be scheduled'),
        ('SCHED','Scheduled'),
        ('IN_PROG','In progress'),
        ('COMPLET','Completed'),
        )
    id = models.AutoField(primary_key=True)
    selected_date = models.DateField()
    selected_hour = models.DateTimeField()
    status_school = models.CharField(max_length=7, choices=STATUS_SCHOOL, verbose_name='Status school')
    status_scientist = models.CharField(max_length=7, choices=STATUS_SCIENTIST, verbose_name='Status scientist')
    school_teacher = models.ForeignKey('SchoolTeacher')
    scientist = models.ForeignKey('Scientist')
    moderator = models.ForeignKey('Moderator')

#------ END class VideoconfSession

#------------------------------
#------------------------------
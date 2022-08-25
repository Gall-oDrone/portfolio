from django.db import models
from django_resized import ResizedImageField
from django_countries.fields import CountryField
from django.core.validators import RegexValidator
from constants import *


class Universities(models.Model):
    thumbnail = models.ImageField(
        upload_to="images/logos/institution/", blank=True)
    university = models.CharField(
        max_length=100, choices=UNIVERSITIES, blank=True)

    def __str__(self):
        return self.university


class Degree(models.Model):
    UNDERGRADUATE = "Undergraduate"
    BACHELOR = "Bachelor's degree"
    MASTER = "Master's degree"
    DOCTORATE = "Doctorate"
    OTHER = "Other"
    DEGREES = [
        (UNDERGRADUATE, ('U')),
        (BACHELOR, ('B')),
        (MASTER, ('M')),
        (DOCTORATE, ('pHd')),
        (OTHER, ('Other')),
    ]
    degree = models.CharField(max_length=100, choices=DEGREES, blank=True)

    def __str__(self):
        return self.degree


class Bachelor(models.Model):
    bachelor_degree = models.CharField(
        max_length=100, choices=BACHELOR_DEGREES, blank=True)

    def __str__(self):
        return self.bachelor_degree


class Master(models.Model):
    master_degree = models.CharField(
        max_length=100, choices=MASTER_DEGREES, blank=True)

    def __str__(self):
        return self.master_degree


class Doctorate(models.Model):
    pHd_degree = models.CharField(
        max_length=100, choices=PHD_DEGREES, blank=True)

    def __str__(self):
        return self.pHd_degree


class Course(models.Model):
    course = models.CharField(max_length=100, choices=COURSES, blank=True)

    def __str__(self):
        return self.course


class UserUndergraduate(models.Model):
    course = models.ForeignKey(
        Course, related_name="user_resume_course", on_delete=models.CASCADE)
    from_date = models.DateTimeField(auto_now_add=False)
    to_date = models.DateTimeField(auto_now_add=False)
    institution = models.CharField(
        max_length=100, choices=UNIVERSITIES, blank=True)


class UserBachelor(models.Model):
    degree = models.CharField(
        max_length=100, choices=BACHELOR_DEGREES, blank=True)
    from_date = models.DateTimeField(auto_now_add=False)
    to_date = models.DateTimeField(auto_now_add=False)
    institution = UNIVERSITIES


class UserMaster(models.Model):
    degree = models.CharField(
        max_length=100, choices=MASTER_DEGREES, blank=True)
    from_date = models.DateTimeField(auto_now_add=False)
    to_date = models.DateTimeField(auto_now_add=False)
    institution = UNIVERSITIES


class UserDoctorate(models.Model):
    degree = models.CharField(max_length=100, choices=PHD_DEGREES, blank=True)
    from_date = models.DateTimeField(auto_now_add=False)
    to_date = models.DateTimeField(auto_now_add=False)
    institution = UNIVERSITIES


class UserDiplomaOrCertificate(models.Model):
    diploma = models.CharField(max_length=100, choices=DIPLOMAS, blank=True)
    certificate = models.CharField(
        max_length=100, choices=CERTIFICATES, blank=True)
    from_date = models.DateTimeField(auto_now_add=False)
    to_date = models.DateTimeField(auto_now_add=False)
    institution = UNIVERSITIES


class ContactForm(models.Model):
    form = models.CharField(max_length=100, choices=CONTACT_FORMS, blank=True)
    value = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.form


class Language(models.Model):
    langauge = models.CharField(max_length=100, choices=LANGUAGES, blank=True)
    level = models.CharField(
        max_length=100, choices=LANGUAGE_LEVELS, blank=True)

    def __str__(self):
        return "Language: {}, level: {}".format(self.langauge, self.level)


class PhoneModel(models.Model):
    phone_regex = RegexValidator(
        regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone_number = models.CharField(
        validators=[phone_regex], max_length=17, blank=True)
    phone_type = models.CharField(
        verbose_name="Type", max_length=50, choices=PHONE_TYPES, blank=True)

    def __str__(self):
        return "{}".format(self.phone_number)


class PersonalInfo(models.Model):
    firstname = models.CharField(max_length=50, blank=True)
    lastname = models.CharField(max_length=50, blank=True)
    # TOADD: Date of birth
    profession = models.CharField(max_length=50, blank=True)
    phone = models.ManyToManyField(
        PhoneModel, related_name="personal_phone", blank=True, null=True)
    about_me = models.TextField(max_length=500, blank=True)

    def __str__(self):
        return "{} {} personal info".format(self.firstname, self.lastname)


class Education(models.Model):
    academic_degree = models.ManyToManyField(Degree, null=True, blank=True)
    undergrad = models.ForeignKey(
        UserUndergraduate, null=True, blank=True, on_delete=models.CASCADE)
    bachelor = models.ManyToManyField(UserBachelor, null=True, blank=True)
    master = models.ManyToManyField(UserMaster, null=True, blank=True)
    phd = models.ManyToManyField(UserDoctorate, null=True, blank=True)
    other_edu = models.ManyToManyField(
        UserDiplomaOrCertificate, null=True, blank=True)


class JobActivityDescription(models.Model):
    job_desc = models.TextField(max_length=500, blank=True)


class TechnologyUsed(models.Model):
    technology = models.CharField(
        max_length=100, choices=TECHNOLOGIES, blank=True)
    image = ResizedImageField(
        size=[66, 66], quality=75, upload_to='images/logos/technology/', null=True, blank=True)


class SkillUsed(models.Model):
    skill = models.CharField(max_length=100, choices=SKILLS, blank=True)


class JobPosition(models.Model):
    position = models.CharField(
        max_length=100, choices=JOB_POSITIONS, blank=True)
    enterprise = models.CharField(
        max_length=100, choices=JOB_POSITIONS, blank=True)
    location = models.CharField(
        max_length=100, choices=JOB_POSITIONS, blank=True)
    from_date = models.DateTimeField(auto_now_add=False)
    to_date = models.DateTimeField(auto_now_add=False)
    job_activities_desc = models.ManyToManyField(
        JobActivityDescription, blank=True)
    technologies_used = models.ManyToManyField(TechnologyUsed, blank=True)
    skills_used = models.ManyToManyField(SkillUsed, blank=True)


class Employment(models.Model):
    job_positions = models.ManyToManyField(JobPosition, blank=True)
    resume = models.FileField(upload_to="files/resume",
                              null=True, verbose_name="Resume")


class ProfileInfo(models.Model):
    personal = models.ForeignKey(
        PersonalInfo, related_name="personal_info", on_delete=models.CASCADE, blank=True, null=True)
    picture = models.ImageField(upload_to="profile/", blank=True)
    country = CountryField(blank_label='(select country)')
    university = models.ForeignKey(
        Universities, on_delete=models.CASCADE, related_name="profile_university")

    education = models.ForeignKey(
        Education, on_delete=models.CASCADE, related_name="user_education", blank=True, null=True)
    undergraduate = models.BooleanField(default=False)
    graduate = models.BooleanField(default=False)
    postgraduate = models.BooleanField(default=False)

    employment = models.ForeignKey(
        Employment, on_delete=models.CASCADE, related_name="user_employment", blank=True, null=True)
    profesional_experience = models.BooleanField(default=False)
    job_position = models.CharField(max_length=400, blank=True, null=True)

    contact_forms = models.ManyToManyField(
        ContactForm, related_name="user_contactform", blank=True, null=True)
    langauges = models.ManyToManyField(
        Language, related_name="user_language", blank=True, null=True)
    website = models.CharField(max_length=50, blank=True, null=True)
    message = models.CharField(max_length=150, blank=True, null=True)
    github = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return "{} {} profile info".format(self.personal.firstname, self.personal.lastname)

    def image_picture(self):
        return self.picture

from django.contrib.sites.models import Site
from constants import TECHNOLOGIES
from rest_framework import serializers
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from .models import (
        ContactForm,
        Universities, 
        ProfileInfo, 
        Degree, 
        Bachelor, 
        Master, 
        Doctorate, 
        Course, 
        PersonalInfo,
        Education,
        JobActivityDescription,
        TechnologyUsed,
        SkillUsed,
        JobPosition,
        Employment,
        UserUndergraduate,
        UserBachelor,
        UserMaster,
        UserDoctorate,
        UserDiplomaOrCertificate,
        PhoneModel,
        Language
    )

class StringSerializer(serializers.StringRelatedField):
    def to_internal_value(self, value):
        return value

class PhoneSerializer(serializers.ModelSerializer):
    phone_number = serializers.SerializerMethodField()
    phone_type = StringSerializer()
    class Meta:
        model = PhoneModel
        fields = ("__all__")
    
    def get_phone_number(self, instance):
        profile_phone = "52"+instance.phone_number
        return profile_phone

class LanguageSerializer(serializers.ModelSerializer):
    langauge = StringSerializer()
    level = StringSerializer()
    class Meta:
        model = Language
        fields = ("__all__")

class PersonalInfoSerializer(serializers.ModelSerializer):
    firstname = StringSerializer()
    lastname = StringSerializer()
    phone = PhoneSerializer(many=True)
    profesion = StringSerializer()
    about_me = StringSerializer()
    class Meta:
        model = PersonalInfo
        fields = ("__all__")

class universitySerializer(serializers.ModelSerializer):
    university = StringSerializer(many=False)
    class Meta:
        model = Universities
        fields = ("university", "thumbnail")

class degreeSerializer(serializers.Serializer):
    class Meta:
        model = Degree
        fields = ("__all__")

class bachelor_degreeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bachelor
        fields = ("__all__")

class master_degreeSerializer(serializers.ModelSerializer):
    # type = serializers.ChoiceField(choices= Master.MASTER_DEGREES)

    class Meta:
        model = Master
        fields = ("__all__")

class pHd_degreeSerializer(serializers.ModelSerializer):
    # type = serializers.ChoiceField(choices= Doctorate.PHD_DEGREES)

    class Meta:
        model = Doctorate
        fields = ("__all__")

class courseSerializer(serializers.ModelSerializer):
    # type = serializers.ChoiceField(choices= Course.COURSES)

    class Meta:
        model = Course
        fields = ("__all__")

class UserUndergraduateSerializer(serializers.ModelSerializer):
    course = courseSerializer()
    from_date = StringSerializer()
    to_date = StringSerializer()
    student_type = StringSerializer()
    # institution = UniSerializer()

    class Meta:
        model = UserUndergraduate
        fields = ("__all__")

class UserBachelorSerializer(serializers.ModelSerializer):
    ##TOFIX
    degree = bachelor_degreeSerializer()
    from_date = StringSerializer()
    to_date = StringSerializer()
    # institution = StringSerializer()

    class Meta:
        model = UserBachelor
        fields = ("__all__")

class UserMasterSerializer(serializers.ModelSerializer):
    degree = master_degreeSerializer()
    from_date = StringSerializer()
    to_date = StringSerializer()
    # institution = StringSerializer()
    class Meta:
        model = UserMaster
        fields = ("__all__")

class UserDoctorateSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserDoctorate
        fields = ("__all__")

class UserDiplomaOrCertificateSerializer(serializers.ModelSerializer):
    diploma = pHd_degreeSerializer()
    certificate = StringSerializer()
    from_date = StringSerializer()
    to_date = StringSerializer()
    # institution = StringSerializer()
    class Meta:
        model = UserDiplomaOrCertificate
        fields = ("__all__")

class EducationSerializer(serializers.ModelSerializer):
    academic_degree = StringSerializer()
    undergrad = UserUndergraduateSerializer()
    bachelor = StringSerializer()
    master = StringSerializer()
    phd = StringSerializer()
    other_edu = StringSerializer()
    class Meta:
        model = Education
        fields = ("__all__")

class JobActivityDescriptionSerializer(serializers.ModelSerializer):
    job_desc = StringSerializer()
    class Meta:
        model = JobActivityDescription
        fields = ("__all__")

class TechnologyUsedSerializer(serializers.ModelSerializer):
    technology = serializers.ChoiceField(choices=TECHNOLOGIES)
    image = serializers.SerializerMethodField()
    class Meta:
        model = TechnologyUsed
        fields = ("__all__")

    def get_image(self, instance):
        request = self.context.get('request')
        print("magic: ", instance.image, type(instance.image), instance.image=="")
        if(instance.image!=""):
            image_url = instance.image.url
            return request.build_absolute_uri(image_url)
        return None

class SkillUsedSerializer(serializers.ModelSerializer):
    class Meta:
        model = SkillUsed
        fields = ("__all__")

class JobPositionSerializer(serializers.ModelSerializer):
    job_activities_desc = JobActivityDescriptionSerializer(many=True)
    technologies_used = TechnologyUsedSerializer(many=True)
    skills_used = SkillUsedSerializer(many=True)
    class Meta:
        model = JobPosition
        fields = ("__all__")

class EmploymentSerializer(serializers.ModelSerializer):
    job_positions = JobPositionSerializer(many=True)
    resume = StringSerializer()
    class Meta:
        model = Employment
        fields = ("__all__")

class FetchDataSerializer(serializers.ListSerializer):
    child = serializers.ListField(child=serializers.CharField())
    allow_null = False
    many = True
    
class testSerializer(serializers.Serializer):
    degree = serializers.SerializerMethodField()
    bachelor = serializers.SerializerMethodField()
    master = serializers.SerializerMethodField()
    pHD = serializers.SerializerMethodField()
    course = serializers.SerializerMethodField()
    university = serializers.SerializerMethodField()

    def get_degree(self, obj):
        ob = []
        for d in Degree.DEGREES:
            ob.append({"value": d[1], "label": d[0]})
        obj = ob
        return obj
    def get_bachelor(self, obj):
        ob = []
        for d in Bachelor.BACHELOR_DEGREES:
            ob.append({"value": d[0], "label": d[0]})
        obj = ob
        return obj
    def get_master(self, obj):
        ob = []
        for d in Master.MASTER_DEGREES:
            ob.append({"value": d[0], "label": d[0]})
        obj = ob
        return obj
    def get_pHD(self, obj):
        ob = []
        for d in Doctorate.PHD_DEGREES:
            ob.append({"value": d[0], "label": d[0]})
        obj = ob
        return obj
    def get_course(self, obj):
        ob = []
        for d in Course.COURSES:
            ob.append({"value": d[0], "label": d[0]})
        obj = ob
        return obj
    def get_university(self, obj):
        ob = []
        for u in Universities.UNIVERSITIES:
            ob.append({"value": u[0], "label": u[0]})
        obj = ob
        return obj
    
    class Meta:
        fields = (
            "degree",
            "bachelor",
            "master",
            "pHD",
            "course",
            "university",
            "data"
        )

class testSerializer2(serializers.Serializer):
    degree = serializers.SerializerMethodField()
    bachelor = serializers.SerializerMethodField()
    def get_degree(self, obj):
        obj = Degree.DEGREES
        return obj
    def get_bachelor(self, obj):
        obj = Bachelor.BACHELOR_DEGREES
        return obj
    def get_master(self, obj):
        obj = Master.MASTER_DEGREES
        return obj
    def get_pHD(self, obj):
        obj = Doctorate.PHD_DEGREES
        return obj
    def get_course(self, obj):
        obj = Course.COURSES
        return obj
    def get_university(self, obj):
        obj = Course.COURSES
        return obj
    
    class Meta:
        fields = (
            "degree",
            "bachelor"
        )

class ProfileInfoSerializer(serializers.ModelSerializer):
    personal = PersonalInfoSerializer(many=False)
    country = StringSerializer(many=False)
    university = StringSerializer(many=False)
    degree = StringSerializer(many=False)
    bachelor = StringSerializer(many=False)
    master = StringSerializer(many=False)
    doctorate = StringSerializer(many=False)
    course  = StringSerializer(many=False)
    employment = EmploymentSerializer(many=False)
    profesional_experience = StringSerializer(many=False)
    job_position = StringSerializer(many=False)
    website = StringSerializer(many=False)
    message = StringSerializer(many=False)
    github = StringSerializer(many=False)
    picture = serializers.SerializerMethodField()
    langauges = LanguageSerializer(many=True)
    class Meta:
        model = ProfileInfo
        fields = ("__all__")
    
    def get_picture(self, obj):
        request = self.context.get('request')
        profile_picture_url = request.build_absolute_uri(obj.picture.url)
        return profile_picture_url

    def update_account_info(self, request):
        data = request.data
        print('update_account_info data: ')
        name = "diego"
        profile = ProfileInfo.objects.get(personal_info = name)
        if(data.get("experience") != None):
            profile.personal_info.firstname = data.get("name"),
        if(data.get("experience") != None):
            profile.work_experience = data.get("experience")
        if(data.get("website") != None):
            profile.website = data.get("website")
        if(data.get("message") != None):
            profile.message = data.get("message")
        if(data.get("github") != None):
            profile.github = data.get("github")

        profile.save()
        if(data.get("university") != None):
            profile.university = Universities.objects.get(university=data.get("university"))
        if(data.get("attendace") != None):
            profile.attendace = data.get("attendace")
        if(data.get("degree") != None):
            profile.degree = Degree.objects.get(degree=data.get("degree"))
        if(data.get("bachelor") != None):
            profile.bachelor = Bachelor(bachelor_degree=data.get("bachelor"))
        if(data.get("master") != None):
            profile.master = Master.objects.get(master_degree=data.get("master"))
        if(data.get("doctorate") != None):
            profile.doctorate = Doctorate.objects.get(pHd_degree=data.get("doctorate"))
        if(data.get("course") != None):
            profile.course = Course.objects.get(course=data.get("course"))
        if(data.get("graduate") != None):
            profile.graduate = data.get("graduate")
        if(data.get("undergraduate") != None):
            profile.undergraduate = data.get("undergraduate")
        if(data.get("postgraduate") != None):
            profile.postgraduate = data.get("postgraduate")
            
        profile.save()
        return profile
    
class ProfilePageSerializer(serializers.ListSerializer):
    info = ProfileInfoSerializer

class ProfileInfoListSerializer(serializers.ListSerializer):
    child = ProfileInfoSerializer()
    allow_null = True
    many = True

class ContactFormSerializer(serializers.ModelSerializer):
    form = StringSerializer()
    value = StringSerializer()
    class Meta:
        model = ContactForm
        fields = ("form","value")

class ProfileContactFormsSerializer(serializers.ModelSerializer):
    personal = serializers.SerializerMethodField()
    contact_forms = ContactFormSerializer(many=True)

    def get_personal(self, instance):
        request = self.context.get('request')
        profile_phone = PhoneSerializer(instance.personal.phone, many=True, context={'request': request}).data
        return profile_phone
    
    class Meta:
        model = ProfileInfo
        fields = ('contact_forms', 'personal')
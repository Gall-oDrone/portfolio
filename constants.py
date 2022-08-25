from django.db import models
import urllib.request
from django.core.files.storage import FileSystemStorage

Humanities = 'humanities'
SocialSciences = 'social_sciences'
NaturalSciences = 'natural_sciences'
FormalSciences = 'formal_sciences'
AppliedSciences = 'applied_sciences'
ACADEMIC_DISCIPLINES_CHOICES = [
        (Humanities, [
            ('arts', 'Arts'),
            ('history', 'History'),
            ('home_economics', 'Home economics'),
            ('languages_literature', 'Languages and literature'),
            ('law', 'Law'),
            ('philosophy', 'Philosophy'),
            ('theology', 'Theology')
        ]),
        (SocialSciences, [
            ('anthropology', 'Anthropology'),
            ('archaeology', 'Archaeology'),
            ('economics', 'Economics'),
            ('geography', 'Geography'),
            ('political_science', 'Political science'),
            ('psychology', 'Psychology'),
            ('sociology', 'Sociology'),
            ('social_work', 'Social Work'),
        ]),
        (NaturalSciences, [
            ('biology', 'Biology'),
            ('chemistry', 'Chemistry'),
            ('earth_science', 'Earth science'),
            ('space_sciences', 'Space sciences'),
            ('physics', 'Physics'),
        ]),
        (FormalSciences, [
            ('computer_science', 'Computer Science'),
            ('mathematics', 'Mathematics'),
            ('statistics', 'Statistics'),
        ]),
        (AppliedSciences, [
            ('business', 'Business'),
            ('engineering_technology', 'Engineering and technology'),
            ('medicine_health', 'Medicine and health'),

        ]),
]

INDUSTRY_FIELDS_CHOICES = [
    ('agriculture', 'Agriculture'),
    ('artist', 'Artist'),
    ('business', 'Business'),
    ('communications', 'Communications'),
    ('education', 'Education'),
    ('engineering', 'Engineering'),
    ('environment', 'Environment'),
    ('financial', 'Financial'),
    ('government', 'Government'),
    ('health', 'Health'),
    ('legal', 'Legal'),
    ('manufacturing', 'Manufacturing'),
    ('service_sector', 'Service Sector'),
    ('technical', 'Technical'),
    ('technology ', 'Technology '),
    ('technology_non_compute', 'Technology - non-Compute'),
]

PROGRAMMER = 'programmer'
PROJECT_MANAGER = 'project_manager'
DATA_ANALYST = 'data_analyst'
BUSINESS_ANALYST = 'business_analyst'
OTHER = 'other'
COLLABORATION_POSITIONS = [
    (PROGRAMMER, ('Programmer')),
    (PROJECT_MANAGER, ('Project Manager')),
    (DATA_ANALYST, ('Data Analyst')),
    (BUSINESS_ANALYST, ('Business Analyst')),
    (OTHER, ('Other')),
]

REJECTED = 'rejected'
ACCEPTED = 'accepted'
EVALUATING = 'evaluating'
COLLABORATI_STATUS = [
    (REJECTED, ('Rejected')),
    (ACCEPTED, ('Accepted')),
    (EVALUATING, ('Evaluating')),
]

PUSH = 'push'
PULL = 'pull'
RECRUITMENT_FORM_CHOCIES = [
    (PUSH, ('Push')),
    (PULL, ('Pull')),
]

DEGREE = "degree"
PROFESSION = "profession"
ROLE_CHOICES = [
    (DEGREE, ('Degree')),
    (PROFESSION, ('Profession')),
]

import ssl
from urllib.parse import urlparse
from django.core.files.base import ContentFile
from django.core.files.temp import NamedTemporaryFile
from django.core.files import File
import base64
from django.conf import settings
ssl._create_default_https_context = ssl._create_unverified_context

url="https://www.oroyfinanzas.com/files/2015/04/mit_logo.jpg"

# current_path = os.path.dirname(__file__)
# image_folder = os.path.join(current_path, mediafiles)
# print("CACAS: ", current_path)
def create_logo(self, url, institution_name, obj):
    institution = institution_name.upper()
    # urllib.request.urlretrieve(url, '/Users/diegogallovalenzuela/djreact/Feedback-App/mediafiles/images/logos/institution/{}-logo.jpg'.format(institution_name))
    try:
        content = urllib.request.urlretrieve(url)
        name = urlparse(url).path.split('/')[-1]
        extension = name.split('.')[-1]
        print("LOGO")
        if settings.USE_S3:
            print("S3 LOGO")
            obj.thumbnail.save(institution_name+"."+extension, File(open(content[0], 'rb')), save=True)
        else:
            obj.thumbnail.save(institution_name+extension, File(open(content[0], 'rb')), save=True)
            # self.signed_file.save("{timestamp}.pdf".format(timestamp=timezone.now().strftime('%Y-%m-%d%/%H-%M-%S')), File(open(tempname, 'rb')))
    except Exception as e: 
        print("ERROR LOGO", e)
    finally:
        # urlcleanup()
        print ("CHECK")
    

# logo_MIT = InstitutionLogo.objects.get(logo="MIT-logo.jpg")
# logo_CAMBRIDGE = InstitutionLogo.objects.get(logo="MIT-logo.jpg")
# logo_OXFORD = InstitutionLogo.objects.get(logo="MIT-logo.jpg")
# logo_STANDFORD = InstitutionLogo.objects.get(logo="MIT-logo.jpg")
# logo_DUKE = InstitutionLogo.objects.get(logo="MIT-logo.jpg")
# logo_CIDE = InstitutionLogo.objects.get(logo="MIT-logo.jpg")
# logo_ITAM = InstitutionLogo.objects.get(logo="MIT-logo.jpg")
# logo_COLMEX = InstitutionLogo.objects.get(logo="MIT-logo.jpg")
# logo_ITESM = InstitutionLogo.objects.get(logo="MIT-logo.jpg")
# logo_UIA = InstitutionLogo.objects.get(logo="MIT-logo.jpg")

logo_MIT = "InstitutionLogo.objects.get(logo="
logo_CAMBRIDGE = "InstitutionLogo.objects.get(logo="
logo_OXFORD = "InstitutionLogo.objects.get(logo="
logo_STANDFORD = "InstitutionLogo.objects.get(logo="
logo_DUKE = "InstitutionLogo.objects.get(logo="
logo_CIDE = "InstitutionLogo.objects.get(logo="
logo_ITAM = "InstitutionLogo.objects.get(logo="
logo_COLMEX = "InstitutionLogo.objects.get(logo="
logo_ITESM = "InstitutionLogo.objects.get(logo="
logo_UIA = "InstitutionLogo.objects.get(logo="

MIT = 'MIT'
CAMBRIDGE = 'University of Cambridge'
OXFORD = 'University of Oxford'
STANDFORD = 'Stanford University'
DUKE = "Duke's University"
CIDE = "Center of Teaching and Research in Economics"
CIC = "Center for Computing Research"
ITAM = "Autonomous Technological Institute of Mexico "
COLMEX = "El Colegio de México"
ITESM = "Monterrey Institute of Technology and Higher Education"
UIA = " Ibero-American University"
OTHER = 'other'
UNIVERSITIES = [
    (MIT, ('Massachusetts Institute of Technology')),
    (CAMBRIDGE, ('University of Cambridge')),
    (OXFORD, ('University of Oxford')),
    (STANDFORD, ('Stanford University')),
    (DUKE, ("Duke's University")),
    (CIDE, ("Center of Teaching and Research in Economics")),
    (CIC, ("Center for Computing Research")),
    (ITAM, ("Instituto Tecnológico Autónomo de México")),
    (COLMEX, ("El Colegio de México")),
    (ITESM, ("Instituto Tecnológico y de Estudios Superiores de Monterrey")),
    (UIA, ("Universidad Iberoamericana")),
    (OTHER, ('other'))
]
# ´´`´
UNIVERSITIES_TEST = [
    # (logo_MIT, [
        (MIT, ('Massachusetts Institute of Technology')),
    # ]),
    (logo_CAMBRIDGE, [
        (CAMBRIDGE, ('University of Cambridge'))
    ]),
    (logo_OXFORD, [
        (OXFORD, ('University of Oxford'))
    ]),
    (logo_STANDFORD, [
        (STANDFORD, ('Stanford University'))
    ]),
    (logo_DUKE, [
        (DUKE, ("Duke's University"))
    ]),
    (logo_CIDE, [
        (CIDE, ("Center of Teaching and Research in Economics"))
    ]),
    (logo_ITAM, [
        (ITAM, ("Instituto Tecnológico Autónomo de México"))
    ]),
    (logo_COLMEX, [
        (COLMEX, ("El Colegio de México"))
    ]),
    (logo_ITESM, [
        (ITESM, ("Instituto Tecnológico y de Estudios Superiores de Monterrey"))
    ]),
    (logo_UIA, [
        (UIA, ("Universidad Iberoamericana"))
    ]),
    (OTHER, [('other')])
]

FRESHMAN = "freshman"
SOPHOMORE = "sophomore"
JUNIOR = "junior"
SENIOR = "senior"
STUDENT_TYPES = [
    (FRESHMAN, ('Freshman')),
    (SOPHOMORE, ('Sophomore')),
    (JUNIOR, ('Junior')),
    (SENIOR, ('Senior')),
]

BACHELOR = "bachelor"
MASTER = "master"
DOCTORATE = "Doctorate"
DIPLOMA = 'diploma'
CERTIFICATE = 'certificate'
OTHER = "other"
DEGREES = [
    (BACHELOR, ('Bachelor Degree')),
    (MASTER, ('Masters Degree')),
    (DOCTORATE, ('Ph.D.')),
    (DIPLOMA, ('Diploma')),
    (CERTIFICATE, ('Certificate')),
    (OTHER, ('Other')),
]

Bachelor_of_Arts = "BA"
Bachelor_of_Science_And_Arts = "BSA"
Bachelor_of_Accountancy = "BAcy"
Bachelor_of_Accounting = "BAcc"
Bachelor_of_Animal_and_Veterinary_Bioscience = "B.An.Vet.Bio.Sc."
Bachelor_of_Applied_Science = "B.A.Sc."
Bachelor_of_Architecture = "BArch "
Bachelor_of_Business_Administration = "BBA"
Bachelor_of_Civil_Engineering = "BCE"
Bachelor_of_Commerce = "BCom"
Bachelor_of_Communications = "B.Comm."
Bachelor_of_Computer_Application = "BCA"
Bachelor_of_Dental_Hygiene = "BDH Or B.D.H"
Bachelor_of_Dental_Medicine = "BDM"
Bachelor_of_Dental_Science = "BDSc or B.D.Sc."
Bachelor_of_Dental_Surgery = "BDS or B.D.S."
Bachelor_of_Dentistry =	"BDent or B.Dent."
Bachelor_of_Design = "BDes or B.Des."
Bachelor_of_Design_Computing = "B.Des.Comp."
Bachelor_of_Design_in_Architecture = "B.Des.Arch."
Bachelor_of_Education =	"BEd or B.Ed."
Bachelor_of_Engineering = "BEng or B.Eng., or BE or B.E"
Bachelor_of_Electronic_Commerce = "BEC or B.E-COM."
Bachelor_of_Electrical_Engineering = "BEE or B.E.E."
Bachelor_of_Fine_Arts = "BFA or B.F.A."
Bachelor_of_Health_Sciences = "B.Hlth.Sci"
Bachelor_of_Information_Technology = "BIT or B.I.T."
Bachelor_of_International_and_Global_Studies = "BIGS or B.I.G.S."
Bachelor_of_Law = "LLB or LL.B."
Bachelor_of_Liberal_Arts_and_Sciences =	"BLAS or B.L.A.S."
Bachelor_of_Library_Science = "BLib or B.Lib., or BLS or B.L.S."
Bachelor_of_Literature = "BLit or B.Lit."
Bachelor_of_Mathematics = "BMath or B.Math"
Bachelor_of_Mechanical_Engineering = "BME or B.M.E."
Bachelor_of_Medical_Science = "B.Med.Sc."
Bachelor_of_Medicine = "MB or M.B."
Bachelor_of_Music = "B.M."
Bachelor_of_Music_Studies = "B.Mus.Studies"
Bachelor_of_Nursing = "BN or B.N."
Bachelor_of_Pharmacy = "B.Pharm."
Bachelor_of_Political_Economic_and_Social_Sciences = "B.P.E.S.S."
Bachelor_of_Resource_Economics = "B.Res.Ec."
Bachelor_of_Science = "BS"
Bachelor_of_Science_in_Dental_Hygiene = "BSDH or B.S.D.H"
Bachelor_of_Science_in_Environmental_and_Occupational_Health = "BS.EOH"
Bachelor_of_Science_in_Nursing = "BSN"
Bachelor_of_Socio_Legal_Studies = "BSLS or B.S.L.S."
Bachelor_of_Surgery = "BS or B.S."
Bachelor_of_Technology = "BTech or B.Tech."
Bachelor_of_Veterinary_Science = "B.V.Sc."
Bachelor_of_Visual_Arts = "BVA or B.V.A."
BACHELOR_DEGREES = [
    ("Bachelor of Arts", ("BA")),
    ("Bachelor of Science_And_Arts", ("BSA")),
    ("Bachelor of Accountancy", ("BAcy")),
    ("Bachelor of Accounting", ("BAcc")),
    ("Bachelor of Animal_and_Veterinary_Bioscience", ("B.An.Vet.Bio.Sc.")),
    ("Bachelor of Applied_Science", ("B.A.Sc.")),
    ("Bachelor of Architecture", ("BArch ")),
    ("Bachelor of Business_Administration", ("BBA")),
    ("Bachelor of Civil_Engineering", ("BCE")),
    ("Bachelor of Commerce", ("BCom")),
    ("Bachelor of Communications", ("B.Comm.")),
    ("Bachelor of Computer_Application", ("BCA")),
    ("Bachelor of Dental_Hygiene", ("BDH Or B.D.H")),
    ("Bachelor of Dental_Medicine", ("BDM")),
    ("Bachelor of Dental_Science", ("BDSc or B.D.Sc.")),
    ("Bachelor of Dental_Surgery", ("BDS or B.D.S.")),
    ("Bachelor of Dentistry", ("BDent or B.Dent.")),
    ("Bachelor of Design", ("BDes or B.Des.")),
    ("Bachelor of Design_Computing", ("B.Des.Comp.")),
    ("Bachelor of Design_in_Architecture", ("B.Des.Arch.")),
    ("Bachelor of Education", ("BEd or B.Ed.")),
    ("Bachelor of Economics", ("BEc or BEcon")),
    ("Bachelor of Engineering", ("BEng or B.Eng., or BE or B.E")),
    ("Bachelor of Electronic_Commerce", ("BEC or B.E-COM.")),
    ("Bachelor of Electrical_Engineering", ("BEE or B.E.E.")),
    ("Bachelor of Fine_Arts", ("BFA or B.F.A.")),
    ("Bachelor of Health_Sciences", ("B.Hlth.Sci")),
    ("Bachelor of Information_Technology", ("BIT or B.I.T.")),
    ("Bachelor of International_and_Global_Studies", ("BIGS or B.I.G.S.")),
    ("Bachelor of Law", ("LLB or LL.B.")),
    ("Bachelor of Liberal_Arts_and_Sciences", (	"BLAS or B.L.A.S.")),
    ("Bachelor of Library_Science", ("BLib or B.Lib., or BLS or B.L.S.")),
    ("Bachelor of Literature", ("BLit or B.Lit.")),
    ("Bachelor of Mathematics", ("BMath or B.Math")),
    ("Bachelor of Mechanical_Engineering", ("BME or B.M.E.")),
    ("Bachelor of Medical_Science", ("B.Med.Sc.")),
    ("Bachelor of Medicine", ("MB or M.B.")),
    ("Bachelor of Music", ("B.M.")),
    ("Bachelor of Music_Studies", ("B.Mus.Studies")),
    ("Bachelor of Nursing", ("BN or B.N.")),
    ("Bachelor of Pharmacy", ("B.Pharm.")),
    ("Bachelor of Political_Economic_and_Social_Sciences", ("B.P.E.S.S.")),
    ("Bachelor of Resource_Economics", ("B.Res.Ec.")),
    ("Bachelor of Science", ("BS")),
    ("Bachelor of Science_in_Dental_Hygiene", ("BSDH or B.S.D.H")),
    ("Bachelor of Science_in_Environmental_and_Occupational_Health", ("BS.EOH")),
    ("Bachelor of Science_in_Nursing", ("BSN")),
    ("Bachelor of Socio_Legal_Studies", ("BSLS or B.S.L.S.")),
    ("Bachelor of Surgery", ("BS or B.S.")),
    ("Bachelor of Technology", ("BTech or B.Tech.")),
    ("Bachelor of Veterinary_Science", ("B.V.Sc.")),
    ("Bachelor of Visual_Arts", ("BVA or B.V.A."))
]

Master_of_Architecture = "M.Arch., M.S."
Master_of_Arts =" MA, M.A. or A.M."
Master_of_Business_Administration =	"MBA or M.B.A."
Master_of_Commerce = "MCom or M.Com"
Master_of_Computer_Application = "MCA"
Master_of_Divinity = "MDiv or M.Div."
Master_of_Education = "M.Ed., M.S.Ed., or MSEd."
Master_of_Emergency_Management = "MEM or M.E.M."
Master_of_Emergency_and_Disaster_Management = "MEDM or M.E.D.M."
Master_of_Engineering =	"M.E., MEng or M.Eng."
Master_of_Fine_Arts = "MFA or M.F.A."
Master_of_Health_or_Healthcare_Management =	"MSc.HM or MHM"
Master_of_International_Affairs = "MIA or M.I.A."
Master_of_International_Studies = "MIS or M.I.S."
Master_of_Laws = "LLM or LL.M."
Master_of_Library_Science =	"MLS"
Master_of_Liberal_Arts = "MLA"
Master_of_Library_and_Information_Science = "MLIS"
Master_of_Music = " M.M."
Master_of_Professional_Studies = "MPS"
Master_of_Public_Administration = "MPA or M.P.A."
Master_of_Public_Health = "MPH or M.P.H."
Master_of_Science = "MS or M.S."
Master_of_Science_in_Information = "MSI or M.S.I."
Master_of_Social_Work =	"MSW or M.S.W."
Master_of_Strategic_Foresight = "MSF or M.S.F."
Master_of_Sustainable_Energy_and_Environmental_Management = "MSEEM"
Master_of_Technology = "MTech or M.Tech."
Master_of_Theology = "ThM or Th.M."
OTHER = "other"
MASTER_DEGREES = [
    ("Master of Architecture", ("M.Arch., M.S.")),
    ("Master of Arts", (" MA, M.A. or A.M.")),
    ("Master of Business_Administration", ("MBA or M.B.A.")),
    ("Master of Commerce", ("MCom or M.Com")),
    ("Master of Computer_Application", ("MCA")),
    ("Master of Divinity", ("MDiv or M.Div.")),
    ("Master of Education", ("M.Ed., M.S.Ed., or MSEd.")),
    ("Master of Emergency_Management", ("MEM or M.E.M.")),
    ("Master of Emergency_and_Disaster_Management", ("MEDM or M.E.D.M.")),
    ("Master of Engineering", ("M.E., MEng or M.Eng.")),
    ("Master of Fine_Arts", ("MFA or M.F.A.")),
    ("Master of Health_or_Healthcare_Management", ("MSc.HM or MHM")),
    ("Master of International_Affairs", ("MIA or M.I.A.")),
    ("Master of International_Studies", ("MIS or M.I.S.")),
    ("Master of Laws", ("LLM or LL.M.")),
    ("Master of Library_Science", ("MLS")),
    ("Master of Liberal_Arts", ("MLA")),
    ("Master of Library_and_Information_Science", ("MLIS")),
    ("Master of Music", (" M.M.")),
    ("Master of Professional_Studies", ("MPS")),
    ("Master of Public_Administration", ("MPA or M.P.A.")),
    ("Master of Public_Health", ("MPH or M.P.H.")),
    ("Master of Science", ("MS or M.S.")),
    ("Master of Science_in_Information", ("MSI or M.S.I.")),
    ("Master of Social_Work", ("MSW or M.S.W.")),
    ("Master of Strategic_Foresight", ("MSF or M.S.F.")),
    ("Master of Sustainable_Energy_and_Environmental_Management", ("MSEEM")),
    ("Master of Technology", ("MTech or M.Tech.")),
    ("Master of Theology", ("ThM or Th.M."))
]

Doctor_of_Acupuncture =	"DAc or D.Ac. or DAc."
Doctor_of_Audiology = "AuD or Au.D."
Doctor_of_Biblical_Studies = "DBS, D.B.S. or DB"
Doctor_of_Chiropractic = "DC or D.C."
Doctor_of_Dental_Surgery = "DDS or D.D.S."
Doctor_of_Divinity = "DD or D.D."
Doctor_of_Education = "EdD or Ed.D."
Doctor_of_Jurisprudence = "JD or J.D."
Doctor_of_Immortality = "ImD or Im.D."
Doctor_of_Law_and_Policy = "LP.D. or DLP"
Doctor_of_Medical_Dentistry = "DMD or D.M.D."
Doctor_of_Medicine = "MD or M.D."
Doctor_of_Ministry = "DMin"
Doctor_of_Metaphysics = "Dr. mph."
Doctor_of_Musical_Arts = "D.M.A."
Doctor_of_Naturopathy = "ND or N.D."
Doctor_of_Nursing_Practice = "DNP or D.N.P."
Doctor_of_Optometry = "OD or O.D."
Doctor_of_Osteopathy = "DO or D.O."
Doctor_of_Pharmacy = "PharmD or Pharm.D."
Doctor_of_Philosophy = "PhD, Ph.D., DPhil, D.Phil., DPh or D.Ph."
Doctor_of_Physical_Therapy = "DPT or D.P.T."
Doctor_of_Practical_Theology = "DPT or D.P.T."
Doctor_of_Psychology = "PsyD or Psy.D."
Doctor_of_Public_Health = "DrPH"
Doctor_of_Religious_Sciences = "Dr. sc. rel. or D.R.S."
Doctor_of_Science = "DSc, D.Sc. or ScD"
Doctor_of_Theology = "D.Th., Th.D. or ThD"
Doctor_of_Veterinary_Medicine = "DVM or D.V.M."

PHD_DEGREES = [
    ("Doctor of Acupuncture", ("DAc or D.Ac. or DAc.")),
    ("Doctor of Audiology", ("AuD or Au.D.")),
    ("Doctor of Biblical_Studies", ("DBS, D.B.S. or DB")),
    ("Doctor of Chiropractic", ("DC or D.C.")),
    ("Doctor of Dental_Surgery", ("DDS or D.D.S.")),
    ("Doctor of Divinity", ("DD or D.D.")),
    ("Doctor of Education", ("EdD or Ed.D.")),
    ("Doctor of Jurisprudence", ("JD or J.D.")),
    ("Doctor of Immortality", ("ImD or Im.D.")),
    ("Doctor of Law_and_Policy", ("LP.D. or DLP")),
    ("Doctor of Medical_Dentistry", ("DMD or D.M.D.")),
    ("Doctor of Medicine", ("MD or M.D.")),
    ("Doctor of Ministry", ("DMin")),
    ("Doctor of Metaphysics", ("Dr. mph.")),
    ("Doctor of Musical_Arts", ("D.M.A.")),
    ("Doctor of Naturopathy", ("ND or N.D.")),
    ("Doctor of Nursing_Practice", ("DNP or D.N.P.")),
    ("Doctor of Optometry", ("OD or O.D.")),
    ("Doctor of Osteopathy", ("DO or D.O.")),
    ("Doctor of Pharmacy", ("PharmD or Pharm.D.")),
    ("Doctor of Philosophy", ("PhD, Ph.D., DPhil, D.Phil., DPh or D.Ph.")),
    ("Doctor of Physical_Therapy", ("DPT or D.P.T.")),
    ("Doctor of Practical_Theology", ("DPT or D.P.T.")),
    ("Doctor of Psychology", ("PsyD or Psy.D.")),
    ("Doctor of Public_Health", ("DrPH")),
    ("Doctor of Religious_Sciences", ("Dr. sc. rel. or D.R.S.")),
    ("Doctor of Science", ("DSc, D.Sc. or ScD")),
    ("Doctor of Theology", ("D.Th., Th.D. or ThD")),
    ("Doctor of Veterinary_Medicine", ("DVM or D.V.M."))
]
COURSES = [
    ("Architecture", ("Architecture")),
    ("Art History", ("Art History")),
    ("Design", ("Design")),
    ("Film Studies", ("Film Studies")),
    ("Fine Arts", ("Fine Arts")),
    ("Graphic Design", ("Graphic Design")),
    ("Music", ("Music")),
    ("Video Game Design", ("Video Game Design")),
    ("Accounting", ("Accounting")),
    ("Entrepreneurship", ("Entrepreneurship")),
    ("Finance", ("Finance")),
    ("Management", ("Management")),
    ("Marketing", ("Marketing")),
    ("Negotiations", ("Negotiations")),
    ("Biomedical Engineering", ("Biomedical_Engineering")),
    ("Chemical Engineering", ("Chemical_Engineering")),
    ("Electrical Engineering", ("Electrical_Engineering")),
    ("Mechanical Engineering", ("Mechanical_Engineering")),
    ("Systems Engineering", ("Systems_Engineering")),
    ("Communications", ("Communications")),
    ("History", ("History")),
    ("Languages", ("Languages")),
    ("Literature", ("Literature")),
    ("Philosophy", ("Philosophy")),
    ("Religious_Studies", ("Religious_Studies")),
    ("Writing", ("Writing")),
    ("Dentistry", ("Dentistry")),
    ("Disease and Epidemiology", ("Disease_and_Epidemiology")),
    ("Healthcare Administration", ("Healthcare_Administration")),
    ("Nursing", ("Nursing")),
    ("Nutrition", ("Nutrition")),
    ("Astronomy", ("Astronomy")),
    ("Biology", ("Biology")),
    ("Chemistry", ("Chemistry")),
    ("Computer Science", ("Computer_Science")),
    ("Earth Sciences", ("Earth_Sciences")),
    ("Environmental Studies", ("Environmental_Studies")),
    ("Mathematics", ("Mathematics")),
    ("Physics", ("Physics")),
    ("Anthropology", ("Anthropology")),
    ("Criminal_Justice", ("Criminal_Justice")),
    ("Early Childhood_Education", ("Early_Childhood_Education")),
    ("Economics", ("Economics")),
    ("Education", ("Education")),
    ("Elementary Education", ("Elementary_Education")),
    ("International Relations", ("International_Relations")),
    ("Law", ("Law")),
    ("Liberal Studies", ("Liberal_Studies")),
    ("Political Science", ("Political_Science")),
    ("Psychology", ("Psychology")),
    ("Social Work", ("Social_Work")),
    ("Sociology", ("Sociology"))
]

DIPLOMAS = [
    ("Other", ("Other"))
]

CERTIFICATES = [
    ("Other", ("Other"))
]

TECHNOLOGIES = [
    ("HTML", ("html")),
    ("CSS", ("css")),
    ("Javascript", ("javascript")),
    ("React", ("react")),
    ("Tailwind", ("tailwind")),
    ("AWS", ("aws")),
    ("Github", ("github")),
]
SKILLS = [
    ("Other", ("Other"))
]
PROGRAMMER = 'programmer'
PROJECT_MANAGER = 'project_manager'
DATA_ANALYST = 'data_analyst'
BUSINESS_ANALYST = 'business_analyst'
OTHER = 'other'
JOB_ACTIVITIES = [
    (PROGRAMMER, ('Programmer')),
    (PROJECT_MANAGER, ('Project Manager')),
    (DATA_ANALYST, ('Data Analyst')),
    (BUSINESS_ANALYST, ('Business Analyst')),
    (OTHER, ('Other')),
]

PROGRAMMER = 'programmer'
PROJECT_MANAGER = 'project_manager'
DATA_ANALYST = 'data_analyst'
BUSINESS_ANALYST = 'business_analyst'
OTHER = 'other'
JOB_POSITIONS = [
    (PROGRAMMER, ('Programmer')),
    (PROJECT_MANAGER, ('Project Manager')),
    (DATA_ANALYST, ('Data Analyst')),
    (BUSINESS_ANALYST, ('Business Analyst')),
    (OTHER, ('Other')),
]

GITHUB = 'Github'
WHATSAPP = 'WhatsApp'
TELEGRAM = 'Telegram'
LINKEDIN = 'Linkedin'
EMAIL = 'Email'

CONTACT_FORMS = [
    (GITHUB, ('github')),
    (WHATSAPP, ('whatsapp')),
    (TELEGRAM, ('telegram')),
    (LINKEDIN, ('linkedin')),
    (EMAIL, ('email')),
]

LANGUAGES = [
    ('Spanish', ('spanish')),
    ('English', ('english')),
]

LANGUAGE_LEVELS = [
    ('Advanced', ('advanced')),
    ('Intermediate', ('intermediate')),
    ('Basic', ('basic')),
    ('Native', ('native')),
]

PHONE_TYPES = [
    ('Home', ('home')),
    ('Office', ('office')),
    ('Mobile', ('mobile')),
]

PROJECT_CATEGORIES= [
    ('Graphic designed', ('grpahic design')),
    ('Programming', ('programming')),
    ('Animation', ('animation')),
]
import os
#local imports
from .extensions import db
from .models import User, ROLES, Setting, Subject, Page

def generate_users():
    for u in users:
        user = User(email=u['email'], 
                password=u['password'],
                name=u['name'],
                confirmed=u['confirmed'],
                role=u['role'])
        db.session.add(user)
    db.session.commit()
    print('users added')

def generate_subjects():
    for s in subjects:
        db.session.add(Subject(title=s['title'], body=s['body'], fees=s['fees']))
    db.session.commit()
    print('subjects added')

def generate_pages():
    for p in pages:
        db.session.add(Page(title=p['title'], body=p['body']))
    db.session.commit()
    print('Pages added')

def generate_settings():
    for s in settings:
        db.session.add(Setting(key=s['key'], value=s['value']))
    db.session.commit()
    print('Settings added')

def setup_db():
    db.drop_all()
    db.create_all()
    generate_users()
    generate_subjects()
    generate_pages()
    generate_settings()
    print('Done setup')

users = [
        {'email':  os.environ['DEV_USERNAME'],
            'password':  os.environ['DEV_PASSWORD'],
            'name': 'Equip Developer',
            'confirmed': True,
            'role': ROLES['developer']
            }, 
        {'email':  os.environ['ADMIN_USERNAME'],
            'password':  os.environ['ADMIN_PASSWORD'],
            'name': 'Equip Editor',
            'confirmed': True,
            'role': ROLES['editor']
            } ]

settings =[ {'key':'APPLICATION_NAME', 'value': 'Equip Youth Africa'},
            {'key': 'APPLICATION_LOGO_DARK', 'value':''},
            {'key': 'APPLICATION_LOGO_LIGHT', 'value':''},
            {'key': 'LOGIN_IMAGE', 'value': ''},
            {'key': 'LANDING_IMAGE_1', 'value':''},
            {'key': 'LANDING_IMAGE_2', 'value': ''},
            {'key': 'LANDING_HEADING_1', 'value':'Welcome to Equip Youth Africa Skills Training'},
            {'key': 'LANDING_TEXT_1', 'value':'We provide Vocational Training Services, partner with individuals, communities, schools and businesses to deliver specialist qualifications and short courses to empower youth and equip them with industry relevant skills. Our study plan will perfectly match your needs, lifestyle, and goals. Our facilities, compassionate team, and fully equipted centre will help you feel completely at ease.'},
            {'key': 'LANDING_HEADING_2', 'value':'Creating a Skilled Generation'},
            {'key': 'LANDING_TEXT_2', 'value':'We offer training for specific industry relevant jobs. Since vocational training often begins after secondary school, students who successfully complete the courses are prepared to take a high-paying, skilled job immediately. Courses we offer'},
            {'key': 'LANDING_HEADING_3', 'value':'Courses'},
            {'key': 'LANDING_TEXT_3', 'value':'With realization of lack of enough skilled human resource for industrial development and increasing unemployment hence poverty, Equip Youth Africa set out to offer hands on training in vocational skills. This training program is market focused and challenge based in the sense to prepare trainees for industrial work and on completion our trainees are assessed and certified by the Directorate of Industrial Training (D.I.T).'},
            {'key': 'LANDING_HEADING_4', 'value': 'Why Equip Youth Africa?'},
            {'key': 'LANDING_TEXT_4', 'value': '85% of the jobs on the market are Technical, 15% are Corporate jobs. Inspite of this fact, 90% of parents pay for their children to pursue Corporate jobs. It is our job to get you into that 85%. We offer training for specific industry relevant jobs. Since vocational training often begins after secondary school, students who successfully complete the courses are prepared to take a high-paying, skilled job immediately. Graduates from Equip Youth Africa have an advantage over informally trained job-seekers because of the certification from Directorate of Industral training, the skills needed to successfully perform a specific job, and training from skilled hands on instructors.'},
            {'key': 'TELEPHONE', 'value': '+ 256 0705 999 864'},
            {'key': 'LOCATION', 'value':'Kireka - Opposite Good Daddy Pri School'},
            {'key': 'WHATSAPP', 'value':'+ 256 0705 999 864'},
            {'key': 'EMAIL', 'value': 'equipyouthafrica.info@gmail.com'},
            {'key': 'TWITTER', 'value':''},
            {'key': 'FACEBOOK', 'value':''},
            {'key': 'YOUTUBE', 'value':''}
            ]

subjects = [
        {'title': 'Brick Laying and Construction', 
            'body': """This course trains you in aspects related to brick laying. This vocational training program will help you do the role in the construction industry. We will work one on one with you as you learn,  beginning with the basics moving to advanced techniques. 

## How will you benefit?
* Start your career in construction
* Learn how to become a brick layer quickly and conveniently
* Learn from professionals in the industry
* Fully equipped training centre and lab
* Easy payment  plans

Enroll today to start enjoying the benefits.

* Career options **
This course provides extended career opportunities for those looking to start their own business  as mechanics, increasing your professional skills and providing extra value for your clients.

** What you'll learn **

* Working with clients and proper client etiquette
* Setting up your workplace
* Marketing your business
* Selling your products and services
* Cost estimation
* Communication in the workplace 
* Team coordination

** Accreditation ** 
This course is recognized and accredited by Directorate of Industrial Training (DIT) for certificates and advanced levels. Our courses take a very "hands on" approach, tutored by industry professionals and will fast-track you into a new career.

** Course Facts **
** Deadline and start date: **
Students can apply at anytime. Places are limited, in demand and entry into the course is on a first come first served basis.

** Medium of instruction: ** English and most of the local languages

** Classes: ** Monday to Friday 8:00 am to 1:00 pm  

## General requirements
* ** Short courses: ** There are NO previous work or education requirements for entry.
* ** DIT Certificate: ** Ordinary Level Certificate

** Tuition Fees **
Tuition Fees have been kept  low keeping in view the objective to provide vocational education for all sections of society.
""",
'fees':'350, 000'},
        {'title': 'Carpentry and Wood Joinery',
            'body': """Develop a sound knowledge of the tools, materials, and building methods used in modern carpentry with Equip Youth Africa's carpentry courses. Carpentry is a highly skilled trade that has evolved to incorporate improved building materials and construction methods. By taking our training courses, you will learn about different carpentry tools, materials, and building methods.


## How will you benefit?

* Start your career as a carpenter
* Learn how to become an auto carpenter quickly and conveniently
* Learn from professionals in the industry
* Fully equipped training centre and lab
* Easy payment  plans

Enroll today to start enjoying the benefits.

## Career options 
This course provides extended career opportunities for those looking to start their own business  as mechanics, increasing your professional skills and providing extra value for your clients.

## What you'll learn

* Working with clients and proper client etiquette
* Setting up your workplace
* Marketing your business
* Selling your products and services
* Cost estimation
* Communication in the workplace 
* Team coordination

## Accreditation  
This course is recognized and accredited by Directorate of Industrial Training (DIT) for certificates and advanced levels. Our courses take a very "hands on" approach, tutored by industry professionals and will fast-track you into a new career.

## Course Facts 
** 
** Deadline and start date: **
Students can apply at anytime. Places are limited, in demand and entry into the course is on a first come first served basis.

** Medium of instruction: ** English and most of the local languages

** Classes: ** Monday to Friday 8:00 am to 1:00 pm  

## General requirements

* ** Short courses: ** There are NO previous work or education requirements for entry.
* ** DIT Certificate: ** Ordinary Level Certificate

** Tuition Fees **
Tuition Fees have been kept  low keeping in view the objective to provide vocational education for all sections of society.""",
            'fees':'350, 000'
        },
        {
                'title': 'Computer Repair and Maintanance',
                'body': """Innovation in technology influences how we live as much as any other aspect of modern life. Computers perform increasingly complex tasks that have the potential to improve our lives in ways we could have never imagined. Read on to learn about five employment areas where you can turn a love of computers into a career. 		

Computer scientists are highly trained professionals who create new technologies. These advances might be in hardware functionality or other computing improvements. Discoveries are also sought in robotics, virtual reality and other relatively new technological areas that are only now being fully explored. 

Computer scientists often perform research on computing processes and work to make them more efficient or innovative. These professionals may work with others, including mechanical and electrical engineers, to solve technological dilemmas. 



** What you'll learn **

* Working with clients and proper client etiquette
* Setting up your workplace
* Working of computers
* Computer systems
* Marketing your business
* Selling your products and services
* Cost estimation
* Communication in the workplace 
* Team coordination

** Accreditation ** 
This course is recognized and accredited by Directorate of Industrial Training (DIT) for certificates and advanced levels. Our courses take a very "hands on" approach, tutored by industry professionals and will fast-track you into a new career.

** Course Facts **
** Deadline and start date: **
Students can apply at anytime. Places are limited, in demand and entry into the course is on a first come first served basis.

** Medium of instruction: ** English and most of the local languages

** Classes: ** Monday to Friday 8:00 am to 1:00 pm  

** General requirements **

*  ** Short courses: ** There are NO previous work or education requirements for entry.
*  ** DIT Certificate: ** Ordinary Level Certificate

** Tuition Fees **

Tuition Fees have been kept  low keeping in view the objective to provide vocational education for all sections of society.""",
                'fees':'350, 000'
                
        },
        { 
                'title': 'Electrical Fitting and Installation',
                'body': """This course trains you in aspects related to electrical installation. This vocational training program will help you do the role of an auto electrician. We will work one on one with you as you learn,  beginning with the basics moving to advanced techniques.  We welcome everyone, whether you have no previous experience and want to become an electrician, or you're an experienced electrician and need to learn advanced skills to progress to a specialised or senior management role.

## How will you benefit?
* Start your career as an electrician
* Learn how to become an electrician quickly and conveniently
* Learn from professionals in the industry
* Fully equipped training centre and lab
* Easy payment  plans

Enroll today to start enjoying the benefits.

** Career options **
This course provides extended career opportunities for those looking to start their own business  as electrican, increasing your professional skills and providing extra value for your clients.

** What you'll learn **

* Working with clients and proper client etiquette
* Setting up your workplace
* Electrical Installation
* Electrical systems
* Maintaining and servicing Electrical equiptment
* Marketing your business
* Selling your products and services
* Cost estimation
* Communication in the workplace 
* Team coordination

** Accreditation ** 
This course is recognized and accredited by Directorate of Industrial Training (DIT) for certificates and advanced levels. Our courses take a very "hands on" approach, tutored by industry professionals and will fast-track you into a new career.

** Course Facts **
** Deadline and start date: **
Students can apply at anytime. Places are limited, in demand and entry into the course is on a first come first served basis.

** Medium of instruction: ** English and most of the local languages

** Classes: ** Monday to Friday 8:00 am to 1:00 pm  


## General requirements
* ** Short courses: ** There are NO previous work or education requirements for entry.
* ** DIT Certificate: ** Ordinary Level Certificate

** Tuition Fees **
Tuition Fees have been kept  low keeping in view the objective to provide vocational education for all sections of society.""",
                'fees':''
        },
        {
                'title': 'Hair dressing and saloon management',
                'body': """This course will guide you as you look to pursue a career in professional hairstyling. We will work one on one with you as you learn,  beginning with the basics moving to advanced hairstyling techniques.  We welcome all students, including those experienced in hairstyling looking to enhance their qualifications and those with no previous experience in hair styling.

** How will you benefit? **

* Start your career in professional hairdressing
* Learn how to become a hairdresser fast and easy
* Learn from professional hairdressers
* Easy payment  plans

Enroll today to start enjoying the benefits.

** Career options **

This course provides extended career opportunities for those looking to start their own business or freelance in hairstyling industry, increasing your professional skills and providing extra value for your clients. This course is perfect for those pursuing work in bridal, private clients, special occasions, fashion industry, Television/film/music  and many more.

** What you'll learn **

* Working with clients and proper client etiquette
* Dressing and styling hair
* Styling products and tools
* Remove chemicals from hair
* Hygiene and safety
* Selling products and services
* Communication in the workplace 
* Team coordination


** Accreditation **
 
This course is recognized and accredited by Directorate of Industrial Training (DIT) for certificates and advanced levels. Our courses take a very "hands on" approach, tutored by industry professionals and will fast-track you into a new career in hairdressing.

** Course Facts **

** Deadline and start date: **
Students can apply at anytime. Places are limited, in demand and entry into the course is on a first come first served basis.

** Medium of instruction: ** English and most of the local languages

** Classes: ** Monday to Friday 8:00 am to 1:00 pm  


** General requirements **

* ** Short courses: ** There are NO previous work or education requirements for entry.
* ** DIT Certificate: ** Ordinary Level Certificate

**  Tuition Fees **
 
Tuition Fees have been kept  low keeping in view the objective to provide vocational education for all section of society. """,
                'fees': ''
        },
        {
                'title': 'Moto Vehicle Repair and Maintanance',
                'body': """This course trains you in aspects related to automobile repair, maintenance and repair. This vocational training program will help you do the role of an auto mechanic. We will work one on one with you as you learn,  beginning with the basics moving to advanced techniques.  We welcome everyone, whether you have no previous experience and want to become a mechanic or motor vehicle technician, or you're an experienced mechanic and need to learn advanced skills to progress to a specialised or senior management role.

## How will you benefit?
* Start your career as a auto mechanic
* Learn how to become an auto mechanic quickly and conveniently
* Learn from professionals in the industry
* Fully equipped training centre and lab
* Easy payment  plans

Enroll today to start enjoying the benefits.

** Career options **
This course provides extended career opportunities for those looking to start their own business  as mechanics, increasing your professional skills and providing extra value for your clients.

** What you'll learn **

* Working with clients and proper client etiquette
* Setting up your workplace
* Working of engines
* Automobile electrical systems
* Engine dismantling, inspection, assembly and tuning
* Marketing your business
* Selling your products and services
* Cost estimation
* Communication in the workplace 
* Team coordination

** Accreditation ** 
This course is recognized and accredited by Directorate of Industrial Training (DIT) for certificates and advanced levels. Our courses take a very "hands on" approach, tutored by industry professionals and will fast-track you into a new career.

** Course Facts **
** Deadline and start date: **
Students can apply at anytime. Places are limited, in demand and entry into the course is on a first come first served basis.

** Medium of instruction: ** English and most of the local languages

** Classes: ** Monday to Friday 8:00 am to 1:00 pm  


** General requirements **

*  ** Short courses: ** There are NO previous work or education requirements for entry.
*  ** DIT Certificate: ** Ordinary Level Certificate

** Tuition Fees **

Tuition Fees have been kept  low keeping in view the objective to provide vocational education for all sections of society.""",
                'fees':''
        },
        { 
                'title': 'Refrigiration and Air Conditioning',
                'body': """Gain skills to help you prepare to become an Air Conditioning & Refrigeration Technician with  Equip Youth African. You will take courses when it works best for your schedule, study in the classroom and in the field, all at your own pace. 

This course Designed to help you prepare for Air Conditioning and Refrigeration  Certification,  from the Directorate of Industrial Training (DIT)

** Who attends this course? **

Those interested in pursuing a career in a growing industry, earning an Air Conditioning & Refrigeration certification can help you take the first steps toward a rewarding job. Technicians work in a variety of environments, including hospitals, schools, office buildings and private home. Some even take steps toward owning their own business! Trained technicians will find themselves doing something new each day, from repairing commercial refrigeration units to fixing complex heating systems. 


** What topics does this course cover? **

Our training covers topics such as  electrical installation, refrigeration systems, electrical systems, Air Conditioning & Refrigeration system design and installation, and more to help you succeed in the Air Conditioning & Refrigeration field. 

** What will I learn? **

By the end of the course, participants will have strengthened their technical knowledge to improve the functioning of Air Conditioning & Refrigeration systems

** FAQ **

** Q. How much do Technicians make per hour? **

** A. ** Salary and hourly pay for technicians can vary based on experience, the city you live in, and your employer.

** Q. Do you need a University degree to become a Technician? **

** A. ** No. To qualify for admission to a training  programme you require  O'level certificate or above.

** Q. What is the job description of a Technician? **

** A. ** HVAC Technicians work on heating, ventilation, cooling, and refrigeration systems that control the temperature and air quality in buildings. Daily work can include installing, cleaning, and maintaining HVAC systems, inspecting and testing systems, and repairing worn devices. Technicians can find themselves working on both industrial and residential Air Conditioing systems depending on their employer.

** Q. Why become an HVAC Technician? **

** A. ** If you’re looking for a career in a hands-on field that offers the opportunity to work on a variety of projects, becoming an Air conditioning technician could be the job for you. Besides allowing you to use your technical and problem-solving skills, the demand for Air Conditioing Technicians is projected to grow much faster than average over the next ten years.""",
                'fees':''
        },
        {
                'title': 'Tailoring and Fashion Design',
                'body': """This course teaches you the skills that you need to succeed quickly and conveniently in the fashion industry. We will work one on one with you as you learn,  beginning with the basics moving to advanced tailoring techniques.  We welcome all students, including those experienced in fashion and design looking to enhance their qualifications and those with no previous experience in tailoring.

** How will you benefit? **
* Start your career in tailoring
* Learn how to become a  tailor quickly and conveniently
* Learn from professionals in the industry
* Easy payment  plans

Enroll today to start enjoying the benefits.

** Career options **
This course provides extended career opportunities for those looking to start their own business in the fashion industry, increasing your professional skills and providing extra value for your clients. This course is perfect for those pursuing work in bridal, private clients and special occasions.

** What you'll learn **
* Working with clients and proper client etiquette
* Setting up your workplace
* Choosing materials
* Sketching designs
* Pattern making
* Marketing your business
* Selling your products and services
* Communication in the workplace 
* Team coordination


** Accreditation **
This course is recognized and accredited by Directorate of Industrial Training (DIT) for certificates and advanced levels. Our courses take a very "hands on" approach, tutored by industry professionals and will fast-track you into a new career.

** Course Facts **
** Deadline and start date: **
Students can apply at anytime. Places are limited, in demand and entry into the course is on a first come first served basis.

** Medium of instruction: ** English and most of the local languages

** Classes: ** Monday to Friday 8:00 am to 1:00 pm  


** General requirements **
* ** Short courses: ** There are NO previous work or education requirements for entry.
* ** DIT Certificate: ** Ordinary Level Certificate

** Tuition Fees ** 
Tuition Fees have been kept  low keeping in view the objective to provide vocational education for all section of society.""",
                'fees':''
        },
        {
                'title': 'Welding & Fabrication',
                'body': """This course is designed for a range of abilities: from beginners who need basic welding training, to experienced welders who want to develop specialist skills.
Welding ideal for anyone who wants to become a welder and is new to welding, metal fabrication, thermal cutting and/or brazing and soldering.

** How will you benefit? **
* Start your career as welder
* Learn how to become an welder quickly and conveniently
* Learn from professionals in the industry
* Fully equipped training centre and lab
* Easy payment  plans

Enroll today to start enjoying the benefits.

** Career options **
This course provides extended career opportunities for those looking to start their own business  as welder, increasing your professional skills and providing extra value for your clients.

** What you'll learn **

* Working with clients and proper client etiquette
* Setting up your workplace
* Marketing your business
* Electric shock Fumes 
* STICK welding 
* Joint preparation 
* Electrode selection 
* Technical drawing 
* Architectural drafting 
* Selling your products and services
* Cost estimation
* Communication in the workplace 
* Team coordination

** Accreditation ** 
This course is recognized and accredited by Directorate of Industrial Training (DIT) for certificates and advanced levels. Our courses take a very "hands on" approach, tutored by industry professionals and will fast-track you into a new career.

** Course Facts **
** Deadline and start date: **
Students can apply at anytime. Places are limited, in demand and entry into the course is on a first come first served basis.

** Medium of instruction: ** English and most of the local languages

** Classes: ** Monday to Friday 8:00 am to 1:00 pm  

## General requirements
* ** Short courses: ** There are NO previous work or education requirements for entry.
* ** DIT Certificate: ** Ordinary Level Certificate

** Tuition Fees **
Tuition Fees have been kept  low keeping in view the objective to provide vocational education for all sections of society.


""",
                'fees':''
        }
        ]

pages = [
        {'title': 'About Us', 'body':"""Equip youth Africa skills training Centre is a youth initiative that was started on 13th/Feb/2013. 

Equip youth Africa was conceived on the vision of Mr. Nimwesiga Edson who was sensitive and motivated for the cause of poverty and a high number of unemployment due to lack of skills among the youth in Uganda. 

He undertook intensive training in Electrical Engineering, computer engineering and specialized in Air conditioning. 

With realization of lack of enough skilled human resource for industrial development and increasing unemployment hence poverty, Equip Youth Africa set out to offer a one year hands on training in vocational skills 

This training program is market focused and challenge based in the sense to prepare trainees for industrial work and on completion our trainees are assessed and certified by the Directorate of Industrial Training (D.I.T) in both Formal assessment for those who completed O’ level and above and Non-Formal for those who are P.7 dropouts and below and ready to deliver under minimum supervision once any employment opportunity comes their way. 

## Problem Statement. 

The young sect of the society is alarmingly increasing from time to time and their way of living is laden with both economic and social problems. The economic problem is basically lack of employment opportunities which has reduced many of them to the level of desperation. As a result the youth do involve in illegal activities such as theft, prostitution, gangster, and kidnapping among others in order to sustain their lives. 

Common social problems are lack of recreation early marriages, lack of self – sustainability, broken families which results in to street kids. 

## Mission 

To train youth in conformity with Industrial standards. 

## Vision. 

Be a Centre of skilled man power enhancing productivity, international competitiveness and recognition improving revenue generation hence economic growth in the long run. 

## “Facts of the matter” 

* For a country to have a sustainable economy it has to have productive citizens but no one is born productive, it is the adopted education system that makes them productive.

* 85% of the jobs on market are technical, 15% are corporate jobs. In spite of this fact, 90% of parents pay for their children to pursue corporate jobs. 

* No one talks about solving unemployment without talking about developing industries but no one talks about developing industries without talking about skilling human resource. 

## Project Objectives.

The overall objective is to create an enabling environment for the youth so that they can both be 
job creators, self-dependent and contribute to the development of their families and be active 
participants in development of the nation.

## Specific Objectives.

To provide sustainable employment after training. This will be achieved by starting up a construction company that will employ trainees in various fields like Welding and fabrication, Brick laying and construction, Carpentry and wood joinery among others. """},
        {'title': 'Apply Now', 'body': """Apply

** Accreditation ** 
This course is recognized and accredited by Directorate of Industrial Training (DIT) for certificates and advanced levels. Our courses take a very "hands on" approach, tutored by industry professionals and will fast-track you into a new career.

** Course Facts **
** Deadline and start date: **
Students can apply at anytime. Places are limited, in demand and entry into the course is on a first come first served basis.

** Medium of instruction: ** English and most of the local languages

** Classes: ** Monday to Friday 8:00 am to 1:00 pm  

## General requirements
* ** Short courses: ** There are NO previous work or education requirements for entry.
* **Craft Level: ** Ordinary Level Certificate or UNEB Junior Technical Certificate
* ** DIT Certificate: ** Ordinary Level Certificate

** Tuition Fees **
Tuition Fees have been kept  low keeping in view the objective to provide vocational education for all sections of society."""}
        ]

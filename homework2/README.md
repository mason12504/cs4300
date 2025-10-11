Mason Andersen  
CS 4300  
Homework 2  
10-6-2025  

Running the program  ---------    
first activate the virtual environment in the devedu container root directory with  
`source HW2/bin/activate`  
then navigate to the directory  
`cd cs4300/homework2/movie_theater_booking`  
Render was not in the cards today so just run    
`python manage.py runserver 0.0.0.0:3000`  in the directory cs4300/homework2/movie_theater_booking  
then hit "app" on devedu to view 

Naviation --------------------  
you can click around the html views for the normal user experience, or go to  
https://app-mason-19.devedu.io/api for the DRF browsable api views. 

Testing ----------------------  
unit testing of models:  
`python manage.py test` will run tests in tests.py that instantiate some models and verify it works as intended

API testing is also handled in tests.py with the command above covering that.


Resources used:  
I used the docs given in the homework, with some youtube videos and AI for things that weren't immediately obvious to me in the docs or things towards the end I didn't plan adequate time for. 
AI was used for exploring concepts, and generating some significant parts of the code. The HTML is based on bootstrap examples with the form part being chatGPT. Tests in tests.py are basically all chatGPT as well with the generated code copy-pasted. The remainder of the assignment is from the resources below and my own learning.  
ChatGPT convo link with GPT-5: https://chatgpt.com/share/68eaa1eb-4e40-8004-a951-13ffc3377323 
https://docs.djangoproject.com/en/5.2/   
https://www.django-rest-framework.org/tutorial/6-viewsets-and-routers/   
https://getbootstrap.com/docs/5.3/getting-started/introduction/  
https://docs.djangoproject.com/en/5.2/topics/testing/  
https://render.com/docs/deploy-django  
https://youtu.be/4MrB4IvW6Ow  
google gemini "django templates for a rest viewset" used for ideas but didn't use generated code  
https://www.django-rest-framework.org/api-guide/renderers/  
https://www.w3schools.com/django/django_templates.php  
https://getbootstrap.com/docs/5.3/components/navbar/  

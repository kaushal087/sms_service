# sms_service
Test SMS API service


Features:

    -> User Authentication and Authorization (Singup/Login for testing purposes)
    -> API /inbound/sms/
        -> User is not authenticated show error (AUTHENTICATION)
        -> Input Validation
        -> If parameter is missing show required error
        -> If parameter is invalid show invalid error
        -> When text is STOP or STOP\n or STOP\r or STOP\r\n :(CACHING)
           The ‘from’ and ‘to’ pair is cached in redis with an expiry of 4 hours.
        -> If unexcepted error, show error


     -> API /outbound/sms/
        -> User is not authenticated show error (AUTHENTICATION)
        -> Input Validation (EXCEPTION HANDLING)
        -> If parameter is invalid show invalid error
        -> If unexcepted error, show error
        -> If the pair ‘to’ and ‘from’ matches the cached pair: (CACHING)
            show error
        -> If 50 request limit reached then show error (THROTTLING)
        -> If unexcepted error, show error

     -> Unit Test for both API /inbound/sms/ and /outbound/sms/


Major Language, framework and libraries used:
    Python 3
    Django==2.1
    django-redis==4.9.0
    djangorestframework==3.8.2
    gunicorn==19.9.0
    psycopg2==2.7.5
    redis==2.10.6


Github Link:
    https://github.com/kaushal087/sms_service



Deployment Instructions:

cd project directory:
    cd sms_service
Create virtual environment:
    virtualenv -p python3 env
Activate virtual environment:
    source env/bin/activate
install requirement:
    pip3 install -r requirement.txt
Collectstatic:
    python manage.py collectstatic
runserver:
    python manage.py runserver

Set os environment variable as well which is given in .env file, (I have set through heroku dashboard)

Postman collection link:
    https://www.getpostman.com/collections/a77d6e19f2094129e3a8

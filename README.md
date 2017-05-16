Hertz, the Attendance Tracker
=============================

Setup
-----
1. Requirements:
    * docker-compose

2. Setting up for the first time
```bash
git clone https://github.com/seccom-ufsc/hertz.git
cd hertz/
docker-compose run web python manage.py createsuperuser
```

3. After that, to start the server
```
docker-compose up -d
```

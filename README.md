Hertz, the Attendance Tracker
=============================

Setup
-----
1. Requirements:
    * docker-compose

2. Setup
```bash
git clone https://github.com/seccom-ufsc/hertz.git
cd hertz/
```

3. After that, to start the server
```bash
docker-compose up -d
```

4. If you are running Hertz for the first time, you need to import the student's data (and create an admin account)
```bash
docker-compose run web python db_populate.py students_data.csv
```

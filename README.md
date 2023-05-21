# Gradebook App
Implementation done purely with Python Django.

To run the app after cloning the repo, follow the steps below:
1. Run command "python manage.py makemigrations"
2. Run command "python manage.py migrate"
3. Create a superuser to access admin functionalities by running "python manage.py createsuperuser"
4. After registering some users by using register page on the app, go to "http://127.0.0.1:8000/admin/" and login as the superuser that you have created
5. Create two usergroups and name them as "lecturer" and "student", assign the users that you have created to any of these groups
6. Login using any of these users, and you'll see specific functions for each user depending on their groups

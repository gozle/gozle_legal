# Running the application on local machine
To run the application on your machine you should follow these steps:
1. Download the repository: `git clone https://github.com/gozle/gozle_legal`
2. Run `Docker Desktop`
3. Input `docker-compose --build` (within a folder in cmd)
4. Migrate the DB `docker-compose exec web python manage.py migrate`
5. Create an admin user profile `docker-compose exec web python manage.py createsuperuser`
6. Finally, Run the Docker machine `docker-compose up -d`
   

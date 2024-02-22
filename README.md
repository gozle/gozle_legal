# Running the application on local machine
To run the application on your machine you should follow these steps:
1. Download the repository: `git clone https://github.com/gozle/gozle_legal`
2. Run `Docker Desktop`
3. Input `docker-compose --build` (within a folder in cmd)
4. Create an admin user profile `docker-compose exec web python manage.py createsuperuser`
5. Finally, Run the Docker machine `docker-compose up -d`

#Problems with connection to Elastic Search
Go To Elastic Search Image in Docker and change the lines like on the screenshot: 
![Docker_Desktop_lFElCzwXs0](https://github.com/gozle/gozle_legal/assets/117362619/97f7eee5-036a-427e-9d0f-b314935e8691)

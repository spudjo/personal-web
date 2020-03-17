# personal-web
 My personal website. Will feature my bio as well as various projects. Still a work on progress, especially the frontend.
 
### Technologies
1. [Flask](https://flask.palletsprojects.com/en/1.1.x/)
2. [Angular](https://angular.io/)
3. [SQLAlchemy](https://pypi.org/project/SQLAlchemy/) and [PostgreSQL](https://www.postgresql.org/)

### Dependancies
Flask, SQLAlchemy, Marshmallow, Psycopg2, SQLAlchemy, Angular

### Requirements
Currently there is no live version of this website up. To check it out, ensure that all dependancies are installed, then install Docker and run the following to create the Postgre database:

 docker run --name personal_web \
    -p 5432:5432 \
    -e POSTGRES_DB=personal_web \
    -e POSTGRES_PASSWORD=mcmXz6ozAuN6PwHyRJgJUctk \
    -d postgres
    
Then, execute [start_backend.bat](start_backend.bat) and [start_frontend.bat](start_frontend.bat).
Finally, navigate to http://localhost:4200/ to check it out.

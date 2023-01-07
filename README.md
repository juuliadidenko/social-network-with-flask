## Microblog, a mini Twitter clone  

**Stack:**  
- Flask, Flask-SQLAlchemy, Flask-Bootstrap
- PostgreSQL
- Elasticsearch
- PyJWT
- PyBabel

#### Create a profile  
Register, login, update your profile, create posts  

#### Connect  
Follow users to see their posts in your feed. Send private messages 

#### Browse  
Find new posts with **Explore** tab. Use **Search** bar to lookup posts. **Translate** posts written in other languages  

#### Export data
Send all of your posts in JSON format to your email


## Quick Start  

1. Clone the repository and navigate into the project folder  
`git clone git@github.com:juuliadidenko/microblog-with-flask.git`  
`cd microblog-with-flask`  
2. Run `docker compose up --build -d`
3. Create database: run
   `docker compose exec microblog flask db init`  
   `docker compose exec microblog flask db migrate`  
   `docker compose exec microblog flask db upgrade`
4. Go to `localhost:8000`

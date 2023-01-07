## Microblog, a mini Twitter clone  

**Stack:**  
- Flask, Flask-SQLAlchemy, Flask-Bootstrap
- PostgreSQL
- Elasticsearch
- PyJWT
- PyBabel

#### Create a profile  
Register, login, update your profile, create posts  

![1-create-profile](https://user-images.githubusercontent.com/104693196/211167893-11f208c1-704c-4e4b-80eb-f717a9de0eed.gif)


#### Connect  
Follow users to see their posts in your feed. Send private messages 

![2-follow-and-message](https://user-images.githubusercontent.com/104693196/211167914-b84e1746-b6f8-4214-a6f9-2162fd7fb8ce.gif)

#### Browse  
Find new posts with **Explore** tab. Use **Search** bar to lookup posts  

![3-explore-and-search](https://user-images.githubusercontent.com/104693196/211167936-d5af9420-2698-4669-a619-af7359bf7c66.gif)

#### Export data
Send all of your posts in JSON format to your email  
(*currently for development purposes all mail goes to mailtrap.io test inbox)  

![export-posts-1](https://user-images.githubusercontent.com/104693196/211167729-f561fbc1-868a-42cc-be46-3e0d782a4d85.jpg)  
![export-posts-2](https://user-images.githubusercontent.com/104693196/211168011-87bc3c47-a143-411b-a651-bf83f76cc340.png)


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

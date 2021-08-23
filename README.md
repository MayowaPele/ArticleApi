# ArticleApi
This is an Article API that contains the title of the articles, author, email and date.  

## Get the APIs consisting of the articles details:
    localhost:8000/articleclass/
    GET: Returns the articles and its details
    POST: Post a new article
    
## Get the APIs of each article:
    localhost:8000/eacharticleclass/id/
    where id represents the id number of each article
    GET: Returns the details of the article with respect to the id
    PUT: Updates the detail of the article with respect to the id
    DELETE: Deletes the entire article with respect to the id

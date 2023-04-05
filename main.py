from fastapi import FastAPI
import typing

app = FastAPI()

@app.get('/blogs')
def blogs(limit = 10, published: bool = True, sort: str | None = None):
    if published:
        return {'data': f'{limit} blogs from the db'}
    else:
        return {'data': f'all blogs from the db'}
@app.get('/blog/unpublished')
def unpublished_blogs():
    return {'data': 'Blogs that was never published'}

@app.get('/blog/{id}')
def get_blog_id(id: int):

    return {'data': id}


@app.get('/about')
def about():
    return {'data':{'about page': {'name', 'surname', 'contact info'}}}
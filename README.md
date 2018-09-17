# Personal-Blog

 By [Lewis Mutuma](https://mutumamutuma.github.io/Portfolio/)

## User Requirements

+ [x] As a user I would like to view the blog posts submitted
+ [x] As a user I would like to comment on blog posts
+ [x] As a user I would like to view the most recent posts
+ [x] As a user I would like to alerted when a new post is made by joining a subscription.

## Writer Requirements

+ [x] As a writer I would like to sign in to the blog.
+ [x] As a writer I would also like to create blog from the application.
+ [x] As a writer I would like to delete comments that I find insulting or degrading.
+ [x] As a writer I would like to update or delete blogs i have created.


## Specifications

[Specifications file](https://github.com/MutumaMutuma/Personal-Blog/blob/master/specs.md)

### Requirements
This project was created on a debian linux platform but should work on other unix based[not limited to] sytems.

* Python 3.6

### Cloning the repository

```git clone```


### Database migrations

```bash
# first initialize the database if the migrations folder does not exist
python manage.py db init
# create  a migration
python manage.py db migrate -m "initial migration"
# upgrade
python manage.py db upgrade
# insert initial data
python manage.py insert_initial_data
```

### Installing dependencies

```
pip3 install -r requirements
```

### Prepare environmet variables

```bash
 export MAIL_USERNAME=YOUR EMAIL
 export MAIL_PASSWORD=EMAIL PASSWORD
 export ADMIN_MAIL_USERNAME=ADMIN ACCOUNT EMAIL
 export DATABASE_URL=POSTGRESQL DATABASE PATH WITH DRIVER
```



### Creating a virtual environment

```
python2.7 -m virtualenv virtual-blog
source virtual-blog/bin/activate
```
### Running Tests

```bash
python3.6 manage.py test
```


## Live Demo

The web app can be accessed from the following link
[click here]()


## Technology used

* [Python3.6](https://www.python.org/)

* [Flask](http://flask.pocoo.org/)

* [Heroku](https://heroku.com)

* [Bootstrap](https://bootstrapcdn.com)

## Contributing

- Git clone [https://github.com/MutumaMutuma/Personal-Blog.git](https://github.com/MutumaMutuma/Personal-Blog.git) 


## License

MIT License

&copy; Lewis Mutuma


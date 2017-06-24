How to set up a flask application
===========

#### Setting up AWS EC2
 - EC2 mirco is fine
 - ports
 - ubuntu 16.04
 - save IP address of server

#### Buy domain
 - route domain to server

#### Update server
 - `sudo apt-get update
    sudo apt-get upgrade`

#### Set up vim config
 - 

#### Setting up nginx
 - 

#### Setting up SSL certificates from let's encrypt

#### Setting up basic flask app
 - create folder `/var/www/vhosts/pahlakhat`. Go into folder
 - setting up virtualenv
   - `sudo apt-get install python-virtualenv`
 - create a virtual environment
   - `virtualenv pahlakhat`
 - activate virtual environment
   - `source pahlakhatenv/bin/activate`
   - prompt will now be prefexed with the name of the virtual environment
 - make a file called `pahlakhat.py` and put following code into it
     ```python
       from flask import Flask
       app = Flask(__name__)

       @app.route('/')
       def hello():
         return "Hello world!"

       if __name__ == '__main__':
         app.run()
     ```

#### Setting up Gunicorn (A production ready Python WSGI server that also provides scalability):
 - inside the virtualenv
   - `pip install gunicorn`
 - change `pahlakhat.py` to include a couple lines for gunicorn to work
     ```python
       from flask import Flask
       from werkzeug.contrib.fixers import ProxyFix
       app = Flask(__name__)

       @app.route('/')
       def hello():
         return "Hello world!"

       app.wsgi_app = ProxyFix(app.wsgi_app)

       if __name__ == '__main__':
         app.run()
     ```
 - Now running `gunicorn pahlakhat:app` will run the apolication
 - We should be able to see `Hello World!` on our browser with a secure certificate as well

### We should be able to test here that the application is working

#### Setting up supervisor on gunicorn

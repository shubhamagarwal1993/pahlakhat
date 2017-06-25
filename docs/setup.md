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
 - install nginx
 - now there should be a folder `/etc/nginx/sites-available` and `/etc/nginx/sites-enabled`.
 - Inside `/etc/nginx/sites-available`
   - make a file called `pahlakhat.conf` and put the following code in it
   ```
     server {
       listen 80;
       listen [::]:80;
       server_name pahlakhat.com www.pahlakhat.com;
       return 301 https://$server_name$request_uri;
     }
     
     server {
     
       listen 443 ssl http2;
       listen [::]:443 ssl http2;
       include snippets/ssl-pahlakhat.com.conf
       include snippets/ssl-params.conf;

       root /var/www/pahlakhat;
       server_name pahlakhat.com www.pahlakhat.com

       access_log /var/www/vhosts/pahlakhat/logs/access.log;
       error_log /var/www/vhosts/pahlakhat/logs/error.log;

       location / {
         proxy_set_header X-Forward-For $proxy_add_x_forwarded_for;
         proxy_set_header Host $http_host;
         proxy_redirect off;
         if (!-f $request_filename) {
           proxy_pass http://127.0.0.1:8000;
           break;
         }
       }
     }
   ```
 - Create the directory for nginx logs:
     `/var/www/vhosts/pahlakhat/logs/`
 - Enable new configuration by creating a symbolic link in sites-enabled directory
     `sudo ln -s /etc/nginx/sites-available/hello.conf /etc/nginx/sites-enabled/`
 - Check configuration for errors:
     `nginx -t`
 - If configuration is ok, then reload nginx
     `sudo service nginx reload`

#### Setting up SSL certificates from let's encrypt
 - check tutorials here `https://www.digitalocean.com/community/tutorials/how-to-secure-nginx-with-let-s-encrypt-on-ubuntu-16-04`

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
 - Now running `gunicorn pahlakhat:app` will run the application
   - `pahlakhat` is the name of the file (without extension) and `app` is the name of the Flask object.
 - We should be able to see `Hello World!` on our browser with a secure certificate as well

### We should be able to test here that the application is working

#### Setting up supervisor on gunicorn
 - install supervisor (can have virtualenv activated)
     `sudo apt-get install supervisor`
 - make a configuration file
     `sudo vim /etc/supervisor/conf.d/pahlakhat.conf`
 - put the following line in it
     ```
       [program:pahlakhat]
       command = /var/www/vhosts/pahlakhat/pahlakhatenv/bin/gunicorn pahlakhat:app -w 4
       directory = /var/www/vhosts/pahlakhat/pahlakhatenv
       user = ubuntu
       redirect_stderr = True
       environment = PRODUCTION=1
     ```
 - now update and restart supervisor
     `sudo supervisorctl reread`
     `sudo supervisorctl update`
     `sudo supervisorctl start pahlakhat`

# LegendaryOnline
This is a fan project to recreate the Marvel Legendary board game digitally.  This prototype is being developed as to support online play between friends and to learn new technologies.

### Setup

Install the latest version of Python (3.X).  Install virtualenv.

```
pip install virtualenv
```

Create a virtual environment at the project root, activate Python, and install the depedencies.
```
virtualenv env
env\Scripts\activate (Windows)
source env/bin/activate (Linux)
pip install -r requirements.txt
```
Note: If the mysql package fails to install, follow the workaround in this [link](http://stackoverflow.com/questions/26866147/mysql-python-install-fatal-error).

Run the database migrations and start the server.
```
python manage.py migrate --settings=legendary.settings.dev
python manage.py runserver --settings=legendary.settings.dev
```

Access the page at http://localhost:8000

### Legal
All product names, logos, images, brands, and copyrights are property of their respective owners.  The images and use of game content is designed for private use and is not intended to generate any income.
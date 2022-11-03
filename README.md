juha valimaki 2022-11-03

### create folder api
mkdir api
### move to folder api
cd api  
### create virtual environment .env under api folder
C:\Users\Omistaja\py_world\api> python -m venv .venv
### activate the virtual environment
.venv\Scripts\activate
### install flask
(.venv) PS C:\Users\Omistaja\py_world\api> pip install flask
### install flask-sqlalchemy
(.venv) PS C:\Users\Omistaja\py_world\api> pip install flask-sqlalchemy
### back up the environment dependencies to a file requirements.txt
(.venv) PS C:\Users\Omistaja\py_world\api> pip freeze > requirements.txt
### start the application app.py
(.venv) PS C:\Users\Omistaja\py_world\api> python app.py
### open your browser and get user guide from address:
http://localhost:5000/

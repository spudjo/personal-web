CALL ../venv/Scripts/activate.bat
set FLASK_APP=src/main.py
set FLASK_ENV=developer
set FLASK_DEBUG=1
flask run
cmd /k

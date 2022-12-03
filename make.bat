IF %1 == run (
    set FLASK_APP = main.py
    flask run
) 

IF %1 == activate (
    .\venv\Scripts\activate
)

IF %1 == ubuntu_env (
    docker run --name ubuntu_env -dit -p 3316:22 ubuntu_env:1.0.2
)
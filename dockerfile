FROM python:3.11.9-slim-bullseye

WORKDIR /Users/ankit/PycharmProjects/FlaskTutorial/flask_working

COPY requirements.txt ./

RUN python3 -m pip install --upgrade pip

RUN pip install -r requirements.txt

COPY . .

CMD ["python3", "-m", "flask", "--app", "loan_app", "run", "--host=0.0.0.0"]
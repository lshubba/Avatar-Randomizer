FROM python:3.8
COPY . /app
WORKDIR /app
RUN /usr/local/bin/python -m pip install --upgrade pip
RUN pip install -r requirements.txt
EXPOSE 5001
CMD ["flask", "--app", "application.py", "run", "--host=0.0.0.0"]
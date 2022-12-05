FROM python:3.8
COPY . /app
WORKDIR /app
ENV FLASK_APP=application.py
RUN /usr/local/bin/python -m pip install --upgrade pip
RUN pip install -r requirements.txt
EXPOSE 5001
ENTRYPOINT [ "python" ]
CMD [ "application.py" ]
# OUT OF SCOPE
FROM python:3.7-buster
COPY . /opt/exercise
WORKDIR /opt/exercise
RUN pip install -e . && mkdir -p instance/uploads
ENV FLASK_APP=appsec-exercise.py
CMD ["flask", "run", "--host=0.0.0.0", "--port=80"]

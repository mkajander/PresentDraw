FROM python:3.7-alpine


COPY . /app
# Install dependencies but we don't have any
#RUN pip install -r requirements.txt

WORKDIR /app

ENTRYPOINT ["python", "present_draw.py"]
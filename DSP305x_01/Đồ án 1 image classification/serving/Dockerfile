FROM python:3

COPY requirements.txt .

RUN pip install -r requirements.txt && \
	rm requirements.txt  
RUN apt-get update && apt-get install -y python3-opencv
RUN pip install opencv-python

EXPOSE 8000

COPY ./app /app

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
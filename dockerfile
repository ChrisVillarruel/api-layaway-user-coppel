FROM python:3.10
WORKDIR /code
COPY ./requirements.txt /code/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt
COPY . /code

# Puerto para el servicio del backend
EXPOSE 100

# Servicio backend API
CMD ["uvicorn", "main:app", "--proxy-headers", "--host", "0.0.0.0", "--port", "100", "--reload"]


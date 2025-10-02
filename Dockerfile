FROM python:3

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

CMD ["python", "app.py"]

# Examen practico - Automatización en Infraestructura Digital II - Froylan Alonso Pérez Alanis - José Manuel Pérez Gutiérrez
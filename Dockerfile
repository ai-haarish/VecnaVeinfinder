FROM python:3.11-slim

RUN apt-get update && apt-get install -y \
    python3-tk \
    tk \
    libgl1 \
    libglib2.0-0

WORKDIR /app

COPY . /app

RUN pip install -r requirements.txt

CMD ["python", "tkinter_gui.py"]

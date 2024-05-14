FROM python:3
WORKDIR /app
COPY . .
RUN pip install --no-cache-dir Flask
EXPOSE 80
CMD ["python3", "mesajlasma.py"]
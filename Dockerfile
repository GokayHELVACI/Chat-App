FROM python:3
WORKDIR /app
COPY . .
RUN pip install --no-cache-dir Flask
EXPOSE 80
CMD ["sudo", "su"]
CMD ["python3", "mesajlasma.py"]
FROM python:3.11-slim
RUN addgroup --system appgroup && adduser --system --group appuser
COPY . /app
WORKDIR /app
RUN chown -R appuser:appgroup /app
RUN pip install --no-cache-dir -r requirements.txt
USER appuser
EXPOSE 5000
CMD ["python", "app.py"]

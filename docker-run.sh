docker build -t flask-skeleton:latest .
docker run --rm -p 5000:5000 --name flask-skeleton flask-skeleton
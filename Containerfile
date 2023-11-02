FROM python:3.7-alpine
COPY . /app
WORKDIR /app
RUN pip install .
RUN kayrrentretientech create-db
RUN kayrrentretientech populate-db
RUN kayrrentretientech add-user -u admin -p admin
EXPOSE 5000
CMD ["kayrrentretientech", "run"]

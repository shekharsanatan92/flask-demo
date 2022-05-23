FROM python:3.9

COPY ./requirement.txt /app/requirements.txt

WORKDIR /app

RUN pip install --upgrade pip
RUN pip install --upgrade cython

RUN pip install --no-cache-dir -r requirements.txt

COPY . /app

EXPOSE 8080

ENTRYPOINT [ "python" ]

CMD ["app.py" ]
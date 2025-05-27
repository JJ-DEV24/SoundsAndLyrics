FROM python:3.12

WORKDIR /code

RUN apt update --yes && apt upgrade --yes

COPY ./requirements.txt ./

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

COPY ./ ./

EXPOSE 80

CMD ["fastapi", "run", "./main.py", "--port", "80"]


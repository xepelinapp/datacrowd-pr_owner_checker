FROM python:3-slim

COPY ./src /src
WORKDIR /src

ARG token

# We are installing a dependency here directly into our app source dir
RUN sh /src/config/install_gh_cli.sh
RUN pip install -r requirements.txt

CMD [ "python",  "/src/main.py" ]

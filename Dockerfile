FROM python:3.8.5-slim-buster

ENV PIP_NO_CACHE_DIR=off
ENV APP_USER=app
ENV APP_DIR=/opt/app

# Safer bash scripts with 'set -euxo pipefail'
SHELL ["/bin/bash", "-euxo", "pipefail", "-c"]

# Add app user
RUN useradd -m -s /bin/bash ${APP_USER} \
    && echo "${APP_USER}:${APP_USER}" | chpasswd

# Copy client files
COPY . ${APP_DIR}

# Install client dependencies
WORKDIR ${APP_DIR}
RUN pip install .

# Drop privileges
USER ${APP_USER}

ENTRYPOINT ["nlp-cli"]

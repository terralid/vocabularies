FROM python:3.12-slim-bookworm

ARG QUARTO_VERSION=1.8.26
ARG TARGETARCH=amd64

ADD https://github.com/quarto-dev/quarto-cli/releases/download/v${QUARTO_VERSION}/quarto-${QUARTO_VERSION}-linux-${TARGETARCH}.tar.gz /tmp/quarto.tar.gz
RUN tar -xzf /tmp/quarto.tar.gz -C /opt \
    && ln -s /opt/quarto-${QUARTO_VERSION}/bin/quarto /usr/local/bin/quarto \
    && rm /tmp/quarto.tar.gz

COPY tools/requirements.txt /tmp/requirements.txt
RUN pip install --no-cache-dir -r /tmp/requirements.txt

# The repository is mounted at runtime (see Makefile).
WORKDIR /repo

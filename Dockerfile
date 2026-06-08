FROM python:3.12-slim-bookworm

WORKDIR /app

COPY ./.github/actions/github_action_main.py .
COPY ./tools ./tools
COPY ./vocabulary ./vocabulary
COPY ./docs ./docs
COPY ./cache ./cache

RUN chmod a+x /app/github_action_main.py

# Force IPv4
RUN echo 'Acquire::ForceIPv4 "true";' > /etc/apt/apt.conf.d/99force-ipv4

# Switch Debian repos to HTTPS
RUN sed -i 's|http://deb.debian.org|https://deb.debian.org|g' /etc/apt/sources.list.d/debian.sources

RUN apt-get update && apt-get install -y --no-install-recommends \
    curl \
    gdebi-core \
    ca-certificates \
    && rm -rf /var/lib/apt/lists/*

RUN pip install -r /app/tools/requirements.txt

RUN curl -LO https://quarto.org/download/latest/quarto-linux-amd64.deb
RUN gdebi --non-interactive quarto-linux-amd64.deb

ENV PYTHONPATH=/app

ENTRYPOINT ["/app/github_action_main.py"]
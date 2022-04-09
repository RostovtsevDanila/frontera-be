FROM python:3.10-buster

ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1
ENV PATH="/venv/bin:$PATH"

CMD ["/app/entrypoint.sh"]

WORKDIR /app
RUN apt-get update \
 && apt-get install -y -qq --no-install-recommends curl nano iputils-ping ethtool tcpdump jq \
 && apt-get install -y -qq --no-install-recommends locales \
 && apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

COPY . /app

RUN python -m pip install pip --upgrade \
 && python -m pip install -r requirements/requirements.txt --no-cache-dir

RUN cp docker/entrypoint.sh ./ && chmod +x ./entrypoint.sh
#RUN python manage.py collectstatic --noinput

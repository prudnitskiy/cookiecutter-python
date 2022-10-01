FROM python:{{cookiecutter.python_major_version}}.{{cookiecutter.python_minor_version}}-alpine
WORKDIR /app
COPY requirements.txt /app/
RUN pip install -r /app/requirements.txt
COPY main.py /app/
{% if cookiecutter.service %}
EXPOSE 8080
{% end -%}
{% if cookiecutter.prometheus %}
EXPOSE 8081
{% end -%}
ENTRYPOINT ["/usr/local/bin/python", "/app/main.py"]

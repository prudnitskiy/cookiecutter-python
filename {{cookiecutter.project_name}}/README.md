# Overview

{{cookiecutter.project_short_description}}

This project was generated with [cookiecutter](https://github.com/audreyr/cookiecutter) using [prudnitskiy/cookiecutter-python](https://github.com/prudnitskiy/cookiecutter-python).

[![Build Status](https://img.shields.io/github/workflow/status/{{cookiecutter.github_username}}/{{cookiecutter.github_repo}}/main)](https://github.com/{{cookiecutter.github_username}}/{{cookiecutter.github_repo}}/actions)
[![Coverage Status](https://img.shields.io/codecov/c/gh/{{cookiecutter.github_username}}/{{cookiecutter.github_repo}})](https://codecov.io/gh/{{cookiecutter.github_username}}/{{cookiecutter.github_repo}})

## Setup

### Requirements

* Python {{cookiecutter.python_major_version}}.{{cookiecutter.python_minor_version}}+

### Installation
#### Docker

You can build a docker image via `docker build -f Dockerfile . -t {{ cookiecutter.github_repo }}`

#### System

- create and enable VEnv
- install dependencies via `pip install -r app/requirements.txt`
- start the app via `python3 app/main.py`

### Usage

{% if cookiecutter.prometheus %}
#### Metrics

Metrics are avaliable via `<host>:8081/metrics`.

Those metrics are exported in prometheus openmetrics standart.
{% end -%}

### Known bugs and limitations

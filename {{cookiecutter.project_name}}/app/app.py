#!/usr/bin/env python3
import logging
import argparse
{% if cookiecutter.use_prometheus == "y" %}
import prometheus_client
{% end -%}

if __name__ == '__main__':
    # Config
    parser = argparse.ArgumentParser(description='ChaosMonkey')
    parser.add_argument('--verbose',
                        '-v',
                        help='verbosity level',
                        default='info')
    parser.add_argument('--dry-run',
                        '-d',
                        action="store_true",
                        help='dry run (no changes)',
                        default=False)
    clargs = parser.parse_args()

    logging.basicConfig(format='[%(levelname)s][%(asctime)s]: %(message)s',
                        level=clargs.verbose.upper())

    #Init
    logging.info("Starting up")
    {% if cookiecutter.use_prometheus == "y" %}
    prom_epoch = Counter('epoch', 'epochs passed since first run')

    prometheus_client.start_http_server(8000)
    {% end -%}

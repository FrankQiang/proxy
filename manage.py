#!/usr/bin/env python3
from app import create_app


class Config(object):
    SECRET_KEY = "SECRET_KEY"
    SCHEDULER_API_ENABLED = True
    REDIS_URL = "redis://proxy_redis:6379/0"

    JOBS = [
        {
            'id': 'get_proxy',
            'func': 'app.jobs:get_proxy',
            'trigger': 'interval',
            'seconds': 30
        }
    ]

    @staticmethod
    def init_app(app):
        pass


app = create_app(Config)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5001)

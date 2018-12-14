from flask import Flask
from flask_redis import FlaskRedis
from flask_apscheduler import APScheduler

redis_store = FlaskRedis()
scheduler = APScheduler()


def create_app(config):
    app = Flask(__name__)
    app.config.from_object(config)
    config.init_app(app)
    redis_store.init_app(app)
    scheduler.init_app(app)
    scheduler.start()
    from .api_1_0 import api_blueprint
    app.register_blueprint(api_blueprint, url_prefix='/api/v1')
    return app

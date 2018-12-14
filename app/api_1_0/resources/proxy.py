import random
from flask import request
from flask_restful import Resource
from app import redis_store
from constant import KEY


class ProxyAPI(Resource):

    def get(self):
        proxies = redis_store.hgetall(KEY)
        if proxies:
            proxy = random.choice(list(proxies.keys()))
            return {"code": 0, "msg": "success",
                    "proxy": proxy.decode("utf-8")
                    }
        else:
            return {"code": 1, "msg": "no more proxy"}

    def delete(self):
        json_data = request.get_json(force=True)
        proxy = json_data.get("proxy", '')
        if proxy:
            redis_store.hdel(KEY, proxy)
        return {"code": 0, "msg": "success"}

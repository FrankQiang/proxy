import requests
from app import redis_store
from constant import KEY, LIMIT, NUM, TAI_YANG_PROXY


def get_proxy():
    len = redis_store.hlen(KEY)
    if len < LIMIT:
        rsp = requests.get(TAI_YANG_PROXY.format(num=NUM))
        data = rsp.json()
        if 0 == data["code"]:
            proxies = data["data"]
            for proxy in proxies:
                ip_port = "{ip}:{port}".format(ip=proxy["ip"],
                                               port=proxy["port"])
                redis_store.hset(KEY, ip_port, 1)

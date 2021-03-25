import time

import redis


class RedisClient(object):

    def __init__(self, **kwargs):
        assert kwargs.get('host'), 'param host is required'
        assert kwargs.get('port'), 'param port is required'
        #assert kwargs.get('password'), 'param password is required'
        assert kwargs.get('db'), 'param db is required'
        self.kwargs = kwargs
        self._connect()

    @classmethod
    def from_config(cls, config):
        kwargs = {}
        for key in dir(config):
            if key.isupper() and key.startswith('REDIS_'):
                kwargs[key.split('REDIS_')[-1].lower()] = getattr(config, key)
        return cls(**kwargs)

    def _connect(self):
        try:
            self.connection = redis.Redis(**self.kwargs)
        except Exception as e:
            print(e)
            time.sleep(3)
            self._connect()

    def set(self, key, value):
        try:
            return self.connection.set(key, value)
        except Exception as e:
            print(e)
            time.sleep(3)
            self._connect()
            return self.set(key, value)

    def get(self, key):
        try:
            return self.connection.get(key)
        except Exception as e:
            print(e)
            time.sleep(3)
            self._connect()
            return self.get(key)

    def rpush(self, key, value):
        try:
            return self.connection.rpush(key, value)
        except Exception as e:
            print(e)
            time.sleep(3)
            self._connect()
            return self.rpush(key, value)

    def lpop(self, key):
        try:
            return self.connection.lpop(key)
        except Exception as e:
            print(e)
            time.sleep(3)
            self._connect()
            return self.lpop(key)

    def zadd(self, key, value, score=-1):
        try:
            return self.connection.zadd(key, {value: score})
        except Exception as e:
            print(e)
            time.sleep(3)
            self._connect()
            return self.zadd(key, value, score)

    def zpop(self, key, batch_size=None):
        try:
            card = self.connection.zcard(key) - 1
            if batch_size:
                batch_size = batch_size - 1
                batch_size = card if batch_size > card else batch_size
            else:
                batch_size = card
            pipe = self.connection.pipeline()
            pipe.multi()
            pipe.zrange(key, 0, batch_size).zremrangebyrank(key, 0, batch_size)
            results, count = pipe.execute()
            return results
        except Exception as e:
            print(e)
            time.sleep(3)
            self._connect()
            return self.zpop(key, batch_size)

    def sadd(self, key, value):
        try:
            return self.connection.sadd(key, value)
        except Exception as e:
            print(e)
            time.sleep(3)
            self._connect()
            return self.sadd(key, value)

    def sismember(self, key, value):
        try:
            return self.connection.sismember(key, value)
        except Exception as e:
            print(e)
            time.sleep(3)
            self._connect()
            return self.sismember(key, value)

    def exits(self, key):
        try:
            return self.connection.exists(key)
        except Exception as e:
            print(e)
            time.sleep(3)
            self._connect()
            return self.exits(key)

    def delete(self, key):
        try:
            return self.connection.delete(key)
        except Exception as e:
            print(e)
            time.sleep(3)
            self._connect()
            return self.delete(key)

    def close(self):
        self.connection.close()



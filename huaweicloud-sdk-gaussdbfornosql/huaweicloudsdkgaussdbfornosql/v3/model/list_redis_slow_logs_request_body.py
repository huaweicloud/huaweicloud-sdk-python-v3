# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListRedisSlowLogsRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'start_time': 'str',
        'end_time': 'str',
        'limit': 'int',
        'line_num': 'str',
        'operate_type': 'str',
        'node_id': 'str',
        'keywords': 'list[str]',
        'max_cost_time': 'float',
        'min_cost_time': 'float'
    }

    attribute_map = {
        'start_time': 'start_time',
        'end_time': 'end_time',
        'limit': 'limit',
        'line_num': 'line_num',
        'operate_type': 'operate_type',
        'node_id': 'node_id',
        'keywords': 'keywords',
        'max_cost_time': 'max_cost_time',
        'min_cost_time': 'min_cost_time'
    }

    def __init__(self, start_time=None, end_time=None, limit=None, line_num=None, operate_type=None, node_id=None, keywords=None, max_cost_time=None, min_cost_time=None):
        r"""ListRedisSlowLogsRequestBody

        The model defined in huaweicloud sdk

        :param start_time: 开始时间，格式为“yyyy-mm-ddThh:mm:ssZ”。 其中，T指某个时间的开始；Z指时区偏移量，例如北京时间偏移显示为+0800。注：开始时间不得早于当前时间30天。
        :type start_time: str
        :param end_time: 结束时间，格式为“yyyy-mm-ddThh:mm:ssZ”。 其中，T指某个时间的开始；Z指时区偏移量，例如北京时间偏移显示为+0800。注：结束时间不能晚于当前时间。
        :type end_time: str
        :param limit: 表示每次查询的日志条数，最大限制100条。
        :type limit: int
        :param line_num: 日志单行序列号，第一次查询时不需要此参数，下一次查询时需要使用，可从上一次查询的返回信息中获取。 说明：当次查询从line_num的下一条日志开始查询，不包含当前line_num日志。
        :type line_num: str
        :param operate_type: 语句类型，取空值，表示查询所有语句类型。支持查询的所有语句类型如下（以\&quot;|\&quot;分割）： set|get|del|incr|incrby|incrbyfloat|decr|decrby|getset|append|mget|keys|setnx|setex|psetex|delvx|mset| msetnx|getrange|substr|setrange|strlen|exists|expire|pexpire|expireat|pexpireat|ttl|pttl|persist|type| scanx|pksetexat|sort|hdel|hset|hget|hgetall|hexists|hincrby|hincrbyfloat|hkeys|hlen|hmget|hmset|hsetnx| hstrlen|hvals|hscan|hscanx|pkhscanrange|pkhrscanrange|lindex|linsert|llen|lpop|lpush|lpushx|lrange|lrem| lset|ltrim|rpop|rpoplpush|rpush|rpushx|zadd|zcard|zscan|zincrby|zrange|zrevrange|zrangebyscore| zrevrangebyscore|zcount|zrem|zunionstore|zinterstore|zrank|zrevrank|zscore|zrangebylex|zrevrangebylex| zlexcount|zremrangebyrank|zremrangebyscore|zremrangebylex|zpopmax|zpopmin|sadd|spop|scard|smembers|sscan| srem|sunion|sunionstore|sinter|sinterstore|sismember|sdiff|sdiffstore|smove|srandmember|bitset|bitget| bitcount|bitpos|bitop|bitfield|pfadd|pfcount|pfmerge|geoadd|georadiusbymember|georadius|geohash|geodist| geopos|xadd|xack|xgroup|xdel|xtrim|xlen|xrange|xrevrange|xclaim|xpending|xinfo|xread|xreadgroup|
        :type operate_type: str
        :param node_id: 节点ID，取空值，表示查询实例下所有允许查询的节点。 具体取值请参考查询实例列表和详情接口\&quot;ListInstances\&quot;中nodes字段数据结构说明的“id”。
        :type node_id: str
        :param keywords: 根据多个关键字搜索日志全文，表示同时匹配所有关键字。 - 最多支持10个关键字。 - 每个关键字最大长度不超过512个字符。
        :type keywords: list[str]
        :param max_cost_time: 支持根据最大执行时间范围查找日志。单位：ms
        :type max_cost_time: float
        :param min_cost_time: 支持根据最小执行时间范围查找日志。单位：ms
        :type min_cost_time: float
        """
        
        

        self._start_time = None
        self._end_time = None
        self._limit = None
        self._line_num = None
        self._operate_type = None
        self._node_id = None
        self._keywords = None
        self._max_cost_time = None
        self._min_cost_time = None
        self.discriminator = None

        self.start_time = start_time
        self.end_time = end_time
        self.limit = limit
        if line_num is not None:
            self.line_num = line_num
        if operate_type is not None:
            self.operate_type = operate_type
        if node_id is not None:
            self.node_id = node_id
        if keywords is not None:
            self.keywords = keywords
        if max_cost_time is not None:
            self.max_cost_time = max_cost_time
        if min_cost_time is not None:
            self.min_cost_time = min_cost_time

    @property
    def start_time(self):
        r"""Gets the start_time of this ListRedisSlowLogsRequestBody.

        开始时间，格式为“yyyy-mm-ddThh:mm:ssZ”。 其中，T指某个时间的开始；Z指时区偏移量，例如北京时间偏移显示为+0800。注：开始时间不得早于当前时间30天。

        :return: The start_time of this ListRedisSlowLogsRequestBody.
        :rtype: str
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        r"""Sets the start_time of this ListRedisSlowLogsRequestBody.

        开始时间，格式为“yyyy-mm-ddThh:mm:ssZ”。 其中，T指某个时间的开始；Z指时区偏移量，例如北京时间偏移显示为+0800。注：开始时间不得早于当前时间30天。

        :param start_time: The start_time of this ListRedisSlowLogsRequestBody.
        :type start_time: str
        """
        self._start_time = start_time

    @property
    def end_time(self):
        r"""Gets the end_time of this ListRedisSlowLogsRequestBody.

        结束时间，格式为“yyyy-mm-ddThh:mm:ssZ”。 其中，T指某个时间的开始；Z指时区偏移量，例如北京时间偏移显示为+0800。注：结束时间不能晚于当前时间。

        :return: The end_time of this ListRedisSlowLogsRequestBody.
        :rtype: str
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        r"""Sets the end_time of this ListRedisSlowLogsRequestBody.

        结束时间，格式为“yyyy-mm-ddThh:mm:ssZ”。 其中，T指某个时间的开始；Z指时区偏移量，例如北京时间偏移显示为+0800。注：结束时间不能晚于当前时间。

        :param end_time: The end_time of this ListRedisSlowLogsRequestBody.
        :type end_time: str
        """
        self._end_time = end_time

    @property
    def limit(self):
        r"""Gets the limit of this ListRedisSlowLogsRequestBody.

        表示每次查询的日志条数，最大限制100条。

        :return: The limit of this ListRedisSlowLogsRequestBody.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListRedisSlowLogsRequestBody.

        表示每次查询的日志条数，最大限制100条。

        :param limit: The limit of this ListRedisSlowLogsRequestBody.
        :type limit: int
        """
        self._limit = limit

    @property
    def line_num(self):
        r"""Gets the line_num of this ListRedisSlowLogsRequestBody.

        日志单行序列号，第一次查询时不需要此参数，下一次查询时需要使用，可从上一次查询的返回信息中获取。 说明：当次查询从line_num的下一条日志开始查询，不包含当前line_num日志。

        :return: The line_num of this ListRedisSlowLogsRequestBody.
        :rtype: str
        """
        return self._line_num

    @line_num.setter
    def line_num(self, line_num):
        r"""Sets the line_num of this ListRedisSlowLogsRequestBody.

        日志单行序列号，第一次查询时不需要此参数，下一次查询时需要使用，可从上一次查询的返回信息中获取。 说明：当次查询从line_num的下一条日志开始查询，不包含当前line_num日志。

        :param line_num: The line_num of this ListRedisSlowLogsRequestBody.
        :type line_num: str
        """
        self._line_num = line_num

    @property
    def operate_type(self):
        r"""Gets the operate_type of this ListRedisSlowLogsRequestBody.

        语句类型，取空值，表示查询所有语句类型。支持查询的所有语句类型如下（以\"|\"分割）： set|get|del|incr|incrby|incrbyfloat|decr|decrby|getset|append|mget|keys|setnx|setex|psetex|delvx|mset| msetnx|getrange|substr|setrange|strlen|exists|expire|pexpire|expireat|pexpireat|ttl|pttl|persist|type| scanx|pksetexat|sort|hdel|hset|hget|hgetall|hexists|hincrby|hincrbyfloat|hkeys|hlen|hmget|hmset|hsetnx| hstrlen|hvals|hscan|hscanx|pkhscanrange|pkhrscanrange|lindex|linsert|llen|lpop|lpush|lpushx|lrange|lrem| lset|ltrim|rpop|rpoplpush|rpush|rpushx|zadd|zcard|zscan|zincrby|zrange|zrevrange|zrangebyscore| zrevrangebyscore|zcount|zrem|zunionstore|zinterstore|zrank|zrevrank|zscore|zrangebylex|zrevrangebylex| zlexcount|zremrangebyrank|zremrangebyscore|zremrangebylex|zpopmax|zpopmin|sadd|spop|scard|smembers|sscan| srem|sunion|sunionstore|sinter|sinterstore|sismember|sdiff|sdiffstore|smove|srandmember|bitset|bitget| bitcount|bitpos|bitop|bitfield|pfadd|pfcount|pfmerge|geoadd|georadiusbymember|georadius|geohash|geodist| geopos|xadd|xack|xgroup|xdel|xtrim|xlen|xrange|xrevrange|xclaim|xpending|xinfo|xread|xreadgroup|

        :return: The operate_type of this ListRedisSlowLogsRequestBody.
        :rtype: str
        """
        return self._operate_type

    @operate_type.setter
    def operate_type(self, operate_type):
        r"""Sets the operate_type of this ListRedisSlowLogsRequestBody.

        语句类型，取空值，表示查询所有语句类型。支持查询的所有语句类型如下（以\"|\"分割）： set|get|del|incr|incrby|incrbyfloat|decr|decrby|getset|append|mget|keys|setnx|setex|psetex|delvx|mset| msetnx|getrange|substr|setrange|strlen|exists|expire|pexpire|expireat|pexpireat|ttl|pttl|persist|type| scanx|pksetexat|sort|hdel|hset|hget|hgetall|hexists|hincrby|hincrbyfloat|hkeys|hlen|hmget|hmset|hsetnx| hstrlen|hvals|hscan|hscanx|pkhscanrange|pkhrscanrange|lindex|linsert|llen|lpop|lpush|lpushx|lrange|lrem| lset|ltrim|rpop|rpoplpush|rpush|rpushx|zadd|zcard|zscan|zincrby|zrange|zrevrange|zrangebyscore| zrevrangebyscore|zcount|zrem|zunionstore|zinterstore|zrank|zrevrank|zscore|zrangebylex|zrevrangebylex| zlexcount|zremrangebyrank|zremrangebyscore|zremrangebylex|zpopmax|zpopmin|sadd|spop|scard|smembers|sscan| srem|sunion|sunionstore|sinter|sinterstore|sismember|sdiff|sdiffstore|smove|srandmember|bitset|bitget| bitcount|bitpos|bitop|bitfield|pfadd|pfcount|pfmerge|geoadd|georadiusbymember|georadius|geohash|geodist| geopos|xadd|xack|xgroup|xdel|xtrim|xlen|xrange|xrevrange|xclaim|xpending|xinfo|xread|xreadgroup|

        :param operate_type: The operate_type of this ListRedisSlowLogsRequestBody.
        :type operate_type: str
        """
        self._operate_type = operate_type

    @property
    def node_id(self):
        r"""Gets the node_id of this ListRedisSlowLogsRequestBody.

        节点ID，取空值，表示查询实例下所有允许查询的节点。 具体取值请参考查询实例列表和详情接口\"ListInstances\"中nodes字段数据结构说明的“id”。

        :return: The node_id of this ListRedisSlowLogsRequestBody.
        :rtype: str
        """
        return self._node_id

    @node_id.setter
    def node_id(self, node_id):
        r"""Sets the node_id of this ListRedisSlowLogsRequestBody.

        节点ID，取空值，表示查询实例下所有允许查询的节点。 具体取值请参考查询实例列表和详情接口\"ListInstances\"中nodes字段数据结构说明的“id”。

        :param node_id: The node_id of this ListRedisSlowLogsRequestBody.
        :type node_id: str
        """
        self._node_id = node_id

    @property
    def keywords(self):
        r"""Gets the keywords of this ListRedisSlowLogsRequestBody.

        根据多个关键字搜索日志全文，表示同时匹配所有关键字。 - 最多支持10个关键字。 - 每个关键字最大长度不超过512个字符。

        :return: The keywords of this ListRedisSlowLogsRequestBody.
        :rtype: list[str]
        """
        return self._keywords

    @keywords.setter
    def keywords(self, keywords):
        r"""Sets the keywords of this ListRedisSlowLogsRequestBody.

        根据多个关键字搜索日志全文，表示同时匹配所有关键字。 - 最多支持10个关键字。 - 每个关键字最大长度不超过512个字符。

        :param keywords: The keywords of this ListRedisSlowLogsRequestBody.
        :type keywords: list[str]
        """
        self._keywords = keywords

    @property
    def max_cost_time(self):
        r"""Gets the max_cost_time of this ListRedisSlowLogsRequestBody.

        支持根据最大执行时间范围查找日志。单位：ms

        :return: The max_cost_time of this ListRedisSlowLogsRequestBody.
        :rtype: float
        """
        return self._max_cost_time

    @max_cost_time.setter
    def max_cost_time(self, max_cost_time):
        r"""Sets the max_cost_time of this ListRedisSlowLogsRequestBody.

        支持根据最大执行时间范围查找日志。单位：ms

        :param max_cost_time: The max_cost_time of this ListRedisSlowLogsRequestBody.
        :type max_cost_time: float
        """
        self._max_cost_time = max_cost_time

    @property
    def min_cost_time(self):
        r"""Gets the min_cost_time of this ListRedisSlowLogsRequestBody.

        支持根据最小执行时间范围查找日志。单位：ms

        :return: The min_cost_time of this ListRedisSlowLogsRequestBody.
        :rtype: float
        """
        return self._min_cost_time

    @min_cost_time.setter
    def min_cost_time(self, min_cost_time):
        r"""Sets the min_cost_time of this ListRedisSlowLogsRequestBody.

        支持根据最小执行时间范围查找日志。单位：ms

        :param min_cost_time: The min_cost_time of this ListRedisSlowLogsRequestBody.
        :type min_cost_time: float
        """
        self._min_cost_time = min_cost_time

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                if attr in self.sensitive_list:
                    result[attr] = "****"
                else:
                    result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        import simplejson as json
        if six.PY2:
            import sys
            reload(sys)
            sys.setdefaultencoding("utf-8")
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ListRedisSlowLogsRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

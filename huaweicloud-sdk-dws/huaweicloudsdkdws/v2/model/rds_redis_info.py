# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class RdsRedisInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'id': 'str',
        'cluster_id': 'str',
        'start_time': 'str',
        'end_time': 'str',
        'status': 'str',
        'redis_conf': 'RedisConf',
        'redis_progress': 'RedisProgress',
        'redis_table_detail': 'RedisTableDetail'
    }

    attribute_map = {
        'id': 'id',
        'cluster_id': 'cluster_id',
        'start_time': 'start_time',
        'end_time': 'end_time',
        'status': 'status',
        'redis_conf': 'redis_conf',
        'redis_progress': 'redis_progress',
        'redis_table_detail': 'redis_table_detail'
    }

    def __init__(self, id=None, cluster_id=None, start_time=None, end_time=None, status=None, redis_conf=None, redis_progress=None, redis_table_detail=None):
        """RdsRedisInfo

        The model defined in huaweicloud sdk

        :param id: ID
        :type id: str
        :param cluster_id: 集群ID
        :type cluster_id: str
        :param start_time: 开始时间
        :type start_time: str
        :param end_time: 结束时间
        :type end_time: str
        :param status: 状态
        :type status: str
        :param redis_conf: 
        :type redis_conf: :class:`huaweicloudsdkdws.v2.RedisConf`
        :param redis_progress: 
        :type redis_progress: :class:`huaweicloudsdkdws.v2.RedisProgress`
        :param redis_table_detail: 
        :type redis_table_detail: :class:`huaweicloudsdkdws.v2.RedisTableDetail`
        """
        
        

        self._id = None
        self._cluster_id = None
        self._start_time = None
        self._end_time = None
        self._status = None
        self._redis_conf = None
        self._redis_progress = None
        self._redis_table_detail = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if cluster_id is not None:
            self.cluster_id = cluster_id
        if start_time is not None:
            self.start_time = start_time
        if end_time is not None:
            self.end_time = end_time
        if status is not None:
            self.status = status
        if redis_conf is not None:
            self.redis_conf = redis_conf
        if redis_progress is not None:
            self.redis_progress = redis_progress
        if redis_table_detail is not None:
            self.redis_table_detail = redis_table_detail

    @property
    def id(self):
        """Gets the id of this RdsRedisInfo.

        ID

        :return: The id of this RdsRedisInfo.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this RdsRedisInfo.

        ID

        :param id: The id of this RdsRedisInfo.
        :type id: str
        """
        self._id = id

    @property
    def cluster_id(self):
        """Gets the cluster_id of this RdsRedisInfo.

        集群ID

        :return: The cluster_id of this RdsRedisInfo.
        :rtype: str
        """
        return self._cluster_id

    @cluster_id.setter
    def cluster_id(self, cluster_id):
        """Sets the cluster_id of this RdsRedisInfo.

        集群ID

        :param cluster_id: The cluster_id of this RdsRedisInfo.
        :type cluster_id: str
        """
        self._cluster_id = cluster_id

    @property
    def start_time(self):
        """Gets the start_time of this RdsRedisInfo.

        开始时间

        :return: The start_time of this RdsRedisInfo.
        :rtype: str
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        """Sets the start_time of this RdsRedisInfo.

        开始时间

        :param start_time: The start_time of this RdsRedisInfo.
        :type start_time: str
        """
        self._start_time = start_time

    @property
    def end_time(self):
        """Gets the end_time of this RdsRedisInfo.

        结束时间

        :return: The end_time of this RdsRedisInfo.
        :rtype: str
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        """Sets the end_time of this RdsRedisInfo.

        结束时间

        :param end_time: The end_time of this RdsRedisInfo.
        :type end_time: str
        """
        self._end_time = end_time

    @property
    def status(self):
        """Gets the status of this RdsRedisInfo.

        状态

        :return: The status of this RdsRedisInfo.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this RdsRedisInfo.

        状态

        :param status: The status of this RdsRedisInfo.
        :type status: str
        """
        self._status = status

    @property
    def redis_conf(self):
        """Gets the redis_conf of this RdsRedisInfo.

        :return: The redis_conf of this RdsRedisInfo.
        :rtype: :class:`huaweicloudsdkdws.v2.RedisConf`
        """
        return self._redis_conf

    @redis_conf.setter
    def redis_conf(self, redis_conf):
        """Sets the redis_conf of this RdsRedisInfo.

        :param redis_conf: The redis_conf of this RdsRedisInfo.
        :type redis_conf: :class:`huaweicloudsdkdws.v2.RedisConf`
        """
        self._redis_conf = redis_conf

    @property
    def redis_progress(self):
        """Gets the redis_progress of this RdsRedisInfo.

        :return: The redis_progress of this RdsRedisInfo.
        :rtype: :class:`huaweicloudsdkdws.v2.RedisProgress`
        """
        return self._redis_progress

    @redis_progress.setter
    def redis_progress(self, redis_progress):
        """Sets the redis_progress of this RdsRedisInfo.

        :param redis_progress: The redis_progress of this RdsRedisInfo.
        :type redis_progress: :class:`huaweicloudsdkdws.v2.RedisProgress`
        """
        self._redis_progress = redis_progress

    @property
    def redis_table_detail(self):
        """Gets the redis_table_detail of this RdsRedisInfo.

        :return: The redis_table_detail of this RdsRedisInfo.
        :rtype: :class:`huaweicloudsdkdws.v2.RedisTableDetail`
        """
        return self._redis_table_detail

    @redis_table_detail.setter
    def redis_table_detail(self, redis_table_detail):
        """Sets the redis_table_detail of this RdsRedisInfo.

        :param redis_table_detail: The redis_table_detail of this RdsRedisInfo.
        :type redis_table_detail: :class:`huaweicloudsdkdws.v2.RedisTableDetail`
        """
        self._redis_table_detail = redis_table_detail

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
        if not isinstance(other, RdsRedisInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

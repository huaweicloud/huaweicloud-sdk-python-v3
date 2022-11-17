# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateRedislogRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'instance_id': 'str',
        'query_time': 'int',
        'log_type': 'str',
        'replication_id': 'str'
    }

    attribute_map = {
        'instance_id': 'instance_id',
        'query_time': 'query_time',
        'log_type': 'log_type',
        'replication_id': 'replication_id'
    }

    def __init__(self, instance_id=None, query_time=None, log_type=None, replication_id=None):
        """CreateRedislogRequest

        The model defined in huaweicloud sdk

        :param instance_id: 实例ID。
        :type instance_id: str
        :param query_time: 日期偏移量，表示从过去的n天开始查询，例如：传入0则表示查询今天的日志，传入7则表示查询过去7天的日志。最大支持0-7。
        :type query_time: int
        :param log_type: 返回日志的类型，当前仅支持Redis运行日志，类型为run
        :type log_type: str
        :param replication_id: 副本ID，可以从分片与副本中查询对应节点的副本ID
        :type replication_id: str
        """
        
        

        self._instance_id = None
        self._query_time = None
        self._log_type = None
        self._replication_id = None
        self.discriminator = None

        self.instance_id = instance_id
        if query_time is not None:
            self.query_time = query_time
        self.log_type = log_type
        if replication_id is not None:
            self.replication_id = replication_id

    @property
    def instance_id(self):
        """Gets the instance_id of this CreateRedislogRequest.

        实例ID。

        :return: The instance_id of this CreateRedislogRequest.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        """Sets the instance_id of this CreateRedislogRequest.

        实例ID。

        :param instance_id: The instance_id of this CreateRedislogRequest.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def query_time(self):
        """Gets the query_time of this CreateRedislogRequest.

        日期偏移量，表示从过去的n天开始查询，例如：传入0则表示查询今天的日志，传入7则表示查询过去7天的日志。最大支持0-7。

        :return: The query_time of this CreateRedislogRequest.
        :rtype: int
        """
        return self._query_time

    @query_time.setter
    def query_time(self, query_time):
        """Sets the query_time of this CreateRedislogRequest.

        日期偏移量，表示从过去的n天开始查询，例如：传入0则表示查询今天的日志，传入7则表示查询过去7天的日志。最大支持0-7。

        :param query_time: The query_time of this CreateRedislogRequest.
        :type query_time: int
        """
        self._query_time = query_time

    @property
    def log_type(self):
        """Gets the log_type of this CreateRedislogRequest.

        返回日志的类型，当前仅支持Redis运行日志，类型为run

        :return: The log_type of this CreateRedislogRequest.
        :rtype: str
        """
        return self._log_type

    @log_type.setter
    def log_type(self, log_type):
        """Sets the log_type of this CreateRedislogRequest.

        返回日志的类型，当前仅支持Redis运行日志，类型为run

        :param log_type: The log_type of this CreateRedislogRequest.
        :type log_type: str
        """
        self._log_type = log_type

    @property
    def replication_id(self):
        """Gets the replication_id of this CreateRedislogRequest.

        副本ID，可以从分片与副本中查询对应节点的副本ID

        :return: The replication_id of this CreateRedislogRequest.
        :rtype: str
        """
        return self._replication_id

    @replication_id.setter
    def replication_id(self, replication_id):
        """Sets the replication_id of this CreateRedislogRequest.

        副本ID，可以从分片与副本中查询对应节点的副本ID

        :param replication_id: The replication_id of this CreateRedislogRequest.
        :type replication_id: str
        """
        self._replication_id = replication_id

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
        if not isinstance(other, CreateRedislogRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListRedislogRequest:

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
        'offset': 'int',
        'limit': 'int',
        'log_type': 'str'
    }

    attribute_map = {
        'instance_id': 'instance_id',
        'offset': 'offset',
        'limit': 'limit',
        'log_type': 'log_type'
    }

    def __init__(self, instance_id=None, offset=None, limit=None, log_type=None):
        """ListRedislogRequest

        The model defined in huaweicloud sdk

        :param instance_id: 实例ID。
        :type instance_id: str
        :param offset: 偏移量，表示从此偏移量开始查询， offset大于等于0
        :type offset: int
        :param limit: 每页显示的条目数量。
        :type limit: int
        :param log_type: 返回日志的类型，当前仅支持Redis运行日志，类型为run
        :type log_type: str
        """
        
        

        self._instance_id = None
        self._offset = None
        self._limit = None
        self._log_type = None
        self.discriminator = None

        self.instance_id = instance_id
        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit
        self.log_type = log_type

    @property
    def instance_id(self):
        """Gets the instance_id of this ListRedislogRequest.

        实例ID。

        :return: The instance_id of this ListRedislogRequest.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        """Sets the instance_id of this ListRedislogRequest.

        实例ID。

        :param instance_id: The instance_id of this ListRedislogRequest.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def offset(self):
        """Gets the offset of this ListRedislogRequest.

        偏移量，表示从此偏移量开始查询， offset大于等于0

        :return: The offset of this ListRedislogRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this ListRedislogRequest.

        偏移量，表示从此偏移量开始查询， offset大于等于0

        :param offset: The offset of this ListRedislogRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        """Gets the limit of this ListRedislogRequest.

        每页显示的条目数量。

        :return: The limit of this ListRedislogRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListRedislogRequest.

        每页显示的条目数量。

        :param limit: The limit of this ListRedislogRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def log_type(self):
        """Gets the log_type of this ListRedislogRequest.

        返回日志的类型，当前仅支持Redis运行日志，类型为run

        :return: The log_type of this ListRedislogRequest.
        :rtype: str
        """
        return self._log_type

    @log_type.setter
    def log_type(self, log_type):
        """Sets the log_type of this ListRedislogRequest.

        返回日志的类型，当前仅支持Redis运行日志，类型为run

        :param log_type: The log_type of this ListRedislogRequest.
        :type log_type: str
        """
        self._log_type = log_type

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
        if not isinstance(other, ListRedislogRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

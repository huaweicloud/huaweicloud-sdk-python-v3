# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class WhiteBlackIpResponseBody:


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
        'ip': 'str',
        'white': 'int',
        'timestamp': 'int'
    }

    attribute_map = {
        'id': 'id',
        'ip': 'ip',
        'white': 'white',
        'timestamp': 'timestamp'
    }

    def __init__(self, id=None, ip=None, white=None, timestamp=None):
        """WhiteBlackIpResponseBody - a model defined in huaweicloud sdk"""
        
        

        self._id = None
        self._ip = None
        self._white = None
        self._timestamp = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if ip is not None:
            self.ip = ip
        if white is not None:
            self.white = white
        if timestamp is not None:
            self.timestamp = timestamp

    @property
    def id(self):
        """Gets the id of this WhiteBlackIpResponseBody.

        规则id

        :return: The id of this WhiteBlackIpResponseBody.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this WhiteBlackIpResponseBody.

        规则id

        :param id: The id of this WhiteBlackIpResponseBody.
        :type: str
        """
        self._id = id

    @property
    def ip(self):
        """Gets the ip of this WhiteBlackIpResponseBody.

        黑白名单

        :return: The ip of this WhiteBlackIpResponseBody.
        :rtype: str
        """
        return self._ip

    @ip.setter
    def ip(self, ip):
        """Sets the ip of this WhiteBlackIpResponseBody.

        黑白名单

        :param ip: The ip of this WhiteBlackIpResponseBody.
        :type: str
        """
        self._ip = ip

    @property
    def white(self):
        """Gets the white of this WhiteBlackIpResponseBody.

        类型，0拦截，1放行

        :return: The white of this WhiteBlackIpResponseBody.
        :rtype: int
        """
        return self._white

    @white.setter
    def white(self, white):
        """Sets the white of this WhiteBlackIpResponseBody.

        类型，0拦截，1放行

        :param white: The white of this WhiteBlackIpResponseBody.
        :type: int
        """
        self._white = white

    @property
    def timestamp(self):
        """Gets the timestamp of this WhiteBlackIpResponseBody.

        创建规则的时间戳

        :return: The timestamp of this WhiteBlackIpResponseBody.
        :rtype: int
        """
        return self._timestamp

    @timestamp.setter
    def timestamp(self, timestamp):
        """Sets the timestamp of this WhiteBlackIpResponseBody.

        创建规则的时间戳

        :param timestamp: The timestamp of this WhiteBlackIpResponseBody.
        :type: int
        """
        self._timestamp = timestamp

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
        if not isinstance(other, WhiteBlackIpResponseBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

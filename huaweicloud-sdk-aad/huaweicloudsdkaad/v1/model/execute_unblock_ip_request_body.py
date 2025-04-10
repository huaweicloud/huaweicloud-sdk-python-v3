# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ExecuteUnblockIpRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'ip': 'str',
        'blocking_time': 'int'
    }

    attribute_map = {
        'ip': 'ip',
        'blocking_time': 'blocking_time'
    }

    def __init__(self, ip=None, blocking_time=None):
        r"""ExecuteUnblockIpRequestBody

        The model defined in huaweicloud sdk

        :param ip: ip地址
        :type ip: str
        :param blocking_time: 用于查询IP的封堵时间
        :type blocking_time: int
        """
        
        

        self._ip = None
        self._blocking_time = None
        self.discriminator = None

        self.ip = ip
        if blocking_time is not None:
            self.blocking_time = blocking_time

    @property
    def ip(self):
        r"""Gets the ip of this ExecuteUnblockIpRequestBody.

        ip地址

        :return: The ip of this ExecuteUnblockIpRequestBody.
        :rtype: str
        """
        return self._ip

    @ip.setter
    def ip(self, ip):
        r"""Sets the ip of this ExecuteUnblockIpRequestBody.

        ip地址

        :param ip: The ip of this ExecuteUnblockIpRequestBody.
        :type ip: str
        """
        self._ip = ip

    @property
    def blocking_time(self):
        r"""Gets the blocking_time of this ExecuteUnblockIpRequestBody.

        用于查询IP的封堵时间

        :return: The blocking_time of this ExecuteUnblockIpRequestBody.
        :rtype: int
        """
        return self._blocking_time

    @blocking_time.setter
    def blocking_time(self, blocking_time):
        r"""Sets the blocking_time of this ExecuteUnblockIpRequestBody.

        用于查询IP的封堵时间

        :param blocking_time: The blocking_time of this ExecuteUnblockIpRequestBody.
        :type blocking_time: int
        """
        self._blocking_time = blocking_time

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
        if not isinstance(other, ExecuteUnblockIpRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

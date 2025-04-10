# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class KafkaBrokerInfo:

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
        'port': 'int'
    }

    attribute_map = {
        'ip': 'ip',
        'port': 'port'
    }

    def __init__(self, ip=None, port=None):
        r"""KafkaBrokerInfo

        The model defined in huaweicloud sdk

        :param ip: IP
        :type ip: str
        :param port: Port
        :type port: int
        """
        
        

        self._ip = None
        self._port = None
        self.discriminator = None

        self.ip = ip
        self.port = port

    @property
    def ip(self):
        r"""Gets the ip of this KafkaBrokerInfo.

        IP

        :return: The ip of this KafkaBrokerInfo.
        :rtype: str
        """
        return self._ip

    @ip.setter
    def ip(self, ip):
        r"""Sets the ip of this KafkaBrokerInfo.

        IP

        :param ip: The ip of this KafkaBrokerInfo.
        :type ip: str
        """
        self._ip = ip

    @property
    def port(self):
        r"""Gets the port of this KafkaBrokerInfo.

        Port

        :return: The port of this KafkaBrokerInfo.
        :rtype: int
        """
        return self._port

    @port.setter
    def port(self, port):
        r"""Sets the port of this KafkaBrokerInfo.

        Port

        :param port: The port of this KafkaBrokerInfo.
        :type port: int
        """
        self._port = port

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
        if not isinstance(other, KafkaBrokerInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

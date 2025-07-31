# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ContainerExtraOpenvpnInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'outside_ip': 'str',
        'outside_port': 'str'
    }

    attribute_map = {
        'outside_ip': 'outside_ip',
        'outside_port': 'outside_port'
    }

    def __init__(self, outside_ip=None, outside_port=None):
        r"""ContainerExtraOpenvpnInfo

        The model defined in huaweicloud sdk

        :param outside_ip: 映射ip
        :type outside_ip: str
        :param outside_port: 映射端口
        :type outside_port: str
        """
        
        

        self._outside_ip = None
        self._outside_port = None
        self.discriminator = None

        if outside_ip is not None:
            self.outside_ip = outside_ip
        if outside_port is not None:
            self.outside_port = outside_port

    @property
    def outside_ip(self):
        r"""Gets the outside_ip of this ContainerExtraOpenvpnInfo.

        映射ip

        :return: The outside_ip of this ContainerExtraOpenvpnInfo.
        :rtype: str
        """
        return self._outside_ip

    @outside_ip.setter
    def outside_ip(self, outside_ip):
        r"""Sets the outside_ip of this ContainerExtraOpenvpnInfo.

        映射ip

        :param outside_ip: The outside_ip of this ContainerExtraOpenvpnInfo.
        :type outside_ip: str
        """
        self._outside_ip = outside_ip

    @property
    def outside_port(self):
        r"""Gets the outside_port of this ContainerExtraOpenvpnInfo.

        映射端口

        :return: The outside_port of this ContainerExtraOpenvpnInfo.
        :rtype: str
        """
        return self._outside_port

    @outside_port.setter
    def outside_port(self, outside_port):
        r"""Sets the outside_port of this ContainerExtraOpenvpnInfo.

        映射端口

        :param outside_port: The outside_port of this ContainerExtraOpenvpnInfo.
        :type outside_port: str
        """
        self._outside_port = outside_port

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
        if not isinstance(other, ContainerExtraOpenvpnInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

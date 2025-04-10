# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class MsdtcHostOption:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'host_name': 'str',
        'ip': 'str'
    }

    attribute_map = {
        'host_name': 'host_name',
        'ip': 'ip'
    }

    def __init__(self, host_name=None, ip=None):
        r"""MsdtcHostOption

        The model defined in huaweicloud sdk

        :param host_name: 主机名称 hostname
        :type host_name: str
        :param ip: 主机ip
        :type ip: str
        """
        
        

        self._host_name = None
        self._ip = None
        self.discriminator = None

        self.host_name = host_name
        self.ip = ip

    @property
    def host_name(self):
        r"""Gets the host_name of this MsdtcHostOption.

        主机名称 hostname

        :return: The host_name of this MsdtcHostOption.
        :rtype: str
        """
        return self._host_name

    @host_name.setter
    def host_name(self, host_name):
        r"""Sets the host_name of this MsdtcHostOption.

        主机名称 hostname

        :param host_name: The host_name of this MsdtcHostOption.
        :type host_name: str
        """
        self._host_name = host_name

    @property
    def ip(self):
        r"""Gets the ip of this MsdtcHostOption.

        主机ip

        :return: The ip of this MsdtcHostOption.
        :rtype: str
        """
        return self._ip

    @ip.setter
    def ip(self, ip):
        r"""Sets the ip of this MsdtcHostOption.

        主机ip

        :param ip: The ip of this MsdtcHostOption.
        :type ip: str
        """
        self._ip = ip

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
        if not isinstance(other, MsdtcHostOption):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

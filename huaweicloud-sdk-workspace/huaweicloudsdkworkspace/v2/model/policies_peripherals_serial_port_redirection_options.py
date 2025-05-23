# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PoliciesPeripheralsSerialPortRedirectionOptions:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'auto_connect_enable': 'bool'
    }

    attribute_map = {
        'auto_connect_enable': 'auto_connect_enable'
    }

    def __init__(self, auto_connect_enable=None):
        r"""PoliciesPeripheralsSerialPortRedirectionOptions

        The model defined in huaweicloud sdk

        :param auto_connect_enable: 是否自动连接客户端串口。取值为： false：表示关闭。 true：表示开启。
        :type auto_connect_enable: bool
        """
        
        

        self._auto_connect_enable = None
        self.discriminator = None

        if auto_connect_enable is not None:
            self.auto_connect_enable = auto_connect_enable

    @property
    def auto_connect_enable(self):
        r"""Gets the auto_connect_enable of this PoliciesPeripheralsSerialPortRedirectionOptions.

        是否自动连接客户端串口。取值为： false：表示关闭。 true：表示开启。

        :return: The auto_connect_enable of this PoliciesPeripheralsSerialPortRedirectionOptions.
        :rtype: bool
        """
        return self._auto_connect_enable

    @auto_connect_enable.setter
    def auto_connect_enable(self, auto_connect_enable):
        r"""Sets the auto_connect_enable of this PoliciesPeripheralsSerialPortRedirectionOptions.

        是否自动连接客户端串口。取值为： false：表示关闭。 true：表示开启。

        :param auto_connect_enable: The auto_connect_enable of this PoliciesPeripheralsSerialPortRedirectionOptions.
        :type auto_connect_enable: bool
        """
        self._auto_connect_enable = auto_connect_enable

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
        if not isinstance(other, PoliciesPeripheralsSerialPortRedirectionOptions):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

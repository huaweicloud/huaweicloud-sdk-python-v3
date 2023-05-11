# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ResetDeviceSecret:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []
    sensitive_list.append('secret')

    openapi_types = {
        'secret': 'str',
        'force_disconnect': 'bool'
    }

    attribute_map = {
        'secret': 'secret',
        'force_disconnect': 'force_disconnect'
    }

    def __init__(self, secret=None, force_disconnect=None):
        """ResetDeviceSecret

        The model defined in huaweicloud sdk

        :param secret: **参数说明**：设备密钥，设置该字段时平台将设备密钥重置为指定值，若不设置则由平台自动生成。 **取值范围**：长度不低于8不超过32，只允许字母、数字、下划线（_）、连接符（-）的组合。
        :type secret: str
        :param force_disconnect: **参数说明**：是否强制断开设备的连接，当前仅限长连接。默认值false。
        :type force_disconnect: bool
        """
        
        

        self._secret = None
        self._force_disconnect = None
        self.discriminator = None

        if secret is not None:
            self.secret = secret
        if force_disconnect is not None:
            self.force_disconnect = force_disconnect

    @property
    def secret(self):
        """Gets the secret of this ResetDeviceSecret.

        **参数说明**：设备密钥，设置该字段时平台将设备密钥重置为指定值，若不设置则由平台自动生成。 **取值范围**：长度不低于8不超过32，只允许字母、数字、下划线（_）、连接符（-）的组合。

        :return: The secret of this ResetDeviceSecret.
        :rtype: str
        """
        return self._secret

    @secret.setter
    def secret(self, secret):
        """Sets the secret of this ResetDeviceSecret.

        **参数说明**：设备密钥，设置该字段时平台将设备密钥重置为指定值，若不设置则由平台自动生成。 **取值范围**：长度不低于8不超过32，只允许字母、数字、下划线（_）、连接符（-）的组合。

        :param secret: The secret of this ResetDeviceSecret.
        :type secret: str
        """
        self._secret = secret

    @property
    def force_disconnect(self):
        """Gets the force_disconnect of this ResetDeviceSecret.

        **参数说明**：是否强制断开设备的连接，当前仅限长连接。默认值false。

        :return: The force_disconnect of this ResetDeviceSecret.
        :rtype: bool
        """
        return self._force_disconnect

    @force_disconnect.setter
    def force_disconnect(self, force_disconnect):
        """Sets the force_disconnect of this ResetDeviceSecret.

        **参数说明**：是否强制断开设备的连接，当前仅限长连接。默认值false。

        :param force_disconnect: The force_disconnect of this ResetDeviceSecret.
        :type force_disconnect: bool
        """
        self._force_disconnect = force_disconnect

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
        if not isinstance(other, ResetDeviceSecret):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

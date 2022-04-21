# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ResetFingerprint:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []
    sensitive_list.append('fingerprint')

    openapi_types = {
        'fingerprint': 'str',
        'force_disconnect': 'bool'
    }

    attribute_map = {
        'fingerprint': 'fingerprint',
        'force_disconnect': 'force_disconnect'
    }

    def __init__(self, fingerprint=None, force_disconnect=None):
        """ResetFingerprint

        The model defined in huaweicloud sdk

        :param fingerprint: **参数说明**：设备指纹。设置改字段时平台将设备指纹重置为指定值；不携带时将之置空，后续设备第一次接入时，该设备指纹的值将设置为第一次接入时的证书指纹。 **取值范围**：长度为40的十六进制字符串或者长度为64的十六进制字符串。
        :type fingerprint: str
        :param force_disconnect: **参数说明**：是否强制断开设备的连接，当前仅限长连接。默认值false。
        :type force_disconnect: bool
        """
        
        

        self._fingerprint = None
        self._force_disconnect = None
        self.discriminator = None

        if fingerprint is not None:
            self.fingerprint = fingerprint
        if force_disconnect is not None:
            self.force_disconnect = force_disconnect

    @property
    def fingerprint(self):
        """Gets the fingerprint of this ResetFingerprint.

        **参数说明**：设备指纹。设置改字段时平台将设备指纹重置为指定值；不携带时将之置空，后续设备第一次接入时，该设备指纹的值将设置为第一次接入时的证书指纹。 **取值范围**：长度为40的十六进制字符串或者长度为64的十六进制字符串。

        :return: The fingerprint of this ResetFingerprint.
        :rtype: str
        """
        return self._fingerprint

    @fingerprint.setter
    def fingerprint(self, fingerprint):
        """Sets the fingerprint of this ResetFingerprint.

        **参数说明**：设备指纹。设置改字段时平台将设备指纹重置为指定值；不携带时将之置空，后续设备第一次接入时，该设备指纹的值将设置为第一次接入时的证书指纹。 **取值范围**：长度为40的十六进制字符串或者长度为64的十六进制字符串。

        :param fingerprint: The fingerprint of this ResetFingerprint.
        :type fingerprint: str
        """
        self._fingerprint = fingerprint

    @property
    def force_disconnect(self):
        """Gets the force_disconnect of this ResetFingerprint.

        **参数说明**：是否强制断开设备的连接，当前仅限长连接。默认值false。

        :return: The force_disconnect of this ResetFingerprint.
        :rtype: bool
        """
        return self._force_disconnect

    @force_disconnect.setter
    def force_disconnect(self, force_disconnect):
        """Sets the force_disconnect of this ResetFingerprint.

        **参数说明**：是否强制断开设备的连接，当前仅限长连接。默认值false。

        :param force_disconnect: The force_disconnect of this ResetFingerprint.
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
        if not isinstance(other, ResetFingerprint):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

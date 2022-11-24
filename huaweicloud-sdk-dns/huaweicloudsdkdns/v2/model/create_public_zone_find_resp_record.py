# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreatePublicZoneFindRespRecord:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'host': 'str',
        'value': 'str'
    }

    attribute_map = {
        'host': 'host',
        'value': 'value'
    }

    def __init__(self, host=None, value=None):
        """CreatePublicZoneFindRespRecord

        The model defined in huaweicloud sdk

        :param host: 找回记录host名称。
        :type host: str
        :param value: 找回记录解析值。
        :type value: str
        """
        
        

        self._host = None
        self._value = None
        self.discriminator = None

        if host is not None:
            self.host = host
        if value is not None:
            self.value = value

    @property
    def host(self):
        """Gets the host of this CreatePublicZoneFindRespRecord.

        找回记录host名称。

        :return: The host of this CreatePublicZoneFindRespRecord.
        :rtype: str
        """
        return self._host

    @host.setter
    def host(self, host):
        """Sets the host of this CreatePublicZoneFindRespRecord.

        找回记录host名称。

        :param host: The host of this CreatePublicZoneFindRespRecord.
        :type host: str
        """
        self._host = host

    @property
    def value(self):
        """Gets the value of this CreatePublicZoneFindRespRecord.

        找回记录解析值。

        :return: The value of this CreatePublicZoneFindRespRecord.
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this CreatePublicZoneFindRespRecord.

        找回记录解析值。

        :param value: The value of this CreatePublicZoneFindRespRecord.
        :type value: str
        """
        self._value = value

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
        if not isinstance(other, CreatePublicZoneFindRespRecord):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

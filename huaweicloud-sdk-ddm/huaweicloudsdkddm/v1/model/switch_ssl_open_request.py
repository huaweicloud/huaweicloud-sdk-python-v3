# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SwitchSslOpenRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'ssl_enabled': 'bool'
    }

    attribute_map = {
        'ssl_enabled': 'ssl_enabled'
    }

    def __init__(self, ssl_enabled=None):
        r"""SwitchSslOpenRequest

        The model defined in huaweicloud sdk

        :param ssl_enabled: true:  打开 false: 关闭
        :type ssl_enabled: bool
        """
        
        

        self._ssl_enabled = None
        self.discriminator = None

        self.ssl_enabled = ssl_enabled

    @property
    def ssl_enabled(self):
        r"""Gets the ssl_enabled of this SwitchSslOpenRequest.

        true:  打开 false: 关闭

        :return: The ssl_enabled of this SwitchSslOpenRequest.
        :rtype: bool
        """
        return self._ssl_enabled

    @ssl_enabled.setter
    def ssl_enabled(self, ssl_enabled):
        r"""Sets the ssl_enabled of this SwitchSslOpenRequest.

        true:  打开 false: 关闭

        :param ssl_enabled: The ssl_enabled of this SwitchSslOpenRequest.
        :type ssl_enabled: bool
        """
        self._ssl_enabled = ssl_enabled

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
        if not isinstance(other, SwitchSslOpenRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

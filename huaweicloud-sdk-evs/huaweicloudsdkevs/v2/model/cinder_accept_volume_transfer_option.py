# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CinderAcceptVolumeTransferOption:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'auth_key': 'str'
    }

    attribute_map = {
        'auth_key': 'auth_key'
    }

    def __init__(self, auth_key=None):
        """CinderAcceptVolumeTransferOption

        The model defined in huaweicloud sdk

        :param auth_key: 云硬盘过户的身份认证密钥。  创建云硬盘过户时会返回该身份认证密钥。
        :type auth_key: str
        """
        
        

        self._auth_key = None
        self.discriminator = None

        self.auth_key = auth_key

    @property
    def auth_key(self):
        """Gets the auth_key of this CinderAcceptVolumeTransferOption.

        云硬盘过户的身份认证密钥。  创建云硬盘过户时会返回该身份认证密钥。

        :return: The auth_key of this CinderAcceptVolumeTransferOption.
        :rtype: str
        """
        return self._auth_key

    @auth_key.setter
    def auth_key(self, auth_key):
        """Sets the auth_key of this CinderAcceptVolumeTransferOption.

        云硬盘过户的身份认证密钥。  创建云硬盘过户时会返回该身份认证密钥。

        :param auth_key: The auth_key of this CinderAcceptVolumeTransferOption.
        :type auth_key: str
        """
        self._auth_key = auth_key

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
        if not isinstance(other, CinderAcceptVolumeTransferOption):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

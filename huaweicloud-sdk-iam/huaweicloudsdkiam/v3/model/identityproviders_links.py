# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class IdentityprovidersLinks:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        '_self': 'str',
        'protocols': 'str'
    }

    attribute_map = {
        '_self': 'self',
        'protocols': 'protocols'
    }

    def __init__(self, _self=None, protocols=None):
        """IdentityprovidersLinks

        The model defined in huaweicloud sdk

        :param _self: 身份提供商的资源链接地址。
        :type _self: str
        :param protocols: 协议的资源链接地址。
        :type protocols: str
        """
        
        

        self.__self = None
        self._protocols = None
        self.discriminator = None

        self._self = _self
        self.protocols = protocols

    @property
    def _self(self):
        """Gets the _self of this IdentityprovidersLinks.

        身份提供商的资源链接地址。

        :return: The _self of this IdentityprovidersLinks.
        :rtype: str
        """
        return self.__self

    @_self.setter
    def _self(self, _self):
        """Sets the _self of this IdentityprovidersLinks.

        身份提供商的资源链接地址。

        :param _self: The _self of this IdentityprovidersLinks.
        :type _self: str
        """
        self.__self = _self

    @property
    def protocols(self):
        """Gets the protocols of this IdentityprovidersLinks.

        协议的资源链接地址。

        :return: The protocols of this IdentityprovidersLinks.
        :rtype: str
        """
        return self._protocols

    @protocols.setter
    def protocols(self, protocols):
        """Sets the protocols of this IdentityprovidersLinks.

        协议的资源链接地址。

        :param protocols: The protocols of this IdentityprovidersLinks.
        :type protocols: str
        """
        self._protocols = protocols

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
        if not isinstance(other, IdentityprovidersLinks):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

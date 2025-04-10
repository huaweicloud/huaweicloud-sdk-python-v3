# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PrivateHookDefaultVersionPrimitiveTypeHolder:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'default_version': 'str'
    }

    attribute_map = {
        'default_version': 'default_version'
    }

    def __init__(self, default_version=None):
        r"""PrivateHookDefaultVersionPrimitiveTypeHolder

        The model defined in huaweicloud sdk

        :param default_version: 私有hook的默认版本号。版本号必须遵循语义化版本号（Semantic Version），为用户自定义。
        :type default_version: str
        """
        
        

        self._default_version = None
        self.discriminator = None

        if default_version is not None:
            self.default_version = default_version

    @property
    def default_version(self):
        r"""Gets the default_version of this PrivateHookDefaultVersionPrimitiveTypeHolder.

        私有hook的默认版本号。版本号必须遵循语义化版本号（Semantic Version），为用户自定义。

        :return: The default_version of this PrivateHookDefaultVersionPrimitiveTypeHolder.
        :rtype: str
        """
        return self._default_version

    @default_version.setter
    def default_version(self, default_version):
        r"""Sets the default_version of this PrivateHookDefaultVersionPrimitiveTypeHolder.

        私有hook的默认版本号。版本号必须遵循语义化版本号（Semantic Version），为用户自定义。

        :param default_version: The default_version of this PrivateHookDefaultVersionPrimitiveTypeHolder.
        :type default_version: str
        """
        self._default_version = default_version

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
        if not isinstance(other, PrivateHookDefaultVersionPrimitiveTypeHolder):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

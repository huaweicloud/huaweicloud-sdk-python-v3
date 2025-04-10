# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PrivateHookVersionPrimitiveTypeHolder:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'hook_version': 'str'
    }

    attribute_map = {
        'hook_version': 'hook_version'
    }

    def __init__(self, hook_version=None):
        r"""PrivateHookVersionPrimitiveTypeHolder

        The model defined in huaweicloud sdk

        :param hook_version: 私有hook的版本号。版本号必须遵循语义化版本号（Semantic Version），为用户自定义。
        :type hook_version: str
        """
        
        

        self._hook_version = None
        self.discriminator = None

        self.hook_version = hook_version

    @property
    def hook_version(self):
        r"""Gets the hook_version of this PrivateHookVersionPrimitiveTypeHolder.

        私有hook的版本号。版本号必须遵循语义化版本号（Semantic Version），为用户自定义。

        :return: The hook_version of this PrivateHookVersionPrimitiveTypeHolder.
        :rtype: str
        """
        return self._hook_version

    @hook_version.setter
    def hook_version(self, hook_version):
        r"""Sets the hook_version of this PrivateHookVersionPrimitiveTypeHolder.

        私有hook的版本号。版本号必须遵循语义化版本号（Semantic Version），为用户自定义。

        :param hook_version: The hook_version of this PrivateHookVersionPrimitiveTypeHolder.
        :type hook_version: str
        """
        self._hook_version = hook_version

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
        if not isinstance(other, PrivateHookVersionPrimitiveTypeHolder):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

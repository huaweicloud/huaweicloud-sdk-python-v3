# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PrivateHookDescriptionPrimitiveTypeHolder:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'hook_description': 'str'
    }

    attribute_map = {
        'hook_description': 'hook_description'
    }

    def __init__(self, hook_description=None):
        r"""PrivateHookDescriptionPrimitiveTypeHolder

        The model defined in huaweicloud sdk

        :param hook_description: 私有hook的描述。可用于客户识别创建的私有hook。可通过UpdatePrivateHook API更新私有hook的描述。
        :type hook_description: str
        """
        
        

        self._hook_description = None
        self.discriminator = None

        if hook_description is not None:
            self.hook_description = hook_description

    @property
    def hook_description(self):
        r"""Gets the hook_description of this PrivateHookDescriptionPrimitiveTypeHolder.

        私有hook的描述。可用于客户识别创建的私有hook。可通过UpdatePrivateHook API更新私有hook的描述。

        :return: The hook_description of this PrivateHookDescriptionPrimitiveTypeHolder.
        :rtype: str
        """
        return self._hook_description

    @hook_description.setter
    def hook_description(self, hook_description):
        r"""Sets the hook_description of this PrivateHookDescriptionPrimitiveTypeHolder.

        私有hook的描述。可用于客户识别创建的私有hook。可通过UpdatePrivateHook API更新私有hook的描述。

        :param hook_description: The hook_description of this PrivateHookDescriptionPrimitiveTypeHolder.
        :type hook_description: str
        """
        self._hook_description = hook_description

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
        if not isinstance(other, PrivateHookDescriptionPrimitiveTypeHolder):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

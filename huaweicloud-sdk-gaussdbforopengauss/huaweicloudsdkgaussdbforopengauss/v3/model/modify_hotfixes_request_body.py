# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ModifyHotfixesRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'hotfixes': 'object'
    }

    attribute_map = {
        'hotfixes': 'hotfixes'
    }

    def __init__(self, hotfixes=None):
        r"""ModifyHotfixesRequestBody

        The model defined in huaweicloud sdk

        :param hotfixes: **参数解释**: 热补丁属性信息。 **约束限制**: 不涉及。
        :type hotfixes: object
        """
        
        

        self._hotfixes = None
        self.discriminator = None

        self.hotfixes = hotfixes

    @property
    def hotfixes(self):
        r"""Gets the hotfixes of this ModifyHotfixesRequestBody.

        **参数解释**: 热补丁属性信息。 **约束限制**: 不涉及。

        :return: The hotfixes of this ModifyHotfixesRequestBody.
        :rtype: object
        """
        return self._hotfixes

    @hotfixes.setter
    def hotfixes(self, hotfixes):
        r"""Sets the hotfixes of this ModifyHotfixesRequestBody.

        **参数解释**: 热补丁属性信息。 **约束限制**: 不涉及。

        :param hotfixes: The hotfixes of this ModifyHotfixesRequestBody.
        :type hotfixes: object
        """
        self._hotfixes = hotfixes

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
        if not isinstance(other, ModifyHotfixesRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

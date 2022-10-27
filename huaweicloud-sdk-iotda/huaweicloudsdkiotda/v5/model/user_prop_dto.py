# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UserPropDTO:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'prop_key': 'str',
        'prop_value': 'str'
    }

    attribute_map = {
        'prop_key': 'prop_key',
        'prop_value': 'prop_value'
    }

    def __init__(self, prop_key=None, prop_value=None):
        """UserPropDTO

        The model defined in huaweicloud sdk

        :param prop_key: **参数说明**：用户自定义属性键。 **取值范围**：长度不超过128，只允许字母、数字、下划线（_）、连接符（-）的组合。
        :type prop_key: str
        :param prop_value: **参数说明**：用户自定义属性值。 **取值范围**：长度不超过128，只允许中文、字母、数字、以及_? &#39;#().,&amp;%@!-等字符的组合。
        :type prop_value: str
        """
        
        

        self._prop_key = None
        self._prop_value = None
        self.discriminator = None

        if prop_key is not None:
            self.prop_key = prop_key
        if prop_value is not None:
            self.prop_value = prop_value

    @property
    def prop_key(self):
        """Gets the prop_key of this UserPropDTO.

        **参数说明**：用户自定义属性键。 **取值范围**：长度不超过128，只允许字母、数字、下划线（_）、连接符（-）的组合。

        :return: The prop_key of this UserPropDTO.
        :rtype: str
        """
        return self._prop_key

    @prop_key.setter
    def prop_key(self, prop_key):
        """Sets the prop_key of this UserPropDTO.

        **参数说明**：用户自定义属性键。 **取值范围**：长度不超过128，只允许字母、数字、下划线（_）、连接符（-）的组合。

        :param prop_key: The prop_key of this UserPropDTO.
        :type prop_key: str
        """
        self._prop_key = prop_key

    @property
    def prop_value(self):
        """Gets the prop_value of this UserPropDTO.

        **参数说明**：用户自定义属性值。 **取值范围**：长度不超过128，只允许中文、字母、数字、以及_? '#().,&%@!-等字符的组合。

        :return: The prop_value of this UserPropDTO.
        :rtype: str
        """
        return self._prop_value

    @prop_value.setter
    def prop_value(self, prop_value):
        """Sets the prop_value of this UserPropDTO.

        **参数说明**：用户自定义属性值。 **取值范围**：长度不超过128，只允许中文、字母、数字、以及_? '#().,&%@!-等字符的组合。

        :param prop_value: The prop_value of this UserPropDTO.
        :type prop_value: str
        """
        self._prop_value = prop_value

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
        if not isinstance(other, UserPropDTO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

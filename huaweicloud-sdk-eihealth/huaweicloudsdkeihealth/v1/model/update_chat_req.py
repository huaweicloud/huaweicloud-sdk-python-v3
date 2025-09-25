# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateChatReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'alias': 'str',
        'enable_top': 'bool'
    }

    attribute_map = {
        'alias': 'alias',
        'enable_top': 'enable_top'
    }

    def __init__(self, alias=None, enable_top=None):
        r"""UpdateChatReq

        The model defined in huaweicloud sdk

        :param alias: **参数解释**： 对话别名。 **约束限制**： 不涉及 **取值范围**： 取值范围为[1-20]个字符。 **默认取值**： 不涉及 
        :type alias: str
        :param enable_top: **参数解释**： 是否置顶对话。 **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及 
        :type enable_top: bool
        """
        
        

        self._alias = None
        self._enable_top = None
        self.discriminator = None

        self.alias = alias
        self.enable_top = enable_top

    @property
    def alias(self):
        r"""Gets the alias of this UpdateChatReq.

        **参数解释**： 对话别名。 **约束限制**： 不涉及 **取值范围**： 取值范围为[1-20]个字符。 **默认取值**： 不涉及 

        :return: The alias of this UpdateChatReq.
        :rtype: str
        """
        return self._alias

    @alias.setter
    def alias(self, alias):
        r"""Sets the alias of this UpdateChatReq.

        **参数解释**： 对话别名。 **约束限制**： 不涉及 **取值范围**： 取值范围为[1-20]个字符。 **默认取值**： 不涉及 

        :param alias: The alias of this UpdateChatReq.
        :type alias: str
        """
        self._alias = alias

    @property
    def enable_top(self):
        r"""Gets the enable_top of this UpdateChatReq.

        **参数解释**： 是否置顶对话。 **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及 

        :return: The enable_top of this UpdateChatReq.
        :rtype: bool
        """
        return self._enable_top

    @enable_top.setter
    def enable_top(self, enable_top):
        r"""Sets the enable_top of this UpdateChatReq.

        **参数解释**： 是否置顶对话。 **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及 

        :param enable_top: The enable_top of this UpdateChatReq.
        :type enable_top: bool
        """
        self._enable_top = enable_top

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
        if not isinstance(other, UpdateChatReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

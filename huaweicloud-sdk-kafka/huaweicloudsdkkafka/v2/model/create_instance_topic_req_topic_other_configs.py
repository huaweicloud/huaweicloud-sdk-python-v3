# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateInstanceTopicReqTopicOtherConfigs:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'name': 'str',
        'value': 'str'
    }

    attribute_map = {
        'name': 'name',
        'value': 'value'
    }

    def __init__(self, name=None, value=None):
        r"""CreateInstanceTopicReqTopicOtherConfigs

        The model defined in huaweicloud sdk

        :param name: **参数解释**： 配置名称。 **约束限制**： 不涉及。 **取值范围**： 不涉及 **默认取值**： 不涉及。 
        :type name: str
        :param value: **参数解释**： 配置值。 **约束限制**： 不涉及。 **取值范围**： 不涉及 **默认取值**： 不涉及。  
        :type value: str
        """
        
        

        self._name = None
        self._value = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if value is not None:
            self.value = value

    @property
    def name(self):
        r"""Gets the name of this CreateInstanceTopicReqTopicOtherConfigs.

        **参数解释**： 配置名称。 **约束限制**： 不涉及。 **取值范围**： 不涉及 **默认取值**： 不涉及。 

        :return: The name of this CreateInstanceTopicReqTopicOtherConfigs.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this CreateInstanceTopicReqTopicOtherConfigs.

        **参数解释**： 配置名称。 **约束限制**： 不涉及。 **取值范围**： 不涉及 **默认取值**： 不涉及。 

        :param name: The name of this CreateInstanceTopicReqTopicOtherConfigs.
        :type name: str
        """
        self._name = name

    @property
    def value(self):
        r"""Gets the value of this CreateInstanceTopicReqTopicOtherConfigs.

        **参数解释**： 配置值。 **约束限制**： 不涉及。 **取值范围**： 不涉及 **默认取值**： 不涉及。  

        :return: The value of this CreateInstanceTopicReqTopicOtherConfigs.
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        r"""Sets the value of this CreateInstanceTopicReqTopicOtherConfigs.

        **参数解释**： 配置值。 **约束限制**： 不涉及。 **取值范围**： 不涉及 **默认取值**： 不涉及。  

        :param value: The value of this CreateInstanceTopicReqTopicOtherConfigs.
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
        if not isinstance(other, CreateInstanceTopicReqTopicOtherConfigs):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

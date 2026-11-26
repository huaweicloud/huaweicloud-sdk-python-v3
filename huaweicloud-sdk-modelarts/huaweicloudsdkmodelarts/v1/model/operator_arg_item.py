# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class OperatorArgItem:

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
        'value': 'str',
        'tips': 'str'
    }

    attribute_map = {
        'name': 'name',
        'value': 'value',
        'tips': 'tips'
    }

    def __init__(self, name=None, value=None, tips=None):
        r"""OperatorArgItem

        The model defined in huaweicloud sdk

        :param name: **参数解释**：参数名。
        :type name: str
        :param value: **参数解释**：参数值
        :type value: str
        :param tips: **参数解释**：参数说明
        :type tips: str
        """
        
        

        self._name = None
        self._value = None
        self._tips = None
        self.discriminator = None

        self.name = name
        self.value = value
        if tips is not None:
            self.tips = tips

    @property
    def name(self):
        r"""Gets the name of this OperatorArgItem.

        **参数解释**：参数名。

        :return: The name of this OperatorArgItem.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this OperatorArgItem.

        **参数解释**：参数名。

        :param name: The name of this OperatorArgItem.
        :type name: str
        """
        self._name = name

    @property
    def value(self):
        r"""Gets the value of this OperatorArgItem.

        **参数解释**：参数值

        :return: The value of this OperatorArgItem.
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        r"""Sets the value of this OperatorArgItem.

        **参数解释**：参数值

        :param value: The value of this OperatorArgItem.
        :type value: str
        """
        self._value = value

    @property
    def tips(self):
        r"""Gets the tips of this OperatorArgItem.

        **参数解释**：参数说明

        :return: The tips of this OperatorArgItem.
        :rtype: str
        """
        return self._tips

    @tips.setter
    def tips(self, tips):
        r"""Sets the tips of this OperatorArgItem.

        **参数解释**：参数说明

        :param tips: The tips of this OperatorArgItem.
        :type tips: str
        """
        self._tips = tips

    def to_dict(self):
        result = {}

        for attr, _ in self.openapi_types.items():
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
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, OperatorArgItem):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

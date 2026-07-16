# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Data:

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
        'type': 'str',
        'value': 'dict(str, object)',
        'used_steps': 'list[str]'
    }

    attribute_map = {
        'name': 'name',
        'type': 'type',
        'value': 'value',
        'used_steps': 'used_steps'
    }

    def __init__(self, name=None, type=None, value=None, used_steps=None):
        r"""Data

        The model defined in huaweicloud sdk

        :param name: 训练数据的名称。填写1-64位，仅包含英文、数字、下划线（_）和中划线（-），并且以英文开头的名称。
        :type name: str
        :param type: 数据来源的类型，可选值为dataset、obs、swr、model、label_task、service、image。
        :type type: str
        :param value: 数据的值。
        :type value: dict(str, object)
        :param used_steps: 使用数据的节点。
        :type used_steps: list[str]
        """
        
        

        self._name = None
        self._type = None
        self._value = None
        self._used_steps = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if type is not None:
            self.type = type
        if value is not None:
            self.value = value
        if used_steps is not None:
            self.used_steps = used_steps

    @property
    def name(self):
        r"""Gets the name of this Data.

        训练数据的名称。填写1-64位，仅包含英文、数字、下划线（_）和中划线（-），并且以英文开头的名称。

        :return: The name of this Data.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this Data.

        训练数据的名称。填写1-64位，仅包含英文、数字、下划线（_）和中划线（-），并且以英文开头的名称。

        :param name: The name of this Data.
        :type name: str
        """
        self._name = name

    @property
    def type(self):
        r"""Gets the type of this Data.

        数据来源的类型，可选值为dataset、obs、swr、model、label_task、service、image。

        :return: The type of this Data.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this Data.

        数据来源的类型，可选值为dataset、obs、swr、model、label_task、service、image。

        :param type: The type of this Data.
        :type type: str
        """
        self._type = type

    @property
    def value(self):
        r"""Gets the value of this Data.

        数据的值。

        :return: The value of this Data.
        :rtype: dict(str, object)
        """
        return self._value

    @value.setter
    def value(self, value):
        r"""Sets the value of this Data.

        数据的值。

        :param value: The value of this Data.
        :type value: dict(str, object)
        """
        self._value = value

    @property
    def used_steps(self):
        r"""Gets the used_steps of this Data.

        使用数据的节点。

        :return: The used_steps of this Data.
        :rtype: list[str]
        """
        return self._used_steps

    @used_steps.setter
    def used_steps(self, used_steps):
        r"""Sets the used_steps of this Data.

        使用数据的节点。

        :param used_steps: The used_steps of this Data.
        :type used_steps: list[str]
        """
        self._used_steps = used_steps

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
        if not isinstance(other, Data):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

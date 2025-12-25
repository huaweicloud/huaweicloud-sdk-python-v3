# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Restriction:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'logic': 'bool',
        'title': 'str',
        'type': 'str',
        'value': 'str'
    }

    attribute_map = {
        'logic': 'logic',
        'title': 'title',
        'type': 'type',
        'value': 'value'
    }

    def __init__(self, logic=None, title=None, type=None, value=None):
        r"""Restriction

        The model defined in huaweicloud sdk

        :param logic: 逻辑条件
        :type logic: bool
        :param title: 相关标题
        :type title: str
        :param type: 规则类型
        :type type: str
        :param value: 规则名称
        :type value: str
        """
        
        

        self._logic = None
        self._title = None
        self._type = None
        self._value = None
        self.discriminator = None

        if logic is not None:
            self.logic = logic
        if title is not None:
            self.title = title
        if type is not None:
            self.type = type
        if value is not None:
            self.value = value

    @property
    def logic(self):
        r"""Gets the logic of this Restriction.

        逻辑条件

        :return: The logic of this Restriction.
        :rtype: bool
        """
        return self._logic

    @logic.setter
    def logic(self, logic):
        r"""Sets the logic of this Restriction.

        逻辑条件

        :param logic: The logic of this Restriction.
        :type logic: bool
        """
        self._logic = logic

    @property
    def title(self):
        r"""Gets the title of this Restriction.

        相关标题

        :return: The title of this Restriction.
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        r"""Sets the title of this Restriction.

        相关标题

        :param title: The title of this Restriction.
        :type title: str
        """
        self._title = title

    @property
    def type(self):
        r"""Gets the type of this Restriction.

        规则类型

        :return: The type of this Restriction.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this Restriction.

        规则类型

        :param type: The type of this Restriction.
        :type type: str
        """
        self._type = type

    @property
    def value(self):
        r"""Gets the value of this Restriction.

        规则名称

        :return: The value of this Restriction.
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        r"""Sets the value of this Restriction.

        规则名称

        :param value: The value of this Restriction.
        :type value: str
        """
        self._value = value

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
        if not isinstance(other, Restriction):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

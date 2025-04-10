# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DeployStrategyGrayReleaseRules:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'type': 'str',
        'key': 'str',
        'value': 'str',
        'condition': 'str'
    }

    attribute_map = {
        'type': 'type',
        'key': 'key',
        'value': 'value',
        'condition': 'condition'
    }

    def __init__(self, type=None, key=None, value=None, condition=None):
        r"""DeployStrategyGrayReleaseRules

        The model defined in huaweicloud sdk

        :param type: 匹配类型
        :type type: str
        :param key: 参数名称
        :type key: str
        :param value: 条件值
        :type value: str
        :param condition: equal相等，match匹配，in枚举
        :type condition: str
        """
        
        

        self._type = None
        self._key = None
        self._value = None
        self._condition = None
        self.discriminator = None

        self.type = type
        self.key = key
        self.value = value
        self.condition = condition

    @property
    def type(self):
        r"""Gets the type of this DeployStrategyGrayReleaseRules.

        匹配类型

        :return: The type of this DeployStrategyGrayReleaseRules.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this DeployStrategyGrayReleaseRules.

        匹配类型

        :param type: The type of this DeployStrategyGrayReleaseRules.
        :type type: str
        """
        self._type = type

    @property
    def key(self):
        r"""Gets the key of this DeployStrategyGrayReleaseRules.

        参数名称

        :return: The key of this DeployStrategyGrayReleaseRules.
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        r"""Sets the key of this DeployStrategyGrayReleaseRules.

        参数名称

        :param key: The key of this DeployStrategyGrayReleaseRules.
        :type key: str
        """
        self._key = key

    @property
    def value(self):
        r"""Gets the value of this DeployStrategyGrayReleaseRules.

        条件值

        :return: The value of this DeployStrategyGrayReleaseRules.
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        r"""Sets the value of this DeployStrategyGrayReleaseRules.

        条件值

        :param value: The value of this DeployStrategyGrayReleaseRules.
        :type value: str
        """
        self._value = value

    @property
    def condition(self):
        r"""Gets the condition of this DeployStrategyGrayReleaseRules.

        equal相等，match匹配，in枚举

        :return: The condition of this DeployStrategyGrayReleaseRules.
        :rtype: str
        """
        return self._condition

    @condition.setter
    def condition(self, condition):
        r"""Sets the condition of this DeployStrategyGrayReleaseRules.

        equal相等，match匹配，in枚举

        :param condition: The condition of this DeployStrategyGrayReleaseRules.
        :type condition: str
        """
        self._condition = condition

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
        if not isinstance(other, DeployStrategyGrayReleaseRules):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

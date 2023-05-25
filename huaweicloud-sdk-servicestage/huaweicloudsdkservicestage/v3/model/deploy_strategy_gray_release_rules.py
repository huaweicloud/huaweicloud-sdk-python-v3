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
        """DeployStrategyGrayReleaseRules

        The model defined in huaweicloud sdk

        :param type: 
        :type type: str
        :param key: 
        :type key: str
        :param value: 
        :type value: str
        :param condition: 
        :type condition: str
        """
        
        

        self._type = None
        self._key = None
        self._value = None
        self._condition = None
        self.discriminator = None

        if type is not None:
            self.type = type
        if key is not None:
            self.key = key
        if value is not None:
            self.value = value
        if condition is not None:
            self.condition = condition

    @property
    def type(self):
        """Gets the type of this DeployStrategyGrayReleaseRules.

        :return: The type of this DeployStrategyGrayReleaseRules.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this DeployStrategyGrayReleaseRules.

        :param type: The type of this DeployStrategyGrayReleaseRules.
        :type type: str
        """
        self._type = type

    @property
    def key(self):
        """Gets the key of this DeployStrategyGrayReleaseRules.

        :return: The key of this DeployStrategyGrayReleaseRules.
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        """Sets the key of this DeployStrategyGrayReleaseRules.

        :param key: The key of this DeployStrategyGrayReleaseRules.
        :type key: str
        """
        self._key = key

    @property
    def value(self):
        """Gets the value of this DeployStrategyGrayReleaseRules.

        :return: The value of this DeployStrategyGrayReleaseRules.
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this DeployStrategyGrayReleaseRules.

        :param value: The value of this DeployStrategyGrayReleaseRules.
        :type value: str
        """
        self._value = value

    @property
    def condition(self):
        """Gets the condition of this DeployStrategyGrayReleaseRules.

        :return: The condition of this DeployStrategyGrayReleaseRules.
        :rtype: str
        """
        return self._condition

    @condition.setter
    def condition(self, condition):
        """Sets the condition of this DeployStrategyGrayReleaseRules.

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

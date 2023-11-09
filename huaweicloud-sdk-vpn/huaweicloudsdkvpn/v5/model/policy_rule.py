# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PolicyRule:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'rule_index': 'int',
        'source': 'str',
        'destination': 'list[str]'
    }

    attribute_map = {
        'rule_index': 'rule_index',
        'source': 'source',
        'destination': 'destination'
    }

    def __init__(self, rule_index=None, source=None, destination=None):
        """PolicyRule

        The model defined in huaweicloud sdk

        :param rule_index: 规则ID
        :type rule_index: int
        :param source: 源地址网段
        :type source: str
        :param destination: 目的地址网段
        :type destination: list[str]
        """
        
        

        self._rule_index = None
        self._source = None
        self._destination = None
        self.discriminator = None

        if rule_index is not None:
            self.rule_index = rule_index
        if source is not None:
            self.source = source
        if destination is not None:
            self.destination = destination

    @property
    def rule_index(self):
        """Gets the rule_index of this PolicyRule.

        规则ID

        :return: The rule_index of this PolicyRule.
        :rtype: int
        """
        return self._rule_index

    @rule_index.setter
    def rule_index(self, rule_index):
        """Sets the rule_index of this PolicyRule.

        规则ID

        :param rule_index: The rule_index of this PolicyRule.
        :type rule_index: int
        """
        self._rule_index = rule_index

    @property
    def source(self):
        """Gets the source of this PolicyRule.

        源地址网段

        :return: The source of this PolicyRule.
        :rtype: str
        """
        return self._source

    @source.setter
    def source(self, source):
        """Sets the source of this PolicyRule.

        源地址网段

        :param source: The source of this PolicyRule.
        :type source: str
        """
        self._source = source

    @property
    def destination(self):
        """Gets the destination of this PolicyRule.

        目的地址网段

        :return: The destination of this PolicyRule.
        :rtype: list[str]
        """
        return self._destination

    @destination.setter
    def destination(self, destination):
        """Sets the destination of this PolicyRule.

        目的地址网段

        :param destination: The destination of this PolicyRule.
        :type destination: list[str]
        """
        self._destination = destination

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
        if not isinstance(other, PolicyRule):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SqlFilterRulePattern:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'pattern': 'str',
        'max_concurrency': 'int'
    }

    attribute_map = {
        'pattern': 'pattern',
        'max_concurrency': 'max_concurrency'
    }

    def __init__(self, pattern=None, max_concurrency=None):
        """SqlFilterRulePattern

        The model defined in huaweicloud sdk

        :param pattern: SQL限流规则。
        :type pattern: str
        :param max_concurrency: 最大并发数。
        :type max_concurrency: int
        """
        
        

        self._pattern = None
        self._max_concurrency = None
        self.discriminator = None

        self.pattern = pattern
        self.max_concurrency = max_concurrency

    @property
    def pattern(self):
        """Gets the pattern of this SqlFilterRulePattern.

        SQL限流规则。

        :return: The pattern of this SqlFilterRulePattern.
        :rtype: str
        """
        return self._pattern

    @pattern.setter
    def pattern(self, pattern):
        """Sets the pattern of this SqlFilterRulePattern.

        SQL限流规则。

        :param pattern: The pattern of this SqlFilterRulePattern.
        :type pattern: str
        """
        self._pattern = pattern

    @property
    def max_concurrency(self):
        """Gets the max_concurrency of this SqlFilterRulePattern.

        最大并发数。

        :return: The max_concurrency of this SqlFilterRulePattern.
        :rtype: int
        """
        return self._max_concurrency

    @max_concurrency.setter
    def max_concurrency(self, max_concurrency):
        """Sets the max_concurrency of this SqlFilterRulePattern.

        最大并发数。

        :param max_concurrency: The max_concurrency of this SqlFilterRulePattern.
        :type max_concurrency: int
        """
        self._max_concurrency = max_concurrency

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
        if not isinstance(other, SqlFilterRulePattern):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

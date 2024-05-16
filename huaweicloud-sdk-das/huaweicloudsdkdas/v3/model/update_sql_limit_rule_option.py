# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateSqlLimitRuleOption:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'max_concurrency': 'int',
        'max_waiting': 'int'
    }

    attribute_map = {
        'max_concurrency': 'max_concurrency',
        'max_waiting': 'max_waiting'
    }

    def __init__(self, max_concurrency=None, max_waiting=None):
        """UpdateSqlLimitRuleOption

        The model defined in huaweicloud sdk

        :param max_concurrency: 最大并发数
        :type max_concurrency: int
        :param max_waiting: 最大等待时间
        :type max_waiting: int
        """
        
        

        self._max_concurrency = None
        self._max_waiting = None
        self.discriminator = None

        self.max_concurrency = max_concurrency
        if max_waiting is not None:
            self.max_waiting = max_waiting

    @property
    def max_concurrency(self):
        """Gets the max_concurrency of this UpdateSqlLimitRuleOption.

        最大并发数

        :return: The max_concurrency of this UpdateSqlLimitRuleOption.
        :rtype: int
        """
        return self._max_concurrency

    @max_concurrency.setter
    def max_concurrency(self, max_concurrency):
        """Sets the max_concurrency of this UpdateSqlLimitRuleOption.

        最大并发数

        :param max_concurrency: The max_concurrency of this UpdateSqlLimitRuleOption.
        :type max_concurrency: int
        """
        self._max_concurrency = max_concurrency

    @property
    def max_waiting(self):
        """Gets the max_waiting of this UpdateSqlLimitRuleOption.

        最大等待时间

        :return: The max_waiting of this UpdateSqlLimitRuleOption.
        :rtype: int
        """
        return self._max_waiting

    @max_waiting.setter
    def max_waiting(self, max_waiting):
        """Sets the max_waiting of this UpdateSqlLimitRuleOption.

        最大等待时间

        :param max_waiting: The max_waiting of this UpdateSqlLimitRuleOption.
        :type max_waiting: int
        """
        self._max_waiting = max_waiting

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
        if not isinstance(other, UpdateSqlLimitRuleOption):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

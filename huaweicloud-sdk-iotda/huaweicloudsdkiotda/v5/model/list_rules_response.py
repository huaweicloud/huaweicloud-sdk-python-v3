# coding: utf-8

import pprint
import re

import six


from huaweicloudsdkcore.sdk_response import SdkResponse


class ListRulesResponse(SdkResponse):


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'marker': 'str',
        'count': 'int',
        'rules': 'list[RuleResponse]'
    }

    attribute_map = {
        'marker': 'marker',
        'count': 'count',
        'rules': 'rules'
    }

    def __init__(self, marker=None, count=None, rules=None):
        """ListRulesResponse - a model defined in huaweicloud sdk"""
        
        super().__init__()

        self._marker = None
        self._count = None
        self._rules = None
        self.discriminator = None

        if marker is not None:
            self.marker = marker
        if count is not None:
            self.count = count
        if rules is not None:
            self.rules = rules

    @property
    def marker(self):
        """Gets the marker of this ListRulesResponse.

        本次分页查询结果中最后一条记录的ID，可在下一次分页查询时使用。

        :return: The marker of this ListRulesResponse.
        :rtype: str
        """
        return self._marker

    @marker.setter
    def marker(self, marker):
        """Sets the marker of this ListRulesResponse.

        本次分页查询结果中最后一条记录的ID，可在下一次分页查询时使用。

        :param marker: The marker of this ListRulesResponse.
        :type: str
        """
        self._marker = marker

    @property
    def count(self):
        """Gets the count of this ListRulesResponse.

        满足查询条件的记录总数。

        :return: The count of this ListRulesResponse.
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        """Sets the count of this ListRulesResponse.

        满足查询条件的记录总数。

        :param count: The count of this ListRulesResponse.
        :type: int
        """
        self._count = count

    @property
    def rules(self):
        """Gets the rules of this ListRulesResponse.

        规则信息列表。

        :return: The rules of this ListRulesResponse.
        :rtype: list[RuleResponse]
        """
        return self._rules

    @rules.setter
    def rules(self, rules):
        """Sets the rules of this ListRulesResponse.

        规则信息列表。

        :param rules: The rules of this ListRulesResponse.
        :type: list[RuleResponse]
        """
        self._rules = rules

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
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ListRulesResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


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
        'rules': 'list[RuleResponse]',
        'count': 'int'
    }

    attribute_map = {
        'rules': 'rules',
        'count': 'count'
    }

    def __init__(self, rules=None, count=None):
        """ListRulesResponse

        The model defined in huaweicloud sdk

        :param rules: 规则配置
        :type rules: list[:class:`huaweicloudsdkief.v1.RuleResponse`]
        :param count: 满足条件的规则个数
        :type count: int
        """
        
        super(ListRulesResponse, self).__init__()

        self._rules = None
        self._count = None
        self.discriminator = None

        if rules is not None:
            self.rules = rules
        if count is not None:
            self.count = count

    @property
    def rules(self):
        """Gets the rules of this ListRulesResponse.

        规则配置

        :return: The rules of this ListRulesResponse.
        :rtype: list[:class:`huaweicloudsdkief.v1.RuleResponse`]
        """
        return self._rules

    @rules.setter
    def rules(self, rules):
        """Sets the rules of this ListRulesResponse.

        规则配置

        :param rules: The rules of this ListRulesResponse.
        :type rules: list[:class:`huaweicloudsdkief.v1.RuleResponse`]
        """
        self._rules = rules

    @property
    def count(self):
        """Gets the count of this ListRulesResponse.

        满足条件的规则个数

        :return: The count of this ListRulesResponse.
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        """Sets the count of this ListRulesResponse.

        满足条件的规则个数

        :param count: The count of this ListRulesResponse.
        :type count: int
        """
        self._count = count

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
        if not isinstance(other, ListRulesResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

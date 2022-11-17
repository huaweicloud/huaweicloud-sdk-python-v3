# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListRulesRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'rule_languages': 'str',
        'rule_severity': 'str',
        'offset': 'int',
        'limit': 'int'
    }

    attribute_map = {
        'rule_languages': 'rule_languages',
        'rule_severity': 'rule_severity',
        'offset': 'offset',
        'limit': 'limit'
    }

    def __init__(self, rule_languages=None, rule_severity=None, offset=None, limit=None):
        """ListRulesRequest

        The model defined in huaweicloud sdk

        :param rule_languages: 规则对应的语言
        :type rule_languages: str
        :param rule_severity: 缺陷等级，0致命，1严重，2一般，3提示
        :type rule_severity: str
        :param offset: 分页索引，偏移量
        :type offset: int
        :param limit: 每页显示的数量
        :type limit: int
        """
        
        

        self._rule_languages = None
        self._rule_severity = None
        self._offset = None
        self._limit = None
        self.discriminator = None

        if rule_languages is not None:
            self.rule_languages = rule_languages
        if rule_severity is not None:
            self.rule_severity = rule_severity
        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit

    @property
    def rule_languages(self):
        """Gets the rule_languages of this ListRulesRequest.

        规则对应的语言

        :return: The rule_languages of this ListRulesRequest.
        :rtype: str
        """
        return self._rule_languages

    @rule_languages.setter
    def rule_languages(self, rule_languages):
        """Sets the rule_languages of this ListRulesRequest.

        规则对应的语言

        :param rule_languages: The rule_languages of this ListRulesRequest.
        :type rule_languages: str
        """
        self._rule_languages = rule_languages

    @property
    def rule_severity(self):
        """Gets the rule_severity of this ListRulesRequest.

        缺陷等级，0致命，1严重，2一般，3提示

        :return: The rule_severity of this ListRulesRequest.
        :rtype: str
        """
        return self._rule_severity

    @rule_severity.setter
    def rule_severity(self, rule_severity):
        """Sets the rule_severity of this ListRulesRequest.

        缺陷等级，0致命，1严重，2一般，3提示

        :param rule_severity: The rule_severity of this ListRulesRequest.
        :type rule_severity: str
        """
        self._rule_severity = rule_severity

    @property
    def offset(self):
        """Gets the offset of this ListRulesRequest.

        分页索引，偏移量

        :return: The offset of this ListRulesRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this ListRulesRequest.

        分页索引，偏移量

        :param offset: The offset of this ListRulesRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        """Gets the limit of this ListRulesRequest.

        每页显示的数量

        :return: The limit of this ListRulesRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListRulesRequest.

        每页显示的数量

        :param limit: The limit of this ListRulesRequest.
        :type limit: int
        """
        self._limit = limit

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
        if not isinstance(other, ListRulesRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

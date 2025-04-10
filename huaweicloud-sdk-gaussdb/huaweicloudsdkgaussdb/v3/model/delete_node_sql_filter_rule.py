# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DeleteNodeSqlFilterRule:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'sql_type': 'str',
        'patterns': 'list[str]'
    }

    attribute_map = {
        'sql_type': 'sql_type',
        'patterns': 'patterns'
    }

    def __init__(self, sql_type=None, patterns=None):
        r"""DeleteNodeSqlFilterRule

        The model defined in huaweicloud sdk

        :param sql_type: Sql限流类型。  取值范围： - SELECT - UPDATE - DELETE
        :type sql_type: str
        :param patterns: SQL限流具体规则。
        :type patterns: list[str]
        """
        
        

        self._sql_type = None
        self._patterns = None
        self.discriminator = None

        self.sql_type = sql_type
        self.patterns = patterns

    @property
    def sql_type(self):
        r"""Gets the sql_type of this DeleteNodeSqlFilterRule.

        Sql限流类型。  取值范围： - SELECT - UPDATE - DELETE

        :return: The sql_type of this DeleteNodeSqlFilterRule.
        :rtype: str
        """
        return self._sql_type

    @sql_type.setter
    def sql_type(self, sql_type):
        r"""Sets the sql_type of this DeleteNodeSqlFilterRule.

        Sql限流类型。  取值范围： - SELECT - UPDATE - DELETE

        :param sql_type: The sql_type of this DeleteNodeSqlFilterRule.
        :type sql_type: str
        """
        self._sql_type = sql_type

    @property
    def patterns(self):
        r"""Gets the patterns of this DeleteNodeSqlFilterRule.

        SQL限流具体规则。

        :return: The patterns of this DeleteNodeSqlFilterRule.
        :rtype: list[str]
        """
        return self._patterns

    @patterns.setter
    def patterns(self, patterns):
        r"""Sets the patterns of this DeleteNodeSqlFilterRule.

        SQL限流具体规则。

        :param patterns: The patterns of this DeleteNodeSqlFilterRule.
        :type patterns: list[str]
        """
        self._patterns = patterns

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
        if not isinstance(other, DeleteNodeSqlFilterRule):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

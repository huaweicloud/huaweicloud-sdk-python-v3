# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DbMatchInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'column_name': 'str',
        'rule_name': 'str',
        'rule_id': 'str',
        'rule_risk_level': 'int',
        'column_line': 'list[int]'
    }

    attribute_map = {
        'column_name': 'column_name',
        'rule_name': 'rule_name',
        'rule_id': 'rule_id',
        'rule_risk_level': 'rule_risk_level',
        'column_line': 'column_line'
    }

    def __init__(self, column_name=None, rule_name=None, rule_id=None, rule_risk_level=None, column_line=None):
        """DbMatchInfo

        The model defined in huaweicloud sdk

        :param column_name: 列名
        :type column_name: str
        :param rule_name: 匹配的规则名
        :type rule_name: str
        :param rule_id: 匹配的规则ID
        :type rule_id: str
        :param rule_risk_level: 匹配规则风险等级
        :type rule_risk_level: int
        :param column_line: 风险数据行
        :type column_line: list[int]
        """
        
        

        self._column_name = None
        self._rule_name = None
        self._rule_id = None
        self._rule_risk_level = None
        self._column_line = None
        self.discriminator = None

        if column_name is not None:
            self.column_name = column_name
        if rule_name is not None:
            self.rule_name = rule_name
        if rule_id is not None:
            self.rule_id = rule_id
        if rule_risk_level is not None:
            self.rule_risk_level = rule_risk_level
        if column_line is not None:
            self.column_line = column_line

    @property
    def column_name(self):
        """Gets the column_name of this DbMatchInfo.

        列名

        :return: The column_name of this DbMatchInfo.
        :rtype: str
        """
        return self._column_name

    @column_name.setter
    def column_name(self, column_name):
        """Sets the column_name of this DbMatchInfo.

        列名

        :param column_name: The column_name of this DbMatchInfo.
        :type column_name: str
        """
        self._column_name = column_name

    @property
    def rule_name(self):
        """Gets the rule_name of this DbMatchInfo.

        匹配的规则名

        :return: The rule_name of this DbMatchInfo.
        :rtype: str
        """
        return self._rule_name

    @rule_name.setter
    def rule_name(self, rule_name):
        """Sets the rule_name of this DbMatchInfo.

        匹配的规则名

        :param rule_name: The rule_name of this DbMatchInfo.
        :type rule_name: str
        """
        self._rule_name = rule_name

    @property
    def rule_id(self):
        """Gets the rule_id of this DbMatchInfo.

        匹配的规则ID

        :return: The rule_id of this DbMatchInfo.
        :rtype: str
        """
        return self._rule_id

    @rule_id.setter
    def rule_id(self, rule_id):
        """Sets the rule_id of this DbMatchInfo.

        匹配的规则ID

        :param rule_id: The rule_id of this DbMatchInfo.
        :type rule_id: str
        """
        self._rule_id = rule_id

    @property
    def rule_risk_level(self):
        """Gets the rule_risk_level of this DbMatchInfo.

        匹配规则风险等级

        :return: The rule_risk_level of this DbMatchInfo.
        :rtype: int
        """
        return self._rule_risk_level

    @rule_risk_level.setter
    def rule_risk_level(self, rule_risk_level):
        """Sets the rule_risk_level of this DbMatchInfo.

        匹配规则风险等级

        :param rule_risk_level: The rule_risk_level of this DbMatchInfo.
        :type rule_risk_level: int
        """
        self._rule_risk_level = rule_risk_level

    @property
    def column_line(self):
        """Gets the column_line of this DbMatchInfo.

        风险数据行

        :return: The column_line of this DbMatchInfo.
        :rtype: list[int]
        """
        return self._column_line

    @column_line.setter
    def column_line(self, column_line):
        """Sets the column_line of this DbMatchInfo.

        风险数据行

        :param column_line: The column_line of this DbMatchInfo.
        :type column_line: list[int]
        """
        self._column_line = column_line

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
        if not isinstance(other, DbMatchInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

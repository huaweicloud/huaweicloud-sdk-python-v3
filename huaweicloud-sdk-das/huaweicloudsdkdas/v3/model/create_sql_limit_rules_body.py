# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateSqlLimitRulesBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'datastore_type': 'str',
        'sql_limit_rules': 'list[CreateSqlLimitRuleOption]'
    }

    attribute_map = {
        'datastore_type': 'datastore_type',
        'sql_limit_rules': 'sql_limit_rules'
    }

    def __init__(self, datastore_type=None, sql_limit_rules=None):
        """CreateSqlLimitRulesBody

        The model defined in huaweicloud sdk

        :param datastore_type: 数据库类型
        :type datastore_type: str
        :param sql_limit_rules: 需要创建的SQL限流规则列表，一次最多创建5个
        :type sql_limit_rules: list[:class:`huaweicloudsdkdas.v3.CreateSqlLimitRuleOption`]
        """
        
        

        self._datastore_type = None
        self._sql_limit_rules = None
        self.discriminator = None

        self.datastore_type = datastore_type
        self.sql_limit_rules = sql_limit_rules

    @property
    def datastore_type(self):
        """Gets the datastore_type of this CreateSqlLimitRulesBody.

        数据库类型

        :return: The datastore_type of this CreateSqlLimitRulesBody.
        :rtype: str
        """
        return self._datastore_type

    @datastore_type.setter
    def datastore_type(self, datastore_type):
        """Sets the datastore_type of this CreateSqlLimitRulesBody.

        数据库类型

        :param datastore_type: The datastore_type of this CreateSqlLimitRulesBody.
        :type datastore_type: str
        """
        self._datastore_type = datastore_type

    @property
    def sql_limit_rules(self):
        """Gets the sql_limit_rules of this CreateSqlLimitRulesBody.

        需要创建的SQL限流规则列表，一次最多创建5个

        :return: The sql_limit_rules of this CreateSqlLimitRulesBody.
        :rtype: list[:class:`huaweicloudsdkdas.v3.CreateSqlLimitRuleOption`]
        """
        return self._sql_limit_rules

    @sql_limit_rules.setter
    def sql_limit_rules(self, sql_limit_rules):
        """Sets the sql_limit_rules of this CreateSqlLimitRulesBody.

        需要创建的SQL限流规则列表，一次最多创建5个

        :param sql_limit_rules: The sql_limit_rules of this CreateSqlLimitRulesBody.
        :type sql_limit_rules: list[:class:`huaweicloudsdkdas.v3.CreateSqlLimitRuleOption`]
        """
        self._sql_limit_rules = sql_limit_rules

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
        if not isinstance(other, CreateSqlLimitRulesBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class EsMatchInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'field_name': 'str',
        'rule_name': 'str',
        'rule_id': 'str',
        'rule_risk_level': 'int'
    }

    attribute_map = {
        'field_name': 'field_name',
        'rule_name': 'rule_name',
        'rule_id': 'rule_id',
        'rule_risk_level': 'rule_risk_level'
    }

    def __init__(self, field_name=None, rule_name=None, rule_id=None, rule_risk_level=None):
        """EsMatchInfo

        The model defined in huaweicloud sdk

        :param field_name: 数据字段名
        :type field_name: str
        :param rule_name: 规则名
        :type rule_name: str
        :param rule_id: 规则ID
        :type rule_id: str
        :param rule_risk_level: 规则风险等级
        :type rule_risk_level: int
        """
        
        

        self._field_name = None
        self._rule_name = None
        self._rule_id = None
        self._rule_risk_level = None
        self.discriminator = None

        if field_name is not None:
            self.field_name = field_name
        if rule_name is not None:
            self.rule_name = rule_name
        if rule_id is not None:
            self.rule_id = rule_id
        if rule_risk_level is not None:
            self.rule_risk_level = rule_risk_level

    @property
    def field_name(self):
        """Gets the field_name of this EsMatchInfo.

        数据字段名

        :return: The field_name of this EsMatchInfo.
        :rtype: str
        """
        return self._field_name

    @field_name.setter
    def field_name(self, field_name):
        """Sets the field_name of this EsMatchInfo.

        数据字段名

        :param field_name: The field_name of this EsMatchInfo.
        :type field_name: str
        """
        self._field_name = field_name

    @property
    def rule_name(self):
        """Gets the rule_name of this EsMatchInfo.

        规则名

        :return: The rule_name of this EsMatchInfo.
        :rtype: str
        """
        return self._rule_name

    @rule_name.setter
    def rule_name(self, rule_name):
        """Sets the rule_name of this EsMatchInfo.

        规则名

        :param rule_name: The rule_name of this EsMatchInfo.
        :type rule_name: str
        """
        self._rule_name = rule_name

    @property
    def rule_id(self):
        """Gets the rule_id of this EsMatchInfo.

        规则ID

        :return: The rule_id of this EsMatchInfo.
        :rtype: str
        """
        return self._rule_id

    @rule_id.setter
    def rule_id(self, rule_id):
        """Sets the rule_id of this EsMatchInfo.

        规则ID

        :param rule_id: The rule_id of this EsMatchInfo.
        :type rule_id: str
        """
        self._rule_id = rule_id

    @property
    def rule_risk_level(self):
        """Gets the rule_risk_level of this EsMatchInfo.

        规则风险等级

        :return: The rule_risk_level of this EsMatchInfo.
        :rtype: int
        """
        return self._rule_risk_level

    @rule_risk_level.setter
    def rule_risk_level(self, rule_risk_level):
        """Sets the rule_risk_level of this EsMatchInfo.

        规则风险等级

        :param rule_risk_level: The rule_risk_level of this EsMatchInfo.
        :type rule_risk_level: int
        """
        self._rule_risk_level = rule_risk_level

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
        if not isinstance(other, EsMatchInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

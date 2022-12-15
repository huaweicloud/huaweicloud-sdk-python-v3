# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CheckRuleFixParamInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'rule_param_id': 'int',
        'rule_desc': 'str',
        'default_value': 'int',
        'range_min': 'int',
        'range_max': 'int'
    }

    attribute_map = {
        'rule_param_id': 'rule_param_id',
        'rule_desc': 'rule_desc',
        'default_value': 'default_value',
        'range_min': 'range_min',
        'range_max': 'range_max'
    }

    def __init__(self, rule_param_id=None, rule_desc=None, default_value=None, range_min=None, range_max=None):
        """CheckRuleFixParamInfo

        The model defined in huaweicloud sdk

        :param rule_param_id: 检查项参数ID
        :type rule_param_id: int
        :param rule_desc: 检查项参数描述
        :type rule_desc: str
        :param default_value: 检查项参数默认值
        :type default_value: int
        :param range_min: 检查项参数可取最小值
        :type range_min: int
        :param range_max: 检查项参数可取最大值
        :type range_max: int
        """
        
        

        self._rule_param_id = None
        self._rule_desc = None
        self._default_value = None
        self._range_min = None
        self._range_max = None
        self.discriminator = None

        if rule_param_id is not None:
            self.rule_param_id = rule_param_id
        if rule_desc is not None:
            self.rule_desc = rule_desc
        if default_value is not None:
            self.default_value = default_value
        if range_min is not None:
            self.range_min = range_min
        if range_max is not None:
            self.range_max = range_max

    @property
    def rule_param_id(self):
        """Gets the rule_param_id of this CheckRuleFixParamInfo.

        检查项参数ID

        :return: The rule_param_id of this CheckRuleFixParamInfo.
        :rtype: int
        """
        return self._rule_param_id

    @rule_param_id.setter
    def rule_param_id(self, rule_param_id):
        """Sets the rule_param_id of this CheckRuleFixParamInfo.

        检查项参数ID

        :param rule_param_id: The rule_param_id of this CheckRuleFixParamInfo.
        :type rule_param_id: int
        """
        self._rule_param_id = rule_param_id

    @property
    def rule_desc(self):
        """Gets the rule_desc of this CheckRuleFixParamInfo.

        检查项参数描述

        :return: The rule_desc of this CheckRuleFixParamInfo.
        :rtype: str
        """
        return self._rule_desc

    @rule_desc.setter
    def rule_desc(self, rule_desc):
        """Sets the rule_desc of this CheckRuleFixParamInfo.

        检查项参数描述

        :param rule_desc: The rule_desc of this CheckRuleFixParamInfo.
        :type rule_desc: str
        """
        self._rule_desc = rule_desc

    @property
    def default_value(self):
        """Gets the default_value of this CheckRuleFixParamInfo.

        检查项参数默认值

        :return: The default_value of this CheckRuleFixParamInfo.
        :rtype: int
        """
        return self._default_value

    @default_value.setter
    def default_value(self, default_value):
        """Sets the default_value of this CheckRuleFixParamInfo.

        检查项参数默认值

        :param default_value: The default_value of this CheckRuleFixParamInfo.
        :type default_value: int
        """
        self._default_value = default_value

    @property
    def range_min(self):
        """Gets the range_min of this CheckRuleFixParamInfo.

        检查项参数可取最小值

        :return: The range_min of this CheckRuleFixParamInfo.
        :rtype: int
        """
        return self._range_min

    @range_min.setter
    def range_min(self, range_min):
        """Sets the range_min of this CheckRuleFixParamInfo.

        检查项参数可取最小值

        :param range_min: The range_min of this CheckRuleFixParamInfo.
        :type range_min: int
        """
        self._range_min = range_min

    @property
    def range_max(self):
        """Gets the range_max of this CheckRuleFixParamInfo.

        检查项参数可取最大值

        :return: The range_max of this CheckRuleFixParamInfo.
        :rtype: int
        """
        return self._range_max

    @range_max.setter
    def range_max(self, range_max):
        """Sets the range_max of this CheckRuleFixParamInfo.

        检查项参数可取最大值

        :param range_max: The range_max of this CheckRuleFixParamInfo.
        :type range_max: int
        """
        self._range_max = range_max

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
        if not isinstance(other, CheckRuleFixParamInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

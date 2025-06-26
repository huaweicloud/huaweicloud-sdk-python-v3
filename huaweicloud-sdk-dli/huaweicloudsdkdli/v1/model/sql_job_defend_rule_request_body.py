# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SqlJobDefendRuleRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'rule_name': 'str',
        'rule_id': 'str',
        'category': 'str',
        'engine_rules': 'object',
        'queue_names': 'list[str]'
    }

    attribute_map = {
        'rule_name': 'rule_name',
        'rule_id': 'rule_id',
        'category': 'category',
        'engine_rules': 'engine_rules',
        'queue_names': 'queue_names'
    }

    def __init__(self, rule_name=None, rule_id=None, category=None, engine_rules=None, queue_names=None):
        r"""SqlJobDefendRuleRequestBody

        The model defined in huaweicloud sdk

        :param rule_name: 规则名称
        :type rule_name: str
        :param rule_id: 规则类型
        :type rule_id: str
        :param category: 规则状态类型
        :type category: str
        :param engine_rules: 规则详情
        :type engine_rules: object
        :param queue_names: 队列名称
        :type queue_names: list[str]
        """
        
        

        self._rule_name = None
        self._rule_id = None
        self._category = None
        self._engine_rules = None
        self._queue_names = None
        self.discriminator = None

        self.rule_name = rule_name
        self.rule_id = rule_id
        self.category = category
        self.engine_rules = engine_rules
        if queue_names is not None:
            self.queue_names = queue_names

    @property
    def rule_name(self):
        r"""Gets the rule_name of this SqlJobDefendRuleRequestBody.

        规则名称

        :return: The rule_name of this SqlJobDefendRuleRequestBody.
        :rtype: str
        """
        return self._rule_name

    @rule_name.setter
    def rule_name(self, rule_name):
        r"""Sets the rule_name of this SqlJobDefendRuleRequestBody.

        规则名称

        :param rule_name: The rule_name of this SqlJobDefendRuleRequestBody.
        :type rule_name: str
        """
        self._rule_name = rule_name

    @property
    def rule_id(self):
        r"""Gets the rule_id of this SqlJobDefendRuleRequestBody.

        规则类型

        :return: The rule_id of this SqlJobDefendRuleRequestBody.
        :rtype: str
        """
        return self._rule_id

    @rule_id.setter
    def rule_id(self, rule_id):
        r"""Sets the rule_id of this SqlJobDefendRuleRequestBody.

        规则类型

        :param rule_id: The rule_id of this SqlJobDefendRuleRequestBody.
        :type rule_id: str
        """
        self._rule_id = rule_id

    @property
    def category(self):
        r"""Gets the category of this SqlJobDefendRuleRequestBody.

        规则状态类型

        :return: The category of this SqlJobDefendRuleRequestBody.
        :rtype: str
        """
        return self._category

    @category.setter
    def category(self, category):
        r"""Sets the category of this SqlJobDefendRuleRequestBody.

        规则状态类型

        :param category: The category of this SqlJobDefendRuleRequestBody.
        :type category: str
        """
        self._category = category

    @property
    def engine_rules(self):
        r"""Gets the engine_rules of this SqlJobDefendRuleRequestBody.

        规则详情

        :return: The engine_rules of this SqlJobDefendRuleRequestBody.
        :rtype: object
        """
        return self._engine_rules

    @engine_rules.setter
    def engine_rules(self, engine_rules):
        r"""Sets the engine_rules of this SqlJobDefendRuleRequestBody.

        规则详情

        :param engine_rules: The engine_rules of this SqlJobDefendRuleRequestBody.
        :type engine_rules: object
        """
        self._engine_rules = engine_rules

    @property
    def queue_names(self):
        r"""Gets the queue_names of this SqlJobDefendRuleRequestBody.

        队列名称

        :return: The queue_names of this SqlJobDefendRuleRequestBody.
        :rtype: list[str]
        """
        return self._queue_names

    @queue_names.setter
    def queue_names(self, queue_names):
        r"""Sets the queue_names of this SqlJobDefendRuleRequestBody.

        队列名称

        :param queue_names: The queue_names of this SqlJobDefendRuleRequestBody.
        :type queue_names: list[str]
        """
        self._queue_names = queue_names

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
        if not isinstance(other, SqlJobDefendRuleRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

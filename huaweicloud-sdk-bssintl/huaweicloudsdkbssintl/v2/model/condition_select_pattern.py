# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ConditionSelectPattern:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'condition_type': 'str',
        'condition_statement': 'str',
        'policy_mode': 'str',
        'official_price': 'str',
        'division_pattern': 'DivisionPattern'
    }

    attribute_map = {
        'condition_type': 'condition_type',
        'condition_statement': 'condition_statement',
        'policy_mode': 'policy_mode',
        'official_price': 'official_price',
        'division_pattern': 'division_pattern'
    }

    def __init__(self, condition_type=None, condition_statement=None, policy_mode=None, official_price=None, division_pattern=None):
        r"""ConditionSelectPattern

        The model defined in huaweicloud sdk

        :param condition_type: 条件类型，SERVICE_HOUR_TIME：时间段 PERIOD_NUM：周期数 PERIOD_TYPE：周期类型，年、月、天、小时 PURCHASE_SCENE：订购场景，订购、续订、变更 NUMBER_OF_PEOPLE：线性大小
        :type condition_type: str
        :param condition_statement: 条件表达式
        :type condition_statement: str
        :param policy_mode: 定价策略类型，SIMPLE：简单定价 DIVISION：阶梯定价
        :type policy_mode: str
        :param official_price: 阶梯官网价，policy_mode取值为SIMPLE时为官网价，如果取值为DIVISION，则价格在division_pattern中。
        :type official_price: str
        :param division_pattern: 
        :type division_pattern: :class:`huaweicloudsdkbssintl.v2.DivisionPattern`
        """
        
        

        self._condition_type = None
        self._condition_statement = None
        self._policy_mode = None
        self._official_price = None
        self._division_pattern = None
        self.discriminator = None

        if condition_type is not None:
            self.condition_type = condition_type
        if condition_statement is not None:
            self.condition_statement = condition_statement
        if policy_mode is not None:
            self.policy_mode = policy_mode
        if official_price is not None:
            self.official_price = official_price
        if division_pattern is not None:
            self.division_pattern = division_pattern

    @property
    def condition_type(self):
        r"""Gets the condition_type of this ConditionSelectPattern.

        条件类型，SERVICE_HOUR_TIME：时间段 PERIOD_NUM：周期数 PERIOD_TYPE：周期类型，年、月、天、小时 PURCHASE_SCENE：订购场景，订购、续订、变更 NUMBER_OF_PEOPLE：线性大小

        :return: The condition_type of this ConditionSelectPattern.
        :rtype: str
        """
        return self._condition_type

    @condition_type.setter
    def condition_type(self, condition_type):
        r"""Sets the condition_type of this ConditionSelectPattern.

        条件类型，SERVICE_HOUR_TIME：时间段 PERIOD_NUM：周期数 PERIOD_TYPE：周期类型，年、月、天、小时 PURCHASE_SCENE：订购场景，订购、续订、变更 NUMBER_OF_PEOPLE：线性大小

        :param condition_type: The condition_type of this ConditionSelectPattern.
        :type condition_type: str
        """
        self._condition_type = condition_type

    @property
    def condition_statement(self):
        r"""Gets the condition_statement of this ConditionSelectPattern.

        条件表达式

        :return: The condition_statement of this ConditionSelectPattern.
        :rtype: str
        """
        return self._condition_statement

    @condition_statement.setter
    def condition_statement(self, condition_statement):
        r"""Sets the condition_statement of this ConditionSelectPattern.

        条件表达式

        :param condition_statement: The condition_statement of this ConditionSelectPattern.
        :type condition_statement: str
        """
        self._condition_statement = condition_statement

    @property
    def policy_mode(self):
        r"""Gets the policy_mode of this ConditionSelectPattern.

        定价策略类型，SIMPLE：简单定价 DIVISION：阶梯定价

        :return: The policy_mode of this ConditionSelectPattern.
        :rtype: str
        """
        return self._policy_mode

    @policy_mode.setter
    def policy_mode(self, policy_mode):
        r"""Sets the policy_mode of this ConditionSelectPattern.

        定价策略类型，SIMPLE：简单定价 DIVISION：阶梯定价

        :param policy_mode: The policy_mode of this ConditionSelectPattern.
        :type policy_mode: str
        """
        self._policy_mode = policy_mode

    @property
    def official_price(self):
        r"""Gets the official_price of this ConditionSelectPattern.

        阶梯官网价，policy_mode取值为SIMPLE时为官网价，如果取值为DIVISION，则价格在division_pattern中。

        :return: The official_price of this ConditionSelectPattern.
        :rtype: str
        """
        return self._official_price

    @official_price.setter
    def official_price(self, official_price):
        r"""Sets the official_price of this ConditionSelectPattern.

        阶梯官网价，policy_mode取值为SIMPLE时为官网价，如果取值为DIVISION，则价格在division_pattern中。

        :param official_price: The official_price of this ConditionSelectPattern.
        :type official_price: str
        """
        self._official_price = official_price

    @property
    def division_pattern(self):
        r"""Gets the division_pattern of this ConditionSelectPattern.

        :return: The division_pattern of this ConditionSelectPattern.
        :rtype: :class:`huaweicloudsdkbssintl.v2.DivisionPattern`
        """
        return self._division_pattern

    @division_pattern.setter
    def division_pattern(self, division_pattern):
        r"""Sets the division_pattern of this ConditionSelectPattern.

        :param division_pattern: The division_pattern of this ConditionSelectPattern.
        :type division_pattern: :class:`huaweicloudsdkbssintl.v2.DivisionPattern`
        """
        self._division_pattern = division_pattern

    def to_dict(self):
        result = {}

        for attr, _ in self.openapi_types.items():
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
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ConditionSelectPattern):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

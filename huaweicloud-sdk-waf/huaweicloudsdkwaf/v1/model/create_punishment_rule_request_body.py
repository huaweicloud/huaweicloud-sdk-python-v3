# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreatePunishmentRuleRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'category': 'str',
        'time_unit': 'str',
        'block_time': 'int',
        'description': 'str'
    }

    attribute_map = {
        'category': 'category',
        'time_unit': 'time_unit',
        'block_time': 'block_time',
        'description': 'description'
    }

    def __init__(self, category=None, time_unit=None, block_time=None, description=None):
        r"""CreatePunishmentRuleRequestBody

        The model defined in huaweicloud sdk

        :param category: **参数解释：** 攻击惩罚类别 **约束限制：** 创建后不可修改，单个类别只能存在一个规则 **取值范围：**  - long_ip_block  - long_cookie_block  - long_params_block  - long_header_block  - short_ip_block  - short_cookie_block  - short_params_block  - short_header_block **默认取值：** 不涉及
        :type category: str
        :param time_unit: **参数解释：** 时间单位，会影响“拦截时间”参数的取值范围 **约束限制：** 不涉及 **取值范围：**  - SECOND  - MINUTE  - HOUR  - DAY  - MONTH **默认取值：** SECOND
        :type time_unit: str
        :param block_time: **参数解释：** 拦截时间 **约束限制：** 取值范围取决于惩罚类别和时间单位 **取值范围：** - short_xxx   - SECOND  [1, 300] - long_xxx   - SECOND [301, 7776000]   - MINUTE [6, 129600]   - HOUR [1, 2160]   - DAY [1, 90]   - MONTH [1, 3] **默认取值：** 不涉及
        :type block_time: int
        :param description: 规则描述
        :type description: str
        """
        
        

        self._category = None
        self._time_unit = None
        self._block_time = None
        self._description = None
        self.discriminator = None

        self.category = category
        if time_unit is not None:
            self.time_unit = time_unit
        self.block_time = block_time
        if description is not None:
            self.description = description

    @property
    def category(self):
        r"""Gets the category of this CreatePunishmentRuleRequestBody.

        **参数解释：** 攻击惩罚类别 **约束限制：** 创建后不可修改，单个类别只能存在一个规则 **取值范围：**  - long_ip_block  - long_cookie_block  - long_params_block  - long_header_block  - short_ip_block  - short_cookie_block  - short_params_block  - short_header_block **默认取值：** 不涉及

        :return: The category of this CreatePunishmentRuleRequestBody.
        :rtype: str
        """
        return self._category

    @category.setter
    def category(self, category):
        r"""Sets the category of this CreatePunishmentRuleRequestBody.

        **参数解释：** 攻击惩罚类别 **约束限制：** 创建后不可修改，单个类别只能存在一个规则 **取值范围：**  - long_ip_block  - long_cookie_block  - long_params_block  - long_header_block  - short_ip_block  - short_cookie_block  - short_params_block  - short_header_block **默认取值：** 不涉及

        :param category: The category of this CreatePunishmentRuleRequestBody.
        :type category: str
        """
        self._category = category

    @property
    def time_unit(self):
        r"""Gets the time_unit of this CreatePunishmentRuleRequestBody.

        **参数解释：** 时间单位，会影响“拦截时间”参数的取值范围 **约束限制：** 不涉及 **取值范围：**  - SECOND  - MINUTE  - HOUR  - DAY  - MONTH **默认取值：** SECOND

        :return: The time_unit of this CreatePunishmentRuleRequestBody.
        :rtype: str
        """
        return self._time_unit

    @time_unit.setter
    def time_unit(self, time_unit):
        r"""Sets the time_unit of this CreatePunishmentRuleRequestBody.

        **参数解释：** 时间单位，会影响“拦截时间”参数的取值范围 **约束限制：** 不涉及 **取值范围：**  - SECOND  - MINUTE  - HOUR  - DAY  - MONTH **默认取值：** SECOND

        :param time_unit: The time_unit of this CreatePunishmentRuleRequestBody.
        :type time_unit: str
        """
        self._time_unit = time_unit

    @property
    def block_time(self):
        r"""Gets the block_time of this CreatePunishmentRuleRequestBody.

        **参数解释：** 拦截时间 **约束限制：** 取值范围取决于惩罚类别和时间单位 **取值范围：** - short_xxx   - SECOND  [1, 300] - long_xxx   - SECOND [301, 7776000]   - MINUTE [6, 129600]   - HOUR [1, 2160]   - DAY [1, 90]   - MONTH [1, 3] **默认取值：** 不涉及

        :return: The block_time of this CreatePunishmentRuleRequestBody.
        :rtype: int
        """
        return self._block_time

    @block_time.setter
    def block_time(self, block_time):
        r"""Sets the block_time of this CreatePunishmentRuleRequestBody.

        **参数解释：** 拦截时间 **约束限制：** 取值范围取决于惩罚类别和时间单位 **取值范围：** - short_xxx   - SECOND  [1, 300] - long_xxx   - SECOND [301, 7776000]   - MINUTE [6, 129600]   - HOUR [1, 2160]   - DAY [1, 90]   - MONTH [1, 3] **默认取值：** 不涉及

        :param block_time: The block_time of this CreatePunishmentRuleRequestBody.
        :type block_time: int
        """
        self._block_time = block_time

    @property
    def description(self):
        r"""Gets the description of this CreatePunishmentRuleRequestBody.

        规则描述

        :return: The description of this CreatePunishmentRuleRequestBody.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this CreatePunishmentRuleRequestBody.

        规则描述

        :param description: The description of this CreatePunishmentRuleRequestBody.
        :type description: str
        """
        self._description = description

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
        if not isinstance(other, CreatePunishmentRuleRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

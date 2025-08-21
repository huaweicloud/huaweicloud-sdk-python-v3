# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AttackReport:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'dst_ip': 'list[ItemVO]',
        'ips_mode': 'int',
        'level': 'list[ItemVO]',
        'rule': 'list[ItemVO]',
        'src_ip': 'list[ItemVO]',
        'trend': 'list[TrendVO]',
        'type': 'list[ItemVO]'
    }

    attribute_map = {
        'dst_ip': 'dst_ip',
        'ips_mode': 'ips_mode',
        'level': 'level',
        'rule': 'rule',
        'src_ip': 'src_ip',
        'trend': 'trend',
        'type': 'type'
    }

    def __init__(self, dst_ip=None, ips_mode=None, level=None, rule=None, src_ip=None, trend=None, type=None):
        r"""AttackReport

        The model defined in huaweicloud sdk

        :param dst_ip: **参数解释**： TOP攻击目的IP **取值范围**： 不涉及
        :type dst_ip: list[:class:`huaweicloudsdkcfw.v1.ItemVO`]
        :param ips_mode: **参数解释**： 入侵防御状态 **取值范围**： 不涉及
        :type ips_mode: int
        :param level: **参数解释**： 攻击等级分布 **取值范围**： 不涉及
        :type level: list[:class:`huaweicloudsdkcfw.v1.ItemVO`]
        :param rule: **参数解释**： TOP攻击规则 **取值范围**： 不涉及
        :type rule: list[:class:`huaweicloudsdkcfw.v1.ItemVO`]
        :param src_ip: **参数解释**： TOP来源IP **取值范围**： 不涉及
        :type src_ip: list[:class:`huaweicloudsdkcfw.v1.ItemVO`]
        :param trend: **参数解释**： 攻击趋势 **取值范围**： 不涉及
        :type trend: list[:class:`huaweicloudsdkcfw.v1.TrendVO`]
        :param type: **参数解释**： TOP攻击分布 **取值范围**： 不涉及
        :type type: list[:class:`huaweicloudsdkcfw.v1.ItemVO`]
        """
        
        

        self._dst_ip = None
        self._ips_mode = None
        self._level = None
        self._rule = None
        self._src_ip = None
        self._trend = None
        self._type = None
        self.discriminator = None

        if dst_ip is not None:
            self.dst_ip = dst_ip
        if ips_mode is not None:
            self.ips_mode = ips_mode
        if level is not None:
            self.level = level
        if rule is not None:
            self.rule = rule
        if src_ip is not None:
            self.src_ip = src_ip
        if trend is not None:
            self.trend = trend
        if type is not None:
            self.type = type

    @property
    def dst_ip(self):
        r"""Gets the dst_ip of this AttackReport.

        **参数解释**： TOP攻击目的IP **取值范围**： 不涉及

        :return: The dst_ip of this AttackReport.
        :rtype: list[:class:`huaweicloudsdkcfw.v1.ItemVO`]
        """
        return self._dst_ip

    @dst_ip.setter
    def dst_ip(self, dst_ip):
        r"""Sets the dst_ip of this AttackReport.

        **参数解释**： TOP攻击目的IP **取值范围**： 不涉及

        :param dst_ip: The dst_ip of this AttackReport.
        :type dst_ip: list[:class:`huaweicloudsdkcfw.v1.ItemVO`]
        """
        self._dst_ip = dst_ip

    @property
    def ips_mode(self):
        r"""Gets the ips_mode of this AttackReport.

        **参数解释**： 入侵防御状态 **取值范围**： 不涉及

        :return: The ips_mode of this AttackReport.
        :rtype: int
        """
        return self._ips_mode

    @ips_mode.setter
    def ips_mode(self, ips_mode):
        r"""Sets the ips_mode of this AttackReport.

        **参数解释**： 入侵防御状态 **取值范围**： 不涉及

        :param ips_mode: The ips_mode of this AttackReport.
        :type ips_mode: int
        """
        self._ips_mode = ips_mode

    @property
    def level(self):
        r"""Gets the level of this AttackReport.

        **参数解释**： 攻击等级分布 **取值范围**： 不涉及

        :return: The level of this AttackReport.
        :rtype: list[:class:`huaweicloudsdkcfw.v1.ItemVO`]
        """
        return self._level

    @level.setter
    def level(self, level):
        r"""Sets the level of this AttackReport.

        **参数解释**： 攻击等级分布 **取值范围**： 不涉及

        :param level: The level of this AttackReport.
        :type level: list[:class:`huaweicloudsdkcfw.v1.ItemVO`]
        """
        self._level = level

    @property
    def rule(self):
        r"""Gets the rule of this AttackReport.

        **参数解释**： TOP攻击规则 **取值范围**： 不涉及

        :return: The rule of this AttackReport.
        :rtype: list[:class:`huaweicloudsdkcfw.v1.ItemVO`]
        """
        return self._rule

    @rule.setter
    def rule(self, rule):
        r"""Sets the rule of this AttackReport.

        **参数解释**： TOP攻击规则 **取值范围**： 不涉及

        :param rule: The rule of this AttackReport.
        :type rule: list[:class:`huaweicloudsdkcfw.v1.ItemVO`]
        """
        self._rule = rule

    @property
    def src_ip(self):
        r"""Gets the src_ip of this AttackReport.

        **参数解释**： TOP来源IP **取值范围**： 不涉及

        :return: The src_ip of this AttackReport.
        :rtype: list[:class:`huaweicloudsdkcfw.v1.ItemVO`]
        """
        return self._src_ip

    @src_ip.setter
    def src_ip(self, src_ip):
        r"""Sets the src_ip of this AttackReport.

        **参数解释**： TOP来源IP **取值范围**： 不涉及

        :param src_ip: The src_ip of this AttackReport.
        :type src_ip: list[:class:`huaweicloudsdkcfw.v1.ItemVO`]
        """
        self._src_ip = src_ip

    @property
    def trend(self):
        r"""Gets the trend of this AttackReport.

        **参数解释**： 攻击趋势 **取值范围**： 不涉及

        :return: The trend of this AttackReport.
        :rtype: list[:class:`huaweicloudsdkcfw.v1.TrendVO`]
        """
        return self._trend

    @trend.setter
    def trend(self, trend):
        r"""Sets the trend of this AttackReport.

        **参数解释**： 攻击趋势 **取值范围**： 不涉及

        :param trend: The trend of this AttackReport.
        :type trend: list[:class:`huaweicloudsdkcfw.v1.TrendVO`]
        """
        self._trend = trend

    @property
    def type(self):
        r"""Gets the type of this AttackReport.

        **参数解释**： TOP攻击分布 **取值范围**： 不涉及

        :return: The type of this AttackReport.
        :rtype: list[:class:`huaweicloudsdkcfw.v1.ItemVO`]
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this AttackReport.

        **参数解释**： TOP攻击分布 **取值范围**： 不涉及

        :param type: The type of this AttackReport.
        :type type: list[:class:`huaweicloudsdkcfw.v1.ItemVO`]
        """
        self._type = type

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
        if not isinstance(other, AttackReport):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AttackDetailVO:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'app_count': 'int',
        'attack_rule_count': 'int',
        'attack_type_count': 'int',
        'count': 'int',
        'dst_ip_count': 'int',
        'dst_port_count': 'int',
        'end_time': 'int',
        'records': 'list[AttackLog]',
        'src_ip_count': 'int',
        'start_time': 'int',
        'total': 'int'
    }

    attribute_map = {
        'app_count': 'app_count',
        'attack_rule_count': 'attack_rule_count',
        'attack_type_count': 'attack_type_count',
        'count': 'count',
        'dst_ip_count': 'dst_ip_count',
        'dst_port_count': 'dst_port_count',
        'end_time': 'end_time',
        'records': 'records',
        'src_ip_count': 'src_ip_count',
        'start_time': 'start_time',
        'total': 'total'
    }

    def __init__(self, app_count=None, attack_rule_count=None, attack_type_count=None, count=None, dst_ip_count=None, dst_port_count=None, end_time=None, records=None, src_ip_count=None, start_time=None, total=None):
        r"""AttackDetailVO

        The model defined in huaweicloud sdk

        :param app_count: **参数解释**： 应用数量 **取值范围**： 不涉及
        :type app_count: int
        :param attack_rule_count: **参数解释**： 攻击规则数量 **取值范围**： 不涉及
        :type attack_rule_count: int
        :param attack_type_count: **参数解释**： 攻击类型数量 **取值范围**： 不涉及
        :type attack_type_count: int
        :param count: **参数解释**： 攻击次数 **取值范围**： 不涉及
        :type count: int
        :param dst_ip_count: **参数解释**： 目的IP数量 **取值范围**： 不涉及
        :type dst_ip_count: int
        :param dst_port_count: **参数解释**： 攻击端口数量 **取值范围**： 不涉及
        :type dst_port_count: int
        :param end_time: **参数解释**： 结束时间 **取值范围**： 不涉及
        :type end_time: int
        :param records: **参数解释**： 攻击事件明细 **取值范围**： 不涉及
        :type records: list[:class:`huaweicloudsdkcfw.v1.AttackLog`]
        :param src_ip_count: **参数解释**： 源IP数量 **取值范围**： 不涉及
        :type src_ip_count: int
        :param start_time: **参数解释**： 开始时间 **取值范围**： 不涉及
        :type start_time: int
        :param total: **参数解释**： 总数 **取值范围**： 不涉及
        :type total: int
        """
        
        

        self._app_count = None
        self._attack_rule_count = None
        self._attack_type_count = None
        self._count = None
        self._dst_ip_count = None
        self._dst_port_count = None
        self._end_time = None
        self._records = None
        self._src_ip_count = None
        self._start_time = None
        self._total = None
        self.discriminator = None

        if app_count is not None:
            self.app_count = app_count
        if attack_rule_count is not None:
            self.attack_rule_count = attack_rule_count
        if attack_type_count is not None:
            self.attack_type_count = attack_type_count
        if count is not None:
            self.count = count
        if dst_ip_count is not None:
            self.dst_ip_count = dst_ip_count
        if dst_port_count is not None:
            self.dst_port_count = dst_port_count
        if end_time is not None:
            self.end_time = end_time
        if records is not None:
            self.records = records
        if src_ip_count is not None:
            self.src_ip_count = src_ip_count
        if start_time is not None:
            self.start_time = start_time
        if total is not None:
            self.total = total

    @property
    def app_count(self):
        r"""Gets the app_count of this AttackDetailVO.

        **参数解释**： 应用数量 **取值范围**： 不涉及

        :return: The app_count of this AttackDetailVO.
        :rtype: int
        """
        return self._app_count

    @app_count.setter
    def app_count(self, app_count):
        r"""Sets the app_count of this AttackDetailVO.

        **参数解释**： 应用数量 **取值范围**： 不涉及

        :param app_count: The app_count of this AttackDetailVO.
        :type app_count: int
        """
        self._app_count = app_count

    @property
    def attack_rule_count(self):
        r"""Gets the attack_rule_count of this AttackDetailVO.

        **参数解释**： 攻击规则数量 **取值范围**： 不涉及

        :return: The attack_rule_count of this AttackDetailVO.
        :rtype: int
        """
        return self._attack_rule_count

    @attack_rule_count.setter
    def attack_rule_count(self, attack_rule_count):
        r"""Sets the attack_rule_count of this AttackDetailVO.

        **参数解释**： 攻击规则数量 **取值范围**： 不涉及

        :param attack_rule_count: The attack_rule_count of this AttackDetailVO.
        :type attack_rule_count: int
        """
        self._attack_rule_count = attack_rule_count

    @property
    def attack_type_count(self):
        r"""Gets the attack_type_count of this AttackDetailVO.

        **参数解释**： 攻击类型数量 **取值范围**： 不涉及

        :return: The attack_type_count of this AttackDetailVO.
        :rtype: int
        """
        return self._attack_type_count

    @attack_type_count.setter
    def attack_type_count(self, attack_type_count):
        r"""Sets the attack_type_count of this AttackDetailVO.

        **参数解释**： 攻击类型数量 **取值范围**： 不涉及

        :param attack_type_count: The attack_type_count of this AttackDetailVO.
        :type attack_type_count: int
        """
        self._attack_type_count = attack_type_count

    @property
    def count(self):
        r"""Gets the count of this AttackDetailVO.

        **参数解释**： 攻击次数 **取值范围**： 不涉及

        :return: The count of this AttackDetailVO.
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        r"""Sets the count of this AttackDetailVO.

        **参数解释**： 攻击次数 **取值范围**： 不涉及

        :param count: The count of this AttackDetailVO.
        :type count: int
        """
        self._count = count

    @property
    def dst_ip_count(self):
        r"""Gets the dst_ip_count of this AttackDetailVO.

        **参数解释**： 目的IP数量 **取值范围**： 不涉及

        :return: The dst_ip_count of this AttackDetailVO.
        :rtype: int
        """
        return self._dst_ip_count

    @dst_ip_count.setter
    def dst_ip_count(self, dst_ip_count):
        r"""Sets the dst_ip_count of this AttackDetailVO.

        **参数解释**： 目的IP数量 **取值范围**： 不涉及

        :param dst_ip_count: The dst_ip_count of this AttackDetailVO.
        :type dst_ip_count: int
        """
        self._dst_ip_count = dst_ip_count

    @property
    def dst_port_count(self):
        r"""Gets the dst_port_count of this AttackDetailVO.

        **参数解释**： 攻击端口数量 **取值范围**： 不涉及

        :return: The dst_port_count of this AttackDetailVO.
        :rtype: int
        """
        return self._dst_port_count

    @dst_port_count.setter
    def dst_port_count(self, dst_port_count):
        r"""Sets the dst_port_count of this AttackDetailVO.

        **参数解释**： 攻击端口数量 **取值范围**： 不涉及

        :param dst_port_count: The dst_port_count of this AttackDetailVO.
        :type dst_port_count: int
        """
        self._dst_port_count = dst_port_count

    @property
    def end_time(self):
        r"""Gets the end_time of this AttackDetailVO.

        **参数解释**： 结束时间 **取值范围**： 不涉及

        :return: The end_time of this AttackDetailVO.
        :rtype: int
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        r"""Sets the end_time of this AttackDetailVO.

        **参数解释**： 结束时间 **取值范围**： 不涉及

        :param end_time: The end_time of this AttackDetailVO.
        :type end_time: int
        """
        self._end_time = end_time

    @property
    def records(self):
        r"""Gets the records of this AttackDetailVO.

        **参数解释**： 攻击事件明细 **取值范围**： 不涉及

        :return: The records of this AttackDetailVO.
        :rtype: list[:class:`huaweicloudsdkcfw.v1.AttackLog`]
        """
        return self._records

    @records.setter
    def records(self, records):
        r"""Sets the records of this AttackDetailVO.

        **参数解释**： 攻击事件明细 **取值范围**： 不涉及

        :param records: The records of this AttackDetailVO.
        :type records: list[:class:`huaweicloudsdkcfw.v1.AttackLog`]
        """
        self._records = records

    @property
    def src_ip_count(self):
        r"""Gets the src_ip_count of this AttackDetailVO.

        **参数解释**： 源IP数量 **取值范围**： 不涉及

        :return: The src_ip_count of this AttackDetailVO.
        :rtype: int
        """
        return self._src_ip_count

    @src_ip_count.setter
    def src_ip_count(self, src_ip_count):
        r"""Sets the src_ip_count of this AttackDetailVO.

        **参数解释**： 源IP数量 **取值范围**： 不涉及

        :param src_ip_count: The src_ip_count of this AttackDetailVO.
        :type src_ip_count: int
        """
        self._src_ip_count = src_ip_count

    @property
    def start_time(self):
        r"""Gets the start_time of this AttackDetailVO.

        **参数解释**： 开始时间 **取值范围**： 不涉及

        :return: The start_time of this AttackDetailVO.
        :rtype: int
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        r"""Sets the start_time of this AttackDetailVO.

        **参数解释**： 开始时间 **取值范围**： 不涉及

        :param start_time: The start_time of this AttackDetailVO.
        :type start_time: int
        """
        self._start_time = start_time

    @property
    def total(self):
        r"""Gets the total of this AttackDetailVO.

        **参数解释**： 总数 **取值范围**： 不涉及

        :return: The total of this AttackDetailVO.
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        r"""Sets the total of this AttackDetailVO.

        **参数解释**： 总数 **取值范围**： 不涉及

        :param total: The total of this AttackDetailVO.
        :type total: int
        """
        self._total = total

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
        if not isinstance(other, AttackDetailVO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

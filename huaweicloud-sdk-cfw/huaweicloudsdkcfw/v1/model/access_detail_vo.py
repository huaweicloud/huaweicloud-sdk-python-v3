# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AccessDetailVO:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'dst_ip_count': 'int',
        'dst_port_count': 'int',
        'hit_count': 'int',
        'protocol_count': 'int',
        'recent_end_time': 'int',
        'recent_start_time': 'int',
        'record_total': 'int',
        'records': 'list[AccessLogInfo]',
        'rule_hit_count': 'int',
        'src_ip_count': 'int'
    }

    attribute_map = {
        'dst_ip_count': 'dst_ip_count',
        'dst_port_count': 'dst_port_count',
        'hit_count': 'hit_count',
        'protocol_count': 'protocol_count',
        'recent_end_time': 'recent_end_time',
        'recent_start_time': 'recent_start_time',
        'record_total': 'record_total',
        'records': 'records',
        'rule_hit_count': 'rule_hit_count',
        'src_ip_count': 'src_ip_count'
    }

    def __init__(self, dst_ip_count=None, dst_port_count=None, hit_count=None, protocol_count=None, recent_end_time=None, recent_start_time=None, record_total=None, records=None, rule_hit_count=None, src_ip_count=None):
        r"""AccessDetailVO

        The model defined in huaweicloud sdk

        :param dst_ip_count: **参数解释**： 目的IP数量 **取值范围**： 不涉及
        :type dst_ip_count: int
        :param dst_port_count: **参数解释**： 目的端口数量 **取值范围**： 不涉及
        :type dst_port_count: int
        :param hit_count: **参数解释**： 命中次数 **取值范围**： 不涉及
        :type hit_count: int
        :param protocol_count: **参数解释**： 协议数量 **取值范围**： 不涉及
        :type protocol_count: int
        :param recent_end_time: **参数解释**： 结束时间 **取值范围**： 不涉及
        :type recent_end_time: int
        :param recent_start_time: **参数解释**： 开始时间 **取值范围**： 不涉及
        :type recent_start_time: int
        :param record_total: **参数解释**： 记录数量 **取值范围**： 不涉及
        :type record_total: int
        :param records: **参数解释**： 命中详情 **取值范围**： 不涉及
        :type records: list[:class:`huaweicloudsdkcfw.v1.AccessLogInfo`]
        :param rule_hit_count: **参数解释**： 命中规则数 **取值范围**： 不涉及
        :type rule_hit_count: int
        :param src_ip_count: **参数解释**： 源IP数量 **取值范围**： 不涉及
        :type src_ip_count: int
        """
        
        

        self._dst_ip_count = None
        self._dst_port_count = None
        self._hit_count = None
        self._protocol_count = None
        self._recent_end_time = None
        self._recent_start_time = None
        self._record_total = None
        self._records = None
        self._rule_hit_count = None
        self._src_ip_count = None
        self.discriminator = None

        if dst_ip_count is not None:
            self.dst_ip_count = dst_ip_count
        if dst_port_count is not None:
            self.dst_port_count = dst_port_count
        if hit_count is not None:
            self.hit_count = hit_count
        if protocol_count is not None:
            self.protocol_count = protocol_count
        if recent_end_time is not None:
            self.recent_end_time = recent_end_time
        if recent_start_time is not None:
            self.recent_start_time = recent_start_time
        if record_total is not None:
            self.record_total = record_total
        if records is not None:
            self.records = records
        if rule_hit_count is not None:
            self.rule_hit_count = rule_hit_count
        if src_ip_count is not None:
            self.src_ip_count = src_ip_count

    @property
    def dst_ip_count(self):
        r"""Gets the dst_ip_count of this AccessDetailVO.

        **参数解释**： 目的IP数量 **取值范围**： 不涉及

        :return: The dst_ip_count of this AccessDetailVO.
        :rtype: int
        """
        return self._dst_ip_count

    @dst_ip_count.setter
    def dst_ip_count(self, dst_ip_count):
        r"""Sets the dst_ip_count of this AccessDetailVO.

        **参数解释**： 目的IP数量 **取值范围**： 不涉及

        :param dst_ip_count: The dst_ip_count of this AccessDetailVO.
        :type dst_ip_count: int
        """
        self._dst_ip_count = dst_ip_count

    @property
    def dst_port_count(self):
        r"""Gets the dst_port_count of this AccessDetailVO.

        **参数解释**： 目的端口数量 **取值范围**： 不涉及

        :return: The dst_port_count of this AccessDetailVO.
        :rtype: int
        """
        return self._dst_port_count

    @dst_port_count.setter
    def dst_port_count(self, dst_port_count):
        r"""Sets the dst_port_count of this AccessDetailVO.

        **参数解释**： 目的端口数量 **取值范围**： 不涉及

        :param dst_port_count: The dst_port_count of this AccessDetailVO.
        :type dst_port_count: int
        """
        self._dst_port_count = dst_port_count

    @property
    def hit_count(self):
        r"""Gets the hit_count of this AccessDetailVO.

        **参数解释**： 命中次数 **取值范围**： 不涉及

        :return: The hit_count of this AccessDetailVO.
        :rtype: int
        """
        return self._hit_count

    @hit_count.setter
    def hit_count(self, hit_count):
        r"""Sets the hit_count of this AccessDetailVO.

        **参数解释**： 命中次数 **取值范围**： 不涉及

        :param hit_count: The hit_count of this AccessDetailVO.
        :type hit_count: int
        """
        self._hit_count = hit_count

    @property
    def protocol_count(self):
        r"""Gets the protocol_count of this AccessDetailVO.

        **参数解释**： 协议数量 **取值范围**： 不涉及

        :return: The protocol_count of this AccessDetailVO.
        :rtype: int
        """
        return self._protocol_count

    @protocol_count.setter
    def protocol_count(self, protocol_count):
        r"""Sets the protocol_count of this AccessDetailVO.

        **参数解释**： 协议数量 **取值范围**： 不涉及

        :param protocol_count: The protocol_count of this AccessDetailVO.
        :type protocol_count: int
        """
        self._protocol_count = protocol_count

    @property
    def recent_end_time(self):
        r"""Gets the recent_end_time of this AccessDetailVO.

        **参数解释**： 结束时间 **取值范围**： 不涉及

        :return: The recent_end_time of this AccessDetailVO.
        :rtype: int
        """
        return self._recent_end_time

    @recent_end_time.setter
    def recent_end_time(self, recent_end_time):
        r"""Sets the recent_end_time of this AccessDetailVO.

        **参数解释**： 结束时间 **取值范围**： 不涉及

        :param recent_end_time: The recent_end_time of this AccessDetailVO.
        :type recent_end_time: int
        """
        self._recent_end_time = recent_end_time

    @property
    def recent_start_time(self):
        r"""Gets the recent_start_time of this AccessDetailVO.

        **参数解释**： 开始时间 **取值范围**： 不涉及

        :return: The recent_start_time of this AccessDetailVO.
        :rtype: int
        """
        return self._recent_start_time

    @recent_start_time.setter
    def recent_start_time(self, recent_start_time):
        r"""Sets the recent_start_time of this AccessDetailVO.

        **参数解释**： 开始时间 **取值范围**： 不涉及

        :param recent_start_time: The recent_start_time of this AccessDetailVO.
        :type recent_start_time: int
        """
        self._recent_start_time = recent_start_time

    @property
    def record_total(self):
        r"""Gets the record_total of this AccessDetailVO.

        **参数解释**： 记录数量 **取值范围**： 不涉及

        :return: The record_total of this AccessDetailVO.
        :rtype: int
        """
        return self._record_total

    @record_total.setter
    def record_total(self, record_total):
        r"""Sets the record_total of this AccessDetailVO.

        **参数解释**： 记录数量 **取值范围**： 不涉及

        :param record_total: The record_total of this AccessDetailVO.
        :type record_total: int
        """
        self._record_total = record_total

    @property
    def records(self):
        r"""Gets the records of this AccessDetailVO.

        **参数解释**： 命中详情 **取值范围**： 不涉及

        :return: The records of this AccessDetailVO.
        :rtype: list[:class:`huaweicloudsdkcfw.v1.AccessLogInfo`]
        """
        return self._records

    @records.setter
    def records(self, records):
        r"""Sets the records of this AccessDetailVO.

        **参数解释**： 命中详情 **取值范围**： 不涉及

        :param records: The records of this AccessDetailVO.
        :type records: list[:class:`huaweicloudsdkcfw.v1.AccessLogInfo`]
        """
        self._records = records

    @property
    def rule_hit_count(self):
        r"""Gets the rule_hit_count of this AccessDetailVO.

        **参数解释**： 命中规则数 **取值范围**： 不涉及

        :return: The rule_hit_count of this AccessDetailVO.
        :rtype: int
        """
        return self._rule_hit_count

    @rule_hit_count.setter
    def rule_hit_count(self, rule_hit_count):
        r"""Sets the rule_hit_count of this AccessDetailVO.

        **参数解释**： 命中规则数 **取值范围**： 不涉及

        :param rule_hit_count: The rule_hit_count of this AccessDetailVO.
        :type rule_hit_count: int
        """
        self._rule_hit_count = rule_hit_count

    @property
    def src_ip_count(self):
        r"""Gets the src_ip_count of this AccessDetailVO.

        **参数解释**： 源IP数量 **取值范围**： 不涉及

        :return: The src_ip_count of this AccessDetailVO.
        :rtype: int
        """
        return self._src_ip_count

    @src_ip_count.setter
    def src_ip_count(self, src_ip_count):
        r"""Sets the src_ip_count of this AccessDetailVO.

        **参数解释**： 源IP数量 **取值范围**： 不涉及

        :param src_ip_count: The src_ip_count of this AccessDetailVO.
        :type src_ip_count: int
        """
        self._src_ip_count = src_ip_count

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
        if not isinstance(other, AccessDetailVO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

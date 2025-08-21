# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AttackTopRespBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'attack_rule': 'list[TopInfo]',
        'attack_type': 'list[TopInfo]',
        'dst_ip': 'list[TopInfo]',
        'dst_port': 'list[TopInfo]',
        'in_src_ip': 'list[TopInfo]',
        'level': 'list[TopInfo]',
        'out_src_ip': 'list[TopInfo]',
        'src_ip': 'list[TopInfo]',
        'src_region_id': 'list[TopInfo]'
    }

    attribute_map = {
        'attack_rule': 'attack_rule',
        'attack_type': 'attack_type',
        'dst_ip': 'dst_ip',
        'dst_port': 'dst_port',
        'in_src_ip': 'in_src_ip',
        'level': 'level',
        'out_src_ip': 'out_src_ip',
        'src_ip': 'src_ip',
        'src_region_id': 'src_region_id'
    }

    def __init__(self, attack_rule=None, attack_type=None, dst_ip=None, dst_port=None, in_src_ip=None, level=None, out_src_ip=None, src_ip=None, src_region_id=None):
        r"""AttackTopRespBody

        The model defined in huaweicloud sdk

        :param attack_rule: **参数解释**： TOP攻击规则 **取值范围**： 不涉及
        :type attack_rule: list[:class:`huaweicloudsdkcfw.v1.TopInfo`]
        :param attack_type: **参数解释**： TOP攻击类型 **取值范围**： 不涉及
        :type attack_type: list[:class:`huaweicloudsdkcfw.v1.TopInfo`]
        :param dst_ip: **参数解释**： TOP攻击目的IP **取值范围**： 不涉及
        :type dst_ip: list[:class:`huaweicloudsdkcfw.v1.TopInfo`]
        :param dst_port: **参数解释**： TOP被攻击端口 **取值范围**： 不涉及
        :type dst_port: list[:class:`huaweicloudsdkcfw.v1.TopInfo`]
        :param in_src_ip: **参数解释**： TOP内部攻击来源IP **取值范围**： 不涉及
        :type in_src_ip: list[:class:`huaweicloudsdkcfw.v1.TopInfo`]
        :param level: **参数解释**： TOP威胁等级 **取值范围**： 不涉及
        :type level: list[:class:`huaweicloudsdkcfw.v1.TopInfo`]
        :param out_src_ip: **参数解释**： TOP外部攻击来源IP **取值范围**： 不涉及
        :type out_src_ip: list[:class:`huaweicloudsdkcfw.v1.TopInfo`]
        :param src_ip: **参数解释**： TOP攻击来源IP **取值范围**： 不涉及
        :type src_ip: list[:class:`huaweicloudsdkcfw.v1.TopInfo`]
        :param src_region_id: **参数解释**： 源地区ID **取值范围**： 不涉及
        :type src_region_id: list[:class:`huaweicloudsdkcfw.v1.TopInfo`]
        """
        
        

        self._attack_rule = None
        self._attack_type = None
        self._dst_ip = None
        self._dst_port = None
        self._in_src_ip = None
        self._level = None
        self._out_src_ip = None
        self._src_ip = None
        self._src_region_id = None
        self.discriminator = None

        if attack_rule is not None:
            self.attack_rule = attack_rule
        if attack_type is not None:
            self.attack_type = attack_type
        if dst_ip is not None:
            self.dst_ip = dst_ip
        if dst_port is not None:
            self.dst_port = dst_port
        if in_src_ip is not None:
            self.in_src_ip = in_src_ip
        if level is not None:
            self.level = level
        if out_src_ip is not None:
            self.out_src_ip = out_src_ip
        if src_ip is not None:
            self.src_ip = src_ip
        if src_region_id is not None:
            self.src_region_id = src_region_id

    @property
    def attack_rule(self):
        r"""Gets the attack_rule of this AttackTopRespBody.

        **参数解释**： TOP攻击规则 **取值范围**： 不涉及

        :return: The attack_rule of this AttackTopRespBody.
        :rtype: list[:class:`huaweicloudsdkcfw.v1.TopInfo`]
        """
        return self._attack_rule

    @attack_rule.setter
    def attack_rule(self, attack_rule):
        r"""Sets the attack_rule of this AttackTopRespBody.

        **参数解释**： TOP攻击规则 **取值范围**： 不涉及

        :param attack_rule: The attack_rule of this AttackTopRespBody.
        :type attack_rule: list[:class:`huaweicloudsdkcfw.v1.TopInfo`]
        """
        self._attack_rule = attack_rule

    @property
    def attack_type(self):
        r"""Gets the attack_type of this AttackTopRespBody.

        **参数解释**： TOP攻击类型 **取值范围**： 不涉及

        :return: The attack_type of this AttackTopRespBody.
        :rtype: list[:class:`huaweicloudsdkcfw.v1.TopInfo`]
        """
        return self._attack_type

    @attack_type.setter
    def attack_type(self, attack_type):
        r"""Sets the attack_type of this AttackTopRespBody.

        **参数解释**： TOP攻击类型 **取值范围**： 不涉及

        :param attack_type: The attack_type of this AttackTopRespBody.
        :type attack_type: list[:class:`huaweicloudsdkcfw.v1.TopInfo`]
        """
        self._attack_type = attack_type

    @property
    def dst_ip(self):
        r"""Gets the dst_ip of this AttackTopRespBody.

        **参数解释**： TOP攻击目的IP **取值范围**： 不涉及

        :return: The dst_ip of this AttackTopRespBody.
        :rtype: list[:class:`huaweicloudsdkcfw.v1.TopInfo`]
        """
        return self._dst_ip

    @dst_ip.setter
    def dst_ip(self, dst_ip):
        r"""Sets the dst_ip of this AttackTopRespBody.

        **参数解释**： TOP攻击目的IP **取值范围**： 不涉及

        :param dst_ip: The dst_ip of this AttackTopRespBody.
        :type dst_ip: list[:class:`huaweicloudsdkcfw.v1.TopInfo`]
        """
        self._dst_ip = dst_ip

    @property
    def dst_port(self):
        r"""Gets the dst_port of this AttackTopRespBody.

        **参数解释**： TOP被攻击端口 **取值范围**： 不涉及

        :return: The dst_port of this AttackTopRespBody.
        :rtype: list[:class:`huaweicloudsdkcfw.v1.TopInfo`]
        """
        return self._dst_port

    @dst_port.setter
    def dst_port(self, dst_port):
        r"""Sets the dst_port of this AttackTopRespBody.

        **参数解释**： TOP被攻击端口 **取值范围**： 不涉及

        :param dst_port: The dst_port of this AttackTopRespBody.
        :type dst_port: list[:class:`huaweicloudsdkcfw.v1.TopInfo`]
        """
        self._dst_port = dst_port

    @property
    def in_src_ip(self):
        r"""Gets the in_src_ip of this AttackTopRespBody.

        **参数解释**： TOP内部攻击来源IP **取值范围**： 不涉及

        :return: The in_src_ip of this AttackTopRespBody.
        :rtype: list[:class:`huaweicloudsdkcfw.v1.TopInfo`]
        """
        return self._in_src_ip

    @in_src_ip.setter
    def in_src_ip(self, in_src_ip):
        r"""Sets the in_src_ip of this AttackTopRespBody.

        **参数解释**： TOP内部攻击来源IP **取值范围**： 不涉及

        :param in_src_ip: The in_src_ip of this AttackTopRespBody.
        :type in_src_ip: list[:class:`huaweicloudsdkcfw.v1.TopInfo`]
        """
        self._in_src_ip = in_src_ip

    @property
    def level(self):
        r"""Gets the level of this AttackTopRespBody.

        **参数解释**： TOP威胁等级 **取值范围**： 不涉及

        :return: The level of this AttackTopRespBody.
        :rtype: list[:class:`huaweicloudsdkcfw.v1.TopInfo`]
        """
        return self._level

    @level.setter
    def level(self, level):
        r"""Sets the level of this AttackTopRespBody.

        **参数解释**： TOP威胁等级 **取值范围**： 不涉及

        :param level: The level of this AttackTopRespBody.
        :type level: list[:class:`huaweicloudsdkcfw.v1.TopInfo`]
        """
        self._level = level

    @property
    def out_src_ip(self):
        r"""Gets the out_src_ip of this AttackTopRespBody.

        **参数解释**： TOP外部攻击来源IP **取值范围**： 不涉及

        :return: The out_src_ip of this AttackTopRespBody.
        :rtype: list[:class:`huaweicloudsdkcfw.v1.TopInfo`]
        """
        return self._out_src_ip

    @out_src_ip.setter
    def out_src_ip(self, out_src_ip):
        r"""Sets the out_src_ip of this AttackTopRespBody.

        **参数解释**： TOP外部攻击来源IP **取值范围**： 不涉及

        :param out_src_ip: The out_src_ip of this AttackTopRespBody.
        :type out_src_ip: list[:class:`huaweicloudsdkcfw.v1.TopInfo`]
        """
        self._out_src_ip = out_src_ip

    @property
    def src_ip(self):
        r"""Gets the src_ip of this AttackTopRespBody.

        **参数解释**： TOP攻击来源IP **取值范围**： 不涉及

        :return: The src_ip of this AttackTopRespBody.
        :rtype: list[:class:`huaweicloudsdkcfw.v1.TopInfo`]
        """
        return self._src_ip

    @src_ip.setter
    def src_ip(self, src_ip):
        r"""Sets the src_ip of this AttackTopRespBody.

        **参数解释**： TOP攻击来源IP **取值范围**： 不涉及

        :param src_ip: The src_ip of this AttackTopRespBody.
        :type src_ip: list[:class:`huaweicloudsdkcfw.v1.TopInfo`]
        """
        self._src_ip = src_ip

    @property
    def src_region_id(self):
        r"""Gets the src_region_id of this AttackTopRespBody.

        **参数解释**： 源地区ID **取值范围**： 不涉及

        :return: The src_region_id of this AttackTopRespBody.
        :rtype: list[:class:`huaweicloudsdkcfw.v1.TopInfo`]
        """
        return self._src_region_id

    @src_region_id.setter
    def src_region_id(self, src_region_id):
        r"""Sets the src_region_id of this AttackTopRespBody.

        **参数解释**： 源地区ID **取值范围**： 不涉及

        :param src_region_id: The src_region_id of this AttackTopRespBody.
        :type src_region_id: list[:class:`huaweicloudsdkcfw.v1.TopInfo`]
        """
        self._src_region_id = src_region_id

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
        if not isinstance(other, AttackTopRespBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

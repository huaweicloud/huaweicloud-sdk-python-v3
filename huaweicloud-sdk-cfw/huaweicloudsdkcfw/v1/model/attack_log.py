# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AttackLog:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'action': 'str',
        'app': 'str',
        'attack_rule': 'str',
        'attack_rule_id': 'str',
        'attack_type': 'str',
        'direction': 'str',
        'dst_ip': 'str',
        'dst_port': 'int',
        'dst_region_id': 'str',
        'dst_region_name': 'str',
        'dst_province_id': 'str',
        'dst_province_name': 'str',
        'dst_city_id': 'str',
        'dst_city_name': 'str',
        'event_time': 'int',
        'level': 'str',
        'protocol': 'str',
        'source': 'str',
        'src_ip': 'str',
        'real_ip': 'str',
        'tag': 'int',
        'src_port': 'int',
        'src_region_id': 'str',
        'src_region_name': 'str',
        'src_province_id': 'str',
        'src_province_name': 'str',
        'src_city_id': 'str',
        'src_city_name': 'str',
        'vgw_id': 'str'
    }

    attribute_map = {
        'action': 'action',
        'app': 'app',
        'attack_rule': 'attack_rule',
        'attack_rule_id': 'attack_rule_id',
        'attack_type': 'attack_type',
        'direction': 'direction',
        'dst_ip': 'dst_ip',
        'dst_port': 'dst_port',
        'dst_region_id': 'dst_region_id',
        'dst_region_name': 'dst_region_name',
        'dst_province_id': 'dst_province_id',
        'dst_province_name': 'dst_province_name',
        'dst_city_id': 'dst_city_id',
        'dst_city_name': 'dst_city_name',
        'event_time': 'event_time',
        'level': 'level',
        'protocol': 'protocol',
        'source': 'source',
        'src_ip': 'src_ip',
        'real_ip': 'real_ip',
        'tag': 'tag',
        'src_port': 'src_port',
        'src_region_id': 'src_region_id',
        'src_region_name': 'src_region_name',
        'src_province_id': 'src_province_id',
        'src_province_name': 'src_province_name',
        'src_city_id': 'src_city_id',
        'src_city_name': 'src_city_name',
        'vgw_id': 'vgw_id'
    }

    def __init__(self, action=None, app=None, attack_rule=None, attack_rule_id=None, attack_type=None, direction=None, dst_ip=None, dst_port=None, dst_region_id=None, dst_region_name=None, dst_province_id=None, dst_province_name=None, dst_city_id=None, dst_city_name=None, event_time=None, level=None, protocol=None, source=None, src_ip=None, real_ip=None, tag=None, src_port=None, src_region_id=None, src_region_name=None, src_province_id=None, src_province_name=None, src_city_id=None, src_city_name=None, vgw_id=None):
        r"""AttackLog

        The model defined in huaweicloud sdk

        :param action: **参数解释**： 动作 **取值范围**： 不涉及
        :type action: str
        :param app: **参数解释**： 应用 **取值范围**： 不涉及
        :type app: str
        :param attack_rule: **参数解释**： 攻击规则 **取值范围**： 不涉及
        :type attack_rule: str
        :param attack_rule_id: **参数解释**： 攻击规则ID **取值范围**： 不涉及
        :type attack_rule_id: str
        :param attack_type: **参数解释**： 攻击类型 **取值范围**： 不涉及
        :type attack_type: str
        :param direction: **参数解释**： 攻击方向 **取值范围**： 不涉及
        :type direction: str
        :param dst_ip: **参数解释**： 目的IP **取值范围**： 不涉及
        :type dst_ip: str
        :param dst_port: **参数解释**： 目的端口 **取值范围**： 不涉及
        :type dst_port: int
        :param dst_region_id: **参数解释**： 目的地区Id **取值范围**： 不涉及
        :type dst_region_id: str
        :param dst_region_name: **参数解释**： 目的地区名称 **取值范围**： 不涉及
        :type dst_region_name: str
        :param dst_province_id: **参数解释**： 目的省份ID **取值范围**： 不涉及
        :type dst_province_id: str
        :param dst_province_name: **参数解释**： 目的省份名称 **取值范围**： 不涉及
        :type dst_province_name: str
        :param dst_city_id: **参数解释**： 目的城市Id **取值范围**： 不涉及
        :type dst_city_id: str
        :param dst_city_name: **参数解释**： 目的城市名称 **取值范围**： 不涉及
        :type dst_city_name: str
        :param event_time: **参数解释**： 发生时间 **取值范围**： 不涉及
        :type event_time: int
        :param level: **参数解释**： 危险等级 **取值范围**： 不涉及
        :type level: str
        :param protocol: **参数解释**： 协议 **取值范围**： 不涉及
        :type protocol: str
        :param source: **参数解释**： 来源 **取值范围**： 不涉及
        :type source: str
        :param src_ip: **参数解释**： 源IP **取值范围**： 不涉及
        :type src_ip: str
        :param real_ip: **参数解释**： 真实IP **取值范围**： 不涉及
        :type real_ip: str
        :param tag: **参数解释**： 标签 **取值范围**： 不涉及
        :type tag: int
        :param src_port: **参数解释**： 源端口 **取值范围**： 不涉及
        :type src_port: int
        :param src_region_id: **参数解释**： 源地区Id **取值范围**： 不涉及
        :type src_region_id: str
        :param src_region_name: **参数解释**： 源地区名称 **取值范围**： 不涉及
        :type src_region_name: str
        :param src_province_id: **参数解释**： 源省份Id **取值范围**： 不涉及
        :type src_province_id: str
        :param src_province_name: **参数解释**： 源省份名称 **取值范围**： 不涉及
        :type src_province_name: str
        :param src_city_id: **参数解释**： 源城市Id **取值范围**： 不涉及
        :type src_city_id: str
        :param src_city_name: **参数解释**： 源城市 **取值范围**： 不涉及
        :type src_city_name: str
        :param vgw_id: **参数解释**： VGW Id **取值范围**： 不涉及
        :type vgw_id: str
        """
        
        

        self._action = None
        self._app = None
        self._attack_rule = None
        self._attack_rule_id = None
        self._attack_type = None
        self._direction = None
        self._dst_ip = None
        self._dst_port = None
        self._dst_region_id = None
        self._dst_region_name = None
        self._dst_province_id = None
        self._dst_province_name = None
        self._dst_city_id = None
        self._dst_city_name = None
        self._event_time = None
        self._level = None
        self._protocol = None
        self._source = None
        self._src_ip = None
        self._real_ip = None
        self._tag = None
        self._src_port = None
        self._src_region_id = None
        self._src_region_name = None
        self._src_province_id = None
        self._src_province_name = None
        self._src_city_id = None
        self._src_city_name = None
        self._vgw_id = None
        self.discriminator = None

        if action is not None:
            self.action = action
        if app is not None:
            self.app = app
        if attack_rule is not None:
            self.attack_rule = attack_rule
        if attack_rule_id is not None:
            self.attack_rule_id = attack_rule_id
        if attack_type is not None:
            self.attack_type = attack_type
        if direction is not None:
            self.direction = direction
        if dst_ip is not None:
            self.dst_ip = dst_ip
        if dst_port is not None:
            self.dst_port = dst_port
        if dst_region_id is not None:
            self.dst_region_id = dst_region_id
        if dst_region_name is not None:
            self.dst_region_name = dst_region_name
        if dst_province_id is not None:
            self.dst_province_id = dst_province_id
        if dst_province_name is not None:
            self.dst_province_name = dst_province_name
        if dst_city_id is not None:
            self.dst_city_id = dst_city_id
        if dst_city_name is not None:
            self.dst_city_name = dst_city_name
        if event_time is not None:
            self.event_time = event_time
        if level is not None:
            self.level = level
        if protocol is not None:
            self.protocol = protocol
        if source is not None:
            self.source = source
        if src_ip is not None:
            self.src_ip = src_ip
        if real_ip is not None:
            self.real_ip = real_ip
        if tag is not None:
            self.tag = tag
        if src_port is not None:
            self.src_port = src_port
        if src_region_id is not None:
            self.src_region_id = src_region_id
        if src_region_name is not None:
            self.src_region_name = src_region_name
        if src_province_id is not None:
            self.src_province_id = src_province_id
        if src_province_name is not None:
            self.src_province_name = src_province_name
        if src_city_id is not None:
            self.src_city_id = src_city_id
        if src_city_name is not None:
            self.src_city_name = src_city_name
        if vgw_id is not None:
            self.vgw_id = vgw_id

    @property
    def action(self):
        r"""Gets the action of this AttackLog.

        **参数解释**： 动作 **取值范围**： 不涉及

        :return: The action of this AttackLog.
        :rtype: str
        """
        return self._action

    @action.setter
    def action(self, action):
        r"""Sets the action of this AttackLog.

        **参数解释**： 动作 **取值范围**： 不涉及

        :param action: The action of this AttackLog.
        :type action: str
        """
        self._action = action

    @property
    def app(self):
        r"""Gets the app of this AttackLog.

        **参数解释**： 应用 **取值范围**： 不涉及

        :return: The app of this AttackLog.
        :rtype: str
        """
        return self._app

    @app.setter
    def app(self, app):
        r"""Sets the app of this AttackLog.

        **参数解释**： 应用 **取值范围**： 不涉及

        :param app: The app of this AttackLog.
        :type app: str
        """
        self._app = app

    @property
    def attack_rule(self):
        r"""Gets the attack_rule of this AttackLog.

        **参数解释**： 攻击规则 **取值范围**： 不涉及

        :return: The attack_rule of this AttackLog.
        :rtype: str
        """
        return self._attack_rule

    @attack_rule.setter
    def attack_rule(self, attack_rule):
        r"""Sets the attack_rule of this AttackLog.

        **参数解释**： 攻击规则 **取值范围**： 不涉及

        :param attack_rule: The attack_rule of this AttackLog.
        :type attack_rule: str
        """
        self._attack_rule = attack_rule

    @property
    def attack_rule_id(self):
        r"""Gets the attack_rule_id of this AttackLog.

        **参数解释**： 攻击规则ID **取值范围**： 不涉及

        :return: The attack_rule_id of this AttackLog.
        :rtype: str
        """
        return self._attack_rule_id

    @attack_rule_id.setter
    def attack_rule_id(self, attack_rule_id):
        r"""Sets the attack_rule_id of this AttackLog.

        **参数解释**： 攻击规则ID **取值范围**： 不涉及

        :param attack_rule_id: The attack_rule_id of this AttackLog.
        :type attack_rule_id: str
        """
        self._attack_rule_id = attack_rule_id

    @property
    def attack_type(self):
        r"""Gets the attack_type of this AttackLog.

        **参数解释**： 攻击类型 **取值范围**： 不涉及

        :return: The attack_type of this AttackLog.
        :rtype: str
        """
        return self._attack_type

    @attack_type.setter
    def attack_type(self, attack_type):
        r"""Sets the attack_type of this AttackLog.

        **参数解释**： 攻击类型 **取值范围**： 不涉及

        :param attack_type: The attack_type of this AttackLog.
        :type attack_type: str
        """
        self._attack_type = attack_type

    @property
    def direction(self):
        r"""Gets the direction of this AttackLog.

        **参数解释**： 攻击方向 **取值范围**： 不涉及

        :return: The direction of this AttackLog.
        :rtype: str
        """
        return self._direction

    @direction.setter
    def direction(self, direction):
        r"""Sets the direction of this AttackLog.

        **参数解释**： 攻击方向 **取值范围**： 不涉及

        :param direction: The direction of this AttackLog.
        :type direction: str
        """
        self._direction = direction

    @property
    def dst_ip(self):
        r"""Gets the dst_ip of this AttackLog.

        **参数解释**： 目的IP **取值范围**： 不涉及

        :return: The dst_ip of this AttackLog.
        :rtype: str
        """
        return self._dst_ip

    @dst_ip.setter
    def dst_ip(self, dst_ip):
        r"""Sets the dst_ip of this AttackLog.

        **参数解释**： 目的IP **取值范围**： 不涉及

        :param dst_ip: The dst_ip of this AttackLog.
        :type dst_ip: str
        """
        self._dst_ip = dst_ip

    @property
    def dst_port(self):
        r"""Gets the dst_port of this AttackLog.

        **参数解释**： 目的端口 **取值范围**： 不涉及

        :return: The dst_port of this AttackLog.
        :rtype: int
        """
        return self._dst_port

    @dst_port.setter
    def dst_port(self, dst_port):
        r"""Sets the dst_port of this AttackLog.

        **参数解释**： 目的端口 **取值范围**： 不涉及

        :param dst_port: The dst_port of this AttackLog.
        :type dst_port: int
        """
        self._dst_port = dst_port

    @property
    def dst_region_id(self):
        r"""Gets the dst_region_id of this AttackLog.

        **参数解释**： 目的地区Id **取值范围**： 不涉及

        :return: The dst_region_id of this AttackLog.
        :rtype: str
        """
        return self._dst_region_id

    @dst_region_id.setter
    def dst_region_id(self, dst_region_id):
        r"""Sets the dst_region_id of this AttackLog.

        **参数解释**： 目的地区Id **取值范围**： 不涉及

        :param dst_region_id: The dst_region_id of this AttackLog.
        :type dst_region_id: str
        """
        self._dst_region_id = dst_region_id

    @property
    def dst_region_name(self):
        r"""Gets the dst_region_name of this AttackLog.

        **参数解释**： 目的地区名称 **取值范围**： 不涉及

        :return: The dst_region_name of this AttackLog.
        :rtype: str
        """
        return self._dst_region_name

    @dst_region_name.setter
    def dst_region_name(self, dst_region_name):
        r"""Sets the dst_region_name of this AttackLog.

        **参数解释**： 目的地区名称 **取值范围**： 不涉及

        :param dst_region_name: The dst_region_name of this AttackLog.
        :type dst_region_name: str
        """
        self._dst_region_name = dst_region_name

    @property
    def dst_province_id(self):
        r"""Gets the dst_province_id of this AttackLog.

        **参数解释**： 目的省份ID **取值范围**： 不涉及

        :return: The dst_province_id of this AttackLog.
        :rtype: str
        """
        return self._dst_province_id

    @dst_province_id.setter
    def dst_province_id(self, dst_province_id):
        r"""Sets the dst_province_id of this AttackLog.

        **参数解释**： 目的省份ID **取值范围**： 不涉及

        :param dst_province_id: The dst_province_id of this AttackLog.
        :type dst_province_id: str
        """
        self._dst_province_id = dst_province_id

    @property
    def dst_province_name(self):
        r"""Gets the dst_province_name of this AttackLog.

        **参数解释**： 目的省份名称 **取值范围**： 不涉及

        :return: The dst_province_name of this AttackLog.
        :rtype: str
        """
        return self._dst_province_name

    @dst_province_name.setter
    def dst_province_name(self, dst_province_name):
        r"""Sets the dst_province_name of this AttackLog.

        **参数解释**： 目的省份名称 **取值范围**： 不涉及

        :param dst_province_name: The dst_province_name of this AttackLog.
        :type dst_province_name: str
        """
        self._dst_province_name = dst_province_name

    @property
    def dst_city_id(self):
        r"""Gets the dst_city_id of this AttackLog.

        **参数解释**： 目的城市Id **取值范围**： 不涉及

        :return: The dst_city_id of this AttackLog.
        :rtype: str
        """
        return self._dst_city_id

    @dst_city_id.setter
    def dst_city_id(self, dst_city_id):
        r"""Sets the dst_city_id of this AttackLog.

        **参数解释**： 目的城市Id **取值范围**： 不涉及

        :param dst_city_id: The dst_city_id of this AttackLog.
        :type dst_city_id: str
        """
        self._dst_city_id = dst_city_id

    @property
    def dst_city_name(self):
        r"""Gets the dst_city_name of this AttackLog.

        **参数解释**： 目的城市名称 **取值范围**： 不涉及

        :return: The dst_city_name of this AttackLog.
        :rtype: str
        """
        return self._dst_city_name

    @dst_city_name.setter
    def dst_city_name(self, dst_city_name):
        r"""Sets the dst_city_name of this AttackLog.

        **参数解释**： 目的城市名称 **取值范围**： 不涉及

        :param dst_city_name: The dst_city_name of this AttackLog.
        :type dst_city_name: str
        """
        self._dst_city_name = dst_city_name

    @property
    def event_time(self):
        r"""Gets the event_time of this AttackLog.

        **参数解释**： 发生时间 **取值范围**： 不涉及

        :return: The event_time of this AttackLog.
        :rtype: int
        """
        return self._event_time

    @event_time.setter
    def event_time(self, event_time):
        r"""Sets the event_time of this AttackLog.

        **参数解释**： 发生时间 **取值范围**： 不涉及

        :param event_time: The event_time of this AttackLog.
        :type event_time: int
        """
        self._event_time = event_time

    @property
    def level(self):
        r"""Gets the level of this AttackLog.

        **参数解释**： 危险等级 **取值范围**： 不涉及

        :return: The level of this AttackLog.
        :rtype: str
        """
        return self._level

    @level.setter
    def level(self, level):
        r"""Sets the level of this AttackLog.

        **参数解释**： 危险等级 **取值范围**： 不涉及

        :param level: The level of this AttackLog.
        :type level: str
        """
        self._level = level

    @property
    def protocol(self):
        r"""Gets the protocol of this AttackLog.

        **参数解释**： 协议 **取值范围**： 不涉及

        :return: The protocol of this AttackLog.
        :rtype: str
        """
        return self._protocol

    @protocol.setter
    def protocol(self, protocol):
        r"""Sets the protocol of this AttackLog.

        **参数解释**： 协议 **取值范围**： 不涉及

        :param protocol: The protocol of this AttackLog.
        :type protocol: str
        """
        self._protocol = protocol

    @property
    def source(self):
        r"""Gets the source of this AttackLog.

        **参数解释**： 来源 **取值范围**： 不涉及

        :return: The source of this AttackLog.
        :rtype: str
        """
        return self._source

    @source.setter
    def source(self, source):
        r"""Sets the source of this AttackLog.

        **参数解释**： 来源 **取值范围**： 不涉及

        :param source: The source of this AttackLog.
        :type source: str
        """
        self._source = source

    @property
    def src_ip(self):
        r"""Gets the src_ip of this AttackLog.

        **参数解释**： 源IP **取值范围**： 不涉及

        :return: The src_ip of this AttackLog.
        :rtype: str
        """
        return self._src_ip

    @src_ip.setter
    def src_ip(self, src_ip):
        r"""Sets the src_ip of this AttackLog.

        **参数解释**： 源IP **取值范围**： 不涉及

        :param src_ip: The src_ip of this AttackLog.
        :type src_ip: str
        """
        self._src_ip = src_ip

    @property
    def real_ip(self):
        r"""Gets the real_ip of this AttackLog.

        **参数解释**： 真实IP **取值范围**： 不涉及

        :return: The real_ip of this AttackLog.
        :rtype: str
        """
        return self._real_ip

    @real_ip.setter
    def real_ip(self, real_ip):
        r"""Sets the real_ip of this AttackLog.

        **参数解释**： 真实IP **取值范围**： 不涉及

        :param real_ip: The real_ip of this AttackLog.
        :type real_ip: str
        """
        self._real_ip = real_ip

    @property
    def tag(self):
        r"""Gets the tag of this AttackLog.

        **参数解释**： 标签 **取值范围**： 不涉及

        :return: The tag of this AttackLog.
        :rtype: int
        """
        return self._tag

    @tag.setter
    def tag(self, tag):
        r"""Sets the tag of this AttackLog.

        **参数解释**： 标签 **取值范围**： 不涉及

        :param tag: The tag of this AttackLog.
        :type tag: int
        """
        self._tag = tag

    @property
    def src_port(self):
        r"""Gets the src_port of this AttackLog.

        **参数解释**： 源端口 **取值范围**： 不涉及

        :return: The src_port of this AttackLog.
        :rtype: int
        """
        return self._src_port

    @src_port.setter
    def src_port(self, src_port):
        r"""Sets the src_port of this AttackLog.

        **参数解释**： 源端口 **取值范围**： 不涉及

        :param src_port: The src_port of this AttackLog.
        :type src_port: int
        """
        self._src_port = src_port

    @property
    def src_region_id(self):
        r"""Gets the src_region_id of this AttackLog.

        **参数解释**： 源地区Id **取值范围**： 不涉及

        :return: The src_region_id of this AttackLog.
        :rtype: str
        """
        return self._src_region_id

    @src_region_id.setter
    def src_region_id(self, src_region_id):
        r"""Sets the src_region_id of this AttackLog.

        **参数解释**： 源地区Id **取值范围**： 不涉及

        :param src_region_id: The src_region_id of this AttackLog.
        :type src_region_id: str
        """
        self._src_region_id = src_region_id

    @property
    def src_region_name(self):
        r"""Gets the src_region_name of this AttackLog.

        **参数解释**： 源地区名称 **取值范围**： 不涉及

        :return: The src_region_name of this AttackLog.
        :rtype: str
        """
        return self._src_region_name

    @src_region_name.setter
    def src_region_name(self, src_region_name):
        r"""Sets the src_region_name of this AttackLog.

        **参数解释**： 源地区名称 **取值范围**： 不涉及

        :param src_region_name: The src_region_name of this AttackLog.
        :type src_region_name: str
        """
        self._src_region_name = src_region_name

    @property
    def src_province_id(self):
        r"""Gets the src_province_id of this AttackLog.

        **参数解释**： 源省份Id **取值范围**： 不涉及

        :return: The src_province_id of this AttackLog.
        :rtype: str
        """
        return self._src_province_id

    @src_province_id.setter
    def src_province_id(self, src_province_id):
        r"""Sets the src_province_id of this AttackLog.

        **参数解释**： 源省份Id **取值范围**： 不涉及

        :param src_province_id: The src_province_id of this AttackLog.
        :type src_province_id: str
        """
        self._src_province_id = src_province_id

    @property
    def src_province_name(self):
        r"""Gets the src_province_name of this AttackLog.

        **参数解释**： 源省份名称 **取值范围**： 不涉及

        :return: The src_province_name of this AttackLog.
        :rtype: str
        """
        return self._src_province_name

    @src_province_name.setter
    def src_province_name(self, src_province_name):
        r"""Sets the src_province_name of this AttackLog.

        **参数解释**： 源省份名称 **取值范围**： 不涉及

        :param src_province_name: The src_province_name of this AttackLog.
        :type src_province_name: str
        """
        self._src_province_name = src_province_name

    @property
    def src_city_id(self):
        r"""Gets the src_city_id of this AttackLog.

        **参数解释**： 源城市Id **取值范围**： 不涉及

        :return: The src_city_id of this AttackLog.
        :rtype: str
        """
        return self._src_city_id

    @src_city_id.setter
    def src_city_id(self, src_city_id):
        r"""Sets the src_city_id of this AttackLog.

        **参数解释**： 源城市Id **取值范围**： 不涉及

        :param src_city_id: The src_city_id of this AttackLog.
        :type src_city_id: str
        """
        self._src_city_id = src_city_id

    @property
    def src_city_name(self):
        r"""Gets the src_city_name of this AttackLog.

        **参数解释**： 源城市 **取值范围**： 不涉及

        :return: The src_city_name of this AttackLog.
        :rtype: str
        """
        return self._src_city_name

    @src_city_name.setter
    def src_city_name(self, src_city_name):
        r"""Sets the src_city_name of this AttackLog.

        **参数解释**： 源城市 **取值范围**： 不涉及

        :param src_city_name: The src_city_name of this AttackLog.
        :type src_city_name: str
        """
        self._src_city_name = src_city_name

    @property
    def vgw_id(self):
        r"""Gets the vgw_id of this AttackLog.

        **参数解释**： VGW Id **取值范围**： 不涉及

        :return: The vgw_id of this AttackLog.
        :rtype: str
        """
        return self._vgw_id

    @vgw_id.setter
    def vgw_id(self, vgw_id):
        r"""Sets the vgw_id of this AttackLog.

        **参数解释**： VGW Id **取值范围**： 不涉及

        :param vgw_id: The vgw_id of this AttackLog.
        :type vgw_id: str
        """
        self._vgw_id = vgw_id

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
        if not isinstance(other, AttackLog):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

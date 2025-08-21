# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AccessLogInfo:

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
        'url': 'str',
        'dst_host': 'str',
        'dst_ip': 'str',
        'dst_port': 'int',
        'dst_region_id': 'str',
        'dst_region_name': 'str',
        'dst_province_id': 'str',
        'dst_province_name': 'str',
        'dst_city_id': 'str',
        'dst_city_name': 'str',
        'hit_time': 'int',
        'log_id': 'str',
        'protocol': 'str',
        'rule_id': 'str',
        'rule_name': 'str',
        'rule_type': 'int',
        'src_ip': 'str',
        'src_port': 'int',
        'src_region_id': 'str',
        'src_region_name': 'str',
        'src_province_id': 'str',
        'src_province_name': 'str',
        'src_city_id': 'str',
        'src_city_name': 'str',
        'vgw_id': 'str',
        'qos_rule_id': 'str',
        'qos_rule_name': 'str',
        'qos_rule_type': 'int'
    }

    attribute_map = {
        'action': 'action',
        'app': 'app',
        'url': 'url',
        'dst_host': 'dst_host',
        'dst_ip': 'dst_ip',
        'dst_port': 'dst_port',
        'dst_region_id': 'dst_region_id',
        'dst_region_name': 'dst_region_name',
        'dst_province_id': 'dst_province_id',
        'dst_province_name': 'dst_province_name',
        'dst_city_id': 'dst_city_id',
        'dst_city_name': 'dst_city_name',
        'hit_time': 'hit_time',
        'log_id': 'log_id',
        'protocol': 'protocol',
        'rule_id': 'rule_id',
        'rule_name': 'rule_name',
        'rule_type': 'rule_type',
        'src_ip': 'src_ip',
        'src_port': 'src_port',
        'src_region_id': 'src_region_id',
        'src_region_name': 'src_region_name',
        'src_province_id': 'src_province_id',
        'src_province_name': 'src_province_name',
        'src_city_id': 'src_city_id',
        'src_city_name': 'src_city_name',
        'vgw_id': 'vgw_id',
        'qos_rule_id': 'qos_rule_id',
        'qos_rule_name': 'qos_rule_name',
        'qos_rule_type': 'qos_rule_type'
    }

    def __init__(self, action=None, app=None, url=None, dst_host=None, dst_ip=None, dst_port=None, dst_region_id=None, dst_region_name=None, dst_province_id=None, dst_province_name=None, dst_city_id=None, dst_city_name=None, hit_time=None, log_id=None, protocol=None, rule_id=None, rule_name=None, rule_type=None, src_ip=None, src_port=None, src_region_id=None, src_region_name=None, src_province_id=None, src_province_name=None, src_city_id=None, src_city_name=None, vgw_id=None, qos_rule_id=None, qos_rule_name=None, qos_rule_type=None):
        r"""AccessLogInfo

        The model defined in huaweicloud sdk

        :param action: **参数解释**： 动作 **取值范围**： 不涉及
        :type action: str
        :param app: **参数解释**： 应用 **取值范围**： 不涉及
        :type app: str
        :param url: 
        :type url: str
        :param dst_host: **参数解释**： 目的域名 **取值范围**： 不涉及
        :type dst_host: str
        :param dst_ip: **参数解释**： 目的IP **取值范围**： 不涉及
        :type dst_ip: str
        :param dst_port: **参数解释**： 目的端口 **取值范围**： 不涉及
        :type dst_port: int
        :param dst_region_id: **参数解释**： 目的地区ID **取值范围**： 不涉及
        :type dst_region_id: str
        :param dst_region_name: **参数解释**： 目的地区名称 **取值范围**： 不涉及
        :type dst_region_name: str
        :param dst_province_id: **参数解释**： 目的省份ID **取值范围**： 不涉及
        :type dst_province_id: str
        :param dst_province_name: **参数解释**： 目的省份名称 **取值范围**： 不涉及
        :type dst_province_name: str
        :param dst_city_id: **参数解释**： 目的城市ID **取值范围**： 不涉及
        :type dst_city_id: str
        :param dst_city_name: **参数解释**： 目的城市名称 **取值范围**： 不涉及
        :type dst_city_name: str
        :param hit_time: **参数解释**： 命中时间 **取值范围**： 不涉及
        :type hit_time: int
        :param log_id: 
        :type log_id: str
        :param protocol: **参数解释**： 协议 **取值范围**： 不涉及
        :type protocol: str
        :param rule_id: **参数解释**： 规则ID **取值范围**： 不涉及
        :type rule_id: str
        :param rule_name: **参数解释**： 规则名称 **取值范围**： 不涉及
        :type rule_name: str
        :param rule_type: 
        :type rule_type: int
        :param src_ip: **参数解释**： 源IP **取值范围**： 不涉及
        :type src_ip: str
        :param src_port: **参数解释**： 源端口 **取值范围**： 不涉及
        :type src_port: int
        :param src_region_id: **参数解释**： 源地区ID **取值范围**： 不涉及
        :type src_region_id: str
        :param src_region_name: **参数解释**： 源地区名称 **取值范围**： 不涉及
        :type src_region_name: str
        :param src_province_id: **参数解释**： 源省份ID **取值范围**： 不涉及
        :type src_province_id: str
        :param src_province_name: **参数解释**： 源省份名称 **取值范围**： 不涉及
        :type src_province_name: str
        :param src_city_id: **参数解释**： 源城市ID **取值范围**： 不涉及
        :type src_city_id: str
        :param src_city_name: **参数解释**： 源城市名称 **取值范围**： 不涉及
        :type src_city_name: str
        :param vgw_id: **参数解释**： VGW　ID **取值范围**： 不涉及
        :type vgw_id: str
        :param qos_rule_id: 
        :type qos_rule_id: str
        :param qos_rule_name: 
        :type qos_rule_name: str
        :param qos_rule_type: 
        :type qos_rule_type: int
        """
        
        

        self._action = None
        self._app = None
        self._url = None
        self._dst_host = None
        self._dst_ip = None
        self._dst_port = None
        self._dst_region_id = None
        self._dst_region_name = None
        self._dst_province_id = None
        self._dst_province_name = None
        self._dst_city_id = None
        self._dst_city_name = None
        self._hit_time = None
        self._log_id = None
        self._protocol = None
        self._rule_id = None
        self._rule_name = None
        self._rule_type = None
        self._src_ip = None
        self._src_port = None
        self._src_region_id = None
        self._src_region_name = None
        self._src_province_id = None
        self._src_province_name = None
        self._src_city_id = None
        self._src_city_name = None
        self._vgw_id = None
        self._qos_rule_id = None
        self._qos_rule_name = None
        self._qos_rule_type = None
        self.discriminator = None

        if action is not None:
            self.action = action
        if app is not None:
            self.app = app
        if url is not None:
            self.url = url
        if dst_host is not None:
            self.dst_host = dst_host
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
        if hit_time is not None:
            self.hit_time = hit_time
        if log_id is not None:
            self.log_id = log_id
        if protocol is not None:
            self.protocol = protocol
        if rule_id is not None:
            self.rule_id = rule_id
        if rule_name is not None:
            self.rule_name = rule_name
        if rule_type is not None:
            self.rule_type = rule_type
        if src_ip is not None:
            self.src_ip = src_ip
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
        if qos_rule_id is not None:
            self.qos_rule_id = qos_rule_id
        if qos_rule_name is not None:
            self.qos_rule_name = qos_rule_name
        if qos_rule_type is not None:
            self.qos_rule_type = qos_rule_type

    @property
    def action(self):
        r"""Gets the action of this AccessLogInfo.

        **参数解释**： 动作 **取值范围**： 不涉及

        :return: The action of this AccessLogInfo.
        :rtype: str
        """
        return self._action

    @action.setter
    def action(self, action):
        r"""Sets the action of this AccessLogInfo.

        **参数解释**： 动作 **取值范围**： 不涉及

        :param action: The action of this AccessLogInfo.
        :type action: str
        """
        self._action = action

    @property
    def app(self):
        r"""Gets the app of this AccessLogInfo.

        **参数解释**： 应用 **取值范围**： 不涉及

        :return: The app of this AccessLogInfo.
        :rtype: str
        """
        return self._app

    @app.setter
    def app(self, app):
        r"""Sets the app of this AccessLogInfo.

        **参数解释**： 应用 **取值范围**： 不涉及

        :param app: The app of this AccessLogInfo.
        :type app: str
        """
        self._app = app

    @property
    def url(self):
        r"""Gets the url of this AccessLogInfo.

        :return: The url of this AccessLogInfo.
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        r"""Sets the url of this AccessLogInfo.

        :param url: The url of this AccessLogInfo.
        :type url: str
        """
        self._url = url

    @property
    def dst_host(self):
        r"""Gets the dst_host of this AccessLogInfo.

        **参数解释**： 目的域名 **取值范围**： 不涉及

        :return: The dst_host of this AccessLogInfo.
        :rtype: str
        """
        return self._dst_host

    @dst_host.setter
    def dst_host(self, dst_host):
        r"""Sets the dst_host of this AccessLogInfo.

        **参数解释**： 目的域名 **取值范围**： 不涉及

        :param dst_host: The dst_host of this AccessLogInfo.
        :type dst_host: str
        """
        self._dst_host = dst_host

    @property
    def dst_ip(self):
        r"""Gets the dst_ip of this AccessLogInfo.

        **参数解释**： 目的IP **取值范围**： 不涉及

        :return: The dst_ip of this AccessLogInfo.
        :rtype: str
        """
        return self._dst_ip

    @dst_ip.setter
    def dst_ip(self, dst_ip):
        r"""Sets the dst_ip of this AccessLogInfo.

        **参数解释**： 目的IP **取值范围**： 不涉及

        :param dst_ip: The dst_ip of this AccessLogInfo.
        :type dst_ip: str
        """
        self._dst_ip = dst_ip

    @property
    def dst_port(self):
        r"""Gets the dst_port of this AccessLogInfo.

        **参数解释**： 目的端口 **取值范围**： 不涉及

        :return: The dst_port of this AccessLogInfo.
        :rtype: int
        """
        return self._dst_port

    @dst_port.setter
    def dst_port(self, dst_port):
        r"""Sets the dst_port of this AccessLogInfo.

        **参数解释**： 目的端口 **取值范围**： 不涉及

        :param dst_port: The dst_port of this AccessLogInfo.
        :type dst_port: int
        """
        self._dst_port = dst_port

    @property
    def dst_region_id(self):
        r"""Gets the dst_region_id of this AccessLogInfo.

        **参数解释**： 目的地区ID **取值范围**： 不涉及

        :return: The dst_region_id of this AccessLogInfo.
        :rtype: str
        """
        return self._dst_region_id

    @dst_region_id.setter
    def dst_region_id(self, dst_region_id):
        r"""Sets the dst_region_id of this AccessLogInfo.

        **参数解释**： 目的地区ID **取值范围**： 不涉及

        :param dst_region_id: The dst_region_id of this AccessLogInfo.
        :type dst_region_id: str
        """
        self._dst_region_id = dst_region_id

    @property
    def dst_region_name(self):
        r"""Gets the dst_region_name of this AccessLogInfo.

        **参数解释**： 目的地区名称 **取值范围**： 不涉及

        :return: The dst_region_name of this AccessLogInfo.
        :rtype: str
        """
        return self._dst_region_name

    @dst_region_name.setter
    def dst_region_name(self, dst_region_name):
        r"""Sets the dst_region_name of this AccessLogInfo.

        **参数解释**： 目的地区名称 **取值范围**： 不涉及

        :param dst_region_name: The dst_region_name of this AccessLogInfo.
        :type dst_region_name: str
        """
        self._dst_region_name = dst_region_name

    @property
    def dst_province_id(self):
        r"""Gets the dst_province_id of this AccessLogInfo.

        **参数解释**： 目的省份ID **取值范围**： 不涉及

        :return: The dst_province_id of this AccessLogInfo.
        :rtype: str
        """
        return self._dst_province_id

    @dst_province_id.setter
    def dst_province_id(self, dst_province_id):
        r"""Sets the dst_province_id of this AccessLogInfo.

        **参数解释**： 目的省份ID **取值范围**： 不涉及

        :param dst_province_id: The dst_province_id of this AccessLogInfo.
        :type dst_province_id: str
        """
        self._dst_province_id = dst_province_id

    @property
    def dst_province_name(self):
        r"""Gets the dst_province_name of this AccessLogInfo.

        **参数解释**： 目的省份名称 **取值范围**： 不涉及

        :return: The dst_province_name of this AccessLogInfo.
        :rtype: str
        """
        return self._dst_province_name

    @dst_province_name.setter
    def dst_province_name(self, dst_province_name):
        r"""Sets the dst_province_name of this AccessLogInfo.

        **参数解释**： 目的省份名称 **取值范围**： 不涉及

        :param dst_province_name: The dst_province_name of this AccessLogInfo.
        :type dst_province_name: str
        """
        self._dst_province_name = dst_province_name

    @property
    def dst_city_id(self):
        r"""Gets the dst_city_id of this AccessLogInfo.

        **参数解释**： 目的城市ID **取值范围**： 不涉及

        :return: The dst_city_id of this AccessLogInfo.
        :rtype: str
        """
        return self._dst_city_id

    @dst_city_id.setter
    def dst_city_id(self, dst_city_id):
        r"""Sets the dst_city_id of this AccessLogInfo.

        **参数解释**： 目的城市ID **取值范围**： 不涉及

        :param dst_city_id: The dst_city_id of this AccessLogInfo.
        :type dst_city_id: str
        """
        self._dst_city_id = dst_city_id

    @property
    def dst_city_name(self):
        r"""Gets the dst_city_name of this AccessLogInfo.

        **参数解释**： 目的城市名称 **取值范围**： 不涉及

        :return: The dst_city_name of this AccessLogInfo.
        :rtype: str
        """
        return self._dst_city_name

    @dst_city_name.setter
    def dst_city_name(self, dst_city_name):
        r"""Sets the dst_city_name of this AccessLogInfo.

        **参数解释**： 目的城市名称 **取值范围**： 不涉及

        :param dst_city_name: The dst_city_name of this AccessLogInfo.
        :type dst_city_name: str
        """
        self._dst_city_name = dst_city_name

    @property
    def hit_time(self):
        r"""Gets the hit_time of this AccessLogInfo.

        **参数解释**： 命中时间 **取值范围**： 不涉及

        :return: The hit_time of this AccessLogInfo.
        :rtype: int
        """
        return self._hit_time

    @hit_time.setter
    def hit_time(self, hit_time):
        r"""Sets the hit_time of this AccessLogInfo.

        **参数解释**： 命中时间 **取值范围**： 不涉及

        :param hit_time: The hit_time of this AccessLogInfo.
        :type hit_time: int
        """
        self._hit_time = hit_time

    @property
    def log_id(self):
        r"""Gets the log_id of this AccessLogInfo.

        :return: The log_id of this AccessLogInfo.
        :rtype: str
        """
        return self._log_id

    @log_id.setter
    def log_id(self, log_id):
        r"""Sets the log_id of this AccessLogInfo.

        :param log_id: The log_id of this AccessLogInfo.
        :type log_id: str
        """
        self._log_id = log_id

    @property
    def protocol(self):
        r"""Gets the protocol of this AccessLogInfo.

        **参数解释**： 协议 **取值范围**： 不涉及

        :return: The protocol of this AccessLogInfo.
        :rtype: str
        """
        return self._protocol

    @protocol.setter
    def protocol(self, protocol):
        r"""Sets the protocol of this AccessLogInfo.

        **参数解释**： 协议 **取值范围**： 不涉及

        :param protocol: The protocol of this AccessLogInfo.
        :type protocol: str
        """
        self._protocol = protocol

    @property
    def rule_id(self):
        r"""Gets the rule_id of this AccessLogInfo.

        **参数解释**： 规则ID **取值范围**： 不涉及

        :return: The rule_id of this AccessLogInfo.
        :rtype: str
        """
        return self._rule_id

    @rule_id.setter
    def rule_id(self, rule_id):
        r"""Sets the rule_id of this AccessLogInfo.

        **参数解释**： 规则ID **取值范围**： 不涉及

        :param rule_id: The rule_id of this AccessLogInfo.
        :type rule_id: str
        """
        self._rule_id = rule_id

    @property
    def rule_name(self):
        r"""Gets the rule_name of this AccessLogInfo.

        **参数解释**： 规则名称 **取值范围**： 不涉及

        :return: The rule_name of this AccessLogInfo.
        :rtype: str
        """
        return self._rule_name

    @rule_name.setter
    def rule_name(self, rule_name):
        r"""Sets the rule_name of this AccessLogInfo.

        **参数解释**： 规则名称 **取值范围**： 不涉及

        :param rule_name: The rule_name of this AccessLogInfo.
        :type rule_name: str
        """
        self._rule_name = rule_name

    @property
    def rule_type(self):
        r"""Gets the rule_type of this AccessLogInfo.

        :return: The rule_type of this AccessLogInfo.
        :rtype: int
        """
        return self._rule_type

    @rule_type.setter
    def rule_type(self, rule_type):
        r"""Sets the rule_type of this AccessLogInfo.

        :param rule_type: The rule_type of this AccessLogInfo.
        :type rule_type: int
        """
        self._rule_type = rule_type

    @property
    def src_ip(self):
        r"""Gets the src_ip of this AccessLogInfo.

        **参数解释**： 源IP **取值范围**： 不涉及

        :return: The src_ip of this AccessLogInfo.
        :rtype: str
        """
        return self._src_ip

    @src_ip.setter
    def src_ip(self, src_ip):
        r"""Sets the src_ip of this AccessLogInfo.

        **参数解释**： 源IP **取值范围**： 不涉及

        :param src_ip: The src_ip of this AccessLogInfo.
        :type src_ip: str
        """
        self._src_ip = src_ip

    @property
    def src_port(self):
        r"""Gets the src_port of this AccessLogInfo.

        **参数解释**： 源端口 **取值范围**： 不涉及

        :return: The src_port of this AccessLogInfo.
        :rtype: int
        """
        return self._src_port

    @src_port.setter
    def src_port(self, src_port):
        r"""Sets the src_port of this AccessLogInfo.

        **参数解释**： 源端口 **取值范围**： 不涉及

        :param src_port: The src_port of this AccessLogInfo.
        :type src_port: int
        """
        self._src_port = src_port

    @property
    def src_region_id(self):
        r"""Gets the src_region_id of this AccessLogInfo.

        **参数解释**： 源地区ID **取值范围**： 不涉及

        :return: The src_region_id of this AccessLogInfo.
        :rtype: str
        """
        return self._src_region_id

    @src_region_id.setter
    def src_region_id(self, src_region_id):
        r"""Sets the src_region_id of this AccessLogInfo.

        **参数解释**： 源地区ID **取值范围**： 不涉及

        :param src_region_id: The src_region_id of this AccessLogInfo.
        :type src_region_id: str
        """
        self._src_region_id = src_region_id

    @property
    def src_region_name(self):
        r"""Gets the src_region_name of this AccessLogInfo.

        **参数解释**： 源地区名称 **取值范围**： 不涉及

        :return: The src_region_name of this AccessLogInfo.
        :rtype: str
        """
        return self._src_region_name

    @src_region_name.setter
    def src_region_name(self, src_region_name):
        r"""Sets the src_region_name of this AccessLogInfo.

        **参数解释**： 源地区名称 **取值范围**： 不涉及

        :param src_region_name: The src_region_name of this AccessLogInfo.
        :type src_region_name: str
        """
        self._src_region_name = src_region_name

    @property
    def src_province_id(self):
        r"""Gets the src_province_id of this AccessLogInfo.

        **参数解释**： 源省份ID **取值范围**： 不涉及

        :return: The src_province_id of this AccessLogInfo.
        :rtype: str
        """
        return self._src_province_id

    @src_province_id.setter
    def src_province_id(self, src_province_id):
        r"""Sets the src_province_id of this AccessLogInfo.

        **参数解释**： 源省份ID **取值范围**： 不涉及

        :param src_province_id: The src_province_id of this AccessLogInfo.
        :type src_province_id: str
        """
        self._src_province_id = src_province_id

    @property
    def src_province_name(self):
        r"""Gets the src_province_name of this AccessLogInfo.

        **参数解释**： 源省份名称 **取值范围**： 不涉及

        :return: The src_province_name of this AccessLogInfo.
        :rtype: str
        """
        return self._src_province_name

    @src_province_name.setter
    def src_province_name(self, src_province_name):
        r"""Sets the src_province_name of this AccessLogInfo.

        **参数解释**： 源省份名称 **取值范围**： 不涉及

        :param src_province_name: The src_province_name of this AccessLogInfo.
        :type src_province_name: str
        """
        self._src_province_name = src_province_name

    @property
    def src_city_id(self):
        r"""Gets the src_city_id of this AccessLogInfo.

        **参数解释**： 源城市ID **取值范围**： 不涉及

        :return: The src_city_id of this AccessLogInfo.
        :rtype: str
        """
        return self._src_city_id

    @src_city_id.setter
    def src_city_id(self, src_city_id):
        r"""Sets the src_city_id of this AccessLogInfo.

        **参数解释**： 源城市ID **取值范围**： 不涉及

        :param src_city_id: The src_city_id of this AccessLogInfo.
        :type src_city_id: str
        """
        self._src_city_id = src_city_id

    @property
    def src_city_name(self):
        r"""Gets the src_city_name of this AccessLogInfo.

        **参数解释**： 源城市名称 **取值范围**： 不涉及

        :return: The src_city_name of this AccessLogInfo.
        :rtype: str
        """
        return self._src_city_name

    @src_city_name.setter
    def src_city_name(self, src_city_name):
        r"""Sets the src_city_name of this AccessLogInfo.

        **参数解释**： 源城市名称 **取值范围**： 不涉及

        :param src_city_name: The src_city_name of this AccessLogInfo.
        :type src_city_name: str
        """
        self._src_city_name = src_city_name

    @property
    def vgw_id(self):
        r"""Gets the vgw_id of this AccessLogInfo.

        **参数解释**： VGW　ID **取值范围**： 不涉及

        :return: The vgw_id of this AccessLogInfo.
        :rtype: str
        """
        return self._vgw_id

    @vgw_id.setter
    def vgw_id(self, vgw_id):
        r"""Sets the vgw_id of this AccessLogInfo.

        **参数解释**： VGW　ID **取值范围**： 不涉及

        :param vgw_id: The vgw_id of this AccessLogInfo.
        :type vgw_id: str
        """
        self._vgw_id = vgw_id

    @property
    def qos_rule_id(self):
        r"""Gets the qos_rule_id of this AccessLogInfo.

        :return: The qos_rule_id of this AccessLogInfo.
        :rtype: str
        """
        return self._qos_rule_id

    @qos_rule_id.setter
    def qos_rule_id(self, qos_rule_id):
        r"""Sets the qos_rule_id of this AccessLogInfo.

        :param qos_rule_id: The qos_rule_id of this AccessLogInfo.
        :type qos_rule_id: str
        """
        self._qos_rule_id = qos_rule_id

    @property
    def qos_rule_name(self):
        r"""Gets the qos_rule_name of this AccessLogInfo.

        :return: The qos_rule_name of this AccessLogInfo.
        :rtype: str
        """
        return self._qos_rule_name

    @qos_rule_name.setter
    def qos_rule_name(self, qos_rule_name):
        r"""Sets the qos_rule_name of this AccessLogInfo.

        :param qos_rule_name: The qos_rule_name of this AccessLogInfo.
        :type qos_rule_name: str
        """
        self._qos_rule_name = qos_rule_name

    @property
    def qos_rule_type(self):
        r"""Gets the qos_rule_type of this AccessLogInfo.

        :return: The qos_rule_type of this AccessLogInfo.
        :rtype: int
        """
        return self._qos_rule_type

    @qos_rule_type.setter
    def qos_rule_type(self, qos_rule_type):
        r"""Sets the qos_rule_type of this AccessLogInfo.

        :param qos_rule_type: The qos_rule_type of this AccessLogInfo.
        :type qos_rule_type: int
        """
        self._qos_rule_type = qos_rule_type

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
        if not isinstance(other, AccessLogInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

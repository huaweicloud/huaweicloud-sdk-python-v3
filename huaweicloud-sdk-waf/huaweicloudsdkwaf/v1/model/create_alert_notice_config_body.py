# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateAlertNoticeConfigBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'enabled': 'bool',
        'prefer_html': 'bool',
        'topic_urn': 'str',
        'sendfreq': 'int',
        'local': 'str',
        'times': 'int',
        'name': 'str',
        'notice_class': 'str',
        'nearly_expired_time': 'int',
        'is_all_enterprise_project': 'bool',
        'description': 'str',
        'threat': 'list[str]',
        'rule_type': 'list[str]'
    }

    attribute_map = {
        'enabled': 'enabled',
        'prefer_html': 'prefer_html',
        'topic_urn': 'topic_urn',
        'sendfreq': 'sendfreq',
        'local': 'local',
        'times': 'times',
        'name': 'name',
        'notice_class': 'notice_class',
        'nearly_expired_time': 'nearly_expired_time',
        'is_all_enterprise_project': 'is_all_enterprise_project',
        'description': 'description',
        'threat': 'threat',
        'rule_type': 'rule_type'
    }

    def __init__(self, enabled=None, prefer_html=None, topic_urn=None, sendfreq=None, local=None, times=None, name=None, notice_class=None, nearly_expired_time=None, is_all_enterprise_project=None, description=None, threat=None, rule_type=None):
        r"""CreateAlertNoticeConfigBody

        The model defined in huaweicloud sdk

        :param enabled: **参数解释：** 功能启用状态：true表示启用当前配置，false表示禁用。 **约束限制：** 不涉及 **取值范围：** - true - false  **默认取值：** true
        :type enabled: bool
        :param prefer_html: **参数解释：** 预留参数，默认为false **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** false
        :type prefer_html: bool
        :param topic_urn: **参数解释：** 通知模板，关联用于发送告警通知的SMN主题URN,通过“消息通知服务”获取 查询可使用的主题，通过 云日志服务的“查询SMN主题”接口，返回体中的\&quot;topic_urn\&quot;字段 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及
        :type topic_urn: str
        :param sendfreq: **参数解释：** 通间间隔,单位为分钟。当通知类型为防护事件时,该参数表示在该时间间隔内,攻击次数等于或者大于设定阈值时,将发送告警通知,支持的值:5、15、30、60、120、360、720、1440;当通知类型为证书到期时,该参数表示每隔多长时间发送一次告警通知,支持的值为1440、10080(单位为分钟)。 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及
        :type sendfreq: int
        :param local: **参数解释：** 地区，指定告警通知的语言或地域相关配置 **约束限制：** 不涉及 **取值范围：** - zh-cn - en-us  **默认取值：** 不涉及
        :type local: str
        :param times: **参数解释：** 当通知类型为防护事件时,需要填写该参数。在该时间间隔内,当攻击次数大于或等于您设置的阈值时才会发送告警通知 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及
        :type times: int
        :param name: **参数解释：** 告警名称，用于标识告警通知配置的名称 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及
        :type name: str
        :param notice_class: **参数解释：** 告警类型，区分不同场景的告警（如防护规则触发、资源异常等） **约束限制：** 不涉及 **取值范围：** - threat_alert_notice：威胁告警通知  - cert_alert_notice：证书告警通知, - rule_alert_notice：规则告警通知, - cname_ip_alert_notice：域名 / IP 告警通知  **默认取值：** 不涉及
        :type notice_class: str
        :param nearly_expired_time: **参数解释：** 提前通知天数，针对过期类告警提前发送通知的天数 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及
        :type nearly_expired_time: int
        :param is_all_enterprise_project: **参数解释：** 是否所有企业项目，标识该告警配置是否适用于所有企业项目 **约束限制：** 不涉及 **取值范围：** - true - false  **默认取值：** true
        :type is_all_enterprise_project: bool
        :param description: **参数解释：** 描述，对告警通知配置的补充说明 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及
        :type description: str
        :param threat: **参数解释：** 威胁类型范围：指定需要告警的威胁类型，如[\&quot;all\&quot;]表示所有威胁 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** all
        :type threat: list[str]
        :param rule_type: **参数解释：** 指定需要告警的规则类型，[\&quot;all\&quot;]表示所有规则类型。 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** all
        :type rule_type: list[str]
        """
        
        

        self._enabled = None
        self._prefer_html = None
        self._topic_urn = None
        self._sendfreq = None
        self._local = None
        self._times = None
        self._name = None
        self._notice_class = None
        self._nearly_expired_time = None
        self._is_all_enterprise_project = None
        self._description = None
        self._threat = None
        self._rule_type = None
        self.discriminator = None

        self.enabled = enabled
        self.prefer_html = prefer_html
        self.topic_urn = topic_urn
        if sendfreq is not None:
            self.sendfreq = sendfreq
        self.local = local
        if times is not None:
            self.times = times
        self.name = name
        self.notice_class = notice_class
        if nearly_expired_time is not None:
            self.nearly_expired_time = nearly_expired_time
        self.is_all_enterprise_project = is_all_enterprise_project
        if description is not None:
            self.description = description
        if threat is not None:
            self.threat = threat
        if rule_type is not None:
            self.rule_type = rule_type

    @property
    def enabled(self):
        r"""Gets the enabled of this CreateAlertNoticeConfigBody.

        **参数解释：** 功能启用状态：true表示启用当前配置，false表示禁用。 **约束限制：** 不涉及 **取值范围：** - true - false  **默认取值：** true

        :return: The enabled of this CreateAlertNoticeConfigBody.
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        r"""Sets the enabled of this CreateAlertNoticeConfigBody.

        **参数解释：** 功能启用状态：true表示启用当前配置，false表示禁用。 **约束限制：** 不涉及 **取值范围：** - true - false  **默认取值：** true

        :param enabled: The enabled of this CreateAlertNoticeConfigBody.
        :type enabled: bool
        """
        self._enabled = enabled

    @property
    def prefer_html(self):
        r"""Gets the prefer_html of this CreateAlertNoticeConfigBody.

        **参数解释：** 预留参数，默认为false **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** false

        :return: The prefer_html of this CreateAlertNoticeConfigBody.
        :rtype: bool
        """
        return self._prefer_html

    @prefer_html.setter
    def prefer_html(self, prefer_html):
        r"""Sets the prefer_html of this CreateAlertNoticeConfigBody.

        **参数解释：** 预留参数，默认为false **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** false

        :param prefer_html: The prefer_html of this CreateAlertNoticeConfigBody.
        :type prefer_html: bool
        """
        self._prefer_html = prefer_html

    @property
    def topic_urn(self):
        r"""Gets the topic_urn of this CreateAlertNoticeConfigBody.

        **参数解释：** 通知模板，关联用于发送告警通知的SMN主题URN,通过“消息通知服务”获取 查询可使用的主题，通过 云日志服务的“查询SMN主题”接口，返回体中的\"topic_urn\"字段 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :return: The topic_urn of this CreateAlertNoticeConfigBody.
        :rtype: str
        """
        return self._topic_urn

    @topic_urn.setter
    def topic_urn(self, topic_urn):
        r"""Sets the topic_urn of this CreateAlertNoticeConfigBody.

        **参数解释：** 通知模板，关联用于发送告警通知的SMN主题URN,通过“消息通知服务”获取 查询可使用的主题，通过 云日志服务的“查询SMN主题”接口，返回体中的\"topic_urn\"字段 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :param topic_urn: The topic_urn of this CreateAlertNoticeConfigBody.
        :type topic_urn: str
        """
        self._topic_urn = topic_urn

    @property
    def sendfreq(self):
        r"""Gets the sendfreq of this CreateAlertNoticeConfigBody.

        **参数解释：** 通间间隔,单位为分钟。当通知类型为防护事件时,该参数表示在该时间间隔内,攻击次数等于或者大于设定阈值时,将发送告警通知,支持的值:5、15、30、60、120、360、720、1440;当通知类型为证书到期时,该参数表示每隔多长时间发送一次告警通知,支持的值为1440、10080(单位为分钟)。 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :return: The sendfreq of this CreateAlertNoticeConfigBody.
        :rtype: int
        """
        return self._sendfreq

    @sendfreq.setter
    def sendfreq(self, sendfreq):
        r"""Sets the sendfreq of this CreateAlertNoticeConfigBody.

        **参数解释：** 通间间隔,单位为分钟。当通知类型为防护事件时,该参数表示在该时间间隔内,攻击次数等于或者大于设定阈值时,将发送告警通知,支持的值:5、15、30、60、120、360、720、1440;当通知类型为证书到期时,该参数表示每隔多长时间发送一次告警通知,支持的值为1440、10080(单位为分钟)。 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :param sendfreq: The sendfreq of this CreateAlertNoticeConfigBody.
        :type sendfreq: int
        """
        self._sendfreq = sendfreq

    @property
    def local(self):
        r"""Gets the local of this CreateAlertNoticeConfigBody.

        **参数解释：** 地区，指定告警通知的语言或地域相关配置 **约束限制：** 不涉及 **取值范围：** - zh-cn - en-us  **默认取值：** 不涉及

        :return: The local of this CreateAlertNoticeConfigBody.
        :rtype: str
        """
        return self._local

    @local.setter
    def local(self, local):
        r"""Sets the local of this CreateAlertNoticeConfigBody.

        **参数解释：** 地区，指定告警通知的语言或地域相关配置 **约束限制：** 不涉及 **取值范围：** - zh-cn - en-us  **默认取值：** 不涉及

        :param local: The local of this CreateAlertNoticeConfigBody.
        :type local: str
        """
        self._local = local

    @property
    def times(self):
        r"""Gets the times of this CreateAlertNoticeConfigBody.

        **参数解释：** 当通知类型为防护事件时,需要填写该参数。在该时间间隔内,当攻击次数大于或等于您设置的阈值时才会发送告警通知 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :return: The times of this CreateAlertNoticeConfigBody.
        :rtype: int
        """
        return self._times

    @times.setter
    def times(self, times):
        r"""Sets the times of this CreateAlertNoticeConfigBody.

        **参数解释：** 当通知类型为防护事件时,需要填写该参数。在该时间间隔内,当攻击次数大于或等于您设置的阈值时才会发送告警通知 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :param times: The times of this CreateAlertNoticeConfigBody.
        :type times: int
        """
        self._times = times

    @property
    def name(self):
        r"""Gets the name of this CreateAlertNoticeConfigBody.

        **参数解释：** 告警名称，用于标识告警通知配置的名称 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :return: The name of this CreateAlertNoticeConfigBody.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this CreateAlertNoticeConfigBody.

        **参数解释：** 告警名称，用于标识告警通知配置的名称 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :param name: The name of this CreateAlertNoticeConfigBody.
        :type name: str
        """
        self._name = name

    @property
    def notice_class(self):
        r"""Gets the notice_class of this CreateAlertNoticeConfigBody.

        **参数解释：** 告警类型，区分不同场景的告警（如防护规则触发、资源异常等） **约束限制：** 不涉及 **取值范围：** - threat_alert_notice：威胁告警通知  - cert_alert_notice：证书告警通知, - rule_alert_notice：规则告警通知, - cname_ip_alert_notice：域名 / IP 告警通知  **默认取值：** 不涉及

        :return: The notice_class of this CreateAlertNoticeConfigBody.
        :rtype: str
        """
        return self._notice_class

    @notice_class.setter
    def notice_class(self, notice_class):
        r"""Sets the notice_class of this CreateAlertNoticeConfigBody.

        **参数解释：** 告警类型，区分不同场景的告警（如防护规则触发、资源异常等） **约束限制：** 不涉及 **取值范围：** - threat_alert_notice：威胁告警通知  - cert_alert_notice：证书告警通知, - rule_alert_notice：规则告警通知, - cname_ip_alert_notice：域名 / IP 告警通知  **默认取值：** 不涉及

        :param notice_class: The notice_class of this CreateAlertNoticeConfigBody.
        :type notice_class: str
        """
        self._notice_class = notice_class

    @property
    def nearly_expired_time(self):
        r"""Gets the nearly_expired_time of this CreateAlertNoticeConfigBody.

        **参数解释：** 提前通知天数，针对过期类告警提前发送通知的天数 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :return: The nearly_expired_time of this CreateAlertNoticeConfigBody.
        :rtype: int
        """
        return self._nearly_expired_time

    @nearly_expired_time.setter
    def nearly_expired_time(self, nearly_expired_time):
        r"""Sets the nearly_expired_time of this CreateAlertNoticeConfigBody.

        **参数解释：** 提前通知天数，针对过期类告警提前发送通知的天数 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :param nearly_expired_time: The nearly_expired_time of this CreateAlertNoticeConfigBody.
        :type nearly_expired_time: int
        """
        self._nearly_expired_time = nearly_expired_time

    @property
    def is_all_enterprise_project(self):
        r"""Gets the is_all_enterprise_project of this CreateAlertNoticeConfigBody.

        **参数解释：** 是否所有企业项目，标识该告警配置是否适用于所有企业项目 **约束限制：** 不涉及 **取值范围：** - true - false  **默认取值：** true

        :return: The is_all_enterprise_project of this CreateAlertNoticeConfigBody.
        :rtype: bool
        """
        return self._is_all_enterprise_project

    @is_all_enterprise_project.setter
    def is_all_enterprise_project(self, is_all_enterprise_project):
        r"""Sets the is_all_enterprise_project of this CreateAlertNoticeConfigBody.

        **参数解释：** 是否所有企业项目，标识该告警配置是否适用于所有企业项目 **约束限制：** 不涉及 **取值范围：** - true - false  **默认取值：** true

        :param is_all_enterprise_project: The is_all_enterprise_project of this CreateAlertNoticeConfigBody.
        :type is_all_enterprise_project: bool
        """
        self._is_all_enterprise_project = is_all_enterprise_project

    @property
    def description(self):
        r"""Gets the description of this CreateAlertNoticeConfigBody.

        **参数解释：** 描述，对告警通知配置的补充说明 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :return: The description of this CreateAlertNoticeConfigBody.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this CreateAlertNoticeConfigBody.

        **参数解释：** 描述，对告警通知配置的补充说明 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :param description: The description of this CreateAlertNoticeConfigBody.
        :type description: str
        """
        self._description = description

    @property
    def threat(self):
        r"""Gets the threat of this CreateAlertNoticeConfigBody.

        **参数解释：** 威胁类型范围：指定需要告警的威胁类型，如[\"all\"]表示所有威胁 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** all

        :return: The threat of this CreateAlertNoticeConfigBody.
        :rtype: list[str]
        """
        return self._threat

    @threat.setter
    def threat(self, threat):
        r"""Sets the threat of this CreateAlertNoticeConfigBody.

        **参数解释：** 威胁类型范围：指定需要告警的威胁类型，如[\"all\"]表示所有威胁 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** all

        :param threat: The threat of this CreateAlertNoticeConfigBody.
        :type threat: list[str]
        """
        self._threat = threat

    @property
    def rule_type(self):
        r"""Gets the rule_type of this CreateAlertNoticeConfigBody.

        **参数解释：** 指定需要告警的规则类型，[\"all\"]表示所有规则类型。 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** all

        :return: The rule_type of this CreateAlertNoticeConfigBody.
        :rtype: list[str]
        """
        return self._rule_type

    @rule_type.setter
    def rule_type(self, rule_type):
        r"""Sets the rule_type of this CreateAlertNoticeConfigBody.

        **参数解释：** 指定需要告警的规则类型，[\"all\"]表示所有规则类型。 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** all

        :param rule_type: The rule_type of this CreateAlertNoticeConfigBody.
        :type rule_type: list[str]
        """
        self._rule_type = rule_type

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
        if not isinstance(other, CreateAlertNoticeConfigBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

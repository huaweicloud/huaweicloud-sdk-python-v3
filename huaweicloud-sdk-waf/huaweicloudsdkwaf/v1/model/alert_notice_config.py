# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AlertNoticeConfig:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'id': 'str',
        'enabled': 'bool',
        'topic_urn': 'str',
        'sendfreq': 'int',
        'locale': 'str',
        'times': 'int',
        'name': 'str',
        'notice_class': 'str',
        'nearly_expired_time': 'int',
        'is_all_enterprise_project': 'bool',
        'description': 'str'
    }

    attribute_map = {
        'id': 'id',
        'enabled': 'enabled',
        'topic_urn': 'topic_urn',
        'sendfreq': 'sendfreq',
        'locale': 'locale',
        'times': 'times',
        'name': 'name',
        'notice_class': 'notice_class',
        'nearly_expired_time': 'nearly_expired_time',
        'is_all_enterprise_project': 'is_all_enterprise_project',
        'description': 'description'
    }

    def __init__(self, id=None, enabled=None, topic_urn=None, sendfreq=None, locale=None, times=None, name=None, notice_class=None, nearly_expired_time=None, is_all_enterprise_project=None, description=None):
        r"""AlertNoticeConfig

        The model defined in huaweicloud sdk

        :param id: **参数解释：** 告警id，用于唯一标识一条告警通知配置 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及
        :type id: str
        :param enabled: **参数解释：** 是否开启告警，控制该告警通知配置的启用/禁用状态 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及
        :type enabled: bool
        :param topic_urn: **参数解释：** 通知模板，关联用于发送告警通知的SMN主题URN **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及
        :type topic_urn: str
        :param sendfreq: **参数解释：** 通知频率，控制告警通知的发送间隔 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及
        :type sendfreq: int
        :param locale: **参数解释：** 地区，指定告警通知的语言或地域相关配置 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及
        :type locale: str
        :param times: **参数解释：** 通知频率（补充说明，与sendfreq协同控制告警发送频次） **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及
        :type times: int
        :param name: **参数解释：** 告警名称，用于标识告警通知配置的名称 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及
        :type name: str
        :param notice_class: **参数解释：** 告警类型，区分不同场景的告警（如防护规则触发、资源异常等） **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及
        :type notice_class: str
        :param nearly_expired_time: **参数解释：** 提前通知天数，针对过期类告警提前发送通知的天数 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及
        :type nearly_expired_time: int
        :param is_all_enterprise_project: **参数解释：** 是否所有企业项目，标识该告警配置是否适用于所有企业项目 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及
        :type is_all_enterprise_project: bool
        :param description: **参数解释：** 描述，对告警通知配置的补充说明 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及
        :type description: str
        """
        
        

        self._id = None
        self._enabled = None
        self._topic_urn = None
        self._sendfreq = None
        self._locale = None
        self._times = None
        self._name = None
        self._notice_class = None
        self._nearly_expired_time = None
        self._is_all_enterprise_project = None
        self._description = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if enabled is not None:
            self.enabled = enabled
        if topic_urn is not None:
            self.topic_urn = topic_urn
        if sendfreq is not None:
            self.sendfreq = sendfreq
        if locale is not None:
            self.locale = locale
        if times is not None:
            self.times = times
        if name is not None:
            self.name = name
        if notice_class is not None:
            self.notice_class = notice_class
        if nearly_expired_time is not None:
            self.nearly_expired_time = nearly_expired_time
        if is_all_enterprise_project is not None:
            self.is_all_enterprise_project = is_all_enterprise_project
        if description is not None:
            self.description = description

    @property
    def id(self):
        r"""Gets the id of this AlertNoticeConfig.

        **参数解释：** 告警id，用于唯一标识一条告警通知配置 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :return: The id of this AlertNoticeConfig.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this AlertNoticeConfig.

        **参数解释：** 告警id，用于唯一标识一条告警通知配置 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :param id: The id of this AlertNoticeConfig.
        :type id: str
        """
        self._id = id

    @property
    def enabled(self):
        r"""Gets the enabled of this AlertNoticeConfig.

        **参数解释：** 是否开启告警，控制该告警通知配置的启用/禁用状态 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :return: The enabled of this AlertNoticeConfig.
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        r"""Sets the enabled of this AlertNoticeConfig.

        **参数解释：** 是否开启告警，控制该告警通知配置的启用/禁用状态 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :param enabled: The enabled of this AlertNoticeConfig.
        :type enabled: bool
        """
        self._enabled = enabled

    @property
    def topic_urn(self):
        r"""Gets the topic_urn of this AlertNoticeConfig.

        **参数解释：** 通知模板，关联用于发送告警通知的SMN主题URN **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :return: The topic_urn of this AlertNoticeConfig.
        :rtype: str
        """
        return self._topic_urn

    @topic_urn.setter
    def topic_urn(self, topic_urn):
        r"""Sets the topic_urn of this AlertNoticeConfig.

        **参数解释：** 通知模板，关联用于发送告警通知的SMN主题URN **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :param topic_urn: The topic_urn of this AlertNoticeConfig.
        :type topic_urn: str
        """
        self._topic_urn = topic_urn

    @property
    def sendfreq(self):
        r"""Gets the sendfreq of this AlertNoticeConfig.

        **参数解释：** 通知频率，控制告警通知的发送间隔 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :return: The sendfreq of this AlertNoticeConfig.
        :rtype: int
        """
        return self._sendfreq

    @sendfreq.setter
    def sendfreq(self, sendfreq):
        r"""Sets the sendfreq of this AlertNoticeConfig.

        **参数解释：** 通知频率，控制告警通知的发送间隔 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :param sendfreq: The sendfreq of this AlertNoticeConfig.
        :type sendfreq: int
        """
        self._sendfreq = sendfreq

    @property
    def locale(self):
        r"""Gets the locale of this AlertNoticeConfig.

        **参数解释：** 地区，指定告警通知的语言或地域相关配置 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :return: The locale of this AlertNoticeConfig.
        :rtype: str
        """
        return self._locale

    @locale.setter
    def locale(self, locale):
        r"""Sets the locale of this AlertNoticeConfig.

        **参数解释：** 地区，指定告警通知的语言或地域相关配置 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :param locale: The locale of this AlertNoticeConfig.
        :type locale: str
        """
        self._locale = locale

    @property
    def times(self):
        r"""Gets the times of this AlertNoticeConfig.

        **参数解释：** 通知频率（补充说明，与sendfreq协同控制告警发送频次） **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :return: The times of this AlertNoticeConfig.
        :rtype: int
        """
        return self._times

    @times.setter
    def times(self, times):
        r"""Sets the times of this AlertNoticeConfig.

        **参数解释：** 通知频率（补充说明，与sendfreq协同控制告警发送频次） **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :param times: The times of this AlertNoticeConfig.
        :type times: int
        """
        self._times = times

    @property
    def name(self):
        r"""Gets the name of this AlertNoticeConfig.

        **参数解释：** 告警名称，用于标识告警通知配置的名称 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :return: The name of this AlertNoticeConfig.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this AlertNoticeConfig.

        **参数解释：** 告警名称，用于标识告警通知配置的名称 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :param name: The name of this AlertNoticeConfig.
        :type name: str
        """
        self._name = name

    @property
    def notice_class(self):
        r"""Gets the notice_class of this AlertNoticeConfig.

        **参数解释：** 告警类型，区分不同场景的告警（如防护规则触发、资源异常等） **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :return: The notice_class of this AlertNoticeConfig.
        :rtype: str
        """
        return self._notice_class

    @notice_class.setter
    def notice_class(self, notice_class):
        r"""Sets the notice_class of this AlertNoticeConfig.

        **参数解释：** 告警类型，区分不同场景的告警（如防护规则触发、资源异常等） **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :param notice_class: The notice_class of this AlertNoticeConfig.
        :type notice_class: str
        """
        self._notice_class = notice_class

    @property
    def nearly_expired_time(self):
        r"""Gets the nearly_expired_time of this AlertNoticeConfig.

        **参数解释：** 提前通知天数，针对过期类告警提前发送通知的天数 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :return: The nearly_expired_time of this AlertNoticeConfig.
        :rtype: int
        """
        return self._nearly_expired_time

    @nearly_expired_time.setter
    def nearly_expired_time(self, nearly_expired_time):
        r"""Sets the nearly_expired_time of this AlertNoticeConfig.

        **参数解释：** 提前通知天数，针对过期类告警提前发送通知的天数 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :param nearly_expired_time: The nearly_expired_time of this AlertNoticeConfig.
        :type nearly_expired_time: int
        """
        self._nearly_expired_time = nearly_expired_time

    @property
    def is_all_enterprise_project(self):
        r"""Gets the is_all_enterprise_project of this AlertNoticeConfig.

        **参数解释：** 是否所有企业项目，标识该告警配置是否适用于所有企业项目 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :return: The is_all_enterprise_project of this AlertNoticeConfig.
        :rtype: bool
        """
        return self._is_all_enterprise_project

    @is_all_enterprise_project.setter
    def is_all_enterprise_project(self, is_all_enterprise_project):
        r"""Sets the is_all_enterprise_project of this AlertNoticeConfig.

        **参数解释：** 是否所有企业项目，标识该告警配置是否适用于所有企业项目 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :param is_all_enterprise_project: The is_all_enterprise_project of this AlertNoticeConfig.
        :type is_all_enterprise_project: bool
        """
        self._is_all_enterprise_project = is_all_enterprise_project

    @property
    def description(self):
        r"""Gets the description of this AlertNoticeConfig.

        **参数解释：** 描述，对告警通知配置的补充说明 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :return: The description of this AlertNoticeConfig.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this AlertNoticeConfig.

        **参数解释：** 描述，对告警通知配置的补充说明 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :param description: The description of this AlertNoticeConfig.
        :type description: str
        """
        self._description = description

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
        if not isinstance(other, AlertNoticeConfig):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

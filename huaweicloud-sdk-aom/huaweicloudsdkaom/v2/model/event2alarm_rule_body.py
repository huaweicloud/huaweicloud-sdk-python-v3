# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Event2alarmRuleBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'user_id': 'str',
        'name': 'str',
        'description': 'str',
        'create_time': 'int',
        'update_time': 'int',
        'resource_provider': 'str',
        'metadata': 'Event2alarmRuleBodyMetadata',
        'enable': 'bool',
        'trigger_policies': 'list[Event2alarmRuleBodyTriggerPolicies]',
        'alarm_type': 'str',
        'action_rule': 'str',
        'inhibit_rule': 'str',
        'route_group_rule': 'str',
        'event_names': 'list[str]',
        'migrated': 'bool',
        'topics': 'list[SmnTopics]'
    }

    attribute_map = {
        'user_id': 'user_id',
        'name': 'name',
        'description': 'description',
        'create_time': 'create_time',
        'update_time': 'update_time',
        'resource_provider': 'resource_provider',
        'metadata': 'metadata',
        'enable': 'enable',
        'trigger_policies': 'trigger_policies',
        'alarm_type': 'alarm_type',
        'action_rule': 'action_rule',
        'inhibit_rule': 'inhibit_rule',
        'route_group_rule': 'route_group_rule',
        'event_names': 'event_names',
        'migrated': 'migrated',
        'topics': 'topics'
    }

    def __init__(self, user_id=None, name=None, description=None, create_time=None, update_time=None, resource_provider=None, metadata=None, enable=None, trigger_policies=None, alarm_type=None, action_rule=None, inhibit_rule=None, route_group_rule=None, event_names=None, migrated=None, topics=None):
        r"""Event2alarmRuleBody

        The model defined in huaweicloud sdk

        :param user_id: 用户项目id
        :type user_id: str
        :param name: 规则名称。规则名称包含大小写字母，数字，特殊字符（_-）和汉字组成，不能以特殊字符开头或结尾，最大长度为100。
        :type name: str
        :param description: 规则描述。描述包含大小写字母，数字，特殊字符（_-&lt;&gt;&#x3D;,.）和汉字组成，不能以下划线、中划线开头结尾，最大长度为1024。
        :type description: str
        :param create_time: 创建时间
        :type create_time: int
        :param update_time: 更新时间
        :type update_time: int
        :param resource_provider: 事件源
        :type resource_provider: str
        :param metadata: 
        :type metadata: :class:`huaweicloudsdkaom.v2.Event2alarmRuleBodyMetadata`
        :param enable: 规则是否启用
        :type enable: bool
        :param trigger_policies: 触发策略
        :type trigger_policies: list[:class:`huaweicloudsdkaom.v2.Event2alarmRuleBodyTriggerPolicies`]
        :param alarm_type: 告警类型。notification：直接告警。denoising：告警降噪。
        :type alarm_type: str
        :param action_rule: 告警行动规则
        :type action_rule: str
        :param inhibit_rule: 告警抑制规则
        :type inhibit_rule: str
        :param route_group_rule: 告警分组规则
        :type route_group_rule: str
        :param event_names: 事件名称
        :type event_names: list[str]
        :param migrated: 是否迁移到2.0
        :type migrated: bool
        :param topics: smn信息
        :type topics: list[:class:`huaweicloudsdkaom.v2.SmnTopics`]
        """
        
        

        self._user_id = None
        self._name = None
        self._description = None
        self._create_time = None
        self._update_time = None
        self._resource_provider = None
        self._metadata = None
        self._enable = None
        self._trigger_policies = None
        self._alarm_type = None
        self._action_rule = None
        self._inhibit_rule = None
        self._route_group_rule = None
        self._event_names = None
        self._migrated = None
        self._topics = None
        self.discriminator = None

        self.user_id = user_id
        self.name = name
        if description is not None:
            self.description = description
        self.create_time = create_time
        if update_time is not None:
            self.update_time = update_time
        if resource_provider is not None:
            self.resource_provider = resource_provider
        self.metadata = metadata
        self.enable = enable
        self.trigger_policies = trigger_policies
        self.alarm_type = alarm_type
        self.action_rule = action_rule
        if inhibit_rule is not None:
            self.inhibit_rule = inhibit_rule
        if route_group_rule is not None:
            self.route_group_rule = route_group_rule
        if event_names is not None:
            self.event_names = event_names
        if migrated is not None:
            self.migrated = migrated
        if topics is not None:
            self.topics = topics

    @property
    def user_id(self):
        r"""Gets the user_id of this Event2alarmRuleBody.

        用户项目id

        :return: The user_id of this Event2alarmRuleBody.
        :rtype: str
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        r"""Sets the user_id of this Event2alarmRuleBody.

        用户项目id

        :param user_id: The user_id of this Event2alarmRuleBody.
        :type user_id: str
        """
        self._user_id = user_id

    @property
    def name(self):
        r"""Gets the name of this Event2alarmRuleBody.

        规则名称。规则名称包含大小写字母，数字，特殊字符（_-）和汉字组成，不能以特殊字符开头或结尾，最大长度为100。

        :return: The name of this Event2alarmRuleBody.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this Event2alarmRuleBody.

        规则名称。规则名称包含大小写字母，数字，特殊字符（_-）和汉字组成，不能以特殊字符开头或结尾，最大长度为100。

        :param name: The name of this Event2alarmRuleBody.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        r"""Gets the description of this Event2alarmRuleBody.

        规则描述。描述包含大小写字母，数字，特殊字符（_-<>=,.）和汉字组成，不能以下划线、中划线开头结尾，最大长度为1024。

        :return: The description of this Event2alarmRuleBody.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this Event2alarmRuleBody.

        规则描述。描述包含大小写字母，数字，特殊字符（_-<>=,.）和汉字组成，不能以下划线、中划线开头结尾，最大长度为1024。

        :param description: The description of this Event2alarmRuleBody.
        :type description: str
        """
        self._description = description

    @property
    def create_time(self):
        r"""Gets the create_time of this Event2alarmRuleBody.

        创建时间

        :return: The create_time of this Event2alarmRuleBody.
        :rtype: int
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        r"""Sets the create_time of this Event2alarmRuleBody.

        创建时间

        :param create_time: The create_time of this Event2alarmRuleBody.
        :type create_time: int
        """
        self._create_time = create_time

    @property
    def update_time(self):
        r"""Gets the update_time of this Event2alarmRuleBody.

        更新时间

        :return: The update_time of this Event2alarmRuleBody.
        :rtype: int
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        r"""Sets the update_time of this Event2alarmRuleBody.

        更新时间

        :param update_time: The update_time of this Event2alarmRuleBody.
        :type update_time: int
        """
        self._update_time = update_time

    @property
    def resource_provider(self):
        r"""Gets the resource_provider of this Event2alarmRuleBody.

        事件源

        :return: The resource_provider of this Event2alarmRuleBody.
        :rtype: str
        """
        return self._resource_provider

    @resource_provider.setter
    def resource_provider(self, resource_provider):
        r"""Sets the resource_provider of this Event2alarmRuleBody.

        事件源

        :param resource_provider: The resource_provider of this Event2alarmRuleBody.
        :type resource_provider: str
        """
        self._resource_provider = resource_provider

    @property
    def metadata(self):
        r"""Gets the metadata of this Event2alarmRuleBody.

        :return: The metadata of this Event2alarmRuleBody.
        :rtype: :class:`huaweicloudsdkaom.v2.Event2alarmRuleBodyMetadata`
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        r"""Sets the metadata of this Event2alarmRuleBody.

        :param metadata: The metadata of this Event2alarmRuleBody.
        :type metadata: :class:`huaweicloudsdkaom.v2.Event2alarmRuleBodyMetadata`
        """
        self._metadata = metadata

    @property
    def enable(self):
        r"""Gets the enable of this Event2alarmRuleBody.

        规则是否启用

        :return: The enable of this Event2alarmRuleBody.
        :rtype: bool
        """
        return self._enable

    @enable.setter
    def enable(self, enable):
        r"""Sets the enable of this Event2alarmRuleBody.

        规则是否启用

        :param enable: The enable of this Event2alarmRuleBody.
        :type enable: bool
        """
        self._enable = enable

    @property
    def trigger_policies(self):
        r"""Gets the trigger_policies of this Event2alarmRuleBody.

        触发策略

        :return: The trigger_policies of this Event2alarmRuleBody.
        :rtype: list[:class:`huaweicloudsdkaom.v2.Event2alarmRuleBodyTriggerPolicies`]
        """
        return self._trigger_policies

    @trigger_policies.setter
    def trigger_policies(self, trigger_policies):
        r"""Sets the trigger_policies of this Event2alarmRuleBody.

        触发策略

        :param trigger_policies: The trigger_policies of this Event2alarmRuleBody.
        :type trigger_policies: list[:class:`huaweicloudsdkaom.v2.Event2alarmRuleBodyTriggerPolicies`]
        """
        self._trigger_policies = trigger_policies

    @property
    def alarm_type(self):
        r"""Gets the alarm_type of this Event2alarmRuleBody.

        告警类型。notification：直接告警。denoising：告警降噪。

        :return: The alarm_type of this Event2alarmRuleBody.
        :rtype: str
        """
        return self._alarm_type

    @alarm_type.setter
    def alarm_type(self, alarm_type):
        r"""Sets the alarm_type of this Event2alarmRuleBody.

        告警类型。notification：直接告警。denoising：告警降噪。

        :param alarm_type: The alarm_type of this Event2alarmRuleBody.
        :type alarm_type: str
        """
        self._alarm_type = alarm_type

    @property
    def action_rule(self):
        r"""Gets the action_rule of this Event2alarmRuleBody.

        告警行动规则

        :return: The action_rule of this Event2alarmRuleBody.
        :rtype: str
        """
        return self._action_rule

    @action_rule.setter
    def action_rule(self, action_rule):
        r"""Sets the action_rule of this Event2alarmRuleBody.

        告警行动规则

        :param action_rule: The action_rule of this Event2alarmRuleBody.
        :type action_rule: str
        """
        self._action_rule = action_rule

    @property
    def inhibit_rule(self):
        r"""Gets the inhibit_rule of this Event2alarmRuleBody.

        告警抑制规则

        :return: The inhibit_rule of this Event2alarmRuleBody.
        :rtype: str
        """
        return self._inhibit_rule

    @inhibit_rule.setter
    def inhibit_rule(self, inhibit_rule):
        r"""Sets the inhibit_rule of this Event2alarmRuleBody.

        告警抑制规则

        :param inhibit_rule: The inhibit_rule of this Event2alarmRuleBody.
        :type inhibit_rule: str
        """
        self._inhibit_rule = inhibit_rule

    @property
    def route_group_rule(self):
        r"""Gets the route_group_rule of this Event2alarmRuleBody.

        告警分组规则

        :return: The route_group_rule of this Event2alarmRuleBody.
        :rtype: str
        """
        return self._route_group_rule

    @route_group_rule.setter
    def route_group_rule(self, route_group_rule):
        r"""Sets the route_group_rule of this Event2alarmRuleBody.

        告警分组规则

        :param route_group_rule: The route_group_rule of this Event2alarmRuleBody.
        :type route_group_rule: str
        """
        self._route_group_rule = route_group_rule

    @property
    def event_names(self):
        r"""Gets the event_names of this Event2alarmRuleBody.

        事件名称

        :return: The event_names of this Event2alarmRuleBody.
        :rtype: list[str]
        """
        return self._event_names

    @event_names.setter
    def event_names(self, event_names):
        r"""Sets the event_names of this Event2alarmRuleBody.

        事件名称

        :param event_names: The event_names of this Event2alarmRuleBody.
        :type event_names: list[str]
        """
        self._event_names = event_names

    @property
    def migrated(self):
        r"""Gets the migrated of this Event2alarmRuleBody.

        是否迁移到2.0

        :return: The migrated of this Event2alarmRuleBody.
        :rtype: bool
        """
        return self._migrated

    @migrated.setter
    def migrated(self, migrated):
        r"""Sets the migrated of this Event2alarmRuleBody.

        是否迁移到2.0

        :param migrated: The migrated of this Event2alarmRuleBody.
        :type migrated: bool
        """
        self._migrated = migrated

    @property
    def topics(self):
        r"""Gets the topics of this Event2alarmRuleBody.

        smn信息

        :return: The topics of this Event2alarmRuleBody.
        :rtype: list[:class:`huaweicloudsdkaom.v2.SmnTopics`]
        """
        return self._topics

    @topics.setter
    def topics(self, topics):
        r"""Sets the topics of this Event2alarmRuleBody.

        smn信息

        :param topics: The topics of this Event2alarmRuleBody.
        :type topics: list[:class:`huaweicloudsdkaom.v2.SmnTopics`]
        """
        self._topics = topics

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
        if not isinstance(other, Event2alarmRuleBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

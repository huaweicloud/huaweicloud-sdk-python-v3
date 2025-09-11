# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PostAlarmsReqV2:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'name': 'str',
        'description': 'str',
        'namespace': 'str',
        'resource_group_id': 'str',
        'resources': 'list[list[Dimension]]',
        'policies': 'list[Policy]',
        'type': 'AlarmType',
        'alarm_notifications': 'list[Notification]',
        'ok_notifications': 'list[Notification]',
        'notification_begin_time': 'str',
        'notification_end_time': 'str',
        'effective_timezone': 'str',
        'enterprise_project_id': 'str',
        'enabled': 'bool',
        'notification_enabled': 'bool',
        'alarm_template_id': 'str',
        'tags': 'list[ResourceTag]',
        'product_name': 'str',
        'resource_level': 'str'
    }

    attribute_map = {
        'name': 'name',
        'description': 'description',
        'namespace': 'namespace',
        'resource_group_id': 'resource_group_id',
        'resources': 'resources',
        'policies': 'policies',
        'type': 'type',
        'alarm_notifications': 'alarm_notifications',
        'ok_notifications': 'ok_notifications',
        'notification_begin_time': 'notification_begin_time',
        'notification_end_time': 'notification_end_time',
        'effective_timezone': 'effective_timezone',
        'enterprise_project_id': 'enterprise_project_id',
        'enabled': 'enabled',
        'notification_enabled': 'notification_enabled',
        'alarm_template_id': 'alarm_template_id',
        'tags': 'tags',
        'product_name': 'product_name',
        'resource_level': 'resource_level'
    }

    def __init__(self, name=None, description=None, namespace=None, resource_group_id=None, resources=None, policies=None, type=None, alarm_notifications=None, ok_notifications=None, notification_begin_time=None, notification_end_time=None, effective_timezone=None, enterprise_project_id=None, enabled=None, notification_enabled=None, alarm_template_id=None, tags=None, product_name=None, resource_level=None):
        r"""PostAlarmsReqV2

        The model defined in huaweicloud sdk

        :param name: **参数解释**： 告警名称。 **约束限制**： 不涉及。 **取值范围**： 只能包含0-9/a-z/A-Z/_/-或汉字，长度[1，128]个字符。           **默认取值**： 不涉及。 
        :type name: str
        :param description: **参数解释**： 告警描述。     **约束限制**： 不涉及。 **取值范围**： 长度为[0,256]个字符。        **默认取值**： 不涉及。 
        :type description: str
        :param namespace: **参数解释**： 查询服务的命名空间，各服务命名空间请参考“[服务命名名称](ces_03_0059.xml)”。    **约束限制**： 不涉及。 **取值范围**： 格式为service.item；service和item必须是字符串，必须以字母开头，只能包含0-9/a-z/A-Z/_。字符串的长度在 0 到 32个字符之间。        **默认取值**： 不涉及。 
        :type namespace: str
        :param resource_group_id: **参数解释**： 资源分组ID     **约束限制**： 不涉及。  **取值范围**： 以rg开头，后跟22位由字母或数字组成的字符串。长度为[2,24]个字符。       **默认取值**： 不涉及。 
        :type resource_group_id: str
        :param resources: **参数解释**： 资源列表。 **约束限制**： 告警规则类型为全部资源、资源分组时，资源维度值传空；告警规则类型为指定资源时，资源维度值必填，可以同时指定监控多个资源。 最多可以指定1000个资源维度。 
        :type resources: list[list[Dimension]]
        :param policies: **参数解释**： 告警策略。 **约束限制**： 当alarm_template_id字段为空时必填，不为空时不填。最多包含50个策略。 
        :type policies: list[:class:`huaweicloudsdkces.v2.Policy`]
        :param type: 
        :type type: :class:`huaweicloudsdkces.v2.AlarmType`
        :param alarm_notifications: **参数解释**： 触发告警时，通知组/主题订阅的信息。 **约束限制**： 不涉及。 **取值范围**： 包含的通知信息的数量最多为10个。 **默认取值**： 不涉及。 
        :type alarm_notifications: list[:class:`huaweicloudsdkces.v2.Notification`]
        :param ok_notifications: **参数解释**： 告警恢复时，通知组/主题订阅的信息。 **约束限制**： 不涉及。 **取值范围**： 包含的通知信息的数量最多为10个。 **默认取值**： 不涉及。 
        :type ok_notifications: list[:class:`huaweicloudsdkces.v2.Notification`]
        :param notification_begin_time: **参数解释**： 告警通知开启时间。    **约束限制**： 不涉及。 **取值范围**： 只能包含数字、“:”，长度为[1,64]个字符。           **默认取值**： 不涉及。 
        :type notification_begin_time: str
        :param notification_end_time: **参数解释**： 告警通知关闭时间。    **约束限制**： 不涉及。 **取值范围**： 只能包含数字、“:”，长度为[1,64]个字符。           **默认取值**： 不涉及。 
        :type notification_end_time: str
        :param effective_timezone: **参数解释**： 时区，形如：\&quot;GMT-08:00\&quot;、\&quot;GMT+08:00\&quot;、\&quot;GMT+0:00\&quot;。    **约束限制**： 不涉及。 **取值范围**： 长度为[1,16]个字符。           **默认取值**： 不涉及。 
        :type effective_timezone: str
        :param enterprise_project_id: **参数解释**： 企业项目ID。     **约束限制**： 不涉及。 **取值范围**： 只能包含小写字母、数字、“-”。           **默认取值**： 不涉及。 
        :type enterprise_project_id: str
        :param enabled: **参数解释**： 是否开启告警规则。     **约束限制**： 不涉及。 **取值范围**： 布尔值。 - true:开启。 - false:关闭。 **默认取值**： true 
        :type enabled: bool
        :param notification_enabled: **参数解释**： 是否开启告警通知。     **约束限制**： 不涉及。 **取值范围**： 布尔值。 - true:开启。 - false:关闭。 **默认取值**： true 
        :type notification_enabled: bool
        :param alarm_template_id: **参数解释**： 告警规则关联告警模板ID，如果传了，告警规则关联的策略会和告警模板策略联动变化。     **约束限制**： 不涉及。 **取值范围**： 以at开头，只包含字母、数字，长度为[2,64]个字符。          **默认取值**： 不涉及。 
        :type alarm_template_id: str
        :param tags: **参数解释**： 租户标签列表。 **约束限制**： 最多包含20个标签。 
        :type tags: list[:class:`huaweicloudsdkces.v2.ResourceTag`]
        :param product_name: **参数解释**： 产品层级跨维规则创建时需要指明的规则产品名称，一般由\&quot;服务命名空间,服务首层维度名称\&quot;组成，如\&quot;SYS.ECS,instance_id\&quot;。 **约束限制**： 不涉及。 **取值范围**： 长度为[0,128]个字符。          **默认取值**： 不涉及。 
        :type product_name: str
        :param resource_level: **参数解释**： 产品层级跨维规则创建时需要指明为产品层级规则，resource_level取值为product即为云产品类型，不填或者取值为dimension则为子维度类型。 **约束限制**： 不涉及。 **取值范围**： 枚举值。 - product：云产品。 - dimension：子维度。 **默认取值**： 子维度。 
        :type resource_level: str
        """
        
        

        self._name = None
        self._description = None
        self._namespace = None
        self._resource_group_id = None
        self._resources = None
        self._policies = None
        self._type = None
        self._alarm_notifications = None
        self._ok_notifications = None
        self._notification_begin_time = None
        self._notification_end_time = None
        self._effective_timezone = None
        self._enterprise_project_id = None
        self._enabled = None
        self._notification_enabled = None
        self._alarm_template_id = None
        self._tags = None
        self._product_name = None
        self._resource_level = None
        self.discriminator = None

        self.name = name
        if description is not None:
            self.description = description
        self.namespace = namespace
        if resource_group_id is not None:
            self.resource_group_id = resource_group_id
        self.resources = resources
        if policies is not None:
            self.policies = policies
        self.type = type
        if alarm_notifications is not None:
            self.alarm_notifications = alarm_notifications
        if ok_notifications is not None:
            self.ok_notifications = ok_notifications
        if notification_begin_time is not None:
            self.notification_begin_time = notification_begin_time
        if notification_end_time is not None:
            self.notification_end_time = notification_end_time
        if effective_timezone is not None:
            self.effective_timezone = effective_timezone
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        self.enabled = enabled
        self.notification_enabled = notification_enabled
        if alarm_template_id is not None:
            self.alarm_template_id = alarm_template_id
        if tags is not None:
            self.tags = tags
        if product_name is not None:
            self.product_name = product_name
        if resource_level is not None:
            self.resource_level = resource_level

    @property
    def name(self):
        r"""Gets the name of this PostAlarmsReqV2.

        **参数解释**： 告警名称。 **约束限制**： 不涉及。 **取值范围**： 只能包含0-9/a-z/A-Z/_/-或汉字，长度[1，128]个字符。           **默认取值**： 不涉及。 

        :return: The name of this PostAlarmsReqV2.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this PostAlarmsReqV2.

        **参数解释**： 告警名称。 **约束限制**： 不涉及。 **取值范围**： 只能包含0-9/a-z/A-Z/_/-或汉字，长度[1，128]个字符。           **默认取值**： 不涉及。 

        :param name: The name of this PostAlarmsReqV2.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        r"""Gets the description of this PostAlarmsReqV2.

        **参数解释**： 告警描述。     **约束限制**： 不涉及。 **取值范围**： 长度为[0,256]个字符。        **默认取值**： 不涉及。 

        :return: The description of this PostAlarmsReqV2.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this PostAlarmsReqV2.

        **参数解释**： 告警描述。     **约束限制**： 不涉及。 **取值范围**： 长度为[0,256]个字符。        **默认取值**： 不涉及。 

        :param description: The description of this PostAlarmsReqV2.
        :type description: str
        """
        self._description = description

    @property
    def namespace(self):
        r"""Gets the namespace of this PostAlarmsReqV2.

        **参数解释**： 查询服务的命名空间，各服务命名空间请参考“[服务命名名称](ces_03_0059.xml)”。    **约束限制**： 不涉及。 **取值范围**： 格式为service.item；service和item必须是字符串，必须以字母开头，只能包含0-9/a-z/A-Z/_。字符串的长度在 0 到 32个字符之间。        **默认取值**： 不涉及。 

        :return: The namespace of this PostAlarmsReqV2.
        :rtype: str
        """
        return self._namespace

    @namespace.setter
    def namespace(self, namespace):
        r"""Sets the namespace of this PostAlarmsReqV2.

        **参数解释**： 查询服务的命名空间，各服务命名空间请参考“[服务命名名称](ces_03_0059.xml)”。    **约束限制**： 不涉及。 **取值范围**： 格式为service.item；service和item必须是字符串，必须以字母开头，只能包含0-9/a-z/A-Z/_。字符串的长度在 0 到 32个字符之间。        **默认取值**： 不涉及。 

        :param namespace: The namespace of this PostAlarmsReqV2.
        :type namespace: str
        """
        self._namespace = namespace

    @property
    def resource_group_id(self):
        r"""Gets the resource_group_id of this PostAlarmsReqV2.

        **参数解释**： 资源分组ID     **约束限制**： 不涉及。  **取值范围**： 以rg开头，后跟22位由字母或数字组成的字符串。长度为[2,24]个字符。       **默认取值**： 不涉及。 

        :return: The resource_group_id of this PostAlarmsReqV2.
        :rtype: str
        """
        return self._resource_group_id

    @resource_group_id.setter
    def resource_group_id(self, resource_group_id):
        r"""Sets the resource_group_id of this PostAlarmsReqV2.

        **参数解释**： 资源分组ID     **约束限制**： 不涉及。  **取值范围**： 以rg开头，后跟22位由字母或数字组成的字符串。长度为[2,24]个字符。       **默认取值**： 不涉及。 

        :param resource_group_id: The resource_group_id of this PostAlarmsReqV2.
        :type resource_group_id: str
        """
        self._resource_group_id = resource_group_id

    @property
    def resources(self):
        r"""Gets the resources of this PostAlarmsReqV2.

        **参数解释**： 资源列表。 **约束限制**： 告警规则类型为全部资源、资源分组时，资源维度值传空；告警规则类型为指定资源时，资源维度值必填，可以同时指定监控多个资源。 最多可以指定1000个资源维度。 

        :return: The resources of this PostAlarmsReqV2.
        :rtype: list[list[Dimension]]
        """
        return self._resources

    @resources.setter
    def resources(self, resources):
        r"""Sets the resources of this PostAlarmsReqV2.

        **参数解释**： 资源列表。 **约束限制**： 告警规则类型为全部资源、资源分组时，资源维度值传空；告警规则类型为指定资源时，资源维度值必填，可以同时指定监控多个资源。 最多可以指定1000个资源维度。 

        :param resources: The resources of this PostAlarmsReqV2.
        :type resources: list[list[Dimension]]
        """
        self._resources = resources

    @property
    def policies(self):
        r"""Gets the policies of this PostAlarmsReqV2.

        **参数解释**： 告警策略。 **约束限制**： 当alarm_template_id字段为空时必填，不为空时不填。最多包含50个策略。 

        :return: The policies of this PostAlarmsReqV2.
        :rtype: list[:class:`huaweicloudsdkces.v2.Policy`]
        """
        return self._policies

    @policies.setter
    def policies(self, policies):
        r"""Sets the policies of this PostAlarmsReqV2.

        **参数解释**： 告警策略。 **约束限制**： 当alarm_template_id字段为空时必填，不为空时不填。最多包含50个策略。 

        :param policies: The policies of this PostAlarmsReqV2.
        :type policies: list[:class:`huaweicloudsdkces.v2.Policy`]
        """
        self._policies = policies

    @property
    def type(self):
        r"""Gets the type of this PostAlarmsReqV2.

        :return: The type of this PostAlarmsReqV2.
        :rtype: :class:`huaweicloudsdkces.v2.AlarmType`
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this PostAlarmsReqV2.

        :param type: The type of this PostAlarmsReqV2.
        :type type: :class:`huaweicloudsdkces.v2.AlarmType`
        """
        self._type = type

    @property
    def alarm_notifications(self):
        r"""Gets the alarm_notifications of this PostAlarmsReqV2.

        **参数解释**： 触发告警时，通知组/主题订阅的信息。 **约束限制**： 不涉及。 **取值范围**： 包含的通知信息的数量最多为10个。 **默认取值**： 不涉及。 

        :return: The alarm_notifications of this PostAlarmsReqV2.
        :rtype: list[:class:`huaweicloudsdkces.v2.Notification`]
        """
        return self._alarm_notifications

    @alarm_notifications.setter
    def alarm_notifications(self, alarm_notifications):
        r"""Sets the alarm_notifications of this PostAlarmsReqV2.

        **参数解释**： 触发告警时，通知组/主题订阅的信息。 **约束限制**： 不涉及。 **取值范围**： 包含的通知信息的数量最多为10个。 **默认取值**： 不涉及。 

        :param alarm_notifications: The alarm_notifications of this PostAlarmsReqV2.
        :type alarm_notifications: list[:class:`huaweicloudsdkces.v2.Notification`]
        """
        self._alarm_notifications = alarm_notifications

    @property
    def ok_notifications(self):
        r"""Gets the ok_notifications of this PostAlarmsReqV2.

        **参数解释**： 告警恢复时，通知组/主题订阅的信息。 **约束限制**： 不涉及。 **取值范围**： 包含的通知信息的数量最多为10个。 **默认取值**： 不涉及。 

        :return: The ok_notifications of this PostAlarmsReqV2.
        :rtype: list[:class:`huaweicloudsdkces.v2.Notification`]
        """
        return self._ok_notifications

    @ok_notifications.setter
    def ok_notifications(self, ok_notifications):
        r"""Sets the ok_notifications of this PostAlarmsReqV2.

        **参数解释**： 告警恢复时，通知组/主题订阅的信息。 **约束限制**： 不涉及。 **取值范围**： 包含的通知信息的数量最多为10个。 **默认取值**： 不涉及。 

        :param ok_notifications: The ok_notifications of this PostAlarmsReqV2.
        :type ok_notifications: list[:class:`huaweicloudsdkces.v2.Notification`]
        """
        self._ok_notifications = ok_notifications

    @property
    def notification_begin_time(self):
        r"""Gets the notification_begin_time of this PostAlarmsReqV2.

        **参数解释**： 告警通知开启时间。    **约束限制**： 不涉及。 **取值范围**： 只能包含数字、“:”，长度为[1,64]个字符。           **默认取值**： 不涉及。 

        :return: The notification_begin_time of this PostAlarmsReqV2.
        :rtype: str
        """
        return self._notification_begin_time

    @notification_begin_time.setter
    def notification_begin_time(self, notification_begin_time):
        r"""Sets the notification_begin_time of this PostAlarmsReqV2.

        **参数解释**： 告警通知开启时间。    **约束限制**： 不涉及。 **取值范围**： 只能包含数字、“:”，长度为[1,64]个字符。           **默认取值**： 不涉及。 

        :param notification_begin_time: The notification_begin_time of this PostAlarmsReqV2.
        :type notification_begin_time: str
        """
        self._notification_begin_time = notification_begin_time

    @property
    def notification_end_time(self):
        r"""Gets the notification_end_time of this PostAlarmsReqV2.

        **参数解释**： 告警通知关闭时间。    **约束限制**： 不涉及。 **取值范围**： 只能包含数字、“:”，长度为[1,64]个字符。           **默认取值**： 不涉及。 

        :return: The notification_end_time of this PostAlarmsReqV2.
        :rtype: str
        """
        return self._notification_end_time

    @notification_end_time.setter
    def notification_end_time(self, notification_end_time):
        r"""Sets the notification_end_time of this PostAlarmsReqV2.

        **参数解释**： 告警通知关闭时间。    **约束限制**： 不涉及。 **取值范围**： 只能包含数字、“:”，长度为[1,64]个字符。           **默认取值**： 不涉及。 

        :param notification_end_time: The notification_end_time of this PostAlarmsReqV2.
        :type notification_end_time: str
        """
        self._notification_end_time = notification_end_time

    @property
    def effective_timezone(self):
        r"""Gets the effective_timezone of this PostAlarmsReqV2.

        **参数解释**： 时区，形如：\"GMT-08:00\"、\"GMT+08:00\"、\"GMT+0:00\"。    **约束限制**： 不涉及。 **取值范围**： 长度为[1,16]个字符。           **默认取值**： 不涉及。 

        :return: The effective_timezone of this PostAlarmsReqV2.
        :rtype: str
        """
        return self._effective_timezone

    @effective_timezone.setter
    def effective_timezone(self, effective_timezone):
        r"""Sets the effective_timezone of this PostAlarmsReqV2.

        **参数解释**： 时区，形如：\"GMT-08:00\"、\"GMT+08:00\"、\"GMT+0:00\"。    **约束限制**： 不涉及。 **取值范围**： 长度为[1,16]个字符。           **默认取值**： 不涉及。 

        :param effective_timezone: The effective_timezone of this PostAlarmsReqV2.
        :type effective_timezone: str
        """
        self._effective_timezone = effective_timezone

    @property
    def enterprise_project_id(self):
        r"""Gets the enterprise_project_id of this PostAlarmsReqV2.

        **参数解释**： 企业项目ID。     **约束限制**： 不涉及。 **取值范围**： 只能包含小写字母、数字、“-”。           **默认取值**： 不涉及。 

        :return: The enterprise_project_id of this PostAlarmsReqV2.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        r"""Sets the enterprise_project_id of this PostAlarmsReqV2.

        **参数解释**： 企业项目ID。     **约束限制**： 不涉及。 **取值范围**： 只能包含小写字母、数字、“-”。           **默认取值**： 不涉及。 

        :param enterprise_project_id: The enterprise_project_id of this PostAlarmsReqV2.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def enabled(self):
        r"""Gets the enabled of this PostAlarmsReqV2.

        **参数解释**： 是否开启告警规则。     **约束限制**： 不涉及。 **取值范围**： 布尔值。 - true:开启。 - false:关闭。 **默认取值**： true 

        :return: The enabled of this PostAlarmsReqV2.
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        r"""Sets the enabled of this PostAlarmsReqV2.

        **参数解释**： 是否开启告警规则。     **约束限制**： 不涉及。 **取值范围**： 布尔值。 - true:开启。 - false:关闭。 **默认取值**： true 

        :param enabled: The enabled of this PostAlarmsReqV2.
        :type enabled: bool
        """
        self._enabled = enabled

    @property
    def notification_enabled(self):
        r"""Gets the notification_enabled of this PostAlarmsReqV2.

        **参数解释**： 是否开启告警通知。     **约束限制**： 不涉及。 **取值范围**： 布尔值。 - true:开启。 - false:关闭。 **默认取值**： true 

        :return: The notification_enabled of this PostAlarmsReqV2.
        :rtype: bool
        """
        return self._notification_enabled

    @notification_enabled.setter
    def notification_enabled(self, notification_enabled):
        r"""Sets the notification_enabled of this PostAlarmsReqV2.

        **参数解释**： 是否开启告警通知。     **约束限制**： 不涉及。 **取值范围**： 布尔值。 - true:开启。 - false:关闭。 **默认取值**： true 

        :param notification_enabled: The notification_enabled of this PostAlarmsReqV2.
        :type notification_enabled: bool
        """
        self._notification_enabled = notification_enabled

    @property
    def alarm_template_id(self):
        r"""Gets the alarm_template_id of this PostAlarmsReqV2.

        **参数解释**： 告警规则关联告警模板ID，如果传了，告警规则关联的策略会和告警模板策略联动变化。     **约束限制**： 不涉及。 **取值范围**： 以at开头，只包含字母、数字，长度为[2,64]个字符。          **默认取值**： 不涉及。 

        :return: The alarm_template_id of this PostAlarmsReqV2.
        :rtype: str
        """
        return self._alarm_template_id

    @alarm_template_id.setter
    def alarm_template_id(self, alarm_template_id):
        r"""Sets the alarm_template_id of this PostAlarmsReqV2.

        **参数解释**： 告警规则关联告警模板ID，如果传了，告警规则关联的策略会和告警模板策略联动变化。     **约束限制**： 不涉及。 **取值范围**： 以at开头，只包含字母、数字，长度为[2,64]个字符。          **默认取值**： 不涉及。 

        :param alarm_template_id: The alarm_template_id of this PostAlarmsReqV2.
        :type alarm_template_id: str
        """
        self._alarm_template_id = alarm_template_id

    @property
    def tags(self):
        r"""Gets the tags of this PostAlarmsReqV2.

        **参数解释**： 租户标签列表。 **约束限制**： 最多包含20个标签。 

        :return: The tags of this PostAlarmsReqV2.
        :rtype: list[:class:`huaweicloudsdkces.v2.ResourceTag`]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        r"""Sets the tags of this PostAlarmsReqV2.

        **参数解释**： 租户标签列表。 **约束限制**： 最多包含20个标签。 

        :param tags: The tags of this PostAlarmsReqV2.
        :type tags: list[:class:`huaweicloudsdkces.v2.ResourceTag`]
        """
        self._tags = tags

    @property
    def product_name(self):
        r"""Gets the product_name of this PostAlarmsReqV2.

        **参数解释**： 产品层级跨维规则创建时需要指明的规则产品名称，一般由\"服务命名空间,服务首层维度名称\"组成，如\"SYS.ECS,instance_id\"。 **约束限制**： 不涉及。 **取值范围**： 长度为[0,128]个字符。          **默认取值**： 不涉及。 

        :return: The product_name of this PostAlarmsReqV2.
        :rtype: str
        """
        return self._product_name

    @product_name.setter
    def product_name(self, product_name):
        r"""Sets the product_name of this PostAlarmsReqV2.

        **参数解释**： 产品层级跨维规则创建时需要指明的规则产品名称，一般由\"服务命名空间,服务首层维度名称\"组成，如\"SYS.ECS,instance_id\"。 **约束限制**： 不涉及。 **取值范围**： 长度为[0,128]个字符。          **默认取值**： 不涉及。 

        :param product_name: The product_name of this PostAlarmsReqV2.
        :type product_name: str
        """
        self._product_name = product_name

    @property
    def resource_level(self):
        r"""Gets the resource_level of this PostAlarmsReqV2.

        **参数解释**： 产品层级跨维规则创建时需要指明为产品层级规则，resource_level取值为product即为云产品类型，不填或者取值为dimension则为子维度类型。 **约束限制**： 不涉及。 **取值范围**： 枚举值。 - product：云产品。 - dimension：子维度。 **默认取值**： 子维度。 

        :return: The resource_level of this PostAlarmsReqV2.
        :rtype: str
        """
        return self._resource_level

    @resource_level.setter
    def resource_level(self, resource_level):
        r"""Sets the resource_level of this PostAlarmsReqV2.

        **参数解释**： 产品层级跨维规则创建时需要指明为产品层级规则，resource_level取值为product即为云产品类型，不填或者取值为dimension则为子维度类型。 **约束限制**： 不涉及。 **取值范围**： 枚举值。 - product：云产品。 - dimension：子维度。 **默认取值**： 子维度。 

        :param resource_level: The resource_level of this PostAlarmsReqV2.
        :type resource_level: str
        """
        self._resource_level = resource_level

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
        if not isinstance(other, PostAlarmsReqV2):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

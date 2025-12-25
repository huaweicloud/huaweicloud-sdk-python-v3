# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class OneResourceGroupResp:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'group_name': 'str',
        'group_id': 'str',
        'create_time': 'datetime',
        'update_time': 'datetime',
        'enterprise_project_id': 'str',
        'type': 'str',
        'status': 'str',
        'event_status': 'str',
        'resource_statistics': 'OneResourceGroupRespResourceStatistics',
        'related_ep_ids': 'list[str]',
        'association_alarm_templates': 'list[AssociationAlarmTemplate]',
        'resource_level': 'str'
    }

    attribute_map = {
        'group_name': 'group_name',
        'group_id': 'group_id',
        'create_time': 'create_time',
        'update_time': 'update_time',
        'enterprise_project_id': 'enterprise_project_id',
        'type': 'type',
        'status': 'status',
        'event_status': 'event_status',
        'resource_statistics': 'resource_statistics',
        'related_ep_ids': 'related_ep_ids',
        'association_alarm_templates': 'association_alarm_templates',
        'resource_level': 'resource_level'
    }

    def __init__(self, group_name=None, group_id=None, create_time=None, update_time=None, enterprise_project_id=None, type=None, status=None, event_status=None, resource_statistics=None, related_ep_ids=None, association_alarm_templates=None, resource_level=None):
        r"""OneResourceGroupResp

        The model defined in huaweicloud sdk

        :param group_name: **参数解释** 资源分组的名称。 **取值范围** 只能为字母、数字、汉字、-或_，长度为[1,128]个字符。
        :type group_name: str
        :param group_id: **参数解释** 资源分组ID。 **取值范围** 以rg开头，后跟22位由字母或数字组成的字符串。
        :type group_id: str
        :param create_time: **参数解释** 资源分组的创建时间，UNIX时间戳，单位毫秒；如：1603819753000。
        :type create_time: datetime
        :param update_time: **参数解释** 资源分组的修改时间，UNIX时间戳，单位毫秒；如：1603819753000。
        :type update_time: datetime
        :param enterprise_project_id: **参数解释** 资源分组归属企业项目ID。 **取值范围** 只能包含小写字母、数字或-，长度为36个字符。或者为0，代表默认企业项目ID。
        :type enterprise_project_id: str
        :param type: **参数解释** 资源分组添加资源方式。 **取值范围** - EPS: 表示匹配企业项目 - TAG: 表示匹配标签 - Manual: 表示手动添加 - COMB: 表示组合匹配 - NAME: 表示匹配实例名称
        :type type: str
        :param status: **参数解释** 资源分组指标告警状态。 **取值范围** - health: 表示无告警 - unhealthy: 表示告警中 - no_alarm_rule: 表示未配置告警规则
        :type status: str
        :param event_status: **参数解释** 资源分组事件告警状态。 **取值范围** - health: 表示无告警 - unhealthy: 表示告警中 - no_alarm_rule: 表示未配置告警规则
        :type event_status: str
        :param resource_statistics: 
        :type resource_statistics: :class:`huaweicloudsdkces.v2.OneResourceGroupRespResourceStatistics`
        :param related_ep_ids: **参数解释** 当资源匹配规则为匹配企业项目时，指定的企业项目列表。
        :type related_ep_ids: list[str]
        :param association_alarm_templates: **参数解释** 关联的告警模板列表。
        :type association_alarm_templates: list[:class:`huaweicloudsdkces.v2.AssociationAlarmTemplate`]
        :param resource_level: **参数解释** 资源层级，资源生效范围。 **取值范围** - product: 云产品 - dimension: 子维度
        :type resource_level: str
        """
        
        

        self._group_name = None
        self._group_id = None
        self._create_time = None
        self._update_time = None
        self._enterprise_project_id = None
        self._type = None
        self._status = None
        self._event_status = None
        self._resource_statistics = None
        self._related_ep_ids = None
        self._association_alarm_templates = None
        self._resource_level = None
        self.discriminator = None

        self.group_name = group_name
        self.group_id = group_id
        self.create_time = create_time
        self.update_time = update_time
        self.enterprise_project_id = enterprise_project_id
        self.type = type
        if status is not None:
            self.status = status
        if event_status is not None:
            self.event_status = event_status
        if resource_statistics is not None:
            self.resource_statistics = resource_statistics
        if related_ep_ids is not None:
            self.related_ep_ids = related_ep_ids
        if association_alarm_templates is not None:
            self.association_alarm_templates = association_alarm_templates
        if resource_level is not None:
            self.resource_level = resource_level

    @property
    def group_name(self):
        r"""Gets the group_name of this OneResourceGroupResp.

        **参数解释** 资源分组的名称。 **取值范围** 只能为字母、数字、汉字、-或_，长度为[1,128]个字符。

        :return: The group_name of this OneResourceGroupResp.
        :rtype: str
        """
        return self._group_name

    @group_name.setter
    def group_name(self, group_name):
        r"""Sets the group_name of this OneResourceGroupResp.

        **参数解释** 资源分组的名称。 **取值范围** 只能为字母、数字、汉字、-或_，长度为[1,128]个字符。

        :param group_name: The group_name of this OneResourceGroupResp.
        :type group_name: str
        """
        self._group_name = group_name

    @property
    def group_id(self):
        r"""Gets the group_id of this OneResourceGroupResp.

        **参数解释** 资源分组ID。 **取值范围** 以rg开头，后跟22位由字母或数字组成的字符串。

        :return: The group_id of this OneResourceGroupResp.
        :rtype: str
        """
        return self._group_id

    @group_id.setter
    def group_id(self, group_id):
        r"""Sets the group_id of this OneResourceGroupResp.

        **参数解释** 资源分组ID。 **取值范围** 以rg开头，后跟22位由字母或数字组成的字符串。

        :param group_id: The group_id of this OneResourceGroupResp.
        :type group_id: str
        """
        self._group_id = group_id

    @property
    def create_time(self):
        r"""Gets the create_time of this OneResourceGroupResp.

        **参数解释** 资源分组的创建时间，UNIX时间戳，单位毫秒；如：1603819753000。

        :return: The create_time of this OneResourceGroupResp.
        :rtype: datetime
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        r"""Sets the create_time of this OneResourceGroupResp.

        **参数解释** 资源分组的创建时间，UNIX时间戳，单位毫秒；如：1603819753000。

        :param create_time: The create_time of this OneResourceGroupResp.
        :type create_time: datetime
        """
        self._create_time = create_time

    @property
    def update_time(self):
        r"""Gets the update_time of this OneResourceGroupResp.

        **参数解释** 资源分组的修改时间，UNIX时间戳，单位毫秒；如：1603819753000。

        :return: The update_time of this OneResourceGroupResp.
        :rtype: datetime
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        r"""Sets the update_time of this OneResourceGroupResp.

        **参数解释** 资源分组的修改时间，UNIX时间戳，单位毫秒；如：1603819753000。

        :param update_time: The update_time of this OneResourceGroupResp.
        :type update_time: datetime
        """
        self._update_time = update_time

    @property
    def enterprise_project_id(self):
        r"""Gets the enterprise_project_id of this OneResourceGroupResp.

        **参数解释** 资源分组归属企业项目ID。 **取值范围** 只能包含小写字母、数字或-，长度为36个字符。或者为0，代表默认企业项目ID。

        :return: The enterprise_project_id of this OneResourceGroupResp.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        r"""Sets the enterprise_project_id of this OneResourceGroupResp.

        **参数解释** 资源分组归属企业项目ID。 **取值范围** 只能包含小写字母、数字或-，长度为36个字符。或者为0，代表默认企业项目ID。

        :param enterprise_project_id: The enterprise_project_id of this OneResourceGroupResp.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def type(self):
        r"""Gets the type of this OneResourceGroupResp.

        **参数解释** 资源分组添加资源方式。 **取值范围** - EPS: 表示匹配企业项目 - TAG: 表示匹配标签 - Manual: 表示手动添加 - COMB: 表示组合匹配 - NAME: 表示匹配实例名称

        :return: The type of this OneResourceGroupResp.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this OneResourceGroupResp.

        **参数解释** 资源分组添加资源方式。 **取值范围** - EPS: 表示匹配企业项目 - TAG: 表示匹配标签 - Manual: 表示手动添加 - COMB: 表示组合匹配 - NAME: 表示匹配实例名称

        :param type: The type of this OneResourceGroupResp.
        :type type: str
        """
        self._type = type

    @property
    def status(self):
        r"""Gets the status of this OneResourceGroupResp.

        **参数解释** 资源分组指标告警状态。 **取值范围** - health: 表示无告警 - unhealthy: 表示告警中 - no_alarm_rule: 表示未配置告警规则

        :return: The status of this OneResourceGroupResp.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this OneResourceGroupResp.

        **参数解释** 资源分组指标告警状态。 **取值范围** - health: 表示无告警 - unhealthy: 表示告警中 - no_alarm_rule: 表示未配置告警规则

        :param status: The status of this OneResourceGroupResp.
        :type status: str
        """
        self._status = status

    @property
    def event_status(self):
        r"""Gets the event_status of this OneResourceGroupResp.

        **参数解释** 资源分组事件告警状态。 **取值范围** - health: 表示无告警 - unhealthy: 表示告警中 - no_alarm_rule: 表示未配置告警规则

        :return: The event_status of this OneResourceGroupResp.
        :rtype: str
        """
        return self._event_status

    @event_status.setter
    def event_status(self, event_status):
        r"""Sets the event_status of this OneResourceGroupResp.

        **参数解释** 资源分组事件告警状态。 **取值范围** - health: 表示无告警 - unhealthy: 表示告警中 - no_alarm_rule: 表示未配置告警规则

        :param event_status: The event_status of this OneResourceGroupResp.
        :type event_status: str
        """
        self._event_status = event_status

    @property
    def resource_statistics(self):
        r"""Gets the resource_statistics of this OneResourceGroupResp.

        :return: The resource_statistics of this OneResourceGroupResp.
        :rtype: :class:`huaweicloudsdkces.v2.OneResourceGroupRespResourceStatistics`
        """
        return self._resource_statistics

    @resource_statistics.setter
    def resource_statistics(self, resource_statistics):
        r"""Sets the resource_statistics of this OneResourceGroupResp.

        :param resource_statistics: The resource_statistics of this OneResourceGroupResp.
        :type resource_statistics: :class:`huaweicloudsdkces.v2.OneResourceGroupRespResourceStatistics`
        """
        self._resource_statistics = resource_statistics

    @property
    def related_ep_ids(self):
        r"""Gets the related_ep_ids of this OneResourceGroupResp.

        **参数解释** 当资源匹配规则为匹配企业项目时，指定的企业项目列表。

        :return: The related_ep_ids of this OneResourceGroupResp.
        :rtype: list[str]
        """
        return self._related_ep_ids

    @related_ep_ids.setter
    def related_ep_ids(self, related_ep_ids):
        r"""Sets the related_ep_ids of this OneResourceGroupResp.

        **参数解释** 当资源匹配规则为匹配企业项目时，指定的企业项目列表。

        :param related_ep_ids: The related_ep_ids of this OneResourceGroupResp.
        :type related_ep_ids: list[str]
        """
        self._related_ep_ids = related_ep_ids

    @property
    def association_alarm_templates(self):
        r"""Gets the association_alarm_templates of this OneResourceGroupResp.

        **参数解释** 关联的告警模板列表。

        :return: The association_alarm_templates of this OneResourceGroupResp.
        :rtype: list[:class:`huaweicloudsdkces.v2.AssociationAlarmTemplate`]
        """
        return self._association_alarm_templates

    @association_alarm_templates.setter
    def association_alarm_templates(self, association_alarm_templates):
        r"""Sets the association_alarm_templates of this OneResourceGroupResp.

        **参数解释** 关联的告警模板列表。

        :param association_alarm_templates: The association_alarm_templates of this OneResourceGroupResp.
        :type association_alarm_templates: list[:class:`huaweicloudsdkces.v2.AssociationAlarmTemplate`]
        """
        self._association_alarm_templates = association_alarm_templates

    @property
    def resource_level(self):
        r"""Gets the resource_level of this OneResourceGroupResp.

        **参数解释** 资源层级，资源生效范围。 **取值范围** - product: 云产品 - dimension: 子维度

        :return: The resource_level of this OneResourceGroupResp.
        :rtype: str
        """
        return self._resource_level

    @resource_level.setter
    def resource_level(self, resource_level):
        r"""Sets the resource_level of this OneResourceGroupResp.

        **参数解释** 资源层级，资源生效范围。 **取值范围** - product: 云产品 - dimension: 子维度

        :param resource_level: The resource_level of this OneResourceGroupResp.
        :type resource_level: str
        """
        self._resource_level = resource_level

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
        if not isinstance(other, OneResourceGroupResp):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

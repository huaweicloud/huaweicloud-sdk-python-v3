# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowEventItemDetailResp:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'content': 'str',
        'group_id': 'str',
        'resource_id': 'str',
        'resource_name': 'str',
        'event_state': 'str',
        'event_level': 'str',
        'event_user': 'str',
        'event_type': 'str',
        'dimensions': 'list[MetricsDimensionResp]'
    }

    attribute_map = {
        'content': 'content',
        'group_id': 'group_id',
        'resource_id': 'resource_id',
        'resource_name': 'resource_name',
        'event_state': 'event_state',
        'event_level': 'event_level',
        'event_user': 'event_user',
        'event_type': 'event_type',
        'dimensions': 'dimensions'
    }

    def __init__(self, content=None, group_id=None, resource_id=None, resource_name=None, event_state=None, event_level=None, event_user=None, event_type=None, dimensions=None):
        r"""ShowEventItemDetailResp

        The model defined in huaweicloud sdk

        :param content: **参数解释**： 事件内容。 **取值范围**： 长度为[1,4096]个字符。 
        :type content: str
        :param group_id: **参数解释**： 所属分组。 **取值范围**： 长度只能为24个字符。 
        :type group_id: str
        :param resource_id: **参数解释**： 资源ID。 **取值范围**： 长度为[1,128]个字符。 
        :type resource_id: str
        :param resource_name: **参数解释**： 资源名称。 **取值范围**： 长度为[1,128]个字符。 
        :type resource_name: str
        :param event_state: **参数解释**： 事件状态。 **取值范围**： 枚举类型：normal\\warning\\incident。 - normal: 正常 - warning: 警告 - incident: 故障 
        :type event_state: str
        :param event_level: **参数解释**： 事件级别。 **取值范围**： 枚举类型：Critical, Major, Minor, Info。 - Critical: 紧急 - Major: 重要 - Minor: 次要 - Info: 提示 
        :type event_level: str
        :param event_user: **参数解释**： 事件用户。 **取值范围**： 下划线、横线、斜杠、@ 符号或点号组成，长度为[0,64]个字符。 
        :type event_user: str
        :param event_type: **参数解释**： 事件类型。 **取值范围**： 枚举类型：EVENT.SYS，EVENT.CUSTOM - EVENT.SYS: 系统事件。 - EVENT.CUSTOM: 自定义事件。 
        :type event_type: str
        :param dimensions: **参数解释**： 事件的维度，根据维度描述资源信息。 用于指定资源、资源分组的事件告警场景中，支持按维度配置告警规则。 **取值范围**： 目前最大支持4个维度 
        :type dimensions: list[:class:`huaweicloudsdkces.v1.MetricsDimensionResp`]
        """
        
        

        self._content = None
        self._group_id = None
        self._resource_id = None
        self._resource_name = None
        self._event_state = None
        self._event_level = None
        self._event_user = None
        self._event_type = None
        self._dimensions = None
        self.discriminator = None

        if content is not None:
            self.content = content
        if group_id is not None:
            self.group_id = group_id
        if resource_id is not None:
            self.resource_id = resource_id
        if resource_name is not None:
            self.resource_name = resource_name
        if event_state is not None:
            self.event_state = event_state
        if event_level is not None:
            self.event_level = event_level
        if event_user is not None:
            self.event_user = event_user
        if event_type is not None:
            self.event_type = event_type
        if dimensions is not None:
            self.dimensions = dimensions

    @property
    def content(self):
        r"""Gets the content of this ShowEventItemDetailResp.

        **参数解释**： 事件内容。 **取值范围**： 长度为[1,4096]个字符。 

        :return: The content of this ShowEventItemDetailResp.
        :rtype: str
        """
        return self._content

    @content.setter
    def content(self, content):
        r"""Sets the content of this ShowEventItemDetailResp.

        **参数解释**： 事件内容。 **取值范围**： 长度为[1,4096]个字符。 

        :param content: The content of this ShowEventItemDetailResp.
        :type content: str
        """
        self._content = content

    @property
    def group_id(self):
        r"""Gets the group_id of this ShowEventItemDetailResp.

        **参数解释**： 所属分组。 **取值范围**： 长度只能为24个字符。 

        :return: The group_id of this ShowEventItemDetailResp.
        :rtype: str
        """
        return self._group_id

    @group_id.setter
    def group_id(self, group_id):
        r"""Sets the group_id of this ShowEventItemDetailResp.

        **参数解释**： 所属分组。 **取值范围**： 长度只能为24个字符。 

        :param group_id: The group_id of this ShowEventItemDetailResp.
        :type group_id: str
        """
        self._group_id = group_id

    @property
    def resource_id(self):
        r"""Gets the resource_id of this ShowEventItemDetailResp.

        **参数解释**： 资源ID。 **取值范围**： 长度为[1,128]个字符。 

        :return: The resource_id of this ShowEventItemDetailResp.
        :rtype: str
        """
        return self._resource_id

    @resource_id.setter
    def resource_id(self, resource_id):
        r"""Sets the resource_id of this ShowEventItemDetailResp.

        **参数解释**： 资源ID。 **取值范围**： 长度为[1,128]个字符。 

        :param resource_id: The resource_id of this ShowEventItemDetailResp.
        :type resource_id: str
        """
        self._resource_id = resource_id

    @property
    def resource_name(self):
        r"""Gets the resource_name of this ShowEventItemDetailResp.

        **参数解释**： 资源名称。 **取值范围**： 长度为[1,128]个字符。 

        :return: The resource_name of this ShowEventItemDetailResp.
        :rtype: str
        """
        return self._resource_name

    @resource_name.setter
    def resource_name(self, resource_name):
        r"""Sets the resource_name of this ShowEventItemDetailResp.

        **参数解释**： 资源名称。 **取值范围**： 长度为[1,128]个字符。 

        :param resource_name: The resource_name of this ShowEventItemDetailResp.
        :type resource_name: str
        """
        self._resource_name = resource_name

    @property
    def event_state(self):
        r"""Gets the event_state of this ShowEventItemDetailResp.

        **参数解释**： 事件状态。 **取值范围**： 枚举类型：normal\\warning\\incident。 - normal: 正常 - warning: 警告 - incident: 故障 

        :return: The event_state of this ShowEventItemDetailResp.
        :rtype: str
        """
        return self._event_state

    @event_state.setter
    def event_state(self, event_state):
        r"""Sets the event_state of this ShowEventItemDetailResp.

        **参数解释**： 事件状态。 **取值范围**： 枚举类型：normal\\warning\\incident。 - normal: 正常 - warning: 警告 - incident: 故障 

        :param event_state: The event_state of this ShowEventItemDetailResp.
        :type event_state: str
        """
        self._event_state = event_state

    @property
    def event_level(self):
        r"""Gets the event_level of this ShowEventItemDetailResp.

        **参数解释**： 事件级别。 **取值范围**： 枚举类型：Critical, Major, Minor, Info。 - Critical: 紧急 - Major: 重要 - Minor: 次要 - Info: 提示 

        :return: The event_level of this ShowEventItemDetailResp.
        :rtype: str
        """
        return self._event_level

    @event_level.setter
    def event_level(self, event_level):
        r"""Sets the event_level of this ShowEventItemDetailResp.

        **参数解释**： 事件级别。 **取值范围**： 枚举类型：Critical, Major, Minor, Info。 - Critical: 紧急 - Major: 重要 - Minor: 次要 - Info: 提示 

        :param event_level: The event_level of this ShowEventItemDetailResp.
        :type event_level: str
        """
        self._event_level = event_level

    @property
    def event_user(self):
        r"""Gets the event_user of this ShowEventItemDetailResp.

        **参数解释**： 事件用户。 **取值范围**： 下划线、横线、斜杠、@ 符号或点号组成，长度为[0,64]个字符。 

        :return: The event_user of this ShowEventItemDetailResp.
        :rtype: str
        """
        return self._event_user

    @event_user.setter
    def event_user(self, event_user):
        r"""Sets the event_user of this ShowEventItemDetailResp.

        **参数解释**： 事件用户。 **取值范围**： 下划线、横线、斜杠、@ 符号或点号组成，长度为[0,64]个字符。 

        :param event_user: The event_user of this ShowEventItemDetailResp.
        :type event_user: str
        """
        self._event_user = event_user

    @property
    def event_type(self):
        r"""Gets the event_type of this ShowEventItemDetailResp.

        **参数解释**： 事件类型。 **取值范围**： 枚举类型：EVENT.SYS，EVENT.CUSTOM - EVENT.SYS: 系统事件。 - EVENT.CUSTOM: 自定义事件。 

        :return: The event_type of this ShowEventItemDetailResp.
        :rtype: str
        """
        return self._event_type

    @event_type.setter
    def event_type(self, event_type):
        r"""Sets the event_type of this ShowEventItemDetailResp.

        **参数解释**： 事件类型。 **取值范围**： 枚举类型：EVENT.SYS，EVENT.CUSTOM - EVENT.SYS: 系统事件。 - EVENT.CUSTOM: 自定义事件。 

        :param event_type: The event_type of this ShowEventItemDetailResp.
        :type event_type: str
        """
        self._event_type = event_type

    @property
    def dimensions(self):
        r"""Gets the dimensions of this ShowEventItemDetailResp.

        **参数解释**： 事件的维度，根据维度描述资源信息。 用于指定资源、资源分组的事件告警场景中，支持按维度配置告警规则。 **取值范围**： 目前最大支持4个维度 

        :return: The dimensions of this ShowEventItemDetailResp.
        :rtype: list[:class:`huaweicloudsdkces.v1.MetricsDimensionResp`]
        """
        return self._dimensions

    @dimensions.setter
    def dimensions(self, dimensions):
        r"""Sets the dimensions of this ShowEventItemDetailResp.

        **参数解释**： 事件的维度，根据维度描述资源信息。 用于指定资源、资源分组的事件告警场景中，支持按维度配置告警规则。 **取值范围**： 目前最大支持4个维度 

        :param dimensions: The dimensions of this ShowEventItemDetailResp.
        :type dimensions: list[:class:`huaweicloudsdkces.v1.MetricsDimensionResp`]
        """
        self._dimensions = dimensions

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
        if not isinstance(other, ShowEventItemDetailResp):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

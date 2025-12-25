# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class GetResourceGroupResources:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'status': 'str',
        'dimensions': 'list[ResourceDimension]',
        'tags': 'str',
        'enterprise_project_id': 'str',
        'event_status': 'str',
        'resource_name': 'str'
    }

    attribute_map = {
        'status': 'status',
        'dimensions': 'dimensions',
        'tags': 'tags',
        'enterprise_project_id': 'enterprise_project_id',
        'event_status': 'event_status',
        'resource_name': 'resource_name'
    }

    def __init__(self, status=None, dimensions=None, tags=None, enterprise_project_id=None, event_status=None, resource_name=None):
        r"""GetResourceGroupResources

        The model defined in huaweicloud sdk

        :param status: **参数解释** 按事件告警状态信息进行过滤。 **取值范围** 枚举值。 - health: 告警中 - unhealthy: 已触发 - no_alarm_rule: 未设置告警规则 
        :type status: str
        :param dimensions: 资源的维度信息
        :type dimensions: list[:class:`huaweicloudsdkces.v2.ResourceDimension`]
        :param tags: **参数解释** 资源的tag信息,格式为key/value的json字符串,样例为\&quot;{\\\&quot;sss\\\&quot;:\\\&quot;aaa\\\&quot;}\&quot;。 **取值范围** 枚举值。 字符串长度[0, 10240] 
        :type tags: str
        :param enterprise_project_id: **参数解释** 企业项目ID。 **取值范围** 由数字、字母和-组成，字符串长度范围[1,128] 
        :type enterprise_project_id: str
        :param event_status: **参数解释** 按事件告警状态信息进行过滤。 **取值范围** 枚举值。 - health: 告警中 - unhealthy: 已触发 - no_alarm_rule: 未设置告警规则 
        :type event_status: str
        :param resource_name: **参数解释** 资源名称 **取值范围** 长度[0,128]个字符 
        :type resource_name: str
        """
        
        

        self._status = None
        self._dimensions = None
        self._tags = None
        self._enterprise_project_id = None
        self._event_status = None
        self._resource_name = None
        self.discriminator = None

        self.status = status
        self.dimensions = dimensions
        if tags is not None:
            self.tags = tags
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        if event_status is not None:
            self.event_status = event_status
        if resource_name is not None:
            self.resource_name = resource_name

    @property
    def status(self):
        r"""Gets the status of this GetResourceGroupResources.

        **参数解释** 按事件告警状态信息进行过滤。 **取值范围** 枚举值。 - health: 告警中 - unhealthy: 已触发 - no_alarm_rule: 未设置告警规则 

        :return: The status of this GetResourceGroupResources.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this GetResourceGroupResources.

        **参数解释** 按事件告警状态信息进行过滤。 **取值范围** 枚举值。 - health: 告警中 - unhealthy: 已触发 - no_alarm_rule: 未设置告警规则 

        :param status: The status of this GetResourceGroupResources.
        :type status: str
        """
        self._status = status

    @property
    def dimensions(self):
        r"""Gets the dimensions of this GetResourceGroupResources.

        资源的维度信息

        :return: The dimensions of this GetResourceGroupResources.
        :rtype: list[:class:`huaweicloudsdkces.v2.ResourceDimension`]
        """
        return self._dimensions

    @dimensions.setter
    def dimensions(self, dimensions):
        r"""Sets the dimensions of this GetResourceGroupResources.

        资源的维度信息

        :param dimensions: The dimensions of this GetResourceGroupResources.
        :type dimensions: list[:class:`huaweicloudsdkces.v2.ResourceDimension`]
        """
        self._dimensions = dimensions

    @property
    def tags(self):
        r"""Gets the tags of this GetResourceGroupResources.

        **参数解释** 资源的tag信息,格式为key/value的json字符串,样例为\"{\\\"sss\\\":\\\"aaa\\\"}\"。 **取值范围** 枚举值。 字符串长度[0, 10240] 

        :return: The tags of this GetResourceGroupResources.
        :rtype: str
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        r"""Sets the tags of this GetResourceGroupResources.

        **参数解释** 资源的tag信息,格式为key/value的json字符串,样例为\"{\\\"sss\\\":\\\"aaa\\\"}\"。 **取值范围** 枚举值。 字符串长度[0, 10240] 

        :param tags: The tags of this GetResourceGroupResources.
        :type tags: str
        """
        self._tags = tags

    @property
    def enterprise_project_id(self):
        r"""Gets the enterprise_project_id of this GetResourceGroupResources.

        **参数解释** 企业项目ID。 **取值范围** 由数字、字母和-组成，字符串长度范围[1,128] 

        :return: The enterprise_project_id of this GetResourceGroupResources.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        r"""Sets the enterprise_project_id of this GetResourceGroupResources.

        **参数解释** 企业项目ID。 **取值范围** 由数字、字母和-组成，字符串长度范围[1,128] 

        :param enterprise_project_id: The enterprise_project_id of this GetResourceGroupResources.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def event_status(self):
        r"""Gets the event_status of this GetResourceGroupResources.

        **参数解释** 按事件告警状态信息进行过滤。 **取值范围** 枚举值。 - health: 告警中 - unhealthy: 已触发 - no_alarm_rule: 未设置告警规则 

        :return: The event_status of this GetResourceGroupResources.
        :rtype: str
        """
        return self._event_status

    @event_status.setter
    def event_status(self, event_status):
        r"""Sets the event_status of this GetResourceGroupResources.

        **参数解释** 按事件告警状态信息进行过滤。 **取值范围** 枚举值。 - health: 告警中 - unhealthy: 已触发 - no_alarm_rule: 未设置告警规则 

        :param event_status: The event_status of this GetResourceGroupResources.
        :type event_status: str
        """
        self._event_status = event_status

    @property
    def resource_name(self):
        r"""Gets the resource_name of this GetResourceGroupResources.

        **参数解释** 资源名称 **取值范围** 长度[0,128]个字符 

        :return: The resource_name of this GetResourceGroupResources.
        :rtype: str
        """
        return self._resource_name

    @resource_name.setter
    def resource_name(self, resource_name):
        r"""Sets the resource_name of this GetResourceGroupResources.

        **参数解释** 资源名称 **取值范围** 长度[0,128]个字符 

        :param resource_name: The resource_name of this GetResourceGroupResources.
        :type resource_name: str
        """
        self._resource_name = resource_name

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
        if not isinstance(other, GetResourceGroupResources):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

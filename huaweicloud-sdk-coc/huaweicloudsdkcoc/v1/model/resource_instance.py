# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ResourceInstance:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'resource_id': 'str',
        'provider': 'str',
        'region_id': 'str',
        'type': 'str',
        'custom_attributes': 'list[Customttribute]',
        'agent_sn': 'str',
        'agent_status': 'str',
        'properties': 'ResourceInstanceProp'
    }

    attribute_map = {
        'resource_id': 'resource_id',
        'provider': 'provider',
        'region_id': 'region_id',
        'type': 'type',
        'custom_attributes': 'custom_attributes',
        'agent_sn': 'agent_sn',
        'agent_status': 'agent_status',
        'properties': 'properties'
    }

    def __init__(self, resource_id=None, provider=None, region_id=None, type=None, custom_attributes=None, agent_sn=None, agent_status=None, properties=None):
        r"""ResourceInstance

        The model defined in huaweicloud sdk

        :param resource_id: 实例唯一id
        :type resource_id: str
        :param provider: 资源提供者：ECS。单个脚本工单， 每个实例的provider是一致的
        :type provider: str
        :param region_id: 机器所属region的ID
        :type region_id: str
        :param type: 资源提供者下资源类型，不传默认为CLOUDSERVER CLOUDSERVER:CLOUDSERVER类型
        :type type: str
        :param custom_attributes: 支持用户自定义5个key_value形式的属性。 约束条件：  - key值长度为20     - value长度为50     - map长度最大为5
        :type custom_attributes: list[:class:`huaweicloudsdkcoc.v1.Customttribute`]
        :param agent_sn: agent纳管id。该参数即将废弃，请勿使用。
        :type agent_sn: str
        :param agent_status: agent纳管状态。该参数即将废弃，请勿使用。
        :type agent_status: str
        :param properties: 
        :type properties: :class:`huaweicloudsdkcoc.v1.ResourceInstanceProp`
        """
        
        

        self._resource_id = None
        self._provider = None
        self._region_id = None
        self._type = None
        self._custom_attributes = None
        self._agent_sn = None
        self._agent_status = None
        self._properties = None
        self.discriminator = None

        self.resource_id = resource_id
        self.provider = provider
        self.region_id = region_id
        self.type = type
        if custom_attributes is not None:
            self.custom_attributes = custom_attributes
        if agent_sn is not None:
            self.agent_sn = agent_sn
        if agent_status is not None:
            self.agent_status = agent_status
        if properties is not None:
            self.properties = properties

    @property
    def resource_id(self):
        r"""Gets the resource_id of this ResourceInstance.

        实例唯一id

        :return: The resource_id of this ResourceInstance.
        :rtype: str
        """
        return self._resource_id

    @resource_id.setter
    def resource_id(self, resource_id):
        r"""Sets the resource_id of this ResourceInstance.

        实例唯一id

        :param resource_id: The resource_id of this ResourceInstance.
        :type resource_id: str
        """
        self._resource_id = resource_id

    @property
    def provider(self):
        r"""Gets the provider of this ResourceInstance.

        资源提供者：ECS。单个脚本工单， 每个实例的provider是一致的

        :return: The provider of this ResourceInstance.
        :rtype: str
        """
        return self._provider

    @provider.setter
    def provider(self, provider):
        r"""Sets the provider of this ResourceInstance.

        资源提供者：ECS。单个脚本工单， 每个实例的provider是一致的

        :param provider: The provider of this ResourceInstance.
        :type provider: str
        """
        self._provider = provider

    @property
    def region_id(self):
        r"""Gets the region_id of this ResourceInstance.

        机器所属region的ID

        :return: The region_id of this ResourceInstance.
        :rtype: str
        """
        return self._region_id

    @region_id.setter
    def region_id(self, region_id):
        r"""Sets the region_id of this ResourceInstance.

        机器所属region的ID

        :param region_id: The region_id of this ResourceInstance.
        :type region_id: str
        """
        self._region_id = region_id

    @property
    def type(self):
        r"""Gets the type of this ResourceInstance.

        资源提供者下资源类型，不传默认为CLOUDSERVER CLOUDSERVER:CLOUDSERVER类型

        :return: The type of this ResourceInstance.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this ResourceInstance.

        资源提供者下资源类型，不传默认为CLOUDSERVER CLOUDSERVER:CLOUDSERVER类型

        :param type: The type of this ResourceInstance.
        :type type: str
        """
        self._type = type

    @property
    def custom_attributes(self):
        r"""Gets the custom_attributes of this ResourceInstance.

        支持用户自定义5个key_value形式的属性。 约束条件：  - key值长度为20     - value长度为50     - map长度最大为5

        :return: The custom_attributes of this ResourceInstance.
        :rtype: list[:class:`huaweicloudsdkcoc.v1.Customttribute`]
        """
        return self._custom_attributes

    @custom_attributes.setter
    def custom_attributes(self, custom_attributes):
        r"""Sets the custom_attributes of this ResourceInstance.

        支持用户自定义5个key_value形式的属性。 约束条件：  - key值长度为20     - value长度为50     - map长度最大为5

        :param custom_attributes: The custom_attributes of this ResourceInstance.
        :type custom_attributes: list[:class:`huaweicloudsdkcoc.v1.Customttribute`]
        """
        self._custom_attributes = custom_attributes

    @property
    def agent_sn(self):
        r"""Gets the agent_sn of this ResourceInstance.

        agent纳管id。该参数即将废弃，请勿使用。

        :return: The agent_sn of this ResourceInstance.
        :rtype: str
        """
        return self._agent_sn

    @agent_sn.setter
    def agent_sn(self, agent_sn):
        r"""Sets the agent_sn of this ResourceInstance.

        agent纳管id。该参数即将废弃，请勿使用。

        :param agent_sn: The agent_sn of this ResourceInstance.
        :type agent_sn: str
        """
        self._agent_sn = agent_sn

    @property
    def agent_status(self):
        r"""Gets the agent_status of this ResourceInstance.

        agent纳管状态。该参数即将废弃，请勿使用。

        :return: The agent_status of this ResourceInstance.
        :rtype: str
        """
        return self._agent_status

    @agent_status.setter
    def agent_status(self, agent_status):
        r"""Sets the agent_status of this ResourceInstance.

        agent纳管状态。该参数即将废弃，请勿使用。

        :param agent_status: The agent_status of this ResourceInstance.
        :type agent_status: str
        """
        self._agent_status = agent_status

    @property
    def properties(self):
        r"""Gets the properties of this ResourceInstance.

        :return: The properties of this ResourceInstance.
        :rtype: :class:`huaweicloudsdkcoc.v1.ResourceInstanceProp`
        """
        return self._properties

    @properties.setter
    def properties(self, properties):
        r"""Sets the properties of this ResourceInstance.

        :param properties: The properties of this ResourceInstance.
        :type properties: :class:`huaweicloudsdkcoc.v1.ResourceInstanceProp`
        """
        self._properties = properties

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
        if not isinstance(other, ResourceInstance):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

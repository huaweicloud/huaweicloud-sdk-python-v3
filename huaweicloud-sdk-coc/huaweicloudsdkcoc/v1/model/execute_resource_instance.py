# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ExecuteResourceInstance:

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
        'region_id': 'str',
        'provider': 'str',
        'type': 'str',
        'custom_attributes': 'list[Customttribute]',
        'agent_sn': 'str',
        'project_id': 'str'
    }

    attribute_map = {
        'resource_id': 'resource_id',
        'region_id': 'region_id',
        'provider': 'provider',
        'type': 'type',
        'custom_attributes': 'custom_attributes',
        'agent_sn': 'agent_sn',
        'project_id': 'project_id'
    }

    def __init__(self, resource_id=None, region_id=None, provider=None, type=None, custom_attributes=None, agent_sn=None, project_id=None):
        r"""ExecuteResourceInstance

        The model defined in huaweicloud sdk

        :param resource_id: ecs云服务器ID
        :type resource_id: str
        :param region_id: 服务器所属region
        :type region_id: str
        :param provider: 资源提供者：ECS，不传默认为：ECS。请保证一次执行， 每个实例的provider是一致的。后续扩展CCE等
        :type provider: str
        :param type: 资源提供者下资源类型，不传默认为CLOUDSERVER CLOUDSERVER:CLOUDSERVER类型 约束：  -不允许跨type支持
        :type type: str
        :param custom_attributes: 支持用户自定义5个key_value形式的属性。  约束条件： - key值长度为10  - value长度为20  - map长度最大为5 - 禁止填写敏感数据
        :type custom_attributes: list[:class:`huaweicloudsdkcoc.v1.Customttribute`]
        :param agent_sn: 该参数已废弃，传入该参数不会生效。
        :type agent_sn: str
        :param project_id: 该参数已废弃，传入该参数不会生效。
        :type project_id: str
        """
        
        

        self._resource_id = None
        self._region_id = None
        self._provider = None
        self._type = None
        self._custom_attributes = None
        self._agent_sn = None
        self._project_id = None
        self.discriminator = None

        self.resource_id = resource_id
        self.region_id = region_id
        if provider is not None:
            self.provider = provider
        if type is not None:
            self.type = type
        if custom_attributes is not None:
            self.custom_attributes = custom_attributes
        if agent_sn is not None:
            self.agent_sn = agent_sn
        if project_id is not None:
            self.project_id = project_id

    @property
    def resource_id(self):
        r"""Gets the resource_id of this ExecuteResourceInstance.

        ecs云服务器ID

        :return: The resource_id of this ExecuteResourceInstance.
        :rtype: str
        """
        return self._resource_id

    @resource_id.setter
    def resource_id(self, resource_id):
        r"""Sets the resource_id of this ExecuteResourceInstance.

        ecs云服务器ID

        :param resource_id: The resource_id of this ExecuteResourceInstance.
        :type resource_id: str
        """
        self._resource_id = resource_id

    @property
    def region_id(self):
        r"""Gets the region_id of this ExecuteResourceInstance.

        服务器所属region

        :return: The region_id of this ExecuteResourceInstance.
        :rtype: str
        """
        return self._region_id

    @region_id.setter
    def region_id(self, region_id):
        r"""Sets the region_id of this ExecuteResourceInstance.

        服务器所属region

        :param region_id: The region_id of this ExecuteResourceInstance.
        :type region_id: str
        """
        self._region_id = region_id

    @property
    def provider(self):
        r"""Gets the provider of this ExecuteResourceInstance.

        资源提供者：ECS，不传默认为：ECS。请保证一次执行， 每个实例的provider是一致的。后续扩展CCE等

        :return: The provider of this ExecuteResourceInstance.
        :rtype: str
        """
        return self._provider

    @provider.setter
    def provider(self, provider):
        r"""Sets the provider of this ExecuteResourceInstance.

        资源提供者：ECS，不传默认为：ECS。请保证一次执行， 每个实例的provider是一致的。后续扩展CCE等

        :param provider: The provider of this ExecuteResourceInstance.
        :type provider: str
        """
        self._provider = provider

    @property
    def type(self):
        r"""Gets the type of this ExecuteResourceInstance.

        资源提供者下资源类型，不传默认为CLOUDSERVER CLOUDSERVER:CLOUDSERVER类型 约束：  -不允许跨type支持

        :return: The type of this ExecuteResourceInstance.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this ExecuteResourceInstance.

        资源提供者下资源类型，不传默认为CLOUDSERVER CLOUDSERVER:CLOUDSERVER类型 约束：  -不允许跨type支持

        :param type: The type of this ExecuteResourceInstance.
        :type type: str
        """
        self._type = type

    @property
    def custom_attributes(self):
        r"""Gets the custom_attributes of this ExecuteResourceInstance.

        支持用户自定义5个key_value形式的属性。  约束条件： - key值长度为10  - value长度为20  - map长度最大为5 - 禁止填写敏感数据

        :return: The custom_attributes of this ExecuteResourceInstance.
        :rtype: list[:class:`huaweicloudsdkcoc.v1.Customttribute`]
        """
        return self._custom_attributes

    @custom_attributes.setter
    def custom_attributes(self, custom_attributes):
        r"""Sets the custom_attributes of this ExecuteResourceInstance.

        支持用户自定义5个key_value形式的属性。  约束条件： - key值长度为10  - value长度为20  - map长度最大为5 - 禁止填写敏感数据

        :param custom_attributes: The custom_attributes of this ExecuteResourceInstance.
        :type custom_attributes: list[:class:`huaweicloudsdkcoc.v1.Customttribute`]
        """
        self._custom_attributes = custom_attributes

    @property
    def agent_sn(self):
        r"""Gets the agent_sn of this ExecuteResourceInstance.

        该参数已废弃，传入该参数不会生效。

        :return: The agent_sn of this ExecuteResourceInstance.
        :rtype: str
        """
        return self._agent_sn

    @agent_sn.setter
    def agent_sn(self, agent_sn):
        r"""Sets the agent_sn of this ExecuteResourceInstance.

        该参数已废弃，传入该参数不会生效。

        :param agent_sn: The agent_sn of this ExecuteResourceInstance.
        :type agent_sn: str
        """
        self._agent_sn = agent_sn

    @property
    def project_id(self):
        r"""Gets the project_id of this ExecuteResourceInstance.

        该参数已废弃，传入该参数不会生效。

        :return: The project_id of this ExecuteResourceInstance.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        r"""Sets the project_id of this ExecuteResourceInstance.

        该参数已废弃，传入该参数不会生效。

        :param project_id: The project_id of this ExecuteResourceInstance.
        :type project_id: str
        """
        self._project_id = project_id

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
        if not isinstance(other, ExecuteResourceInstance):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

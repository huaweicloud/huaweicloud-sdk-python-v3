# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class LoadbalancerResp:

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
        'tenant_id': 'str',
        'name': 'str',
        'description': 'str',
        'vip_subnet_id': 'str',
        'vip_port_id': 'str',
        'vip_address': 'str',
        'listeners': 'list[ResourceList]',
        'pools': 'list[ResourceList]',
        'provider': 'str',
        'operating_status': 'str',
        'provisioning_status': 'str',
        'admin_state_up': 'bool',
        'created_at': 'str',
        'updated_at': 'str',
        'enterprise_project_id': 'str',
        'project_id': 'str',
        'tags': 'list[str]'
    }

    attribute_map = {
        'id': 'id',
        'tenant_id': 'tenant_id',
        'name': 'name',
        'description': 'description',
        'vip_subnet_id': 'vip_subnet_id',
        'vip_port_id': 'vip_port_id',
        'vip_address': 'vip_address',
        'listeners': 'listeners',
        'pools': 'pools',
        'provider': 'provider',
        'operating_status': 'operating_status',
        'provisioning_status': 'provisioning_status',
        'admin_state_up': 'admin_state_up',
        'created_at': 'created_at',
        'updated_at': 'updated_at',
        'enterprise_project_id': 'enterprise_project_id',
        'project_id': 'project_id',
        'tags': 'tags'
    }

    def __init__(self, id=None, tenant_id=None, name=None, description=None, vip_subnet_id=None, vip_port_id=None, vip_address=None, listeners=None, pools=None, provider=None, operating_status=None, provisioning_status=None, admin_state_up=None, created_at=None, updated_at=None, enterprise_project_id=None, project_id=None, tags=None):
        """LoadbalancerResp

        The model defined in huaweicloud sdk

        :param id: 负载均衡器ID
        :type id: str
        :param tenant_id: 负载均衡器所在的项目ID。
        :type tenant_id: str
        :param name: 负载均衡器名称。
        :type name: str
        :param description: 负载均衡器的描述信息
        :type description: str
        :param vip_subnet_id: 负载均衡器所在的子网的IPv4子网ID。仅支持内网类型。
        :type vip_subnet_id: str
        :param vip_port_id: 负载均衡器虚拟IP对应的端口ID
        :type vip_port_id: str
        :param vip_address: 负载均衡器的虚拟IP。
        :type vip_address: str
        :param listeners: 负载均衡器关联的监听器ID的列表
        :type listeners: list[:class:`huaweicloudsdkelb.v2.ResourceList`]
        :param pools: 负载均衡器关联的后端云服务器组ID的列表。
        :type pools: list[:class:`huaweicloudsdkelb.v2.ResourceList`]
        :param provider: 负载均衡器的供应者名称。只支持vlb
        :type provider: str
        :param operating_status: 负载均衡器的操作状态
        :type operating_status: str
        :param provisioning_status: 负载均衡器的配置状态
        :type provisioning_status: str
        :param admin_state_up: 负载均衡器的管理状态。只支持设定为true，该字段的值无实际意义。
        :type admin_state_up: bool
        :param created_at: 负载均衡器的创建时间
        :type created_at: str
        :param updated_at: 负载均衡器的更新时间
        :type updated_at: str
        :param enterprise_project_id: 负载均衡器的企业项目ID。
        :type enterprise_project_id: str
        :param project_id: 负载均衡器所在的项目ID。
        :type project_id: str
        :param tags: 负载均衡器的标签列表
        :type tags: list[str]
        """
        
        

        self._id = None
        self._tenant_id = None
        self._name = None
        self._description = None
        self._vip_subnet_id = None
        self._vip_port_id = None
        self._vip_address = None
        self._listeners = None
        self._pools = None
        self._provider = None
        self._operating_status = None
        self._provisioning_status = None
        self._admin_state_up = None
        self._created_at = None
        self._updated_at = None
        self._enterprise_project_id = None
        self._project_id = None
        self._tags = None
        self.discriminator = None

        self.id = id
        self.tenant_id = tenant_id
        self.name = name
        self.description = description
        self.vip_subnet_id = vip_subnet_id
        self.vip_port_id = vip_port_id
        self.vip_address = vip_address
        self.listeners = listeners
        self.pools = pools
        self.provider = provider
        self.operating_status = operating_status
        self.provisioning_status = provisioning_status
        self.admin_state_up = admin_state_up
        self.created_at = created_at
        self.updated_at = updated_at
        self.enterprise_project_id = enterprise_project_id
        self.project_id = project_id
        self.tags = tags

    @property
    def id(self):
        """Gets the id of this LoadbalancerResp.

        负载均衡器ID

        :return: The id of this LoadbalancerResp.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this LoadbalancerResp.

        负载均衡器ID

        :param id: The id of this LoadbalancerResp.
        :type id: str
        """
        self._id = id

    @property
    def tenant_id(self):
        """Gets the tenant_id of this LoadbalancerResp.

        负载均衡器所在的项目ID。

        :return: The tenant_id of this LoadbalancerResp.
        :rtype: str
        """
        return self._tenant_id

    @tenant_id.setter
    def tenant_id(self, tenant_id):
        """Sets the tenant_id of this LoadbalancerResp.

        负载均衡器所在的项目ID。

        :param tenant_id: The tenant_id of this LoadbalancerResp.
        :type tenant_id: str
        """
        self._tenant_id = tenant_id

    @property
    def name(self):
        """Gets the name of this LoadbalancerResp.

        负载均衡器名称。

        :return: The name of this LoadbalancerResp.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this LoadbalancerResp.

        负载均衡器名称。

        :param name: The name of this LoadbalancerResp.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        """Gets the description of this LoadbalancerResp.

        负载均衡器的描述信息

        :return: The description of this LoadbalancerResp.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this LoadbalancerResp.

        负载均衡器的描述信息

        :param description: The description of this LoadbalancerResp.
        :type description: str
        """
        self._description = description

    @property
    def vip_subnet_id(self):
        """Gets the vip_subnet_id of this LoadbalancerResp.

        负载均衡器所在的子网的IPv4子网ID。仅支持内网类型。

        :return: The vip_subnet_id of this LoadbalancerResp.
        :rtype: str
        """
        return self._vip_subnet_id

    @vip_subnet_id.setter
    def vip_subnet_id(self, vip_subnet_id):
        """Sets the vip_subnet_id of this LoadbalancerResp.

        负载均衡器所在的子网的IPv4子网ID。仅支持内网类型。

        :param vip_subnet_id: The vip_subnet_id of this LoadbalancerResp.
        :type vip_subnet_id: str
        """
        self._vip_subnet_id = vip_subnet_id

    @property
    def vip_port_id(self):
        """Gets the vip_port_id of this LoadbalancerResp.

        负载均衡器虚拟IP对应的端口ID

        :return: The vip_port_id of this LoadbalancerResp.
        :rtype: str
        """
        return self._vip_port_id

    @vip_port_id.setter
    def vip_port_id(self, vip_port_id):
        """Sets the vip_port_id of this LoadbalancerResp.

        负载均衡器虚拟IP对应的端口ID

        :param vip_port_id: The vip_port_id of this LoadbalancerResp.
        :type vip_port_id: str
        """
        self._vip_port_id = vip_port_id

    @property
    def vip_address(self):
        """Gets the vip_address of this LoadbalancerResp.

        负载均衡器的虚拟IP。

        :return: The vip_address of this LoadbalancerResp.
        :rtype: str
        """
        return self._vip_address

    @vip_address.setter
    def vip_address(self, vip_address):
        """Sets the vip_address of this LoadbalancerResp.

        负载均衡器的虚拟IP。

        :param vip_address: The vip_address of this LoadbalancerResp.
        :type vip_address: str
        """
        self._vip_address = vip_address

    @property
    def listeners(self):
        """Gets the listeners of this LoadbalancerResp.

        负载均衡器关联的监听器ID的列表

        :return: The listeners of this LoadbalancerResp.
        :rtype: list[:class:`huaweicloudsdkelb.v2.ResourceList`]
        """
        return self._listeners

    @listeners.setter
    def listeners(self, listeners):
        """Sets the listeners of this LoadbalancerResp.

        负载均衡器关联的监听器ID的列表

        :param listeners: The listeners of this LoadbalancerResp.
        :type listeners: list[:class:`huaweicloudsdkelb.v2.ResourceList`]
        """
        self._listeners = listeners

    @property
    def pools(self):
        """Gets the pools of this LoadbalancerResp.

        负载均衡器关联的后端云服务器组ID的列表。

        :return: The pools of this LoadbalancerResp.
        :rtype: list[:class:`huaweicloudsdkelb.v2.ResourceList`]
        """
        return self._pools

    @pools.setter
    def pools(self, pools):
        """Sets the pools of this LoadbalancerResp.

        负载均衡器关联的后端云服务器组ID的列表。

        :param pools: The pools of this LoadbalancerResp.
        :type pools: list[:class:`huaweicloudsdkelb.v2.ResourceList`]
        """
        self._pools = pools

    @property
    def provider(self):
        """Gets the provider of this LoadbalancerResp.

        负载均衡器的供应者名称。只支持vlb

        :return: The provider of this LoadbalancerResp.
        :rtype: str
        """
        return self._provider

    @provider.setter
    def provider(self, provider):
        """Sets the provider of this LoadbalancerResp.

        负载均衡器的供应者名称。只支持vlb

        :param provider: The provider of this LoadbalancerResp.
        :type provider: str
        """
        self._provider = provider

    @property
    def operating_status(self):
        """Gets the operating_status of this LoadbalancerResp.

        负载均衡器的操作状态

        :return: The operating_status of this LoadbalancerResp.
        :rtype: str
        """
        return self._operating_status

    @operating_status.setter
    def operating_status(self, operating_status):
        """Sets the operating_status of this LoadbalancerResp.

        负载均衡器的操作状态

        :param operating_status: The operating_status of this LoadbalancerResp.
        :type operating_status: str
        """
        self._operating_status = operating_status

    @property
    def provisioning_status(self):
        """Gets the provisioning_status of this LoadbalancerResp.

        负载均衡器的配置状态

        :return: The provisioning_status of this LoadbalancerResp.
        :rtype: str
        """
        return self._provisioning_status

    @provisioning_status.setter
    def provisioning_status(self, provisioning_status):
        """Sets the provisioning_status of this LoadbalancerResp.

        负载均衡器的配置状态

        :param provisioning_status: The provisioning_status of this LoadbalancerResp.
        :type provisioning_status: str
        """
        self._provisioning_status = provisioning_status

    @property
    def admin_state_up(self):
        """Gets the admin_state_up of this LoadbalancerResp.

        负载均衡器的管理状态。只支持设定为true，该字段的值无实际意义。

        :return: The admin_state_up of this LoadbalancerResp.
        :rtype: bool
        """
        return self._admin_state_up

    @admin_state_up.setter
    def admin_state_up(self, admin_state_up):
        """Sets the admin_state_up of this LoadbalancerResp.

        负载均衡器的管理状态。只支持设定为true，该字段的值无实际意义。

        :param admin_state_up: The admin_state_up of this LoadbalancerResp.
        :type admin_state_up: bool
        """
        self._admin_state_up = admin_state_up

    @property
    def created_at(self):
        """Gets the created_at of this LoadbalancerResp.

        负载均衡器的创建时间

        :return: The created_at of this LoadbalancerResp.
        :rtype: str
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this LoadbalancerResp.

        负载均衡器的创建时间

        :param created_at: The created_at of this LoadbalancerResp.
        :type created_at: str
        """
        self._created_at = created_at

    @property
    def updated_at(self):
        """Gets the updated_at of this LoadbalancerResp.

        负载均衡器的更新时间

        :return: The updated_at of this LoadbalancerResp.
        :rtype: str
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this LoadbalancerResp.

        负载均衡器的更新时间

        :param updated_at: The updated_at of this LoadbalancerResp.
        :type updated_at: str
        """
        self._updated_at = updated_at

    @property
    def enterprise_project_id(self):
        """Gets the enterprise_project_id of this LoadbalancerResp.

        负载均衡器的企业项目ID。

        :return: The enterprise_project_id of this LoadbalancerResp.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        """Sets the enterprise_project_id of this LoadbalancerResp.

        负载均衡器的企业项目ID。

        :param enterprise_project_id: The enterprise_project_id of this LoadbalancerResp.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def project_id(self):
        """Gets the project_id of this LoadbalancerResp.

        负载均衡器所在的项目ID。

        :return: The project_id of this LoadbalancerResp.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """Sets the project_id of this LoadbalancerResp.

        负载均衡器所在的项目ID。

        :param project_id: The project_id of this LoadbalancerResp.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def tags(self):
        """Gets the tags of this LoadbalancerResp.

        负载均衡器的标签列表

        :return: The tags of this LoadbalancerResp.
        :rtype: list[str]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this LoadbalancerResp.

        负载均衡器的标签列表

        :param tags: The tags of this LoadbalancerResp.
        :type tags: list[str]
        """
        self._tags = tags

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
        if not isinstance(other, LoadbalancerResp):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

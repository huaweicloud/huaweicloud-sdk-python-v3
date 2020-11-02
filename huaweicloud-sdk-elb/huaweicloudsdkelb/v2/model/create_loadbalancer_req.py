# coding: utf-8

import pprint
import re

import six





class CreateLoadbalancerReq:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'tenant_id': 'str',
        'name': 'str',
        'description': 'str',
        'vip_subnet_id': 'str',
        'vip_address': 'str',
        'provider': 'str',
        'admin_state_up': 'bool',
        'enterprise_project_id': 'str'
    }

    attribute_map = {
        'tenant_id': 'tenant_id',
        'name': 'name',
        'description': 'description',
        'vip_subnet_id': 'vip_subnet_id',
        'vip_address': 'vip_address',
        'provider': 'provider',
        'admin_state_up': 'admin_state_up',
        'enterprise_project_id': 'enterprise_project_id'
    }

    def __init__(self, tenant_id=None, name=None, description=None, vip_subnet_id=None, vip_address=None, provider=None, admin_state_up=None, enterprise_project_id=None):
        """CreateLoadbalancerReq - a model defined in huaweicloud sdk"""
        
        

        self._tenant_id = None
        self._name = None
        self._description = None
        self._vip_subnet_id = None
        self._vip_address = None
        self._provider = None
        self._admin_state_up = None
        self._enterprise_project_id = None
        self.discriminator = None

        if tenant_id is not None:
            self.tenant_id = tenant_id
        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        self.vip_subnet_id = vip_subnet_id
        if vip_address is not None:
            self.vip_address = vip_address
        if provider is not None:
            self.provider = provider
        if admin_state_up is not None:
            self.admin_state_up = admin_state_up
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id

    @property
    def tenant_id(self):
        """Gets the tenant_id of this CreateLoadbalancerReq.

        负载均衡器所在的项目ID。

        :return: The tenant_id of this CreateLoadbalancerReq.
        :rtype: str
        """
        return self._tenant_id

    @tenant_id.setter
    def tenant_id(self, tenant_id):
        """Sets the tenant_id of this CreateLoadbalancerReq.

        负载均衡器所在的项目ID。

        :param tenant_id: The tenant_id of this CreateLoadbalancerReq.
        :type: str
        """
        self._tenant_id = tenant_id

    @property
    def name(self):
        """Gets the name of this CreateLoadbalancerReq.

        负载均衡器名称。

        :return: The name of this CreateLoadbalancerReq.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CreateLoadbalancerReq.

        负载均衡器名称。

        :param name: The name of this CreateLoadbalancerReq.
        :type: str
        """
        self._name = name

    @property
    def description(self):
        """Gets the description of this CreateLoadbalancerReq.

        负载均衡器的描述信息

        :return: The description of this CreateLoadbalancerReq.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this CreateLoadbalancerReq.

        负载均衡器的描述信息

        :param description: The description of this CreateLoadbalancerReq.
        :type: str
        """
        self._description = description

    @property
    def vip_subnet_id(self):
        """Gets the vip_subnet_id of this CreateLoadbalancerReq.

        负载均衡器所在的子网ID

        :return: The vip_subnet_id of this CreateLoadbalancerReq.
        :rtype: str
        """
        return self._vip_subnet_id

    @vip_subnet_id.setter
    def vip_subnet_id(self, vip_subnet_id):
        """Sets the vip_subnet_id of this CreateLoadbalancerReq.

        负载均衡器所在的子网ID

        :param vip_subnet_id: The vip_subnet_id of this CreateLoadbalancerReq.
        :type: str
        """
        self._vip_subnet_id = vip_subnet_id

    @property
    def vip_address(self):
        """Gets the vip_address of this CreateLoadbalancerReq.

        负载均衡器的虚拟IP。

        :return: The vip_address of this CreateLoadbalancerReq.
        :rtype: str
        """
        return self._vip_address

    @vip_address.setter
    def vip_address(self, vip_address):
        """Sets the vip_address of this CreateLoadbalancerReq.

        负载均衡器的虚拟IP。

        :param vip_address: The vip_address of this CreateLoadbalancerReq.
        :type: str
        """
        self._vip_address = vip_address

    @property
    def provider(self):
        """Gets the provider of this CreateLoadbalancerReq.

        负载均衡器的供应者名称。只支持vlb

        :return: The provider of this CreateLoadbalancerReq.
        :rtype: str
        """
        return self._provider

    @provider.setter
    def provider(self, provider):
        """Sets the provider of this CreateLoadbalancerReq.

        负载均衡器的供应者名称。只支持vlb

        :param provider: The provider of this CreateLoadbalancerReq.
        :type: str
        """
        self._provider = provider

    @property
    def admin_state_up(self):
        """Gets the admin_state_up of this CreateLoadbalancerReq.

        负载均衡器的管理状态。只支持设定为true，该字段的值无实际意义。

        :return: The admin_state_up of this CreateLoadbalancerReq.
        :rtype: bool
        """
        return self._admin_state_up

    @admin_state_up.setter
    def admin_state_up(self, admin_state_up):
        """Sets the admin_state_up of this CreateLoadbalancerReq.

        负载均衡器的管理状态。只支持设定为true，该字段的值无实际意义。

        :param admin_state_up: The admin_state_up of this CreateLoadbalancerReq.
        :type: bool
        """
        self._admin_state_up = admin_state_up

    @property
    def enterprise_project_id(self):
        """Gets the enterprise_project_id of this CreateLoadbalancerReq.

        企业项目ID。创建负载均衡器时，给负载均衡器绑定企业项目ID。取值范围：最大长度36字节，带“-”连字符的UUID格式，或者是字符串“0”。“0”表示默认企业项目。 关于企业项目ID的获取及企业项目特性的详细信息，请参见《企业管理用户指南》。

        :return: The enterprise_project_id of this CreateLoadbalancerReq.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        """Sets the enterprise_project_id of this CreateLoadbalancerReq.

        企业项目ID。创建负载均衡器时，给负载均衡器绑定企业项目ID。取值范围：最大长度36字节，带“-”连字符的UUID格式，或者是字符串“0”。“0”表示默认企业项目。 关于企业项目ID的获取及企业项目特性的详细信息，请参见《企业管理用户指南》。

        :param enterprise_project_id: The enterprise_project_id of this CreateLoadbalancerReq.
        :type: str
        """
        self._enterprise_project_id = enterprise_project_id

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
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, CreateLoadbalancerReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

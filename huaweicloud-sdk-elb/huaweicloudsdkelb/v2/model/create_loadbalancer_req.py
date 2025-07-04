# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


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
        'enterprise_project_id': 'str',
        'protection_status': 'str',
        'protection_reason': 'str',
        'prepaid_options': 'PrepaidCreateOption'
    }

    attribute_map = {
        'tenant_id': 'tenant_id',
        'name': 'name',
        'description': 'description',
        'vip_subnet_id': 'vip_subnet_id',
        'vip_address': 'vip_address',
        'provider': 'provider',
        'admin_state_up': 'admin_state_up',
        'enterprise_project_id': 'enterprise_project_id',
        'protection_status': 'protection_status',
        'protection_reason': 'protection_reason',
        'prepaid_options': 'prepaid_options'
    }

    def __init__(self, tenant_id=None, name=None, description=None, vip_subnet_id=None, vip_address=None, provider=None, admin_state_up=None, enterprise_project_id=None, protection_status=None, protection_reason=None, prepaid_options=None):
        r"""CreateLoadbalancerReq

        The model defined in huaweicloud sdk

        :param tenant_id: 负载均衡器所在的项目ID。
        :type tenant_id: str
        :param name: 负载均衡器名称。
        :type name: str
        :param description: 负载均衡器的描述信息
        :type description: str
        :param vip_subnet_id: 负载均衡器所在的子网IPv4子网ID
        :type vip_subnet_id: str
        :param vip_address: 负载均衡器的虚拟IP。
        :type vip_address: str
        :param provider: 负载均衡器的供应者名称。只支持vlb
        :type provider: str
        :param admin_state_up: 负载均衡器的管理状态。只支持设定为true，该字段的值无实际意义。
        :type admin_state_up: bool
        :param enterprise_project_id: 企业项目ID。创建负载均衡器时，给负载均衡器绑定企业项目ID。取值范围：最大长度36字节，带“-”连字符的UUID格式，或者是字符串“0”。“0”表示默认企业项目。 关于企业项目ID的获取及企业项目特性的详细信息，请参见《企业管理用户指南》。
        :type enterprise_project_id: str
        :param protection_status: 修改保护状态, 取值： - nonProtection: 不保护，默认值为nonProtection - consoleProtection: 控制台修改保护
        :type protection_status: str
        :param protection_reason: 设置保护的原因 &gt;仅当protection_status为consoleProtection时有效。
        :type protection_reason: str
        :param prepaid_options: 
        :type prepaid_options: :class:`huaweicloudsdkelb.v2.PrepaidCreateOption`
        """
        
        

        self._tenant_id = None
        self._name = None
        self._description = None
        self._vip_subnet_id = None
        self._vip_address = None
        self._provider = None
        self._admin_state_up = None
        self._enterprise_project_id = None
        self._protection_status = None
        self._protection_reason = None
        self._prepaid_options = None
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
        if protection_status is not None:
            self.protection_status = protection_status
        if protection_reason is not None:
            self.protection_reason = protection_reason
        if prepaid_options is not None:
            self.prepaid_options = prepaid_options

    @property
    def tenant_id(self):
        r"""Gets the tenant_id of this CreateLoadbalancerReq.

        负载均衡器所在的项目ID。

        :return: The tenant_id of this CreateLoadbalancerReq.
        :rtype: str
        """
        return self._tenant_id

    @tenant_id.setter
    def tenant_id(self, tenant_id):
        r"""Sets the tenant_id of this CreateLoadbalancerReq.

        负载均衡器所在的项目ID。

        :param tenant_id: The tenant_id of this CreateLoadbalancerReq.
        :type tenant_id: str
        """
        self._tenant_id = tenant_id

    @property
    def name(self):
        r"""Gets the name of this CreateLoadbalancerReq.

        负载均衡器名称。

        :return: The name of this CreateLoadbalancerReq.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this CreateLoadbalancerReq.

        负载均衡器名称。

        :param name: The name of this CreateLoadbalancerReq.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        r"""Gets the description of this CreateLoadbalancerReq.

        负载均衡器的描述信息

        :return: The description of this CreateLoadbalancerReq.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this CreateLoadbalancerReq.

        负载均衡器的描述信息

        :param description: The description of this CreateLoadbalancerReq.
        :type description: str
        """
        self._description = description

    @property
    def vip_subnet_id(self):
        r"""Gets the vip_subnet_id of this CreateLoadbalancerReq.

        负载均衡器所在的子网IPv4子网ID

        :return: The vip_subnet_id of this CreateLoadbalancerReq.
        :rtype: str
        """
        return self._vip_subnet_id

    @vip_subnet_id.setter
    def vip_subnet_id(self, vip_subnet_id):
        r"""Sets the vip_subnet_id of this CreateLoadbalancerReq.

        负载均衡器所在的子网IPv4子网ID

        :param vip_subnet_id: The vip_subnet_id of this CreateLoadbalancerReq.
        :type vip_subnet_id: str
        """
        self._vip_subnet_id = vip_subnet_id

    @property
    def vip_address(self):
        r"""Gets the vip_address of this CreateLoadbalancerReq.

        负载均衡器的虚拟IP。

        :return: The vip_address of this CreateLoadbalancerReq.
        :rtype: str
        """
        return self._vip_address

    @vip_address.setter
    def vip_address(self, vip_address):
        r"""Sets the vip_address of this CreateLoadbalancerReq.

        负载均衡器的虚拟IP。

        :param vip_address: The vip_address of this CreateLoadbalancerReq.
        :type vip_address: str
        """
        self._vip_address = vip_address

    @property
    def provider(self):
        r"""Gets the provider of this CreateLoadbalancerReq.

        负载均衡器的供应者名称。只支持vlb

        :return: The provider of this CreateLoadbalancerReq.
        :rtype: str
        """
        return self._provider

    @provider.setter
    def provider(self, provider):
        r"""Sets the provider of this CreateLoadbalancerReq.

        负载均衡器的供应者名称。只支持vlb

        :param provider: The provider of this CreateLoadbalancerReq.
        :type provider: str
        """
        self._provider = provider

    @property
    def admin_state_up(self):
        r"""Gets the admin_state_up of this CreateLoadbalancerReq.

        负载均衡器的管理状态。只支持设定为true，该字段的值无实际意义。

        :return: The admin_state_up of this CreateLoadbalancerReq.
        :rtype: bool
        """
        return self._admin_state_up

    @admin_state_up.setter
    def admin_state_up(self, admin_state_up):
        r"""Sets the admin_state_up of this CreateLoadbalancerReq.

        负载均衡器的管理状态。只支持设定为true，该字段的值无实际意义。

        :param admin_state_up: The admin_state_up of this CreateLoadbalancerReq.
        :type admin_state_up: bool
        """
        self._admin_state_up = admin_state_up

    @property
    def enterprise_project_id(self):
        r"""Gets the enterprise_project_id of this CreateLoadbalancerReq.

        企业项目ID。创建负载均衡器时，给负载均衡器绑定企业项目ID。取值范围：最大长度36字节，带“-”连字符的UUID格式，或者是字符串“0”。“0”表示默认企业项目。 关于企业项目ID的获取及企业项目特性的详细信息，请参见《企业管理用户指南》。

        :return: The enterprise_project_id of this CreateLoadbalancerReq.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        r"""Sets the enterprise_project_id of this CreateLoadbalancerReq.

        企业项目ID。创建负载均衡器时，给负载均衡器绑定企业项目ID。取值范围：最大长度36字节，带“-”连字符的UUID格式，或者是字符串“0”。“0”表示默认企业项目。 关于企业项目ID的获取及企业项目特性的详细信息，请参见《企业管理用户指南》。

        :param enterprise_project_id: The enterprise_project_id of this CreateLoadbalancerReq.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def protection_status(self):
        r"""Gets the protection_status of this CreateLoadbalancerReq.

        修改保护状态, 取值： - nonProtection: 不保护，默认值为nonProtection - consoleProtection: 控制台修改保护

        :return: The protection_status of this CreateLoadbalancerReq.
        :rtype: str
        """
        return self._protection_status

    @protection_status.setter
    def protection_status(self, protection_status):
        r"""Sets the protection_status of this CreateLoadbalancerReq.

        修改保护状态, 取值： - nonProtection: 不保护，默认值为nonProtection - consoleProtection: 控制台修改保护

        :param protection_status: The protection_status of this CreateLoadbalancerReq.
        :type protection_status: str
        """
        self._protection_status = protection_status

    @property
    def protection_reason(self):
        r"""Gets the protection_reason of this CreateLoadbalancerReq.

        设置保护的原因 >仅当protection_status为consoleProtection时有效。

        :return: The protection_reason of this CreateLoadbalancerReq.
        :rtype: str
        """
        return self._protection_reason

    @protection_reason.setter
    def protection_reason(self, protection_reason):
        r"""Sets the protection_reason of this CreateLoadbalancerReq.

        设置保护的原因 >仅当protection_status为consoleProtection时有效。

        :param protection_reason: The protection_reason of this CreateLoadbalancerReq.
        :type protection_reason: str
        """
        self._protection_reason = protection_reason

    @property
    def prepaid_options(self):
        r"""Gets the prepaid_options of this CreateLoadbalancerReq.

        :return: The prepaid_options of this CreateLoadbalancerReq.
        :rtype: :class:`huaweicloudsdkelb.v2.PrepaidCreateOption`
        """
        return self._prepaid_options

    @prepaid_options.setter
    def prepaid_options(self, prepaid_options):
        r"""Sets the prepaid_options of this CreateLoadbalancerReq.

        :param prepaid_options: The prepaid_options of this CreateLoadbalancerReq.
        :type prepaid_options: :class:`huaweicloudsdkelb.v2.PrepaidCreateOption`
        """
        self._prepaid_options = prepaid_options

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
        if not isinstance(other, CreateLoadbalancerReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class LoadBalancer:

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
        'name': 'str',
        'guaranteed': 'str',
        'billing_info': 'str',
        'description': 'str',
        'vpc_id': 'str',
        'provisioning_status': 'str',
        'listeners': 'list[IdListWrapper]',
        'vip_address': 'str',
        'vip_port_id': 'str',
        'ipv6_vip_address': 'str',
        'publicips': 'list[PublicIpInfo]'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'guaranteed': 'guaranteed',
        'billing_info': 'billing_info',
        'description': 'description',
        'vpc_id': 'vpc_id',
        'provisioning_status': 'provisioning_status',
        'listeners': 'listeners',
        'vip_address': 'vip_address',
        'vip_port_id': 'vip_port_id',
        'ipv6_vip_address': 'ipv6_vip_address',
        'publicips': 'publicips'
    }

    def __init__(self, id=None, name=None, guaranteed=None, billing_info=None, description=None, vpc_id=None, provisioning_status=None, listeners=None, vip_address=None, vip_port_id=None, ipv6_vip_address=None, publicips=None):
        r"""LoadBalancer

        The model defined in huaweicloud sdk

        :param id: 负载均衡器ID。
        :type id: str
        :param name: 负载均衡器名称。
        :type name: str
        :param guaranteed: 是否独享型负载均衡器。
        :type guaranteed: str
        :param billing_info: 资源账单信息。
        :type billing_info: str
        :param description: 描述信息。
        :type description: str
        :param vpc_id: 负载均衡器所属VPC ID，即虚拟私有云ID。
        :type vpc_id: str
        :param provisioning_status: 负载均衡器的配置状态。
        :type provisioning_status: str
        :param listeners: 关联的listener列表。
        :type listeners: list[:class:`huaweicloudsdkcss.v1.IdListWrapper`]
        :param vip_address: 负载均衡器的IPv4虚拟IP地址。
        :type vip_address: str
        :param vip_port_id: 负载均衡器的IPv4对应的port ID。
        :type vip_port_id: str
        :param ipv6_vip_address: 负载均衡器的IPv6地址。
        :type ipv6_vip_address: str
        :param publicips: 负载均衡器绑定的公网IP。
        :type publicips: list[:class:`huaweicloudsdkcss.v1.PublicIpInfo`]
        """
        
        

        self._id = None
        self._name = None
        self._guaranteed = None
        self._billing_info = None
        self._description = None
        self._vpc_id = None
        self._provisioning_status = None
        self._listeners = None
        self._vip_address = None
        self._vip_port_id = None
        self._ipv6_vip_address = None
        self._publicips = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if guaranteed is not None:
            self.guaranteed = guaranteed
        if billing_info is not None:
            self.billing_info = billing_info
        if description is not None:
            self.description = description
        if vpc_id is not None:
            self.vpc_id = vpc_id
        if provisioning_status is not None:
            self.provisioning_status = provisioning_status
        if listeners is not None:
            self.listeners = listeners
        if vip_address is not None:
            self.vip_address = vip_address
        if vip_port_id is not None:
            self.vip_port_id = vip_port_id
        if ipv6_vip_address is not None:
            self.ipv6_vip_address = ipv6_vip_address
        if publicips is not None:
            self.publicips = publicips

    @property
    def id(self):
        r"""Gets the id of this LoadBalancer.

        负载均衡器ID。

        :return: The id of this LoadBalancer.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this LoadBalancer.

        负载均衡器ID。

        :param id: The id of this LoadBalancer.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        r"""Gets the name of this LoadBalancer.

        负载均衡器名称。

        :return: The name of this LoadBalancer.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this LoadBalancer.

        负载均衡器名称。

        :param name: The name of this LoadBalancer.
        :type name: str
        """
        self._name = name

    @property
    def guaranteed(self):
        r"""Gets the guaranteed of this LoadBalancer.

        是否独享型负载均衡器。

        :return: The guaranteed of this LoadBalancer.
        :rtype: str
        """
        return self._guaranteed

    @guaranteed.setter
    def guaranteed(self, guaranteed):
        r"""Sets the guaranteed of this LoadBalancer.

        是否独享型负载均衡器。

        :param guaranteed: The guaranteed of this LoadBalancer.
        :type guaranteed: str
        """
        self._guaranteed = guaranteed

    @property
    def billing_info(self):
        r"""Gets the billing_info of this LoadBalancer.

        资源账单信息。

        :return: The billing_info of this LoadBalancer.
        :rtype: str
        """
        return self._billing_info

    @billing_info.setter
    def billing_info(self, billing_info):
        r"""Sets the billing_info of this LoadBalancer.

        资源账单信息。

        :param billing_info: The billing_info of this LoadBalancer.
        :type billing_info: str
        """
        self._billing_info = billing_info

    @property
    def description(self):
        r"""Gets the description of this LoadBalancer.

        描述信息。

        :return: The description of this LoadBalancer.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this LoadBalancer.

        描述信息。

        :param description: The description of this LoadBalancer.
        :type description: str
        """
        self._description = description

    @property
    def vpc_id(self):
        r"""Gets the vpc_id of this LoadBalancer.

        负载均衡器所属VPC ID，即虚拟私有云ID。

        :return: The vpc_id of this LoadBalancer.
        :rtype: str
        """
        return self._vpc_id

    @vpc_id.setter
    def vpc_id(self, vpc_id):
        r"""Sets the vpc_id of this LoadBalancer.

        负载均衡器所属VPC ID，即虚拟私有云ID。

        :param vpc_id: The vpc_id of this LoadBalancer.
        :type vpc_id: str
        """
        self._vpc_id = vpc_id

    @property
    def provisioning_status(self):
        r"""Gets the provisioning_status of this LoadBalancer.

        负载均衡器的配置状态。

        :return: The provisioning_status of this LoadBalancer.
        :rtype: str
        """
        return self._provisioning_status

    @provisioning_status.setter
    def provisioning_status(self, provisioning_status):
        r"""Sets the provisioning_status of this LoadBalancer.

        负载均衡器的配置状态。

        :param provisioning_status: The provisioning_status of this LoadBalancer.
        :type provisioning_status: str
        """
        self._provisioning_status = provisioning_status

    @property
    def listeners(self):
        r"""Gets the listeners of this LoadBalancer.

        关联的listener列表。

        :return: The listeners of this LoadBalancer.
        :rtype: list[:class:`huaweicloudsdkcss.v1.IdListWrapper`]
        """
        return self._listeners

    @listeners.setter
    def listeners(self, listeners):
        r"""Sets the listeners of this LoadBalancer.

        关联的listener列表。

        :param listeners: The listeners of this LoadBalancer.
        :type listeners: list[:class:`huaweicloudsdkcss.v1.IdListWrapper`]
        """
        self._listeners = listeners

    @property
    def vip_address(self):
        r"""Gets the vip_address of this LoadBalancer.

        负载均衡器的IPv4虚拟IP地址。

        :return: The vip_address of this LoadBalancer.
        :rtype: str
        """
        return self._vip_address

    @vip_address.setter
    def vip_address(self, vip_address):
        r"""Sets the vip_address of this LoadBalancer.

        负载均衡器的IPv4虚拟IP地址。

        :param vip_address: The vip_address of this LoadBalancer.
        :type vip_address: str
        """
        self._vip_address = vip_address

    @property
    def vip_port_id(self):
        r"""Gets the vip_port_id of this LoadBalancer.

        负载均衡器的IPv4对应的port ID。

        :return: The vip_port_id of this LoadBalancer.
        :rtype: str
        """
        return self._vip_port_id

    @vip_port_id.setter
    def vip_port_id(self, vip_port_id):
        r"""Sets the vip_port_id of this LoadBalancer.

        负载均衡器的IPv4对应的port ID。

        :param vip_port_id: The vip_port_id of this LoadBalancer.
        :type vip_port_id: str
        """
        self._vip_port_id = vip_port_id

    @property
    def ipv6_vip_address(self):
        r"""Gets the ipv6_vip_address of this LoadBalancer.

        负载均衡器的IPv6地址。

        :return: The ipv6_vip_address of this LoadBalancer.
        :rtype: str
        """
        return self._ipv6_vip_address

    @ipv6_vip_address.setter
    def ipv6_vip_address(self, ipv6_vip_address):
        r"""Sets the ipv6_vip_address of this LoadBalancer.

        负载均衡器的IPv6地址。

        :param ipv6_vip_address: The ipv6_vip_address of this LoadBalancer.
        :type ipv6_vip_address: str
        """
        self._ipv6_vip_address = ipv6_vip_address

    @property
    def publicips(self):
        r"""Gets the publicips of this LoadBalancer.

        负载均衡器绑定的公网IP。

        :return: The publicips of this LoadBalancer.
        :rtype: list[:class:`huaweicloudsdkcss.v1.PublicIpInfo`]
        """
        return self._publicips

    @publicips.setter
    def publicips(self, publicips):
        r"""Sets the publicips of this LoadBalancer.

        负载均衡器绑定的公网IP。

        :param publicips: The publicips of this LoadBalancer.
        :type publicips: list[:class:`huaweicloudsdkcss.v1.PublicIpInfo`]
        """
        self._publicips = publicips

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
        if not isinstance(other, LoadBalancer):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

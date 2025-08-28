# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class EsLoadBalancerResource:

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
        'listeners': 'EsListenersResource',
        'vip_address': 'str',
        'publicips': 'EsPublicipsResource'
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
        'publicips': 'publicips'
    }

    def __init__(self, id=None, name=None, guaranteed=None, billing_info=None, description=None, vpc_id=None, provisioning_status=None, listeners=None, vip_address=None, publicips=None):
        r"""EsLoadBalancerResource

        The model defined in huaweicloud sdk

        :param id: 负载均衡器ID。
        :type id: str
        :param name: 负载均衡器名称。
        :type name: str
        :param guaranteed: Indicates whether the LB is an exclusive LB. - false：共享型。 - true：独享型。
        :type guaranteed: str
        :param billing_info: 资源账单信息 - 空：按需计费。 - 非空：包周期计费。
        :type billing_info: str
        :param description: 描述信息。
        :type description: str
        :param vpc_id: 负载均衡器所属VPC ID。
        :type vpc_id: str
        :param provisioning_status: 负载均衡器的配置状态。
        :type provisioning_status: str
        :param listeners: 
        :type listeners: :class:`huaweicloudsdkcss.v1.EsListenersResource`
        :param vip_address: 负载均衡器的IPv4虚拟IP地址。
        :type vip_address: str
        :param publicips: 
        :type publicips: :class:`huaweicloudsdkcss.v1.EsPublicipsResource`
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
        if publicips is not None:
            self.publicips = publicips

    @property
    def id(self):
        r"""Gets the id of this EsLoadBalancerResource.

        负载均衡器ID。

        :return: The id of this EsLoadBalancerResource.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this EsLoadBalancerResource.

        负载均衡器ID。

        :param id: The id of this EsLoadBalancerResource.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        r"""Gets the name of this EsLoadBalancerResource.

        负载均衡器名称。

        :return: The name of this EsLoadBalancerResource.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this EsLoadBalancerResource.

        负载均衡器名称。

        :param name: The name of this EsLoadBalancerResource.
        :type name: str
        """
        self._name = name

    @property
    def guaranteed(self):
        r"""Gets the guaranteed of this EsLoadBalancerResource.

        Indicates whether the LB is an exclusive LB. - false：共享型。 - true：独享型。

        :return: The guaranteed of this EsLoadBalancerResource.
        :rtype: str
        """
        return self._guaranteed

    @guaranteed.setter
    def guaranteed(self, guaranteed):
        r"""Sets the guaranteed of this EsLoadBalancerResource.

        Indicates whether the LB is an exclusive LB. - false：共享型。 - true：独享型。

        :param guaranteed: The guaranteed of this EsLoadBalancerResource.
        :type guaranteed: str
        """
        self._guaranteed = guaranteed

    @property
    def billing_info(self):
        r"""Gets the billing_info of this EsLoadBalancerResource.

        资源账单信息 - 空：按需计费。 - 非空：包周期计费。

        :return: The billing_info of this EsLoadBalancerResource.
        :rtype: str
        """
        return self._billing_info

    @billing_info.setter
    def billing_info(self, billing_info):
        r"""Sets the billing_info of this EsLoadBalancerResource.

        资源账单信息 - 空：按需计费。 - 非空：包周期计费。

        :param billing_info: The billing_info of this EsLoadBalancerResource.
        :type billing_info: str
        """
        self._billing_info = billing_info

    @property
    def description(self):
        r"""Gets the description of this EsLoadBalancerResource.

        描述信息。

        :return: The description of this EsLoadBalancerResource.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this EsLoadBalancerResource.

        描述信息。

        :param description: The description of this EsLoadBalancerResource.
        :type description: str
        """
        self._description = description

    @property
    def vpc_id(self):
        r"""Gets the vpc_id of this EsLoadBalancerResource.

        负载均衡器所属VPC ID。

        :return: The vpc_id of this EsLoadBalancerResource.
        :rtype: str
        """
        return self._vpc_id

    @vpc_id.setter
    def vpc_id(self, vpc_id):
        r"""Sets the vpc_id of this EsLoadBalancerResource.

        负载均衡器所属VPC ID。

        :param vpc_id: The vpc_id of this EsLoadBalancerResource.
        :type vpc_id: str
        """
        self._vpc_id = vpc_id

    @property
    def provisioning_status(self):
        r"""Gets the provisioning_status of this EsLoadBalancerResource.

        负载均衡器的配置状态。

        :return: The provisioning_status of this EsLoadBalancerResource.
        :rtype: str
        """
        return self._provisioning_status

    @provisioning_status.setter
    def provisioning_status(self, provisioning_status):
        r"""Sets the provisioning_status of this EsLoadBalancerResource.

        负载均衡器的配置状态。

        :param provisioning_status: The provisioning_status of this EsLoadBalancerResource.
        :type provisioning_status: str
        """
        self._provisioning_status = provisioning_status

    @property
    def listeners(self):
        r"""Gets the listeners of this EsLoadBalancerResource.

        :return: The listeners of this EsLoadBalancerResource.
        :rtype: :class:`huaweicloudsdkcss.v1.EsListenersResource`
        """
        return self._listeners

    @listeners.setter
    def listeners(self, listeners):
        r"""Sets the listeners of this EsLoadBalancerResource.

        :param listeners: The listeners of this EsLoadBalancerResource.
        :type listeners: :class:`huaweicloudsdkcss.v1.EsListenersResource`
        """
        self._listeners = listeners

    @property
    def vip_address(self):
        r"""Gets the vip_address of this EsLoadBalancerResource.

        负载均衡器的IPv4虚拟IP地址。

        :return: The vip_address of this EsLoadBalancerResource.
        :rtype: str
        """
        return self._vip_address

    @vip_address.setter
    def vip_address(self, vip_address):
        r"""Sets the vip_address of this EsLoadBalancerResource.

        负载均衡器的IPv4虚拟IP地址。

        :param vip_address: The vip_address of this EsLoadBalancerResource.
        :type vip_address: str
        """
        self._vip_address = vip_address

    @property
    def publicips(self):
        r"""Gets the publicips of this EsLoadBalancerResource.

        :return: The publicips of this EsLoadBalancerResource.
        :rtype: :class:`huaweicloudsdkcss.v1.EsPublicipsResource`
        """
        return self._publicips

    @publicips.setter
    def publicips(self, publicips):
        r"""Sets the publicips of this EsLoadBalancerResource.

        :param publicips: The publicips of this EsLoadBalancerResource.
        :type publicips: :class:`huaweicloudsdkcss.v1.EsPublicipsResource`
        """
        self._publicips = publicips

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
        if not isinstance(other, EsLoadBalancerResource):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

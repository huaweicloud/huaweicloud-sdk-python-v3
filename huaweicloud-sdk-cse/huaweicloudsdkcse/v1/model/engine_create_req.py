# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class EngineCreateReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'name': 'str',
        'description': 'str',
        'payment': 'str',
        'flavor': 'str',
        'az_list': 'list[str]',
        'auth_type': 'str',
        'vpc': 'str',
        'vpc_id': 'str',
        'network_id': 'str',
        'subnet_cidr': 'str',
        'public_ip_id': 'str',
        'auth_cred': 'EngineRbacPwd',
        'spec_type': 'str',
        'inputs': 'dict(str, str)',
        'enginestate_info': 'EngineCreateReqEnginestateInfo',
        'period_type': 'int',
        'flavor_type': 'EngineCreateReqFlavorType',
        'enterprise_project': 'EngineCreateReqEnterpriseProject',
        'vpc_cidr': 'str',
        'resource_params': 'EngineCreateReqResourceParams',
        'product_id': 'str',
        'capacity_product_id': 'str',
        'is_free': 'bool',
        'subnet_name': 'str',
        'tags': 'list[str]',
        'maintenance_config': 'EngineCreateReqMaintenanceConfig',
        'elbid': 'str'
    }

    attribute_map = {
        'name': 'name',
        'description': 'description',
        'payment': 'payment',
        'flavor': 'flavor',
        'az_list': 'azList',
        'auth_type': 'authType',
        'vpc': 'vpc',
        'vpc_id': 'vpcId',
        'network_id': 'networkId',
        'subnet_cidr': 'subnetCidr',
        'public_ip_id': 'publicIpId',
        'auth_cred': 'auth_cred',
        'spec_type': 'specType',
        'inputs': 'inputs',
        'enginestate_info': 'enginestateInfo',
        'period_type': 'periodType',
        'flavor_type': 'flavorType',
        'enterprise_project': 'enterpriseProject',
        'vpc_cidr': 'vpcCidr',
        'resource_params': 'resourceParams',
        'product_id': 'productId',
        'capacity_product_id': 'capacityProductId',
        'is_free': 'isFree',
        'subnet_name': 'subnetName',
        'tags': 'tags',
        'maintenance_config': 'maintenanceConfig',
        'elbid': 'elbid'
    }

    def __init__(self, name=None, description=None, payment=None, flavor=None, az_list=None, auth_type=None, vpc=None, vpc_id=None, network_id=None, subnet_cidr=None, public_ip_id=None, auth_cred=None, spec_type=None, inputs=None, enginestate_info=None, period_type=None, flavor_type=None, enterprise_project=None, vpc_cidr=None, resource_params=None, product_id=None, capacity_product_id=None, is_free=None, subnet_name=None, tags=None, maintenance_config=None, elbid=None):
        r"""EngineCreateReq

        The model defined in huaweicloud sdk

        :param name: 微服务引擎的名称，名称为字母开头，字母、数字、-组成，且不能以-结尾，3-24个字符。
        :type name: str
        :param description: 微服务引擎描述，长度0~255。
        :type description: str
        :param payment: 微服务引擎计费方式，1表示按需
        :type payment: str
        :param flavor: 微服务引擎的规格
        :type flavor: str
        :param az_list: 当前局点可用区列表，创建ServiceComb引擎专享版需要填写。
        :type az_list: list[str]
        :param auth_type: ServiceComb引擎专享版与注册配置中心认证方式，RBAC为安全认证，NONE为无认证。
        :type auth_type: str
        :param vpc: vpc名称
        :type vpc: str
        :param vpc_id: vpc标识
        :type vpc_id: str
        :param network_id: 微服务引擎子网ID
        :type network_id: str
        :param subnet_cidr: 微服务引擎子网划分
        :type subnet_cidr: str
        :param public_ip_id: ServiceComb引擎专享版公网地址ID，当前为null
        :type public_ip_id: str
        :param auth_cred: 
        :type auth_cred: :class:`huaweicloudsdkcse.v1.EngineRbacPwd`
        :param spec_type: 微服务引擎部署类型
        :type spec_type: str
        :param inputs: 引擎附加参数
        :type inputs: dict(str, str)
        :param enginestate_info: 
        :type enginestate_info: :class:`huaweicloudsdkcse.v1.EngineCreateReqEnginestateInfo`
        :param period_type: 创建阶段类型
        :type period_type: int
        :param flavor_type: 
        :type flavor_type: :class:`huaweicloudsdkcse.v1.EngineCreateReqFlavorType`
        :param enterprise_project: 
        :type enterprise_project: :class:`huaweicloudsdkcse.v1.EngineCreateReqEnterpriseProject`
        :param vpc_cidr: 网关vpc划分
        :type vpc_cidr: str
        :param resource_params: 
        :type resource_params: :class:`huaweicloudsdkcse.v1.EngineCreateReqResourceParams`
        :param product_id: 产品ID
        :type product_id: str
        :param capacity_product_id: 容量产品ID
        :type capacity_product_id: str
        :param is_free: 微服务引擎是否免费
        :type is_free: bool
        :param subnet_name: 微服务引擎使用的子网名称
        :type subnet_name: str
        :param tags: 标签
        :type tags: list[str]
        :param maintenance_config: 
        :type maintenance_config: :class:`huaweicloudsdkcse.v1.EngineCreateReqMaintenanceConfig`
        :param elbid: 微服务引擎使用的elb的id
        :type elbid: str
        """
        
        

        self._name = None
        self._description = None
        self._payment = None
        self._flavor = None
        self._az_list = None
        self._auth_type = None
        self._vpc = None
        self._vpc_id = None
        self._network_id = None
        self._subnet_cidr = None
        self._public_ip_id = None
        self._auth_cred = None
        self._spec_type = None
        self._inputs = None
        self._enginestate_info = None
        self._period_type = None
        self._flavor_type = None
        self._enterprise_project = None
        self._vpc_cidr = None
        self._resource_params = None
        self._product_id = None
        self._capacity_product_id = None
        self._is_free = None
        self._subnet_name = None
        self._tags = None
        self._maintenance_config = None
        self._elbid = None
        self.discriminator = None

        self.name = name
        if description is not None:
            self.description = description
        self.payment = payment
        self.flavor = flavor
        if az_list is not None:
            self.az_list = az_list
        self.auth_type = auth_type
        self.vpc = vpc
        if vpc_id is not None:
            self.vpc_id = vpc_id
        self.network_id = network_id
        self.subnet_cidr = subnet_cidr
        if public_ip_id is not None:
            self.public_ip_id = public_ip_id
        if auth_cred is not None:
            self.auth_cred = auth_cred
        self.spec_type = spec_type
        if inputs is not None:
            self.inputs = inputs
        if enginestate_info is not None:
            self.enginestate_info = enginestate_info
        if period_type is not None:
            self.period_type = period_type
        if flavor_type is not None:
            self.flavor_type = flavor_type
        if enterprise_project is not None:
            self.enterprise_project = enterprise_project
        if vpc_cidr is not None:
            self.vpc_cidr = vpc_cidr
        if resource_params is not None:
            self.resource_params = resource_params
        if product_id is not None:
            self.product_id = product_id
        if capacity_product_id is not None:
            self.capacity_product_id = capacity_product_id
        if is_free is not None:
            self.is_free = is_free
        if subnet_name is not None:
            self.subnet_name = subnet_name
        if tags is not None:
            self.tags = tags
        if maintenance_config is not None:
            self.maintenance_config = maintenance_config
        if elbid is not None:
            self.elbid = elbid

    @property
    def name(self):
        r"""Gets the name of this EngineCreateReq.

        微服务引擎的名称，名称为字母开头，字母、数字、-组成，且不能以-结尾，3-24个字符。

        :return: The name of this EngineCreateReq.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this EngineCreateReq.

        微服务引擎的名称，名称为字母开头，字母、数字、-组成，且不能以-结尾，3-24个字符。

        :param name: The name of this EngineCreateReq.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        r"""Gets the description of this EngineCreateReq.

        微服务引擎描述，长度0~255。

        :return: The description of this EngineCreateReq.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this EngineCreateReq.

        微服务引擎描述，长度0~255。

        :param description: The description of this EngineCreateReq.
        :type description: str
        """
        self._description = description

    @property
    def payment(self):
        r"""Gets the payment of this EngineCreateReq.

        微服务引擎计费方式，1表示按需

        :return: The payment of this EngineCreateReq.
        :rtype: str
        """
        return self._payment

    @payment.setter
    def payment(self, payment):
        r"""Sets the payment of this EngineCreateReq.

        微服务引擎计费方式，1表示按需

        :param payment: The payment of this EngineCreateReq.
        :type payment: str
        """
        self._payment = payment

    @property
    def flavor(self):
        r"""Gets the flavor of this EngineCreateReq.

        微服务引擎的规格

        :return: The flavor of this EngineCreateReq.
        :rtype: str
        """
        return self._flavor

    @flavor.setter
    def flavor(self, flavor):
        r"""Sets the flavor of this EngineCreateReq.

        微服务引擎的规格

        :param flavor: The flavor of this EngineCreateReq.
        :type flavor: str
        """
        self._flavor = flavor

    @property
    def az_list(self):
        r"""Gets the az_list of this EngineCreateReq.

        当前局点可用区列表，创建ServiceComb引擎专享版需要填写。

        :return: The az_list of this EngineCreateReq.
        :rtype: list[str]
        """
        return self._az_list

    @az_list.setter
    def az_list(self, az_list):
        r"""Sets the az_list of this EngineCreateReq.

        当前局点可用区列表，创建ServiceComb引擎专享版需要填写。

        :param az_list: The az_list of this EngineCreateReq.
        :type az_list: list[str]
        """
        self._az_list = az_list

    @property
    def auth_type(self):
        r"""Gets the auth_type of this EngineCreateReq.

        ServiceComb引擎专享版与注册配置中心认证方式，RBAC为安全认证，NONE为无认证。

        :return: The auth_type of this EngineCreateReq.
        :rtype: str
        """
        return self._auth_type

    @auth_type.setter
    def auth_type(self, auth_type):
        r"""Sets the auth_type of this EngineCreateReq.

        ServiceComb引擎专享版与注册配置中心认证方式，RBAC为安全认证，NONE为无认证。

        :param auth_type: The auth_type of this EngineCreateReq.
        :type auth_type: str
        """
        self._auth_type = auth_type

    @property
    def vpc(self):
        r"""Gets the vpc of this EngineCreateReq.

        vpc名称

        :return: The vpc of this EngineCreateReq.
        :rtype: str
        """
        return self._vpc

    @vpc.setter
    def vpc(self, vpc):
        r"""Sets the vpc of this EngineCreateReq.

        vpc名称

        :param vpc: The vpc of this EngineCreateReq.
        :type vpc: str
        """
        self._vpc = vpc

    @property
    def vpc_id(self):
        r"""Gets the vpc_id of this EngineCreateReq.

        vpc标识

        :return: The vpc_id of this EngineCreateReq.
        :rtype: str
        """
        return self._vpc_id

    @vpc_id.setter
    def vpc_id(self, vpc_id):
        r"""Sets the vpc_id of this EngineCreateReq.

        vpc标识

        :param vpc_id: The vpc_id of this EngineCreateReq.
        :type vpc_id: str
        """
        self._vpc_id = vpc_id

    @property
    def network_id(self):
        r"""Gets the network_id of this EngineCreateReq.

        微服务引擎子网ID

        :return: The network_id of this EngineCreateReq.
        :rtype: str
        """
        return self._network_id

    @network_id.setter
    def network_id(self, network_id):
        r"""Sets the network_id of this EngineCreateReq.

        微服务引擎子网ID

        :param network_id: The network_id of this EngineCreateReq.
        :type network_id: str
        """
        self._network_id = network_id

    @property
    def subnet_cidr(self):
        r"""Gets the subnet_cidr of this EngineCreateReq.

        微服务引擎子网划分

        :return: The subnet_cidr of this EngineCreateReq.
        :rtype: str
        """
        return self._subnet_cidr

    @subnet_cidr.setter
    def subnet_cidr(self, subnet_cidr):
        r"""Sets the subnet_cidr of this EngineCreateReq.

        微服务引擎子网划分

        :param subnet_cidr: The subnet_cidr of this EngineCreateReq.
        :type subnet_cidr: str
        """
        self._subnet_cidr = subnet_cidr

    @property
    def public_ip_id(self):
        r"""Gets the public_ip_id of this EngineCreateReq.

        ServiceComb引擎专享版公网地址ID，当前为null

        :return: The public_ip_id of this EngineCreateReq.
        :rtype: str
        """
        return self._public_ip_id

    @public_ip_id.setter
    def public_ip_id(self, public_ip_id):
        r"""Sets the public_ip_id of this EngineCreateReq.

        ServiceComb引擎专享版公网地址ID，当前为null

        :param public_ip_id: The public_ip_id of this EngineCreateReq.
        :type public_ip_id: str
        """
        self._public_ip_id = public_ip_id

    @property
    def auth_cred(self):
        r"""Gets the auth_cred of this EngineCreateReq.

        :return: The auth_cred of this EngineCreateReq.
        :rtype: :class:`huaweicloudsdkcse.v1.EngineRbacPwd`
        """
        return self._auth_cred

    @auth_cred.setter
    def auth_cred(self, auth_cred):
        r"""Sets the auth_cred of this EngineCreateReq.

        :param auth_cred: The auth_cred of this EngineCreateReq.
        :type auth_cred: :class:`huaweicloudsdkcse.v1.EngineRbacPwd`
        """
        self._auth_cred = auth_cred

    @property
    def spec_type(self):
        r"""Gets the spec_type of this EngineCreateReq.

        微服务引擎部署类型

        :return: The spec_type of this EngineCreateReq.
        :rtype: str
        """
        return self._spec_type

    @spec_type.setter
    def spec_type(self, spec_type):
        r"""Sets the spec_type of this EngineCreateReq.

        微服务引擎部署类型

        :param spec_type: The spec_type of this EngineCreateReq.
        :type spec_type: str
        """
        self._spec_type = spec_type

    @property
    def inputs(self):
        r"""Gets the inputs of this EngineCreateReq.

        引擎附加参数

        :return: The inputs of this EngineCreateReq.
        :rtype: dict(str, str)
        """
        return self._inputs

    @inputs.setter
    def inputs(self, inputs):
        r"""Sets the inputs of this EngineCreateReq.

        引擎附加参数

        :param inputs: The inputs of this EngineCreateReq.
        :type inputs: dict(str, str)
        """
        self._inputs = inputs

    @property
    def enginestate_info(self):
        r"""Gets the enginestate_info of this EngineCreateReq.

        :return: The enginestate_info of this EngineCreateReq.
        :rtype: :class:`huaweicloudsdkcse.v1.EngineCreateReqEnginestateInfo`
        """
        return self._enginestate_info

    @enginestate_info.setter
    def enginestate_info(self, enginestate_info):
        r"""Sets the enginestate_info of this EngineCreateReq.

        :param enginestate_info: The enginestate_info of this EngineCreateReq.
        :type enginestate_info: :class:`huaweicloudsdkcse.v1.EngineCreateReqEnginestateInfo`
        """
        self._enginestate_info = enginestate_info

    @property
    def period_type(self):
        r"""Gets the period_type of this EngineCreateReq.

        创建阶段类型

        :return: The period_type of this EngineCreateReq.
        :rtype: int
        """
        return self._period_type

    @period_type.setter
    def period_type(self, period_type):
        r"""Sets the period_type of this EngineCreateReq.

        创建阶段类型

        :param period_type: The period_type of this EngineCreateReq.
        :type period_type: int
        """
        self._period_type = period_type

    @property
    def flavor_type(self):
        r"""Gets the flavor_type of this EngineCreateReq.

        :return: The flavor_type of this EngineCreateReq.
        :rtype: :class:`huaweicloudsdkcse.v1.EngineCreateReqFlavorType`
        """
        return self._flavor_type

    @flavor_type.setter
    def flavor_type(self, flavor_type):
        r"""Sets the flavor_type of this EngineCreateReq.

        :param flavor_type: The flavor_type of this EngineCreateReq.
        :type flavor_type: :class:`huaweicloudsdkcse.v1.EngineCreateReqFlavorType`
        """
        self._flavor_type = flavor_type

    @property
    def enterprise_project(self):
        r"""Gets the enterprise_project of this EngineCreateReq.

        :return: The enterprise_project of this EngineCreateReq.
        :rtype: :class:`huaweicloudsdkcse.v1.EngineCreateReqEnterpriseProject`
        """
        return self._enterprise_project

    @enterprise_project.setter
    def enterprise_project(self, enterprise_project):
        r"""Sets the enterprise_project of this EngineCreateReq.

        :param enterprise_project: The enterprise_project of this EngineCreateReq.
        :type enterprise_project: :class:`huaweicloudsdkcse.v1.EngineCreateReqEnterpriseProject`
        """
        self._enterprise_project = enterprise_project

    @property
    def vpc_cidr(self):
        r"""Gets the vpc_cidr of this EngineCreateReq.

        网关vpc划分

        :return: The vpc_cidr of this EngineCreateReq.
        :rtype: str
        """
        return self._vpc_cidr

    @vpc_cidr.setter
    def vpc_cidr(self, vpc_cidr):
        r"""Sets the vpc_cidr of this EngineCreateReq.

        网关vpc划分

        :param vpc_cidr: The vpc_cidr of this EngineCreateReq.
        :type vpc_cidr: str
        """
        self._vpc_cidr = vpc_cidr

    @property
    def resource_params(self):
        r"""Gets the resource_params of this EngineCreateReq.

        :return: The resource_params of this EngineCreateReq.
        :rtype: :class:`huaweicloudsdkcse.v1.EngineCreateReqResourceParams`
        """
        return self._resource_params

    @resource_params.setter
    def resource_params(self, resource_params):
        r"""Sets the resource_params of this EngineCreateReq.

        :param resource_params: The resource_params of this EngineCreateReq.
        :type resource_params: :class:`huaweicloudsdkcse.v1.EngineCreateReqResourceParams`
        """
        self._resource_params = resource_params

    @property
    def product_id(self):
        r"""Gets the product_id of this EngineCreateReq.

        产品ID

        :return: The product_id of this EngineCreateReq.
        :rtype: str
        """
        return self._product_id

    @product_id.setter
    def product_id(self, product_id):
        r"""Sets the product_id of this EngineCreateReq.

        产品ID

        :param product_id: The product_id of this EngineCreateReq.
        :type product_id: str
        """
        self._product_id = product_id

    @property
    def capacity_product_id(self):
        r"""Gets the capacity_product_id of this EngineCreateReq.

        容量产品ID

        :return: The capacity_product_id of this EngineCreateReq.
        :rtype: str
        """
        return self._capacity_product_id

    @capacity_product_id.setter
    def capacity_product_id(self, capacity_product_id):
        r"""Sets the capacity_product_id of this EngineCreateReq.

        容量产品ID

        :param capacity_product_id: The capacity_product_id of this EngineCreateReq.
        :type capacity_product_id: str
        """
        self._capacity_product_id = capacity_product_id

    @property
    def is_free(self):
        r"""Gets the is_free of this EngineCreateReq.

        微服务引擎是否免费

        :return: The is_free of this EngineCreateReq.
        :rtype: bool
        """
        return self._is_free

    @is_free.setter
    def is_free(self, is_free):
        r"""Sets the is_free of this EngineCreateReq.

        微服务引擎是否免费

        :param is_free: The is_free of this EngineCreateReq.
        :type is_free: bool
        """
        self._is_free = is_free

    @property
    def subnet_name(self):
        r"""Gets the subnet_name of this EngineCreateReq.

        微服务引擎使用的子网名称

        :return: The subnet_name of this EngineCreateReq.
        :rtype: str
        """
        return self._subnet_name

    @subnet_name.setter
    def subnet_name(self, subnet_name):
        r"""Sets the subnet_name of this EngineCreateReq.

        微服务引擎使用的子网名称

        :param subnet_name: The subnet_name of this EngineCreateReq.
        :type subnet_name: str
        """
        self._subnet_name = subnet_name

    @property
    def tags(self):
        r"""Gets the tags of this EngineCreateReq.

        标签

        :return: The tags of this EngineCreateReq.
        :rtype: list[str]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        r"""Sets the tags of this EngineCreateReq.

        标签

        :param tags: The tags of this EngineCreateReq.
        :type tags: list[str]
        """
        self._tags = tags

    @property
    def maintenance_config(self):
        r"""Gets the maintenance_config of this EngineCreateReq.

        :return: The maintenance_config of this EngineCreateReq.
        :rtype: :class:`huaweicloudsdkcse.v1.EngineCreateReqMaintenanceConfig`
        """
        return self._maintenance_config

    @maintenance_config.setter
    def maintenance_config(self, maintenance_config):
        r"""Sets the maintenance_config of this EngineCreateReq.

        :param maintenance_config: The maintenance_config of this EngineCreateReq.
        :type maintenance_config: :class:`huaweicloudsdkcse.v1.EngineCreateReqMaintenanceConfig`
        """
        self._maintenance_config = maintenance_config

    @property
    def elbid(self):
        r"""Gets the elbid of this EngineCreateReq.

        微服务引擎使用的elb的id

        :return: The elbid of this EngineCreateReq.
        :rtype: str
        """
        return self._elbid

    @elbid.setter
    def elbid(self, elbid):
        r"""Sets the elbid of this EngineCreateReq.

        微服务引擎使用的elb的id

        :param elbid: The elbid of this EngineCreateReq.
        :type elbid: str
        """
        self._elbid = elbid

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
        if not isinstance(other, EngineCreateReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

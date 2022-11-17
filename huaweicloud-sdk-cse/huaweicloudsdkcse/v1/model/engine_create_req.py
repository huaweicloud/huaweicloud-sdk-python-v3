# coding: utf-8

import re
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
        'network_id': 'str',
        'subnet_cidr': 'str',
        'public_ip_id': 'str',
        'auth_cred': 'EngineRbacPwd',
        'spec_type': 'str',
        'inputs': 'dict(str, str)'
    }

    attribute_map = {
        'name': 'name',
        'description': 'description',
        'payment': 'payment',
        'flavor': 'flavor',
        'az_list': 'azList',
        'auth_type': 'authType',
        'vpc': 'vpc',
        'network_id': 'networkId',
        'subnet_cidr': 'subnetCidr',
        'public_ip_id': 'publicIpId',
        'auth_cred': 'auth_cred',
        'spec_type': 'specType',
        'inputs': 'inputs'
    }

    def __init__(self, name=None, description=None, payment=None, flavor=None, az_list=None, auth_type=None, vpc=None, network_id=None, subnet_cidr=None, public_ip_id=None, auth_cred=None, spec_type=None, inputs=None):
        """EngineCreateReq

        The model defined in huaweicloud sdk

        :param name: 微服务引擎专享版的名称，名称为字母开头，字母、数字、-组成，且不能以-结尾，3-24个字符。
        :type name: str
        :param description: 微服务引擎专享版描述，长度0~255。
        :type description: str
        :param payment: 微服务引擎专享版计费方式，1表示按需
        :type payment: str
        :param flavor: 微服务引擎专享版的规格
        :type flavor: str
        :param az_list: 当前局点可用区列表。
        :type az_list: list[str]
        :param auth_type: 微服务引擎专享版认证方式，RBAC为安全认证，NONE为无认证。
        :type auth_type: str
        :param vpc: vpc名称
        :type vpc: str
        :param network_id: 微服务引擎专享版子网ID
        :type network_id: str
        :param subnet_cidr: 微服务引擎专享版子网划分
        :type subnet_cidr: str
        :param public_ip_id: 微服务引擎专享版公网地址ID，当前为null
        :type public_ip_id: str
        :param auth_cred: 
        :type auth_cred: :class:`huaweicloudsdkcse.v1.EngineRbacPwd`
        :param spec_type: 微服务引擎专享版应用部署类型
        :type spec_type: str
        :param inputs: 引擎附加参数
        :type inputs: dict(str, str)
        """
        
        

        self._name = None
        self._description = None
        self._payment = None
        self._flavor = None
        self._az_list = None
        self._auth_type = None
        self._vpc = None
        self._network_id = None
        self._subnet_cidr = None
        self._public_ip_id = None
        self._auth_cred = None
        self._spec_type = None
        self._inputs = None
        self.discriminator = None

        self.name = name
        if description is not None:
            self.description = description
        self.payment = payment
        self.flavor = flavor
        self.az_list = az_list
        self.auth_type = auth_type
        self.vpc = vpc
        self.network_id = network_id
        self.subnet_cidr = subnet_cidr
        if public_ip_id is not None:
            self.public_ip_id = public_ip_id
        if auth_cred is not None:
            self.auth_cred = auth_cred
        self.spec_type = spec_type
        if inputs is not None:
            self.inputs = inputs

    @property
    def name(self):
        """Gets the name of this EngineCreateReq.

        微服务引擎专享版的名称，名称为字母开头，字母、数字、-组成，且不能以-结尾，3-24个字符。

        :return: The name of this EngineCreateReq.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this EngineCreateReq.

        微服务引擎专享版的名称，名称为字母开头，字母、数字、-组成，且不能以-结尾，3-24个字符。

        :param name: The name of this EngineCreateReq.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        """Gets the description of this EngineCreateReq.

        微服务引擎专享版描述，长度0~255。

        :return: The description of this EngineCreateReq.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this EngineCreateReq.

        微服务引擎专享版描述，长度0~255。

        :param description: The description of this EngineCreateReq.
        :type description: str
        """
        self._description = description

    @property
    def payment(self):
        """Gets the payment of this EngineCreateReq.

        微服务引擎专享版计费方式，1表示按需

        :return: The payment of this EngineCreateReq.
        :rtype: str
        """
        return self._payment

    @payment.setter
    def payment(self, payment):
        """Sets the payment of this EngineCreateReq.

        微服务引擎专享版计费方式，1表示按需

        :param payment: The payment of this EngineCreateReq.
        :type payment: str
        """
        self._payment = payment

    @property
    def flavor(self):
        """Gets the flavor of this EngineCreateReq.

        微服务引擎专享版的规格

        :return: The flavor of this EngineCreateReq.
        :rtype: str
        """
        return self._flavor

    @flavor.setter
    def flavor(self, flavor):
        """Sets the flavor of this EngineCreateReq.

        微服务引擎专享版的规格

        :param flavor: The flavor of this EngineCreateReq.
        :type flavor: str
        """
        self._flavor = flavor

    @property
    def az_list(self):
        """Gets the az_list of this EngineCreateReq.

        当前局点可用区列表。

        :return: The az_list of this EngineCreateReq.
        :rtype: list[str]
        """
        return self._az_list

    @az_list.setter
    def az_list(self, az_list):
        """Sets the az_list of this EngineCreateReq.

        当前局点可用区列表。

        :param az_list: The az_list of this EngineCreateReq.
        :type az_list: list[str]
        """
        self._az_list = az_list

    @property
    def auth_type(self):
        """Gets the auth_type of this EngineCreateReq.

        微服务引擎专享版认证方式，RBAC为安全认证，NONE为无认证。

        :return: The auth_type of this EngineCreateReq.
        :rtype: str
        """
        return self._auth_type

    @auth_type.setter
    def auth_type(self, auth_type):
        """Sets the auth_type of this EngineCreateReq.

        微服务引擎专享版认证方式，RBAC为安全认证，NONE为无认证。

        :param auth_type: The auth_type of this EngineCreateReq.
        :type auth_type: str
        """
        self._auth_type = auth_type

    @property
    def vpc(self):
        """Gets the vpc of this EngineCreateReq.

        vpc名称

        :return: The vpc of this EngineCreateReq.
        :rtype: str
        """
        return self._vpc

    @vpc.setter
    def vpc(self, vpc):
        """Sets the vpc of this EngineCreateReq.

        vpc名称

        :param vpc: The vpc of this EngineCreateReq.
        :type vpc: str
        """
        self._vpc = vpc

    @property
    def network_id(self):
        """Gets the network_id of this EngineCreateReq.

        微服务引擎专享版子网ID

        :return: The network_id of this EngineCreateReq.
        :rtype: str
        """
        return self._network_id

    @network_id.setter
    def network_id(self, network_id):
        """Sets the network_id of this EngineCreateReq.

        微服务引擎专享版子网ID

        :param network_id: The network_id of this EngineCreateReq.
        :type network_id: str
        """
        self._network_id = network_id

    @property
    def subnet_cidr(self):
        """Gets the subnet_cidr of this EngineCreateReq.

        微服务引擎专享版子网划分

        :return: The subnet_cidr of this EngineCreateReq.
        :rtype: str
        """
        return self._subnet_cidr

    @subnet_cidr.setter
    def subnet_cidr(self, subnet_cidr):
        """Sets the subnet_cidr of this EngineCreateReq.

        微服务引擎专享版子网划分

        :param subnet_cidr: The subnet_cidr of this EngineCreateReq.
        :type subnet_cidr: str
        """
        self._subnet_cidr = subnet_cidr

    @property
    def public_ip_id(self):
        """Gets the public_ip_id of this EngineCreateReq.

        微服务引擎专享版公网地址ID，当前为null

        :return: The public_ip_id of this EngineCreateReq.
        :rtype: str
        """
        return self._public_ip_id

    @public_ip_id.setter
    def public_ip_id(self, public_ip_id):
        """Sets the public_ip_id of this EngineCreateReq.

        微服务引擎专享版公网地址ID，当前为null

        :param public_ip_id: The public_ip_id of this EngineCreateReq.
        :type public_ip_id: str
        """
        self._public_ip_id = public_ip_id

    @property
    def auth_cred(self):
        """Gets the auth_cred of this EngineCreateReq.

        :return: The auth_cred of this EngineCreateReq.
        :rtype: :class:`huaweicloudsdkcse.v1.EngineRbacPwd`
        """
        return self._auth_cred

    @auth_cred.setter
    def auth_cred(self, auth_cred):
        """Sets the auth_cred of this EngineCreateReq.

        :param auth_cred: The auth_cred of this EngineCreateReq.
        :type auth_cred: :class:`huaweicloudsdkcse.v1.EngineRbacPwd`
        """
        self._auth_cred = auth_cred

    @property
    def spec_type(self):
        """Gets the spec_type of this EngineCreateReq.

        微服务引擎专享版应用部署类型

        :return: The spec_type of this EngineCreateReq.
        :rtype: str
        """
        return self._spec_type

    @spec_type.setter
    def spec_type(self, spec_type):
        """Sets the spec_type of this EngineCreateReq.

        微服务引擎专享版应用部署类型

        :param spec_type: The spec_type of this EngineCreateReq.
        :type spec_type: str
        """
        self._spec_type = spec_type

    @property
    def inputs(self):
        """Gets the inputs of this EngineCreateReq.

        引擎附加参数

        :return: The inputs of this EngineCreateReq.
        :rtype: dict(str, str)
        """
        return self._inputs

    @inputs.setter
    def inputs(self, inputs):
        """Sets the inputs of this EngineCreateReq.

        引擎附加参数

        :param inputs: The inputs of this EngineCreateReq.
        :type inputs: dict(str, str)
        """
        self._inputs = inputs

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

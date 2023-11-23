# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateNatGatewayOption:

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
        'router_id': 'str',
        'internal_network_id': 'str',
        'description': 'str',
        'spec': 'str',
        'enterprise_project_id': 'str',
        'session_conf': 'SessionConfiguration',
        'ngport_ip_address': 'str'
    }

    attribute_map = {
        'name': 'name',
        'router_id': 'router_id',
        'internal_network_id': 'internal_network_id',
        'description': 'description',
        'spec': 'spec',
        'enterprise_project_id': 'enterprise_project_id',
        'session_conf': 'session_conf',
        'ngport_ip_address': 'ngport_ip_address'
    }

    def __init__(self, name=None, router_id=None, internal_network_id=None, description=None, spec=None, enterprise_project_id=None, session_conf=None, ngport_ip_address=None):
        """CreateNatGatewayOption

        The model defined in huaweicloud sdk

        :param name: 公网NAT网关实例的名字，长度限制为64。 公网NAT网关实例的名字仅支持数字、字母、_（下划线）、-（中划线）、中文。 
        :type name: str
        :param router_id: VPC的id。
        :type router_id: str
        :param internal_network_id: 公网NAT网关下行口（DVR的下一跳）所属的network id。
        :type internal_network_id: str
        :param description: 公网NAT网关实例的描述，长度范围小于等于255个字符，不能包含“&lt;”和“&gt;”。
        :type description: str
        :param spec: 公网NAT网关的规格。 取值为： “1”：小型，SNAT最大连接数10000 “2”：中型，SNAT最大连接数50000 “3”：大型，SNAT最大连接数200000 “4”：超大型，SNAT最大连接数1000000 
        :type spec: str
        :param enterprise_project_id: 企业项目ID 创建公网NAT网关实例时，关联的企业项目ID。 关于企业项目ID的获取及企业项目特性的详细信息，请参考《企业管理用户指南》。
        :type enterprise_project_id: str
        :param session_conf: 
        :type session_conf: :class:`huaweicloudsdknat.v2.SessionConfiguration`
        :param ngport_ip_address: 公网NAT网关私有IP地址，由VPC中子网分配。
        :type ngport_ip_address: str
        """
        
        

        self._name = None
        self._router_id = None
        self._internal_network_id = None
        self._description = None
        self._spec = None
        self._enterprise_project_id = None
        self._session_conf = None
        self._ngport_ip_address = None
        self.discriminator = None

        self.name = name
        self.router_id = router_id
        self.internal_network_id = internal_network_id
        if description is not None:
            self.description = description
        self.spec = spec
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        if session_conf is not None:
            self.session_conf = session_conf
        if ngport_ip_address is not None:
            self.ngport_ip_address = ngport_ip_address

    @property
    def name(self):
        """Gets the name of this CreateNatGatewayOption.

        公网NAT网关实例的名字，长度限制为64。 公网NAT网关实例的名字仅支持数字、字母、_（下划线）、-（中划线）、中文。 

        :return: The name of this CreateNatGatewayOption.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CreateNatGatewayOption.

        公网NAT网关实例的名字，长度限制为64。 公网NAT网关实例的名字仅支持数字、字母、_（下划线）、-（中划线）、中文。 

        :param name: The name of this CreateNatGatewayOption.
        :type name: str
        """
        self._name = name

    @property
    def router_id(self):
        """Gets the router_id of this CreateNatGatewayOption.

        VPC的id。

        :return: The router_id of this CreateNatGatewayOption.
        :rtype: str
        """
        return self._router_id

    @router_id.setter
    def router_id(self, router_id):
        """Sets the router_id of this CreateNatGatewayOption.

        VPC的id。

        :param router_id: The router_id of this CreateNatGatewayOption.
        :type router_id: str
        """
        self._router_id = router_id

    @property
    def internal_network_id(self):
        """Gets the internal_network_id of this CreateNatGatewayOption.

        公网NAT网关下行口（DVR的下一跳）所属的network id。

        :return: The internal_network_id of this CreateNatGatewayOption.
        :rtype: str
        """
        return self._internal_network_id

    @internal_network_id.setter
    def internal_network_id(self, internal_network_id):
        """Sets the internal_network_id of this CreateNatGatewayOption.

        公网NAT网关下行口（DVR的下一跳）所属的network id。

        :param internal_network_id: The internal_network_id of this CreateNatGatewayOption.
        :type internal_network_id: str
        """
        self._internal_network_id = internal_network_id

    @property
    def description(self):
        """Gets the description of this CreateNatGatewayOption.

        公网NAT网关实例的描述，长度范围小于等于255个字符，不能包含“<”和“>”。

        :return: The description of this CreateNatGatewayOption.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this CreateNatGatewayOption.

        公网NAT网关实例的描述，长度范围小于等于255个字符，不能包含“<”和“>”。

        :param description: The description of this CreateNatGatewayOption.
        :type description: str
        """
        self._description = description

    @property
    def spec(self):
        """Gets the spec of this CreateNatGatewayOption.

        公网NAT网关的规格。 取值为： “1”：小型，SNAT最大连接数10000 “2”：中型，SNAT最大连接数50000 “3”：大型，SNAT最大连接数200000 “4”：超大型，SNAT最大连接数1000000 

        :return: The spec of this CreateNatGatewayOption.
        :rtype: str
        """
        return self._spec

    @spec.setter
    def spec(self, spec):
        """Sets the spec of this CreateNatGatewayOption.

        公网NAT网关的规格。 取值为： “1”：小型，SNAT最大连接数10000 “2”：中型，SNAT最大连接数50000 “3”：大型，SNAT最大连接数200000 “4”：超大型，SNAT最大连接数1000000 

        :param spec: The spec of this CreateNatGatewayOption.
        :type spec: str
        """
        self._spec = spec

    @property
    def enterprise_project_id(self):
        """Gets the enterprise_project_id of this CreateNatGatewayOption.

        企业项目ID 创建公网NAT网关实例时，关联的企业项目ID。 关于企业项目ID的获取及企业项目特性的详细信息，请参考《企业管理用户指南》。

        :return: The enterprise_project_id of this CreateNatGatewayOption.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        """Sets the enterprise_project_id of this CreateNatGatewayOption.

        企业项目ID 创建公网NAT网关实例时，关联的企业项目ID。 关于企业项目ID的获取及企业项目特性的详细信息，请参考《企业管理用户指南》。

        :param enterprise_project_id: The enterprise_project_id of this CreateNatGatewayOption.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def session_conf(self):
        """Gets the session_conf of this CreateNatGatewayOption.

        :return: The session_conf of this CreateNatGatewayOption.
        :rtype: :class:`huaweicloudsdknat.v2.SessionConfiguration`
        """
        return self._session_conf

    @session_conf.setter
    def session_conf(self, session_conf):
        """Sets the session_conf of this CreateNatGatewayOption.

        :param session_conf: The session_conf of this CreateNatGatewayOption.
        :type session_conf: :class:`huaweicloudsdknat.v2.SessionConfiguration`
        """
        self._session_conf = session_conf

    @property
    def ngport_ip_address(self):
        """Gets the ngport_ip_address of this CreateNatGatewayOption.

        公网NAT网关私有IP地址，由VPC中子网分配。

        :return: The ngport_ip_address of this CreateNatGatewayOption.
        :rtype: str
        """
        return self._ngport_ip_address

    @ngport_ip_address.setter
    def ngport_ip_address(self, ngport_ip_address):
        """Sets the ngport_ip_address of this CreateNatGatewayOption.

        公网NAT网关私有IP地址，由VPC中子网分配。

        :param ngport_ip_address: The ngport_ip_address of this CreateNatGatewayOption.
        :type ngport_ip_address: str
        """
        self._ngport_ip_address = ngport_ip_address

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
        if not isinstance(other, CreateNatGatewayOption):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

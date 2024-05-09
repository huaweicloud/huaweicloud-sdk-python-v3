# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ChangeVpcNicBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'port_id': 'str',
        'subnet_id': 'str',
        'security_groups': 'ChangeVpcSecurityGroups',
        'ip_address': 'str'
    }

    attribute_map = {
        'port_id': 'port_id',
        'subnet_id': 'subnet_id',
        'security_groups': 'security_groups',
        'ip_address': 'ip_address'
    }

    def __init__(self, port_id=None, subnet_id=None, security_groups=None, ip_address=None):
        """ChangeVpcNicBody

        The model defined in huaweicloud sdk

        :param port_id: 网卡ID，UUID格式。 当该字段不为空时，表示挂载指定的网卡。port_id和subnet_id不能同时为空。 网卡ID可以从虚拟私有云的“查询端口列表”章节查询到。 约束： 网卡必须带有安全组。 网卡状态必须为DOWN。 网卡的vpcid必须和传入的vpcid一致。 当port_id和subnet_id同时存在的时候，优先使用port_id。当选择port_id不为空时，代表此时使用的是弹性网卡，此时security_groups和ip_address等参数不生效。
        :type port_id: str
        :param subnet_id: 云服务器云主机添加网卡的信息。 需要指定云服务器云主机所属虚拟私有云下已创建的网络（network）的ID，UUID格式。
        :type subnet_id: str
        :param security_groups: 
        :type security_groups: :class:`huaweicloudsdkecs.v2.ChangeVpcSecurityGroups`
        :param ip_address: P地址，无该参数表示自动分配IP地址
        :type ip_address: str
        """
        
        

        self._port_id = None
        self._subnet_id = None
        self._security_groups = None
        self._ip_address = None
        self.discriminator = None

        if port_id is not None:
            self.port_id = port_id
        if subnet_id is not None:
            self.subnet_id = subnet_id
        if security_groups is not None:
            self.security_groups = security_groups
        if ip_address is not None:
            self.ip_address = ip_address

    @property
    def port_id(self):
        """Gets the port_id of this ChangeVpcNicBody.

        网卡ID，UUID格式。 当该字段不为空时，表示挂载指定的网卡。port_id和subnet_id不能同时为空。 网卡ID可以从虚拟私有云的“查询端口列表”章节查询到。 约束： 网卡必须带有安全组。 网卡状态必须为DOWN。 网卡的vpcid必须和传入的vpcid一致。 当port_id和subnet_id同时存在的时候，优先使用port_id。当选择port_id不为空时，代表此时使用的是弹性网卡，此时security_groups和ip_address等参数不生效。

        :return: The port_id of this ChangeVpcNicBody.
        :rtype: str
        """
        return self._port_id

    @port_id.setter
    def port_id(self, port_id):
        """Sets the port_id of this ChangeVpcNicBody.

        网卡ID，UUID格式。 当该字段不为空时，表示挂载指定的网卡。port_id和subnet_id不能同时为空。 网卡ID可以从虚拟私有云的“查询端口列表”章节查询到。 约束： 网卡必须带有安全组。 网卡状态必须为DOWN。 网卡的vpcid必须和传入的vpcid一致。 当port_id和subnet_id同时存在的时候，优先使用port_id。当选择port_id不为空时，代表此时使用的是弹性网卡，此时security_groups和ip_address等参数不生效。

        :param port_id: The port_id of this ChangeVpcNicBody.
        :type port_id: str
        """
        self._port_id = port_id

    @property
    def subnet_id(self):
        """Gets the subnet_id of this ChangeVpcNicBody.

        云服务器云主机添加网卡的信息。 需要指定云服务器云主机所属虚拟私有云下已创建的网络（network）的ID，UUID格式。

        :return: The subnet_id of this ChangeVpcNicBody.
        :rtype: str
        """
        return self._subnet_id

    @subnet_id.setter
    def subnet_id(self, subnet_id):
        """Sets the subnet_id of this ChangeVpcNicBody.

        云服务器云主机添加网卡的信息。 需要指定云服务器云主机所属虚拟私有云下已创建的网络（network）的ID，UUID格式。

        :param subnet_id: The subnet_id of this ChangeVpcNicBody.
        :type subnet_id: str
        """
        self._subnet_id = subnet_id

    @property
    def security_groups(self):
        """Gets the security_groups of this ChangeVpcNicBody.

        :return: The security_groups of this ChangeVpcNicBody.
        :rtype: :class:`huaweicloudsdkecs.v2.ChangeVpcSecurityGroups`
        """
        return self._security_groups

    @security_groups.setter
    def security_groups(self, security_groups):
        """Sets the security_groups of this ChangeVpcNicBody.

        :param security_groups: The security_groups of this ChangeVpcNicBody.
        :type security_groups: :class:`huaweicloudsdkecs.v2.ChangeVpcSecurityGroups`
        """
        self._security_groups = security_groups

    @property
    def ip_address(self):
        """Gets the ip_address of this ChangeVpcNicBody.

        P地址，无该参数表示自动分配IP地址

        :return: The ip_address of this ChangeVpcNicBody.
        :rtype: str
        """
        return self._ip_address

    @ip_address.setter
    def ip_address(self, ip_address):
        """Sets the ip_address of this ChangeVpcNicBody.

        P地址，无该参数表示自动分配IP地址

        :param ip_address: The ip_address of this ChangeVpcNicBody.
        :type ip_address: str
        """
        self._ip_address = ip_address

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
        if not isinstance(other, ChangeVpcNicBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

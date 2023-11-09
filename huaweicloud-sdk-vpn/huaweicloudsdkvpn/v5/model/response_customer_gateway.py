# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ResponseCustomerGateway:

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
        'route_mode': 'str',
        'bgp_asn': 'int',
        'ip': 'str',
        'ca_certificate': 'CaCertificate',
        'created_at': 'datetime',
        'updated_at': 'datetime'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'route_mode': 'route_mode',
        'bgp_asn': 'bgp_asn',
        'ip': 'ip',
        'ca_certificate': 'ca_certificate',
        'created_at': 'created_at',
        'updated_at': 'updated_at'
    }

    def __init__(self, id=None, name=None, route_mode=None, bgp_asn=None, ip=None, ca_certificate=None, created_at=None, updated_at=None):
        """ResponseCustomerGateway

        The model defined in huaweicloud sdk

        :param id: 网关的ID
        :type id: str
        :param name: 网关名称
        :type name: str
        :param route_mode: 网关路由模式
        :type route_mode: str
        :param bgp_asn: 网关的bgp asn号
        :type bgp_asn: int
        :param ip: 网关ip地址
        :type ip: str
        :param ca_certificate: 
        :type ca_certificate: :class:`huaweicloudsdkvpn.v5.CaCertificate`
        :param created_at: 创建时间
        :type created_at: datetime
        :param updated_at: 更新时间
        :type updated_at: datetime
        """
        
        

        self._id = None
        self._name = None
        self._route_mode = None
        self._bgp_asn = None
        self._ip = None
        self._ca_certificate = None
        self._created_at = None
        self._updated_at = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if route_mode is not None:
            self.route_mode = route_mode
        if bgp_asn is not None:
            self.bgp_asn = bgp_asn
        if ip is not None:
            self.ip = ip
        if ca_certificate is not None:
            self.ca_certificate = ca_certificate
        if created_at is not None:
            self.created_at = created_at
        if updated_at is not None:
            self.updated_at = updated_at

    @property
    def id(self):
        """Gets the id of this ResponseCustomerGateway.

        网关的ID

        :return: The id of this ResponseCustomerGateway.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ResponseCustomerGateway.

        网关的ID

        :param id: The id of this ResponseCustomerGateway.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        """Gets the name of this ResponseCustomerGateway.

        网关名称

        :return: The name of this ResponseCustomerGateway.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ResponseCustomerGateway.

        网关名称

        :param name: The name of this ResponseCustomerGateway.
        :type name: str
        """
        self._name = name

    @property
    def route_mode(self):
        """Gets the route_mode of this ResponseCustomerGateway.

        网关路由模式

        :return: The route_mode of this ResponseCustomerGateway.
        :rtype: str
        """
        return self._route_mode

    @route_mode.setter
    def route_mode(self, route_mode):
        """Sets the route_mode of this ResponseCustomerGateway.

        网关路由模式

        :param route_mode: The route_mode of this ResponseCustomerGateway.
        :type route_mode: str
        """
        self._route_mode = route_mode

    @property
    def bgp_asn(self):
        """Gets the bgp_asn of this ResponseCustomerGateway.

        网关的bgp asn号

        :return: The bgp_asn of this ResponseCustomerGateway.
        :rtype: int
        """
        return self._bgp_asn

    @bgp_asn.setter
    def bgp_asn(self, bgp_asn):
        """Sets the bgp_asn of this ResponseCustomerGateway.

        网关的bgp asn号

        :param bgp_asn: The bgp_asn of this ResponseCustomerGateway.
        :type bgp_asn: int
        """
        self._bgp_asn = bgp_asn

    @property
    def ip(self):
        """Gets the ip of this ResponseCustomerGateway.

        网关ip地址

        :return: The ip of this ResponseCustomerGateway.
        :rtype: str
        """
        return self._ip

    @ip.setter
    def ip(self, ip):
        """Sets the ip of this ResponseCustomerGateway.

        网关ip地址

        :param ip: The ip of this ResponseCustomerGateway.
        :type ip: str
        """
        self._ip = ip

    @property
    def ca_certificate(self):
        """Gets the ca_certificate of this ResponseCustomerGateway.

        :return: The ca_certificate of this ResponseCustomerGateway.
        :rtype: :class:`huaweicloudsdkvpn.v5.CaCertificate`
        """
        return self._ca_certificate

    @ca_certificate.setter
    def ca_certificate(self, ca_certificate):
        """Sets the ca_certificate of this ResponseCustomerGateway.

        :param ca_certificate: The ca_certificate of this ResponseCustomerGateway.
        :type ca_certificate: :class:`huaweicloudsdkvpn.v5.CaCertificate`
        """
        self._ca_certificate = ca_certificate

    @property
    def created_at(self):
        """Gets the created_at of this ResponseCustomerGateway.

        创建时间

        :return: The created_at of this ResponseCustomerGateway.
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this ResponseCustomerGateway.

        创建时间

        :param created_at: The created_at of this ResponseCustomerGateway.
        :type created_at: datetime
        """
        self._created_at = created_at

    @property
    def updated_at(self):
        """Gets the updated_at of this ResponseCustomerGateway.

        更新时间

        :return: The updated_at of this ResponseCustomerGateway.
        :rtype: datetime
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this ResponseCustomerGateway.

        更新时间

        :param updated_at: The updated_at of this ResponseCustomerGateway.
        :type updated_at: datetime
        """
        self._updated_at = updated_at

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
        if not isinstance(other, ResponseCustomerGateway):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

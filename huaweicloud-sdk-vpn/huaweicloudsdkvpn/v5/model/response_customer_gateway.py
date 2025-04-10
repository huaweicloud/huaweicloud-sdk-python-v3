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
        'bgp_asn': 'int',
        'id_type': 'str',
        'id_value': 'str',
        'ca_certificate': 'CaCertificate',
        'created_at': 'datetime',
        'updated_at': 'datetime',
        'tags': 'list[VpnResourceTag]'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'bgp_asn': 'bgp_asn',
        'id_type': 'id_type',
        'id_value': 'id_value',
        'ca_certificate': 'ca_certificate',
        'created_at': 'created_at',
        'updated_at': 'updated_at',
        'tags': 'tags'
    }

    def __init__(self, id=None, name=None, bgp_asn=None, id_type=None, id_value=None, ca_certificate=None, created_at=None, updated_at=None, tags=None):
        r"""ResponseCustomerGateway

        The model defined in huaweicloud sdk

        :param id: 网关的ID
        :type id: str
        :param name: 网关名称
        :type name: str
        :param bgp_asn: 网关的bgp asn号
        :type bgp_asn: int
        :param id_type: 对端网关标识类型
        :type id_type: str
        :param id_value: 对端网关标识值
        :type id_value: str
        :param ca_certificate: 
        :type ca_certificate: :class:`huaweicloudsdkvpn.v5.CaCertificate`
        :param created_at: 创建时间
        :type created_at: datetime
        :param updated_at: 更新时间
        :type updated_at: datetime
        :param tags: 标签
        :type tags: list[:class:`huaweicloudsdkvpn.v5.VpnResourceTag`]
        """
        
        

        self._id = None
        self._name = None
        self._bgp_asn = None
        self._id_type = None
        self._id_value = None
        self._ca_certificate = None
        self._created_at = None
        self._updated_at = None
        self._tags = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if bgp_asn is not None:
            self.bgp_asn = bgp_asn
        if id_type is not None:
            self.id_type = id_type
        if id_value is not None:
            self.id_value = id_value
        if ca_certificate is not None:
            self.ca_certificate = ca_certificate
        if created_at is not None:
            self.created_at = created_at
        if updated_at is not None:
            self.updated_at = updated_at
        if tags is not None:
            self.tags = tags

    @property
    def id(self):
        r"""Gets the id of this ResponseCustomerGateway.

        网关的ID

        :return: The id of this ResponseCustomerGateway.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this ResponseCustomerGateway.

        网关的ID

        :param id: The id of this ResponseCustomerGateway.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        r"""Gets the name of this ResponseCustomerGateway.

        网关名称

        :return: The name of this ResponseCustomerGateway.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this ResponseCustomerGateway.

        网关名称

        :param name: The name of this ResponseCustomerGateway.
        :type name: str
        """
        self._name = name

    @property
    def bgp_asn(self):
        r"""Gets the bgp_asn of this ResponseCustomerGateway.

        网关的bgp asn号

        :return: The bgp_asn of this ResponseCustomerGateway.
        :rtype: int
        """
        return self._bgp_asn

    @bgp_asn.setter
    def bgp_asn(self, bgp_asn):
        r"""Sets the bgp_asn of this ResponseCustomerGateway.

        网关的bgp asn号

        :param bgp_asn: The bgp_asn of this ResponseCustomerGateway.
        :type bgp_asn: int
        """
        self._bgp_asn = bgp_asn

    @property
    def id_type(self):
        r"""Gets the id_type of this ResponseCustomerGateway.

        对端网关标识类型

        :return: The id_type of this ResponseCustomerGateway.
        :rtype: str
        """
        return self._id_type

    @id_type.setter
    def id_type(self, id_type):
        r"""Sets the id_type of this ResponseCustomerGateway.

        对端网关标识类型

        :param id_type: The id_type of this ResponseCustomerGateway.
        :type id_type: str
        """
        self._id_type = id_type

    @property
    def id_value(self):
        r"""Gets the id_value of this ResponseCustomerGateway.

        对端网关标识值

        :return: The id_value of this ResponseCustomerGateway.
        :rtype: str
        """
        return self._id_value

    @id_value.setter
    def id_value(self, id_value):
        r"""Sets the id_value of this ResponseCustomerGateway.

        对端网关标识值

        :param id_value: The id_value of this ResponseCustomerGateway.
        :type id_value: str
        """
        self._id_value = id_value

    @property
    def ca_certificate(self):
        r"""Gets the ca_certificate of this ResponseCustomerGateway.

        :return: The ca_certificate of this ResponseCustomerGateway.
        :rtype: :class:`huaweicloudsdkvpn.v5.CaCertificate`
        """
        return self._ca_certificate

    @ca_certificate.setter
    def ca_certificate(self, ca_certificate):
        r"""Sets the ca_certificate of this ResponseCustomerGateway.

        :param ca_certificate: The ca_certificate of this ResponseCustomerGateway.
        :type ca_certificate: :class:`huaweicloudsdkvpn.v5.CaCertificate`
        """
        self._ca_certificate = ca_certificate

    @property
    def created_at(self):
        r"""Gets the created_at of this ResponseCustomerGateway.

        创建时间

        :return: The created_at of this ResponseCustomerGateway.
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        r"""Sets the created_at of this ResponseCustomerGateway.

        创建时间

        :param created_at: The created_at of this ResponseCustomerGateway.
        :type created_at: datetime
        """
        self._created_at = created_at

    @property
    def updated_at(self):
        r"""Gets the updated_at of this ResponseCustomerGateway.

        更新时间

        :return: The updated_at of this ResponseCustomerGateway.
        :rtype: datetime
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        r"""Sets the updated_at of this ResponseCustomerGateway.

        更新时间

        :param updated_at: The updated_at of this ResponseCustomerGateway.
        :type updated_at: datetime
        """
        self._updated_at = updated_at

    @property
    def tags(self):
        r"""Gets the tags of this ResponseCustomerGateway.

        标签

        :return: The tags of this ResponseCustomerGateway.
        :rtype: list[:class:`huaweicloudsdkvpn.v5.VpnResourceTag`]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        r"""Sets the tags of this ResponseCustomerGateway.

        标签

        :param tags: The tags of this ResponseCustomerGateway.
        :type tags: list[:class:`huaweicloudsdkvpn.v5.VpnResourceTag`]
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
        if not isinstance(other, ResponseCustomerGateway):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

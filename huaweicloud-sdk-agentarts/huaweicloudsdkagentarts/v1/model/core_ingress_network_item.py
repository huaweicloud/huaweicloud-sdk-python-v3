# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CoreIngressNetworkItem:

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
        'status': 'str',
        'subnet_id': 'str',
        'ip_address': 'str',
        'created_at': 'datetime',
        'updated_at': 'datetime',
        'default_private_zone_domain_name': 'str'
    }

    attribute_map = {
        'id': 'id',
        'status': 'status',
        'subnet_id': 'subnet_id',
        'ip_address': 'ip_address',
        'created_at': 'created_at',
        'updated_at': 'updated_at',
        'default_private_zone_domain_name': 'default_private_zone_domain_name'
    }

    def __init__(self, id=None, status=None, subnet_id=None, ip_address=None, created_at=None, updated_at=None, default_private_zone_domain_name=None):
        r"""CoreIngressNetworkItem

        The model defined in huaweicloud sdk

        :param id: **参数解释**: 入站网络ID。
        :type id: str
        :param status: **参数解释**: 入站网络状态。
        :type status: str
        :param subnet_id: **参数解释**: VPC子网ID。
        :type subnet_id: str
        :param ip_address: **参数解释**: 分配的IP地址。
        :type ip_address: str
        :param created_at: **参数解释**: 资源创建时间。
        :type created_at: datetime
        :param updated_at: **参数解释**: 资源最后更新时间。
        :type updated_at: datetime
        :param default_private_zone_domain_name: **参数解释**: 默认私网域名。
        :type default_private_zone_domain_name: str
        """
        
        

        self._id = None
        self._status = None
        self._subnet_id = None
        self._ip_address = None
        self._created_at = None
        self._updated_at = None
        self._default_private_zone_domain_name = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if status is not None:
            self.status = status
        if subnet_id is not None:
            self.subnet_id = subnet_id
        if ip_address is not None:
            self.ip_address = ip_address
        if created_at is not None:
            self.created_at = created_at
        if updated_at is not None:
            self.updated_at = updated_at
        if default_private_zone_domain_name is not None:
            self.default_private_zone_domain_name = default_private_zone_domain_name

    @property
    def id(self):
        r"""Gets the id of this CoreIngressNetworkItem.

        **参数解释**: 入站网络ID。

        :return: The id of this CoreIngressNetworkItem.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this CoreIngressNetworkItem.

        **参数解释**: 入站网络ID。

        :param id: The id of this CoreIngressNetworkItem.
        :type id: str
        """
        self._id = id

    @property
    def status(self):
        r"""Gets the status of this CoreIngressNetworkItem.

        **参数解释**: 入站网络状态。

        :return: The status of this CoreIngressNetworkItem.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this CoreIngressNetworkItem.

        **参数解释**: 入站网络状态。

        :param status: The status of this CoreIngressNetworkItem.
        :type status: str
        """
        self._status = status

    @property
    def subnet_id(self):
        r"""Gets the subnet_id of this CoreIngressNetworkItem.

        **参数解释**: VPC子网ID。

        :return: The subnet_id of this CoreIngressNetworkItem.
        :rtype: str
        """
        return self._subnet_id

    @subnet_id.setter
    def subnet_id(self, subnet_id):
        r"""Sets the subnet_id of this CoreIngressNetworkItem.

        **参数解释**: VPC子网ID。

        :param subnet_id: The subnet_id of this CoreIngressNetworkItem.
        :type subnet_id: str
        """
        self._subnet_id = subnet_id

    @property
    def ip_address(self):
        r"""Gets the ip_address of this CoreIngressNetworkItem.

        **参数解释**: 分配的IP地址。

        :return: The ip_address of this CoreIngressNetworkItem.
        :rtype: str
        """
        return self._ip_address

    @ip_address.setter
    def ip_address(self, ip_address):
        r"""Sets the ip_address of this CoreIngressNetworkItem.

        **参数解释**: 分配的IP地址。

        :param ip_address: The ip_address of this CoreIngressNetworkItem.
        :type ip_address: str
        """
        self._ip_address = ip_address

    @property
    def created_at(self):
        r"""Gets the created_at of this CoreIngressNetworkItem.

        **参数解释**: 资源创建时间。

        :return: The created_at of this CoreIngressNetworkItem.
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        r"""Sets the created_at of this CoreIngressNetworkItem.

        **参数解释**: 资源创建时间。

        :param created_at: The created_at of this CoreIngressNetworkItem.
        :type created_at: datetime
        """
        self._created_at = created_at

    @property
    def updated_at(self):
        r"""Gets the updated_at of this CoreIngressNetworkItem.

        **参数解释**: 资源最后更新时间。

        :return: The updated_at of this CoreIngressNetworkItem.
        :rtype: datetime
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        r"""Sets the updated_at of this CoreIngressNetworkItem.

        **参数解释**: 资源最后更新时间。

        :param updated_at: The updated_at of this CoreIngressNetworkItem.
        :type updated_at: datetime
        """
        self._updated_at = updated_at

    @property
    def default_private_zone_domain_name(self):
        r"""Gets the default_private_zone_domain_name of this CoreIngressNetworkItem.

        **参数解释**: 默认私网域名。

        :return: The default_private_zone_domain_name of this CoreIngressNetworkItem.
        :rtype: str
        """
        return self._default_private_zone_domain_name

    @default_private_zone_domain_name.setter
    def default_private_zone_domain_name(self, default_private_zone_domain_name):
        r"""Sets the default_private_zone_domain_name of this CoreIngressNetworkItem.

        **参数解释**: 默认私网域名。

        :param default_private_zone_domain_name: The default_private_zone_domain_name of this CoreIngressNetworkItem.
        :type default_private_zone_domain_name: str
        """
        self._default_private_zone_domain_name = default_private_zone_domain_name

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
        if not isinstance(other, CoreIngressNetworkItem):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

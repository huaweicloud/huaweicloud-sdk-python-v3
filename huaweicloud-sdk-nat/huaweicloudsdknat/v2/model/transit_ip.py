# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class TransitIp:

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
        'project_id': 'str',
        'network_interface_id': 'str',
        'ip_address': 'str',
        'created_at': 'datetime',
        'updated_at': 'datetime',
        'virsubnet_id': 'str',
        'tags': 'list[PrivateTag]',
        'gateway_id': 'str',
        'enterprise_project_id': 'str'
    }

    attribute_map = {
        'id': 'id',
        'project_id': 'project_id',
        'network_interface_id': 'network_interface_id',
        'ip_address': 'ip_address',
        'created_at': 'created_at',
        'updated_at': 'updated_at',
        'virsubnet_id': 'virsubnet_id',
        'tags': 'tags',
        'gateway_id': 'gateway_id',
        'enterprise_project_id': 'enterprise_project_id'
    }

    def __init__(self, id=None, project_id=None, network_interface_id=None, ip_address=None, created_at=None, updated_at=None, virsubnet_id=None, tags=None, gateway_id=None, enterprise_project_id=None):
        """TransitIp

        The model defined in huaweicloud sdk

        :param id: 中转IP的ID。
        :type id: str
        :param project_id: 项目的ID。
        :type project_id: str
        :param network_interface_id: 中转IP的网络接口ID。
        :type network_interface_id: str
        :param ip_address: 中转IP的地址。
        :type ip_address: str
        :param created_at: 中转IP的创建时间，遵循UTC时间，格式是yyyy-mm-ddThh:mm:ssZ
        :type created_at: datetime
        :param updated_at: 中转IP的更新时间，遵循UTC时间，格式是yyyy-mm-ddThh:mm:ssZ
        :type updated_at: datetime
        :param virsubnet_id: 当前租户子网的ID。
        :type virsubnet_id: str
        :param tags: 标签列表。
        :type tags: list[:class:`huaweicloudsdknat.v2.PrivateTag`]
        :param gateway_id: 中转IP绑定的私网NAT网关实例的ID。
        :type gateway_id: str
        :param enterprise_project_id: 企业项目ID。创建中转IP时，关联的企业项目ID。
        :type enterprise_project_id: str
        """
        
        

        self._id = None
        self._project_id = None
        self._network_interface_id = None
        self._ip_address = None
        self._created_at = None
        self._updated_at = None
        self._virsubnet_id = None
        self._tags = None
        self._gateway_id = None
        self._enterprise_project_id = None
        self.discriminator = None

        self.id = id
        self.project_id = project_id
        self.network_interface_id = network_interface_id
        self.ip_address = ip_address
        self.created_at = created_at
        self.updated_at = updated_at
        if virsubnet_id is not None:
            self.virsubnet_id = virsubnet_id
        if tags is not None:
            self.tags = tags
        self.gateway_id = gateway_id
        self.enterprise_project_id = enterprise_project_id

    @property
    def id(self):
        """Gets the id of this TransitIp.

        中转IP的ID。

        :return: The id of this TransitIp.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this TransitIp.

        中转IP的ID。

        :param id: The id of this TransitIp.
        :type id: str
        """
        self._id = id

    @property
    def project_id(self):
        """Gets the project_id of this TransitIp.

        项目的ID。

        :return: The project_id of this TransitIp.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """Sets the project_id of this TransitIp.

        项目的ID。

        :param project_id: The project_id of this TransitIp.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def network_interface_id(self):
        """Gets the network_interface_id of this TransitIp.

        中转IP的网络接口ID。

        :return: The network_interface_id of this TransitIp.
        :rtype: str
        """
        return self._network_interface_id

    @network_interface_id.setter
    def network_interface_id(self, network_interface_id):
        """Sets the network_interface_id of this TransitIp.

        中转IP的网络接口ID。

        :param network_interface_id: The network_interface_id of this TransitIp.
        :type network_interface_id: str
        """
        self._network_interface_id = network_interface_id

    @property
    def ip_address(self):
        """Gets the ip_address of this TransitIp.

        中转IP的地址。

        :return: The ip_address of this TransitIp.
        :rtype: str
        """
        return self._ip_address

    @ip_address.setter
    def ip_address(self, ip_address):
        """Sets the ip_address of this TransitIp.

        中转IP的地址。

        :param ip_address: The ip_address of this TransitIp.
        :type ip_address: str
        """
        self._ip_address = ip_address

    @property
    def created_at(self):
        """Gets the created_at of this TransitIp.

        中转IP的创建时间，遵循UTC时间，格式是yyyy-mm-ddThh:mm:ssZ

        :return: The created_at of this TransitIp.
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this TransitIp.

        中转IP的创建时间，遵循UTC时间，格式是yyyy-mm-ddThh:mm:ssZ

        :param created_at: The created_at of this TransitIp.
        :type created_at: datetime
        """
        self._created_at = created_at

    @property
    def updated_at(self):
        """Gets the updated_at of this TransitIp.

        中转IP的更新时间，遵循UTC时间，格式是yyyy-mm-ddThh:mm:ssZ

        :return: The updated_at of this TransitIp.
        :rtype: datetime
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this TransitIp.

        中转IP的更新时间，遵循UTC时间，格式是yyyy-mm-ddThh:mm:ssZ

        :param updated_at: The updated_at of this TransitIp.
        :type updated_at: datetime
        """
        self._updated_at = updated_at

    @property
    def virsubnet_id(self):
        """Gets the virsubnet_id of this TransitIp.

        当前租户子网的ID。

        :return: The virsubnet_id of this TransitIp.
        :rtype: str
        """
        return self._virsubnet_id

    @virsubnet_id.setter
    def virsubnet_id(self, virsubnet_id):
        """Sets the virsubnet_id of this TransitIp.

        当前租户子网的ID。

        :param virsubnet_id: The virsubnet_id of this TransitIp.
        :type virsubnet_id: str
        """
        self._virsubnet_id = virsubnet_id

    @property
    def tags(self):
        """Gets the tags of this TransitIp.

        标签列表。

        :return: The tags of this TransitIp.
        :rtype: list[:class:`huaweicloudsdknat.v2.PrivateTag`]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this TransitIp.

        标签列表。

        :param tags: The tags of this TransitIp.
        :type tags: list[:class:`huaweicloudsdknat.v2.PrivateTag`]
        """
        self._tags = tags

    @property
    def gateway_id(self):
        """Gets the gateway_id of this TransitIp.

        中转IP绑定的私网NAT网关实例的ID。

        :return: The gateway_id of this TransitIp.
        :rtype: str
        """
        return self._gateway_id

    @gateway_id.setter
    def gateway_id(self, gateway_id):
        """Sets the gateway_id of this TransitIp.

        中转IP绑定的私网NAT网关实例的ID。

        :param gateway_id: The gateway_id of this TransitIp.
        :type gateway_id: str
        """
        self._gateway_id = gateway_id

    @property
    def enterprise_project_id(self):
        """Gets the enterprise_project_id of this TransitIp.

        企业项目ID。创建中转IP时，关联的企业项目ID。

        :return: The enterprise_project_id of this TransitIp.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        """Sets the enterprise_project_id of this TransitIp.

        企业项目ID。创建中转IP时，关联的企业项目ID。

        :param enterprise_project_id: The enterprise_project_id of this TransitIp.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

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
        if not isinstance(other, TransitIp):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

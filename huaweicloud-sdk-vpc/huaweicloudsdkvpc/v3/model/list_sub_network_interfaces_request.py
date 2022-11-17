# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListSubNetworkInterfacesRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'limit': 'int',
        'marker': 'str',
        'id': 'list[str]',
        'virsubnet_id': 'list[str]',
        'private_ip_address': 'list[str]',
        'mac_address': 'list[str]',
        'vpc_id': 'list[str]',
        'description': 'list[str]',
        'parent_id': 'list[str]'
    }

    attribute_map = {
        'limit': 'limit',
        'marker': 'marker',
        'id': 'id',
        'virsubnet_id': 'virsubnet_id',
        'private_ip_address': 'private_ip_address',
        'mac_address': 'mac_address',
        'vpc_id': 'vpc_id',
        'description': 'description',
        'parent_id': 'parent_id'
    }

    def __init__(self, limit=None, marker=None, id=None, virsubnet_id=None, private_ip_address=None, mac_address=None, vpc_id=None, description=None, parent_id=None):
        """ListSubNetworkInterfacesRequest

        The model defined in huaweicloud sdk

        :param limit: 功能说明：每页返回的个数 取值范围：0-2000
        :type limit: int
        :param marker: 分页查询起始的资源ID，为空时查询第一页
        :type marker: str
        :param id: 功能说明：辅助弹性网卡ID，支持多ID过滤 使用场景：查询需要的多个辅助弹性网卡信息
        :type id: list[str]
        :param virsubnet_id: 功能说明：辅助弹性网卡所属虚拟子网的ID，支持多个ID过滤 使用场景：过滤需要的单个或者多个虚拟子网下的辅助弹性网卡
        :type virsubnet_id: list[str]
        :param private_ip_address: 功能说明：辅助弹性网卡的私有IPv4地址，支持多个地址同时过滤 使用场景：通过单个或者多个ip地址过滤查询辅助弹性网卡
        :type private_ip_address: list[str]
        :param mac_address: 功能说明：辅助弹性网卡的mac地址，支持多个同时过滤 使用场景：使用mac地址精确过滤辅助弹性网卡
        :type mac_address: list[str]
        :param vpc_id: 功能说明：辅助弹性网卡所属的VPC_ID，支持多ID过滤 使用场景：过滤单个或多个VPC下的辅助弹性网卡信息
        :type vpc_id: list[str]
        :param description: 功能说明：辅助弹性网卡的描述信息，支持多个同时过滤 使用场景：通过描述信息过滤辅助弹性网卡
        :type description: list[str]
        :param parent_id: 功能说明：辅助弹性网卡的宿主网卡的ID，支持多ID过滤 使用场景：过滤单个或多个宿主网卡下存在的辅助弹性网卡
        :type parent_id: list[str]
        """
        
        

        self._limit = None
        self._marker = None
        self._id = None
        self._virsubnet_id = None
        self._private_ip_address = None
        self._mac_address = None
        self._vpc_id = None
        self._description = None
        self._parent_id = None
        self.discriminator = None

        if limit is not None:
            self.limit = limit
        if marker is not None:
            self.marker = marker
        if id is not None:
            self.id = id
        if virsubnet_id is not None:
            self.virsubnet_id = virsubnet_id
        if private_ip_address is not None:
            self.private_ip_address = private_ip_address
        if mac_address is not None:
            self.mac_address = mac_address
        if vpc_id is not None:
            self.vpc_id = vpc_id
        if description is not None:
            self.description = description
        if parent_id is not None:
            self.parent_id = parent_id

    @property
    def limit(self):
        """Gets the limit of this ListSubNetworkInterfacesRequest.

        功能说明：每页返回的个数 取值范围：0-2000

        :return: The limit of this ListSubNetworkInterfacesRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListSubNetworkInterfacesRequest.

        功能说明：每页返回的个数 取值范围：0-2000

        :param limit: The limit of this ListSubNetworkInterfacesRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def marker(self):
        """Gets the marker of this ListSubNetworkInterfacesRequest.

        分页查询起始的资源ID，为空时查询第一页

        :return: The marker of this ListSubNetworkInterfacesRequest.
        :rtype: str
        """
        return self._marker

    @marker.setter
    def marker(self, marker):
        """Sets the marker of this ListSubNetworkInterfacesRequest.

        分页查询起始的资源ID，为空时查询第一页

        :param marker: The marker of this ListSubNetworkInterfacesRequest.
        :type marker: str
        """
        self._marker = marker

    @property
    def id(self):
        """Gets the id of this ListSubNetworkInterfacesRequest.

        功能说明：辅助弹性网卡ID，支持多ID过滤 使用场景：查询需要的多个辅助弹性网卡信息

        :return: The id of this ListSubNetworkInterfacesRequest.
        :rtype: list[str]
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ListSubNetworkInterfacesRequest.

        功能说明：辅助弹性网卡ID，支持多ID过滤 使用场景：查询需要的多个辅助弹性网卡信息

        :param id: The id of this ListSubNetworkInterfacesRequest.
        :type id: list[str]
        """
        self._id = id

    @property
    def virsubnet_id(self):
        """Gets the virsubnet_id of this ListSubNetworkInterfacesRequest.

        功能说明：辅助弹性网卡所属虚拟子网的ID，支持多个ID过滤 使用场景：过滤需要的单个或者多个虚拟子网下的辅助弹性网卡

        :return: The virsubnet_id of this ListSubNetworkInterfacesRequest.
        :rtype: list[str]
        """
        return self._virsubnet_id

    @virsubnet_id.setter
    def virsubnet_id(self, virsubnet_id):
        """Sets the virsubnet_id of this ListSubNetworkInterfacesRequest.

        功能说明：辅助弹性网卡所属虚拟子网的ID，支持多个ID过滤 使用场景：过滤需要的单个或者多个虚拟子网下的辅助弹性网卡

        :param virsubnet_id: The virsubnet_id of this ListSubNetworkInterfacesRequest.
        :type virsubnet_id: list[str]
        """
        self._virsubnet_id = virsubnet_id

    @property
    def private_ip_address(self):
        """Gets the private_ip_address of this ListSubNetworkInterfacesRequest.

        功能说明：辅助弹性网卡的私有IPv4地址，支持多个地址同时过滤 使用场景：通过单个或者多个ip地址过滤查询辅助弹性网卡

        :return: The private_ip_address of this ListSubNetworkInterfacesRequest.
        :rtype: list[str]
        """
        return self._private_ip_address

    @private_ip_address.setter
    def private_ip_address(self, private_ip_address):
        """Sets the private_ip_address of this ListSubNetworkInterfacesRequest.

        功能说明：辅助弹性网卡的私有IPv4地址，支持多个地址同时过滤 使用场景：通过单个或者多个ip地址过滤查询辅助弹性网卡

        :param private_ip_address: The private_ip_address of this ListSubNetworkInterfacesRequest.
        :type private_ip_address: list[str]
        """
        self._private_ip_address = private_ip_address

    @property
    def mac_address(self):
        """Gets the mac_address of this ListSubNetworkInterfacesRequest.

        功能说明：辅助弹性网卡的mac地址，支持多个同时过滤 使用场景：使用mac地址精确过滤辅助弹性网卡

        :return: The mac_address of this ListSubNetworkInterfacesRequest.
        :rtype: list[str]
        """
        return self._mac_address

    @mac_address.setter
    def mac_address(self, mac_address):
        """Sets the mac_address of this ListSubNetworkInterfacesRequest.

        功能说明：辅助弹性网卡的mac地址，支持多个同时过滤 使用场景：使用mac地址精确过滤辅助弹性网卡

        :param mac_address: The mac_address of this ListSubNetworkInterfacesRequest.
        :type mac_address: list[str]
        """
        self._mac_address = mac_address

    @property
    def vpc_id(self):
        """Gets the vpc_id of this ListSubNetworkInterfacesRequest.

        功能说明：辅助弹性网卡所属的VPC_ID，支持多ID过滤 使用场景：过滤单个或多个VPC下的辅助弹性网卡信息

        :return: The vpc_id of this ListSubNetworkInterfacesRequest.
        :rtype: list[str]
        """
        return self._vpc_id

    @vpc_id.setter
    def vpc_id(self, vpc_id):
        """Sets the vpc_id of this ListSubNetworkInterfacesRequest.

        功能说明：辅助弹性网卡所属的VPC_ID，支持多ID过滤 使用场景：过滤单个或多个VPC下的辅助弹性网卡信息

        :param vpc_id: The vpc_id of this ListSubNetworkInterfacesRequest.
        :type vpc_id: list[str]
        """
        self._vpc_id = vpc_id

    @property
    def description(self):
        """Gets the description of this ListSubNetworkInterfacesRequest.

        功能说明：辅助弹性网卡的描述信息，支持多个同时过滤 使用场景：通过描述信息过滤辅助弹性网卡

        :return: The description of this ListSubNetworkInterfacesRequest.
        :rtype: list[str]
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this ListSubNetworkInterfacesRequest.

        功能说明：辅助弹性网卡的描述信息，支持多个同时过滤 使用场景：通过描述信息过滤辅助弹性网卡

        :param description: The description of this ListSubNetworkInterfacesRequest.
        :type description: list[str]
        """
        self._description = description

    @property
    def parent_id(self):
        """Gets the parent_id of this ListSubNetworkInterfacesRequest.

        功能说明：辅助弹性网卡的宿主网卡的ID，支持多ID过滤 使用场景：过滤单个或多个宿主网卡下存在的辅助弹性网卡

        :return: The parent_id of this ListSubNetworkInterfacesRequest.
        :rtype: list[str]
        """
        return self._parent_id

    @parent_id.setter
    def parent_id(self, parent_id):
        """Sets the parent_id of this ListSubNetworkInterfacesRequest.

        功能说明：辅助弹性网卡的宿主网卡的ID，支持多ID过滤 使用场景：过滤单个或多个宿主网卡下存在的辅助弹性网卡

        :param parent_id: The parent_id of this ListSubNetworkInterfacesRequest.
        :type parent_id: list[str]
        """
        self._parent_id = parent_id

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
        if not isinstance(other, ListSubNetworkInterfacesRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

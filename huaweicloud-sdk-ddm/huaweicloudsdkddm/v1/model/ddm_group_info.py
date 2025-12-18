# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DdmGroupInfo:

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
        'role': 'str',
        'endpoint': 'str',
        'ipv6_endpoint': 'str',
        'node_count': 'int',
        'load_balance': 'bool',
        'is_default_group': 'bool',
        'extend_map': 'dict(str, str)',
        'nodes': 'list[DdmNodeInfo]'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'role': 'role',
        'endpoint': 'endpoint',
        'ipv6_endpoint': 'ipv6_endpoint',
        'node_count': 'node_count',
        'load_balance': 'load_balance',
        'is_default_group': 'is_default_group',
        'extend_map': 'extend_map',
        'nodes': 'nodes'
    }

    def __init__(self, id=None, name=None, role=None, endpoint=None, ipv6_endpoint=None, node_count=None, load_balance=None, is_default_group=None, extend_map=None, nodes=None):
        r"""DdmGroupInfo

        The model defined in huaweicloud sdk

        :param id: 组ID。
        :type id: str
        :param name: 名称。
        :type name: str
        :param role: 角色。
        :type role: str
        :param endpoint: 组ip。
        :type endpoint: str
        :param ipv6_endpoint: ipv6。
        :type ipv6_endpoint: str
        :param node_count: 节点数量。
        :type node_count: int
        :param load_balance: 负载均衡。
        :type load_balance: bool
        :param is_default_group: 是否默认组。
        :type is_default_group: bool
        :param extend_map: 其他信息。
        :type extend_map: dict(str, str)
        :param nodes: 节点信息。
        :type nodes: list[:class:`huaweicloudsdkddm.v1.DdmNodeInfo`]
        """
        
        

        self._id = None
        self._name = None
        self._role = None
        self._endpoint = None
        self._ipv6_endpoint = None
        self._node_count = None
        self._load_balance = None
        self._is_default_group = None
        self._extend_map = None
        self._nodes = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if role is not None:
            self.role = role
        if endpoint is not None:
            self.endpoint = endpoint
        if ipv6_endpoint is not None:
            self.ipv6_endpoint = ipv6_endpoint
        if node_count is not None:
            self.node_count = node_count
        if load_balance is not None:
            self.load_balance = load_balance
        if is_default_group is not None:
            self.is_default_group = is_default_group
        if extend_map is not None:
            self.extend_map = extend_map
        if nodes is not None:
            self.nodes = nodes

    @property
    def id(self):
        r"""Gets the id of this DdmGroupInfo.

        组ID。

        :return: The id of this DdmGroupInfo.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this DdmGroupInfo.

        组ID。

        :param id: The id of this DdmGroupInfo.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        r"""Gets the name of this DdmGroupInfo.

        名称。

        :return: The name of this DdmGroupInfo.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this DdmGroupInfo.

        名称。

        :param name: The name of this DdmGroupInfo.
        :type name: str
        """
        self._name = name

    @property
    def role(self):
        r"""Gets the role of this DdmGroupInfo.

        角色。

        :return: The role of this DdmGroupInfo.
        :rtype: str
        """
        return self._role

    @role.setter
    def role(self, role):
        r"""Sets the role of this DdmGroupInfo.

        角色。

        :param role: The role of this DdmGroupInfo.
        :type role: str
        """
        self._role = role

    @property
    def endpoint(self):
        r"""Gets the endpoint of this DdmGroupInfo.

        组ip。

        :return: The endpoint of this DdmGroupInfo.
        :rtype: str
        """
        return self._endpoint

    @endpoint.setter
    def endpoint(self, endpoint):
        r"""Sets the endpoint of this DdmGroupInfo.

        组ip。

        :param endpoint: The endpoint of this DdmGroupInfo.
        :type endpoint: str
        """
        self._endpoint = endpoint

    @property
    def ipv6_endpoint(self):
        r"""Gets the ipv6_endpoint of this DdmGroupInfo.

        ipv6。

        :return: The ipv6_endpoint of this DdmGroupInfo.
        :rtype: str
        """
        return self._ipv6_endpoint

    @ipv6_endpoint.setter
    def ipv6_endpoint(self, ipv6_endpoint):
        r"""Sets the ipv6_endpoint of this DdmGroupInfo.

        ipv6。

        :param ipv6_endpoint: The ipv6_endpoint of this DdmGroupInfo.
        :type ipv6_endpoint: str
        """
        self._ipv6_endpoint = ipv6_endpoint

    @property
    def node_count(self):
        r"""Gets the node_count of this DdmGroupInfo.

        节点数量。

        :return: The node_count of this DdmGroupInfo.
        :rtype: int
        """
        return self._node_count

    @node_count.setter
    def node_count(self, node_count):
        r"""Sets the node_count of this DdmGroupInfo.

        节点数量。

        :param node_count: The node_count of this DdmGroupInfo.
        :type node_count: int
        """
        self._node_count = node_count

    @property
    def load_balance(self):
        r"""Gets the load_balance of this DdmGroupInfo.

        负载均衡。

        :return: The load_balance of this DdmGroupInfo.
        :rtype: bool
        """
        return self._load_balance

    @load_balance.setter
    def load_balance(self, load_balance):
        r"""Sets the load_balance of this DdmGroupInfo.

        负载均衡。

        :param load_balance: The load_balance of this DdmGroupInfo.
        :type load_balance: bool
        """
        self._load_balance = load_balance

    @property
    def is_default_group(self):
        r"""Gets the is_default_group of this DdmGroupInfo.

        是否默认组。

        :return: The is_default_group of this DdmGroupInfo.
        :rtype: bool
        """
        return self._is_default_group

    @is_default_group.setter
    def is_default_group(self, is_default_group):
        r"""Sets the is_default_group of this DdmGroupInfo.

        是否默认组。

        :param is_default_group: The is_default_group of this DdmGroupInfo.
        :type is_default_group: bool
        """
        self._is_default_group = is_default_group

    @property
    def extend_map(self):
        r"""Gets the extend_map of this DdmGroupInfo.

        其他信息。

        :return: The extend_map of this DdmGroupInfo.
        :rtype: dict(str, str)
        """
        return self._extend_map

    @extend_map.setter
    def extend_map(self, extend_map):
        r"""Sets the extend_map of this DdmGroupInfo.

        其他信息。

        :param extend_map: The extend_map of this DdmGroupInfo.
        :type extend_map: dict(str, str)
        """
        self._extend_map = extend_map

    @property
    def nodes(self):
        r"""Gets the nodes of this DdmGroupInfo.

        节点信息。

        :return: The nodes of this DdmGroupInfo.
        :rtype: list[:class:`huaweicloudsdkddm.v1.DdmNodeInfo`]
        """
        return self._nodes

    @nodes.setter
    def nodes(self, nodes):
        r"""Sets the nodes of this DdmGroupInfo.

        节点信息。

        :param nodes: The nodes of this DdmGroupInfo.
        :type nodes: list[:class:`huaweicloudsdkddm.v1.DdmNodeInfo`]
        """
        self._nodes = nodes

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
        if not isinstance(other, DdmGroupInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

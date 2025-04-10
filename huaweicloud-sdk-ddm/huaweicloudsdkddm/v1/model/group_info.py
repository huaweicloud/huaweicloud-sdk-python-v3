# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class GroupInfo:

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
        'is_load_balance': 'bool',
        'is_default_group': 'bool',
        'cpu_num_per_node': 'int',
        'mem_num_per_node': 'int',
        'architecture': 'str',
        'node_list': 'list[GroupNodeInfo]'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'role': 'role',
        'endpoint': 'endpoint',
        'ipv6_endpoint': 'ipv6_endpoint',
        'is_load_balance': 'is_load_balance',
        'is_default_group': 'is_default_group',
        'cpu_num_per_node': 'cpu_num_per_node',
        'mem_num_per_node': 'mem_num_per_node',
        'architecture': 'architecture',
        'node_list': 'node_list'
    }

    def __init__(self, id=None, name=None, role=None, endpoint=None, ipv6_endpoint=None, is_load_balance=None, is_default_group=None, cpu_num_per_node=None, mem_num_per_node=None, architecture=None, node_list=None):
        r"""GroupInfo

        The model defined in huaweicloud sdk

        :param id: 组ID。
        :type id: str
        :param name: 组名称。
        :type name: str
        :param role: 组角色类型。
        :type role: str
        :param endpoint: 组连接地址，如未开启负载均衡，则返回的是组内节点连接地址串。
        :type endpoint: str
        :param ipv6_endpoint: 组ipv6连接地址。
        :type ipv6_endpoint: str
        :param is_load_balance: 是否开启负载均衡。
        :type is_load_balance: bool
        :param is_default_group: 是否默认组。
        :type is_default_group: bool
        :param cpu_num_per_node: 单节点CPU核数。
        :type cpu_num_per_node: int
        :param mem_num_per_node: 单节点内存大小,单位G。
        :type mem_num_per_node: int
        :param architecture: CPU架构。
        :type architecture: str
        :param node_list: 节点信息列表。
        :type node_list: list[:class:`huaweicloudsdkddm.v1.GroupNodeInfo`]
        """
        
        

        self._id = None
        self._name = None
        self._role = None
        self._endpoint = None
        self._ipv6_endpoint = None
        self._is_load_balance = None
        self._is_default_group = None
        self._cpu_num_per_node = None
        self._mem_num_per_node = None
        self._architecture = None
        self._node_list = None
        self.discriminator = None

        self.id = id
        self.name = name
        self.role = role
        self.endpoint = endpoint
        if ipv6_endpoint is not None:
            self.ipv6_endpoint = ipv6_endpoint
        self.is_load_balance = is_load_balance
        self.is_default_group = is_default_group
        self.cpu_num_per_node = cpu_num_per_node
        self.mem_num_per_node = mem_num_per_node
        self.architecture = architecture
        self.node_list = node_list

    @property
    def id(self):
        r"""Gets the id of this GroupInfo.

        组ID。

        :return: The id of this GroupInfo.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this GroupInfo.

        组ID。

        :param id: The id of this GroupInfo.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        r"""Gets the name of this GroupInfo.

        组名称。

        :return: The name of this GroupInfo.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this GroupInfo.

        组名称。

        :param name: The name of this GroupInfo.
        :type name: str
        """
        self._name = name

    @property
    def role(self):
        r"""Gets the role of this GroupInfo.

        组角色类型。

        :return: The role of this GroupInfo.
        :rtype: str
        """
        return self._role

    @role.setter
    def role(self, role):
        r"""Sets the role of this GroupInfo.

        组角色类型。

        :param role: The role of this GroupInfo.
        :type role: str
        """
        self._role = role

    @property
    def endpoint(self):
        r"""Gets the endpoint of this GroupInfo.

        组连接地址，如未开启负载均衡，则返回的是组内节点连接地址串。

        :return: The endpoint of this GroupInfo.
        :rtype: str
        """
        return self._endpoint

    @endpoint.setter
    def endpoint(self, endpoint):
        r"""Sets the endpoint of this GroupInfo.

        组连接地址，如未开启负载均衡，则返回的是组内节点连接地址串。

        :param endpoint: The endpoint of this GroupInfo.
        :type endpoint: str
        """
        self._endpoint = endpoint

    @property
    def ipv6_endpoint(self):
        r"""Gets the ipv6_endpoint of this GroupInfo.

        组ipv6连接地址。

        :return: The ipv6_endpoint of this GroupInfo.
        :rtype: str
        """
        return self._ipv6_endpoint

    @ipv6_endpoint.setter
    def ipv6_endpoint(self, ipv6_endpoint):
        r"""Sets the ipv6_endpoint of this GroupInfo.

        组ipv6连接地址。

        :param ipv6_endpoint: The ipv6_endpoint of this GroupInfo.
        :type ipv6_endpoint: str
        """
        self._ipv6_endpoint = ipv6_endpoint

    @property
    def is_load_balance(self):
        r"""Gets the is_load_balance of this GroupInfo.

        是否开启负载均衡。

        :return: The is_load_balance of this GroupInfo.
        :rtype: bool
        """
        return self._is_load_balance

    @is_load_balance.setter
    def is_load_balance(self, is_load_balance):
        r"""Sets the is_load_balance of this GroupInfo.

        是否开启负载均衡。

        :param is_load_balance: The is_load_balance of this GroupInfo.
        :type is_load_balance: bool
        """
        self._is_load_balance = is_load_balance

    @property
    def is_default_group(self):
        r"""Gets the is_default_group of this GroupInfo.

        是否默认组。

        :return: The is_default_group of this GroupInfo.
        :rtype: bool
        """
        return self._is_default_group

    @is_default_group.setter
    def is_default_group(self, is_default_group):
        r"""Sets the is_default_group of this GroupInfo.

        是否默认组。

        :param is_default_group: The is_default_group of this GroupInfo.
        :type is_default_group: bool
        """
        self._is_default_group = is_default_group

    @property
    def cpu_num_per_node(self):
        r"""Gets the cpu_num_per_node of this GroupInfo.

        单节点CPU核数。

        :return: The cpu_num_per_node of this GroupInfo.
        :rtype: int
        """
        return self._cpu_num_per_node

    @cpu_num_per_node.setter
    def cpu_num_per_node(self, cpu_num_per_node):
        r"""Sets the cpu_num_per_node of this GroupInfo.

        单节点CPU核数。

        :param cpu_num_per_node: The cpu_num_per_node of this GroupInfo.
        :type cpu_num_per_node: int
        """
        self._cpu_num_per_node = cpu_num_per_node

    @property
    def mem_num_per_node(self):
        r"""Gets the mem_num_per_node of this GroupInfo.

        单节点内存大小,单位G。

        :return: The mem_num_per_node of this GroupInfo.
        :rtype: int
        """
        return self._mem_num_per_node

    @mem_num_per_node.setter
    def mem_num_per_node(self, mem_num_per_node):
        r"""Sets the mem_num_per_node of this GroupInfo.

        单节点内存大小,单位G。

        :param mem_num_per_node: The mem_num_per_node of this GroupInfo.
        :type mem_num_per_node: int
        """
        self._mem_num_per_node = mem_num_per_node

    @property
    def architecture(self):
        r"""Gets the architecture of this GroupInfo.

        CPU架构。

        :return: The architecture of this GroupInfo.
        :rtype: str
        """
        return self._architecture

    @architecture.setter
    def architecture(self, architecture):
        r"""Sets the architecture of this GroupInfo.

        CPU架构。

        :param architecture: The architecture of this GroupInfo.
        :type architecture: str
        """
        self._architecture = architecture

    @property
    def node_list(self):
        r"""Gets the node_list of this GroupInfo.

        节点信息列表。

        :return: The node_list of this GroupInfo.
        :rtype: list[:class:`huaweicloudsdkddm.v1.GroupNodeInfo`]
        """
        return self._node_list

    @node_list.setter
    def node_list(self, node_list):
        r"""Sets the node_list of this GroupInfo.

        节点信息列表。

        :param node_list: The node_list of this GroupInfo.
        :type node_list: list[:class:`huaweicloudsdkddm.v1.GroupNodeInfo`]
        """
        self._node_list = node_list

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
        if not isinstance(other, GroupInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

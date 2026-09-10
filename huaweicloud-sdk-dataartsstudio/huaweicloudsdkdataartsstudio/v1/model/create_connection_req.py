# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateConnectionReq:

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
        'dest_vpc_id': 'str',
        'dest_network_id': 'str',
        'clusters': 'list[str]',
        'hosts': 'list[ConnectionsHost]',
        'routetable_id': 'str'
    }

    attribute_map = {
        'name': 'name',
        'dest_vpc_id': 'dest_vpc_id',
        'dest_network_id': 'dest_network_id',
        'clusters': 'clusters',
        'hosts': 'hosts',
        'routetable_id': 'routetable_id'
    }

    def __init__(self, name=None, dest_vpc_id=None, dest_network_id=None, clusters=None, hosts=None, routetable_id=None):
        r"""CreateConnectionReq

        The model defined in huaweicloud sdk

        :param name: 连接名称。长度64，数字字母下划线组成。
        :type name: str
        :param dest_vpc_id: 对应服务的vpc的ID。
        :type dest_vpc_id: str
        :param dest_network_id: 对应服务的子网网络ID，即为需要建立连接的服务所在的子网。
        :type dest_network_id: str
        :param clusters: 需要使用连接的集群ID列表。单条最大长度128字符。
        :type clusters: list[str]
        :param hosts: 用户自定义主机信息，最大支持2万条记录。
        :type hosts: list[:class:`huaweicloudsdkdataartsstudio.v1.ConnectionsHost`]
        :param routetable_id: 对应服务的子网关联的路由表。
        :type routetable_id: str
        """
        
        

        self._name = None
        self._dest_vpc_id = None
        self._dest_network_id = None
        self._clusters = None
        self._hosts = None
        self._routetable_id = None
        self.discriminator = None

        self.name = name
        self.dest_vpc_id = dest_vpc_id
        self.dest_network_id = dest_network_id
        if clusters is not None:
            self.clusters = clusters
        if hosts is not None:
            self.hosts = hosts
        if routetable_id is not None:
            self.routetable_id = routetable_id

    @property
    def name(self):
        r"""Gets the name of this CreateConnectionReq.

        连接名称。长度64，数字字母下划线组成。

        :return: The name of this CreateConnectionReq.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this CreateConnectionReq.

        连接名称。长度64，数字字母下划线组成。

        :param name: The name of this CreateConnectionReq.
        :type name: str
        """
        self._name = name

    @property
    def dest_vpc_id(self):
        r"""Gets the dest_vpc_id of this CreateConnectionReq.

        对应服务的vpc的ID。

        :return: The dest_vpc_id of this CreateConnectionReq.
        :rtype: str
        """
        return self._dest_vpc_id

    @dest_vpc_id.setter
    def dest_vpc_id(self, dest_vpc_id):
        r"""Sets the dest_vpc_id of this CreateConnectionReq.

        对应服务的vpc的ID。

        :param dest_vpc_id: The dest_vpc_id of this CreateConnectionReq.
        :type dest_vpc_id: str
        """
        self._dest_vpc_id = dest_vpc_id

    @property
    def dest_network_id(self):
        r"""Gets the dest_network_id of this CreateConnectionReq.

        对应服务的子网网络ID，即为需要建立连接的服务所在的子网。

        :return: The dest_network_id of this CreateConnectionReq.
        :rtype: str
        """
        return self._dest_network_id

    @dest_network_id.setter
    def dest_network_id(self, dest_network_id):
        r"""Sets the dest_network_id of this CreateConnectionReq.

        对应服务的子网网络ID，即为需要建立连接的服务所在的子网。

        :param dest_network_id: The dest_network_id of this CreateConnectionReq.
        :type dest_network_id: str
        """
        self._dest_network_id = dest_network_id

    @property
    def clusters(self):
        r"""Gets the clusters of this CreateConnectionReq.

        需要使用连接的集群ID列表。单条最大长度128字符。

        :return: The clusters of this CreateConnectionReq.
        :rtype: list[str]
        """
        return self._clusters

    @clusters.setter
    def clusters(self, clusters):
        r"""Sets the clusters of this CreateConnectionReq.

        需要使用连接的集群ID列表。单条最大长度128字符。

        :param clusters: The clusters of this CreateConnectionReq.
        :type clusters: list[str]
        """
        self._clusters = clusters

    @property
    def hosts(self):
        r"""Gets the hosts of this CreateConnectionReq.

        用户自定义主机信息，最大支持2万条记录。

        :return: The hosts of this CreateConnectionReq.
        :rtype: list[:class:`huaweicloudsdkdataartsstudio.v1.ConnectionsHost`]
        """
        return self._hosts

    @hosts.setter
    def hosts(self, hosts):
        r"""Sets the hosts of this CreateConnectionReq.

        用户自定义主机信息，最大支持2万条记录。

        :param hosts: The hosts of this CreateConnectionReq.
        :type hosts: list[:class:`huaweicloudsdkdataartsstudio.v1.ConnectionsHost`]
        """
        self._hosts = hosts

    @property
    def routetable_id(self):
        r"""Gets the routetable_id of this CreateConnectionReq.

        对应服务的子网关联的路由表。

        :return: The routetable_id of this CreateConnectionReq.
        :rtype: str
        """
        return self._routetable_id

    @routetable_id.setter
    def routetable_id(self, routetable_id):
        r"""Sets the routetable_id of this CreateConnectionReq.

        对应服务的子网关联的路由表。

        :param routetable_id: The routetable_id of this CreateConnectionReq.
        :type routetable_id: str
        """
        self._routetable_id = routetable_id

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
        if not isinstance(other, CreateConnectionReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

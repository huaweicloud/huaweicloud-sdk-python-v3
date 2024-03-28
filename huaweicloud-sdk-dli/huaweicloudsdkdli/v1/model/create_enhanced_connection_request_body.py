# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateEnhancedConnectionRequestBody:

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
        'elastic_resource_pools': 'list[str]',
        'queues': 'list[str]',
        'hosts': 'list[EnhancedConnectionHost]',
        'routetable_id': 'str',
        'tags': 'list[Tag]'
    }

    attribute_map = {
        'name': 'name',
        'dest_vpc_id': 'dest_vpc_id',
        'dest_network_id': 'dest_network_id',
        'elastic_resource_pools': 'elastic_resource_pools',
        'queues': 'queues',
        'hosts': 'hosts',
        'routetable_id': 'routetable_id',
        'tags': 'tags'
    }

    def __init__(self, name=None, dest_vpc_id=None, dest_network_id=None, elastic_resource_pools=None, queues=None, hosts=None, routetable_id=None, tags=None):
        """CreateEnhancedConnectionRequestBody

        The model defined in huaweicloud sdk

        :param name: 连接名称。长度64，数字字母下划线组成。
        :type name: str
        :param dest_vpc_id: 对应服务的vpc的ID。
        :type dest_vpc_id: str
        :param dest_network_id: 对应服务的子网网络ID，即为需要建立连接的服务所在的子网。
        :type dest_network_id: str
        :param elastic_resource_pools: 弹性资源池列表。
        :type elastic_resource_pools: list[str]
        :param queues: 需要使用跨源的队列列表。
        :type queues: list[str]
        :param hosts: 用户自定义主机信息，最大支持2万条记录。
        :type hosts: list[:class:`huaweicloudsdkdli.v1.EnhancedConnectionHost`]
        :param routetable_id: 对应服务的子网关联的路由表。
        :type routetable_id: str
        :param tags: 标签
        :type tags: list[:class:`huaweicloudsdkdli.v1.Tag`]
        """
        
        

        self._name = None
        self._dest_vpc_id = None
        self._dest_network_id = None
        self._elastic_resource_pools = None
        self._queues = None
        self._hosts = None
        self._routetable_id = None
        self._tags = None
        self.discriminator = None

        self.name = name
        self.dest_vpc_id = dest_vpc_id
        self.dest_network_id = dest_network_id
        if elastic_resource_pools is not None:
            self.elastic_resource_pools = elastic_resource_pools
        if queues is not None:
            self.queues = queues
        if hosts is not None:
            self.hosts = hosts
        if routetable_id is not None:
            self.routetable_id = routetable_id
        if tags is not None:
            self.tags = tags

    @property
    def name(self):
        """Gets the name of this CreateEnhancedConnectionRequestBody.

        连接名称。长度64，数字字母下划线组成。

        :return: The name of this CreateEnhancedConnectionRequestBody.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CreateEnhancedConnectionRequestBody.

        连接名称。长度64，数字字母下划线组成。

        :param name: The name of this CreateEnhancedConnectionRequestBody.
        :type name: str
        """
        self._name = name

    @property
    def dest_vpc_id(self):
        """Gets the dest_vpc_id of this CreateEnhancedConnectionRequestBody.

        对应服务的vpc的ID。

        :return: The dest_vpc_id of this CreateEnhancedConnectionRequestBody.
        :rtype: str
        """
        return self._dest_vpc_id

    @dest_vpc_id.setter
    def dest_vpc_id(self, dest_vpc_id):
        """Sets the dest_vpc_id of this CreateEnhancedConnectionRequestBody.

        对应服务的vpc的ID。

        :param dest_vpc_id: The dest_vpc_id of this CreateEnhancedConnectionRequestBody.
        :type dest_vpc_id: str
        """
        self._dest_vpc_id = dest_vpc_id

    @property
    def dest_network_id(self):
        """Gets the dest_network_id of this CreateEnhancedConnectionRequestBody.

        对应服务的子网网络ID，即为需要建立连接的服务所在的子网。

        :return: The dest_network_id of this CreateEnhancedConnectionRequestBody.
        :rtype: str
        """
        return self._dest_network_id

    @dest_network_id.setter
    def dest_network_id(self, dest_network_id):
        """Sets the dest_network_id of this CreateEnhancedConnectionRequestBody.

        对应服务的子网网络ID，即为需要建立连接的服务所在的子网。

        :param dest_network_id: The dest_network_id of this CreateEnhancedConnectionRequestBody.
        :type dest_network_id: str
        """
        self._dest_network_id = dest_network_id

    @property
    def elastic_resource_pools(self):
        """Gets the elastic_resource_pools of this CreateEnhancedConnectionRequestBody.

        弹性资源池列表。

        :return: The elastic_resource_pools of this CreateEnhancedConnectionRequestBody.
        :rtype: list[str]
        """
        return self._elastic_resource_pools

    @elastic_resource_pools.setter
    def elastic_resource_pools(self, elastic_resource_pools):
        """Sets the elastic_resource_pools of this CreateEnhancedConnectionRequestBody.

        弹性资源池列表。

        :param elastic_resource_pools: The elastic_resource_pools of this CreateEnhancedConnectionRequestBody.
        :type elastic_resource_pools: list[str]
        """
        self._elastic_resource_pools = elastic_resource_pools

    @property
    def queues(self):
        """Gets the queues of this CreateEnhancedConnectionRequestBody.

        需要使用跨源的队列列表。

        :return: The queues of this CreateEnhancedConnectionRequestBody.
        :rtype: list[str]
        """
        return self._queues

    @queues.setter
    def queues(self, queues):
        """Sets the queues of this CreateEnhancedConnectionRequestBody.

        需要使用跨源的队列列表。

        :param queues: The queues of this CreateEnhancedConnectionRequestBody.
        :type queues: list[str]
        """
        self._queues = queues

    @property
    def hosts(self):
        """Gets the hosts of this CreateEnhancedConnectionRequestBody.

        用户自定义主机信息，最大支持2万条记录。

        :return: The hosts of this CreateEnhancedConnectionRequestBody.
        :rtype: list[:class:`huaweicloudsdkdli.v1.EnhancedConnectionHost`]
        """
        return self._hosts

    @hosts.setter
    def hosts(self, hosts):
        """Sets the hosts of this CreateEnhancedConnectionRequestBody.

        用户自定义主机信息，最大支持2万条记录。

        :param hosts: The hosts of this CreateEnhancedConnectionRequestBody.
        :type hosts: list[:class:`huaweicloudsdkdli.v1.EnhancedConnectionHost`]
        """
        self._hosts = hosts

    @property
    def routetable_id(self):
        """Gets the routetable_id of this CreateEnhancedConnectionRequestBody.

        对应服务的子网关联的路由表。

        :return: The routetable_id of this CreateEnhancedConnectionRequestBody.
        :rtype: str
        """
        return self._routetable_id

    @routetable_id.setter
    def routetable_id(self, routetable_id):
        """Sets the routetable_id of this CreateEnhancedConnectionRequestBody.

        对应服务的子网关联的路由表。

        :param routetable_id: The routetable_id of this CreateEnhancedConnectionRequestBody.
        :type routetable_id: str
        """
        self._routetable_id = routetable_id

    @property
    def tags(self):
        """Gets the tags of this CreateEnhancedConnectionRequestBody.

        标签

        :return: The tags of this CreateEnhancedConnectionRequestBody.
        :rtype: list[:class:`huaweicloudsdkdli.v1.Tag`]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this CreateEnhancedConnectionRequestBody.

        标签

        :param tags: The tags of this CreateEnhancedConnectionRequestBody.
        :type tags: list[:class:`huaweicloudsdkdli.v1.Tag`]
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
        if not isinstance(other, CreateEnhancedConnectionRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

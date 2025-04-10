# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BatchCreateProtectedInstancesRequestParams:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'name_prefix': 'str',
        'description': 'str',
        'server_group_id': 'str',
        'cluster_id': 'str',
        'primary_subnet_id': 'str',
        'tenancy': 'str',
        'dedicated_host_id': 'str',
        'servers': 'list[ServerInfo]',
        'tags': 'list[ResourceTag]'
    }

    attribute_map = {
        'name_prefix': 'name_prefix',
        'description': 'description',
        'server_group_id': 'server_group_id',
        'cluster_id': 'cluster_id',
        'primary_subnet_id': 'primary_subnet_id',
        'tenancy': 'tenancy',
        'dedicated_host_id': 'dedicated_host_id',
        'servers': 'servers',
        'tags': 'tags'
    }

    def __init__(self, name_prefix=None, description=None, server_group_id=None, cluster_id=None, primary_subnet_id=None, tenancy=None, dedicated_host_id=None, servers=None, tags=None):
        r"""BatchCreateProtectedInstancesRequestParams

        The model defined in huaweicloud sdk

        :param name_prefix: 保护实例的名称前缀，批量创建保护实例时，为区分不同保护实例，创建过程中系统会自动在名称后加\&quot;-0001\&quot;的类似标记，故此时名称的长度为[1-59]个字符。只包含中文字符、英文字母（a～ｚ、Ａ～Ｚ）、数字（０~９）、小数点（．）、下划线（_）、中划线（-）。
        :type name_prefix: str
        :param description: 保护实例的描述，最大支持长度为64个字符。不能包含左尖括号（&lt;）或右尖括号（&gt;）。
        :type description: str
        :param server_group_id: 需要加入的保护组ID。
        :type server_group_id: str
        :param cluster_id: 专属分布式存储池ID。当容灾站点磁盘选择专属分布式存储时指定该字段。
        :type cluster_id: str
        :param primary_subnet_id: 容灾站点云服务器主网卡所在的子网subnetID，与neutron_network_id字段值一致。
        :type primary_subnet_id: str
        :param tenancy: 在专属主机或共享池中创建容灾站点云服务器，默认为在共享池中创建。值为：shared或dedicated。shared：表示共享池。dedicated：表示专属主机。
        :type tenancy: str
        :param dedicated_host_id: 专属主机id，此属性仅在tenancy值为dedicated时有效。若不指定此属性，系统将自动分配租户可以自动放置弹性云服务器的专属主机。
        :type dedicated_host_id: str
        :param servers: 用于创建保护实例的云服务器信息列表。
        :type servers: list[:class:`huaweicloudsdksdrs.v1.ServerInfo`]
        :param tags: 标签列表。
        :type tags: list[:class:`huaweicloudsdksdrs.v1.ResourceTag`]
        """
        
        

        self._name_prefix = None
        self._description = None
        self._server_group_id = None
        self._cluster_id = None
        self._primary_subnet_id = None
        self._tenancy = None
        self._dedicated_host_id = None
        self._servers = None
        self._tags = None
        self.discriminator = None

        self.name_prefix = name_prefix
        if description is not None:
            self.description = description
        self.server_group_id = server_group_id
        if cluster_id is not None:
            self.cluster_id = cluster_id
        if primary_subnet_id is not None:
            self.primary_subnet_id = primary_subnet_id
        if tenancy is not None:
            self.tenancy = tenancy
        if dedicated_host_id is not None:
            self.dedicated_host_id = dedicated_host_id
        self.servers = servers
        if tags is not None:
            self.tags = tags

    @property
    def name_prefix(self):
        r"""Gets the name_prefix of this BatchCreateProtectedInstancesRequestParams.

        保护实例的名称前缀，批量创建保护实例时，为区分不同保护实例，创建过程中系统会自动在名称后加\"-0001\"的类似标记，故此时名称的长度为[1-59]个字符。只包含中文字符、英文字母（a～ｚ、Ａ～Ｚ）、数字（０~９）、小数点（．）、下划线（_）、中划线（-）。

        :return: The name_prefix of this BatchCreateProtectedInstancesRequestParams.
        :rtype: str
        """
        return self._name_prefix

    @name_prefix.setter
    def name_prefix(self, name_prefix):
        r"""Sets the name_prefix of this BatchCreateProtectedInstancesRequestParams.

        保护实例的名称前缀，批量创建保护实例时，为区分不同保护实例，创建过程中系统会自动在名称后加\"-0001\"的类似标记，故此时名称的长度为[1-59]个字符。只包含中文字符、英文字母（a～ｚ、Ａ～Ｚ）、数字（０~９）、小数点（．）、下划线（_）、中划线（-）。

        :param name_prefix: The name_prefix of this BatchCreateProtectedInstancesRequestParams.
        :type name_prefix: str
        """
        self._name_prefix = name_prefix

    @property
    def description(self):
        r"""Gets the description of this BatchCreateProtectedInstancesRequestParams.

        保护实例的描述，最大支持长度为64个字符。不能包含左尖括号（<）或右尖括号（>）。

        :return: The description of this BatchCreateProtectedInstancesRequestParams.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this BatchCreateProtectedInstancesRequestParams.

        保护实例的描述，最大支持长度为64个字符。不能包含左尖括号（<）或右尖括号（>）。

        :param description: The description of this BatchCreateProtectedInstancesRequestParams.
        :type description: str
        """
        self._description = description

    @property
    def server_group_id(self):
        r"""Gets the server_group_id of this BatchCreateProtectedInstancesRequestParams.

        需要加入的保护组ID。

        :return: The server_group_id of this BatchCreateProtectedInstancesRequestParams.
        :rtype: str
        """
        return self._server_group_id

    @server_group_id.setter
    def server_group_id(self, server_group_id):
        r"""Sets the server_group_id of this BatchCreateProtectedInstancesRequestParams.

        需要加入的保护组ID。

        :param server_group_id: The server_group_id of this BatchCreateProtectedInstancesRequestParams.
        :type server_group_id: str
        """
        self._server_group_id = server_group_id

    @property
    def cluster_id(self):
        r"""Gets the cluster_id of this BatchCreateProtectedInstancesRequestParams.

        专属分布式存储池ID。当容灾站点磁盘选择专属分布式存储时指定该字段。

        :return: The cluster_id of this BatchCreateProtectedInstancesRequestParams.
        :rtype: str
        """
        return self._cluster_id

    @cluster_id.setter
    def cluster_id(self, cluster_id):
        r"""Sets the cluster_id of this BatchCreateProtectedInstancesRequestParams.

        专属分布式存储池ID。当容灾站点磁盘选择专属分布式存储时指定该字段。

        :param cluster_id: The cluster_id of this BatchCreateProtectedInstancesRequestParams.
        :type cluster_id: str
        """
        self._cluster_id = cluster_id

    @property
    def primary_subnet_id(self):
        r"""Gets the primary_subnet_id of this BatchCreateProtectedInstancesRequestParams.

        容灾站点云服务器主网卡所在的子网subnetID，与neutron_network_id字段值一致。

        :return: The primary_subnet_id of this BatchCreateProtectedInstancesRequestParams.
        :rtype: str
        """
        return self._primary_subnet_id

    @primary_subnet_id.setter
    def primary_subnet_id(self, primary_subnet_id):
        r"""Sets the primary_subnet_id of this BatchCreateProtectedInstancesRequestParams.

        容灾站点云服务器主网卡所在的子网subnetID，与neutron_network_id字段值一致。

        :param primary_subnet_id: The primary_subnet_id of this BatchCreateProtectedInstancesRequestParams.
        :type primary_subnet_id: str
        """
        self._primary_subnet_id = primary_subnet_id

    @property
    def tenancy(self):
        r"""Gets the tenancy of this BatchCreateProtectedInstancesRequestParams.

        在专属主机或共享池中创建容灾站点云服务器，默认为在共享池中创建。值为：shared或dedicated。shared：表示共享池。dedicated：表示专属主机。

        :return: The tenancy of this BatchCreateProtectedInstancesRequestParams.
        :rtype: str
        """
        return self._tenancy

    @tenancy.setter
    def tenancy(self, tenancy):
        r"""Sets the tenancy of this BatchCreateProtectedInstancesRequestParams.

        在专属主机或共享池中创建容灾站点云服务器，默认为在共享池中创建。值为：shared或dedicated。shared：表示共享池。dedicated：表示专属主机。

        :param tenancy: The tenancy of this BatchCreateProtectedInstancesRequestParams.
        :type tenancy: str
        """
        self._tenancy = tenancy

    @property
    def dedicated_host_id(self):
        r"""Gets the dedicated_host_id of this BatchCreateProtectedInstancesRequestParams.

        专属主机id，此属性仅在tenancy值为dedicated时有效。若不指定此属性，系统将自动分配租户可以自动放置弹性云服务器的专属主机。

        :return: The dedicated_host_id of this BatchCreateProtectedInstancesRequestParams.
        :rtype: str
        """
        return self._dedicated_host_id

    @dedicated_host_id.setter
    def dedicated_host_id(self, dedicated_host_id):
        r"""Sets the dedicated_host_id of this BatchCreateProtectedInstancesRequestParams.

        专属主机id，此属性仅在tenancy值为dedicated时有效。若不指定此属性，系统将自动分配租户可以自动放置弹性云服务器的专属主机。

        :param dedicated_host_id: The dedicated_host_id of this BatchCreateProtectedInstancesRequestParams.
        :type dedicated_host_id: str
        """
        self._dedicated_host_id = dedicated_host_id

    @property
    def servers(self):
        r"""Gets the servers of this BatchCreateProtectedInstancesRequestParams.

        用于创建保护实例的云服务器信息列表。

        :return: The servers of this BatchCreateProtectedInstancesRequestParams.
        :rtype: list[:class:`huaweicloudsdksdrs.v1.ServerInfo`]
        """
        return self._servers

    @servers.setter
    def servers(self, servers):
        r"""Sets the servers of this BatchCreateProtectedInstancesRequestParams.

        用于创建保护实例的云服务器信息列表。

        :param servers: The servers of this BatchCreateProtectedInstancesRequestParams.
        :type servers: list[:class:`huaweicloudsdksdrs.v1.ServerInfo`]
        """
        self._servers = servers

    @property
    def tags(self):
        r"""Gets the tags of this BatchCreateProtectedInstancesRequestParams.

        标签列表。

        :return: The tags of this BatchCreateProtectedInstancesRequestParams.
        :rtype: list[:class:`huaweicloudsdksdrs.v1.ResourceTag`]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        r"""Sets the tags of this BatchCreateProtectedInstancesRequestParams.

        标签列表。

        :param tags: The tags of this BatchCreateProtectedInstancesRequestParams.
        :type tags: list[:class:`huaweicloudsdksdrs.v1.ResourceTag`]
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
        if not isinstance(other, BatchCreateProtectedInstancesRequestParams):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

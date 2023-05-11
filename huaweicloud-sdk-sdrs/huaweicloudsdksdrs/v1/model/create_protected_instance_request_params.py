# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateProtectedInstanceRequestParams:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'server_group_id': 'str',
        'server_id': 'str',
        'name': 'str',
        'description': 'str',
        'cluster_id': 'str',
        'primary_subnet_id': 'str',
        'primary_ip_address': 'str',
        'tags': 'list[ResourceTag]',
        'flavor_ref': 'str',
        'tenancy': 'str',
        'dedicated_host_id': 'str'
    }

    attribute_map = {
        'server_group_id': 'server_group_id',
        'server_id': 'server_id',
        'name': 'name',
        'description': 'description',
        'cluster_id': 'cluster_id',
        'primary_subnet_id': 'primary_subnet_id',
        'primary_ip_address': 'primary_ip_address',
        'tags': 'tags',
        'flavor_ref': 'flavorRef',
        'tenancy': 'tenancy',
        'dedicated_host_id': 'dedicated_host_id'
    }

    def __init__(self, server_group_id=None, server_id=None, name=None, description=None, cluster_id=None, primary_subnet_id=None, primary_ip_address=None, tags=None, flavor_ref=None, tenancy=None, dedicated_host_id=None):
        """CreateProtectedInstanceRequestParams

        The model defined in huaweicloud sdk

        :param server_group_id: 需要加入的保护组ID。
        :type server_group_id: str
        :param server_id: 指定的生产站点云服务器ID。
        :type server_id: str
        :param name: 指定保护实例的名称，最大支持长度为64个字节。只包含中文字符、英文字母（a～ｚ、Ａ～Ｚ）、数字（０~９）、小数点（．）、下划线（_）、中划线（-）。
        :type name: str
        :param description: 指定保护实例的描述，最大支持长度为64个字节。不能包含左尖括号（&lt;）或右尖括号（&gt;）。
        :type description: str
        :param cluster_id: 专属分布式存储池ID。 当容灾站点磁盘选择专属分布式存储时指定该字段。
        :type cluster_id: str
        :param primary_subnet_id: 容灾站点云服务器主网卡所在的子网subnetID，与neutron_network_id字段值一致。
        :type primary_subnet_id: str
        :param primary_ip_address: 容灾站点云服务器主网卡IP地址。此参数仅在传入primary_subnet_id时有效。指定primary_subnet_id时，如果不指定该参数，将自动分配容灾站点云服务器主网卡IP地址。
        :type primary_ip_address: str
        :param tags: 标签列表。
        :type tags: list[:class:`huaweicloudsdksdrs.v1.ResourceTag`]
        :param flavor_ref: 指定的容灾站点云服务器的flavor ID。 查询flavor列表，请参见查询云服务器规格变更支持列表。  说明:不指定此参数时，容灾站点云服务器的flavor ID默认和生产站点云服务器保持一致。 不同规格的云服务器在性能上存在差异，可能会对云服务器上运行的应用产生影响。为保证切换/故障切换后云服务器的性能，建议容灾站点服务器的规格（CPU、内存）不低于生产站点云服务器的规格（CPU、内存）。 生产站点云服务器和容灾站点云服务器的flavor存在匹配关系，可以通过上述接口使用生产站点云服务器过滤出满足要求的容灾站点云服务器flavor。
        :type flavor_ref: str
        :param tenancy: 在专属主机或共享池中创建容灾站点云服务器，默认为在共享池中创建。 值为：shared或dedicated。shared：表示共享池。 dedicated：表示专属主机。
        :type tenancy: str
        :param dedicated_host_id: 专属主机id，此属性仅在tenancy值为dedicated时有效。 若不指定此属性，系统将自动分配租户可以自动放置弹性云服务器的专属主机。
        :type dedicated_host_id: str
        """
        
        

        self._server_group_id = None
        self._server_id = None
        self._name = None
        self._description = None
        self._cluster_id = None
        self._primary_subnet_id = None
        self._primary_ip_address = None
        self._tags = None
        self._flavor_ref = None
        self._tenancy = None
        self._dedicated_host_id = None
        self.discriminator = None

        self.server_group_id = server_group_id
        self.server_id = server_id
        self.name = name
        if description is not None:
            self.description = description
        if cluster_id is not None:
            self.cluster_id = cluster_id
        if primary_subnet_id is not None:
            self.primary_subnet_id = primary_subnet_id
        if primary_ip_address is not None:
            self.primary_ip_address = primary_ip_address
        if tags is not None:
            self.tags = tags
        if flavor_ref is not None:
            self.flavor_ref = flavor_ref
        if tenancy is not None:
            self.tenancy = tenancy
        if dedicated_host_id is not None:
            self.dedicated_host_id = dedicated_host_id

    @property
    def server_group_id(self):
        """Gets the server_group_id of this CreateProtectedInstanceRequestParams.

        需要加入的保护组ID。

        :return: The server_group_id of this CreateProtectedInstanceRequestParams.
        :rtype: str
        """
        return self._server_group_id

    @server_group_id.setter
    def server_group_id(self, server_group_id):
        """Sets the server_group_id of this CreateProtectedInstanceRequestParams.

        需要加入的保护组ID。

        :param server_group_id: The server_group_id of this CreateProtectedInstanceRequestParams.
        :type server_group_id: str
        """
        self._server_group_id = server_group_id

    @property
    def server_id(self):
        """Gets the server_id of this CreateProtectedInstanceRequestParams.

        指定的生产站点云服务器ID。

        :return: The server_id of this CreateProtectedInstanceRequestParams.
        :rtype: str
        """
        return self._server_id

    @server_id.setter
    def server_id(self, server_id):
        """Sets the server_id of this CreateProtectedInstanceRequestParams.

        指定的生产站点云服务器ID。

        :param server_id: The server_id of this CreateProtectedInstanceRequestParams.
        :type server_id: str
        """
        self._server_id = server_id

    @property
    def name(self):
        """Gets the name of this CreateProtectedInstanceRequestParams.

        指定保护实例的名称，最大支持长度为64个字节。只包含中文字符、英文字母（a～ｚ、Ａ～Ｚ）、数字（０~９）、小数点（．）、下划线（_）、中划线（-）。

        :return: The name of this CreateProtectedInstanceRequestParams.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CreateProtectedInstanceRequestParams.

        指定保护实例的名称，最大支持长度为64个字节。只包含中文字符、英文字母（a～ｚ、Ａ～Ｚ）、数字（０~９）、小数点（．）、下划线（_）、中划线（-）。

        :param name: The name of this CreateProtectedInstanceRequestParams.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        """Gets the description of this CreateProtectedInstanceRequestParams.

        指定保护实例的描述，最大支持长度为64个字节。不能包含左尖括号（<）或右尖括号（>）。

        :return: The description of this CreateProtectedInstanceRequestParams.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this CreateProtectedInstanceRequestParams.

        指定保护实例的描述，最大支持长度为64个字节。不能包含左尖括号（<）或右尖括号（>）。

        :param description: The description of this CreateProtectedInstanceRequestParams.
        :type description: str
        """
        self._description = description

    @property
    def cluster_id(self):
        """Gets the cluster_id of this CreateProtectedInstanceRequestParams.

        专属分布式存储池ID。 当容灾站点磁盘选择专属分布式存储时指定该字段。

        :return: The cluster_id of this CreateProtectedInstanceRequestParams.
        :rtype: str
        """
        return self._cluster_id

    @cluster_id.setter
    def cluster_id(self, cluster_id):
        """Sets the cluster_id of this CreateProtectedInstanceRequestParams.

        专属分布式存储池ID。 当容灾站点磁盘选择专属分布式存储时指定该字段。

        :param cluster_id: The cluster_id of this CreateProtectedInstanceRequestParams.
        :type cluster_id: str
        """
        self._cluster_id = cluster_id

    @property
    def primary_subnet_id(self):
        """Gets the primary_subnet_id of this CreateProtectedInstanceRequestParams.

        容灾站点云服务器主网卡所在的子网subnetID，与neutron_network_id字段值一致。

        :return: The primary_subnet_id of this CreateProtectedInstanceRequestParams.
        :rtype: str
        """
        return self._primary_subnet_id

    @primary_subnet_id.setter
    def primary_subnet_id(self, primary_subnet_id):
        """Sets the primary_subnet_id of this CreateProtectedInstanceRequestParams.

        容灾站点云服务器主网卡所在的子网subnetID，与neutron_network_id字段值一致。

        :param primary_subnet_id: The primary_subnet_id of this CreateProtectedInstanceRequestParams.
        :type primary_subnet_id: str
        """
        self._primary_subnet_id = primary_subnet_id

    @property
    def primary_ip_address(self):
        """Gets the primary_ip_address of this CreateProtectedInstanceRequestParams.

        容灾站点云服务器主网卡IP地址。此参数仅在传入primary_subnet_id时有效。指定primary_subnet_id时，如果不指定该参数，将自动分配容灾站点云服务器主网卡IP地址。

        :return: The primary_ip_address of this CreateProtectedInstanceRequestParams.
        :rtype: str
        """
        return self._primary_ip_address

    @primary_ip_address.setter
    def primary_ip_address(self, primary_ip_address):
        """Sets the primary_ip_address of this CreateProtectedInstanceRequestParams.

        容灾站点云服务器主网卡IP地址。此参数仅在传入primary_subnet_id时有效。指定primary_subnet_id时，如果不指定该参数，将自动分配容灾站点云服务器主网卡IP地址。

        :param primary_ip_address: The primary_ip_address of this CreateProtectedInstanceRequestParams.
        :type primary_ip_address: str
        """
        self._primary_ip_address = primary_ip_address

    @property
    def tags(self):
        """Gets the tags of this CreateProtectedInstanceRequestParams.

        标签列表。

        :return: The tags of this CreateProtectedInstanceRequestParams.
        :rtype: list[:class:`huaweicloudsdksdrs.v1.ResourceTag`]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this CreateProtectedInstanceRequestParams.

        标签列表。

        :param tags: The tags of this CreateProtectedInstanceRequestParams.
        :type tags: list[:class:`huaweicloudsdksdrs.v1.ResourceTag`]
        """
        self._tags = tags

    @property
    def flavor_ref(self):
        """Gets the flavor_ref of this CreateProtectedInstanceRequestParams.

        指定的容灾站点云服务器的flavor ID。 查询flavor列表，请参见查询云服务器规格变更支持列表。  说明:不指定此参数时，容灾站点云服务器的flavor ID默认和生产站点云服务器保持一致。 不同规格的云服务器在性能上存在差异，可能会对云服务器上运行的应用产生影响。为保证切换/故障切换后云服务器的性能，建议容灾站点服务器的规格（CPU、内存）不低于生产站点云服务器的规格（CPU、内存）。 生产站点云服务器和容灾站点云服务器的flavor存在匹配关系，可以通过上述接口使用生产站点云服务器过滤出满足要求的容灾站点云服务器flavor。

        :return: The flavor_ref of this CreateProtectedInstanceRequestParams.
        :rtype: str
        """
        return self._flavor_ref

    @flavor_ref.setter
    def flavor_ref(self, flavor_ref):
        """Sets the flavor_ref of this CreateProtectedInstanceRequestParams.

        指定的容灾站点云服务器的flavor ID。 查询flavor列表，请参见查询云服务器规格变更支持列表。  说明:不指定此参数时，容灾站点云服务器的flavor ID默认和生产站点云服务器保持一致。 不同规格的云服务器在性能上存在差异，可能会对云服务器上运行的应用产生影响。为保证切换/故障切换后云服务器的性能，建议容灾站点服务器的规格（CPU、内存）不低于生产站点云服务器的规格（CPU、内存）。 生产站点云服务器和容灾站点云服务器的flavor存在匹配关系，可以通过上述接口使用生产站点云服务器过滤出满足要求的容灾站点云服务器flavor。

        :param flavor_ref: The flavor_ref of this CreateProtectedInstanceRequestParams.
        :type flavor_ref: str
        """
        self._flavor_ref = flavor_ref

    @property
    def tenancy(self):
        """Gets the tenancy of this CreateProtectedInstanceRequestParams.

        在专属主机或共享池中创建容灾站点云服务器，默认为在共享池中创建。 值为：shared或dedicated。shared：表示共享池。 dedicated：表示专属主机。

        :return: The tenancy of this CreateProtectedInstanceRequestParams.
        :rtype: str
        """
        return self._tenancy

    @tenancy.setter
    def tenancy(self, tenancy):
        """Sets the tenancy of this CreateProtectedInstanceRequestParams.

        在专属主机或共享池中创建容灾站点云服务器，默认为在共享池中创建。 值为：shared或dedicated。shared：表示共享池。 dedicated：表示专属主机。

        :param tenancy: The tenancy of this CreateProtectedInstanceRequestParams.
        :type tenancy: str
        """
        self._tenancy = tenancy

    @property
    def dedicated_host_id(self):
        """Gets the dedicated_host_id of this CreateProtectedInstanceRequestParams.

        专属主机id，此属性仅在tenancy值为dedicated时有效。 若不指定此属性，系统将自动分配租户可以自动放置弹性云服务器的专属主机。

        :return: The dedicated_host_id of this CreateProtectedInstanceRequestParams.
        :rtype: str
        """
        return self._dedicated_host_id

    @dedicated_host_id.setter
    def dedicated_host_id(self, dedicated_host_id):
        """Sets the dedicated_host_id of this CreateProtectedInstanceRequestParams.

        专属主机id，此属性仅在tenancy值为dedicated时有效。 若不指定此属性，系统将自动分配租户可以自动放置弹性云服务器的专属主机。

        :param dedicated_host_id: The dedicated_host_id of this CreateProtectedInstanceRequestParams.
        :type dedicated_host_id: str
        """
        self._dedicated_host_id = dedicated_host_id

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
        if not isinstance(other, CreateProtectedInstanceRequestParams):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

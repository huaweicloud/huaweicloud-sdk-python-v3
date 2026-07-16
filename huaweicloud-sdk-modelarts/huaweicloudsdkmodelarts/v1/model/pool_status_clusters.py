# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PoolStatusClusters:

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
        'cluster_flavor': 'str',
        'type': 'str',
        'version': 'str',
        'plugins': 'PoolStatusClustersPlugins'
    }

    attribute_map = {
        'name': 'name',
        'cluster_flavor': 'clusterFlavor',
        'type': 'type',
        'version': 'version',
        'plugins': 'plugins'
    }

    def __init__(self, name=None, cluster_flavor=None, type=None, version=None, plugins=None):
        r"""PoolStatusClusters

        The model defined in huaweicloud sdk

        :param name: **参数解释**：集群名称。 **取值范围**：不涉及。
        :type name: str
        :param cluster_flavor: **参数解释**：标准池的集群规格。 **取值范围**：不涉及。
        :type cluster_flavor: str
        :param type: **参数解释**：资源池集群的类型。 **取值范围**：不涉及。
        :type type: str
        :param version: **参数解释**：集群的版本号。 **取值范围**：不涉及。
        :type version: str
        :param plugins: 
        :type plugins: :class:`huaweicloudsdkmodelarts.v1.PoolStatusClustersPlugins`
        """
        
        

        self._name = None
        self._cluster_flavor = None
        self._type = None
        self._version = None
        self._plugins = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if cluster_flavor is not None:
            self.cluster_flavor = cluster_flavor
        if type is not None:
            self.type = type
        if version is not None:
            self.version = version
        if plugins is not None:
            self.plugins = plugins

    @property
    def name(self):
        r"""Gets the name of this PoolStatusClusters.

        **参数解释**：集群名称。 **取值范围**：不涉及。

        :return: The name of this PoolStatusClusters.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this PoolStatusClusters.

        **参数解释**：集群名称。 **取值范围**：不涉及。

        :param name: The name of this PoolStatusClusters.
        :type name: str
        """
        self._name = name

    @property
    def cluster_flavor(self):
        r"""Gets the cluster_flavor of this PoolStatusClusters.

        **参数解释**：标准池的集群规格。 **取值范围**：不涉及。

        :return: The cluster_flavor of this PoolStatusClusters.
        :rtype: str
        """
        return self._cluster_flavor

    @cluster_flavor.setter
    def cluster_flavor(self, cluster_flavor):
        r"""Sets the cluster_flavor of this PoolStatusClusters.

        **参数解释**：标准池的集群规格。 **取值范围**：不涉及。

        :param cluster_flavor: The cluster_flavor of this PoolStatusClusters.
        :type cluster_flavor: str
        """
        self._cluster_flavor = cluster_flavor

    @property
    def type(self):
        r"""Gets the type of this PoolStatusClusters.

        **参数解释**：资源池集群的类型。 **取值范围**：不涉及。

        :return: The type of this PoolStatusClusters.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this PoolStatusClusters.

        **参数解释**：资源池集群的类型。 **取值范围**：不涉及。

        :param type: The type of this PoolStatusClusters.
        :type type: str
        """
        self._type = type

    @property
    def version(self):
        r"""Gets the version of this PoolStatusClusters.

        **参数解释**：集群的版本号。 **取值范围**：不涉及。

        :return: The version of this PoolStatusClusters.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        r"""Sets the version of this PoolStatusClusters.

        **参数解释**：集群的版本号。 **取值范围**：不涉及。

        :param version: The version of this PoolStatusClusters.
        :type version: str
        """
        self._version = version

    @property
    def plugins(self):
        r"""Gets the plugins of this PoolStatusClusters.

        :return: The plugins of this PoolStatusClusters.
        :rtype: :class:`huaweicloudsdkmodelarts.v1.PoolStatusClustersPlugins`
        """
        return self._plugins

    @plugins.setter
    def plugins(self, plugins):
        r"""Sets the plugins of this PoolStatusClusters.

        :param plugins: The plugins of this PoolStatusClusters.
        :type plugins: :class:`huaweicloudsdkmodelarts.v1.PoolStatusClustersPlugins`
        """
        self._plugins = plugins

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
        if not isinstance(other, PoolStatusClusters):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

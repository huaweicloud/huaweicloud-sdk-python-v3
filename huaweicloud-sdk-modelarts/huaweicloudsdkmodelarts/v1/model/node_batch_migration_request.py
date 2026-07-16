# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class NodeBatchMigrationRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'migrate_node_names': 'list[str]',
        'from_cluster_name': 'str',
        'to_cluster_name': 'str',
        'to_pool_name': 'str',
        'resource_spec': 'MigrateResourceSpec'
    }

    attribute_map = {
        'migrate_node_names': 'migrateNodeNames',
        'from_cluster_name': 'fromClusterName',
        'to_cluster_name': 'toClusterName',
        'to_pool_name': 'toPoolName',
        'resource_spec': 'resourceSpec'
    }

    def __init__(self, migrate_node_names=None, from_cluster_name=None, to_cluster_name=None, to_pool_name=None, resource_spec=None):
        r"""NodeBatchMigrationRequest

        The model defined in huaweicloud sdk

        :param migrate_node_names: **参数解释**：待迁移的节点名称列表。 **约束限制**：不涉及。
        :type migrate_node_names: list[str]
        :param from_cluster_name: **参数解释**：迁移起始集群名称。 专属算力资源时该字段与源资源池名称相同，取自源资源池metadata.name字段的值； 轻量算力集群时该字段取自迁移节点metadata.labels[os.modelarts.node/cluster]字段的值。 **约束限制**：不涉及。 **取值范围**：不涉及。 **默认取值**：不涉及。
        :type from_cluster_name: str
        :param to_cluster_name: **参数解释**：迁移目标集群名称。 专属算力资源时该字段与源资源池名称相同，取自目标资源池metadata.name字段的值； 轻量算力集群时该字段取自目标资源池内节点metadata.labels[os.modelarts.node/cluster]字段的值。 **约束限制**：不涉及。 **取值范围**：不涉及。 **默认取值**：不涉及。
        :type to_cluster_name: str
        :param to_pool_name: **参数解释**：迁移目标资源池名称。该字段取自目标资源池metadata.name字段的值。 **约束限制**：不涉及。 **取值范围**：不涉及。 **默认取值**：不涉及。
        :type to_pool_name: str
        :param resource_spec: 
        :type resource_spec: :class:`huaweicloudsdkmodelarts.v1.MigrateResourceSpec`
        """
        
        

        self._migrate_node_names = None
        self._from_cluster_name = None
        self._to_cluster_name = None
        self._to_pool_name = None
        self._resource_spec = None
        self.discriminator = None

        self.migrate_node_names = migrate_node_names
        self.from_cluster_name = from_cluster_name
        self.to_cluster_name = to_cluster_name
        if to_pool_name is not None:
            self.to_pool_name = to_pool_name
        if resource_spec is not None:
            self.resource_spec = resource_spec

    @property
    def migrate_node_names(self):
        r"""Gets the migrate_node_names of this NodeBatchMigrationRequest.

        **参数解释**：待迁移的节点名称列表。 **约束限制**：不涉及。

        :return: The migrate_node_names of this NodeBatchMigrationRequest.
        :rtype: list[str]
        """
        return self._migrate_node_names

    @migrate_node_names.setter
    def migrate_node_names(self, migrate_node_names):
        r"""Sets the migrate_node_names of this NodeBatchMigrationRequest.

        **参数解释**：待迁移的节点名称列表。 **约束限制**：不涉及。

        :param migrate_node_names: The migrate_node_names of this NodeBatchMigrationRequest.
        :type migrate_node_names: list[str]
        """
        self._migrate_node_names = migrate_node_names

    @property
    def from_cluster_name(self):
        r"""Gets the from_cluster_name of this NodeBatchMigrationRequest.

        **参数解释**：迁移起始集群名称。 专属算力资源时该字段与源资源池名称相同，取自源资源池metadata.name字段的值； 轻量算力集群时该字段取自迁移节点metadata.labels[os.modelarts.node/cluster]字段的值。 **约束限制**：不涉及。 **取值范围**：不涉及。 **默认取值**：不涉及。

        :return: The from_cluster_name of this NodeBatchMigrationRequest.
        :rtype: str
        """
        return self._from_cluster_name

    @from_cluster_name.setter
    def from_cluster_name(self, from_cluster_name):
        r"""Sets the from_cluster_name of this NodeBatchMigrationRequest.

        **参数解释**：迁移起始集群名称。 专属算力资源时该字段与源资源池名称相同，取自源资源池metadata.name字段的值； 轻量算力集群时该字段取自迁移节点metadata.labels[os.modelarts.node/cluster]字段的值。 **约束限制**：不涉及。 **取值范围**：不涉及。 **默认取值**：不涉及。

        :param from_cluster_name: The from_cluster_name of this NodeBatchMigrationRequest.
        :type from_cluster_name: str
        """
        self._from_cluster_name = from_cluster_name

    @property
    def to_cluster_name(self):
        r"""Gets the to_cluster_name of this NodeBatchMigrationRequest.

        **参数解释**：迁移目标集群名称。 专属算力资源时该字段与源资源池名称相同，取自目标资源池metadata.name字段的值； 轻量算力集群时该字段取自目标资源池内节点metadata.labels[os.modelarts.node/cluster]字段的值。 **约束限制**：不涉及。 **取值范围**：不涉及。 **默认取值**：不涉及。

        :return: The to_cluster_name of this NodeBatchMigrationRequest.
        :rtype: str
        """
        return self._to_cluster_name

    @to_cluster_name.setter
    def to_cluster_name(self, to_cluster_name):
        r"""Sets the to_cluster_name of this NodeBatchMigrationRequest.

        **参数解释**：迁移目标集群名称。 专属算力资源时该字段与源资源池名称相同，取自目标资源池metadata.name字段的值； 轻量算力集群时该字段取自目标资源池内节点metadata.labels[os.modelarts.node/cluster]字段的值。 **约束限制**：不涉及。 **取值范围**：不涉及。 **默认取值**：不涉及。

        :param to_cluster_name: The to_cluster_name of this NodeBatchMigrationRequest.
        :type to_cluster_name: str
        """
        self._to_cluster_name = to_cluster_name

    @property
    def to_pool_name(self):
        r"""Gets the to_pool_name of this NodeBatchMigrationRequest.

        **参数解释**：迁移目标资源池名称。该字段取自目标资源池metadata.name字段的值。 **约束限制**：不涉及。 **取值范围**：不涉及。 **默认取值**：不涉及。

        :return: The to_pool_name of this NodeBatchMigrationRequest.
        :rtype: str
        """
        return self._to_pool_name

    @to_pool_name.setter
    def to_pool_name(self, to_pool_name):
        r"""Sets the to_pool_name of this NodeBatchMigrationRequest.

        **参数解释**：迁移目标资源池名称。该字段取自目标资源池metadata.name字段的值。 **约束限制**：不涉及。 **取值范围**：不涉及。 **默认取值**：不涉及。

        :param to_pool_name: The to_pool_name of this NodeBatchMigrationRequest.
        :type to_pool_name: str
        """
        self._to_pool_name = to_pool_name

    @property
    def resource_spec(self):
        r"""Gets the resource_spec of this NodeBatchMigrationRequest.

        :return: The resource_spec of this NodeBatchMigrationRequest.
        :rtype: :class:`huaweicloudsdkmodelarts.v1.MigrateResourceSpec`
        """
        return self._resource_spec

    @resource_spec.setter
    def resource_spec(self, resource_spec):
        r"""Sets the resource_spec of this NodeBatchMigrationRequest.

        :param resource_spec: The resource_spec of this NodeBatchMigrationRequest.
        :type resource_spec: :class:`huaweicloudsdkmodelarts.v1.MigrateResourceSpec`
        """
        self._resource_spec = resource_spec

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
        if not isinstance(other, NodeBatchMigrationRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

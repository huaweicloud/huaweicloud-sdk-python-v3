# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class MigrateResourceSpec:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'flavor': 'str',
        'creating_step': 'CreatingStep',
        'node_pool': 'str',
        'root_volume': 'RootVolume',
        'data_volumes': 'list[DataVolumeItem]',
        'volume_group_configs': 'list[VolumeGroupConfig]',
        'labels': 'dict(str, str)',
        'taints': 'list[Taints]',
        'tags': 'list[UserTags]',
        'network': 'NodeNetwork',
        'extend_params': 'ResourceExtendParams'
    }

    attribute_map = {
        'flavor': 'flavor',
        'creating_step': 'creatingStep',
        'node_pool': 'nodePool',
        'root_volume': 'rootVolume',
        'data_volumes': 'dataVolumes',
        'volume_group_configs': 'volumeGroupConfigs',
        'labels': 'labels',
        'taints': 'taints',
        'tags': 'tags',
        'network': 'network',
        'extend_params': 'extendParams'
    }

    def __init__(self, flavor=None, creating_step=None, node_pool=None, root_volume=None, data_volumes=None, volume_group_configs=None, labels=None, taints=None, tags=None, network=None, extend_params=None):
        r"""MigrateResourceSpec

        The model defined in huaweicloud sdk

        :param flavor: **参数解释**：资源规格名称，跨资源池迁移时该参数必传。 **约束限制**：不涉及。 **取值范围**：不涉及。 **默认取值**：不涉及。
        :type flavor: str
        :param creating_step: 
        :type creating_step: :class:`huaweicloudsdkmodelarts.v1.CreatingStep`
        :param node_pool: **参数解释**：资源迁移的目标节点池名称。 **约束限制**：不涉及。 **取值范围**：不涉及。 **默认取值**：不涉及。
        :type node_pool: str
        :param root_volume: 
        :type root_volume: :class:`huaweicloudsdkmodelarts.v1.RootVolume`
        :param data_volumes: **参数解释**：目标节点池的数据盘盘信息，新建节点池时有效。 **约束限制**：不涉及。
        :type data_volumes: list[:class:`huaweicloudsdkmodelarts.v1.DataVolumeItem`]
        :param volume_group_configs: **参数解释**：磁盘高级配置。存在自定义数据盘时必须指定对应的高级配置，新建节点池时有效。 **约束限制**：不涉及。
        :type volume_group_configs: list[:class:`huaweicloudsdkmodelarts.v1.VolumeGroupConfig`]
        :param labels: **参数解释**：k8s标签，格式为key/value键值对，非特权池不能指定。新建节点池时有效。 **约束限制**：不涉及。
        :type labels: dict(str, str)
        :param taints: **参数解释**：支持给创建出来的节点加taints来设置反亲和性，非特权池不能指定。新建节点池时有效。 **约束限制**：不涉及。
        :type taints: list[:class:`huaweicloudsdkmodelarts.v1.Taints`]
        :param tags: **参数解释**：资源标签。新建节点池时有效。 **约束限制**：不涉及。
        :type tags: list[:class:`huaweicloudsdkmodelarts.v1.UserTags`]
        :param network: 
        :type network: :class:`huaweicloudsdkmodelarts.v1.NodeNetwork`
        :param extend_params: 
        :type extend_params: :class:`huaweicloudsdkmodelarts.v1.ResourceExtendParams`
        """
        
        

        self._flavor = None
        self._creating_step = None
        self._node_pool = None
        self._root_volume = None
        self._data_volumes = None
        self._volume_group_configs = None
        self._labels = None
        self._taints = None
        self._tags = None
        self._network = None
        self._extend_params = None
        self.discriminator = None

        self.flavor = flavor
        if creating_step is not None:
            self.creating_step = creating_step
        if node_pool is not None:
            self.node_pool = node_pool
        if root_volume is not None:
            self.root_volume = root_volume
        if data_volumes is not None:
            self.data_volumes = data_volumes
        if volume_group_configs is not None:
            self.volume_group_configs = volume_group_configs
        if labels is not None:
            self.labels = labels
        if taints is not None:
            self.taints = taints
        if tags is not None:
            self.tags = tags
        if network is not None:
            self.network = network
        if extend_params is not None:
            self.extend_params = extend_params

    @property
    def flavor(self):
        r"""Gets the flavor of this MigrateResourceSpec.

        **参数解释**：资源规格名称，跨资源池迁移时该参数必传。 **约束限制**：不涉及。 **取值范围**：不涉及。 **默认取值**：不涉及。

        :return: The flavor of this MigrateResourceSpec.
        :rtype: str
        """
        return self._flavor

    @flavor.setter
    def flavor(self, flavor):
        r"""Sets the flavor of this MigrateResourceSpec.

        **参数解释**：资源规格名称，跨资源池迁移时该参数必传。 **约束限制**：不涉及。 **取值范围**：不涉及。 **默认取值**：不涉及。

        :param flavor: The flavor of this MigrateResourceSpec.
        :type flavor: str
        """
        self._flavor = flavor

    @property
    def creating_step(self):
        r"""Gets the creating_step of this MigrateResourceSpec.

        :return: The creating_step of this MigrateResourceSpec.
        :rtype: :class:`huaweicloudsdkmodelarts.v1.CreatingStep`
        """
        return self._creating_step

    @creating_step.setter
    def creating_step(self, creating_step):
        r"""Sets the creating_step of this MigrateResourceSpec.

        :param creating_step: The creating_step of this MigrateResourceSpec.
        :type creating_step: :class:`huaweicloudsdkmodelarts.v1.CreatingStep`
        """
        self._creating_step = creating_step

    @property
    def node_pool(self):
        r"""Gets the node_pool of this MigrateResourceSpec.

        **参数解释**：资源迁移的目标节点池名称。 **约束限制**：不涉及。 **取值范围**：不涉及。 **默认取值**：不涉及。

        :return: The node_pool of this MigrateResourceSpec.
        :rtype: str
        """
        return self._node_pool

    @node_pool.setter
    def node_pool(self, node_pool):
        r"""Sets the node_pool of this MigrateResourceSpec.

        **参数解释**：资源迁移的目标节点池名称。 **约束限制**：不涉及。 **取值范围**：不涉及。 **默认取值**：不涉及。

        :param node_pool: The node_pool of this MigrateResourceSpec.
        :type node_pool: str
        """
        self._node_pool = node_pool

    @property
    def root_volume(self):
        r"""Gets the root_volume of this MigrateResourceSpec.

        :return: The root_volume of this MigrateResourceSpec.
        :rtype: :class:`huaweicloudsdkmodelarts.v1.RootVolume`
        """
        return self._root_volume

    @root_volume.setter
    def root_volume(self, root_volume):
        r"""Sets the root_volume of this MigrateResourceSpec.

        :param root_volume: The root_volume of this MigrateResourceSpec.
        :type root_volume: :class:`huaweicloudsdkmodelarts.v1.RootVolume`
        """
        self._root_volume = root_volume

    @property
    def data_volumes(self):
        r"""Gets the data_volumes of this MigrateResourceSpec.

        **参数解释**：目标节点池的数据盘盘信息，新建节点池时有效。 **约束限制**：不涉及。

        :return: The data_volumes of this MigrateResourceSpec.
        :rtype: list[:class:`huaweicloudsdkmodelarts.v1.DataVolumeItem`]
        """
        return self._data_volumes

    @data_volumes.setter
    def data_volumes(self, data_volumes):
        r"""Sets the data_volumes of this MigrateResourceSpec.

        **参数解释**：目标节点池的数据盘盘信息，新建节点池时有效。 **约束限制**：不涉及。

        :param data_volumes: The data_volumes of this MigrateResourceSpec.
        :type data_volumes: list[:class:`huaweicloudsdkmodelarts.v1.DataVolumeItem`]
        """
        self._data_volumes = data_volumes

    @property
    def volume_group_configs(self):
        r"""Gets the volume_group_configs of this MigrateResourceSpec.

        **参数解释**：磁盘高级配置。存在自定义数据盘时必须指定对应的高级配置，新建节点池时有效。 **约束限制**：不涉及。

        :return: The volume_group_configs of this MigrateResourceSpec.
        :rtype: list[:class:`huaweicloudsdkmodelarts.v1.VolumeGroupConfig`]
        """
        return self._volume_group_configs

    @volume_group_configs.setter
    def volume_group_configs(self, volume_group_configs):
        r"""Sets the volume_group_configs of this MigrateResourceSpec.

        **参数解释**：磁盘高级配置。存在自定义数据盘时必须指定对应的高级配置，新建节点池时有效。 **约束限制**：不涉及。

        :param volume_group_configs: The volume_group_configs of this MigrateResourceSpec.
        :type volume_group_configs: list[:class:`huaweicloudsdkmodelarts.v1.VolumeGroupConfig`]
        """
        self._volume_group_configs = volume_group_configs

    @property
    def labels(self):
        r"""Gets the labels of this MigrateResourceSpec.

        **参数解释**：k8s标签，格式为key/value键值对，非特权池不能指定。新建节点池时有效。 **约束限制**：不涉及。

        :return: The labels of this MigrateResourceSpec.
        :rtype: dict(str, str)
        """
        return self._labels

    @labels.setter
    def labels(self, labels):
        r"""Sets the labels of this MigrateResourceSpec.

        **参数解释**：k8s标签，格式为key/value键值对，非特权池不能指定。新建节点池时有效。 **约束限制**：不涉及。

        :param labels: The labels of this MigrateResourceSpec.
        :type labels: dict(str, str)
        """
        self._labels = labels

    @property
    def taints(self):
        r"""Gets the taints of this MigrateResourceSpec.

        **参数解释**：支持给创建出来的节点加taints来设置反亲和性，非特权池不能指定。新建节点池时有效。 **约束限制**：不涉及。

        :return: The taints of this MigrateResourceSpec.
        :rtype: list[:class:`huaweicloudsdkmodelarts.v1.Taints`]
        """
        return self._taints

    @taints.setter
    def taints(self, taints):
        r"""Sets the taints of this MigrateResourceSpec.

        **参数解释**：支持给创建出来的节点加taints来设置反亲和性，非特权池不能指定。新建节点池时有效。 **约束限制**：不涉及。

        :param taints: The taints of this MigrateResourceSpec.
        :type taints: list[:class:`huaweicloudsdkmodelarts.v1.Taints`]
        """
        self._taints = taints

    @property
    def tags(self):
        r"""Gets the tags of this MigrateResourceSpec.

        **参数解释**：资源标签。新建节点池时有效。 **约束限制**：不涉及。

        :return: The tags of this MigrateResourceSpec.
        :rtype: list[:class:`huaweicloudsdkmodelarts.v1.UserTags`]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        r"""Sets the tags of this MigrateResourceSpec.

        **参数解释**：资源标签。新建节点池时有效。 **约束限制**：不涉及。

        :param tags: The tags of this MigrateResourceSpec.
        :type tags: list[:class:`huaweicloudsdkmodelarts.v1.UserTags`]
        """
        self._tags = tags

    @property
    def network(self):
        r"""Gets the network of this MigrateResourceSpec.

        :return: The network of this MigrateResourceSpec.
        :rtype: :class:`huaweicloudsdkmodelarts.v1.NodeNetwork`
        """
        return self._network

    @network.setter
    def network(self, network):
        r"""Sets the network of this MigrateResourceSpec.

        :param network: The network of this MigrateResourceSpec.
        :type network: :class:`huaweicloudsdkmodelarts.v1.NodeNetwork`
        """
        self._network = network

    @property
    def extend_params(self):
        r"""Gets the extend_params of this MigrateResourceSpec.

        :return: The extend_params of this MigrateResourceSpec.
        :rtype: :class:`huaweicloudsdkmodelarts.v1.ResourceExtendParams`
        """
        return self._extend_params

    @extend_params.setter
    def extend_params(self, extend_params):
        r"""Sets the extend_params of this MigrateResourceSpec.

        :param extend_params: The extend_params of this MigrateResourceSpec.
        :type extend_params: :class:`huaweicloudsdkmodelarts.v1.ResourceExtendParams`
        """
        self._extend_params = extend_params

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
        if not isinstance(other, MigrateResourceSpec):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

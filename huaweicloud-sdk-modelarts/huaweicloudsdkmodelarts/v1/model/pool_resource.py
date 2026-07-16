# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PoolResource:

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
        'count': 'int',
        'max_count': 'int',
        'azs': 'list[PoolNodeAz]',
        'node_pool': 'str',
        'taints': 'list[Taints]',
        'labels': 'dict(str, str)',
        'tags': 'list[UserTags]',
        'network': 'NodeNetwork',
        'extend_params': 'ResourceExtendParams',
        'creating_step': 'CreatingStep',
        'root_volume': 'RootVolume',
        'data_volumes': 'list[DataVolumeItem]',
        'volume_group_configs': 'list[VolumeGroupConfig]',
        'os': 'Os'
    }

    attribute_map = {
        'flavor': 'flavor',
        'count': 'count',
        'max_count': 'maxCount',
        'azs': 'azs',
        'node_pool': 'nodePool',
        'taints': 'taints',
        'labels': 'labels',
        'tags': 'tags',
        'network': 'network',
        'extend_params': 'extendParams',
        'creating_step': 'creatingStep',
        'root_volume': 'rootVolume',
        'data_volumes': 'dataVolumes',
        'volume_group_configs': 'volumeGroupConfigs',
        'os': 'os'
    }

    def __init__(self, flavor=None, count=None, max_count=None, azs=None, node_pool=None, taints=None, labels=None, tags=None, network=None, extend_params=None, creating_step=None, root_volume=None, data_volumes=None, volume_group_configs=None, os=None):
        r"""PoolResource

        The model defined in huaweicloud sdk

        :param flavor: **参数解释**：资源规格名称，比如：modelarts.vm.gpu.t4u8。 **取值范围**：不涉及。
        :type flavor: str
        :param count: **参数解释**：规格保障使用量。 **取值范围**：不涉及。
        :type count: int
        :param max_count: **参数解释**：资源规格的弹性使用量，物理池该值和count相同[，逻辑池该值大于等于count](tag:hcs,hcso)。 **取值范围**：不涉及。
        :type max_count: int
        :param azs: **参数解释**：资源池中节点的AZ信息。
        :type azs: list[:class:`huaweicloudsdkmodelarts.v1.PoolNodeAz`]
        :param node_pool: **参数解释**：节点池名称。比如：nodePool-1。 **取值范围**：不涉及。
        :type node_pool: str
        :param taints: **参数解释**：支持给创建出来的节点加taints来设置反亲和性，非特权池不能指定。
        :type taints: list[:class:`huaweicloudsdkmodelarts.v1.Taints`]
        :param labels: **参数解释**：k8s标签，格式为key/value键值对。
        :type labels: dict(str, str)
        :param tags: **参数解释**：资源标签，非特权池不能指定。
        :type tags: list[:class:`huaweicloudsdkmodelarts.v1.UserTags`]
        :param network: 
        :type network: :class:`huaweicloudsdkmodelarts.v1.NodeNetwork`
        :param extend_params: 
        :type extend_params: :class:`huaweicloudsdkmodelarts.v1.ResourceExtendParams`
        :param creating_step: 
        :type creating_step: :class:`huaweicloudsdkmodelarts.v1.CreatingStep`
        :param root_volume: 
        :type root_volume: :class:`huaweicloudsdkmodelarts.v1.RootVolume`
        :param data_volumes: **参数解释**：自定义数据盘（云硬盘）列表信息。
        :type data_volumes: list[:class:`huaweicloudsdkmodelarts.v1.DataVolumeItem`]
        :param volume_group_configs: **参数解释**：磁盘高级配置。存在自定义数据盘时必须指定对应的高级配置。
        :type volume_group_configs: list[:class:`huaweicloudsdkmodelarts.v1.VolumeGroupConfig`]
        :param os: 
        :type os: :class:`huaweicloudsdkmodelarts.v1.Os`
        """
        
        

        self._flavor = None
        self._count = None
        self._max_count = None
        self._azs = None
        self._node_pool = None
        self._taints = None
        self._labels = None
        self._tags = None
        self._network = None
        self._extend_params = None
        self._creating_step = None
        self._root_volume = None
        self._data_volumes = None
        self._volume_group_configs = None
        self._os = None
        self.discriminator = None

        self.flavor = flavor
        self.count = count
        self.max_count = max_count
        if azs is not None:
            self.azs = azs
        if node_pool is not None:
            self.node_pool = node_pool
        if taints is not None:
            self.taints = taints
        if labels is not None:
            self.labels = labels
        if tags is not None:
            self.tags = tags
        if network is not None:
            self.network = network
        if extend_params is not None:
            self.extend_params = extend_params
        if creating_step is not None:
            self.creating_step = creating_step
        if root_volume is not None:
            self.root_volume = root_volume
        if data_volumes is not None:
            self.data_volumes = data_volumes
        if volume_group_configs is not None:
            self.volume_group_configs = volume_group_configs
        if os is not None:
            self.os = os

    @property
    def flavor(self):
        r"""Gets the flavor of this PoolResource.

        **参数解释**：资源规格名称，比如：modelarts.vm.gpu.t4u8。 **取值范围**：不涉及。

        :return: The flavor of this PoolResource.
        :rtype: str
        """
        return self._flavor

    @flavor.setter
    def flavor(self, flavor):
        r"""Sets the flavor of this PoolResource.

        **参数解释**：资源规格名称，比如：modelarts.vm.gpu.t4u8。 **取值范围**：不涉及。

        :param flavor: The flavor of this PoolResource.
        :type flavor: str
        """
        self._flavor = flavor

    @property
    def count(self):
        r"""Gets the count of this PoolResource.

        **参数解释**：规格保障使用量。 **取值范围**：不涉及。

        :return: The count of this PoolResource.
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        r"""Sets the count of this PoolResource.

        **参数解释**：规格保障使用量。 **取值范围**：不涉及。

        :param count: The count of this PoolResource.
        :type count: int
        """
        self._count = count

    @property
    def max_count(self):
        r"""Gets the max_count of this PoolResource.

        **参数解释**：资源规格的弹性使用量，物理池该值和count相同[，逻辑池该值大于等于count](tag:hcs,hcso)。 **取值范围**：不涉及。

        :return: The max_count of this PoolResource.
        :rtype: int
        """
        return self._max_count

    @max_count.setter
    def max_count(self, max_count):
        r"""Sets the max_count of this PoolResource.

        **参数解释**：资源规格的弹性使用量，物理池该值和count相同[，逻辑池该值大于等于count](tag:hcs,hcso)。 **取值范围**：不涉及。

        :param max_count: The max_count of this PoolResource.
        :type max_count: int
        """
        self._max_count = max_count

    @property
    def azs(self):
        r"""Gets the azs of this PoolResource.

        **参数解释**：资源池中节点的AZ信息。

        :return: The azs of this PoolResource.
        :rtype: list[:class:`huaweicloudsdkmodelarts.v1.PoolNodeAz`]
        """
        return self._azs

    @azs.setter
    def azs(self, azs):
        r"""Sets the azs of this PoolResource.

        **参数解释**：资源池中节点的AZ信息。

        :param azs: The azs of this PoolResource.
        :type azs: list[:class:`huaweicloudsdkmodelarts.v1.PoolNodeAz`]
        """
        self._azs = azs

    @property
    def node_pool(self):
        r"""Gets the node_pool of this PoolResource.

        **参数解释**：节点池名称。比如：nodePool-1。 **取值范围**：不涉及。

        :return: The node_pool of this PoolResource.
        :rtype: str
        """
        return self._node_pool

    @node_pool.setter
    def node_pool(self, node_pool):
        r"""Sets the node_pool of this PoolResource.

        **参数解释**：节点池名称。比如：nodePool-1。 **取值范围**：不涉及。

        :param node_pool: The node_pool of this PoolResource.
        :type node_pool: str
        """
        self._node_pool = node_pool

    @property
    def taints(self):
        r"""Gets the taints of this PoolResource.

        **参数解释**：支持给创建出来的节点加taints来设置反亲和性，非特权池不能指定。

        :return: The taints of this PoolResource.
        :rtype: list[:class:`huaweicloudsdkmodelarts.v1.Taints`]
        """
        return self._taints

    @taints.setter
    def taints(self, taints):
        r"""Sets the taints of this PoolResource.

        **参数解释**：支持给创建出来的节点加taints来设置反亲和性，非特权池不能指定。

        :param taints: The taints of this PoolResource.
        :type taints: list[:class:`huaweicloudsdkmodelarts.v1.Taints`]
        """
        self._taints = taints

    @property
    def labels(self):
        r"""Gets the labels of this PoolResource.

        **参数解释**：k8s标签，格式为key/value键值对。

        :return: The labels of this PoolResource.
        :rtype: dict(str, str)
        """
        return self._labels

    @labels.setter
    def labels(self, labels):
        r"""Sets the labels of this PoolResource.

        **参数解释**：k8s标签，格式为key/value键值对。

        :param labels: The labels of this PoolResource.
        :type labels: dict(str, str)
        """
        self._labels = labels

    @property
    def tags(self):
        r"""Gets the tags of this PoolResource.

        **参数解释**：资源标签，非特权池不能指定。

        :return: The tags of this PoolResource.
        :rtype: list[:class:`huaweicloudsdkmodelarts.v1.UserTags`]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        r"""Sets the tags of this PoolResource.

        **参数解释**：资源标签，非特权池不能指定。

        :param tags: The tags of this PoolResource.
        :type tags: list[:class:`huaweicloudsdkmodelarts.v1.UserTags`]
        """
        self._tags = tags

    @property
    def network(self):
        r"""Gets the network of this PoolResource.

        :return: The network of this PoolResource.
        :rtype: :class:`huaweicloudsdkmodelarts.v1.NodeNetwork`
        """
        return self._network

    @network.setter
    def network(self, network):
        r"""Sets the network of this PoolResource.

        :param network: The network of this PoolResource.
        :type network: :class:`huaweicloudsdkmodelarts.v1.NodeNetwork`
        """
        self._network = network

    @property
    def extend_params(self):
        r"""Gets the extend_params of this PoolResource.

        :return: The extend_params of this PoolResource.
        :rtype: :class:`huaweicloudsdkmodelarts.v1.ResourceExtendParams`
        """
        return self._extend_params

    @extend_params.setter
    def extend_params(self, extend_params):
        r"""Sets the extend_params of this PoolResource.

        :param extend_params: The extend_params of this PoolResource.
        :type extend_params: :class:`huaweicloudsdkmodelarts.v1.ResourceExtendParams`
        """
        self._extend_params = extend_params

    @property
    def creating_step(self):
        r"""Gets the creating_step of this PoolResource.

        :return: The creating_step of this PoolResource.
        :rtype: :class:`huaweicloudsdkmodelarts.v1.CreatingStep`
        """
        return self._creating_step

    @creating_step.setter
    def creating_step(self, creating_step):
        r"""Sets the creating_step of this PoolResource.

        :param creating_step: The creating_step of this PoolResource.
        :type creating_step: :class:`huaweicloudsdkmodelarts.v1.CreatingStep`
        """
        self._creating_step = creating_step

    @property
    def root_volume(self):
        r"""Gets the root_volume of this PoolResource.

        :return: The root_volume of this PoolResource.
        :rtype: :class:`huaweicloudsdkmodelarts.v1.RootVolume`
        """
        return self._root_volume

    @root_volume.setter
    def root_volume(self, root_volume):
        r"""Sets the root_volume of this PoolResource.

        :param root_volume: The root_volume of this PoolResource.
        :type root_volume: :class:`huaweicloudsdkmodelarts.v1.RootVolume`
        """
        self._root_volume = root_volume

    @property
    def data_volumes(self):
        r"""Gets the data_volumes of this PoolResource.

        **参数解释**：自定义数据盘（云硬盘）列表信息。

        :return: The data_volumes of this PoolResource.
        :rtype: list[:class:`huaweicloudsdkmodelarts.v1.DataVolumeItem`]
        """
        return self._data_volumes

    @data_volumes.setter
    def data_volumes(self, data_volumes):
        r"""Sets the data_volumes of this PoolResource.

        **参数解释**：自定义数据盘（云硬盘）列表信息。

        :param data_volumes: The data_volumes of this PoolResource.
        :type data_volumes: list[:class:`huaweicloudsdkmodelarts.v1.DataVolumeItem`]
        """
        self._data_volumes = data_volumes

    @property
    def volume_group_configs(self):
        r"""Gets the volume_group_configs of this PoolResource.

        **参数解释**：磁盘高级配置。存在自定义数据盘时必须指定对应的高级配置。

        :return: The volume_group_configs of this PoolResource.
        :rtype: list[:class:`huaweicloudsdkmodelarts.v1.VolumeGroupConfig`]
        """
        return self._volume_group_configs

    @volume_group_configs.setter
    def volume_group_configs(self, volume_group_configs):
        r"""Sets the volume_group_configs of this PoolResource.

        **参数解释**：磁盘高级配置。存在自定义数据盘时必须指定对应的高级配置。

        :param volume_group_configs: The volume_group_configs of this PoolResource.
        :type volume_group_configs: list[:class:`huaweicloudsdkmodelarts.v1.VolumeGroupConfig`]
        """
        self._volume_group_configs = volume_group_configs

    @property
    def os(self):
        r"""Gets the os of this PoolResource.

        :return: The os of this PoolResource.
        :rtype: :class:`huaweicloudsdkmodelarts.v1.Os`
        """
        return self._os

    @os.setter
    def os(self, os):
        r"""Sets the os of this PoolResource.

        :param os: The os of this PoolResource.
        :type os: :class:`huaweicloudsdkmodelarts.v1.Os`
        """
        self._os = os

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
        if not isinstance(other, PoolResource):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

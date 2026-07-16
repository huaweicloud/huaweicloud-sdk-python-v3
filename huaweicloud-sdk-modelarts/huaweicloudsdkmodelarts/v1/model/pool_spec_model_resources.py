# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PoolSpecModelResources:

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
        'extend_params': 'PoolSpecModelExtendParams',
        'os': 'Os',
        'data_volumes': 'PoolSpecModelDataVolumes',
        'volume_group_configs': 'PoolSpecModelVolumeGroupConfigs'
    }

    attribute_map = {
        'flavor': 'flavor',
        'count': 'count',
        'max_count': 'maxCount',
        'azs': 'azs',
        'extend_params': 'extendParams',
        'os': 'os',
        'data_volumes': 'dataVolumes',
        'volume_group_configs': 'volumeGroupConfigs'
    }

    def __init__(self, flavor=None, count=None, max_count=None, azs=None, extend_params=None, os=None, data_volumes=None, volume_group_configs=None):
        r"""PoolSpecModelResources

        The model defined in huaweicloud sdk

        :param flavor: **参数解释**：资源规格ID。 **取值范围**：不涉及。
        :type flavor: str
        :param count: **参数解释**：资源池中资源规格实例数量。 **取值范围**：不涉及。
        :type count: int
        :param max_count: **参数解释**：资源规格的弹性资源量。物理池中该值和count必须一致。 **取值范围**：不涉及。
        :type max_count: int
        :param azs: **参数解释**：资源池中期望创建的资源规格实例的az分布。
        :type azs: list[:class:`huaweicloudsdkmodelarts.v1.PoolNodeAz`]
        :param extend_params: 
        :type extend_params: :class:`huaweicloudsdkmodelarts.v1.PoolSpecModelExtendParams`
        :param os: 
        :type os: :class:`huaweicloudsdkmodelarts.v1.Os`
        :param data_volumes: 
        :type data_volumes: :class:`huaweicloudsdkmodelarts.v1.PoolSpecModelDataVolumes`
        :param volume_group_configs: 
        :type volume_group_configs: :class:`huaweicloudsdkmodelarts.v1.PoolSpecModelVolumeGroupConfigs`
        """
        
        

        self._flavor = None
        self._count = None
        self._max_count = None
        self._azs = None
        self._extend_params = None
        self._os = None
        self._data_volumes = None
        self._volume_group_configs = None
        self.discriminator = None

        if flavor is not None:
            self.flavor = flavor
        if count is not None:
            self.count = count
        if max_count is not None:
            self.max_count = max_count
        if azs is not None:
            self.azs = azs
        if extend_params is not None:
            self.extend_params = extend_params
        if os is not None:
            self.os = os
        if data_volumes is not None:
            self.data_volumes = data_volumes
        if volume_group_configs is not None:
            self.volume_group_configs = volume_group_configs

    @property
    def flavor(self):
        r"""Gets the flavor of this PoolSpecModelResources.

        **参数解释**：资源规格ID。 **取值范围**：不涉及。

        :return: The flavor of this PoolSpecModelResources.
        :rtype: str
        """
        return self._flavor

    @flavor.setter
    def flavor(self, flavor):
        r"""Sets the flavor of this PoolSpecModelResources.

        **参数解释**：资源规格ID。 **取值范围**：不涉及。

        :param flavor: The flavor of this PoolSpecModelResources.
        :type flavor: str
        """
        self._flavor = flavor

    @property
    def count(self):
        r"""Gets the count of this PoolSpecModelResources.

        **参数解释**：资源池中资源规格实例数量。 **取值范围**：不涉及。

        :return: The count of this PoolSpecModelResources.
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        r"""Sets the count of this PoolSpecModelResources.

        **参数解释**：资源池中资源规格实例数量。 **取值范围**：不涉及。

        :param count: The count of this PoolSpecModelResources.
        :type count: int
        """
        self._count = count

    @property
    def max_count(self):
        r"""Gets the max_count of this PoolSpecModelResources.

        **参数解释**：资源规格的弹性资源量。物理池中该值和count必须一致。 **取值范围**：不涉及。

        :return: The max_count of this PoolSpecModelResources.
        :rtype: int
        """
        return self._max_count

    @max_count.setter
    def max_count(self, max_count):
        r"""Sets the max_count of this PoolSpecModelResources.

        **参数解释**：资源规格的弹性资源量。物理池中该值和count必须一致。 **取值范围**：不涉及。

        :param max_count: The max_count of this PoolSpecModelResources.
        :type max_count: int
        """
        self._max_count = max_count

    @property
    def azs(self):
        r"""Gets the azs of this PoolSpecModelResources.

        **参数解释**：资源池中期望创建的资源规格实例的az分布。

        :return: The azs of this PoolSpecModelResources.
        :rtype: list[:class:`huaweicloudsdkmodelarts.v1.PoolNodeAz`]
        """
        return self._azs

    @azs.setter
    def azs(self, azs):
        r"""Sets the azs of this PoolSpecModelResources.

        **参数解释**：资源池中期望创建的资源规格实例的az分布。

        :param azs: The azs of this PoolSpecModelResources.
        :type azs: list[:class:`huaweicloudsdkmodelarts.v1.PoolNodeAz`]
        """
        self._azs = azs

    @property
    def extend_params(self):
        r"""Gets the extend_params of this PoolSpecModelResources.

        :return: The extend_params of this PoolSpecModelResources.
        :rtype: :class:`huaweicloudsdkmodelarts.v1.PoolSpecModelExtendParams`
        """
        return self._extend_params

    @extend_params.setter
    def extend_params(self, extend_params):
        r"""Sets the extend_params of this PoolSpecModelResources.

        :param extend_params: The extend_params of this PoolSpecModelResources.
        :type extend_params: :class:`huaweicloudsdkmodelarts.v1.PoolSpecModelExtendParams`
        """
        self._extend_params = extend_params

    @property
    def os(self):
        r"""Gets the os of this PoolSpecModelResources.

        :return: The os of this PoolSpecModelResources.
        :rtype: :class:`huaweicloudsdkmodelarts.v1.Os`
        """
        return self._os

    @os.setter
    def os(self, os):
        r"""Sets the os of this PoolSpecModelResources.

        :param os: The os of this PoolSpecModelResources.
        :type os: :class:`huaweicloudsdkmodelarts.v1.Os`
        """
        self._os = os

    @property
    def data_volumes(self):
        r"""Gets the data_volumes of this PoolSpecModelResources.

        :return: The data_volumes of this PoolSpecModelResources.
        :rtype: :class:`huaweicloudsdkmodelarts.v1.PoolSpecModelDataVolumes`
        """
        return self._data_volumes

    @data_volumes.setter
    def data_volumes(self, data_volumes):
        r"""Sets the data_volumes of this PoolSpecModelResources.

        :param data_volumes: The data_volumes of this PoolSpecModelResources.
        :type data_volumes: :class:`huaweicloudsdkmodelarts.v1.PoolSpecModelDataVolumes`
        """
        self._data_volumes = data_volumes

    @property
    def volume_group_configs(self):
        r"""Gets the volume_group_configs of this PoolSpecModelResources.

        :return: The volume_group_configs of this PoolSpecModelResources.
        :rtype: :class:`huaweicloudsdkmodelarts.v1.PoolSpecModelVolumeGroupConfigs`
        """
        return self._volume_group_configs

    @volume_group_configs.setter
    def volume_group_configs(self, volume_group_configs):
        r"""Sets the volume_group_configs of this PoolSpecModelResources.

        :param volume_group_configs: The volume_group_configs of this PoolSpecModelResources.
        :type volume_group_configs: :class:`huaweicloudsdkmodelarts.v1.PoolSpecModelVolumeGroupConfigs`
        """
        self._volume_group_configs = volume_group_configs

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
        if not isinstance(other, PoolSpecModelResources):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

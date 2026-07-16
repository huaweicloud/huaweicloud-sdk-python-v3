# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PoolSpecModelVolumeGroupConfigs:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'volume_group': 'str',
        'docker_thin_pool': 'int',
        'lvm_config': 'PoolSpecModelVolumeGroupConfigsLvmConfig'
    }

    attribute_map = {
        'volume_group': 'volumeGroup',
        'docker_thin_pool': 'dockerThinPool',
        'lvm_config': 'lvmConfig'
    }

    def __init__(self, volume_group=None, docker_thin_pool=None, lvm_config=None):
        r"""PoolSpecModelVolumeGroupConfigs

        The model defined in huaweicloud sdk

        :param volume_group: **参数解释**：磁盘分组名称。作为dataVolumes中volumeGroup的索引。 **取值范围**：不涉及。
        :type volume_group: str
        :param docker_thin_pool: **参数解释**：资源池节点容器盘占数据盘的百分比。仅磁盘分组名称为vgpaas时，即容器盘，才可指定此参数。 **取值范围**：不涉及。
        :type docker_thin_pool: int
        :param lvm_config: 
        :type lvm_config: :class:`huaweicloudsdkmodelarts.v1.PoolSpecModelVolumeGroupConfigsLvmConfig`
        """
        
        

        self._volume_group = None
        self._docker_thin_pool = None
        self._lvm_config = None
        self.discriminator = None

        if volume_group is not None:
            self.volume_group = volume_group
        if docker_thin_pool is not None:
            self.docker_thin_pool = docker_thin_pool
        if lvm_config is not None:
            self.lvm_config = lvm_config

    @property
    def volume_group(self):
        r"""Gets the volume_group of this PoolSpecModelVolumeGroupConfigs.

        **参数解释**：磁盘分组名称。作为dataVolumes中volumeGroup的索引。 **取值范围**：不涉及。

        :return: The volume_group of this PoolSpecModelVolumeGroupConfigs.
        :rtype: str
        """
        return self._volume_group

    @volume_group.setter
    def volume_group(self, volume_group):
        r"""Sets the volume_group of this PoolSpecModelVolumeGroupConfigs.

        **参数解释**：磁盘分组名称。作为dataVolumes中volumeGroup的索引。 **取值范围**：不涉及。

        :param volume_group: The volume_group of this PoolSpecModelVolumeGroupConfigs.
        :type volume_group: str
        """
        self._volume_group = volume_group

    @property
    def docker_thin_pool(self):
        r"""Gets the docker_thin_pool of this PoolSpecModelVolumeGroupConfigs.

        **参数解释**：资源池节点容器盘占数据盘的百分比。仅磁盘分组名称为vgpaas时，即容器盘，才可指定此参数。 **取值范围**：不涉及。

        :return: The docker_thin_pool of this PoolSpecModelVolumeGroupConfigs.
        :rtype: int
        """
        return self._docker_thin_pool

    @docker_thin_pool.setter
    def docker_thin_pool(self, docker_thin_pool):
        r"""Sets the docker_thin_pool of this PoolSpecModelVolumeGroupConfigs.

        **参数解释**：资源池节点容器盘占数据盘的百分比。仅磁盘分组名称为vgpaas时，即容器盘，才可指定此参数。 **取值范围**：不涉及。

        :param docker_thin_pool: The docker_thin_pool of this PoolSpecModelVolumeGroupConfigs.
        :type docker_thin_pool: int
        """
        self._docker_thin_pool = docker_thin_pool

    @property
    def lvm_config(self):
        r"""Gets the lvm_config of this PoolSpecModelVolumeGroupConfigs.

        :return: The lvm_config of this PoolSpecModelVolumeGroupConfigs.
        :rtype: :class:`huaweicloudsdkmodelarts.v1.PoolSpecModelVolumeGroupConfigsLvmConfig`
        """
        return self._lvm_config

    @lvm_config.setter
    def lvm_config(self, lvm_config):
        r"""Sets the lvm_config of this PoolSpecModelVolumeGroupConfigs.

        :param lvm_config: The lvm_config of this PoolSpecModelVolumeGroupConfigs.
        :type lvm_config: :class:`huaweicloudsdkmodelarts.v1.PoolSpecModelVolumeGroupConfigsLvmConfig`
        """
        self._lvm_config = lvm_config

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
        if not isinstance(other, PoolSpecModelVolumeGroupConfigs):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

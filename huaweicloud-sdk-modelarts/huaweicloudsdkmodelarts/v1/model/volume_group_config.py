# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class VolumeGroupConfig:

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
        'lvm_config': 'LvmConfig',
        'types': 'list[str]'
    }

    attribute_map = {
        'volume_group': 'volumeGroup',
        'docker_thin_pool': 'dockerThinPool',
        'lvm_config': 'lvmConfig',
        'types': 'types'
    }

    def __init__(self, volume_group=None, docker_thin_pool=None, lvm_config=None, types=None):
        r"""VolumeGroupConfig

        The model defined in huaweicloud sdk

        :param volume_group: **参数解释**：磁盘分组名称。作为dataVolumes中volumeGroup的索引。 **取值范围**：不涉及。
        :type volume_group: str
        :param docker_thin_pool: **参数解释**：资源池节点容器盘占数据盘的百分比。仅磁盘分组名称为vgpaas时，即容器盘，才可指定此参数。 **取值范围**：不涉及。
        :type docker_thin_pool: int
        :param lvm_config: 
        :type lvm_config: :class:`huaweicloudsdkmodelarts.v1.LvmConfig`
        :param types: **参数解释**：存储类型。可选项如下： - volume：云硬盘。当指定dataVolumes时，该值为缺省值。 - local：本地盘。使用本地盘必须指定该字段。
        :type types: list[str]
        """
        
        

        self._volume_group = None
        self._docker_thin_pool = None
        self._lvm_config = None
        self._types = None
        self.discriminator = None

        self.volume_group = volume_group
        if docker_thin_pool is not None:
            self.docker_thin_pool = docker_thin_pool
        if lvm_config is not None:
            self.lvm_config = lvm_config
        if types is not None:
            self.types = types

    @property
    def volume_group(self):
        r"""Gets the volume_group of this VolumeGroupConfig.

        **参数解释**：磁盘分组名称。作为dataVolumes中volumeGroup的索引。 **取值范围**：不涉及。

        :return: The volume_group of this VolumeGroupConfig.
        :rtype: str
        """
        return self._volume_group

    @volume_group.setter
    def volume_group(self, volume_group):
        r"""Sets the volume_group of this VolumeGroupConfig.

        **参数解释**：磁盘分组名称。作为dataVolumes中volumeGroup的索引。 **取值范围**：不涉及。

        :param volume_group: The volume_group of this VolumeGroupConfig.
        :type volume_group: str
        """
        self._volume_group = volume_group

    @property
    def docker_thin_pool(self):
        r"""Gets the docker_thin_pool of this VolumeGroupConfig.

        **参数解释**：资源池节点容器盘占数据盘的百分比。仅磁盘分组名称为vgpaas时，即容器盘，才可指定此参数。 **取值范围**：不涉及。

        :return: The docker_thin_pool of this VolumeGroupConfig.
        :rtype: int
        """
        return self._docker_thin_pool

    @docker_thin_pool.setter
    def docker_thin_pool(self, docker_thin_pool):
        r"""Sets the docker_thin_pool of this VolumeGroupConfig.

        **参数解释**：资源池节点容器盘占数据盘的百分比。仅磁盘分组名称为vgpaas时，即容器盘，才可指定此参数。 **取值范围**：不涉及。

        :param docker_thin_pool: The docker_thin_pool of this VolumeGroupConfig.
        :type docker_thin_pool: int
        """
        self._docker_thin_pool = docker_thin_pool

    @property
    def lvm_config(self):
        r"""Gets the lvm_config of this VolumeGroupConfig.

        :return: The lvm_config of this VolumeGroupConfig.
        :rtype: :class:`huaweicloudsdkmodelarts.v1.LvmConfig`
        """
        return self._lvm_config

    @lvm_config.setter
    def lvm_config(self, lvm_config):
        r"""Sets the lvm_config of this VolumeGroupConfig.

        :param lvm_config: The lvm_config of this VolumeGroupConfig.
        :type lvm_config: :class:`huaweicloudsdkmodelarts.v1.LvmConfig`
        """
        self._lvm_config = lvm_config

    @property
    def types(self):
        r"""Gets the types of this VolumeGroupConfig.

        **参数解释**：存储类型。可选项如下： - volume：云硬盘。当指定dataVolumes时，该值为缺省值。 - local：本地盘。使用本地盘必须指定该字段。

        :return: The types of this VolumeGroupConfig.
        :rtype: list[str]
        """
        return self._types

    @types.setter
    def types(self, types):
        r"""Sets the types of this VolumeGroupConfig.

        **参数解释**：存储类型。可选项如下： - volume：云硬盘。当指定dataVolumes时，该值为缺省值。 - local：本地盘。使用本地盘必须指定该字段。

        :param types: The types of this VolumeGroupConfig.
        :type types: list[str]
        """
        self._types = types

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
        if not isinstance(other, VolumeGroupConfig):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

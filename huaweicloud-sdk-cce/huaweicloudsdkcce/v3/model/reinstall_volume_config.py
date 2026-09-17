# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ReinstallVolumeConfig:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'lvm_config': 'str',
        'storage': 'Storage',
        'volume_reset_policy': 'str'
    }

    attribute_map = {
        'lvm_config': 'lvmConfig',
        'storage': 'storage',
        'volume_reset_policy': 'volumeResetPolicy'
    }

    def __init__(self, lvm_config=None, storage=None, volume_reset_policy=None):
        r"""ReinstallVolumeConfig

        The model defined in huaweicloud sdk

        :param lvm_config: **参数解释**: Docker数据盘配置项(已废弃)。  默认配置示例如下： &#x60;&#x60;&#x60; \&quot;lvmConfig\&quot;:\&quot;dockerThinpool&#x3D;vgpaas/90%VG;kubernetesLV&#x3D;vgpaas/10%VG;diskType&#x3D;evs;lvType&#x3D;linear\&quot; &#x60;&#x60;&#x60;  包含如下字段：   - userLV：用户空间的大小，示例格式：vgpaas/20%VG   - userPath：用户空间挂载路径，示例格式：/home/wqt-test   - diskType：磁盘类型，目前只有evs、hdd和ssd三种格式   - lvType：逻辑卷的类型，目前支持linear和striped两种，示例格式：striped   - dockerThinpool：Docker盘的空间大小，示例格式：vgpaas/60%VG   - kubernetesLV：Kubelet空间大小，示例格式：vgpaas/20%VG  **约束限制**: 不涉及 **取值范围**: 不涉及 **默认取值**: 不涉及
        :type lvm_config: str
        :param storage: 
        :type storage: :class:`huaweicloudsdkcce.v3.Storage`
        :param volume_reset_policy: **参数解释**： 节点重置时磁盘数据的保留策略。 不传或该字段为空时，默认使用reset_managed_volumes策略清空由CCE管理的数据盘。 **约束限制**： 当保留自定义挂载卷时，挂载到指定目录与作为持久存储卷的高级配置不允许修改。 **取值范围**： - reset_managed_volumes：清空由CCE管理的数据盘。 - retain_custom_volumes：保留用户自定义挂载卷（包括挂载到指定目录的卷和用作本地持久卷的卷），集群版本需为v1.29.15-r90、v1.30.14-r90、v1.31.14-r50、v1.32.13-r20、v1.33.12-r0、v1.34.8-r0、v1.35.5-r0、v1.36.1-r10或以上版本。  **默认取值**： reset_managed_volumes
        :type volume_reset_policy: str
        """
        
        

        self._lvm_config = None
        self._storage = None
        self._volume_reset_policy = None
        self.discriminator = None

        if lvm_config is not None:
            self.lvm_config = lvm_config
        if storage is not None:
            self.storage = storage
        if volume_reset_policy is not None:
            self.volume_reset_policy = volume_reset_policy

    @property
    def lvm_config(self):
        r"""Gets the lvm_config of this ReinstallVolumeConfig.

        **参数解释**: Docker数据盘配置项(已废弃)。  默认配置示例如下： ``` \"lvmConfig\":\"dockerThinpool=vgpaas/90%VG;kubernetesLV=vgpaas/10%VG;diskType=evs;lvType=linear\" ```  包含如下字段：   - userLV：用户空间的大小，示例格式：vgpaas/20%VG   - userPath：用户空间挂载路径，示例格式：/home/wqt-test   - diskType：磁盘类型，目前只有evs、hdd和ssd三种格式   - lvType：逻辑卷的类型，目前支持linear和striped两种，示例格式：striped   - dockerThinpool：Docker盘的空间大小，示例格式：vgpaas/60%VG   - kubernetesLV：Kubelet空间大小，示例格式：vgpaas/20%VG  **约束限制**: 不涉及 **取值范围**: 不涉及 **默认取值**: 不涉及

        :return: The lvm_config of this ReinstallVolumeConfig.
        :rtype: str
        """
        return self._lvm_config

    @lvm_config.setter
    def lvm_config(self, lvm_config):
        r"""Sets the lvm_config of this ReinstallVolumeConfig.

        **参数解释**: Docker数据盘配置项(已废弃)。  默认配置示例如下： ``` \"lvmConfig\":\"dockerThinpool=vgpaas/90%VG;kubernetesLV=vgpaas/10%VG;diskType=evs;lvType=linear\" ```  包含如下字段：   - userLV：用户空间的大小，示例格式：vgpaas/20%VG   - userPath：用户空间挂载路径，示例格式：/home/wqt-test   - diskType：磁盘类型，目前只有evs、hdd和ssd三种格式   - lvType：逻辑卷的类型，目前支持linear和striped两种，示例格式：striped   - dockerThinpool：Docker盘的空间大小，示例格式：vgpaas/60%VG   - kubernetesLV：Kubelet空间大小，示例格式：vgpaas/20%VG  **约束限制**: 不涉及 **取值范围**: 不涉及 **默认取值**: 不涉及

        :param lvm_config: The lvm_config of this ReinstallVolumeConfig.
        :type lvm_config: str
        """
        self._lvm_config = lvm_config

    @property
    def storage(self):
        r"""Gets the storage of this ReinstallVolumeConfig.

        :return: The storage of this ReinstallVolumeConfig.
        :rtype: :class:`huaweicloudsdkcce.v3.Storage`
        """
        return self._storage

    @storage.setter
    def storage(self, storage):
        r"""Sets the storage of this ReinstallVolumeConfig.

        :param storage: The storage of this ReinstallVolumeConfig.
        :type storage: :class:`huaweicloudsdkcce.v3.Storage`
        """
        self._storage = storage

    @property
    def volume_reset_policy(self):
        r"""Gets the volume_reset_policy of this ReinstallVolumeConfig.

        **参数解释**： 节点重置时磁盘数据的保留策略。 不传或该字段为空时，默认使用reset_managed_volumes策略清空由CCE管理的数据盘。 **约束限制**： 当保留自定义挂载卷时，挂载到指定目录与作为持久存储卷的高级配置不允许修改。 **取值范围**： - reset_managed_volumes：清空由CCE管理的数据盘。 - retain_custom_volumes：保留用户自定义挂载卷（包括挂载到指定目录的卷和用作本地持久卷的卷），集群版本需为v1.29.15-r90、v1.30.14-r90、v1.31.14-r50、v1.32.13-r20、v1.33.12-r0、v1.34.8-r0、v1.35.5-r0、v1.36.1-r10或以上版本。  **默认取值**： reset_managed_volumes

        :return: The volume_reset_policy of this ReinstallVolumeConfig.
        :rtype: str
        """
        return self._volume_reset_policy

    @volume_reset_policy.setter
    def volume_reset_policy(self, volume_reset_policy):
        r"""Sets the volume_reset_policy of this ReinstallVolumeConfig.

        **参数解释**： 节点重置时磁盘数据的保留策略。 不传或该字段为空时，默认使用reset_managed_volumes策略清空由CCE管理的数据盘。 **约束限制**： 当保留自定义挂载卷时，挂载到指定目录与作为持久存储卷的高级配置不允许修改。 **取值范围**： - reset_managed_volumes：清空由CCE管理的数据盘。 - retain_custom_volumes：保留用户自定义挂载卷（包括挂载到指定目录的卷和用作本地持久卷的卷），集群版本需为v1.29.15-r90、v1.30.14-r90、v1.31.14-r50、v1.32.13-r20、v1.33.12-r0、v1.34.8-r0、v1.35.5-r0、v1.36.1-r10或以上版本。  **默认取值**： reset_managed_volumes

        :param volume_reset_policy: The volume_reset_policy of this ReinstallVolumeConfig.
        :type volume_reset_policy: str
        """
        self._volume_reset_policy = volume_reset_policy

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
        if not isinstance(other, ReinstallVolumeConfig):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

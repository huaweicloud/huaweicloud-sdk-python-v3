# coding: utf-8

import re
import six



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
        'storage': 'Storage'
    }

    attribute_map = {
        'lvm_config': 'lvmConfig',
        'storage': 'storage'
    }

    def __init__(self, lvm_config=None, storage=None):
        """ReinstallVolumeConfig

        The model defined in huaweicloud sdk

        :param lvm_config: Docker数据盘配置项。 默认配置示例如下： &#x60;&#x60;&#x60; \&quot;lvmConfig\&quot;:\&quot;dockerThinpool&#x3D;vgpaas/90%VG;kubernetesLV&#x3D;vgpaas/10%VG;diskType&#x3D;evs;lvType&#x3D;linear\&quot; &#x60;&#x60;&#x60; 包含如下字段：   - userLV：用户空间的大小，示例格式：vgpaas/20%VG   - userPath：用户空间挂载路径，示例格式：/home/wqt-test   - diskType：磁盘类型，目前只有evs、hdd和ssd三种格式   - lvType：逻辑卷的类型，目前支持linear和striped两种，示例格式：striped   - dockerThinpool：Docker盘的空间大小，示例格式：vgpaas/60%VG   - kubernetesLV：Kubelet空间大小，示例格式：vgpaas/20%VG 
        :type lvm_config: str
        :param storage: 
        :type storage: :class:`huaweicloudsdkcce.v3.Storage`
        """
        
        

        self._lvm_config = None
        self._storage = None
        self.discriminator = None

        if lvm_config is not None:
            self.lvm_config = lvm_config
        if storage is not None:
            self.storage = storage

    @property
    def lvm_config(self):
        """Gets the lvm_config of this ReinstallVolumeConfig.

        Docker数据盘配置项。 默认配置示例如下： ``` \"lvmConfig\":\"dockerThinpool=vgpaas/90%VG;kubernetesLV=vgpaas/10%VG;diskType=evs;lvType=linear\" ``` 包含如下字段：   - userLV：用户空间的大小，示例格式：vgpaas/20%VG   - userPath：用户空间挂载路径，示例格式：/home/wqt-test   - diskType：磁盘类型，目前只有evs、hdd和ssd三种格式   - lvType：逻辑卷的类型，目前支持linear和striped两种，示例格式：striped   - dockerThinpool：Docker盘的空间大小，示例格式：vgpaas/60%VG   - kubernetesLV：Kubelet空间大小，示例格式：vgpaas/20%VG 

        :return: The lvm_config of this ReinstallVolumeConfig.
        :rtype: str
        """
        return self._lvm_config

    @lvm_config.setter
    def lvm_config(self, lvm_config):
        """Sets the lvm_config of this ReinstallVolumeConfig.

        Docker数据盘配置项。 默认配置示例如下： ``` \"lvmConfig\":\"dockerThinpool=vgpaas/90%VG;kubernetesLV=vgpaas/10%VG;diskType=evs;lvType=linear\" ``` 包含如下字段：   - userLV：用户空间的大小，示例格式：vgpaas/20%VG   - userPath：用户空间挂载路径，示例格式：/home/wqt-test   - diskType：磁盘类型，目前只有evs、hdd和ssd三种格式   - lvType：逻辑卷的类型，目前支持linear和striped两种，示例格式：striped   - dockerThinpool：Docker盘的空间大小，示例格式：vgpaas/60%VG   - kubernetesLV：Kubelet空间大小，示例格式：vgpaas/20%VG 

        :param lvm_config: The lvm_config of this ReinstallVolumeConfig.
        :type lvm_config: str
        """
        self._lvm_config = lvm_config

    @property
    def storage(self):
        """Gets the storage of this ReinstallVolumeConfig.


        :return: The storage of this ReinstallVolumeConfig.
        :rtype: :class:`huaweicloudsdkcce.v3.Storage`
        """
        return self._storage

    @storage.setter
    def storage(self, storage):
        """Sets the storage of this ReinstallVolumeConfig.


        :param storage: The storage of this ReinstallVolumeConfig.
        :type storage: :class:`huaweicloudsdkcce.v3.Storage`
        """
        self._storage = storage

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
        if not isinstance(other, ReinstallVolumeConfig):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

# coding: utf-8

import pprint
import re

import six





class PersistentVolumeClaimSpec:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'access_modes': 'list[str]',
        'resources': 'ResourceRequirements',
        'storage_class_name': 'str',
        'storage_type': 'str',
        'volume_id': 'str',
        'volume_mode': 'str',
        'volume_name': 'str'
    }

    attribute_map = {
        'access_modes': 'accessModes',
        'resources': 'resources',
        'storage_class_name': 'storageClassName',
        'storage_type': 'storageType',
        'volume_id': 'volumeID',
        'volume_mode': 'volumeMode',
        'volume_name': 'volumeName'
    }

    def __init__(self, access_modes=None, resources=None, storage_class_name=None, storage_type=None, volume_id=None, volume_mode=None, volume_name=None):
        """PersistentVolumeClaimSpec - a model defined in huaweicloud sdk"""
        
        

        self._access_modes = None
        self._resources = None
        self._storage_class_name = None
        self._storage_type = None
        self._volume_id = None
        self._volume_mode = None
        self._volume_name = None
        self.discriminator = None

        self.access_modes = access_modes
        if resources is not None:
            self.resources = resources
        if storage_class_name is not None:
            self.storage_class_name = storage_class_name
        self.storage_type = storage_type
        self.volume_id = volume_id
        if volume_mode is not None:
            self.volume_mode = volume_mode
        if volume_name is not None:
            self.volume_name = volume_name

    @property
    def access_modes(self):
        """Gets the access_modes of this PersistentVolumeClaimSpec.

        指定volume应该具有的访问模式，列表中仅第一个配置参数有效。 - ReadWriteOnce：该卷可以被单个节点以读/写模式挂载   >集群版本为v1.13.10且storage-driver版本为1.0.19时，才支持此功能。 - ReadOnlyMany：该卷可以被多个节点以只读模式挂载（默认） - ReadWriteMany：该卷可以被多个节点以读/写模式挂载

        :return: The access_modes of this PersistentVolumeClaimSpec.
        :rtype: list[str]
        """
        return self._access_modes

    @access_modes.setter
    def access_modes(self, access_modes):
        """Sets the access_modes of this PersistentVolumeClaimSpec.

        指定volume应该具有的访问模式，列表中仅第一个配置参数有效。 - ReadWriteOnce：该卷可以被单个节点以读/写模式挂载   >集群版本为v1.13.10且storage-driver版本为1.0.19时，才支持此功能。 - ReadOnlyMany：该卷可以被多个节点以只读模式挂载（默认） - ReadWriteMany：该卷可以被多个节点以读/写模式挂载

        :param access_modes: The access_modes of this PersistentVolumeClaimSpec.
        :type: list[str]
        """
        self._access_modes = access_modes

    @property
    def resources(self):
        """Gets the resources of this PersistentVolumeClaimSpec.


        :return: The resources of this PersistentVolumeClaimSpec.
        :rtype: ResourceRequirements
        """
        return self._resources

    @resources.setter
    def resources(self, resources):
        """Sets the resources of this PersistentVolumeClaimSpec.


        :param resources: The resources of this PersistentVolumeClaimSpec.
        :type: ResourceRequirements
        """
        self._resources = resources

    @property
    def storage_class_name(self):
        """Gets the storage_class_name of this PersistentVolumeClaimSpec.

        PVC的StorageClass名称

        :return: The storage_class_name of this PersistentVolumeClaimSpec.
        :rtype: str
        """
        return self._storage_class_name

    @storage_class_name.setter
    def storage_class_name(self, storage_class_name):
        """Sets the storage_class_name of this PersistentVolumeClaimSpec.

        PVC的StorageClass名称

        :param storage_class_name: The storage_class_name of this PersistentVolumeClaimSpec.
        :type: str
        """
        self._storage_class_name = storage_class_name

    @property
    def storage_type(self):
        """Gets the storage_type of this PersistentVolumeClaimSpec.

        云存储的类型，和volumeID搭配使用。即volumeID和storageType必须同时被配置。  - bs：EVS云存储，详情可参见[使用云硬盘存储卷](https://support.huaweicloud.com/usermanual-cce/cce_01_0044.html) 。 - nfs：SFS弹性文件存储，详情可参见[使用文件存储卷](https://support.huaweicloud.com/usermanual-cce/cce_01_0111.html) 。 - obs：OBS对象存储，详情可参见[使用对象存储卷](https://support.huaweicloud.com/usermanual-cce/cce_01_0160.html) 。 - efs：SFS Turbo极速文件存储，详情可参见[使用极速文件存储卷](https://support.huaweicloud.com/usermanual-cce/cce_01_0125.html)。

        :return: The storage_type of this PersistentVolumeClaimSpec.
        :rtype: str
        """
        return self._storage_type

    @storage_type.setter
    def storage_type(self, storage_type):
        """Sets the storage_type of this PersistentVolumeClaimSpec.

        云存储的类型，和volumeID搭配使用。即volumeID和storageType必须同时被配置。  - bs：EVS云存储，详情可参见[使用云硬盘存储卷](https://support.huaweicloud.com/usermanual-cce/cce_01_0044.html) 。 - nfs：SFS弹性文件存储，详情可参见[使用文件存储卷](https://support.huaweicloud.com/usermanual-cce/cce_01_0111.html) 。 - obs：OBS对象存储，详情可参见[使用对象存储卷](https://support.huaweicloud.com/usermanual-cce/cce_01_0160.html) 。 - efs：SFS Turbo极速文件存储，详情可参见[使用极速文件存储卷](https://support.huaweicloud.com/usermanual-cce/cce_01_0125.html)。

        :param storage_type: The storage_type of this PersistentVolumeClaimSpec.
        :type: str
        """
        self._storage_type = storage_type

    @property
    def volume_id(self):
        """Gets the volume_id of this PersistentVolumeClaimSpec.

        资源需为已经存在的存储资源 - 如果存储资源类型是SFS、EVS、SFS-Turbo，本参数需要填入对应资源的ID - 如果资源类型为OBS，本参数填入OBS名称

        :return: The volume_id of this PersistentVolumeClaimSpec.
        :rtype: str
        """
        return self._volume_id

    @volume_id.setter
    def volume_id(self, volume_id):
        """Sets the volume_id of this PersistentVolumeClaimSpec.

        资源需为已经存在的存储资源 - 如果存储资源类型是SFS、EVS、SFS-Turbo，本参数需要填入对应资源的ID - 如果资源类型为OBS，本参数填入OBS名称

        :param volume_id: The volume_id of this PersistentVolumeClaimSpec.
        :type: str
        """
        self._volume_id = volume_id

    @property
    def volume_mode(self):
        """Gets the volume_mode of this PersistentVolumeClaimSpec.

        PVC指定的PV类型

        :return: The volume_mode of this PersistentVolumeClaimSpec.
        :rtype: str
        """
        return self._volume_mode

    @volume_mode.setter
    def volume_mode(self, volume_mode):
        """Sets the volume_mode of this PersistentVolumeClaimSpec.

        PVC指定的PV类型

        :param volume_mode: The volume_mode of this PersistentVolumeClaimSpec.
        :type: str
        """
        self._volume_mode = volume_mode

    @property
    def volume_name(self):
        """Gets the volume_name of this PersistentVolumeClaimSpec.

        PVC绑定的PV名称

        :return: The volume_name of this PersistentVolumeClaimSpec.
        :rtype: str
        """
        return self._volume_name

    @volume_name.setter
    def volume_name(self, volume_name):
        """Sets the volume_name of this PersistentVolumeClaimSpec.

        PVC绑定的PV名称

        :param volume_name: The volume_name of this PersistentVolumeClaimSpec.
        :type: str
        """
        self._volume_name = volume_name

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
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, PersistentVolumeClaimSpec):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

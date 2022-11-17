# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BackupExtendInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'auto_trigger': 'bool',
        'bootable': 'bool',
        'incremental': 'bool',
        'snapshot_id': 'str',
        'support_lld': 'bool',
        'supported_restore_mode': 'str',
        'os_images_data': 'list[ImageData]',
        'contain_system_disk': 'bool',
        'encrypted': 'bool',
        'system_disk': 'bool',
        'is_multi_az': 'bool'
    }

    attribute_map = {
        'auto_trigger': 'auto_trigger',
        'bootable': 'bootable',
        'incremental': 'incremental',
        'snapshot_id': 'snapshot_id',
        'support_lld': 'support_lld',
        'supported_restore_mode': 'supported_restore_mode',
        'os_images_data': 'os_images_data',
        'contain_system_disk': 'contain_system_disk',
        'encrypted': 'encrypted',
        'system_disk': 'system_disk',
        'is_multi_az': 'is_multi_az'
    }

    def __init__(self, auto_trigger=None, bootable=None, incremental=None, snapshot_id=None, support_lld=None, supported_restore_mode=None, os_images_data=None, contain_system_disk=None, encrypted=None, system_disk=None, is_multi_az=None):
        """BackupExtendInfo

        The model defined in huaweicloud sdk

        :param auto_trigger: 是否是自动生成的备份副本
        :type auto_trigger: bool
        :param bootable: 是否系统盘备份
        :type bootable: bool
        :param incremental: 是否是增备
        :type incremental: bool
        :param snapshot_id: 卷备份副本的快照id
        :type snapshot_id: str
        :param support_lld: 是否支持lazyloading快速恢复
        :type support_lld: bool
        :param supported_restore_mode: 备份支持恢复的方式，当前取值包含na,snapshot和backup。如果该字段取值为snapshot，代表备份此时已经支持创建整机镜像；如果该字段取值为backup，备份支持通过云服务器上硬盘的备份进行恢复；如果该字段取值为na，备份不支持恢复。
        :type supported_restore_mode: str
        :param os_images_data: 备份注册镜像ID列表
        :type os_images_data: list[:class:`huaweicloudsdkcbr.v1.ImageData`]
        :param contain_system_disk: 整机备份是否包含系统盘
        :type contain_system_disk: bool
        :param encrypted: 是否加密
        :type encrypted: bool
        :param system_disk: 是否是系统盘
        :type system_disk: bool
        :param is_multi_az: 备份类型是否为多AZ
        :type is_multi_az: bool
        """
        
        

        self._auto_trigger = None
        self._bootable = None
        self._incremental = None
        self._snapshot_id = None
        self._support_lld = None
        self._supported_restore_mode = None
        self._os_images_data = None
        self._contain_system_disk = None
        self._encrypted = None
        self._system_disk = None
        self._is_multi_az = None
        self.discriminator = None

        if auto_trigger is not None:
            self.auto_trigger = auto_trigger
        if bootable is not None:
            self.bootable = bootable
        if incremental is not None:
            self.incremental = incremental
        if snapshot_id is not None:
            self.snapshot_id = snapshot_id
        if support_lld is not None:
            self.support_lld = support_lld
        if supported_restore_mode is not None:
            self.supported_restore_mode = supported_restore_mode
        if os_images_data is not None:
            self.os_images_data = os_images_data
        if contain_system_disk is not None:
            self.contain_system_disk = contain_system_disk
        if encrypted is not None:
            self.encrypted = encrypted
        if system_disk is not None:
            self.system_disk = system_disk
        if is_multi_az is not None:
            self.is_multi_az = is_multi_az

    @property
    def auto_trigger(self):
        """Gets the auto_trigger of this BackupExtendInfo.

        是否是自动生成的备份副本

        :return: The auto_trigger of this BackupExtendInfo.
        :rtype: bool
        """
        return self._auto_trigger

    @auto_trigger.setter
    def auto_trigger(self, auto_trigger):
        """Sets the auto_trigger of this BackupExtendInfo.

        是否是自动生成的备份副本

        :param auto_trigger: The auto_trigger of this BackupExtendInfo.
        :type auto_trigger: bool
        """
        self._auto_trigger = auto_trigger

    @property
    def bootable(self):
        """Gets the bootable of this BackupExtendInfo.

        是否系统盘备份

        :return: The bootable of this BackupExtendInfo.
        :rtype: bool
        """
        return self._bootable

    @bootable.setter
    def bootable(self, bootable):
        """Sets the bootable of this BackupExtendInfo.

        是否系统盘备份

        :param bootable: The bootable of this BackupExtendInfo.
        :type bootable: bool
        """
        self._bootable = bootable

    @property
    def incremental(self):
        """Gets the incremental of this BackupExtendInfo.

        是否是增备

        :return: The incremental of this BackupExtendInfo.
        :rtype: bool
        """
        return self._incremental

    @incremental.setter
    def incremental(self, incremental):
        """Sets the incremental of this BackupExtendInfo.

        是否是增备

        :param incremental: The incremental of this BackupExtendInfo.
        :type incremental: bool
        """
        self._incremental = incremental

    @property
    def snapshot_id(self):
        """Gets the snapshot_id of this BackupExtendInfo.

        卷备份副本的快照id

        :return: The snapshot_id of this BackupExtendInfo.
        :rtype: str
        """
        return self._snapshot_id

    @snapshot_id.setter
    def snapshot_id(self, snapshot_id):
        """Sets the snapshot_id of this BackupExtendInfo.

        卷备份副本的快照id

        :param snapshot_id: The snapshot_id of this BackupExtendInfo.
        :type snapshot_id: str
        """
        self._snapshot_id = snapshot_id

    @property
    def support_lld(self):
        """Gets the support_lld of this BackupExtendInfo.

        是否支持lazyloading快速恢复

        :return: The support_lld of this BackupExtendInfo.
        :rtype: bool
        """
        return self._support_lld

    @support_lld.setter
    def support_lld(self, support_lld):
        """Sets the support_lld of this BackupExtendInfo.

        是否支持lazyloading快速恢复

        :param support_lld: The support_lld of this BackupExtendInfo.
        :type support_lld: bool
        """
        self._support_lld = support_lld

    @property
    def supported_restore_mode(self):
        """Gets the supported_restore_mode of this BackupExtendInfo.

        备份支持恢复的方式，当前取值包含na,snapshot和backup。如果该字段取值为snapshot，代表备份此时已经支持创建整机镜像；如果该字段取值为backup，备份支持通过云服务器上硬盘的备份进行恢复；如果该字段取值为na，备份不支持恢复。

        :return: The supported_restore_mode of this BackupExtendInfo.
        :rtype: str
        """
        return self._supported_restore_mode

    @supported_restore_mode.setter
    def supported_restore_mode(self, supported_restore_mode):
        """Sets the supported_restore_mode of this BackupExtendInfo.

        备份支持恢复的方式，当前取值包含na,snapshot和backup。如果该字段取值为snapshot，代表备份此时已经支持创建整机镜像；如果该字段取值为backup，备份支持通过云服务器上硬盘的备份进行恢复；如果该字段取值为na，备份不支持恢复。

        :param supported_restore_mode: The supported_restore_mode of this BackupExtendInfo.
        :type supported_restore_mode: str
        """
        self._supported_restore_mode = supported_restore_mode

    @property
    def os_images_data(self):
        """Gets the os_images_data of this BackupExtendInfo.

        备份注册镜像ID列表

        :return: The os_images_data of this BackupExtendInfo.
        :rtype: list[:class:`huaweicloudsdkcbr.v1.ImageData`]
        """
        return self._os_images_data

    @os_images_data.setter
    def os_images_data(self, os_images_data):
        """Sets the os_images_data of this BackupExtendInfo.

        备份注册镜像ID列表

        :param os_images_data: The os_images_data of this BackupExtendInfo.
        :type os_images_data: list[:class:`huaweicloudsdkcbr.v1.ImageData`]
        """
        self._os_images_data = os_images_data

    @property
    def contain_system_disk(self):
        """Gets the contain_system_disk of this BackupExtendInfo.

        整机备份是否包含系统盘

        :return: The contain_system_disk of this BackupExtendInfo.
        :rtype: bool
        """
        return self._contain_system_disk

    @contain_system_disk.setter
    def contain_system_disk(self, contain_system_disk):
        """Sets the contain_system_disk of this BackupExtendInfo.

        整机备份是否包含系统盘

        :param contain_system_disk: The contain_system_disk of this BackupExtendInfo.
        :type contain_system_disk: bool
        """
        self._contain_system_disk = contain_system_disk

    @property
    def encrypted(self):
        """Gets the encrypted of this BackupExtendInfo.

        是否加密

        :return: The encrypted of this BackupExtendInfo.
        :rtype: bool
        """
        return self._encrypted

    @encrypted.setter
    def encrypted(self, encrypted):
        """Sets the encrypted of this BackupExtendInfo.

        是否加密

        :param encrypted: The encrypted of this BackupExtendInfo.
        :type encrypted: bool
        """
        self._encrypted = encrypted

    @property
    def system_disk(self):
        """Gets the system_disk of this BackupExtendInfo.

        是否是系统盘

        :return: The system_disk of this BackupExtendInfo.
        :rtype: bool
        """
        return self._system_disk

    @system_disk.setter
    def system_disk(self, system_disk):
        """Sets the system_disk of this BackupExtendInfo.

        是否是系统盘

        :param system_disk: The system_disk of this BackupExtendInfo.
        :type system_disk: bool
        """
        self._system_disk = system_disk

    @property
    def is_multi_az(self):
        """Gets the is_multi_az of this BackupExtendInfo.

        备份类型是否为多AZ

        :return: The is_multi_az of this BackupExtendInfo.
        :rtype: bool
        """
        return self._is_multi_az

    @is_multi_az.setter
    def is_multi_az(self, is_multi_az):
        """Sets the is_multi_az of this BackupExtendInfo.

        备份类型是否为多AZ

        :param is_multi_az: The is_multi_az of this BackupExtendInfo.
        :type is_multi_az: bool
        """
        self._is_multi_az = is_multi_az

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
        if not isinstance(other, BackupExtendInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

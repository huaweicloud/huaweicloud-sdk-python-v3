# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class NovaServerBlockDeviceMapping:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'source_type': 'str',
        'destination_type': 'str',
        'guest_format': 'str',
        'device_name': 'str',
        'delete_on_termination': 'bool',
        'boot_index': 'str',
        'uuid': 'str',
        'volume_size': 'int',
        'volume_type': 'str'
    }

    attribute_map = {
        'source_type': 'source_type',
        'destination_type': 'destination_type',
        'guest_format': 'guest_format',
        'device_name': 'device_name',
        'delete_on_termination': 'delete_on_termination',
        'boot_index': 'boot_index',
        'uuid': 'uuid',
        'volume_size': 'volume_size',
        'volume_type': 'volume_type'
    }

    def __init__(self, source_type=None, destination_type=None, guest_format=None, device_name=None, delete_on_termination=None, boot_index=None, uuid=None, volume_size=None, volume_type=None):
        """NovaServerBlockDeviceMapping

        The model defined in huaweicloud sdk

        :param source_type: 卷设备的源头类型，当前只支持volume、image、snapshot、blank类型。  当使用卷创建云服务器时，source_type设置为volume；当使用镜像创建云服务器时，source_type设置为image；当使用快照创建云服务器时，source_type设置为snapshot；当创建空数据卷时，source_type设置为blank。  - 说明： -  - 当卷设备的源头类型为snapshot时，且boot_index为0，则该快照对应的云硬盘必须为系统盘。
        :type source_type: str
        :param destination_type: 卷设备的目标类型，当前仅支持volume类型。  - volume：卷。 - local：本地文件，当前不支持该类型。
        :type destination_type: str
        :param guest_format: local文件系统格式，例如：swap, ext4。  当前不支持该功能。
        :type guest_format: str
        :param device_name: 卷设备名称。  &gt; 说明： &gt;  &gt; 该字段已经废弃。 &gt;  &gt; 用户指定的device_name不会生效，系统会默认生成一个device_name。
        :type device_name: str
        :param delete_on_termination: 删除弹性云服务器时，是否删除卷，默认值false。  true：删除弹性云服务器时，删除卷  false：删除弹性云服务器时，不删除卷
        :type delete_on_termination: bool
        :param boot_index: 启动标识，“0”代表启动盘，“-1“代表非启动盘。  &gt; 说明： &gt;  &gt; 当卷设备的源头类型全为volume时，boot_index的值有一个为0。
        :type boot_index: str
        :param uuid: 当source_type值是volume时，uuid为卷的uuid；  当source_type值是snapshot时，uuid为快照的uuid；  当source_type值是image时，uuid为镜像的uuid；
        :type uuid: str
        :param volume_size: 卷大小，整数，在source_type是image或blank，destination_type是volume的时候必选。  单位为GB。
        :type volume_size: int
        :param volume_type: 卷类型，在source_type是image，destination_type是volume时建议填写。  卷类型取值范围请参考 EVS 服务 [磁盘类型介绍](https://support.huaweicloud.com/productdesc-evs/zh-cn_topic_0044524691.html)。
        :type volume_type: str
        """
        
        

        self._source_type = None
        self._destination_type = None
        self._guest_format = None
        self._device_name = None
        self._delete_on_termination = None
        self._boot_index = None
        self._uuid = None
        self._volume_size = None
        self._volume_type = None
        self.discriminator = None

        self.source_type = source_type
        if destination_type is not None:
            self.destination_type = destination_type
        if guest_format is not None:
            self.guest_format = guest_format
        if device_name is not None:
            self.device_name = device_name
        if delete_on_termination is not None:
            self.delete_on_termination = delete_on_termination
        if boot_index is not None:
            self.boot_index = boot_index
        if uuid is not None:
            self.uuid = uuid
        if volume_size is not None:
            self.volume_size = volume_size
        if volume_type is not None:
            self.volume_type = volume_type

    @property
    def source_type(self):
        """Gets the source_type of this NovaServerBlockDeviceMapping.

        卷设备的源头类型，当前只支持volume、image、snapshot、blank类型。  当使用卷创建云服务器时，source_type设置为volume；当使用镜像创建云服务器时，source_type设置为image；当使用快照创建云服务器时，source_type设置为snapshot；当创建空数据卷时，source_type设置为blank。  - 说明： -  - 当卷设备的源头类型为snapshot时，且boot_index为0，则该快照对应的云硬盘必须为系统盘。

        :return: The source_type of this NovaServerBlockDeviceMapping.
        :rtype: str
        """
        return self._source_type

    @source_type.setter
    def source_type(self, source_type):
        """Sets the source_type of this NovaServerBlockDeviceMapping.

        卷设备的源头类型，当前只支持volume、image、snapshot、blank类型。  当使用卷创建云服务器时，source_type设置为volume；当使用镜像创建云服务器时，source_type设置为image；当使用快照创建云服务器时，source_type设置为snapshot；当创建空数据卷时，source_type设置为blank。  - 说明： -  - 当卷设备的源头类型为snapshot时，且boot_index为0，则该快照对应的云硬盘必须为系统盘。

        :param source_type: The source_type of this NovaServerBlockDeviceMapping.
        :type source_type: str
        """
        self._source_type = source_type

    @property
    def destination_type(self):
        """Gets the destination_type of this NovaServerBlockDeviceMapping.

        卷设备的目标类型，当前仅支持volume类型。  - volume：卷。 - local：本地文件，当前不支持该类型。

        :return: The destination_type of this NovaServerBlockDeviceMapping.
        :rtype: str
        """
        return self._destination_type

    @destination_type.setter
    def destination_type(self, destination_type):
        """Sets the destination_type of this NovaServerBlockDeviceMapping.

        卷设备的目标类型，当前仅支持volume类型。  - volume：卷。 - local：本地文件，当前不支持该类型。

        :param destination_type: The destination_type of this NovaServerBlockDeviceMapping.
        :type destination_type: str
        """
        self._destination_type = destination_type

    @property
    def guest_format(self):
        """Gets the guest_format of this NovaServerBlockDeviceMapping.

        local文件系统格式，例如：swap, ext4。  当前不支持该功能。

        :return: The guest_format of this NovaServerBlockDeviceMapping.
        :rtype: str
        """
        return self._guest_format

    @guest_format.setter
    def guest_format(self, guest_format):
        """Sets the guest_format of this NovaServerBlockDeviceMapping.

        local文件系统格式，例如：swap, ext4。  当前不支持该功能。

        :param guest_format: The guest_format of this NovaServerBlockDeviceMapping.
        :type guest_format: str
        """
        self._guest_format = guest_format

    @property
    def device_name(self):
        """Gets the device_name of this NovaServerBlockDeviceMapping.

        卷设备名称。  > 说明： >  > 该字段已经废弃。 >  > 用户指定的device_name不会生效，系统会默认生成一个device_name。

        :return: The device_name of this NovaServerBlockDeviceMapping.
        :rtype: str
        """
        return self._device_name

    @device_name.setter
    def device_name(self, device_name):
        """Sets the device_name of this NovaServerBlockDeviceMapping.

        卷设备名称。  > 说明： >  > 该字段已经废弃。 >  > 用户指定的device_name不会生效，系统会默认生成一个device_name。

        :param device_name: The device_name of this NovaServerBlockDeviceMapping.
        :type device_name: str
        """
        self._device_name = device_name

    @property
    def delete_on_termination(self):
        """Gets the delete_on_termination of this NovaServerBlockDeviceMapping.

        删除弹性云服务器时，是否删除卷，默认值false。  true：删除弹性云服务器时，删除卷  false：删除弹性云服务器时，不删除卷

        :return: The delete_on_termination of this NovaServerBlockDeviceMapping.
        :rtype: bool
        """
        return self._delete_on_termination

    @delete_on_termination.setter
    def delete_on_termination(self, delete_on_termination):
        """Sets the delete_on_termination of this NovaServerBlockDeviceMapping.

        删除弹性云服务器时，是否删除卷，默认值false。  true：删除弹性云服务器时，删除卷  false：删除弹性云服务器时，不删除卷

        :param delete_on_termination: The delete_on_termination of this NovaServerBlockDeviceMapping.
        :type delete_on_termination: bool
        """
        self._delete_on_termination = delete_on_termination

    @property
    def boot_index(self):
        """Gets the boot_index of this NovaServerBlockDeviceMapping.

        启动标识，“0”代表启动盘，“-1“代表非启动盘。  > 说明： >  > 当卷设备的源头类型全为volume时，boot_index的值有一个为0。

        :return: The boot_index of this NovaServerBlockDeviceMapping.
        :rtype: str
        """
        return self._boot_index

    @boot_index.setter
    def boot_index(self, boot_index):
        """Sets the boot_index of this NovaServerBlockDeviceMapping.

        启动标识，“0”代表启动盘，“-1“代表非启动盘。  > 说明： >  > 当卷设备的源头类型全为volume时，boot_index的值有一个为0。

        :param boot_index: The boot_index of this NovaServerBlockDeviceMapping.
        :type boot_index: str
        """
        self._boot_index = boot_index

    @property
    def uuid(self):
        """Gets the uuid of this NovaServerBlockDeviceMapping.

        当source_type值是volume时，uuid为卷的uuid；  当source_type值是snapshot时，uuid为快照的uuid；  当source_type值是image时，uuid为镜像的uuid；

        :return: The uuid of this NovaServerBlockDeviceMapping.
        :rtype: str
        """
        return self._uuid

    @uuid.setter
    def uuid(self, uuid):
        """Sets the uuid of this NovaServerBlockDeviceMapping.

        当source_type值是volume时，uuid为卷的uuid；  当source_type值是snapshot时，uuid为快照的uuid；  当source_type值是image时，uuid为镜像的uuid；

        :param uuid: The uuid of this NovaServerBlockDeviceMapping.
        :type uuid: str
        """
        self._uuid = uuid

    @property
    def volume_size(self):
        """Gets the volume_size of this NovaServerBlockDeviceMapping.

        卷大小，整数，在source_type是image或blank，destination_type是volume的时候必选。  单位为GB。

        :return: The volume_size of this NovaServerBlockDeviceMapping.
        :rtype: int
        """
        return self._volume_size

    @volume_size.setter
    def volume_size(self, volume_size):
        """Sets the volume_size of this NovaServerBlockDeviceMapping.

        卷大小，整数，在source_type是image或blank，destination_type是volume的时候必选。  单位为GB。

        :param volume_size: The volume_size of this NovaServerBlockDeviceMapping.
        :type volume_size: int
        """
        self._volume_size = volume_size

    @property
    def volume_type(self):
        """Gets the volume_type of this NovaServerBlockDeviceMapping.

        卷类型，在source_type是image，destination_type是volume时建议填写。  卷类型取值范围请参考 EVS 服务 [磁盘类型介绍](https://support.huaweicloud.com/productdesc-evs/zh-cn_topic_0044524691.html)。

        :return: The volume_type of this NovaServerBlockDeviceMapping.
        :rtype: str
        """
        return self._volume_type

    @volume_type.setter
    def volume_type(self, volume_type):
        """Sets the volume_type of this NovaServerBlockDeviceMapping.

        卷类型，在source_type是image，destination_type是volume时建议填写。  卷类型取值范围请参考 EVS 服务 [磁盘类型介绍](https://support.huaweicloud.com/productdesc-evs/zh-cn_topic_0044524691.html)。

        :param volume_type: The volume_type of this NovaServerBlockDeviceMapping.
        :type volume_type: str
        """
        self._volume_type = volume_type

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
        if not isinstance(other, NovaServerBlockDeviceMapping):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

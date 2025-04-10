# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class VolumeAttach:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'id': 'str',
        'delete_on_termination': 'bool',
        'device': 'str',
        'boot_index': 'str',
        'size': 'int'
    }

    attribute_map = {
        'id': 'id',
        'delete_on_termination': 'delete_on_termination',
        'device': 'device',
        'boot_index': 'bootIndex',
        'size': 'size'
    }

    def __init__(self, id=None, delete_on_termination=None, device=None, boot_index=None, size=None):
        r"""VolumeAttach

        The model defined in huaweicloud sdk

        :param id: 云磁盘ID。
        :type id: str
        :param delete_on_termination: 一个标志，指示在删除服务器时是否删除附加的卷。 默认情况下，这是False
        :type delete_on_termination: bool
        :param device: 挂载点
        :type device: str
        :param boot_index: 盘在云服务器上的挂载顺序，0表示启动盘。
        :type boot_index: str
        :param size: 云盘大小（单位：GB）。
        :type size: int
        """
        
        

        self._id = None
        self._delete_on_termination = None
        self._device = None
        self._boot_index = None
        self._size = None
        self.discriminator = None

        self.id = id
        if delete_on_termination is not None:
            self.delete_on_termination = delete_on_termination
        if device is not None:
            self.device = device
        if boot_index is not None:
            self.boot_index = boot_index
        if size is not None:
            self.size = size

    @property
    def id(self):
        r"""Gets the id of this VolumeAttach.

        云磁盘ID。

        :return: The id of this VolumeAttach.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this VolumeAttach.

        云磁盘ID。

        :param id: The id of this VolumeAttach.
        :type id: str
        """
        self._id = id

    @property
    def delete_on_termination(self):
        r"""Gets the delete_on_termination of this VolumeAttach.

        一个标志，指示在删除服务器时是否删除附加的卷。 默认情况下，这是False

        :return: The delete_on_termination of this VolumeAttach.
        :rtype: bool
        """
        return self._delete_on_termination

    @delete_on_termination.setter
    def delete_on_termination(self, delete_on_termination):
        r"""Sets the delete_on_termination of this VolumeAttach.

        一个标志，指示在删除服务器时是否删除附加的卷。 默认情况下，这是False

        :param delete_on_termination: The delete_on_termination of this VolumeAttach.
        :type delete_on_termination: bool
        """
        self._delete_on_termination = delete_on_termination

    @property
    def device(self):
        r"""Gets the device of this VolumeAttach.

        挂载点

        :return: The device of this VolumeAttach.
        :rtype: str
        """
        return self._device

    @device.setter
    def device(self, device):
        r"""Sets the device of this VolumeAttach.

        挂载点

        :param device: The device of this VolumeAttach.
        :type device: str
        """
        self._device = device

    @property
    def boot_index(self):
        r"""Gets the boot_index of this VolumeAttach.

        盘在云服务器上的挂载顺序，0表示启动盘。

        :return: The boot_index of this VolumeAttach.
        :rtype: str
        """
        return self._boot_index

    @boot_index.setter
    def boot_index(self, boot_index):
        r"""Sets the boot_index of this VolumeAttach.

        盘在云服务器上的挂载顺序，0表示启动盘。

        :param boot_index: The boot_index of this VolumeAttach.
        :type boot_index: str
        """
        self._boot_index = boot_index

    @property
    def size(self):
        r"""Gets the size of this VolumeAttach.

        云盘大小（单位：GB）。

        :return: The size of this VolumeAttach.
        :rtype: int
        """
        return self._size

    @size.setter
    def size(self, size):
        r"""Sets the size of this VolumeAttach.

        云盘大小（单位：GB）。

        :param size: The size of this VolumeAttach.
        :type size: int
        """
        self._size = size

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
        if not isinstance(other, VolumeAttach):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class VolumesAttached:

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
        'boot_index': 'str',
        'delete_on_termination': 'str',
        'device': 'str'
    }

    attribute_map = {
        'id': 'id',
        'boot_index': 'bootIndex',
        'delete_on_termination': 'delete_on_termination',
        'device': 'device'
    }

    def __init__(self, id=None, boot_index=None, delete_on_termination=None, device=None):
        """VolumesAttached

        The model defined in huaweicloud sdk

        :param id: 磁盘ID，格式为UUID。
        :type id: str
        :param boot_index: 启动标识。  - “0”代表系统盘 - 非“0”为数据盘。
        :type boot_index: str
        :param delete_on_termination: 删边缘实例时是否一并删除该磁盘。  - true：是 - false：否
        :type delete_on_termination: str
        :param device: 硬盘挂载盘符，即磁盘挂载点。
        :type device: str
        """
        
        

        self._id = None
        self._boot_index = None
        self._delete_on_termination = None
        self._device = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if boot_index is not None:
            self.boot_index = boot_index
        if delete_on_termination is not None:
            self.delete_on_termination = delete_on_termination
        if device is not None:
            self.device = device

    @property
    def id(self):
        """Gets the id of this VolumesAttached.

        磁盘ID，格式为UUID。

        :return: The id of this VolumesAttached.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this VolumesAttached.

        磁盘ID，格式为UUID。

        :param id: The id of this VolumesAttached.
        :type id: str
        """
        self._id = id

    @property
    def boot_index(self):
        """Gets the boot_index of this VolumesAttached.

        启动标识。  - “0”代表系统盘 - 非“0”为数据盘。

        :return: The boot_index of this VolumesAttached.
        :rtype: str
        """
        return self._boot_index

    @boot_index.setter
    def boot_index(self, boot_index):
        """Sets the boot_index of this VolumesAttached.

        启动标识。  - “0”代表系统盘 - 非“0”为数据盘。

        :param boot_index: The boot_index of this VolumesAttached.
        :type boot_index: str
        """
        self._boot_index = boot_index

    @property
    def delete_on_termination(self):
        """Gets the delete_on_termination of this VolumesAttached.

        删边缘实例时是否一并删除该磁盘。  - true：是 - false：否

        :return: The delete_on_termination of this VolumesAttached.
        :rtype: str
        """
        return self._delete_on_termination

    @delete_on_termination.setter
    def delete_on_termination(self, delete_on_termination):
        """Sets the delete_on_termination of this VolumesAttached.

        删边缘实例时是否一并删除该磁盘。  - true：是 - false：否

        :param delete_on_termination: The delete_on_termination of this VolumesAttached.
        :type delete_on_termination: str
        """
        self._delete_on_termination = delete_on_termination

    @property
    def device(self):
        """Gets the device of this VolumesAttached.

        硬盘挂载盘符，即磁盘挂载点。

        :return: The device of this VolumesAttached.
        :rtype: str
        """
        return self._device

    @device.setter
    def device(self, device):
        """Sets the device of this VolumesAttached.

        硬盘挂载盘符，即磁盘挂载点。

        :param device: The device of this VolumesAttached.
        :type device: str
        """
        self._device = device

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
        if not isinstance(other, VolumesAttached):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

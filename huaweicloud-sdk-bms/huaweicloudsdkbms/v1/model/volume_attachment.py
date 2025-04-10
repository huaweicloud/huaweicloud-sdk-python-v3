# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class VolumeAttachment:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'volume_id': 'str',
        'device': 'str'
    }

    attribute_map = {
        'volume_id': 'volumeId',
        'device': 'device'
    }

    def __init__(self, volume_id=None, device=None):
        r"""VolumeAttachment

        The model defined in huaweicloud sdk

        :param volume_id: 要挂卷的卷ID。可以从云硬盘控制台查询，或者通过调用“查询云硬盘列表”API获取。
        :type volume_id: str
        :param device: 磁盘挂载点，如/dev/sda、/dev/sdb。新增加的磁盘挂载点不能和已有的磁盘挂载点相同。需要根据已有设备名称顺序指定，否则不写device或device的值为空时，由系统自动生成。
        :type device: str
        """
        
        

        self._volume_id = None
        self._device = None
        self.discriminator = None

        self.volume_id = volume_id
        if device is not None:
            self.device = device

    @property
    def volume_id(self):
        r"""Gets the volume_id of this VolumeAttachment.

        要挂卷的卷ID。可以从云硬盘控制台查询，或者通过调用“查询云硬盘列表”API获取。

        :return: The volume_id of this VolumeAttachment.
        :rtype: str
        """
        return self._volume_id

    @volume_id.setter
    def volume_id(self, volume_id):
        r"""Sets the volume_id of this VolumeAttachment.

        要挂卷的卷ID。可以从云硬盘控制台查询，或者通过调用“查询云硬盘列表”API获取。

        :param volume_id: The volume_id of this VolumeAttachment.
        :type volume_id: str
        """
        self._volume_id = volume_id

    @property
    def device(self):
        r"""Gets the device of this VolumeAttachment.

        磁盘挂载点，如/dev/sda、/dev/sdb。新增加的磁盘挂载点不能和已有的磁盘挂载点相同。需要根据已有设备名称顺序指定，否则不写device或device的值为空时，由系统自动生成。

        :return: The device of this VolumeAttachment.
        :rtype: str
        """
        return self._device

    @device.setter
    def device(self, device):
        r"""Sets the device of this VolumeAttachment.

        磁盘挂载点，如/dev/sda、/dev/sdb。新增加的磁盘挂载点不能和已有的磁盘挂载点相同。需要根据已有设备名称顺序指定，否则不写device或device的值为空时，由系统自动生成。

        :param device: The device of this VolumeAttachment.
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
        if not isinstance(other, VolumeAttachment):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

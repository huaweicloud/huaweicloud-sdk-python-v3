# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class VolumeVO:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'volume_type': 'str',
        'size': 'str',
        'count': 'int'
    }

    attribute_map = {
        'volume_type': 'volumeType',
        'size': 'size',
        'count': 'count'
    }

    def __init__(self, volume_type=None, size=None, count=None):
        r"""VolumeVO

        The model defined in huaweicloud sdk

        :param volume_type: **参数解释**：磁盘类型[，具体内容可参考磁盘类型及性能介绍](tag:hc)。 **取值范围**：   - SSD：超高IO硬盘   - GPSSD：通用型SSD
        :type volume_type: str
        :param size: **参数解释**：磁盘大小，单位为Gi。 **取值范围**：不涉及。
        :type size: str
        :param count: **参数解释**：磁盘个数。不指定默认值为1。 **取值范围**：不涉及。
        :type count: int
        """
        
        

        self._volume_type = None
        self._size = None
        self._count = None
        self.discriminator = None

        self.volume_type = volume_type
        self.size = size
        if count is not None:
            self.count = count

    @property
    def volume_type(self):
        r"""Gets the volume_type of this VolumeVO.

        **参数解释**：磁盘类型[，具体内容可参考磁盘类型及性能介绍](tag:hc)。 **取值范围**：   - SSD：超高IO硬盘   - GPSSD：通用型SSD

        :return: The volume_type of this VolumeVO.
        :rtype: str
        """
        return self._volume_type

    @volume_type.setter
    def volume_type(self, volume_type):
        r"""Sets the volume_type of this VolumeVO.

        **参数解释**：磁盘类型[，具体内容可参考磁盘类型及性能介绍](tag:hc)。 **取值范围**：   - SSD：超高IO硬盘   - GPSSD：通用型SSD

        :param volume_type: The volume_type of this VolumeVO.
        :type volume_type: str
        """
        self._volume_type = volume_type

    @property
    def size(self):
        r"""Gets the size of this VolumeVO.

        **参数解释**：磁盘大小，单位为Gi。 **取值范围**：不涉及。

        :return: The size of this VolumeVO.
        :rtype: str
        """
        return self._size

    @size.setter
    def size(self, size):
        r"""Sets the size of this VolumeVO.

        **参数解释**：磁盘大小，单位为Gi。 **取值范围**：不涉及。

        :param size: The size of this VolumeVO.
        :type size: str
        """
        self._size = size

    @property
    def count(self):
        r"""Gets the count of this VolumeVO.

        **参数解释**：磁盘个数。不指定默认值为1。 **取值范围**：不涉及。

        :return: The count of this VolumeVO.
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        r"""Sets the count of this VolumeVO.

        **参数解释**：磁盘个数。不指定默认值为1。 **取值范围**：不涉及。

        :param count: The count of this VolumeVO.
        :type count: int
        """
        self._count = count

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
        if not isinstance(other, VolumeVO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

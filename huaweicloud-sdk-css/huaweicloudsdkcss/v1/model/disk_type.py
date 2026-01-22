# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DiskType:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'availability_zone': 'str',
        'volume_names': 'list[str]'
    }

    attribute_map = {
        'availability_zone': 'availabilityZone',
        'volume_names': 'volumeNames'
    }

    def __init__(self, availability_zone=None, volume_names=None):
        r"""DiskType

        The model defined in huaweicloud sdk

        :param availability_zone: **参数解释**： 可用区。 **取值范围**： 不涉及
        :type availability_zone: str
        :param volume_names: **参数解释**： 磁盘类型。 **取值范围**： - SATA：普通IO - SAS：高IO - SSD：超高IO - ESSD：极速型SSD
        :type volume_names: list[str]
        """
        
        

        self._availability_zone = None
        self._volume_names = None
        self.discriminator = None

        if availability_zone is not None:
            self.availability_zone = availability_zone
        if volume_names is not None:
            self.volume_names = volume_names

    @property
    def availability_zone(self):
        r"""Gets the availability_zone of this DiskType.

        **参数解释**： 可用区。 **取值范围**： 不涉及

        :return: The availability_zone of this DiskType.
        :rtype: str
        """
        return self._availability_zone

    @availability_zone.setter
    def availability_zone(self, availability_zone):
        r"""Sets the availability_zone of this DiskType.

        **参数解释**： 可用区。 **取值范围**： 不涉及

        :param availability_zone: The availability_zone of this DiskType.
        :type availability_zone: str
        """
        self._availability_zone = availability_zone

    @property
    def volume_names(self):
        r"""Gets the volume_names of this DiskType.

        **参数解释**： 磁盘类型。 **取值范围**： - SATA：普通IO - SAS：高IO - SSD：超高IO - ESSD：极速型SSD

        :return: The volume_names of this DiskType.
        :rtype: list[str]
        """
        return self._volume_names

    @volume_names.setter
    def volume_names(self, volume_names):
        r"""Sets the volume_names of this DiskType.

        **参数解释**： 磁盘类型。 **取值范围**： - SATA：普通IO - SAS：高IO - SSD：超高IO - ESSD：极速型SSD

        :param volume_names: The volume_names of this DiskType.
        :type volume_names: list[str]
        """
        self._volume_names = volume_names

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
        if not isinstance(other, DiskType):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

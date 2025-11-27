# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowVolumeInRecycleRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'volume_id': 'str'
    }

    attribute_map = {
        'volume_id': 'volume_id'
    }

    def __init__(self, volume_id=None):
        r"""ShowVolumeInRecycleRequest

        The model defined in huaweicloud sdk

        :param volume_id: **参数解释** 云硬盘ID。 可通过[查询所有云硬盘详情](evs_04_2006.xml)获取云硬盘ID。 **约束限制** 不涉及。 **取值范围** 不涉及。 **默认取值** 不涉及。
        :type volume_id: str
        """
        
        

        self._volume_id = None
        self.discriminator = None

        self.volume_id = volume_id

    @property
    def volume_id(self):
        r"""Gets the volume_id of this ShowVolumeInRecycleRequest.

        **参数解释** 云硬盘ID。 可通过[查询所有云硬盘详情](evs_04_2006.xml)获取云硬盘ID。 **约束限制** 不涉及。 **取值范围** 不涉及。 **默认取值** 不涉及。

        :return: The volume_id of this ShowVolumeInRecycleRequest.
        :rtype: str
        """
        return self._volume_id

    @volume_id.setter
    def volume_id(self, volume_id):
        r"""Sets the volume_id of this ShowVolumeInRecycleRequest.

        **参数解释** 云硬盘ID。 可通过[查询所有云硬盘详情](evs_04_2006.xml)获取云硬盘ID。 **约束限制** 不涉及。 **取值范围** 不涉及。 **默认取值** 不涉及。

        :param volume_id: The volume_id of this ShowVolumeInRecycleRequest.
        :type volume_id: str
        """
        self._volume_id = volume_id

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
        if not isinstance(other, ShowVolumeInRecycleRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

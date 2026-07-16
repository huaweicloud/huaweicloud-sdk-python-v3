# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DetachDevServerVolumeRequest:

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
        'volume_id': 'str'
    }

    attribute_map = {
        'id': 'id',
        'volume_id': 'volume_id'
    }

    def __init__(self, id=None, volume_id=None):
        r"""DetachDevServerVolumeRequest

        The model defined in huaweicloud sdk

        :param id: **参数解释**：Lite Server实例ID。 **约束限制**：^[0-9a-f]{8}-[0-9a-f]{4}-[1-5][0-9a-f]{3}-[89ab][0-9a-f]{3}-[0-9a-f]{12}$。 **取值范围**：不涉及。 **默认取值**：不涉及。
        :type id: str
        :param volume_id: **参数解释**：要卸载的磁盘ID。 **约束限制**：[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}。 **取值范围**：不涉及。 **默认取值**：不涉及。
        :type volume_id: str
        """
        
        

        self._id = None
        self._volume_id = None
        self.discriminator = None

        self.id = id
        self.volume_id = volume_id

    @property
    def id(self):
        r"""Gets the id of this DetachDevServerVolumeRequest.

        **参数解释**：Lite Server实例ID。 **约束限制**：^[0-9a-f]{8}-[0-9a-f]{4}-[1-5][0-9a-f]{3}-[89ab][0-9a-f]{3}-[0-9a-f]{12}$。 **取值范围**：不涉及。 **默认取值**：不涉及。

        :return: The id of this DetachDevServerVolumeRequest.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this DetachDevServerVolumeRequest.

        **参数解释**：Lite Server实例ID。 **约束限制**：^[0-9a-f]{8}-[0-9a-f]{4}-[1-5][0-9a-f]{3}-[89ab][0-9a-f]{3}-[0-9a-f]{12}$。 **取值范围**：不涉及。 **默认取值**：不涉及。

        :param id: The id of this DetachDevServerVolumeRequest.
        :type id: str
        """
        self._id = id

    @property
    def volume_id(self):
        r"""Gets the volume_id of this DetachDevServerVolumeRequest.

        **参数解释**：要卸载的磁盘ID。 **约束限制**：[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}。 **取值范围**：不涉及。 **默认取值**：不涉及。

        :return: The volume_id of this DetachDevServerVolumeRequest.
        :rtype: str
        """
        return self._volume_id

    @volume_id.setter
    def volume_id(self, volume_id):
        r"""Sets the volume_id of this DetachDevServerVolumeRequest.

        **参数解释**：要卸载的磁盘ID。 **约束限制**：[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}。 **取值范围**：不涉及。 **默认取值**：不涉及。

        :param volume_id: The volume_id of this DetachDevServerVolumeRequest.
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
        if not isinstance(other, DetachDevServerVolumeRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class EwPrivateNetworkSegmentsDto:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'private_network_segments': 'list[PrivateNetworkSegmentVO]'
    }

    attribute_map = {
        'private_network_segments': 'private_network_segments'
    }

    def __init__(self, private_network_segments=None):
        r"""EwPrivateNetworkSegmentsDto

        The model defined in huaweicloud sdk

        :param private_network_segments: **参数解释**： 私网网段的信息列表，用于东西向VPC防护引流 **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及
        :type private_network_segments: list[:class:`huaweicloudsdkcfw.v1.PrivateNetworkSegmentVO`]
        """
        
        

        self._private_network_segments = None
        self.discriminator = None

        self.private_network_segments = private_network_segments

    @property
    def private_network_segments(self):
        r"""Gets the private_network_segments of this EwPrivateNetworkSegmentsDto.

        **参数解释**： 私网网段的信息列表，用于东西向VPC防护引流 **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及

        :return: The private_network_segments of this EwPrivateNetworkSegmentsDto.
        :rtype: list[:class:`huaweicloudsdkcfw.v1.PrivateNetworkSegmentVO`]
        """
        return self._private_network_segments

    @private_network_segments.setter
    def private_network_segments(self, private_network_segments):
        r"""Sets the private_network_segments of this EwPrivateNetworkSegmentsDto.

        **参数解释**： 私网网段的信息列表，用于东西向VPC防护引流 **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及

        :param private_network_segments: The private_network_segments of this EwPrivateNetworkSegmentsDto.
        :type private_network_segments: list[:class:`huaweicloudsdkcfw.v1.PrivateNetworkSegmentVO`]
        """
        self._private_network_segments = private_network_segments

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
        if not isinstance(other, EwPrivateNetworkSegmentsDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

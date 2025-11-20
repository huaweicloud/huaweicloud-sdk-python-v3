# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AvailabilityZones:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'primary': 'str',
        'standby': 'str'
    }

    attribute_map = {
        'primary': 'primary',
        'standby': 'standby'
    }

    def __init__(self, primary=None, standby=None):
        r"""AvailabilityZones

        The model defined in huaweicloud sdk

        :param primary: - 参数解释：ESW实例默认主节点所在的可用区。 - 约束限制：1-128字符。 - 取值范围：当前区域可用区id。 - 默认取值：不涉及。
        :type primary: str
        :param standby: - 参数解释：ESW实例默认备节点所在的可用区。 - 约束限制：1-128字符。 - 取值范围：当前区域可用区id。 - 默认取值：不涉及。
        :type standby: str
        """
        
        

        self._primary = None
        self._standby = None
        self.discriminator = None

        self.primary = primary
        self.standby = standby

    @property
    def primary(self):
        r"""Gets the primary of this AvailabilityZones.

        - 参数解释：ESW实例默认主节点所在的可用区。 - 约束限制：1-128字符。 - 取值范围：当前区域可用区id。 - 默认取值：不涉及。

        :return: The primary of this AvailabilityZones.
        :rtype: str
        """
        return self._primary

    @primary.setter
    def primary(self, primary):
        r"""Sets the primary of this AvailabilityZones.

        - 参数解释：ESW实例默认主节点所在的可用区。 - 约束限制：1-128字符。 - 取值范围：当前区域可用区id。 - 默认取值：不涉及。

        :param primary: The primary of this AvailabilityZones.
        :type primary: str
        """
        self._primary = primary

    @property
    def standby(self):
        r"""Gets the standby of this AvailabilityZones.

        - 参数解释：ESW实例默认备节点所在的可用区。 - 约束限制：1-128字符。 - 取值范围：当前区域可用区id。 - 默认取值：不涉及。

        :return: The standby of this AvailabilityZones.
        :rtype: str
        """
        return self._standby

    @standby.setter
    def standby(self, standby):
        r"""Sets the standby of this AvailabilityZones.

        - 参数解释：ESW实例默认备节点所在的可用区。 - 约束限制：1-128字符。 - 取值范围：当前区域可用区id。 - 默认取值：不涉及。

        :param standby: The standby of this AvailabilityZones.
        :type standby: str
        """
        self._standby = standby

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
        if not isinstance(other, AvailabilityZones):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

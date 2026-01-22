# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BatchResetConsumeOffsetReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'groups': 'list[str]',
        'timestamp': 'int'
    }

    attribute_map = {
        'groups': 'groups',
        'timestamp': 'timestamp'
    }

    def __init__(self, groups=None, timestamp=None):
        r"""BatchResetConsumeOffsetReq

        The model defined in huaweicloud sdk

        :param groups: **参数解释**： 消费组列表。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。
        :type groups: list[str]
        :param timestamp: **参数解释**： 重置的时间。-1表示重置到最新位点。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。
        :type timestamp: int
        """
        
        

        self._groups = None
        self._timestamp = None
        self.discriminator = None

        if groups is not None:
            self.groups = groups
        if timestamp is not None:
            self.timestamp = timestamp

    @property
    def groups(self):
        r"""Gets the groups of this BatchResetConsumeOffsetReq.

        **参数解释**： 消费组列表。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。

        :return: The groups of this BatchResetConsumeOffsetReq.
        :rtype: list[str]
        """
        return self._groups

    @groups.setter
    def groups(self, groups):
        r"""Sets the groups of this BatchResetConsumeOffsetReq.

        **参数解释**： 消费组列表。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。

        :param groups: The groups of this BatchResetConsumeOffsetReq.
        :type groups: list[str]
        """
        self._groups = groups

    @property
    def timestamp(self):
        r"""Gets the timestamp of this BatchResetConsumeOffsetReq.

        **参数解释**： 重置的时间。-1表示重置到最新位点。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。

        :return: The timestamp of this BatchResetConsumeOffsetReq.
        :rtype: int
        """
        return self._timestamp

    @timestamp.setter
    def timestamp(self, timestamp):
        r"""Sets the timestamp of this BatchResetConsumeOffsetReq.

        **参数解释**： 重置的时间。-1表示重置到最新位点。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。

        :param timestamp: The timestamp of this BatchResetConsumeOffsetReq.
        :type timestamp: int
        """
        self._timestamp = timestamp

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
        if not isinstance(other, BatchResetConsumeOffsetReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

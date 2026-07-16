# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateCoreCodeInterpreterRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'observability': 'CoreToolsObservability',
        'tags': 'list[CoreToolsTag]'
    }

    attribute_map = {
        'observability': 'observability',
        'tags': 'tags'
    }

    def __init__(self, observability=None, tags=None):
        r"""UpdateCoreCodeInterpreterRequestBody

        The model defined in huaweicloud sdk

        :param observability: 
        :type observability: :class:`huaweicloudsdkagentarts.v1.CoreToolsObservability`
        :param tags: **参数解释：** 资源标签。 **约束范围：** 不涉及。 **取值范围：** 最多20个，且键值不能重复。 **默认取值：** 不涉及。
        :type tags: list[:class:`huaweicloudsdkagentarts.v1.CoreToolsTag`]
        """
        
        

        self._observability = None
        self._tags = None
        self.discriminator = None

        if observability is not None:
            self.observability = observability
        if tags is not None:
            self.tags = tags

    @property
    def observability(self):
        r"""Gets the observability of this UpdateCoreCodeInterpreterRequestBody.

        :return: The observability of this UpdateCoreCodeInterpreterRequestBody.
        :rtype: :class:`huaweicloudsdkagentarts.v1.CoreToolsObservability`
        """
        return self._observability

    @observability.setter
    def observability(self, observability):
        r"""Sets the observability of this UpdateCoreCodeInterpreterRequestBody.

        :param observability: The observability of this UpdateCoreCodeInterpreterRequestBody.
        :type observability: :class:`huaweicloudsdkagentarts.v1.CoreToolsObservability`
        """
        self._observability = observability

    @property
    def tags(self):
        r"""Gets the tags of this UpdateCoreCodeInterpreterRequestBody.

        **参数解释：** 资源标签。 **约束范围：** 不涉及。 **取值范围：** 最多20个，且键值不能重复。 **默认取值：** 不涉及。

        :return: The tags of this UpdateCoreCodeInterpreterRequestBody.
        :rtype: list[:class:`huaweicloudsdkagentarts.v1.CoreToolsTag`]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        r"""Sets the tags of this UpdateCoreCodeInterpreterRequestBody.

        **参数解释：** 资源标签。 **约束范围：** 不涉及。 **取值范围：** 最多20个，且键值不能重复。 **默认取值：** 不涉及。

        :param tags: The tags of this UpdateCoreCodeInterpreterRequestBody.
        :type tags: list[:class:`huaweicloudsdkagentarts.v1.CoreToolsTag`]
        """
        self._tags = tags

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
        if not isinstance(other, UpdateCoreCodeInterpreterRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

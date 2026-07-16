# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateImageGroupRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'read_me': 'str',
        'tags': 'list[UpdateImageGroupRequestBodyTags]'
    }

    attribute_map = {
        'read_me': 'read_me',
        'tags': 'tags'
    }

    def __init__(self, read_me=None, tags=None):
        r"""UpdateImageGroupRequestBody

        The model defined in huaweicloud sdk

        :param read_me: **参数解释**：镜像组更新的概览信息。 **约束限制**：不涉及。 **取值范围**：长度限制30000个字符。 **默认取值**：不涉及。
        :type read_me: str
        :param tags: **参数解释**：镜像组更新的标签。 **约束限制**：最大支持20个标签。 **取值范围**：key值最大支持长度128，value值最大支持255。 **默认取值**：不涉及。
        :type tags: list[:class:`huaweicloudsdkmodelarts.v1.UpdateImageGroupRequestBodyTags`]
        """
        
        

        self._read_me = None
        self._tags = None
        self.discriminator = None

        if read_me is not None:
            self.read_me = read_me
        if tags is not None:
            self.tags = tags

    @property
    def read_me(self):
        r"""Gets the read_me of this UpdateImageGroupRequestBody.

        **参数解释**：镜像组更新的概览信息。 **约束限制**：不涉及。 **取值范围**：长度限制30000个字符。 **默认取值**：不涉及。

        :return: The read_me of this UpdateImageGroupRequestBody.
        :rtype: str
        """
        return self._read_me

    @read_me.setter
    def read_me(self, read_me):
        r"""Sets the read_me of this UpdateImageGroupRequestBody.

        **参数解释**：镜像组更新的概览信息。 **约束限制**：不涉及。 **取值范围**：长度限制30000个字符。 **默认取值**：不涉及。

        :param read_me: The read_me of this UpdateImageGroupRequestBody.
        :type read_me: str
        """
        self._read_me = read_me

    @property
    def tags(self):
        r"""Gets the tags of this UpdateImageGroupRequestBody.

        **参数解释**：镜像组更新的标签。 **约束限制**：最大支持20个标签。 **取值范围**：key值最大支持长度128，value值最大支持255。 **默认取值**：不涉及。

        :return: The tags of this UpdateImageGroupRequestBody.
        :rtype: list[:class:`huaweicloudsdkmodelarts.v1.UpdateImageGroupRequestBodyTags`]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        r"""Sets the tags of this UpdateImageGroupRequestBody.

        **参数解释**：镜像组更新的标签。 **约束限制**：最大支持20个标签。 **取值范围**：key值最大支持长度128，value值最大支持255。 **默认取值**：不涉及。

        :param tags: The tags of this UpdateImageGroupRequestBody.
        :type tags: list[:class:`huaweicloudsdkmodelarts.v1.UpdateImageGroupRequestBodyTags`]
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
        if not isinstance(other, UpdateImageGroupRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

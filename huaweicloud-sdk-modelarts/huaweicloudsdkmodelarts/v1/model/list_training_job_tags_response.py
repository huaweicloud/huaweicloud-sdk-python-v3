# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListTrainingJobTagsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'tags': 'list[ProjectTag]'
    }

    attribute_map = {
        'tags': 'tags'
    }

    def __init__(self, tags=None):
        r"""ListTrainingJobTagsResponse

        The model defined in huaweicloud sdk

        :param tags: **参数解释**：标签列表，按key聚合，每个key下包含该项目下该key出现过的所有不同value。 **取值范围**：不涉及。
        :type tags: list[:class:`huaweicloudsdkmodelarts.v1.ProjectTag`]
        """
        
        super().__init__()

        self._tags = None
        self.discriminator = None

        if tags is not None:
            self.tags = tags

    @property
    def tags(self):
        r"""Gets the tags of this ListTrainingJobTagsResponse.

        **参数解释**：标签列表，按key聚合，每个key下包含该项目下该key出现过的所有不同value。 **取值范围**：不涉及。

        :return: The tags of this ListTrainingJobTagsResponse.
        :rtype: list[:class:`huaweicloudsdkmodelarts.v1.ProjectTag`]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        r"""Sets the tags of this ListTrainingJobTagsResponse.

        **参数解释**：标签列表，按key聚合，每个key下包含该项目下该key出现过的所有不同value。 **取值范围**：不涉及。

        :param tags: The tags of this ListTrainingJobTagsResponse.
        :type tags: list[:class:`huaweicloudsdkmodelarts.v1.ProjectTag`]
        """
        self._tags = tags

    def to_dict(self):
        import warnings
        warnings.warn("ListTrainingJobTagsResponse.to_dict() is deprecated and no longer maintained, "
                      "use to_json_object() to get the response content.", DeprecationWarning)
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
        if not isinstance(other, ListTrainingJobTagsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

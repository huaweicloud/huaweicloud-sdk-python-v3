# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DeleteInferTmsTagsRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'tags': 'list[TmsTagForDeletion]',
        'resource_id': 'str'
    }

    attribute_map = {
        'tags': 'tags',
        'resource_id': 'resource_id'
    }

    def __init__(self, tags=None, resource_id=None):
        r"""DeleteInferTmsTagsRequest

        The model defined in huaweicloud sdk

        :param tags: **参数解释：** 要删除的标签列表。
        :type tags: list[:class:`huaweicloudsdkmodelarts.v1.TmsTagForDeletion`]
        :param resource_id: **参数解释：** 待删除标签的资源ID。 **取值范围：** 不涉及。
        :type resource_id: str
        """
        
        

        self._tags = None
        self._resource_id = None
        self.discriminator = None

        self.tags = tags
        if resource_id is not None:
            self.resource_id = resource_id

    @property
    def tags(self):
        r"""Gets the tags of this DeleteInferTmsTagsRequest.

        **参数解释：** 要删除的标签列表。

        :return: The tags of this DeleteInferTmsTagsRequest.
        :rtype: list[:class:`huaweicloudsdkmodelarts.v1.TmsTagForDeletion`]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        r"""Sets the tags of this DeleteInferTmsTagsRequest.

        **参数解释：** 要删除的标签列表。

        :param tags: The tags of this DeleteInferTmsTagsRequest.
        :type tags: list[:class:`huaweicloudsdkmodelarts.v1.TmsTagForDeletion`]
        """
        self._tags = tags

    @property
    def resource_id(self):
        r"""Gets the resource_id of this DeleteInferTmsTagsRequest.

        **参数解释：** 待删除标签的资源ID。 **取值范围：** 不涉及。

        :return: The resource_id of this DeleteInferTmsTagsRequest.
        :rtype: str
        """
        return self._resource_id

    @resource_id.setter
    def resource_id(self, resource_id):
        r"""Sets the resource_id of this DeleteInferTmsTagsRequest.

        **参数解释：** 待删除标签的资源ID。 **取值范围：** 不涉及。

        :param resource_id: The resource_id of this DeleteInferTmsTagsRequest.
        :type resource_id: str
        """
        self._resource_id = resource_id

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
        if not isinstance(other, DeleteInferTmsTagsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

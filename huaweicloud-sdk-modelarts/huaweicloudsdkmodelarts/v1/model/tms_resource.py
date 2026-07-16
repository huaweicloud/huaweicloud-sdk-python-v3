# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class TmsResource:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'resource_detail': 'object',
        'resource_id': 'str',
        'resource_name': 'str',
        'tags': 'list[InferTmsTag]'
    }

    attribute_map = {
        'resource_detail': 'resource_detail',
        'resource_id': 'resource_id',
        'resource_name': 'resource_name',
        'tags': 'tags'
    }

    def __init__(self, resource_detail=None, resource_id=None, resource_name=None, tags=None):
        r"""TmsResource

        The model defined in huaweicloud sdk

        :param resource_detail: **参数解释：** 资源详情，用于扩展，默认为空。 **取值范围：** 不涉及
        :type resource_detail: object
        :param resource_id: **参数解释：** 资源ID。 **取值范围：** 不涉及
        :type resource_id: str
        :param resource_name: **参数解释：** 资源名称。 **取值范围：** 不涉及
        :type resource_name: str
        :param tags: **参数解释：** 当前资源的所有标签。 **取值范围：** 不涉及
        :type tags: list[:class:`huaweicloudsdkmodelarts.v1.InferTmsTag`]
        """
        
        

        self._resource_detail = None
        self._resource_id = None
        self._resource_name = None
        self._tags = None
        self.discriminator = None

        self.resource_detail = resource_detail
        self.resource_id = resource_id
        self.resource_name = resource_name
        self.tags = tags

    @property
    def resource_detail(self):
        r"""Gets the resource_detail of this TmsResource.

        **参数解释：** 资源详情，用于扩展，默认为空。 **取值范围：** 不涉及

        :return: The resource_detail of this TmsResource.
        :rtype: object
        """
        return self._resource_detail

    @resource_detail.setter
    def resource_detail(self, resource_detail):
        r"""Sets the resource_detail of this TmsResource.

        **参数解释：** 资源详情，用于扩展，默认为空。 **取值范围：** 不涉及

        :param resource_detail: The resource_detail of this TmsResource.
        :type resource_detail: object
        """
        self._resource_detail = resource_detail

    @property
    def resource_id(self):
        r"""Gets the resource_id of this TmsResource.

        **参数解释：** 资源ID。 **取值范围：** 不涉及

        :return: The resource_id of this TmsResource.
        :rtype: str
        """
        return self._resource_id

    @resource_id.setter
    def resource_id(self, resource_id):
        r"""Sets the resource_id of this TmsResource.

        **参数解释：** 资源ID。 **取值范围：** 不涉及

        :param resource_id: The resource_id of this TmsResource.
        :type resource_id: str
        """
        self._resource_id = resource_id

    @property
    def resource_name(self):
        r"""Gets the resource_name of this TmsResource.

        **参数解释：** 资源名称。 **取值范围：** 不涉及

        :return: The resource_name of this TmsResource.
        :rtype: str
        """
        return self._resource_name

    @resource_name.setter
    def resource_name(self, resource_name):
        r"""Sets the resource_name of this TmsResource.

        **参数解释：** 资源名称。 **取值范围：** 不涉及

        :param resource_name: The resource_name of this TmsResource.
        :type resource_name: str
        """
        self._resource_name = resource_name

    @property
    def tags(self):
        r"""Gets the tags of this TmsResource.

        **参数解释：** 当前资源的所有标签。 **取值范围：** 不涉及

        :return: The tags of this TmsResource.
        :rtype: list[:class:`huaweicloudsdkmodelarts.v1.InferTmsTag`]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        r"""Sets the tags of this TmsResource.

        **参数解释：** 当前资源的所有标签。 **取值范围：** 不涉及

        :param tags: The tags of this TmsResource.
        :type tags: list[:class:`huaweicloudsdkmodelarts.v1.InferTmsTag`]
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
        if not isinstance(other, TmsResource):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

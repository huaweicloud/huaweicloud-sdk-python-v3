# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class OpsTmsResource:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'resource_id': 'str',
        'resource_detail': 'object',
        'tags': 'list[OpsTmsTag]',
        'sys_tags': 'list[OpsTmsTag]',
        'resource_name': 'str'
    }

    attribute_map = {
        'resource_id': 'resource_id',
        'resource_detail': 'resource_detail',
        'tags': 'tags',
        'sys_tags': 'sys_tags',
        'resource_name': 'resource_name'
    }

    def __init__(self, resource_id=None, resource_detail=None, tags=None, sys_tags=None, resource_name=None):
        r"""OpsTmsResource

        The model defined in huaweicloud sdk

        :param resource_id: **参数解释：** 资源的唯一标识符。 **约束限制：** 不涉及。 **取值范围：** 不涉及。
        :type resource_id: str
        :param resource_detail: **参数解释：** 资源详细信息对象。 **约束限制：** 不涉及。
        :type resource_detail: object
        :param tags: **参数解释：** 资源绑定的自定义标签列表。数组元素为OpsTmsTag对象，包含key和value字段。 **约束限制：** 不涉及。
        :type tags: list[:class:`huaweicloudsdkagentarts.v1.OpsTmsTag`]
        :param sys_tags: **参数解释：** 资源绑定的系统标签列表。数组元素为OpsTmsTag对象，包含key和value字段。 **约束限制：** 不涉及。
        :type sys_tags: list[:class:`huaweicloudsdkagentarts.v1.OpsTmsTag`]
        :param resource_name: **参数解释：** 资源名称。 **约束限制：** 不涉及。 **取值范围：** 不涉及。
        :type resource_name: str
        """
        
        

        self._resource_id = None
        self._resource_detail = None
        self._tags = None
        self._sys_tags = None
        self._resource_name = None
        self.discriminator = None

        if resource_id is not None:
            self.resource_id = resource_id
        if resource_detail is not None:
            self.resource_detail = resource_detail
        if tags is not None:
            self.tags = tags
        if sys_tags is not None:
            self.sys_tags = sys_tags
        if resource_name is not None:
            self.resource_name = resource_name

    @property
    def resource_id(self):
        r"""Gets the resource_id of this OpsTmsResource.

        **参数解释：** 资源的唯一标识符。 **约束限制：** 不涉及。 **取值范围：** 不涉及。

        :return: The resource_id of this OpsTmsResource.
        :rtype: str
        """
        return self._resource_id

    @resource_id.setter
    def resource_id(self, resource_id):
        r"""Sets the resource_id of this OpsTmsResource.

        **参数解释：** 资源的唯一标识符。 **约束限制：** 不涉及。 **取值范围：** 不涉及。

        :param resource_id: The resource_id of this OpsTmsResource.
        :type resource_id: str
        """
        self._resource_id = resource_id

    @property
    def resource_detail(self):
        r"""Gets the resource_detail of this OpsTmsResource.

        **参数解释：** 资源详细信息对象。 **约束限制：** 不涉及。

        :return: The resource_detail of this OpsTmsResource.
        :rtype: object
        """
        return self._resource_detail

    @resource_detail.setter
    def resource_detail(self, resource_detail):
        r"""Sets the resource_detail of this OpsTmsResource.

        **参数解释：** 资源详细信息对象。 **约束限制：** 不涉及。

        :param resource_detail: The resource_detail of this OpsTmsResource.
        :type resource_detail: object
        """
        self._resource_detail = resource_detail

    @property
    def tags(self):
        r"""Gets the tags of this OpsTmsResource.

        **参数解释：** 资源绑定的自定义标签列表。数组元素为OpsTmsTag对象，包含key和value字段。 **约束限制：** 不涉及。

        :return: The tags of this OpsTmsResource.
        :rtype: list[:class:`huaweicloudsdkagentarts.v1.OpsTmsTag`]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        r"""Sets the tags of this OpsTmsResource.

        **参数解释：** 资源绑定的自定义标签列表。数组元素为OpsTmsTag对象，包含key和value字段。 **约束限制：** 不涉及。

        :param tags: The tags of this OpsTmsResource.
        :type tags: list[:class:`huaweicloudsdkagentarts.v1.OpsTmsTag`]
        """
        self._tags = tags

    @property
    def sys_tags(self):
        r"""Gets the sys_tags of this OpsTmsResource.

        **参数解释：** 资源绑定的系统标签列表。数组元素为OpsTmsTag对象，包含key和value字段。 **约束限制：** 不涉及。

        :return: The sys_tags of this OpsTmsResource.
        :rtype: list[:class:`huaweicloudsdkagentarts.v1.OpsTmsTag`]
        """
        return self._sys_tags

    @sys_tags.setter
    def sys_tags(self, sys_tags):
        r"""Sets the sys_tags of this OpsTmsResource.

        **参数解释：** 资源绑定的系统标签列表。数组元素为OpsTmsTag对象，包含key和value字段。 **约束限制：** 不涉及。

        :param sys_tags: The sys_tags of this OpsTmsResource.
        :type sys_tags: list[:class:`huaweicloudsdkagentarts.v1.OpsTmsTag`]
        """
        self._sys_tags = sys_tags

    @property
    def resource_name(self):
        r"""Gets the resource_name of this OpsTmsResource.

        **参数解释：** 资源名称。 **约束限制：** 不涉及。 **取值范围：** 不涉及。

        :return: The resource_name of this OpsTmsResource.
        :rtype: str
        """
        return self._resource_name

    @resource_name.setter
    def resource_name(self, resource_name):
        r"""Sets the resource_name of this OpsTmsResource.

        **参数解释：** 资源名称。 **约束限制：** 不涉及。 **取值范围：** 不涉及。

        :param resource_name: The resource_name of this OpsTmsResource.
        :type resource_name: str
        """
        self._resource_name = resource_name

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
        if not isinstance(other, OpsTmsResource):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

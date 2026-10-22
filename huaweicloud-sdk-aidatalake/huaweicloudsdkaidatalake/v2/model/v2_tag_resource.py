# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class V2TagResource:

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
        'resource_name': 'str',
        'tags': 'list[ResourceTag]',
        'sys_tags': 'list[SystemTag]'
    }

    attribute_map = {
        'resource_id': 'resource_id',
        'resource_detail': 'resource_detail',
        'resource_name': 'resource_name',
        'tags': 'tags',
        'sys_tags': 'sys_tags'
    }

    def __init__(self, resource_id=None, resource_detail=None, resource_name=None, tags=None, sys_tags=None):
        r"""V2TagResource

        The model defined in huaweicloud sdk

        :param resource_id: **参数解释**：标签资源ID。 **取值范围**：由英文字母、数字和中划线组成，长度不超过64个字符。 
        :type resource_id: str
        :param resource_detail: **参数解释**：标签资源详情。 资源对象，用于扩展。默认为空。 
        :type resource_detail: object
        :param resource_name: **参数解释**：标签资源名称。 **取值范围**：不涉及。 
        :type resource_name: str
        :param tags: **参数解释**：标签列表，没有标签默认为空数组，每个元素为一个ResourceTag对象，包含key（标签键）和value（标签值）字段。 
        :type tags: list[:class:`huaweicloudsdkaidatalake.v2.ResourceTag`]
        :param sys_tags: **参数解释**：系统标签列表，没有系统标签默认不返回，每个元素为一个SystemTag对象，包含key（系统标签键）和value（系统标签值）字段。 
        :type sys_tags: list[:class:`huaweicloudsdkaidatalake.v2.SystemTag`]
        """
        
        

        self._resource_id = None
        self._resource_detail = None
        self._resource_name = None
        self._tags = None
        self._sys_tags = None
        self.discriminator = None

        if resource_id is not None:
            self.resource_id = resource_id
        if resource_detail is not None:
            self.resource_detail = resource_detail
        if resource_name is not None:
            self.resource_name = resource_name
        if tags is not None:
            self.tags = tags
        if sys_tags is not None:
            self.sys_tags = sys_tags

    @property
    def resource_id(self):
        r"""Gets the resource_id of this V2TagResource.

        **参数解释**：标签资源ID。 **取值范围**：由英文字母、数字和中划线组成，长度不超过64个字符。 

        :return: The resource_id of this V2TagResource.
        :rtype: str
        """
        return self._resource_id

    @resource_id.setter
    def resource_id(self, resource_id):
        r"""Sets the resource_id of this V2TagResource.

        **参数解释**：标签资源ID。 **取值范围**：由英文字母、数字和中划线组成，长度不超过64个字符。 

        :param resource_id: The resource_id of this V2TagResource.
        :type resource_id: str
        """
        self._resource_id = resource_id

    @property
    def resource_detail(self):
        r"""Gets the resource_detail of this V2TagResource.

        **参数解释**：标签资源详情。 资源对象，用于扩展。默认为空。 

        :return: The resource_detail of this V2TagResource.
        :rtype: object
        """
        return self._resource_detail

    @resource_detail.setter
    def resource_detail(self, resource_detail):
        r"""Sets the resource_detail of this V2TagResource.

        **参数解释**：标签资源详情。 资源对象，用于扩展。默认为空。 

        :param resource_detail: The resource_detail of this V2TagResource.
        :type resource_detail: object
        """
        self._resource_detail = resource_detail

    @property
    def resource_name(self):
        r"""Gets the resource_name of this V2TagResource.

        **参数解释**：标签资源名称。 **取值范围**：不涉及。 

        :return: The resource_name of this V2TagResource.
        :rtype: str
        """
        return self._resource_name

    @resource_name.setter
    def resource_name(self, resource_name):
        r"""Sets the resource_name of this V2TagResource.

        **参数解释**：标签资源名称。 **取值范围**：不涉及。 

        :param resource_name: The resource_name of this V2TagResource.
        :type resource_name: str
        """
        self._resource_name = resource_name

    @property
    def tags(self):
        r"""Gets the tags of this V2TagResource.

        **参数解释**：标签列表，没有标签默认为空数组，每个元素为一个ResourceTag对象，包含key（标签键）和value（标签值）字段。 

        :return: The tags of this V2TagResource.
        :rtype: list[:class:`huaweicloudsdkaidatalake.v2.ResourceTag`]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        r"""Sets the tags of this V2TagResource.

        **参数解释**：标签列表，没有标签默认为空数组，每个元素为一个ResourceTag对象，包含key（标签键）和value（标签值）字段。 

        :param tags: The tags of this V2TagResource.
        :type tags: list[:class:`huaweicloudsdkaidatalake.v2.ResourceTag`]
        """
        self._tags = tags

    @property
    def sys_tags(self):
        r"""Gets the sys_tags of this V2TagResource.

        **参数解释**：系统标签列表，没有系统标签默认不返回，每个元素为一个SystemTag对象，包含key（系统标签键）和value（系统标签值）字段。 

        :return: The sys_tags of this V2TagResource.
        :rtype: list[:class:`huaweicloudsdkaidatalake.v2.SystemTag`]
        """
        return self._sys_tags

    @sys_tags.setter
    def sys_tags(self, sys_tags):
        r"""Sets the sys_tags of this V2TagResource.

        **参数解释**：系统标签列表，没有系统标签默认不返回，每个元素为一个SystemTag对象，包含key（系统标签键）和value（系统标签值）字段。 

        :param sys_tags: The sys_tags of this V2TagResource.
        :type sys_tags: list[:class:`huaweicloudsdkaidatalake.v2.SystemTag`]
        """
        self._sys_tags = sys_tags

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
        if not isinstance(other, V2TagResource):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

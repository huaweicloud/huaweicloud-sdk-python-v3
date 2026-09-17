# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateOpsDatasetRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'name': 'str',
        'description': 'str',
        'schemas': 'list[CreateOpsSchemaRequest]',
        'use_default_schema': 'bool',
        'tags': 'list[OpsTmsTag]'
    }

    attribute_map = {
        'name': 'name',
        'description': 'description',
        'schemas': 'schemas',
        'use_default_schema': 'use_default_schema',
        'tags': 'tags'
    }

    def __init__(self, name=None, description=None, schemas=None, use_default_schema=None, tags=None):
        r"""CreateOpsDatasetRequestBody

        The model defined in huaweicloud sdk

        :param name: **参数解释：** 评测集的名称。 **约束限制：** 字符串长度2-50字符，租户内唯一。 **取值范围：** 支持中英文、数字、下划线（_）、中划线（-）和空格，长度2-50字符，但不允许以空格开头或结尾。 **默认取值：** 不涉及。
        :type name: str
        :param description: **参数解释：** 评测集的用途及业务背景描述。 **约束限制：** 长度0-200字符。 **取值范围：** 任意字符串。 **默认取值：** 不涉及。
        :type description: str
        :param schemas: **参数解释：** 定义评测集结构的一组字段配置列表。 **约束限制：** 列表元素数量上限为50个。 **取值范围：** CreateOpsSchemaRequest 对象数组。 **默认取值：** 空列表。
        :type schemas: list[:class:`huaweicloudsdkagentarts.v1.CreateOpsSchemaRequest`]
        :param use_default_schema: **参数解释：** 是否使用平台默认的字段定义。为true时使用默认Schema，此时可不传schemas。 **约束限制：** 不涉及。 **取值范围：** - true：使用默认字段定义 - false：使用自定义字段定义 **默认取值：** false。
        :type use_default_schema: bool
        :param tags: **参数解释：** 创建评测集时绑定的TMS标签列表，默认为空列表。 **约束限制：** 数组长度0到50。 **取值范围：** 不涉及。 **默认取值：** 不涉及。
        :type tags: list[:class:`huaweicloudsdkagentarts.v1.OpsTmsTag`]
        """
        
        

        self._name = None
        self._description = None
        self._schemas = None
        self._use_default_schema = None
        self._tags = None
        self.discriminator = None

        self.name = name
        if description is not None:
            self.description = description
        if schemas is not None:
            self.schemas = schemas
        if use_default_schema is not None:
            self.use_default_schema = use_default_schema
        if tags is not None:
            self.tags = tags

    @property
    def name(self):
        r"""Gets the name of this CreateOpsDatasetRequestBody.

        **参数解释：** 评测集的名称。 **约束限制：** 字符串长度2-50字符，租户内唯一。 **取值范围：** 支持中英文、数字、下划线（_）、中划线（-）和空格，长度2-50字符，但不允许以空格开头或结尾。 **默认取值：** 不涉及。

        :return: The name of this CreateOpsDatasetRequestBody.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this CreateOpsDatasetRequestBody.

        **参数解释：** 评测集的名称。 **约束限制：** 字符串长度2-50字符，租户内唯一。 **取值范围：** 支持中英文、数字、下划线（_）、中划线（-）和空格，长度2-50字符，但不允许以空格开头或结尾。 **默认取值：** 不涉及。

        :param name: The name of this CreateOpsDatasetRequestBody.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        r"""Gets the description of this CreateOpsDatasetRequestBody.

        **参数解释：** 评测集的用途及业务背景描述。 **约束限制：** 长度0-200字符。 **取值范围：** 任意字符串。 **默认取值：** 不涉及。

        :return: The description of this CreateOpsDatasetRequestBody.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this CreateOpsDatasetRequestBody.

        **参数解释：** 评测集的用途及业务背景描述。 **约束限制：** 长度0-200字符。 **取值范围：** 任意字符串。 **默认取值：** 不涉及。

        :param description: The description of this CreateOpsDatasetRequestBody.
        :type description: str
        """
        self._description = description

    @property
    def schemas(self):
        r"""Gets the schemas of this CreateOpsDatasetRequestBody.

        **参数解释：** 定义评测集结构的一组字段配置列表。 **约束限制：** 列表元素数量上限为50个。 **取值范围：** CreateOpsSchemaRequest 对象数组。 **默认取值：** 空列表。

        :return: The schemas of this CreateOpsDatasetRequestBody.
        :rtype: list[:class:`huaweicloudsdkagentarts.v1.CreateOpsSchemaRequest`]
        """
        return self._schemas

    @schemas.setter
    def schemas(self, schemas):
        r"""Sets the schemas of this CreateOpsDatasetRequestBody.

        **参数解释：** 定义评测集结构的一组字段配置列表。 **约束限制：** 列表元素数量上限为50个。 **取值范围：** CreateOpsSchemaRequest 对象数组。 **默认取值：** 空列表。

        :param schemas: The schemas of this CreateOpsDatasetRequestBody.
        :type schemas: list[:class:`huaweicloudsdkagentarts.v1.CreateOpsSchemaRequest`]
        """
        self._schemas = schemas

    @property
    def use_default_schema(self):
        r"""Gets the use_default_schema of this CreateOpsDatasetRequestBody.

        **参数解释：** 是否使用平台默认的字段定义。为true时使用默认Schema，此时可不传schemas。 **约束限制：** 不涉及。 **取值范围：** - true：使用默认字段定义 - false：使用自定义字段定义 **默认取值：** false。

        :return: The use_default_schema of this CreateOpsDatasetRequestBody.
        :rtype: bool
        """
        return self._use_default_schema

    @use_default_schema.setter
    def use_default_schema(self, use_default_schema):
        r"""Sets the use_default_schema of this CreateOpsDatasetRequestBody.

        **参数解释：** 是否使用平台默认的字段定义。为true时使用默认Schema，此时可不传schemas。 **约束限制：** 不涉及。 **取值范围：** - true：使用默认字段定义 - false：使用自定义字段定义 **默认取值：** false。

        :param use_default_schema: The use_default_schema of this CreateOpsDatasetRequestBody.
        :type use_default_schema: bool
        """
        self._use_default_schema = use_default_schema

    @property
    def tags(self):
        r"""Gets the tags of this CreateOpsDatasetRequestBody.

        **参数解释：** 创建评测集时绑定的TMS标签列表，默认为空列表。 **约束限制：** 数组长度0到50。 **取值范围：** 不涉及。 **默认取值：** 不涉及。

        :return: The tags of this CreateOpsDatasetRequestBody.
        :rtype: list[:class:`huaweicloudsdkagentarts.v1.OpsTmsTag`]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        r"""Sets the tags of this CreateOpsDatasetRequestBody.

        **参数解释：** 创建评测集时绑定的TMS标签列表，默认为空列表。 **约束限制：** 数组长度0到50。 **取值范围：** 不涉及。 **默认取值：** 不涉及。

        :param tags: The tags of this CreateOpsDatasetRequestBody.
        :type tags: list[:class:`huaweicloudsdkagentarts.v1.OpsTmsTag`]
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
        if not isinstance(other, CreateOpsDatasetRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

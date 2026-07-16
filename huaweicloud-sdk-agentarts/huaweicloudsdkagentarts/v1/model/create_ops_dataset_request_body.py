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
        'schemas': 'list[CreateOpsSchemaRequest]'
    }

    attribute_map = {
        'name': 'name',
        'description': 'description',
        'schemas': 'schemas'
    }

    def __init__(self, name=None, description=None, schemas=None):
        r"""CreateOpsDatasetRequestBody

        The model defined in huaweicloud sdk

        :param name: **参数解释：** 评测集的名称。 **约束限制：** 字符串长度2-50字符，租户内唯一。 **取值范围：** 支持中英文、数字、下划线（_）、中划线（-）和空格，长度2-50字符，但不允许以空格开头或结尾。 **默认取值：** 不涉及。
        :type name: str
        :param description: **参数解释：** 评测集的用途及业务背景描述。 **约束限制：** 长度0-200字符。 **取值范围：** 任意字符串。 **默认取值：** 不涉及。
        :type description: str
        :param schemas: **参数解释：** 定义评测集结构的一组字段配置列表。 **约束限制：** 列表元素数量上限为50个。 **取值范围：** CreateOpsSchemaRequest 对象数组。 **默认取值：** 空列表。
        :type schemas: list[:class:`huaweicloudsdkagentarts.v1.CreateOpsSchemaRequest`]
        """
        
        

        self._name = None
        self._description = None
        self._schemas = None
        self.discriminator = None

        self.name = name
        if description is not None:
            self.description = description
        if schemas is not None:
            self.schemas = schemas

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

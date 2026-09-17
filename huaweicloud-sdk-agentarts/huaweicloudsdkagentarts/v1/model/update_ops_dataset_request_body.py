# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateOpsDatasetRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'tags': 'list[OpsTmsTag]',
        'schemas': 'list[OpsCreateSchemaRequest]',
        'name': 'str',
        'description': 'str'
    }

    attribute_map = {
        'tags': 'tags',
        'schemas': 'schemas',
        'name': 'name',
        'description': 'description'
    }

    def __init__(self, tags=None, schemas=None, name=None, description=None):
        r"""UpdateOpsDatasetRequestBody

        The model defined in huaweicloud sdk

        :param tags: **参数解释：** 更新评测集时绑定的TMS标签列表，传入则全量替换。 **约束限制：** 数组元素最小数量为0，最大数量为50。 **取值范围：** 不涉及。 **默认取值：** 不涉及。
        :type tags: list[:class:`huaweicloudsdkagentarts.v1.OpsTmsTag`]
        :param schemas: **参数解释：** 定义评测集结构的一组字段配置列表。 **约束限制：** 数组元素最小数量为0，最大数量为50。 **取值范围：** 不涉及。 **默认取值：** 不涉及。
        :type schemas: list[:class:`huaweicloudsdkagentarts.v1.OpsCreateSchemaRequest`]
        :param name: **参数解释：** 待更新的评测集显示名称。 **约束限制：** 必填参数；长度1到255字符。 **取值范围：** 中英文、数字、下划线（_）、中划线（-）等。 **默认取值：** 不涉及。 
        :type name: str
        :param description: **参数解释：** 待更新的评测集用途或内容详细描述。 **约束限制：** 可选参数；长度0到200字符。 **取值范围：** 任意字符串。 **默认取值：** 不涉及。 
        :type description: str
        """
        
        

        self._tags = None
        self._schemas = None
        self._name = None
        self._description = None
        self.discriminator = None

        if tags is not None:
            self.tags = tags
        if schemas is not None:
            self.schemas = schemas
        self.name = name
        if description is not None:
            self.description = description

    @property
    def tags(self):
        r"""Gets the tags of this UpdateOpsDatasetRequestBody.

        **参数解释：** 更新评测集时绑定的TMS标签列表，传入则全量替换。 **约束限制：** 数组元素最小数量为0，最大数量为50。 **取值范围：** 不涉及。 **默认取值：** 不涉及。

        :return: The tags of this UpdateOpsDatasetRequestBody.
        :rtype: list[:class:`huaweicloudsdkagentarts.v1.OpsTmsTag`]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        r"""Sets the tags of this UpdateOpsDatasetRequestBody.

        **参数解释：** 更新评测集时绑定的TMS标签列表，传入则全量替换。 **约束限制：** 数组元素最小数量为0，最大数量为50。 **取值范围：** 不涉及。 **默认取值：** 不涉及。

        :param tags: The tags of this UpdateOpsDatasetRequestBody.
        :type tags: list[:class:`huaweicloudsdkagentarts.v1.OpsTmsTag`]
        """
        self._tags = tags

    @property
    def schemas(self):
        r"""Gets the schemas of this UpdateOpsDatasetRequestBody.

        **参数解释：** 定义评测集结构的一组字段配置列表。 **约束限制：** 数组元素最小数量为0，最大数量为50。 **取值范围：** 不涉及。 **默认取值：** 不涉及。

        :return: The schemas of this UpdateOpsDatasetRequestBody.
        :rtype: list[:class:`huaweicloudsdkagentarts.v1.OpsCreateSchemaRequest`]
        """
        return self._schemas

    @schemas.setter
    def schemas(self, schemas):
        r"""Sets the schemas of this UpdateOpsDatasetRequestBody.

        **参数解释：** 定义评测集结构的一组字段配置列表。 **约束限制：** 数组元素最小数量为0，最大数量为50。 **取值范围：** 不涉及。 **默认取值：** 不涉及。

        :param schemas: The schemas of this UpdateOpsDatasetRequestBody.
        :type schemas: list[:class:`huaweicloudsdkagentarts.v1.OpsCreateSchemaRequest`]
        """
        self._schemas = schemas

    @property
    def name(self):
        r"""Gets the name of this UpdateOpsDatasetRequestBody.

        **参数解释：** 待更新的评测集显示名称。 **约束限制：** 必填参数；长度1到255字符。 **取值范围：** 中英文、数字、下划线（_）、中划线（-）等。 **默认取值：** 不涉及。 

        :return: The name of this UpdateOpsDatasetRequestBody.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this UpdateOpsDatasetRequestBody.

        **参数解释：** 待更新的评测集显示名称。 **约束限制：** 必填参数；长度1到255字符。 **取值范围：** 中英文、数字、下划线（_）、中划线（-）等。 **默认取值：** 不涉及。 

        :param name: The name of this UpdateOpsDatasetRequestBody.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        r"""Gets the description of this UpdateOpsDatasetRequestBody.

        **参数解释：** 待更新的评测集用途或内容详细描述。 **约束限制：** 可选参数；长度0到200字符。 **取值范围：** 任意字符串。 **默认取值：** 不涉及。 

        :return: The description of this UpdateOpsDatasetRequestBody.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this UpdateOpsDatasetRequestBody.

        **参数解释：** 待更新的评测集用途或内容详细描述。 **约束限制：** 可选参数；长度0到200字符。 **取值范围：** 任意字符串。 **默认取值：** 不涉及。 

        :param description: The description of this UpdateOpsDatasetRequestBody.
        :type description: str
        """
        self._description = description

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
        if not isinstance(other, UpdateOpsDatasetRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateOpsLabelRequestBody:

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
        'type': 'str',
        'description': 'str',
        'enums': 'list[OpsLabelValueItem]'
    }

    attribute_map = {
        'name': 'name',
        'type': 'type',
        'description': 'description',
        'enums': 'enums'
    }

    def __init__(self, name=None, type=None, description=None, enums=None):
        r"""CreateOpsLabelRequestBody

        The model defined in huaweicloud sdk

        :param name: **参数解释：** 待创建的标签名称。 **约束限制：** 字符串长度为0到100个字符。 **取值范围：** 长度为0-100。 **默认取值：** 不涉及。 
        :type name: str
        :param type: **参数解释：** 标签的类型（如 free-text 等），用于定义标签的交互或存储逻辑。 **约束限制：** 字符串长度为0到100个字符。 **取值范围：** 长度为0-100。 **默认取值：** 不涉及。 
        :type type: str
        :param description: **参数解释：** 对该标签用途或含义的详细描述。 **约束限制：** 字符串长度为0到400个字符。 **取值范围：** 长度为0-400。 **默认取值：** 不涉及。 
        :type description: str
        :param enums: **参数解释：** 标签的可选值（枚举）列表，定义该标签下包含的具体标记项。 **约束限制：** 数组长度为0到100。 **取值范围：** 不涉及。 **默认取值：** 空列表。 
        :type enums: list[:class:`huaweicloudsdkagentarts.v1.OpsLabelValueItem`]
        """
        
        

        self._name = None
        self._type = None
        self._description = None
        self._enums = None
        self.discriminator = None

        self.name = name
        self.type = type
        if description is not None:
            self.description = description
        self.enums = enums

    @property
    def name(self):
        r"""Gets the name of this CreateOpsLabelRequestBody.

        **参数解释：** 待创建的标签名称。 **约束限制：** 字符串长度为0到100个字符。 **取值范围：** 长度为0-100。 **默认取值：** 不涉及。 

        :return: The name of this CreateOpsLabelRequestBody.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this CreateOpsLabelRequestBody.

        **参数解释：** 待创建的标签名称。 **约束限制：** 字符串长度为0到100个字符。 **取值范围：** 长度为0-100。 **默认取值：** 不涉及。 

        :param name: The name of this CreateOpsLabelRequestBody.
        :type name: str
        """
        self._name = name

    @property
    def type(self):
        r"""Gets the type of this CreateOpsLabelRequestBody.

        **参数解释：** 标签的类型（如 free-text 等），用于定义标签的交互或存储逻辑。 **约束限制：** 字符串长度为0到100个字符。 **取值范围：** 长度为0-100。 **默认取值：** 不涉及。 

        :return: The type of this CreateOpsLabelRequestBody.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this CreateOpsLabelRequestBody.

        **参数解释：** 标签的类型（如 free-text 等），用于定义标签的交互或存储逻辑。 **约束限制：** 字符串长度为0到100个字符。 **取值范围：** 长度为0-100。 **默认取值：** 不涉及。 

        :param type: The type of this CreateOpsLabelRequestBody.
        :type type: str
        """
        self._type = type

    @property
    def description(self):
        r"""Gets the description of this CreateOpsLabelRequestBody.

        **参数解释：** 对该标签用途或含义的详细描述。 **约束限制：** 字符串长度为0到400个字符。 **取值范围：** 长度为0-400。 **默认取值：** 不涉及。 

        :return: The description of this CreateOpsLabelRequestBody.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this CreateOpsLabelRequestBody.

        **参数解释：** 对该标签用途或含义的详细描述。 **约束限制：** 字符串长度为0到400个字符。 **取值范围：** 长度为0-400。 **默认取值：** 不涉及。 

        :param description: The description of this CreateOpsLabelRequestBody.
        :type description: str
        """
        self._description = description

    @property
    def enums(self):
        r"""Gets the enums of this CreateOpsLabelRequestBody.

        **参数解释：** 标签的可选值（枚举）列表，定义该标签下包含的具体标记项。 **约束限制：** 数组长度为0到100。 **取值范围：** 不涉及。 **默认取值：** 空列表。 

        :return: The enums of this CreateOpsLabelRequestBody.
        :rtype: list[:class:`huaweicloudsdkagentarts.v1.OpsLabelValueItem`]
        """
        return self._enums

    @enums.setter
    def enums(self, enums):
        r"""Sets the enums of this CreateOpsLabelRequestBody.

        **参数解释：** 标签的可选值（枚举）列表，定义该标签下包含的具体标记项。 **约束限制：** 数组长度为0到100。 **取值范围：** 不涉及。 **默认取值：** 空列表。 

        :param enums: The enums of this CreateOpsLabelRequestBody.
        :type enums: list[:class:`huaweicloudsdkagentarts.v1.OpsLabelValueItem`]
        """
        self._enums = enums

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
        if not isinstance(other, CreateOpsLabelRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

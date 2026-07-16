# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateOpsLabelResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'id': 'str',
        'name': 'str',
        'type': 'str',
        'description': 'str',
        'enums': 'list[OpsLabelValueItem]'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'type': 'type',
        'description': 'description',
        'enums': 'enums'
    }

    def __init__(self, id=None, name=None, type=None, description=None, enums=None):
        r"""UpdateOpsLabelResponse

        The model defined in huaweicloud sdk

        :param id: **参数解释：** 标签的唯一标识符（ID）。 **约束限制：** 字符串长度为1到64个字符。 **取值范围：** 不涉及。 **默认取值：** 不涉及。 
        :type id: str
        :param name: **参数解释：** 更新后的标签名称。 **取值范围：** 不涉及。 
        :type name: str
        :param type: **参数解释：** 标签的类型（如free-text等）。 **取值范围：** 不涉及。 
        :type type: str
        :param description: **参数解释：** 标签的详细描述信息。 **取值范围：** 不涉及。 
        :type description: str
        :param enums: **参数解释：** 更新后的标签可选值（枚举）列表。 **取值范围：** 不涉及。 
        :type enums: list[:class:`huaweicloudsdkagentarts.v1.OpsLabelValueItem`]
        """
        
        super().__init__()

        self._id = None
        self._name = None
        self._type = None
        self._description = None
        self._enums = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if type is not None:
            self.type = type
        if description is not None:
            self.description = description
        if enums is not None:
            self.enums = enums

    @property
    def id(self):
        r"""Gets the id of this UpdateOpsLabelResponse.

        **参数解释：** 标签的唯一标识符（ID）。 **约束限制：** 字符串长度为1到64个字符。 **取值范围：** 不涉及。 **默认取值：** 不涉及。 

        :return: The id of this UpdateOpsLabelResponse.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this UpdateOpsLabelResponse.

        **参数解释：** 标签的唯一标识符（ID）。 **约束限制：** 字符串长度为1到64个字符。 **取值范围：** 不涉及。 **默认取值：** 不涉及。 

        :param id: The id of this UpdateOpsLabelResponse.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        r"""Gets the name of this UpdateOpsLabelResponse.

        **参数解释：** 更新后的标签名称。 **取值范围：** 不涉及。 

        :return: The name of this UpdateOpsLabelResponse.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this UpdateOpsLabelResponse.

        **参数解释：** 更新后的标签名称。 **取值范围：** 不涉及。 

        :param name: The name of this UpdateOpsLabelResponse.
        :type name: str
        """
        self._name = name

    @property
    def type(self):
        r"""Gets the type of this UpdateOpsLabelResponse.

        **参数解释：** 标签的类型（如free-text等）。 **取值范围：** 不涉及。 

        :return: The type of this UpdateOpsLabelResponse.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this UpdateOpsLabelResponse.

        **参数解释：** 标签的类型（如free-text等）。 **取值范围：** 不涉及。 

        :param type: The type of this UpdateOpsLabelResponse.
        :type type: str
        """
        self._type = type

    @property
    def description(self):
        r"""Gets the description of this UpdateOpsLabelResponse.

        **参数解释：** 标签的详细描述信息。 **取值范围：** 不涉及。 

        :return: The description of this UpdateOpsLabelResponse.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this UpdateOpsLabelResponse.

        **参数解释：** 标签的详细描述信息。 **取值范围：** 不涉及。 

        :param description: The description of this UpdateOpsLabelResponse.
        :type description: str
        """
        self._description = description

    @property
    def enums(self):
        r"""Gets the enums of this UpdateOpsLabelResponse.

        **参数解释：** 更新后的标签可选值（枚举）列表。 **取值范围：** 不涉及。 

        :return: The enums of this UpdateOpsLabelResponse.
        :rtype: list[:class:`huaweicloudsdkagentarts.v1.OpsLabelValueItem`]
        """
        return self._enums

    @enums.setter
    def enums(self, enums):
        r"""Sets the enums of this UpdateOpsLabelResponse.

        **参数解释：** 更新后的标签可选值（枚举）列表。 **取值范围：** 不涉及。 

        :param enums: The enums of this UpdateOpsLabelResponse.
        :type enums: list[:class:`huaweicloudsdkagentarts.v1.OpsLabelValueItem`]
        """
        self._enums = enums

    def to_dict(self):
        import warnings
        warnings.warn("UpdateOpsLabelResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, UpdateOpsLabelResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

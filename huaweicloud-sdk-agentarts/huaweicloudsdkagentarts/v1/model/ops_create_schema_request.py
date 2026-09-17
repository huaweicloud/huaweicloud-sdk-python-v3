# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class OpsCreateSchemaRequest:

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
        'content_type': 'str',
        'is_required': 'bool',
        'description': 'str'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'type': 'type',
        'content_type': 'content_type',
        'is_required': 'is_required',
        'description': 'description'
    }

    def __init__(self, id=None, name=None, type=None, content_type=None, is_required=None, description=None):
        r"""OpsCreateSchemaRequest

        The model defined in huaweicloud sdk

        :param id: **参数解释：** 字段的唯一标识符。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。
        :type id: str
        :param name: **参数解释：** 评测集字段的唯一标识符。 **约束限制：** 不涉及。 **取值范围：** 由英文字母、数字和下划线组成，且以字母开头，长度为1~50个字符。 **默认取值：** 不涉及。
        :type name: str
        :param type: **参数解释：** 字段的数据存储与校验类型。 **约束限制：** 必填；必须在预定义的枚举值中选择。 **取值范围：** - String：字符串类型 - Integer：整数类型 - Float：浮点数类型 - Boolean：布尔值类型 **默认取值：** 不涉及。
        :type type: str
        :param content_type: **参数解释：** 字段的内容类型。 **约束限制：** 不涉及。 **取值范围：** - text：纯文本 - image：图片 - audio：音频 - video：视频 - file：文件 **默认取值：** 不涉及。
        :type content_type: str
        :param is_required: **参数解释：** 标识该字段在写入数据时是否必填。 **约束限制：** 不涉及。 **取值范围：** - true：必填 - false：可选 **默认取值：** false。
        :type is_required: bool
        :param description: **参数解释：** 该字段的具体业务含义说明。 **约束限制：** 不涉及。 **取值范围：** 由任意字符组成，长度为1~200个字符。 **默认取值：** 不涉及。
        :type description: str
        """
        
        

        self._id = None
        self._name = None
        self._type = None
        self._content_type = None
        self._is_required = None
        self._description = None
        self.discriminator = None

        if id is not None:
            self.id = id
        self.name = name
        self.type = type
        if content_type is not None:
            self.content_type = content_type
        if is_required is not None:
            self.is_required = is_required
        if description is not None:
            self.description = description

    @property
    def id(self):
        r"""Gets the id of this OpsCreateSchemaRequest.

        **参数解释：** 字段的唯一标识符。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。

        :return: The id of this OpsCreateSchemaRequest.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this OpsCreateSchemaRequest.

        **参数解释：** 字段的唯一标识符。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。

        :param id: The id of this OpsCreateSchemaRequest.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        r"""Gets the name of this OpsCreateSchemaRequest.

        **参数解释：** 评测集字段的唯一标识符。 **约束限制：** 不涉及。 **取值范围：** 由英文字母、数字和下划线组成，且以字母开头，长度为1~50个字符。 **默认取值：** 不涉及。

        :return: The name of this OpsCreateSchemaRequest.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this OpsCreateSchemaRequest.

        **参数解释：** 评测集字段的唯一标识符。 **约束限制：** 不涉及。 **取值范围：** 由英文字母、数字和下划线组成，且以字母开头，长度为1~50个字符。 **默认取值：** 不涉及。

        :param name: The name of this OpsCreateSchemaRequest.
        :type name: str
        """
        self._name = name

    @property
    def type(self):
        r"""Gets the type of this OpsCreateSchemaRequest.

        **参数解释：** 字段的数据存储与校验类型。 **约束限制：** 必填；必须在预定义的枚举值中选择。 **取值范围：** - String：字符串类型 - Integer：整数类型 - Float：浮点数类型 - Boolean：布尔值类型 **默认取值：** 不涉及。

        :return: The type of this OpsCreateSchemaRequest.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this OpsCreateSchemaRequest.

        **参数解释：** 字段的数据存储与校验类型。 **约束限制：** 必填；必须在预定义的枚举值中选择。 **取值范围：** - String：字符串类型 - Integer：整数类型 - Float：浮点数类型 - Boolean：布尔值类型 **默认取值：** 不涉及。

        :param type: The type of this OpsCreateSchemaRequest.
        :type type: str
        """
        self._type = type

    @property
    def content_type(self):
        r"""Gets the content_type of this OpsCreateSchemaRequest.

        **参数解释：** 字段的内容类型。 **约束限制：** 不涉及。 **取值范围：** - text：纯文本 - image：图片 - audio：音频 - video：视频 - file：文件 **默认取值：** 不涉及。

        :return: The content_type of this OpsCreateSchemaRequest.
        :rtype: str
        """
        return self._content_type

    @content_type.setter
    def content_type(self, content_type):
        r"""Sets the content_type of this OpsCreateSchemaRequest.

        **参数解释：** 字段的内容类型。 **约束限制：** 不涉及。 **取值范围：** - text：纯文本 - image：图片 - audio：音频 - video：视频 - file：文件 **默认取值：** 不涉及。

        :param content_type: The content_type of this OpsCreateSchemaRequest.
        :type content_type: str
        """
        self._content_type = content_type

    @property
    def is_required(self):
        r"""Gets the is_required of this OpsCreateSchemaRequest.

        **参数解释：** 标识该字段在写入数据时是否必填。 **约束限制：** 不涉及。 **取值范围：** - true：必填 - false：可选 **默认取值：** false。

        :return: The is_required of this OpsCreateSchemaRequest.
        :rtype: bool
        """
        return self._is_required

    @is_required.setter
    def is_required(self, is_required):
        r"""Sets the is_required of this OpsCreateSchemaRequest.

        **参数解释：** 标识该字段在写入数据时是否必填。 **约束限制：** 不涉及。 **取值范围：** - true：必填 - false：可选 **默认取值：** false。

        :param is_required: The is_required of this OpsCreateSchemaRequest.
        :type is_required: bool
        """
        self._is_required = is_required

    @property
    def description(self):
        r"""Gets the description of this OpsCreateSchemaRequest.

        **参数解释：** 该字段的具体业务含义说明。 **约束限制：** 不涉及。 **取值范围：** 由任意字符组成，长度为1~200个字符。 **默认取值：** 不涉及。

        :return: The description of this OpsCreateSchemaRequest.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this OpsCreateSchemaRequest.

        **参数解释：** 该字段的具体业务含义说明。 **约束限制：** 不涉及。 **取值范围：** 由任意字符组成，长度为1~200个字符。 **默认取值：** 不涉及。

        :param description: The description of this OpsCreateSchemaRequest.
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
        if not isinstance(other, OpsCreateSchemaRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

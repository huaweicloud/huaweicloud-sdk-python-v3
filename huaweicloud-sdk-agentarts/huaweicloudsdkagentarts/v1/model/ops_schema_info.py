# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class OpsSchemaInfo:

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
        'is_required': 'bool'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'type': 'type',
        'description': 'description',
        'is_required': 'is_required'
    }

    def __init__(self, id=None, name=None, type=None, description=None, is_required=None):
        r"""OpsSchemaInfo

        The model defined in huaweicloud sdk

        :param id: **参数解释：** 字段的唯一标识符。 **取值范围：** 符合通用唯一识别码(UUID)标准的字符串。
        :type id: str
        :param name: **参数解释：** 字段的键名（Key），用于在数据条目中作为属性名。 **取值范围：** 建议符合变量命名规范的字符串。
        :type name: str
        :param type: **参数解释：** 字段的数据类型，定义数据的存储和解析方式。 **取值范围：** 支持String, Integer, Float, Boolean, Object, Array&lt;String&gt;,Array&lt;Integer&gt;,Array&lt;Float&gt;,Array&lt;Boolean&gt;,Array&lt;Object&gt; 以及Trajectory。
        :type type: str
        :param description: **参数解释：** 对该字段业务含义或用途的详细文字说明。 **取值范围：** 描述字段的业务含义或用途的文本，最大长度10000字符。
        :type description: str
        :param is_required: **参数解释：** 标识该字段在数据条目中是否为必须存在的必填项。 **取值范围：** - true：必填 - false：选填
        :type is_required: bool
        """
        
        

        self._id = None
        self._name = None
        self._type = None
        self._description = None
        self._is_required = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if type is not None:
            self.type = type
        if description is not None:
            self.description = description
        if is_required is not None:
            self.is_required = is_required

    @property
    def id(self):
        r"""Gets the id of this OpsSchemaInfo.

        **参数解释：** 字段的唯一标识符。 **取值范围：** 符合通用唯一识别码(UUID)标准的字符串。

        :return: The id of this OpsSchemaInfo.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this OpsSchemaInfo.

        **参数解释：** 字段的唯一标识符。 **取值范围：** 符合通用唯一识别码(UUID)标准的字符串。

        :param id: The id of this OpsSchemaInfo.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        r"""Gets the name of this OpsSchemaInfo.

        **参数解释：** 字段的键名（Key），用于在数据条目中作为属性名。 **取值范围：** 建议符合变量命名规范的字符串。

        :return: The name of this OpsSchemaInfo.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this OpsSchemaInfo.

        **参数解释：** 字段的键名（Key），用于在数据条目中作为属性名。 **取值范围：** 建议符合变量命名规范的字符串。

        :param name: The name of this OpsSchemaInfo.
        :type name: str
        """
        self._name = name

    @property
    def type(self):
        r"""Gets the type of this OpsSchemaInfo.

        **参数解释：** 字段的数据类型，定义数据的存储和解析方式。 **取值范围：** 支持String, Integer, Float, Boolean, Object, Array<String>,Array<Integer>,Array<Float>,Array<Boolean>,Array<Object> 以及Trajectory。

        :return: The type of this OpsSchemaInfo.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this OpsSchemaInfo.

        **参数解释：** 字段的数据类型，定义数据的存储和解析方式。 **取值范围：** 支持String, Integer, Float, Boolean, Object, Array<String>,Array<Integer>,Array<Float>,Array<Boolean>,Array<Object> 以及Trajectory。

        :param type: The type of this OpsSchemaInfo.
        :type type: str
        """
        self._type = type

    @property
    def description(self):
        r"""Gets the description of this OpsSchemaInfo.

        **参数解释：** 对该字段业务含义或用途的详细文字说明。 **取值范围：** 描述字段的业务含义或用途的文本，最大长度10000字符。

        :return: The description of this OpsSchemaInfo.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this OpsSchemaInfo.

        **参数解释：** 对该字段业务含义或用途的详细文字说明。 **取值范围：** 描述字段的业务含义或用途的文本，最大长度10000字符。

        :param description: The description of this OpsSchemaInfo.
        :type description: str
        """
        self._description = description

    @property
    def is_required(self):
        r"""Gets the is_required of this OpsSchemaInfo.

        **参数解释：** 标识该字段在数据条目中是否为必须存在的必填项。 **取值范围：** - true：必填 - false：选填

        :return: The is_required of this OpsSchemaInfo.
        :rtype: bool
        """
        return self._is_required

    @is_required.setter
    def is_required(self, is_required):
        r"""Sets the is_required of this OpsSchemaInfo.

        **参数解释：** 标识该字段在数据条目中是否为必须存在的必填项。 **取值范围：** - true：必填 - false：选填

        :param is_required: The is_required of this OpsSchemaInfo.
        :type is_required: bool
        """
        self._is_required = is_required

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
        if not isinstance(other, OpsSchemaInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

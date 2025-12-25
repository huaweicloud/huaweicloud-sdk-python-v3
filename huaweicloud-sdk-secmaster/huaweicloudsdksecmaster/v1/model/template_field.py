# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class TemplateField:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'default_value': 'str',
        'description': 'str',
        'example': 'str',
        'name': 'str',
        'required': 'bool',
        'restrictions': 'list[Restriction]',
        'template_field_id': 'str',
        'title': 'str',
        'type': 'str'
    }

    attribute_map = {
        'default_value': 'default_value',
        'description': 'description',
        'example': 'example',
        'name': 'name',
        'required': 'required',
        'restrictions': 'restrictions',
        'template_field_id': 'template_field_id',
        'title': 'title',
        'type': 'type'
    }

    def __init__(self, default_value=None, description=None, example=None, name=None, required=None, restrictions=None, template_field_id=None, title=None, type=None):
        r"""TemplateField

        The model defined in huaweicloud sdk

        :param default_value: 默认值
        :type default_value: str
        :param description: 描述信息
        :type description: str
        :param example: 示例
        :type example: str
        :param name: 规则名称
        :type name: str
        :param required: 是否必填
        :type required: bool
        :param restrictions: 相关描述信息
        :type restrictions: list[:class:`huaweicloudsdksecmaster.v1.Restriction`]
        :param template_field_id: UUID
        :type template_field_id: str
        :param title: 相关标题
        :type title: str
        :param type: 规则类型
        :type type: str
        """
        
        

        self._default_value = None
        self._description = None
        self._example = None
        self._name = None
        self._required = None
        self._restrictions = None
        self._template_field_id = None
        self._title = None
        self._type = None
        self.discriminator = None

        if default_value is not None:
            self.default_value = default_value
        if description is not None:
            self.description = description
        if example is not None:
            self.example = example
        if name is not None:
            self.name = name
        if required is not None:
            self.required = required
        if restrictions is not None:
            self.restrictions = restrictions
        if template_field_id is not None:
            self.template_field_id = template_field_id
        if title is not None:
            self.title = title
        if type is not None:
            self.type = type

    @property
    def default_value(self):
        r"""Gets the default_value of this TemplateField.

        默认值

        :return: The default_value of this TemplateField.
        :rtype: str
        """
        return self._default_value

    @default_value.setter
    def default_value(self, default_value):
        r"""Sets the default_value of this TemplateField.

        默认值

        :param default_value: The default_value of this TemplateField.
        :type default_value: str
        """
        self._default_value = default_value

    @property
    def description(self):
        r"""Gets the description of this TemplateField.

        描述信息

        :return: The description of this TemplateField.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this TemplateField.

        描述信息

        :param description: The description of this TemplateField.
        :type description: str
        """
        self._description = description

    @property
    def example(self):
        r"""Gets the example of this TemplateField.

        示例

        :return: The example of this TemplateField.
        :rtype: str
        """
        return self._example

    @example.setter
    def example(self, example):
        r"""Sets the example of this TemplateField.

        示例

        :param example: The example of this TemplateField.
        :type example: str
        """
        self._example = example

    @property
    def name(self):
        r"""Gets the name of this TemplateField.

        规则名称

        :return: The name of this TemplateField.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this TemplateField.

        规则名称

        :param name: The name of this TemplateField.
        :type name: str
        """
        self._name = name

    @property
    def required(self):
        r"""Gets the required of this TemplateField.

        是否必填

        :return: The required of this TemplateField.
        :rtype: bool
        """
        return self._required

    @required.setter
    def required(self, required):
        r"""Sets the required of this TemplateField.

        是否必填

        :param required: The required of this TemplateField.
        :type required: bool
        """
        self._required = required

    @property
    def restrictions(self):
        r"""Gets the restrictions of this TemplateField.

        相关描述信息

        :return: The restrictions of this TemplateField.
        :rtype: list[:class:`huaweicloudsdksecmaster.v1.Restriction`]
        """
        return self._restrictions

    @restrictions.setter
    def restrictions(self, restrictions):
        r"""Sets the restrictions of this TemplateField.

        相关描述信息

        :param restrictions: The restrictions of this TemplateField.
        :type restrictions: list[:class:`huaweicloudsdksecmaster.v1.Restriction`]
        """
        self._restrictions = restrictions

    @property
    def template_field_id(self):
        r"""Gets the template_field_id of this TemplateField.

        UUID

        :return: The template_field_id of this TemplateField.
        :rtype: str
        """
        return self._template_field_id

    @template_field_id.setter
    def template_field_id(self, template_field_id):
        r"""Sets the template_field_id of this TemplateField.

        UUID

        :param template_field_id: The template_field_id of this TemplateField.
        :type template_field_id: str
        """
        self._template_field_id = template_field_id

    @property
    def title(self):
        r"""Gets the title of this TemplateField.

        相关标题

        :return: The title of this TemplateField.
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        r"""Sets the title of this TemplateField.

        相关标题

        :param title: The title of this TemplateField.
        :type title: str
        """
        self._title = title

    @property
    def type(self):
        r"""Gets the type of this TemplateField.

        规则类型

        :return: The type of this TemplateField.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this TemplateField.

        规则类型

        :param type: The type of this TemplateField.
        :type type: str
        """
        self._type = type

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
        if not isinstance(other, TemplateField):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

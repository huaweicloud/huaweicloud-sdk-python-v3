# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class FieldVO:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'display_name': 'str',
        'created_by': 'str',
        'field_type': 'str',
        'show_on_card': 'bool',
        'optional': 'bool',
        'all_options': 'list[OptionEntity]',
        'default_value': 'str'
    }

    attribute_map = {
        'display_name': 'display_name',
        'created_by': 'created_by',
        'field_type': 'field_type',
        'show_on_card': 'show_on_card',
        'optional': 'optional',
        'all_options': 'all_options',
        'default_value': 'default_value'
    }

    def __init__(self, display_name=None, created_by=None, field_type=None, show_on_card=None, optional=None, all_options=None, default_value=None):
        r"""FieldVO

        The model defined in huaweicloud sdk

        :param display_name: 字段名称
        :type display_name: str
        :param created_by: 添加人
        :type created_by: str
        :param field_type: 字段类型
        :type field_type: str
        :param show_on_card: 是否显示在新建页
        :type show_on_card: bool
        :param optional: 是否必填
        :type optional: bool
        :param all_options: 字段选项
        :type all_options: list[:class:`huaweicloudsdkprojectman.v4.OptionEntity`]
        :param default_value: 默认值
        :type default_value: str
        """
        
        

        self._display_name = None
        self._created_by = None
        self._field_type = None
        self._show_on_card = None
        self._optional = None
        self._all_options = None
        self._default_value = None
        self.discriminator = None

        if display_name is not None:
            self.display_name = display_name
        if created_by is not None:
            self.created_by = created_by
        if field_type is not None:
            self.field_type = field_type
        if show_on_card is not None:
            self.show_on_card = show_on_card
        if optional is not None:
            self.optional = optional
        if all_options is not None:
            self.all_options = all_options
        if default_value is not None:
            self.default_value = default_value

    @property
    def display_name(self):
        r"""Gets the display_name of this FieldVO.

        字段名称

        :return: The display_name of this FieldVO.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        r"""Sets the display_name of this FieldVO.

        字段名称

        :param display_name: The display_name of this FieldVO.
        :type display_name: str
        """
        self._display_name = display_name

    @property
    def created_by(self):
        r"""Gets the created_by of this FieldVO.

        添加人

        :return: The created_by of this FieldVO.
        :rtype: str
        """
        return self._created_by

    @created_by.setter
    def created_by(self, created_by):
        r"""Sets the created_by of this FieldVO.

        添加人

        :param created_by: The created_by of this FieldVO.
        :type created_by: str
        """
        self._created_by = created_by

    @property
    def field_type(self):
        r"""Gets the field_type of this FieldVO.

        字段类型

        :return: The field_type of this FieldVO.
        :rtype: str
        """
        return self._field_type

    @field_type.setter
    def field_type(self, field_type):
        r"""Sets the field_type of this FieldVO.

        字段类型

        :param field_type: The field_type of this FieldVO.
        :type field_type: str
        """
        self._field_type = field_type

    @property
    def show_on_card(self):
        r"""Gets the show_on_card of this FieldVO.

        是否显示在新建页

        :return: The show_on_card of this FieldVO.
        :rtype: bool
        """
        return self._show_on_card

    @show_on_card.setter
    def show_on_card(self, show_on_card):
        r"""Sets the show_on_card of this FieldVO.

        是否显示在新建页

        :param show_on_card: The show_on_card of this FieldVO.
        :type show_on_card: bool
        """
        self._show_on_card = show_on_card

    @property
    def optional(self):
        r"""Gets the optional of this FieldVO.

        是否必填

        :return: The optional of this FieldVO.
        :rtype: bool
        """
        return self._optional

    @optional.setter
    def optional(self, optional):
        r"""Sets the optional of this FieldVO.

        是否必填

        :param optional: The optional of this FieldVO.
        :type optional: bool
        """
        self._optional = optional

    @property
    def all_options(self):
        r"""Gets the all_options of this FieldVO.

        字段选项

        :return: The all_options of this FieldVO.
        :rtype: list[:class:`huaweicloudsdkprojectman.v4.OptionEntity`]
        """
        return self._all_options

    @all_options.setter
    def all_options(self, all_options):
        r"""Sets the all_options of this FieldVO.

        字段选项

        :param all_options: The all_options of this FieldVO.
        :type all_options: list[:class:`huaweicloudsdkprojectman.v4.OptionEntity`]
        """
        self._all_options = all_options

    @property
    def default_value(self):
        r"""Gets the default_value of this FieldVO.

        默认值

        :return: The default_value of this FieldVO.
        :rtype: str
        """
        return self._default_value

    @default_value.setter
    def default_value(self, default_value):
        r"""Sets the default_value of this FieldVO.

        默认值

        :param default_value: The default_value of this FieldVO.
        :type default_value: str
        """
        self._default_value = default_value

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
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
        if six.PY2:
            import sys
            reload(sys)
            sys.setdefaultencoding("utf-8")
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, FieldVO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateConnectionDto:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'description': 'str',
        'fields': 'list[ConnectionModuleFieldUpdateVo]',
        'module_id': 'str',
        'name': 'str',
        'template_id': 'str',
        'title': 'str'
    }

    attribute_map = {
        'description': 'description',
        'fields': 'fields',
        'module_id': 'module_id',
        'name': 'name',
        'template_id': 'template_id',
        'title': 'title'
    }

    def __init__(self, description=None, fields=None, module_id=None, name=None, template_id=None, title=None):
        r"""UpdateConnectionDto

        The model defined in huaweicloud sdk

        :param description: 描述信息
        :type description: str
        :param fields: 相关描述信息
        :type fields: list[:class:`huaweicloudsdksecmaster.v1.ConnectionModuleFieldUpdateVo`]
        :param module_id: UUID
        :type module_id: str
        :param name: 所属租户名称
        :type name: str
        :param template_id: UUID
        :type template_id: str
        :param title: 相关标题
        :type title: str
        """
        
        

        self._description = None
        self._fields = None
        self._module_id = None
        self._name = None
        self._template_id = None
        self._title = None
        self.discriminator = None

        if description is not None:
            self.description = description
        if fields is not None:
            self.fields = fields
        self.module_id = module_id
        self.name = name
        self.template_id = template_id
        self.title = title

    @property
    def description(self):
        r"""Gets the description of this UpdateConnectionDto.

        描述信息

        :return: The description of this UpdateConnectionDto.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this UpdateConnectionDto.

        描述信息

        :param description: The description of this UpdateConnectionDto.
        :type description: str
        """
        self._description = description

    @property
    def fields(self):
        r"""Gets the fields of this UpdateConnectionDto.

        相关描述信息

        :return: The fields of this UpdateConnectionDto.
        :rtype: list[:class:`huaweicloudsdksecmaster.v1.ConnectionModuleFieldUpdateVo`]
        """
        return self._fields

    @fields.setter
    def fields(self, fields):
        r"""Sets the fields of this UpdateConnectionDto.

        相关描述信息

        :param fields: The fields of this UpdateConnectionDto.
        :type fields: list[:class:`huaweicloudsdksecmaster.v1.ConnectionModuleFieldUpdateVo`]
        """
        self._fields = fields

    @property
    def module_id(self):
        r"""Gets the module_id of this UpdateConnectionDto.

        UUID

        :return: The module_id of this UpdateConnectionDto.
        :rtype: str
        """
        return self._module_id

    @module_id.setter
    def module_id(self, module_id):
        r"""Sets the module_id of this UpdateConnectionDto.

        UUID

        :param module_id: The module_id of this UpdateConnectionDto.
        :type module_id: str
        """
        self._module_id = module_id

    @property
    def name(self):
        r"""Gets the name of this UpdateConnectionDto.

        所属租户名称

        :return: The name of this UpdateConnectionDto.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this UpdateConnectionDto.

        所属租户名称

        :param name: The name of this UpdateConnectionDto.
        :type name: str
        """
        self._name = name

    @property
    def template_id(self):
        r"""Gets the template_id of this UpdateConnectionDto.

        UUID

        :return: The template_id of this UpdateConnectionDto.
        :rtype: str
        """
        return self._template_id

    @template_id.setter
    def template_id(self, template_id):
        r"""Sets the template_id of this UpdateConnectionDto.

        UUID

        :param template_id: The template_id of this UpdateConnectionDto.
        :type template_id: str
        """
        self._template_id = template_id

    @property
    def title(self):
        r"""Gets the title of this UpdateConnectionDto.

        相关标题

        :return: The title of this UpdateConnectionDto.
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        r"""Sets the title of this UpdateConnectionDto.

        相关标题

        :param title: The title of this UpdateConnectionDto.
        :type title: str
        """
        self._title = title

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
        if not isinstance(other, UpdateConnectionDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

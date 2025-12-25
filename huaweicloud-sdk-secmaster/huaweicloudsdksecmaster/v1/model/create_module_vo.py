# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateModuleVo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'children': 'list[CreateModuleVo]',
        'connection_module_id': 'str',
        'fields': 'list[ModuleFieldVo]',
        'name': 'str',
        'template_id': 'str'
    }

    attribute_map = {
        'children': 'children',
        'connection_module_id': 'connection_module_id',
        'fields': 'fields',
        'name': 'name',
        'template_id': 'template_id'
    }

    def __init__(self, children=None, connection_module_id=None, fields=None, name=None, template_id=None):
        r"""CreateModuleVo

        The model defined in huaweicloud sdk

        :param children: 相关描述信息
        :type children: list[:class:`huaweicloudsdksecmaster.v1.CreateModuleVo`]
        :param connection_module_id: UUID
        :type connection_module_id: str
        :param fields: 相关描述信息
        :type fields: list[:class:`huaweicloudsdksecmaster.v1.ModuleFieldVo`]
        :param name: 名称
        :type name: str
        :param template_id: UUID
        :type template_id: str
        """
        
        

        self._children = None
        self._connection_module_id = None
        self._fields = None
        self._name = None
        self._template_id = None
        self.discriminator = None

        if children is not None:
            self.children = children
        if connection_module_id is not None:
            self.connection_module_id = connection_module_id
        if fields is not None:
            self.fields = fields
        if name is not None:
            self.name = name
        if template_id is not None:
            self.template_id = template_id

    @property
    def children(self):
        r"""Gets the children of this CreateModuleVo.

        相关描述信息

        :return: The children of this CreateModuleVo.
        :rtype: list[:class:`huaweicloudsdksecmaster.v1.CreateModuleVo`]
        """
        return self._children

    @children.setter
    def children(self, children):
        r"""Sets the children of this CreateModuleVo.

        相关描述信息

        :param children: The children of this CreateModuleVo.
        :type children: list[:class:`huaweicloudsdksecmaster.v1.CreateModuleVo`]
        """
        self._children = children

    @property
    def connection_module_id(self):
        r"""Gets the connection_module_id of this CreateModuleVo.

        UUID

        :return: The connection_module_id of this CreateModuleVo.
        :rtype: str
        """
        return self._connection_module_id

    @connection_module_id.setter
    def connection_module_id(self, connection_module_id):
        r"""Sets the connection_module_id of this CreateModuleVo.

        UUID

        :param connection_module_id: The connection_module_id of this CreateModuleVo.
        :type connection_module_id: str
        """
        self._connection_module_id = connection_module_id

    @property
    def fields(self):
        r"""Gets the fields of this CreateModuleVo.

        相关描述信息

        :return: The fields of this CreateModuleVo.
        :rtype: list[:class:`huaweicloudsdksecmaster.v1.ModuleFieldVo`]
        """
        return self._fields

    @fields.setter
    def fields(self, fields):
        r"""Sets the fields of this CreateModuleVo.

        相关描述信息

        :param fields: The fields of this CreateModuleVo.
        :type fields: list[:class:`huaweicloudsdksecmaster.v1.ModuleFieldVo`]
        """
        self._fields = fields

    @property
    def name(self):
        r"""Gets the name of this CreateModuleVo.

        名称

        :return: The name of this CreateModuleVo.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this CreateModuleVo.

        名称

        :param name: The name of this CreateModuleVo.
        :type name: str
        """
        self._name = name

    @property
    def template_id(self):
        r"""Gets the template_id of this CreateModuleVo.

        UUID

        :return: The template_id of this CreateModuleVo.
        :rtype: str
        """
        return self._template_id

    @template_id.setter
    def template_id(self, template_id):
        r"""Sets the template_id of this CreateModuleVo.

        UUID

        :param template_id: The template_id of this CreateModuleVo.
        :type template_id: str
        """
        self._template_id = template_id

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
        if not isinstance(other, CreateModuleVo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

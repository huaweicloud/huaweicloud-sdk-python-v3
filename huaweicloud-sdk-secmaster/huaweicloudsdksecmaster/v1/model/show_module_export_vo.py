# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowModuleExportVo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'children': 'list[ShowModuleExportVo]',
        'fields': 'list[ShowModuleFieldExportVo]',
        'module_id': 'str',
        'name': 'str',
        'template_id': 'str'
    }

    attribute_map = {
        'children': 'children',
        'fields': 'fields',
        'module_id': 'module_id',
        'name': 'name',
        'template_id': 'template_id'
    }

    def __init__(self, children=None, fields=None, module_id=None, name=None, template_id=None):
        r"""ShowModuleExportVo

        The model defined in huaweicloud sdk

        :param children: 相关描述信息
        :type children: list[:class:`huaweicloudsdksecmaster.v1.ShowModuleExportVo`]
        :param fields: 相关描述信息
        :type fields: list[:class:`huaweicloudsdksecmaster.v1.ShowModuleFieldExportVo`]
        :param module_id: UUID
        :type module_id: str
        :param name: 所属租户名称
        :type name: str
        :param template_id: UUID
        :type template_id: str
        """
        
        

        self._children = None
        self._fields = None
        self._module_id = None
        self._name = None
        self._template_id = None
        self.discriminator = None

        if children is not None:
            self.children = children
        if fields is not None:
            self.fields = fields
        if module_id is not None:
            self.module_id = module_id
        if name is not None:
            self.name = name
        if template_id is not None:
            self.template_id = template_id

    @property
    def children(self):
        r"""Gets the children of this ShowModuleExportVo.

        相关描述信息

        :return: The children of this ShowModuleExportVo.
        :rtype: list[:class:`huaweicloudsdksecmaster.v1.ShowModuleExportVo`]
        """
        return self._children

    @children.setter
    def children(self, children):
        r"""Sets the children of this ShowModuleExportVo.

        相关描述信息

        :param children: The children of this ShowModuleExportVo.
        :type children: list[:class:`huaweicloudsdksecmaster.v1.ShowModuleExportVo`]
        """
        self._children = children

    @property
    def fields(self):
        r"""Gets the fields of this ShowModuleExportVo.

        相关描述信息

        :return: The fields of this ShowModuleExportVo.
        :rtype: list[:class:`huaweicloudsdksecmaster.v1.ShowModuleFieldExportVo`]
        """
        return self._fields

    @fields.setter
    def fields(self, fields):
        r"""Sets the fields of this ShowModuleExportVo.

        相关描述信息

        :param fields: The fields of this ShowModuleExportVo.
        :type fields: list[:class:`huaweicloudsdksecmaster.v1.ShowModuleFieldExportVo`]
        """
        self._fields = fields

    @property
    def module_id(self):
        r"""Gets the module_id of this ShowModuleExportVo.

        UUID

        :return: The module_id of this ShowModuleExportVo.
        :rtype: str
        """
        return self._module_id

    @module_id.setter
    def module_id(self, module_id):
        r"""Sets the module_id of this ShowModuleExportVo.

        UUID

        :param module_id: The module_id of this ShowModuleExportVo.
        :type module_id: str
        """
        self._module_id = module_id

    @property
    def name(self):
        r"""Gets the name of this ShowModuleExportVo.

        所属租户名称

        :return: The name of this ShowModuleExportVo.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this ShowModuleExportVo.

        所属租户名称

        :param name: The name of this ShowModuleExportVo.
        :type name: str
        """
        self._name = name

    @property
    def template_id(self):
        r"""Gets the template_id of this ShowModuleExportVo.

        UUID

        :return: The template_id of this ShowModuleExportVo.
        :rtype: str
        """
        return self._template_id

    @template_id.setter
    def template_id(self, template_id):
        r"""Sets the template_id of this ShowModuleExportVo.

        UUID

        :param template_id: The template_id of this ShowModuleExportVo.
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
        if not isinstance(other, ShowModuleExportVo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

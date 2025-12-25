# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowTemplateFields:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'fields': 'list[TemplateField]',
        'template_id': 'str'
    }

    attribute_map = {
        'fields': 'fields',
        'template_id': 'template_id'
    }

    def __init__(self, fields=None, template_id=None):
        r"""ShowTemplateFields

        The model defined in huaweicloud sdk

        :param fields: 相关描述信息
        :type fields: list[:class:`huaweicloudsdksecmaster.v1.TemplateField`]
        :param template_id: UUID
        :type template_id: str
        """
        
        

        self._fields = None
        self._template_id = None
        self.discriminator = None

        if fields is not None:
            self.fields = fields
        if template_id is not None:
            self.template_id = template_id

    @property
    def fields(self):
        r"""Gets the fields of this ShowTemplateFields.

        相关描述信息

        :return: The fields of this ShowTemplateFields.
        :rtype: list[:class:`huaweicloudsdksecmaster.v1.TemplateField`]
        """
        return self._fields

    @fields.setter
    def fields(self, fields):
        r"""Sets the fields of this ShowTemplateFields.

        相关描述信息

        :param fields: The fields of this ShowTemplateFields.
        :type fields: list[:class:`huaweicloudsdksecmaster.v1.TemplateField`]
        """
        self._fields = fields

    @property
    def template_id(self):
        r"""Gets the template_id of this ShowTemplateFields.

        UUID

        :return: The template_id of this ShowTemplateFields.
        :rtype: str
        """
        return self._template_id

    @template_id.setter
    def template_id(self, template_id):
        r"""Sets the template_id of this ShowTemplateFields.

        UUID

        :param template_id: The template_id of this ShowTemplateFields.
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
        if not isinstance(other, ShowTemplateFields):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

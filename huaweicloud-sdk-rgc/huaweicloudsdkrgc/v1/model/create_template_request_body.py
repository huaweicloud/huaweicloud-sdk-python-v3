# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateTemplateRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []
    sensitive_list.append('template_body')

    openapi_types = {
        'template_name': 'str',
        'template_type': 'str',
        'template_description': 'str',
        'template_body': 'str'
    }

    attribute_map = {
        'template_name': 'template_name',
        'template_type': 'template_type',
        'template_description': 'template_description',
        'template_body': 'template_body'
    }

    def __init__(self, template_name=None, template_type=None, template_description=None, template_body=None):
        r"""CreateTemplateRequestBody

        The model defined in huaweicloud sdk

        :param template_name: 模板名称。
        :type template_name: str
        :param template_type: 模板类型，包括预置和自定义。
        :type template_type: str
        :param template_description: 模板描述。
        :type template_description: str
        :param template_body: 模板内容。
        :type template_body: str
        """
        
        

        self._template_name = None
        self._template_type = None
        self._template_description = None
        self._template_body = None
        self.discriminator = None

        self.template_name = template_name
        self.template_type = template_type
        if template_description is not None:
            self.template_description = template_description
        if template_body is not None:
            self.template_body = template_body

    @property
    def template_name(self):
        r"""Gets the template_name of this CreateTemplateRequestBody.

        模板名称。

        :return: The template_name of this CreateTemplateRequestBody.
        :rtype: str
        """
        return self._template_name

    @template_name.setter
    def template_name(self, template_name):
        r"""Sets the template_name of this CreateTemplateRequestBody.

        模板名称。

        :param template_name: The template_name of this CreateTemplateRequestBody.
        :type template_name: str
        """
        self._template_name = template_name

    @property
    def template_type(self):
        r"""Gets the template_type of this CreateTemplateRequestBody.

        模板类型，包括预置和自定义。

        :return: The template_type of this CreateTemplateRequestBody.
        :rtype: str
        """
        return self._template_type

    @template_type.setter
    def template_type(self, template_type):
        r"""Sets the template_type of this CreateTemplateRequestBody.

        模板类型，包括预置和自定义。

        :param template_type: The template_type of this CreateTemplateRequestBody.
        :type template_type: str
        """
        self._template_type = template_type

    @property
    def template_description(self):
        r"""Gets the template_description of this CreateTemplateRequestBody.

        模板描述。

        :return: The template_description of this CreateTemplateRequestBody.
        :rtype: str
        """
        return self._template_description

    @template_description.setter
    def template_description(self, template_description):
        r"""Sets the template_description of this CreateTemplateRequestBody.

        模板描述。

        :param template_description: The template_description of this CreateTemplateRequestBody.
        :type template_description: str
        """
        self._template_description = template_description

    @property
    def template_body(self):
        r"""Gets the template_body of this CreateTemplateRequestBody.

        模板内容。

        :return: The template_body of this CreateTemplateRequestBody.
        :rtype: str
        """
        return self._template_body

    @template_body.setter
    def template_body(self, template_body):
        r"""Sets the template_body of this CreateTemplateRequestBody.

        模板内容。

        :param template_body: The template_body of this CreateTemplateRequestBody.
        :type template_body: str
        """
        self._template_body = template_body

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
        if not isinstance(other, CreateTemplateRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PredefinedTemplate:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'template_name': 'str',
        'template_description': 'str',
        'template_file_name': 'str'
    }

    attribute_map = {
        'template_name': 'template_name',
        'template_description': 'template_description',
        'template_file_name': 'template_file_name'
    }

    def __init__(self, template_name=None, template_description=None, template_file_name=None):
        """PredefinedTemplate

        The model defined in huaweicloud sdk

        :param template_name: 模板名称。
        :type template_name: str
        :param template_description: 模板描述。
        :type template_description: str
        :param template_file_name: 模板文件名称。
        :type template_file_name: str
        """
        
        

        self._template_name = None
        self._template_description = None
        self._template_file_name = None
        self.discriminator = None

        if template_name is not None:
            self.template_name = template_name
        if template_description is not None:
            self.template_description = template_description
        if template_file_name is not None:
            self.template_file_name = template_file_name

    @property
    def template_name(self):
        """Gets the template_name of this PredefinedTemplate.

        模板名称。

        :return: The template_name of this PredefinedTemplate.
        :rtype: str
        """
        return self._template_name

    @template_name.setter
    def template_name(self, template_name):
        """Sets the template_name of this PredefinedTemplate.

        模板名称。

        :param template_name: The template_name of this PredefinedTemplate.
        :type template_name: str
        """
        self._template_name = template_name

    @property
    def template_description(self):
        """Gets the template_description of this PredefinedTemplate.

        模板描述。

        :return: The template_description of this PredefinedTemplate.
        :rtype: str
        """
        return self._template_description

    @template_description.setter
    def template_description(self, template_description):
        """Sets the template_description of this PredefinedTemplate.

        模板描述。

        :param template_description: The template_description of this PredefinedTemplate.
        :type template_description: str
        """
        self._template_description = template_description

    @property
    def template_file_name(self):
        """Gets the template_file_name of this PredefinedTemplate.

        模板文件名称。

        :return: The template_file_name of this PredefinedTemplate.
        :rtype: str
        """
        return self._template_file_name

    @template_file_name.setter
    def template_file_name(self, template_file_name):
        """Sets the template_file_name of this PredefinedTemplate.

        模板文件名称。

        :param template_file_name: The template_file_name of this PredefinedTemplate.
        :type template_file_name: str
        """
        self._template_file_name = template_file_name

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
        if not isinstance(other, PredefinedTemplate):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

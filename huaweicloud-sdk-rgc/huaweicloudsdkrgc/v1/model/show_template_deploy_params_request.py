# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowTemplateDeployParamsRequest:

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
        'version': 'str'
    }

    attribute_map = {
        'template_name': 'template_name',
        'version': 'version'
    }

    def __init__(self, template_name=None, version=None):
        r"""ShowTemplateDeployParamsRequest

        The model defined in huaweicloud sdk

        :param template_name: 模板名称。
        :type template_name: str
        :param version: 模板版本。
        :type version: str
        """
        
        

        self._template_name = None
        self._version = None
        self.discriminator = None

        self.template_name = template_name
        self.version = version

    @property
    def template_name(self):
        r"""Gets the template_name of this ShowTemplateDeployParamsRequest.

        模板名称。

        :return: The template_name of this ShowTemplateDeployParamsRequest.
        :rtype: str
        """
        return self._template_name

    @template_name.setter
    def template_name(self, template_name):
        r"""Sets the template_name of this ShowTemplateDeployParamsRequest.

        模板名称。

        :param template_name: The template_name of this ShowTemplateDeployParamsRequest.
        :type template_name: str
        """
        self._template_name = template_name

    @property
    def version(self):
        r"""Gets the version of this ShowTemplateDeployParamsRequest.

        模板版本。

        :return: The version of this ShowTemplateDeployParamsRequest.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        r"""Sets the version of this ShowTemplateDeployParamsRequest.

        模板版本。

        :param version: The version of this ShowTemplateDeployParamsRequest.
        :type version: str
        """
        self._version = version

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
        if not isinstance(other, ShowTemplateDeployParamsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class TemplateSetting:

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
        'template_contents': 'list[str]'
    }

    attribute_map = {
        'template_name': 'template_name',
        'template_contents': 'template_contents'
    }

    def __init__(self, template_name=None, template_contents=None):
        r"""TemplateSetting

        The model defined in huaweicloud sdk

        :param template_name: 模板名称
        :type template_name: str
        :param template_contents: 模板内容列表
        :type template_contents: list[str]
        """
        
        

        self._template_name = None
        self._template_contents = None
        self.discriminator = None

        self.template_name = template_name
        self.template_contents = template_contents

    @property
    def template_name(self):
        r"""Gets the template_name of this TemplateSetting.

        模板名称

        :return: The template_name of this TemplateSetting.
        :rtype: str
        """
        return self._template_name

    @template_name.setter
    def template_name(self, template_name):
        r"""Sets the template_name of this TemplateSetting.

        模板名称

        :param template_name: The template_name of this TemplateSetting.
        :type template_name: str
        """
        self._template_name = template_name

    @property
    def template_contents(self):
        r"""Gets the template_contents of this TemplateSetting.

        模板内容列表

        :return: The template_contents of this TemplateSetting.
        :rtype: list[str]
        """
        return self._template_contents

    @template_contents.setter
    def template_contents(self, template_contents):
        r"""Sets the template_contents of this TemplateSetting.

        模板内容列表

        :param template_contents: The template_contents of this TemplateSetting.
        :type template_contents: list[str]
        """
        self._template_contents = template_contents

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
        if not isinstance(other, TemplateSetting):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

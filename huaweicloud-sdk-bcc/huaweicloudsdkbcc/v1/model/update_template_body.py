# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateTemplateBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'template_contents': 'list[TemplateItemEnum]'
    }

    attribute_map = {
        'template_contents': 'template_contents'
    }

    def __init__(self, template_contents=None):
        r"""UpdateTemplateBody

        The model defined in huaweicloud sdk

        :param template_contents: 模板内容列表
        :type template_contents: list[:class:`huaweicloudsdkbcc.v1.TemplateItemEnum`]
        """
        
        

        self._template_contents = None
        self.discriminator = None

        self.template_contents = template_contents

    @property
    def template_contents(self):
        r"""Gets the template_contents of this UpdateTemplateBody.

        模板内容列表

        :return: The template_contents of this UpdateTemplateBody.
        :rtype: list[:class:`huaweicloudsdkbcc.v1.TemplateItemEnum`]
        """
        return self._template_contents

    @template_contents.setter
    def template_contents(self, template_contents):
        r"""Sets the template_contents of this UpdateTemplateBody.

        模板内容列表

        :param template_contents: The template_contents of this UpdateTemplateBody.
        :type template_contents: list[:class:`huaweicloudsdkbcc.v1.TemplateItemEnum`]
        """
        self._template_contents = template_contents

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
        if not isinstance(other, UpdateTemplateBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

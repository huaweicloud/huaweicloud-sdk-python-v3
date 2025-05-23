# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DeleteNotificationTemplateBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'template_names': 'list[str]'
    }

    attribute_map = {
        'template_names': 'template_names'
    }

    def __init__(self, template_names=None):
        r"""DeleteNotificationTemplateBody

        The model defined in huaweicloud sdk

        :param template_names: 待删除模板名称数组
        :type template_names: list[str]
        """
        
        

        self._template_names = None
        self.discriminator = None

        self.template_names = template_names

    @property
    def template_names(self):
        r"""Gets the template_names of this DeleteNotificationTemplateBody.

        待删除模板名称数组

        :return: The template_names of this DeleteNotificationTemplateBody.
        :rtype: list[str]
        """
        return self._template_names

    @template_names.setter
    def template_names(self, template_names):
        r"""Sets the template_names of this DeleteNotificationTemplateBody.

        待删除模板名称数组

        :param template_names: The template_names of this DeleteNotificationTemplateBody.
        :type template_names: list[str]
        """
        self._template_names = template_names

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
        if not isinstance(other, DeleteNotificationTemplateBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

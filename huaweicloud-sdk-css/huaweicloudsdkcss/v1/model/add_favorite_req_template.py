# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AddFavoriteReqTemplate:

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
        'desc': 'str'
    }

    attribute_map = {
        'template_name': 'templateName',
        'desc': 'desc'
    }

    def __init__(self, template_name=None, desc=None):
        """AddFavoriteReqTemplate

        The model defined in huaweicloud sdk

        :param template_name: 模板名称。
        :type template_name: str
        :param desc: 模板描述。
        :type desc: str
        """
        
        

        self._template_name = None
        self._desc = None
        self.discriminator = None

        self.template_name = template_name
        if desc is not None:
            self.desc = desc

    @property
    def template_name(self):
        """Gets the template_name of this AddFavoriteReqTemplate.

        模板名称。

        :return: The template_name of this AddFavoriteReqTemplate.
        :rtype: str
        """
        return self._template_name

    @template_name.setter
    def template_name(self, template_name):
        """Sets the template_name of this AddFavoriteReqTemplate.

        模板名称。

        :param template_name: The template_name of this AddFavoriteReqTemplate.
        :type template_name: str
        """
        self._template_name = template_name

    @property
    def desc(self):
        """Gets the desc of this AddFavoriteReqTemplate.

        模板描述。

        :return: The desc of this AddFavoriteReqTemplate.
        :rtype: str
        """
        return self._desc

    @desc.setter
    def desc(self, desc):
        """Sets the desc of this AddFavoriteReqTemplate.

        模板描述。

        :param desc: The desc of this AddFavoriteReqTemplate.
        :type desc: str
        """
        self._desc = desc

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
        if not isinstance(other, AddFavoriteReqTemplate):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

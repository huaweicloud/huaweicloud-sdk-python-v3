# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AimPersonalTemplatePage:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'page_order': 'int',
        'contents': 'list[AimPersonalTemplateContent]'
    }

    attribute_map = {
        'page_order': 'page_order',
        'contents': 'contents'
    }

    def __init__(self, page_order=None, contents=None):
        """AimPersonalTemplatePage

        The model defined in huaweicloud sdk

        :param page_order: 分页显示，指示当前展示第几页，从1开始，最大支持10页。
        :type page_order: int
        :param contents: 该page下的协议内容。
        :type contents: list[:class:`huaweicloudsdkkoomessage.v1.AimPersonalTemplateContent`]
        """
        
        

        self._page_order = None
        self._contents = None
        self.discriminator = None

        self.page_order = page_order
        self.contents = contents

    @property
    def page_order(self):
        """Gets the page_order of this AimPersonalTemplatePage.

        分页显示，指示当前展示第几页，从1开始，最大支持10页。

        :return: The page_order of this AimPersonalTemplatePage.
        :rtype: int
        """
        return self._page_order

    @page_order.setter
    def page_order(self, page_order):
        """Sets the page_order of this AimPersonalTemplatePage.

        分页显示，指示当前展示第几页，从1开始，最大支持10页。

        :param page_order: The page_order of this AimPersonalTemplatePage.
        :type page_order: int
        """
        self._page_order = page_order

    @property
    def contents(self):
        """Gets the contents of this AimPersonalTemplatePage.

        该page下的协议内容。

        :return: The contents of this AimPersonalTemplatePage.
        :rtype: list[:class:`huaweicloudsdkkoomessage.v1.AimPersonalTemplateContent`]
        """
        return self._contents

    @contents.setter
    def contents(self, contents):
        """Sets the contents of this AimPersonalTemplatePage.

        该page下的协议内容。

        :param contents: The contents of this AimPersonalTemplatePage.
        :type contents: list[:class:`huaweicloudsdkkoomessage.v1.AimPersonalTemplateContent`]
        """
        self._contents = contents

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
        if not isinstance(other, AimPersonalTemplatePage):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

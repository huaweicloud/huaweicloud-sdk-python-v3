# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AppTemplateResourceDetail:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'resource_name': 'str',
        'icon': 'str',
        'href': 'str'
    }

    attribute_map = {
        'resource_name': 'resource_name',
        'icon': 'icon',
        'href': 'href'
    }

    def __init__(self, resource_name=None, icon=None, href=None):
        r"""AppTemplateResourceDetail

        The model defined in huaweicloud sdk

        :param resource_name: 资源名称
        :type resource_name: str
        :param icon: 图标文件（base64编码）
        :type icon: str
        :param href: 超链接地址
        :type href: str
        """
        
        

        self._resource_name = None
        self._icon = None
        self._href = None
        self.discriminator = None

        if resource_name is not None:
            self.resource_name = resource_name
        if icon is not None:
            self.icon = icon
        if href is not None:
            self.href = href

    @property
    def resource_name(self):
        r"""Gets the resource_name of this AppTemplateResourceDetail.

        资源名称

        :return: The resource_name of this AppTemplateResourceDetail.
        :rtype: str
        """
        return self._resource_name

    @resource_name.setter
    def resource_name(self, resource_name):
        r"""Sets the resource_name of this AppTemplateResourceDetail.

        资源名称

        :param resource_name: The resource_name of this AppTemplateResourceDetail.
        :type resource_name: str
        """
        self._resource_name = resource_name

    @property
    def icon(self):
        r"""Gets the icon of this AppTemplateResourceDetail.

        图标文件（base64编码）

        :return: The icon of this AppTemplateResourceDetail.
        :rtype: str
        """
        return self._icon

    @icon.setter
    def icon(self, icon):
        r"""Sets the icon of this AppTemplateResourceDetail.

        图标文件（base64编码）

        :param icon: The icon of this AppTemplateResourceDetail.
        :type icon: str
        """
        self._icon = icon

    @property
    def href(self):
        r"""Gets the href of this AppTemplateResourceDetail.

        超链接地址

        :return: The href of this AppTemplateResourceDetail.
        :rtype: str
        """
        return self._href

    @href.setter
    def href(self, href):
        r"""Sets the href of this AppTemplateResourceDetail.

        超链接地址

        :param href: The href of this AppTemplateResourceDetail.
        :type href: str
        """
        self._href = href

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
        if not isinstance(other, AppTemplateResourceDetail):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class WafBlockPage:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'template': 'str',
        'custom_page': 'WafCustomPage',
        'redirect_url': 'str'
    }

    attribute_map = {
        'template': 'template',
        'custom_page': 'custom_page',
        'redirect_url': 'redirect_url'
    }

    def __init__(self, template=None, custom_page=None, redirect_url=None):
        """WafBlockPage

        The model defined in huaweicloud sdk

        :param template: 拦截模板名称
        :type template: str
        :param custom_page: 
        :type custom_page: :class:`huaweicloudsdkedgesec.v1.WafCustomPage`
        :param redirect_url: 重定向URL
        :type redirect_url: str
        """
        
        

        self._template = None
        self._custom_page = None
        self._redirect_url = None
        self.discriminator = None

        self.template = template
        if custom_page is not None:
            self.custom_page = custom_page
        if redirect_url is not None:
            self.redirect_url = redirect_url

    @property
    def template(self):
        """Gets the template of this WafBlockPage.

        拦截模板名称

        :return: The template of this WafBlockPage.
        :rtype: str
        """
        return self._template

    @template.setter
    def template(self, template):
        """Sets the template of this WafBlockPage.

        拦截模板名称

        :param template: The template of this WafBlockPage.
        :type template: str
        """
        self._template = template

    @property
    def custom_page(self):
        """Gets the custom_page of this WafBlockPage.

        :return: The custom_page of this WafBlockPage.
        :rtype: :class:`huaweicloudsdkedgesec.v1.WafCustomPage`
        """
        return self._custom_page

    @custom_page.setter
    def custom_page(self, custom_page):
        """Sets the custom_page of this WafBlockPage.

        :param custom_page: The custom_page of this WafBlockPage.
        :type custom_page: :class:`huaweicloudsdkedgesec.v1.WafCustomPage`
        """
        self._custom_page = custom_page

    @property
    def redirect_url(self):
        """Gets the redirect_url of this WafBlockPage.

        重定向URL

        :return: The redirect_url of this WafBlockPage.
        :rtype: str
        """
        return self._redirect_url

    @redirect_url.setter
    def redirect_url(self, redirect_url):
        """Sets the redirect_url of this WafBlockPage.

        重定向URL

        :param redirect_url: The redirect_url of this WafBlockPage.
        :type redirect_url: str
        """
        self._redirect_url = redirect_url

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
        if not isinstance(other, WafBlockPage):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

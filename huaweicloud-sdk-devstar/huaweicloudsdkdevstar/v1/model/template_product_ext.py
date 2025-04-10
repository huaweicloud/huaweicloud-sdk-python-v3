# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class TemplateProductExt:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'id': 'str',
        'productshort': 'str',
        'product_name': 'str',
        'home_link': 'str',
        'api_link': 'str',
        'sdk_link': 'str',
        'doc_link': 'str',
        'logo_link': 'str'
    }

    attribute_map = {
        'id': 'id',
        'productshort': 'productshort',
        'product_name': 'product_name',
        'home_link': 'home_link',
        'api_link': 'api_link',
        'sdk_link': 'sdk_link',
        'doc_link': 'doc_link',
        'logo_link': 'logo_link'
    }

    def __init__(self, id=None, productshort=None, product_name=None, home_link=None, api_link=None, sdk_link=None, doc_link=None, logo_link=None):
        r"""TemplateProductExt

        The model defined in huaweicloud sdk

        :param id: 产品id。
        :type id: str
        :param productshort: 产品短名。
        :type productshort: str
        :param product_name: 产品名。
        :type product_name: str
        :param home_link: 首页链接。
        :type home_link: str
        :param api_link: api调试链接。
        :type api_link: str
        :param sdk_link: sdk下载链接。
        :type sdk_link: str
        :param doc_link: 文档链接。
        :type doc_link: str
        :param logo_link: logo链接。
        :type logo_link: str
        """
        
        

        self._id = None
        self._productshort = None
        self._product_name = None
        self._home_link = None
        self._api_link = None
        self._sdk_link = None
        self._doc_link = None
        self._logo_link = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if productshort is not None:
            self.productshort = productshort
        if product_name is not None:
            self.product_name = product_name
        if home_link is not None:
            self.home_link = home_link
        if api_link is not None:
            self.api_link = api_link
        if sdk_link is not None:
            self.sdk_link = sdk_link
        if doc_link is not None:
            self.doc_link = doc_link
        if logo_link is not None:
            self.logo_link = logo_link

    @property
    def id(self):
        r"""Gets the id of this TemplateProductExt.

        产品id。

        :return: The id of this TemplateProductExt.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this TemplateProductExt.

        产品id。

        :param id: The id of this TemplateProductExt.
        :type id: str
        """
        self._id = id

    @property
    def productshort(self):
        r"""Gets the productshort of this TemplateProductExt.

        产品短名。

        :return: The productshort of this TemplateProductExt.
        :rtype: str
        """
        return self._productshort

    @productshort.setter
    def productshort(self, productshort):
        r"""Sets the productshort of this TemplateProductExt.

        产品短名。

        :param productshort: The productshort of this TemplateProductExt.
        :type productshort: str
        """
        self._productshort = productshort

    @property
    def product_name(self):
        r"""Gets the product_name of this TemplateProductExt.

        产品名。

        :return: The product_name of this TemplateProductExt.
        :rtype: str
        """
        return self._product_name

    @product_name.setter
    def product_name(self, product_name):
        r"""Sets the product_name of this TemplateProductExt.

        产品名。

        :param product_name: The product_name of this TemplateProductExt.
        :type product_name: str
        """
        self._product_name = product_name

    @property
    def home_link(self):
        r"""Gets the home_link of this TemplateProductExt.

        首页链接。

        :return: The home_link of this TemplateProductExt.
        :rtype: str
        """
        return self._home_link

    @home_link.setter
    def home_link(self, home_link):
        r"""Sets the home_link of this TemplateProductExt.

        首页链接。

        :param home_link: The home_link of this TemplateProductExt.
        :type home_link: str
        """
        self._home_link = home_link

    @property
    def api_link(self):
        r"""Gets the api_link of this TemplateProductExt.

        api调试链接。

        :return: The api_link of this TemplateProductExt.
        :rtype: str
        """
        return self._api_link

    @api_link.setter
    def api_link(self, api_link):
        r"""Sets the api_link of this TemplateProductExt.

        api调试链接。

        :param api_link: The api_link of this TemplateProductExt.
        :type api_link: str
        """
        self._api_link = api_link

    @property
    def sdk_link(self):
        r"""Gets the sdk_link of this TemplateProductExt.

        sdk下载链接。

        :return: The sdk_link of this TemplateProductExt.
        :rtype: str
        """
        return self._sdk_link

    @sdk_link.setter
    def sdk_link(self, sdk_link):
        r"""Sets the sdk_link of this TemplateProductExt.

        sdk下载链接。

        :param sdk_link: The sdk_link of this TemplateProductExt.
        :type sdk_link: str
        """
        self._sdk_link = sdk_link

    @property
    def doc_link(self):
        r"""Gets the doc_link of this TemplateProductExt.

        文档链接。

        :return: The doc_link of this TemplateProductExt.
        :rtype: str
        """
        return self._doc_link

    @doc_link.setter
    def doc_link(self, doc_link):
        r"""Sets the doc_link of this TemplateProductExt.

        文档链接。

        :param doc_link: The doc_link of this TemplateProductExt.
        :type doc_link: str
        """
        self._doc_link = doc_link

    @property
    def logo_link(self):
        r"""Gets the logo_link of this TemplateProductExt.

        logo链接。

        :return: The logo_link of this TemplateProductExt.
        :rtype: str
        """
        return self._logo_link

    @logo_link.setter
    def logo_link(self, logo_link):
        r"""Sets the logo_link of this TemplateProductExt.

        logo链接。

        :param logo_link: The logo_link of this TemplateProductExt.
        :type logo_link: str
        """
        self._logo_link = logo_link

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
        if not isinstance(other, TemplateProductExt):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

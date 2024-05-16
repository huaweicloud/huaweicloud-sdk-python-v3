# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AppSearchParam:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'business_id': 'int',
        'region': 'str',
        'page': 'int',
        'page_size': 'int',
        'keyword': 'str'
    }

    attribute_map = {
        'business_id': 'business_id',
        'region': 'region',
        'page': 'page',
        'page_size': 'page_size',
        'keyword': 'keyword'
    }

    def __init__(self, business_id=None, region=None, page=None, page_size=None, keyword=None):
        """AppSearchParam

        The model defined in huaweicloud sdk

        :param business_id: 应用id。
        :type business_id: int
        :param region: 区域名称。
        :type region: str
        :param page: 页码。
        :type page: int
        :param page_size: 每页条数。
        :type page_size: int
        :param keyword: 关键字。
        :type keyword: str
        """
        
        

        self._business_id = None
        self._region = None
        self._page = None
        self._page_size = None
        self._keyword = None
        self.discriminator = None

        self.business_id = business_id
        self.region = region
        self.page = page
        if page_size is not None:
            self.page_size = page_size
        if keyword is not None:
            self.keyword = keyword

    @property
    def business_id(self):
        """Gets the business_id of this AppSearchParam.

        应用id。

        :return: The business_id of this AppSearchParam.
        :rtype: int
        """
        return self._business_id

    @business_id.setter
    def business_id(self, business_id):
        """Sets the business_id of this AppSearchParam.

        应用id。

        :param business_id: The business_id of this AppSearchParam.
        :type business_id: int
        """
        self._business_id = business_id

    @property
    def region(self):
        """Gets the region of this AppSearchParam.

        区域名称。

        :return: The region of this AppSearchParam.
        :rtype: str
        """
        return self._region

    @region.setter
    def region(self, region):
        """Sets the region of this AppSearchParam.

        区域名称。

        :param region: The region of this AppSearchParam.
        :type region: str
        """
        self._region = region

    @property
    def page(self):
        """Gets the page of this AppSearchParam.

        页码。

        :return: The page of this AppSearchParam.
        :rtype: int
        """
        return self._page

    @page.setter
    def page(self, page):
        """Sets the page of this AppSearchParam.

        页码。

        :param page: The page of this AppSearchParam.
        :type page: int
        """
        self._page = page

    @property
    def page_size(self):
        """Gets the page_size of this AppSearchParam.

        每页条数。

        :return: The page_size of this AppSearchParam.
        :rtype: int
        """
        return self._page_size

    @page_size.setter
    def page_size(self, page_size):
        """Sets the page_size of this AppSearchParam.

        每页条数。

        :param page_size: The page_size of this AppSearchParam.
        :type page_size: int
        """
        self._page_size = page_size

    @property
    def keyword(self):
        """Gets the keyword of this AppSearchParam.

        关键字。

        :return: The keyword of this AppSearchParam.
        :rtype: str
        """
        return self._keyword

    @keyword.setter
    def keyword(self, keyword):
        """Sets the keyword of this AppSearchParam.

        关键字。

        :param keyword: The keyword of this AppSearchParam.
        :type keyword: str
        """
        self._keyword = keyword

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
        if not isinstance(other, AppSearchParam):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

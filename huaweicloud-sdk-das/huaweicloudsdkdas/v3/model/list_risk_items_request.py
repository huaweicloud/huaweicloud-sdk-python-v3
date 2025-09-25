# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListRiskItemsRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'x_language': 'str',
        'datastore_type': 'str',
        'page': 'int',
        'limit': 'int'
    }

    attribute_map = {
        'x_language': 'X-Language',
        'datastore_type': 'datastore_type',
        'page': 'page',
        'limit': 'limit'
    }

    def __init__(self, x_language=None, datastore_type=None, page=None, limit=None):
        r"""ListRiskItemsRequest

        The model defined in huaweicloud sdk

        :param x_language: 语言
        :type x_language: str
        :param datastore_type: 数据库类型
        :type datastore_type: str
        :param page: 页码，默认1
        :type page: int
        :param limit: 每页记录数，默认20。
        :type limit: int
        """
        
        

        self._x_language = None
        self._datastore_type = None
        self._page = None
        self._limit = None
        self.discriminator = None

        if x_language is not None:
            self.x_language = x_language
        self.datastore_type = datastore_type
        if page is not None:
            self.page = page
        if limit is not None:
            self.limit = limit

    @property
    def x_language(self):
        r"""Gets the x_language of this ListRiskItemsRequest.

        语言

        :return: The x_language of this ListRiskItemsRequest.
        :rtype: str
        """
        return self._x_language

    @x_language.setter
    def x_language(self, x_language):
        r"""Sets the x_language of this ListRiskItemsRequest.

        语言

        :param x_language: The x_language of this ListRiskItemsRequest.
        :type x_language: str
        """
        self._x_language = x_language

    @property
    def datastore_type(self):
        r"""Gets the datastore_type of this ListRiskItemsRequest.

        数据库类型

        :return: The datastore_type of this ListRiskItemsRequest.
        :rtype: str
        """
        return self._datastore_type

    @datastore_type.setter
    def datastore_type(self, datastore_type):
        r"""Sets the datastore_type of this ListRiskItemsRequest.

        数据库类型

        :param datastore_type: The datastore_type of this ListRiskItemsRequest.
        :type datastore_type: str
        """
        self._datastore_type = datastore_type

    @property
    def page(self):
        r"""Gets the page of this ListRiskItemsRequest.

        页码，默认1

        :return: The page of this ListRiskItemsRequest.
        :rtype: int
        """
        return self._page

    @page.setter
    def page(self, page):
        r"""Sets the page of this ListRiskItemsRequest.

        页码，默认1

        :param page: The page of this ListRiskItemsRequest.
        :type page: int
        """
        self._page = page

    @property
    def limit(self):
        r"""Gets the limit of this ListRiskItemsRequest.

        每页记录数，默认20。

        :return: The limit of this ListRiskItemsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListRiskItemsRequest.

        每页记录数，默认20。

        :param limit: The limit of this ListRiskItemsRequest.
        :type limit: int
        """
        self._limit = limit

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
        if not isinstance(other, ListRiskItemsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

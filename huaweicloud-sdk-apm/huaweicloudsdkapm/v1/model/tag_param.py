# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class TagParam:

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
        'keyword': 'str',
        'page_enable': 'bool',
        'page_number': 'int',
        'page_size': 'int'
    }

    attribute_map = {
        'business_id': 'business_id',
        'keyword': 'keyword',
        'page_enable': 'page_enable',
        'page_number': 'page_number',
        'page_size': 'page_size'
    }

    def __init__(self, business_id=None, keyword=None, page_enable=None, page_number=None, page_size=None):
        r"""TagParam

        The model defined in huaweicloud sdk

        :param business_id: 应用id。
        :type business_id: int
        :param keyword: 关键字。
        :type keyword: str
        :param page_enable: 是否分页。
        :type page_enable: bool
        :param page_number: 每页容量。
        :type page_number: int
        :param page_size: 当前页码。
        :type page_size: int
        """
        
        

        self._business_id = None
        self._keyword = None
        self._page_enable = None
        self._page_number = None
        self._page_size = None
        self.discriminator = None

        self.business_id = business_id
        if keyword is not None:
            self.keyword = keyword
        if page_enable is not None:
            self.page_enable = page_enable
        if page_number is not None:
            self.page_number = page_number
        if page_size is not None:
            self.page_size = page_size

    @property
    def business_id(self):
        r"""Gets the business_id of this TagParam.

        应用id。

        :return: The business_id of this TagParam.
        :rtype: int
        """
        return self._business_id

    @business_id.setter
    def business_id(self, business_id):
        r"""Sets the business_id of this TagParam.

        应用id。

        :param business_id: The business_id of this TagParam.
        :type business_id: int
        """
        self._business_id = business_id

    @property
    def keyword(self):
        r"""Gets the keyword of this TagParam.

        关键字。

        :return: The keyword of this TagParam.
        :rtype: str
        """
        return self._keyword

    @keyword.setter
    def keyword(self, keyword):
        r"""Sets the keyword of this TagParam.

        关键字。

        :param keyword: The keyword of this TagParam.
        :type keyword: str
        """
        self._keyword = keyword

    @property
    def page_enable(self):
        r"""Gets the page_enable of this TagParam.

        是否分页。

        :return: The page_enable of this TagParam.
        :rtype: bool
        """
        return self._page_enable

    @page_enable.setter
    def page_enable(self, page_enable):
        r"""Sets the page_enable of this TagParam.

        是否分页。

        :param page_enable: The page_enable of this TagParam.
        :type page_enable: bool
        """
        self._page_enable = page_enable

    @property
    def page_number(self):
        r"""Gets the page_number of this TagParam.

        每页容量。

        :return: The page_number of this TagParam.
        :rtype: int
        """
        return self._page_number

    @page_number.setter
    def page_number(self, page_number):
        r"""Sets the page_number of this TagParam.

        每页容量。

        :param page_number: The page_number of this TagParam.
        :type page_number: int
        """
        self._page_number = page_number

    @property
    def page_size(self):
        r"""Gets the page_size of this TagParam.

        当前页码。

        :return: The page_size of this TagParam.
        :rtype: int
        """
        return self._page_size

    @page_size.setter
    def page_size(self, page_size):
        r"""Sets the page_size of this TagParam.

        当前页码。

        :param page_size: The page_size of this TagParam.
        :type page_size: int
        """
        self._page_size = page_size

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
        if not isinstance(other, TagParam):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

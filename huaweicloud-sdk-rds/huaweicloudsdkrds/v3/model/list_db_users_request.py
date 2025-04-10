# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListDbUsersRequest:

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
        'instance_id': 'str',
        'page': 'int',
        'limit': 'int'
    }

    attribute_map = {
        'x_language': 'X-Language',
        'instance_id': 'instance_id',
        'page': 'page',
        'limit': 'limit'
    }

    def __init__(self, x_language=None, instance_id=None, page=None, limit=None):
        r"""ListDbUsersRequest

        The model defined in huaweicloud sdk

        :param x_language: 语言
        :type x_language: str
        :param instance_id: 实例ID。
        :type instance_id: str
        :param page: 分页页码，从1开始。
        :type page: int
        :param limit: 每页数据条数。取值范围[1, 100]。
        :type limit: int
        """
        
        

        self._x_language = None
        self._instance_id = None
        self._page = None
        self._limit = None
        self.discriminator = None

        if x_language is not None:
            self.x_language = x_language
        self.instance_id = instance_id
        self.page = page
        self.limit = limit

    @property
    def x_language(self):
        r"""Gets the x_language of this ListDbUsersRequest.

        语言

        :return: The x_language of this ListDbUsersRequest.
        :rtype: str
        """
        return self._x_language

    @x_language.setter
    def x_language(self, x_language):
        r"""Sets the x_language of this ListDbUsersRequest.

        语言

        :param x_language: The x_language of this ListDbUsersRequest.
        :type x_language: str
        """
        self._x_language = x_language

    @property
    def instance_id(self):
        r"""Gets the instance_id of this ListDbUsersRequest.

        实例ID。

        :return: The instance_id of this ListDbUsersRequest.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        r"""Sets the instance_id of this ListDbUsersRequest.

        实例ID。

        :param instance_id: The instance_id of this ListDbUsersRequest.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def page(self):
        r"""Gets the page of this ListDbUsersRequest.

        分页页码，从1开始。

        :return: The page of this ListDbUsersRequest.
        :rtype: int
        """
        return self._page

    @page.setter
    def page(self, page):
        r"""Sets the page of this ListDbUsersRequest.

        分页页码，从1开始。

        :param page: The page of this ListDbUsersRequest.
        :type page: int
        """
        self._page = page

    @property
    def limit(self):
        r"""Gets the limit of this ListDbUsersRequest.

        每页数据条数。取值范围[1, 100]。

        :return: The limit of this ListDbUsersRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListDbUsersRequest.

        每页数据条数。取值范围[1, 100]。

        :param limit: The limit of this ListDbUsersRequest.
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
        if not isinstance(other, ListDbUsersRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

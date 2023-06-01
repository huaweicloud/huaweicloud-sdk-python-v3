# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ResponseCodeSum:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'sum1xx': 'int',
        'sum2xx': 'int',
        'sum3xx': 'int',
        'sum4xx': 'int',
        'sum5xx': 'int'
    }

    attribute_map = {
        'sum1xx': 'sum1xx',
        'sum2xx': 'sum2xx',
        'sum3xx': 'sum3xx',
        'sum4xx': 'sum4xx',
        'sum5xx': 'sum5xx'
    }

    def __init__(self, sum1xx=None, sum2xx=None, sum3xx=None, sum4xx=None, sum5xx=None):
        """ResponseCodeSum

        The model defined in huaweicloud sdk

        :param sum1xx: 1xx请求数
        :type sum1xx: int
        :param sum2xx: 2xx请求数
        :type sum2xx: int
        :param sum3xx: 3xx请求数
        :type sum3xx: int
        :param sum4xx: 4xx请求数
        :type sum4xx: int
        :param sum5xx: 5xx请求数
        :type sum5xx: int
        """
        
        

        self._sum1xx = None
        self._sum2xx = None
        self._sum3xx = None
        self._sum4xx = None
        self._sum5xx = None
        self.discriminator = None

        if sum1xx is not None:
            self.sum1xx = sum1xx
        if sum2xx is not None:
            self.sum2xx = sum2xx
        if sum3xx is not None:
            self.sum3xx = sum3xx
        if sum4xx is not None:
            self.sum4xx = sum4xx
        if sum5xx is not None:
            self.sum5xx = sum5xx

    @property
    def sum1xx(self):
        """Gets the sum1xx of this ResponseCodeSum.

        1xx请求数

        :return: The sum1xx of this ResponseCodeSum.
        :rtype: int
        """
        return self._sum1xx

    @sum1xx.setter
    def sum1xx(self, sum1xx):
        """Sets the sum1xx of this ResponseCodeSum.

        1xx请求数

        :param sum1xx: The sum1xx of this ResponseCodeSum.
        :type sum1xx: int
        """
        self._sum1xx = sum1xx

    @property
    def sum2xx(self):
        """Gets the sum2xx of this ResponseCodeSum.

        2xx请求数

        :return: The sum2xx of this ResponseCodeSum.
        :rtype: int
        """
        return self._sum2xx

    @sum2xx.setter
    def sum2xx(self, sum2xx):
        """Sets the sum2xx of this ResponseCodeSum.

        2xx请求数

        :param sum2xx: The sum2xx of this ResponseCodeSum.
        :type sum2xx: int
        """
        self._sum2xx = sum2xx

    @property
    def sum3xx(self):
        """Gets the sum3xx of this ResponseCodeSum.

        3xx请求数

        :return: The sum3xx of this ResponseCodeSum.
        :rtype: int
        """
        return self._sum3xx

    @sum3xx.setter
    def sum3xx(self, sum3xx):
        """Sets the sum3xx of this ResponseCodeSum.

        3xx请求数

        :param sum3xx: The sum3xx of this ResponseCodeSum.
        :type sum3xx: int
        """
        self._sum3xx = sum3xx

    @property
    def sum4xx(self):
        """Gets the sum4xx of this ResponseCodeSum.

        4xx请求数

        :return: The sum4xx of this ResponseCodeSum.
        :rtype: int
        """
        return self._sum4xx

    @sum4xx.setter
    def sum4xx(self, sum4xx):
        """Sets the sum4xx of this ResponseCodeSum.

        4xx请求数

        :param sum4xx: The sum4xx of this ResponseCodeSum.
        :type sum4xx: int
        """
        self._sum4xx = sum4xx

    @property
    def sum5xx(self):
        """Gets the sum5xx of this ResponseCodeSum.

        5xx请求数

        :return: The sum5xx of this ResponseCodeSum.
        :rtype: int
        """
        return self._sum5xx

    @sum5xx.setter
    def sum5xx(self, sum5xx):
        """Sets the sum5xx of this ResponseCodeSum.

        5xx请求数

        :param sum5xx: The sum5xx of this ResponseCodeSum.
        :type sum5xx: int
        """
        self._sum5xx = sum5xx

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
        if not isinstance(other, ResponseCodeSum):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

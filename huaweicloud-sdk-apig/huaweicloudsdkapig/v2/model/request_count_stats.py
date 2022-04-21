# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class RequestCountStats:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'req_count': 'int',
        'req_count2xx': 'int',
        'req_count4xx': 'int',
        'req_count5xx': 'int',
        'req_count_error': 'int'
    }

    attribute_map = {
        'req_count': 'req_count',
        'req_count2xx': 'req_count2xx',
        'req_count4xx': 'req_count4xx',
        'req_count5xx': 'req_count5xx',
        'req_count_error': 'req_count_error'
    }

    def __init__(self, req_count=None, req_count2xx=None, req_count4xx=None, req_count5xx=None, req_count_error=None):
        """RequestCountStats

        The model defined in huaweicloud sdk

        :param req_count: 请求总次数
        :type req_count: int
        :param req_count2xx: 2xx响应码总次数
        :type req_count2xx: int
        :param req_count4xx: 4xx响应码总次数
        :type req_count4xx: int
        :param req_count5xx: 5xx响应码总次数
        :type req_count5xx: int
        :param req_count_error: 错误次数
        :type req_count_error: int
        """
        
        

        self._req_count = None
        self._req_count2xx = None
        self._req_count4xx = None
        self._req_count5xx = None
        self._req_count_error = None
        self.discriminator = None

        if req_count is not None:
            self.req_count = req_count
        if req_count2xx is not None:
            self.req_count2xx = req_count2xx
        if req_count4xx is not None:
            self.req_count4xx = req_count4xx
        if req_count5xx is not None:
            self.req_count5xx = req_count5xx
        if req_count_error is not None:
            self.req_count_error = req_count_error

    @property
    def req_count(self):
        """Gets the req_count of this RequestCountStats.

        请求总次数

        :return: The req_count of this RequestCountStats.
        :rtype: int
        """
        return self._req_count

    @req_count.setter
    def req_count(self, req_count):
        """Sets the req_count of this RequestCountStats.

        请求总次数

        :param req_count: The req_count of this RequestCountStats.
        :type req_count: int
        """
        self._req_count = req_count

    @property
    def req_count2xx(self):
        """Gets the req_count2xx of this RequestCountStats.

        2xx响应码总次数

        :return: The req_count2xx of this RequestCountStats.
        :rtype: int
        """
        return self._req_count2xx

    @req_count2xx.setter
    def req_count2xx(self, req_count2xx):
        """Sets the req_count2xx of this RequestCountStats.

        2xx响应码总次数

        :param req_count2xx: The req_count2xx of this RequestCountStats.
        :type req_count2xx: int
        """
        self._req_count2xx = req_count2xx

    @property
    def req_count4xx(self):
        """Gets the req_count4xx of this RequestCountStats.

        4xx响应码总次数

        :return: The req_count4xx of this RequestCountStats.
        :rtype: int
        """
        return self._req_count4xx

    @req_count4xx.setter
    def req_count4xx(self, req_count4xx):
        """Sets the req_count4xx of this RequestCountStats.

        4xx响应码总次数

        :param req_count4xx: The req_count4xx of this RequestCountStats.
        :type req_count4xx: int
        """
        self._req_count4xx = req_count4xx

    @property
    def req_count5xx(self):
        """Gets the req_count5xx of this RequestCountStats.

        5xx响应码总次数

        :return: The req_count5xx of this RequestCountStats.
        :rtype: int
        """
        return self._req_count5xx

    @req_count5xx.setter
    def req_count5xx(self, req_count5xx):
        """Sets the req_count5xx of this RequestCountStats.

        5xx响应码总次数

        :param req_count5xx: The req_count5xx of this RequestCountStats.
        :type req_count5xx: int
        """
        self._req_count5xx = req_count5xx

    @property
    def req_count_error(self):
        """Gets the req_count_error of this RequestCountStats.

        错误次数

        :return: The req_count_error of this RequestCountStats.
        :rtype: int
        """
        return self._req_count_error

    @req_count_error.setter
    def req_count_error(self, req_count_error):
        """Sets the req_count_error of this RequestCountStats.

        错误次数

        :param req_count_error: The req_count_error of this RequestCountStats.
        :type req_count_error: int
        """
        self._req_count_error = req_count_error

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
        if not isinstance(other, RequestCountStats):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

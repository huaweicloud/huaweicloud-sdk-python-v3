# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class QueryRunListParam:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'page': 'int',
        'page_size': 'int',
        'start_time': 'str',
        'end_time': 'str'
    }

    attribute_map = {
        'page': 'page',
        'page_size': 'page_size',
        'start_time': 'start_time',
        'end_time': 'end_time'
    }

    def __init__(self, page=None, page_size=None, start_time=None, end_time=None):
        """QueryRunListParam

        The model defined in huaweicloud sdk

        :param page: 页码
        :type page: int
        :param page_size: 每页大小
        :type page_size: int
        :param start_time: 查询开始时间
        :type start_time: str
        :param end_time: 查询结束时间
        :type end_time: str
        """
        
        

        self._page = None
        self._page_size = None
        self._start_time = None
        self._end_time = None
        self.discriminator = None

        self.page = page
        self.page_size = page_size
        if start_time is not None:
            self.start_time = start_time
        if end_time is not None:
            self.end_time = end_time

    @property
    def page(self):
        """Gets the page of this QueryRunListParam.

        页码

        :return: The page of this QueryRunListParam.
        :rtype: int
        """
        return self._page

    @page.setter
    def page(self, page):
        """Sets the page of this QueryRunListParam.

        页码

        :param page: The page of this QueryRunListParam.
        :type page: int
        """
        self._page = page

    @property
    def page_size(self):
        """Gets the page_size of this QueryRunListParam.

        每页大小

        :return: The page_size of this QueryRunListParam.
        :rtype: int
        """
        return self._page_size

    @page_size.setter
    def page_size(self, page_size):
        """Sets the page_size of this QueryRunListParam.

        每页大小

        :param page_size: The page_size of this QueryRunListParam.
        :type page_size: int
        """
        self._page_size = page_size

    @property
    def start_time(self):
        """Gets the start_time of this QueryRunListParam.

        查询开始时间

        :return: The start_time of this QueryRunListParam.
        :rtype: str
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        """Sets the start_time of this QueryRunListParam.

        查询开始时间

        :param start_time: The start_time of this QueryRunListParam.
        :type start_time: str
        """
        self._start_time = start_time

    @property
    def end_time(self):
        """Gets the end_time of this QueryRunListParam.

        查询结束时间

        :return: The end_time of this QueryRunListParam.
        :rtype: str
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        """Sets the end_time of this QueryRunListParam.

        查询结束时间

        :param end_time: The end_time of this QueryRunListParam.
        :type end_time: str
        """
        self._end_time = end_time

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
        if not isinstance(other, QueryRunListParam):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

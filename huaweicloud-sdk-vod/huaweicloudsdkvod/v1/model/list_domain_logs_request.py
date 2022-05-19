# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListDomainLogsRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'domain_name': 'str',
        'query_date': 'str',
        'page_size': 'int',
        'page_number': 'int'
    }

    attribute_map = {
        'domain_name': 'domain_name',
        'query_date': 'query_date',
        'page_size': 'page_size',
        'page_number': 'page_number'
    }

    def __init__(self, domain_name=None, query_date=None, page_size=None, page_number=None):
        """ListDomainLogsRequest

        The model defined in huaweicloud sdk

        :param domain_name: 加速域名，参考格式：www.test1.com。
        :type domain_name: str
        :param query_date: 查询开始时间，格式为yyyyMMddHHmmss。 - 查询结果为开始时间之后24小时内的日志数据 - 只能查最近一个月内的数据
        :type query_date: str
        :param page_size: 每页显示日志数量。 
        :type page_size: int
        :param page_number: 当前页数。 
        :type page_number: int
        """
        
        

        self._domain_name = None
        self._query_date = None
        self._page_size = None
        self._page_number = None
        self.discriminator = None

        self.domain_name = domain_name
        self.query_date = query_date
        if page_size is not None:
            self.page_size = page_size
        if page_number is not None:
            self.page_number = page_number

    @property
    def domain_name(self):
        """Gets the domain_name of this ListDomainLogsRequest.

        加速域名，参考格式：www.test1.com。

        :return: The domain_name of this ListDomainLogsRequest.
        :rtype: str
        """
        return self._domain_name

    @domain_name.setter
    def domain_name(self, domain_name):
        """Sets the domain_name of this ListDomainLogsRequest.

        加速域名，参考格式：www.test1.com。

        :param domain_name: The domain_name of this ListDomainLogsRequest.
        :type domain_name: str
        """
        self._domain_name = domain_name

    @property
    def query_date(self):
        """Gets the query_date of this ListDomainLogsRequest.

        查询开始时间，格式为yyyyMMddHHmmss。 - 查询结果为开始时间之后24小时内的日志数据 - 只能查最近一个月内的数据

        :return: The query_date of this ListDomainLogsRequest.
        :rtype: str
        """
        return self._query_date

    @query_date.setter
    def query_date(self, query_date):
        """Sets the query_date of this ListDomainLogsRequest.

        查询开始时间，格式为yyyyMMddHHmmss。 - 查询结果为开始时间之后24小时内的日志数据 - 只能查最近一个月内的数据

        :param query_date: The query_date of this ListDomainLogsRequest.
        :type query_date: str
        """
        self._query_date = query_date

    @property
    def page_size(self):
        """Gets the page_size of this ListDomainLogsRequest.

        每页显示日志数量。 

        :return: The page_size of this ListDomainLogsRequest.
        :rtype: int
        """
        return self._page_size

    @page_size.setter
    def page_size(self, page_size):
        """Sets the page_size of this ListDomainLogsRequest.

        每页显示日志数量。 

        :param page_size: The page_size of this ListDomainLogsRequest.
        :type page_size: int
        """
        self._page_size = page_size

    @property
    def page_number(self):
        """Gets the page_number of this ListDomainLogsRequest.

        当前页数。 

        :return: The page_number of this ListDomainLogsRequest.
        :rtype: int
        """
        return self._page_number

    @page_number.setter
    def page_number(self, page_number):
        """Sets the page_number of this ListDomainLogsRequest.

        当前页数。 

        :param page_number: The page_number of this ListDomainLogsRequest.
        :type page_number: int
        """
        self._page_number = page_number

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
        if not isinstance(other, ListDomainLogsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

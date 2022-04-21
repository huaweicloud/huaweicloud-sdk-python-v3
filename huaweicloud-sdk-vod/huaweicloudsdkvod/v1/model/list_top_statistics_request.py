# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListTopStatisticsRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'domain': 'str',
        'date': 'str'
    }

    attribute_map = {
        'domain': 'domain',
        'date': 'date'
    }

    def __init__(self, domain=None, date=None):
        """ListTopStatisticsRequest

        The model defined in huaweicloud sdk

        :param domain: 查询域名，暂只支持查询单个或者全部域名。  取值如下： - 单个加速域名，格式：example.test1.com。 - ALL：表示查询名下全部域名。
        :type domain: str
        :param date: 查询日期，格式为yyyymmdd - date必须为昨天或之前的日期。 - 最多只能查最近一个月内的数据。
        :type date: str
        """
        
        

        self._domain = None
        self._date = None
        self.discriminator = None

        self.domain = domain
        self.date = date

    @property
    def domain(self):
        """Gets the domain of this ListTopStatisticsRequest.

        查询域名，暂只支持查询单个或者全部域名。  取值如下： - 单个加速域名，格式：example.test1.com。 - ALL：表示查询名下全部域名。

        :return: The domain of this ListTopStatisticsRequest.
        :rtype: str
        """
        return self._domain

    @domain.setter
    def domain(self, domain):
        """Sets the domain of this ListTopStatisticsRequest.

        查询域名，暂只支持查询单个或者全部域名。  取值如下： - 单个加速域名，格式：example.test1.com。 - ALL：表示查询名下全部域名。

        :param domain: The domain of this ListTopStatisticsRequest.
        :type domain: str
        """
        self._domain = domain

    @property
    def date(self):
        """Gets the date of this ListTopStatisticsRequest.

        查询日期，格式为yyyymmdd - date必须为昨天或之前的日期。 - 最多只能查最近一个月内的数据。

        :return: The date of this ListTopStatisticsRequest.
        :rtype: str
        """
        return self._date

    @date.setter
    def date(self, date):
        """Sets the date of this ListTopStatisticsRequest.

        查询日期，格式为yyyymmdd - date必须为昨天或之前的日期。 - 最多只能查最近一个月内的数据。

        :param date: The date of this ListTopStatisticsRequest.
        :type date: str
        """
        self._date = date

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
        if not isinstance(other, ListTopStatisticsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

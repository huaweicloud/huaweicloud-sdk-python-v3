# coding: utf-8

import pprint
import re

import six





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
        """ListTopStatisticsRequest - a model defined in huaweicloud sdk"""
        
        

        self._domain = None
        self._date = None
        self.discriminator = None

        self.domain = domain
        self.date = date

    @property
    def domain(self):
        """Gets the domain of this ListTopStatisticsRequest.

        加速域名，格式：www.test1.com。ALL表示查询名下全部域名。（TopN视频信息要么查询单个域名要么查询所有域名） 

        :return: The domain of this ListTopStatisticsRequest.
        :rtype: str
        """
        return self._domain

    @domain.setter
    def domain(self, domain):
        """Sets the domain of this ListTopStatisticsRequest.

        加速域名，格式：www.test1.com。ALL表示查询名下全部域名。（TopN视频信息要么查询单个域名要么查询所有域名） 

        :param domain: The domain of this ListTopStatisticsRequest.
        :type: str
        """
        self._domain = domain

    @property
    def date(self):
        """Gets the date of this ListTopStatisticsRequest.

        查询日期，格式为yyyymmdd。 1）  date必须为昨天或之前的日期 2）  只能查最近一个月内的数据 

        :return: The date of this ListTopStatisticsRequest.
        :rtype: str
        """
        return self._date

    @date.setter
    def date(self, date):
        """Sets the date of this ListTopStatisticsRequest.

        查询日期，格式为yyyymmdd。 1）  date必须为昨天或之前的日期 2）  只能查最近一个月内的数据 

        :param date: The date of this ListTopStatisticsRequest.
        :type: str
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
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ListTopStatisticsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

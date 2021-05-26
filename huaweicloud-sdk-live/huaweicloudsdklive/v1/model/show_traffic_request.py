# coding: utf-8

import pprint
import re

import six





class ShowTrafficRequest:


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
        'start_time': 'str',
        'end_time': 'str',
        'step': 'int'
    }

    attribute_map = {
        'domain': 'domain',
        'start_time': 'start_time',
        'end_time': 'end_time',
        'step': 'step'
    }

    def __init__(self, domain=None, start_time=None, end_time=None, step=None):
        """ShowTrafficRequest - a model defined in huaweicloud sdk"""
        
        

        self._domain = None
        self._start_time = None
        self._end_time = None
        self._step = None
        self.discriminator = None

        if domain is not None:
            self.domain = domain
        if start_time is not None:
            self.start_time = start_time
        if end_time is not None:
            self.end_time = end_time
        if step is not None:
            self.step = step

    @property
    def domain(self):
        """Gets the domain of this ShowTrafficRequest.

        播放域名，不指定域名表示查询租户所有域名汇总流量

        :return: The domain of this ShowTrafficRequest.
        :rtype: str
        """
        return self._domain

    @domain.setter
    def domain(self, domain):
        """Sets the domain of this ShowTrafficRequest.

        播放域名，不指定域名表示查询租户所有域名汇总流量

        :param domain: The domain of this ShowTrafficRequest.
        :type: str
        """
        self._domain = domain

    @property
    def start_time(self):
        """Gets the start_time of this ShowTrafficRequest.

        查询起始时间，UTC时间，格式：yyyy-MM-ddTHH:mm:ssZ

        :return: The start_time of this ShowTrafficRequest.
        :rtype: str
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        """Sets the start_time of this ShowTrafficRequest.

        查询起始时间，UTC时间，格式：yyyy-MM-ddTHH:mm:ssZ

        :param start_time: The start_time of this ShowTrafficRequest.
        :type: str
        """
        self._start_time = start_time

    @property
    def end_time(self):
        """Gets the end_time of this ShowTrafficRequest.

        查询结束时间，UTC时间，格式：yyyy-MM-ddTHH:mm:ssZ。  - start_time与end_time均不存在时，服务端从最近一个统计周期的数据里查询。 - start_time存在、end_time不存在时，end_time取当前时间。 - start_time不存在、end_time存在时，请求非法。 - 只能查询最近三个月内的数据，start_time和end_time的跨度不能大于30天。 

        :return: The end_time of this ShowTrafficRequest.
        :rtype: str
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        """Sets the end_time of this ShowTrafficRequest.

        查询结束时间，UTC时间，格式：yyyy-MM-ddTHH:mm:ssZ。  - start_time与end_time均不存在时，服务端从最近一个统计周期的数据里查询。 - start_time存在、end_time不存在时，end_time取当前时间。 - start_time不存在、end_time存在时，请求非法。 - 只能查询最近三个月内的数据，start_time和end_time的跨度不能大于30天。 

        :param end_time: The end_time of this ShowTrafficRequest.
        :type: str
        """
        self._end_time = end_time

    @property
    def step(self):
        """Gets the step of this ShowTrafficRequest.

        统计周期，单位分钟

        :return: The step of this ShowTrafficRequest.
        :rtype: int
        """
        return self._step

    @step.setter
    def step(self, step):
        """Sets the step of this ShowTrafficRequest.

        统计周期，单位分钟

        :param step: The step of this ShowTrafficRequest.
        :type: int
        """
        self._step = step

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
        if not isinstance(other, ShowTrafficRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

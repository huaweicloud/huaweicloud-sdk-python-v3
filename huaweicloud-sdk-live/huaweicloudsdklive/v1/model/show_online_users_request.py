# coding: utf-8

import pprint
import re

import six





class ShowOnlineUsersRequest:


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
        'app_name': 'str',
        'stream_name': 'str',
        'start_time': 'datetime',
        'end_time': 'datetime',
        'step': 'int'
    }

    attribute_map = {
        'domain': 'domain',
        'app_name': 'app_name',
        'stream_name': 'stream_name',
        'start_time': 'start_time',
        'end_time': 'end_time',
        'step': 'step'
    }

    def __init__(self, domain=None, app_name=None, stream_name=None, start_time=None, end_time=None, step=None):
        """ShowOnlineUsersRequest - a model defined in huaweicloud sdk"""
        
        

        self._domain = None
        self._app_name = None
        self._stream_name = None
        self._start_time = None
        self._end_time = None
        self._step = None
        self.discriminator = None

        self.domain = domain
        if app_name is not None:
            self.app_name = app_name
        if stream_name is not None:
            self.stream_name = stream_name
        if start_time is not None:
            self.start_time = start_time
        if end_time is not None:
            self.end_time = end_time
        if step is not None:
            self.step = step

    @property
    def domain(self):
        """Gets the domain of this ShowOnlineUsersRequest.

        直播播放域名

        :return: The domain of this ShowOnlineUsersRequest.
        :rtype: str
        """
        return self._domain

    @domain.setter
    def domain(self, domain):
        """Sets the domain of this ShowOnlineUsersRequest.

        直播播放域名

        :param domain: The domain of this ShowOnlineUsersRequest.
        :type: str
        """
        self._domain = domain

    @property
    def app_name(self):
        """Gets the app_name of this ShowOnlineUsersRequest.

        应用名称。 默认为“live”，若您需要自定义应用名称，请先提交工单申请。 

        :return: The app_name of this ShowOnlineUsersRequest.
        :rtype: str
        """
        return self._app_name

    @app_name.setter
    def app_name(self, app_name):
        """Sets the app_name of this ShowOnlineUsersRequest.

        应用名称。 默认为“live”，若您需要自定义应用名称，请先提交工单申请。 

        :param app_name: The app_name of this ShowOnlineUsersRequest.
        :type: str
        """
        self._app_name = app_name

    @property
    def stream_name(self):
        """Gets the stream_name of this ShowOnlineUsersRequest.

        流名称

        :return: The stream_name of this ShowOnlineUsersRequest.
        :rtype: str
        """
        return self._stream_name

    @stream_name.setter
    def stream_name(self, stream_name):
        """Sets the stream_name of this ShowOnlineUsersRequest.

        流名称

        :param stream_name: The stream_name of this ShowOnlineUsersRequest.
        :type: str
        """
        self._stream_name = stream_name

    @property
    def start_time(self):
        """Gets the start_time of this ShowOnlineUsersRequest.

        查询开始时间，UTC时间，格式：yyyy-mm-ddThh:mm:ssZ。无开始时间表示查询最近统计周期在线人数数据

        :return: The start_time of this ShowOnlineUsersRequest.
        :rtype: datetime
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        """Sets the start_time of this ShowOnlineUsersRequest.

        查询开始时间，UTC时间，格式：yyyy-mm-ddThh:mm:ssZ。无开始时间表示查询最近统计周期在线人数数据

        :param start_time: The start_time of this ShowOnlineUsersRequest.
        :type: datetime
        """
        self._start_time = start_time

    @property
    def end_time(self):
        """Gets the end_time of this ShowOnlineUsersRequest.

        查询结束时间，UTC时间，格式：yyyy-MM-ddTHH:mm:ssZ。  - start_time与end_time均不存在时，服务端从最近一个统计周期的数据里查询。 - start_time存在、end_time不存在时，end_time取当前时间。 - start_time不存在、end_time存在时，请求非法。 - 只能查询最近三个月内的数据，start_time和end_time的跨度不能大于30天。 

        :return: The end_time of this ShowOnlineUsersRequest.
        :rtype: datetime
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        """Sets the end_time of this ShowOnlineUsersRequest.

        查询结束时间，UTC时间，格式：yyyy-MM-ddTHH:mm:ssZ。  - start_time与end_time均不存在时，服务端从最近一个统计周期的数据里查询。 - start_time存在、end_time不存在时，end_time取当前时间。 - start_time不存在、end_time存在时，请求非法。 - 只能查询最近三个月内的数据，start_time和end_time的跨度不能大于30天。 

        :param end_time: The end_time of this ShowOnlineUsersRequest.
        :type: datetime
        """
        self._end_time = end_time

    @property
    def step(self):
        """Gets the step of this ShowOnlineUsersRequest.

        统计周期。 单位：分钟 

        :return: The step of this ShowOnlineUsersRequest.
        :rtype: int
        """
        return self._step

    @step.setter
    def step(self, step):
        """Sets the step of this ShowOnlineUsersRequest.

        统计周期。 单位：分钟 

        :param step: The step of this ShowOnlineUsersRequest.
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
        if not isinstance(other, ShowOnlineUsersRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

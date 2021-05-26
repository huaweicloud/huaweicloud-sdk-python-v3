# coding: utf-8

import pprint
import re

import six





class ListDomainTrafficSummaryRequest:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'play_domains': 'list[str]',
        'app': 'str',
        'stream': 'str',
        'region': 'list[str]',
        'isp': 'list[str]',
        'start_time': 'str',
        'end_time': 'str'
    }

    attribute_map = {
        'play_domains': 'play_domains',
        'app': 'app',
        'stream': 'stream',
        'region': 'region',
        'isp': 'isp',
        'start_time': 'start_time',
        'end_time': 'end_time'
    }

    def __init__(self, play_domains=None, app=None, stream=None, region=None, isp=None, start_time=None, end_time=None):
        """ListDomainTrafficSummaryRequest - a model defined in huaweicloud sdk"""
        
        

        self._play_domains = None
        self._app = None
        self._stream = None
        self._region = None
        self._isp = None
        self._start_time = None
        self._end_time = None
        self.discriminator = None

        self.play_domains = play_domains
        if app is not None:
            self.app = app
        if stream is not None:
            self.stream = stream
        if region is not None:
            self.region = region
        if isp is not None:
            self.isp = isp
        if start_time is not None:
            self.start_time = start_time
        if end_time is not None:
            self.end_time = end_time

    @property
    def play_domains(self):
        """Gets the play_domains of this ListDomainTrafficSummaryRequest.

        播放域名列表，最多支持查询10个域名，多个域名以逗号分隔。 

        :return: The play_domains of this ListDomainTrafficSummaryRequest.
        :rtype: list[str]
        """
        return self._play_domains

    @play_domains.setter
    def play_domains(self, play_domains):
        """Sets the play_domains of this ListDomainTrafficSummaryRequest.

        播放域名列表，最多支持查询10个域名，多个域名以逗号分隔。 

        :param play_domains: The play_domains of this ListDomainTrafficSummaryRequest.
        :type: list[str]
        """
        self._play_domains = play_domains

    @property
    def app(self):
        """Gets the app of this ListDomainTrafficSummaryRequest.

        应用名称。

        :return: The app of this ListDomainTrafficSummaryRequest.
        :rtype: str
        """
        return self._app

    @app.setter
    def app(self, app):
        """Sets the app of this ListDomainTrafficSummaryRequest.

        应用名称。

        :param app: The app of this ListDomainTrafficSummaryRequest.
        :type: str
        """
        self._app = app

    @property
    def stream(self):
        """Gets the stream of this ListDomainTrafficSummaryRequest.

        流名。

        :return: The stream of this ListDomainTrafficSummaryRequest.
        :rtype: str
        """
        return self._stream

    @stream.setter
    def stream(self, stream):
        """Sets the stream of this ListDomainTrafficSummaryRequest.

        流名。

        :param stream: The stream of this ListDomainTrafficSummaryRequest.
        :type: str
        """
        self._stream = stream

    @property
    def region(self):
        """Gets the region of this ListDomainTrafficSummaryRequest.

        区域列表。具体取值请参考[省份名称缩写](live_03_0043.xml)，不填写查询所有区域。 

        :return: The region of this ListDomainTrafficSummaryRequest.
        :rtype: list[str]
        """
        return self._region

    @region.setter
    def region(self, region):
        """Sets the region of this ListDomainTrafficSummaryRequest.

        区域列表。具体取值请参考[省份名称缩写](live_03_0043.xml)，不填写查询所有区域。 

        :param region: The region of this ListDomainTrafficSummaryRequest.
        :type: list[str]
        """
        self._region = region

    @property
    def isp(self):
        """Gets the isp of this ListDomainTrafficSummaryRequest.

        运营商列表。取值如下： - \"CMCC ：移动\" - \"CTCC ： 电信\" - \"CUCC ：联通\" - \"OTHER: 其他\"  不填写查询所有运营商。 

        :return: The isp of this ListDomainTrafficSummaryRequest.
        :rtype: list[str]
        """
        return self._isp

    @isp.setter
    def isp(self, isp):
        """Sets the isp of this ListDomainTrafficSummaryRequest.

        运营商列表。取值如下： - \"CMCC ：移动\" - \"CTCC ： 电信\" - \"CUCC ：联通\" - \"OTHER: 其他\"  不填写查询所有运营商。 

        :param isp: The isp of this ListDomainTrafficSummaryRequest.
        :type: list[str]
        """
        self._isp = isp

    @property
    def start_time(self):
        """Gets the start_time of this ListDomainTrafficSummaryRequest.

        起始时间。日期格式按照ISO8601表示法，并使用UTC时间。  格式为：YYYY-MM-DDThh:mm:ssZ。最大查询跨度31天，最大查询周期90天。  若参数为空，默认查询7天数据。 

        :return: The start_time of this ListDomainTrafficSummaryRequest.
        :rtype: str
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        """Sets the start_time of this ListDomainTrafficSummaryRequest.

        起始时间。日期格式按照ISO8601表示法，并使用UTC时间。  格式为：YYYY-MM-DDThh:mm:ssZ。最大查询跨度31天，最大查询周期90天。  若参数为空，默认查询7天数据。 

        :param start_time: The start_time of this ListDomainTrafficSummaryRequest.
        :type: str
        """
        self._start_time = start_time

    @property
    def end_time(self):
        """Gets the end_time of this ListDomainTrafficSummaryRequest.

        结束时间。日期格式按照ISO8601表示法，并使用UTC时间。格式为：YYYY-MM-DDThh:mm:ssZ。  若参数为空，默认为当前时间。结束时间需大于起始时间。 

        :return: The end_time of this ListDomainTrafficSummaryRequest.
        :rtype: str
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        """Sets the end_time of this ListDomainTrafficSummaryRequest.

        结束时间。日期格式按照ISO8601表示法，并使用UTC时间。格式为：YYYY-MM-DDThh:mm:ssZ。  若参数为空，默认为当前时间。结束时间需大于起始时间。 

        :param end_time: The end_time of this ListDomainTrafficSummaryRequest.
        :type: str
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
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ListDomainTrafficSummaryRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListDomainTrafficDetailRequest:

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
        'protocol': 'str',
        'interval': 'int',
        'start_time': 'str',
        'end_time': 'str',
        'service_type': 'str'
    }

    attribute_map = {
        'play_domains': 'play_domains',
        'app': 'app',
        'stream': 'stream',
        'region': 'region',
        'isp': 'isp',
        'protocol': 'protocol',
        'interval': 'interval',
        'start_time': 'start_time',
        'end_time': 'end_time',
        'service_type': 'service_type'
    }

    def __init__(self, play_domains=None, app=None, stream=None, region=None, isp=None, protocol=None, interval=None, start_time=None, end_time=None, service_type=None):
        """ListDomainTrafficDetailRequest

        The model defined in huaweicloud sdk

        :param play_domains: 播放域名列表，最多支持查询100个域名，多个域名以逗号分隔。  如果不传入域名，则查询租户下所有播放域名的流量数据。 
        :type play_domains: list[str]
        :param app: 应用名称。
        :type app: str
        :param stream: 流名。
        :type stream: str
        :param region: 区域列表。具体取值请参考[省份名称缩写](live_03_0043.xml)，不填写查询所有区域。 
        :type region: list[str]
        :param isp: 运营商列表，取值如下： - CMCC ：移动 - CTCC ： 电信 - CUCC ：联通 - OTHER ：其他  不填写查询所有运营商。 
        :type isp: list[str]
        :param protocol: 请求协议
        :type protocol: str
        :param interval: 查询数据的时间粒度。支持300（默认值）, 3600和86400秒。不传值时，使用默认值300秒。 
        :type interval: int
        :param start_time: 起始时间。日期格式按照ISO8601表示法，并使用UTC时间。  格式为：YYYY-MM-DDThh:mm:ssZ。最大查询跨度31天，最大查询周期一年。  若参数为空，默认查询7天数据。 
        :type start_time: str
        :param end_time: 结束时间。日期格式按照ISO8601表示法，并使用UTC时间。格式为：YYYY-MM-DDThh:mm:ssZ。  若参数为空，默认为当前时间。结束时间需大于起始时间。 
        :type end_time: str
        :param service_type: 服务类型： - Live：直播 - LLL：超低时延直播 - ALL: 默认所有直播 
        :type service_type: str
        """
        
        

        self._play_domains = None
        self._app = None
        self._stream = None
        self._region = None
        self._isp = None
        self._protocol = None
        self._interval = None
        self._start_time = None
        self._end_time = None
        self._service_type = None
        self.discriminator = None

        if play_domains is not None:
            self.play_domains = play_domains
        if app is not None:
            self.app = app
        if stream is not None:
            self.stream = stream
        if region is not None:
            self.region = region
        if isp is not None:
            self.isp = isp
        if protocol is not None:
            self.protocol = protocol
        if interval is not None:
            self.interval = interval
        if start_time is not None:
            self.start_time = start_time
        if end_time is not None:
            self.end_time = end_time
        if service_type is not None:
            self.service_type = service_type

    @property
    def play_domains(self):
        """Gets the play_domains of this ListDomainTrafficDetailRequest.

        播放域名列表，最多支持查询100个域名，多个域名以逗号分隔。  如果不传入域名，则查询租户下所有播放域名的流量数据。 

        :return: The play_domains of this ListDomainTrafficDetailRequest.
        :rtype: list[str]
        """
        return self._play_domains

    @play_domains.setter
    def play_domains(self, play_domains):
        """Sets the play_domains of this ListDomainTrafficDetailRequest.

        播放域名列表，最多支持查询100个域名，多个域名以逗号分隔。  如果不传入域名，则查询租户下所有播放域名的流量数据。 

        :param play_domains: The play_domains of this ListDomainTrafficDetailRequest.
        :type play_domains: list[str]
        """
        self._play_domains = play_domains

    @property
    def app(self):
        """Gets the app of this ListDomainTrafficDetailRequest.

        应用名称。

        :return: The app of this ListDomainTrafficDetailRequest.
        :rtype: str
        """
        return self._app

    @app.setter
    def app(self, app):
        """Sets the app of this ListDomainTrafficDetailRequest.

        应用名称。

        :param app: The app of this ListDomainTrafficDetailRequest.
        :type app: str
        """
        self._app = app

    @property
    def stream(self):
        """Gets the stream of this ListDomainTrafficDetailRequest.

        流名。

        :return: The stream of this ListDomainTrafficDetailRequest.
        :rtype: str
        """
        return self._stream

    @stream.setter
    def stream(self, stream):
        """Sets the stream of this ListDomainTrafficDetailRequest.

        流名。

        :param stream: The stream of this ListDomainTrafficDetailRequest.
        :type stream: str
        """
        self._stream = stream

    @property
    def region(self):
        """Gets the region of this ListDomainTrafficDetailRequest.

        区域列表。具体取值请参考[省份名称缩写](live_03_0043.xml)，不填写查询所有区域。 

        :return: The region of this ListDomainTrafficDetailRequest.
        :rtype: list[str]
        """
        return self._region

    @region.setter
    def region(self, region):
        """Sets the region of this ListDomainTrafficDetailRequest.

        区域列表。具体取值请参考[省份名称缩写](live_03_0043.xml)，不填写查询所有区域。 

        :param region: The region of this ListDomainTrafficDetailRequest.
        :type region: list[str]
        """
        self._region = region

    @property
    def isp(self):
        """Gets the isp of this ListDomainTrafficDetailRequest.

        运营商列表，取值如下： - CMCC ：移动 - CTCC ： 电信 - CUCC ：联通 - OTHER ：其他  不填写查询所有运营商。 

        :return: The isp of this ListDomainTrafficDetailRequest.
        :rtype: list[str]
        """
        return self._isp

    @isp.setter
    def isp(self, isp):
        """Sets the isp of this ListDomainTrafficDetailRequest.

        运营商列表，取值如下： - CMCC ：移动 - CTCC ： 电信 - CUCC ：联通 - OTHER ：其他  不填写查询所有运营商。 

        :param isp: The isp of this ListDomainTrafficDetailRequest.
        :type isp: list[str]
        """
        self._isp = isp

    @property
    def protocol(self):
        """Gets the protocol of this ListDomainTrafficDetailRequest.

        请求协议

        :return: The protocol of this ListDomainTrafficDetailRequest.
        :rtype: str
        """
        return self._protocol

    @protocol.setter
    def protocol(self, protocol):
        """Sets the protocol of this ListDomainTrafficDetailRequest.

        请求协议

        :param protocol: The protocol of this ListDomainTrafficDetailRequest.
        :type protocol: str
        """
        self._protocol = protocol

    @property
    def interval(self):
        """Gets the interval of this ListDomainTrafficDetailRequest.

        查询数据的时间粒度。支持300（默认值）, 3600和86400秒。不传值时，使用默认值300秒。 

        :return: The interval of this ListDomainTrafficDetailRequest.
        :rtype: int
        """
        return self._interval

    @interval.setter
    def interval(self, interval):
        """Sets the interval of this ListDomainTrafficDetailRequest.

        查询数据的时间粒度。支持300（默认值）, 3600和86400秒。不传值时，使用默认值300秒。 

        :param interval: The interval of this ListDomainTrafficDetailRequest.
        :type interval: int
        """
        self._interval = interval

    @property
    def start_time(self):
        """Gets the start_time of this ListDomainTrafficDetailRequest.

        起始时间。日期格式按照ISO8601表示法，并使用UTC时间。  格式为：YYYY-MM-DDThh:mm:ssZ。最大查询跨度31天，最大查询周期一年。  若参数为空，默认查询7天数据。 

        :return: The start_time of this ListDomainTrafficDetailRequest.
        :rtype: str
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        """Sets the start_time of this ListDomainTrafficDetailRequest.

        起始时间。日期格式按照ISO8601表示法，并使用UTC时间。  格式为：YYYY-MM-DDThh:mm:ssZ。最大查询跨度31天，最大查询周期一年。  若参数为空，默认查询7天数据。 

        :param start_time: The start_time of this ListDomainTrafficDetailRequest.
        :type start_time: str
        """
        self._start_time = start_time

    @property
    def end_time(self):
        """Gets the end_time of this ListDomainTrafficDetailRequest.

        结束时间。日期格式按照ISO8601表示法，并使用UTC时间。格式为：YYYY-MM-DDThh:mm:ssZ。  若参数为空，默认为当前时间。结束时间需大于起始时间。 

        :return: The end_time of this ListDomainTrafficDetailRequest.
        :rtype: str
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        """Sets the end_time of this ListDomainTrafficDetailRequest.

        结束时间。日期格式按照ISO8601表示法，并使用UTC时间。格式为：YYYY-MM-DDThh:mm:ssZ。  若参数为空，默认为当前时间。结束时间需大于起始时间。 

        :param end_time: The end_time of this ListDomainTrafficDetailRequest.
        :type end_time: str
        """
        self._end_time = end_time

    @property
    def service_type(self):
        """Gets the service_type of this ListDomainTrafficDetailRequest.

        服务类型： - Live：直播 - LLL：超低时延直播 - ALL: 默认所有直播 

        :return: The service_type of this ListDomainTrafficDetailRequest.
        :rtype: str
        """
        return self._service_type

    @service_type.setter
    def service_type(self, service_type):
        """Sets the service_type of this ListDomainTrafficDetailRequest.

        服务类型： - Live：直播 - LLL：超低时延直播 - ALL: 默认所有直播 

        :param service_type: The service_type of this ListDomainTrafficDetailRequest.
        :type service_type: str
        """
        self._service_type = service_type

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
        if not isinstance(other, ListDomainTrafficDetailRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

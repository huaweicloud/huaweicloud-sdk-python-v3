# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListAreaDetailRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'start_time': 'str',
        'end_time': 'str',
        'play_domains': 'list[str]',
        'app': 'str',
        'stream': 'str',
        'interval': 'int',
        'isp': 'list[str]',
        'area': 'list[str]',
        'metric': 'str',
        'protocol': 'str'
    }

    attribute_map = {
        'start_time': 'start_time',
        'end_time': 'end_time',
        'play_domains': 'play_domains',
        'app': 'app',
        'stream': 'stream',
        'interval': 'interval',
        'isp': 'isp',
        'area': 'area',
        'metric': 'metric',
        'protocol': 'protocol'
    }

    def __init__(self, start_time=None, end_time=None, play_domains=None, app=None, stream=None, interval=None, isp=None, area=None, metric=None, protocol=None):
        """ListAreaDetailRequest

        The model defined in huaweicloud sdk

        :param start_time: 查询起始时间。日期格式按照ISO8601表示法，并使用UTC时间。  格式为：YYYY-MM-DDThh:mm:ssZ。最大查询跨度1天，最大查询周期90天。 
        :type start_time: str
        :param end_time: 查询结束时间。日期格式按照ISO8601表示法，并使用UTC时间。  格式为：YYYY-MM-DDThh:mm:ssZ。最大查询跨度1天，最大查询周期90天。 
        :type end_time: str
        :param play_domains: 需查询的播放域名列表，最多支持查询10个域名。 
        :type play_domains: list[str]
        :param app: 需查询的app。 
        :type app: str
        :param stream: 流名称。
        :type stream: str
        :param interval: 查询数据的时间粒度。支持300（默认值）、3600和86400秒。若参数为空，则默认为300秒。  注意，若metric的值为player（观众数），则interval填入的值不起效果，查询粒度interval默认为60秒。 
        :type interval: int
        :param isp: 运营商列表，取值如下： - CMCC：移动 - CTCC：电信 - CUCC：联通 - OTHER：其他  若参数为空，则查询所有运营商。 
        :type isp: list[str]
        :param area: 需查询的计费大区，取值如下： - CN - AP1 - AP2 - AP3 - EU - MEAA - NA - SA 
        :type area: list[str]
        :param metric: 指标，取值如下： - bandwidth：带宽 - traffic：流量 - player：观众数 
        :type metric: str
        :param protocol: 请求协议，取值如下： - flv - hls 
        :type protocol: str
        """
        
        

        self._start_time = None
        self._end_time = None
        self._play_domains = None
        self._app = None
        self._stream = None
        self._interval = None
        self._isp = None
        self._area = None
        self._metric = None
        self._protocol = None
        self.discriminator = None

        self.start_time = start_time
        self.end_time = end_time
        self.play_domains = play_domains
        if app is not None:
            self.app = app
        if stream is not None:
            self.stream = stream
        if interval is not None:
            self.interval = interval
        if isp is not None:
            self.isp = isp
        self.area = area
        self.metric = metric
        if protocol is not None:
            self.protocol = protocol

    @property
    def start_time(self):
        """Gets the start_time of this ListAreaDetailRequest.

        查询起始时间。日期格式按照ISO8601表示法，并使用UTC时间。  格式为：YYYY-MM-DDThh:mm:ssZ。最大查询跨度1天，最大查询周期90天。 

        :return: The start_time of this ListAreaDetailRequest.
        :rtype: str
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        """Sets the start_time of this ListAreaDetailRequest.

        查询起始时间。日期格式按照ISO8601表示法，并使用UTC时间。  格式为：YYYY-MM-DDThh:mm:ssZ。最大查询跨度1天，最大查询周期90天。 

        :param start_time: The start_time of this ListAreaDetailRequest.
        :type start_time: str
        """
        self._start_time = start_time

    @property
    def end_time(self):
        """Gets the end_time of this ListAreaDetailRequest.

        查询结束时间。日期格式按照ISO8601表示法，并使用UTC时间。  格式为：YYYY-MM-DDThh:mm:ssZ。最大查询跨度1天，最大查询周期90天。 

        :return: The end_time of this ListAreaDetailRequest.
        :rtype: str
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        """Sets the end_time of this ListAreaDetailRequest.

        查询结束时间。日期格式按照ISO8601表示法，并使用UTC时间。  格式为：YYYY-MM-DDThh:mm:ssZ。最大查询跨度1天，最大查询周期90天。 

        :param end_time: The end_time of this ListAreaDetailRequest.
        :type end_time: str
        """
        self._end_time = end_time

    @property
    def play_domains(self):
        """Gets the play_domains of this ListAreaDetailRequest.

        需查询的播放域名列表，最多支持查询10个域名。 

        :return: The play_domains of this ListAreaDetailRequest.
        :rtype: list[str]
        """
        return self._play_domains

    @play_domains.setter
    def play_domains(self, play_domains):
        """Sets the play_domains of this ListAreaDetailRequest.

        需查询的播放域名列表，最多支持查询10个域名。 

        :param play_domains: The play_domains of this ListAreaDetailRequest.
        :type play_domains: list[str]
        """
        self._play_domains = play_domains

    @property
    def app(self):
        """Gets the app of this ListAreaDetailRequest.

        需查询的app。 

        :return: The app of this ListAreaDetailRequest.
        :rtype: str
        """
        return self._app

    @app.setter
    def app(self, app):
        """Sets the app of this ListAreaDetailRequest.

        需查询的app。 

        :param app: The app of this ListAreaDetailRequest.
        :type app: str
        """
        self._app = app

    @property
    def stream(self):
        """Gets the stream of this ListAreaDetailRequest.

        流名称。

        :return: The stream of this ListAreaDetailRequest.
        :rtype: str
        """
        return self._stream

    @stream.setter
    def stream(self, stream):
        """Sets the stream of this ListAreaDetailRequest.

        流名称。

        :param stream: The stream of this ListAreaDetailRequest.
        :type stream: str
        """
        self._stream = stream

    @property
    def interval(self):
        """Gets the interval of this ListAreaDetailRequest.

        查询数据的时间粒度。支持300（默认值）、3600和86400秒。若参数为空，则默认为300秒。  注意，若metric的值为player（观众数），则interval填入的值不起效果，查询粒度interval默认为60秒。 

        :return: The interval of this ListAreaDetailRequest.
        :rtype: int
        """
        return self._interval

    @interval.setter
    def interval(self, interval):
        """Sets the interval of this ListAreaDetailRequest.

        查询数据的时间粒度。支持300（默认值）、3600和86400秒。若参数为空，则默认为300秒。  注意，若metric的值为player（观众数），则interval填入的值不起效果，查询粒度interval默认为60秒。 

        :param interval: The interval of this ListAreaDetailRequest.
        :type interval: int
        """
        self._interval = interval

    @property
    def isp(self):
        """Gets the isp of this ListAreaDetailRequest.

        运营商列表，取值如下： - CMCC：移动 - CTCC：电信 - CUCC：联通 - OTHER：其他  若参数为空，则查询所有运营商。 

        :return: The isp of this ListAreaDetailRequest.
        :rtype: list[str]
        """
        return self._isp

    @isp.setter
    def isp(self, isp):
        """Sets the isp of this ListAreaDetailRequest.

        运营商列表，取值如下： - CMCC：移动 - CTCC：电信 - CUCC：联通 - OTHER：其他  若参数为空，则查询所有运营商。 

        :param isp: The isp of this ListAreaDetailRequest.
        :type isp: list[str]
        """
        self._isp = isp

    @property
    def area(self):
        """Gets the area of this ListAreaDetailRequest.

        需查询的计费大区，取值如下： - CN - AP1 - AP2 - AP3 - EU - MEAA - NA - SA 

        :return: The area of this ListAreaDetailRequest.
        :rtype: list[str]
        """
        return self._area

    @area.setter
    def area(self, area):
        """Sets the area of this ListAreaDetailRequest.

        需查询的计费大区，取值如下： - CN - AP1 - AP2 - AP3 - EU - MEAA - NA - SA 

        :param area: The area of this ListAreaDetailRequest.
        :type area: list[str]
        """
        self._area = area

    @property
    def metric(self):
        """Gets the metric of this ListAreaDetailRequest.

        指标，取值如下： - bandwidth：带宽 - traffic：流量 - player：观众数 

        :return: The metric of this ListAreaDetailRequest.
        :rtype: str
        """
        return self._metric

    @metric.setter
    def metric(self, metric):
        """Sets the metric of this ListAreaDetailRequest.

        指标，取值如下： - bandwidth：带宽 - traffic：流量 - player：观众数 

        :param metric: The metric of this ListAreaDetailRequest.
        :type metric: str
        """
        self._metric = metric

    @property
    def protocol(self):
        """Gets the protocol of this ListAreaDetailRequest.

        请求协议，取值如下： - flv - hls 

        :return: The protocol of this ListAreaDetailRequest.
        :rtype: str
        """
        return self._protocol

    @protocol.setter
    def protocol(self, protocol):
        """Sets the protocol of this ListAreaDetailRequest.

        请求协议，取值如下： - flv - hls 

        :param protocol: The protocol of this ListAreaDetailRequest.
        :type protocol: str
        """
        self._protocol = protocol

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
        if not isinstance(other, ListAreaDetailRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

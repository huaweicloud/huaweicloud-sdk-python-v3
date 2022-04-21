# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowUpBandwidthRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'publish_domains': 'list[str]',
        'app': 'str',
        'stream': 'str',
        'region': 'list[str]',
        'isp': 'list[str]',
        'interval': 'int',
        'start_time': 'str',
        'end_time': 'str'
    }

    attribute_map = {
        'publish_domains': 'publish_domains',
        'app': 'app',
        'stream': 'stream',
        'region': 'region',
        'isp': 'isp',
        'interval': 'interval',
        'start_time': 'start_time',
        'end_time': 'end_time'
    }

    def __init__(self, publish_domains=None, app=None, stream=None, region=None, isp=None, interval=None, start_time=None, end_time=None):
        """ShowUpBandwidthRequest

        The model defined in huaweicloud sdk

        :param publish_domains: 推流域名列表，最多支持查询100个域名，多个域名以逗号分隔，若查询多个域名，则返回的是多个域名合并数据。 
        :type publish_domains: list[str]
        :param app: 应用名称。 
        :type app: str
        :param stream: 流名。 
        :type stream: str
        :param region: 区域列表。具体取值请参考[省份名称缩写](live_03_0043.xml)，不填写查询所有区域。 
        :type region: list[str]
        :param isp: 运营商列表，取值如下： - CMCC ：移动 - CTCC ： 电信 - CUCC ：联通 - OTHER ：其他  不填写查询所有运营商。 
        :type isp: list[str]
        :param interval: 查询数据的时间粒度。支持300（默认值），3600和86400秒。不传值时，使用默认值300秒。 
        :type interval: int
        :param start_time: 起始时间。日期格式按照ISO8601表示法，并使用UTC时间。  格式为：YYYY-MM-DDThh:mm:ssZ。 最大查询跨度31天，最大查询周期1年。  若参数为空，默认查询7天数据。 
        :type start_time: str
        :param end_time: 结束时间。日期格式按照ISO8601表示法，并使用UTC时间。 格式为：YYYY-MM-DDThh:mm:ssZ。  若参数为空，默认为当前时间，最大查询跨度31天，最大查询周期1年。结束时间需大于起始时间。 
        :type end_time: str
        """
        
        

        self._publish_domains = None
        self._app = None
        self._stream = None
        self._region = None
        self._isp = None
        self._interval = None
        self._start_time = None
        self._end_time = None
        self.discriminator = None

        self.publish_domains = publish_domains
        if app is not None:
            self.app = app
        if stream is not None:
            self.stream = stream
        if region is not None:
            self.region = region
        if isp is not None:
            self.isp = isp
        if interval is not None:
            self.interval = interval
        if start_time is not None:
            self.start_time = start_time
        if end_time is not None:
            self.end_time = end_time

    @property
    def publish_domains(self):
        """Gets the publish_domains of this ShowUpBandwidthRequest.

        推流域名列表，最多支持查询100个域名，多个域名以逗号分隔，若查询多个域名，则返回的是多个域名合并数据。 

        :return: The publish_domains of this ShowUpBandwidthRequest.
        :rtype: list[str]
        """
        return self._publish_domains

    @publish_domains.setter
    def publish_domains(self, publish_domains):
        """Sets the publish_domains of this ShowUpBandwidthRequest.

        推流域名列表，最多支持查询100个域名，多个域名以逗号分隔，若查询多个域名，则返回的是多个域名合并数据。 

        :param publish_domains: The publish_domains of this ShowUpBandwidthRequest.
        :type publish_domains: list[str]
        """
        self._publish_domains = publish_domains

    @property
    def app(self):
        """Gets the app of this ShowUpBandwidthRequest.

        应用名称。 

        :return: The app of this ShowUpBandwidthRequest.
        :rtype: str
        """
        return self._app

    @app.setter
    def app(self, app):
        """Sets the app of this ShowUpBandwidthRequest.

        应用名称。 

        :param app: The app of this ShowUpBandwidthRequest.
        :type app: str
        """
        self._app = app

    @property
    def stream(self):
        """Gets the stream of this ShowUpBandwidthRequest.

        流名。 

        :return: The stream of this ShowUpBandwidthRequest.
        :rtype: str
        """
        return self._stream

    @stream.setter
    def stream(self, stream):
        """Sets the stream of this ShowUpBandwidthRequest.

        流名。 

        :param stream: The stream of this ShowUpBandwidthRequest.
        :type stream: str
        """
        self._stream = stream

    @property
    def region(self):
        """Gets the region of this ShowUpBandwidthRequest.

        区域列表。具体取值请参考[省份名称缩写](live_03_0043.xml)，不填写查询所有区域。 

        :return: The region of this ShowUpBandwidthRequest.
        :rtype: list[str]
        """
        return self._region

    @region.setter
    def region(self, region):
        """Sets the region of this ShowUpBandwidthRequest.

        区域列表。具体取值请参考[省份名称缩写](live_03_0043.xml)，不填写查询所有区域。 

        :param region: The region of this ShowUpBandwidthRequest.
        :type region: list[str]
        """
        self._region = region

    @property
    def isp(self):
        """Gets the isp of this ShowUpBandwidthRequest.

        运营商列表，取值如下： - CMCC ：移动 - CTCC ： 电信 - CUCC ：联通 - OTHER ：其他  不填写查询所有运营商。 

        :return: The isp of this ShowUpBandwidthRequest.
        :rtype: list[str]
        """
        return self._isp

    @isp.setter
    def isp(self, isp):
        """Sets the isp of this ShowUpBandwidthRequest.

        运营商列表，取值如下： - CMCC ：移动 - CTCC ： 电信 - CUCC ：联通 - OTHER ：其他  不填写查询所有运营商。 

        :param isp: The isp of this ShowUpBandwidthRequest.
        :type isp: list[str]
        """
        self._isp = isp

    @property
    def interval(self):
        """Gets the interval of this ShowUpBandwidthRequest.

        查询数据的时间粒度。支持300（默认值），3600和86400秒。不传值时，使用默认值300秒。 

        :return: The interval of this ShowUpBandwidthRequest.
        :rtype: int
        """
        return self._interval

    @interval.setter
    def interval(self, interval):
        """Sets the interval of this ShowUpBandwidthRequest.

        查询数据的时间粒度。支持300（默认值），3600和86400秒。不传值时，使用默认值300秒。 

        :param interval: The interval of this ShowUpBandwidthRequest.
        :type interval: int
        """
        self._interval = interval

    @property
    def start_time(self):
        """Gets the start_time of this ShowUpBandwidthRequest.

        起始时间。日期格式按照ISO8601表示法，并使用UTC时间。  格式为：YYYY-MM-DDThh:mm:ssZ。 最大查询跨度31天，最大查询周期1年。  若参数为空，默认查询7天数据。 

        :return: The start_time of this ShowUpBandwidthRequest.
        :rtype: str
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        """Sets the start_time of this ShowUpBandwidthRequest.

        起始时间。日期格式按照ISO8601表示法，并使用UTC时间。  格式为：YYYY-MM-DDThh:mm:ssZ。 最大查询跨度31天，最大查询周期1年。  若参数为空，默认查询7天数据。 

        :param start_time: The start_time of this ShowUpBandwidthRequest.
        :type start_time: str
        """
        self._start_time = start_time

    @property
    def end_time(self):
        """Gets the end_time of this ShowUpBandwidthRequest.

        结束时间。日期格式按照ISO8601表示法，并使用UTC时间。 格式为：YYYY-MM-DDThh:mm:ssZ。  若参数为空，默认为当前时间，最大查询跨度31天，最大查询周期1年。结束时间需大于起始时间。 

        :return: The end_time of this ShowUpBandwidthRequest.
        :rtype: str
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        """Sets the end_time of this ShowUpBandwidthRequest.

        结束时间。日期格式按照ISO8601表示法，并使用UTC时间。 格式为：YYYY-MM-DDThh:mm:ssZ。  若参数为空，默认为当前时间，最大查询跨度31天，最大查询周期1年。结束时间需大于起始时间。 

        :param end_time: The end_time of this ShowUpBandwidthRequest.
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
        if not isinstance(other, ShowUpBandwidthRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

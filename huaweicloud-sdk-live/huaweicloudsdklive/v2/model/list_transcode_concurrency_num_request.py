# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListTranscodeConcurrencyNumRequest:

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
        'interval': 'int',
        'start_time': 'str',
        'end_time': 'str'
    }

    attribute_map = {
        'publish_domains': 'publish_domains',
        'app': 'app',
        'interval': 'interval',
        'start_time': 'start_time',
        'end_time': 'end_time'
    }

    def __init__(self, publish_domains=None, app=None, interval=None, start_time=None, end_time=None):
        r"""ListTranscodeConcurrencyNumRequest

        The model defined in huaweicloud sdk

        :param publish_domains: 推流域名列表，最多支持查询100个域名，多个域名以逗号分隔。  若查询多个域名，则返回的是多个域名合并数据。 
        :type publish_domains: list[str]
        :param app: 应用名称
        :type app: str
        :param interval: 查询数据的时间粒度。支持60, 300（默认值）和3600秒。不传值时，使用默认值300秒。 
        :type interval: int
        :param start_time: 起始时间。日期格式按照ISO8601表示法，并使用UTC时间。  格式为：YYYY-MM-DDThh:mm:ssZ。最大查询跨度1天，最大查询周期90天。  若参数为空，默认查询1天数据。 
        :type start_time: str
        :param end_time: 结束时间。日期格式按照ISO8601表示法，并使用UTC时间。  格式为：YYYY-MM-DDThh:mm:ssZ。最大查询跨度1天，最大查询周期90天。  若参数为空，默认为当前时间。结束时间需大于起始时间。 
        :type end_time: str
        """
        
        

        self._publish_domains = None
        self._app = None
        self._interval = None
        self._start_time = None
        self._end_time = None
        self.discriminator = None

        self.publish_domains = publish_domains
        if app is not None:
            self.app = app
        if interval is not None:
            self.interval = interval
        if start_time is not None:
            self.start_time = start_time
        if end_time is not None:
            self.end_time = end_time

    @property
    def publish_domains(self):
        r"""Gets the publish_domains of this ListTranscodeConcurrencyNumRequest.

        推流域名列表，最多支持查询100个域名，多个域名以逗号分隔。  若查询多个域名，则返回的是多个域名合并数据。 

        :return: The publish_domains of this ListTranscodeConcurrencyNumRequest.
        :rtype: list[str]
        """
        return self._publish_domains

    @publish_domains.setter
    def publish_domains(self, publish_domains):
        r"""Sets the publish_domains of this ListTranscodeConcurrencyNumRequest.

        推流域名列表，最多支持查询100个域名，多个域名以逗号分隔。  若查询多个域名，则返回的是多个域名合并数据。 

        :param publish_domains: The publish_domains of this ListTranscodeConcurrencyNumRequest.
        :type publish_domains: list[str]
        """
        self._publish_domains = publish_domains

    @property
    def app(self):
        r"""Gets the app of this ListTranscodeConcurrencyNumRequest.

        应用名称

        :return: The app of this ListTranscodeConcurrencyNumRequest.
        :rtype: str
        """
        return self._app

    @app.setter
    def app(self, app):
        r"""Sets the app of this ListTranscodeConcurrencyNumRequest.

        应用名称

        :param app: The app of this ListTranscodeConcurrencyNumRequest.
        :type app: str
        """
        self._app = app

    @property
    def interval(self):
        r"""Gets the interval of this ListTranscodeConcurrencyNumRequest.

        查询数据的时间粒度。支持60, 300（默认值）和3600秒。不传值时，使用默认值300秒。 

        :return: The interval of this ListTranscodeConcurrencyNumRequest.
        :rtype: int
        """
        return self._interval

    @interval.setter
    def interval(self, interval):
        r"""Sets the interval of this ListTranscodeConcurrencyNumRequest.

        查询数据的时间粒度。支持60, 300（默认值）和3600秒。不传值时，使用默认值300秒。 

        :param interval: The interval of this ListTranscodeConcurrencyNumRequest.
        :type interval: int
        """
        self._interval = interval

    @property
    def start_time(self):
        r"""Gets the start_time of this ListTranscodeConcurrencyNumRequest.

        起始时间。日期格式按照ISO8601表示法，并使用UTC时间。  格式为：YYYY-MM-DDThh:mm:ssZ。最大查询跨度1天，最大查询周期90天。  若参数为空，默认查询1天数据。 

        :return: The start_time of this ListTranscodeConcurrencyNumRequest.
        :rtype: str
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        r"""Sets the start_time of this ListTranscodeConcurrencyNumRequest.

        起始时间。日期格式按照ISO8601表示法，并使用UTC时间。  格式为：YYYY-MM-DDThh:mm:ssZ。最大查询跨度1天，最大查询周期90天。  若参数为空，默认查询1天数据。 

        :param start_time: The start_time of this ListTranscodeConcurrencyNumRequest.
        :type start_time: str
        """
        self._start_time = start_time

    @property
    def end_time(self):
        r"""Gets the end_time of this ListTranscodeConcurrencyNumRequest.

        结束时间。日期格式按照ISO8601表示法，并使用UTC时间。  格式为：YYYY-MM-DDThh:mm:ssZ。最大查询跨度1天，最大查询周期90天。  若参数为空，默认为当前时间。结束时间需大于起始时间。 

        :return: The end_time of this ListTranscodeConcurrencyNumRequest.
        :rtype: str
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        r"""Sets the end_time of this ListTranscodeConcurrencyNumRequest.

        结束时间。日期格式按照ISO8601表示法，并使用UTC时间。  格式为：YYYY-MM-DDThh:mm:ssZ。最大查询跨度1天，最大查询周期90天。  若参数为空，默认为当前时间。结束时间需大于起始时间。 

        :param end_time: The end_time of this ListTranscodeConcurrencyNumRequest.
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
        if not isinstance(other, ListTranscodeConcurrencyNumRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

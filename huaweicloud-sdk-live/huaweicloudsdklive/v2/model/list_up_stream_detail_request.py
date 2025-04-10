# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListUpStreamDetailRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'publish_domain': 'str',
        'app': 'str',
        'stream': 'str',
        'start_time': 'str',
        'end_time': 'str'
    }

    attribute_map = {
        'publish_domain': 'publish_domain',
        'app': 'app',
        'stream': 'stream',
        'start_time': 'start_time',
        'end_time': 'end_time'
    }

    def __init__(self, publish_domain=None, app=None, stream=None, start_time=None, end_time=None):
        r"""ListUpStreamDetailRequest

        The model defined in huaweicloud sdk

        :param publish_domain: 推流域名。 
        :type publish_domain: str
        :param app: 应用名。 
        :type app: str
        :param stream: 流名。 
        :type stream: str
        :param start_time: 起始时间。日期格式按照ISO8601表示法，并使用UTC时间。  格式为：YYYY-MM-DDThh:mm:ssZ。最大查询跨度1天，最大查询周期1个月。  若参数为空，默认查询最近1小时数据。 
        :type start_time: str
        :param end_time: 结束时间。日期格式按照ISO8601表示法，并使用UTC时间。  格式为：YYYY-MM-DDThh:mm:ssZ。最大查询跨度1天，最大查询周期1个月。  若参数为空，默认为当前时间。结束时间需大于起始时间。 
        :type end_time: str
        """
        
        

        self._publish_domain = None
        self._app = None
        self._stream = None
        self._start_time = None
        self._end_time = None
        self.discriminator = None

        self.publish_domain = publish_domain
        self.app = app
        self.stream = stream
        if start_time is not None:
            self.start_time = start_time
        if end_time is not None:
            self.end_time = end_time

    @property
    def publish_domain(self):
        r"""Gets the publish_domain of this ListUpStreamDetailRequest.

        推流域名。 

        :return: The publish_domain of this ListUpStreamDetailRequest.
        :rtype: str
        """
        return self._publish_domain

    @publish_domain.setter
    def publish_domain(self, publish_domain):
        r"""Sets the publish_domain of this ListUpStreamDetailRequest.

        推流域名。 

        :param publish_domain: The publish_domain of this ListUpStreamDetailRequest.
        :type publish_domain: str
        """
        self._publish_domain = publish_domain

    @property
    def app(self):
        r"""Gets the app of this ListUpStreamDetailRequest.

        应用名。 

        :return: The app of this ListUpStreamDetailRequest.
        :rtype: str
        """
        return self._app

    @app.setter
    def app(self, app):
        r"""Sets the app of this ListUpStreamDetailRequest.

        应用名。 

        :param app: The app of this ListUpStreamDetailRequest.
        :type app: str
        """
        self._app = app

    @property
    def stream(self):
        r"""Gets the stream of this ListUpStreamDetailRequest.

        流名。 

        :return: The stream of this ListUpStreamDetailRequest.
        :rtype: str
        """
        return self._stream

    @stream.setter
    def stream(self, stream):
        r"""Sets the stream of this ListUpStreamDetailRequest.

        流名。 

        :param stream: The stream of this ListUpStreamDetailRequest.
        :type stream: str
        """
        self._stream = stream

    @property
    def start_time(self):
        r"""Gets the start_time of this ListUpStreamDetailRequest.

        起始时间。日期格式按照ISO8601表示法，并使用UTC时间。  格式为：YYYY-MM-DDThh:mm:ssZ。最大查询跨度1天，最大查询周期1个月。  若参数为空，默认查询最近1小时数据。 

        :return: The start_time of this ListUpStreamDetailRequest.
        :rtype: str
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        r"""Sets the start_time of this ListUpStreamDetailRequest.

        起始时间。日期格式按照ISO8601表示法，并使用UTC时间。  格式为：YYYY-MM-DDThh:mm:ssZ。最大查询跨度1天，最大查询周期1个月。  若参数为空，默认查询最近1小时数据。 

        :param start_time: The start_time of this ListUpStreamDetailRequest.
        :type start_time: str
        """
        self._start_time = start_time

    @property
    def end_time(self):
        r"""Gets the end_time of this ListUpStreamDetailRequest.

        结束时间。日期格式按照ISO8601表示法，并使用UTC时间。  格式为：YYYY-MM-DDThh:mm:ssZ。最大查询跨度1天，最大查询周期1个月。  若参数为空，默认为当前时间。结束时间需大于起始时间。 

        :return: The end_time of this ListUpStreamDetailRequest.
        :rtype: str
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        r"""Sets the end_time of this ListUpStreamDetailRequest.

        结束时间。日期格式按照ISO8601表示法，并使用UTC时间。  格式为：YYYY-MM-DDThh:mm:ssZ。最大查询跨度1天，最大查询周期1个月。  若参数为空，默认为当前时间。结束时间需大于起始时间。 

        :param end_time: The end_time of this ListUpStreamDetailRequest.
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
        if not isinstance(other, ListUpStreamDetailRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListHistoryStreamsRequest:

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
        'app': 'str',
        'stream': 'str',
        'start_time': 'str',
        'end_time': 'str',
        'offset': 'int',
        'limit': 'int'
    }

    attribute_map = {
        'domain': 'domain',
        'app': 'app',
        'stream': 'stream',
        'start_time': 'start_time',
        'end_time': 'end_time',
        'offset': 'offset',
        'limit': 'limit'
    }

    def __init__(self, domain=None, app=None, stream=None, start_time=None, end_time=None, offset=None, limit=None):
        r"""ListHistoryStreamsRequest

        The model defined in huaweicloud sdk

        :param domain: 推流域名。 
        :type domain: str
        :param app: 应用名称。
        :type app: str
        :param stream: 流名称。
        :type stream: str
        :param start_time: 起始时间。日期格式按照ISO8601表示法，并使用UTC时间。  格式为：YYYY-MM-DDThh:mm:ssZ。最大查询跨度1天。  若参数为空，默认查询1天数据。 
        :type start_time: str
        :param end_time: 结束时间。日期格式按照ISO8601表示法，并使用UTC时间。 格式为：YYYY-MM-DDThh:mm:ssZ。  若参数为空，默认为当前时间，最大查询跨度1天。结束时间需大于起始时间。 
        :type end_time: str
        :param offset: 分页编号，默认为0
        :type offset: int
        :param limit: 每页记录数。  取值范围：[1,100]  默认值：10。 
        :type limit: int
        """
        
        

        self._domain = None
        self._app = None
        self._stream = None
        self._start_time = None
        self._end_time = None
        self._offset = None
        self._limit = None
        self.discriminator = None

        self.domain = domain
        if app is not None:
            self.app = app
        if stream is not None:
            self.stream = stream
        if start_time is not None:
            self.start_time = start_time
        if end_time is not None:
            self.end_time = end_time
        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit

    @property
    def domain(self):
        r"""Gets the domain of this ListHistoryStreamsRequest.

        推流域名。 

        :return: The domain of this ListHistoryStreamsRequest.
        :rtype: str
        """
        return self._domain

    @domain.setter
    def domain(self, domain):
        r"""Sets the domain of this ListHistoryStreamsRequest.

        推流域名。 

        :param domain: The domain of this ListHistoryStreamsRequest.
        :type domain: str
        """
        self._domain = domain

    @property
    def app(self):
        r"""Gets the app of this ListHistoryStreamsRequest.

        应用名称。

        :return: The app of this ListHistoryStreamsRequest.
        :rtype: str
        """
        return self._app

    @app.setter
    def app(self, app):
        r"""Sets the app of this ListHistoryStreamsRequest.

        应用名称。

        :param app: The app of this ListHistoryStreamsRequest.
        :type app: str
        """
        self._app = app

    @property
    def stream(self):
        r"""Gets the stream of this ListHistoryStreamsRequest.

        流名称。

        :return: The stream of this ListHistoryStreamsRequest.
        :rtype: str
        """
        return self._stream

    @stream.setter
    def stream(self, stream):
        r"""Sets the stream of this ListHistoryStreamsRequest.

        流名称。

        :param stream: The stream of this ListHistoryStreamsRequest.
        :type stream: str
        """
        self._stream = stream

    @property
    def start_time(self):
        r"""Gets the start_time of this ListHistoryStreamsRequest.

        起始时间。日期格式按照ISO8601表示法，并使用UTC时间。  格式为：YYYY-MM-DDThh:mm:ssZ。最大查询跨度1天。  若参数为空，默认查询1天数据。 

        :return: The start_time of this ListHistoryStreamsRequest.
        :rtype: str
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        r"""Sets the start_time of this ListHistoryStreamsRequest.

        起始时间。日期格式按照ISO8601表示法，并使用UTC时间。  格式为：YYYY-MM-DDThh:mm:ssZ。最大查询跨度1天。  若参数为空，默认查询1天数据。 

        :param start_time: The start_time of this ListHistoryStreamsRequest.
        :type start_time: str
        """
        self._start_time = start_time

    @property
    def end_time(self):
        r"""Gets the end_time of this ListHistoryStreamsRequest.

        结束时间。日期格式按照ISO8601表示法，并使用UTC时间。 格式为：YYYY-MM-DDThh:mm:ssZ。  若参数为空，默认为当前时间，最大查询跨度1天。结束时间需大于起始时间。 

        :return: The end_time of this ListHistoryStreamsRequest.
        :rtype: str
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        r"""Sets the end_time of this ListHistoryStreamsRequest.

        结束时间。日期格式按照ISO8601表示法，并使用UTC时间。 格式为：YYYY-MM-DDThh:mm:ssZ。  若参数为空，默认为当前时间，最大查询跨度1天。结束时间需大于起始时间。 

        :param end_time: The end_time of this ListHistoryStreamsRequest.
        :type end_time: str
        """
        self._end_time = end_time

    @property
    def offset(self):
        r"""Gets the offset of this ListHistoryStreamsRequest.

        分页编号，默认为0

        :return: The offset of this ListHistoryStreamsRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListHistoryStreamsRequest.

        分页编号，默认为0

        :param offset: The offset of this ListHistoryStreamsRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        r"""Gets the limit of this ListHistoryStreamsRequest.

        每页记录数。  取值范围：[1,100]  默认值：10。 

        :return: The limit of this ListHistoryStreamsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListHistoryStreamsRequest.

        每页记录数。  取值范围：[1,100]  默认值：10。 

        :param limit: The limit of this ListHistoryStreamsRequest.
        :type limit: int
        """
        self._limit = limit

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
        if not isinstance(other, ListHistoryStreamsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

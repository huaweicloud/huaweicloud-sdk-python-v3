# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ContentInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'body_type': 'int',
        'bodys': 'list[object]',
        'check_end_length': 'object',
        'check_end_str': 'object',
        'check_end_type': 'object',
        'connect_timeout': 'int',
        'connect_type': 'int',
        'headers': 'list[ContentHeader]',
        'http_version': 'str',
        'method': 'str',
        'name': 'str',
        'protocol_type': 'int',
        'return_timeout': 'int',
        'return_timeout_param': 'str',
        'url': 'str',
        'rtmp_url': 'str',
        'flv_url': 'str',
        'bitrate_type': 'int',
        'duration': 'int',
        'retry_delay': 'int',
        'retry_time': 'int'
    }

    attribute_map = {
        'body_type': 'body_type',
        'bodys': 'bodys',
        'check_end_length': 'check_end_length',
        'check_end_str': 'check_end_str',
        'check_end_type': 'check_end_type',
        'connect_timeout': 'connect_timeout',
        'connect_type': 'connect_type',
        'headers': 'headers',
        'http_version': 'http_version',
        'method': 'method',
        'name': 'name',
        'protocol_type': 'protocol_type',
        'return_timeout': 'return_timeout',
        'return_timeout_param': 'return_timeout_param',
        'url': 'url',
        'rtmp_url': 'rtmp_url',
        'flv_url': 'flv_url',
        'bitrate_type': 'bitrate_type',
        'duration': 'duration',
        'retry_delay': 'retry_delay',
        'retry_time': 'retry_time'
    }

    def __init__(self, body_type=None, bodys=None, check_end_length=None, check_end_str=None, check_end_type=None, connect_timeout=None, connect_type=None, headers=None, http_version=None, method=None, name=None, protocol_type=None, return_timeout=None, return_timeout_param=None, url=None, rtmp_url=None, flv_url=None, bitrate_type=None, duration=None, retry_delay=None, retry_time=None):
        """ContentInfo

        The model defined in huaweicloud sdk

        :param body_type: body类型（0：字符串；1：form-data格式；3：x-www-form-urlencoded格式）
        :type body_type: int
        :param bodys: bodys
        :type bodys: list[object]
        :param check_end_length: TCP/UDP协议返回数据长度
        :type check_end_length: object
        :param check_end_str: TCP/UDP协议返回结束符
        :type check_end_str: object
        :param check_end_type: TCP/UDP协议返回结束类型，1：返回数据长度；2：结束符
        :type check_end_type: object
        :param connect_timeout: 超时时间
        :type connect_timeout: int
        :param connect_type: 连接设置，当前版本已未使用
        :type connect_type: int
        :param headers: 请求头
        :type headers: list[:class:`huaweicloudsdkcpts.v1.ContentHeader`]
        :param http_version: HTTP版本
        :type http_version: str
        :param method: HTTP方法
        :type method: str
        :param name: 用例名称
        :type name: str
        :param protocol_type: 协议类型（1：HTTP；2：HTTPS；3：TCP；4：UDP；7：HLS/RTMP；9：WebSocket；10：HTTP-FLV）
        :type protocol_type: int
        :param return_timeout: 响应超时
        :type return_timeout: int
        :param return_timeout_param: 响应超时参数
        :type return_timeout_param: str
        :param url: 请求地址
        :type url: str
        :param rtmp_url: rtmp地址
        :type rtmp_url: str
        :param flv_url: flv地址
        :type flv_url: str
        :param bitrate_type: 分辨率策略
        :type bitrate_type: int
        :param duration: 持续时间
        :type duration: int
        :param retry_delay: HLS重试延迟时间
        :type retry_delay: int
        :param retry_time: HLS重试次数
        :type retry_time: int
        """
        
        

        self._body_type = None
        self._bodys = None
        self._check_end_length = None
        self._check_end_str = None
        self._check_end_type = None
        self._connect_timeout = None
        self._connect_type = None
        self._headers = None
        self._http_version = None
        self._method = None
        self._name = None
        self._protocol_type = None
        self._return_timeout = None
        self._return_timeout_param = None
        self._url = None
        self._rtmp_url = None
        self._flv_url = None
        self._bitrate_type = None
        self._duration = None
        self._retry_delay = None
        self._retry_time = None
        self.discriminator = None

        if body_type is not None:
            self.body_type = body_type
        if bodys is not None:
            self.bodys = bodys
        if check_end_length is not None:
            self.check_end_length = check_end_length
        if check_end_str is not None:
            self.check_end_str = check_end_str
        if check_end_type is not None:
            self.check_end_type = check_end_type
        if connect_timeout is not None:
            self.connect_timeout = connect_timeout
        if connect_type is not None:
            self.connect_type = connect_type
        if headers is not None:
            self.headers = headers
        if http_version is not None:
            self.http_version = http_version
        if method is not None:
            self.method = method
        if name is not None:
            self.name = name
        if protocol_type is not None:
            self.protocol_type = protocol_type
        if return_timeout is not None:
            self.return_timeout = return_timeout
        if return_timeout_param is not None:
            self.return_timeout_param = return_timeout_param
        if url is not None:
            self.url = url
        if rtmp_url is not None:
            self.rtmp_url = rtmp_url
        if flv_url is not None:
            self.flv_url = flv_url
        if bitrate_type is not None:
            self.bitrate_type = bitrate_type
        if duration is not None:
            self.duration = duration
        if retry_delay is not None:
            self.retry_delay = retry_delay
        if retry_time is not None:
            self.retry_time = retry_time

    @property
    def body_type(self):
        """Gets the body_type of this ContentInfo.

        body类型（0：字符串；1：form-data格式；3：x-www-form-urlencoded格式）

        :return: The body_type of this ContentInfo.
        :rtype: int
        """
        return self._body_type

    @body_type.setter
    def body_type(self, body_type):
        """Sets the body_type of this ContentInfo.

        body类型（0：字符串；1：form-data格式；3：x-www-form-urlencoded格式）

        :param body_type: The body_type of this ContentInfo.
        :type body_type: int
        """
        self._body_type = body_type

    @property
    def bodys(self):
        """Gets the bodys of this ContentInfo.

        bodys

        :return: The bodys of this ContentInfo.
        :rtype: list[object]
        """
        return self._bodys

    @bodys.setter
    def bodys(self, bodys):
        """Sets the bodys of this ContentInfo.

        bodys

        :param bodys: The bodys of this ContentInfo.
        :type bodys: list[object]
        """
        self._bodys = bodys

    @property
    def check_end_length(self):
        """Gets the check_end_length of this ContentInfo.

        TCP/UDP协议返回数据长度

        :return: The check_end_length of this ContentInfo.
        :rtype: object
        """
        return self._check_end_length

    @check_end_length.setter
    def check_end_length(self, check_end_length):
        """Sets the check_end_length of this ContentInfo.

        TCP/UDP协议返回数据长度

        :param check_end_length: The check_end_length of this ContentInfo.
        :type check_end_length: object
        """
        self._check_end_length = check_end_length

    @property
    def check_end_str(self):
        """Gets the check_end_str of this ContentInfo.

        TCP/UDP协议返回结束符

        :return: The check_end_str of this ContentInfo.
        :rtype: object
        """
        return self._check_end_str

    @check_end_str.setter
    def check_end_str(self, check_end_str):
        """Sets the check_end_str of this ContentInfo.

        TCP/UDP协议返回结束符

        :param check_end_str: The check_end_str of this ContentInfo.
        :type check_end_str: object
        """
        self._check_end_str = check_end_str

    @property
    def check_end_type(self):
        """Gets the check_end_type of this ContentInfo.

        TCP/UDP协议返回结束类型，1：返回数据长度；2：结束符

        :return: The check_end_type of this ContentInfo.
        :rtype: object
        """
        return self._check_end_type

    @check_end_type.setter
    def check_end_type(self, check_end_type):
        """Sets the check_end_type of this ContentInfo.

        TCP/UDP协议返回结束类型，1：返回数据长度；2：结束符

        :param check_end_type: The check_end_type of this ContentInfo.
        :type check_end_type: object
        """
        self._check_end_type = check_end_type

    @property
    def connect_timeout(self):
        """Gets the connect_timeout of this ContentInfo.

        超时时间

        :return: The connect_timeout of this ContentInfo.
        :rtype: int
        """
        return self._connect_timeout

    @connect_timeout.setter
    def connect_timeout(self, connect_timeout):
        """Sets the connect_timeout of this ContentInfo.

        超时时间

        :param connect_timeout: The connect_timeout of this ContentInfo.
        :type connect_timeout: int
        """
        self._connect_timeout = connect_timeout

    @property
    def connect_type(self):
        """Gets the connect_type of this ContentInfo.

        连接设置，当前版本已未使用

        :return: The connect_type of this ContentInfo.
        :rtype: int
        """
        return self._connect_type

    @connect_type.setter
    def connect_type(self, connect_type):
        """Sets the connect_type of this ContentInfo.

        连接设置，当前版本已未使用

        :param connect_type: The connect_type of this ContentInfo.
        :type connect_type: int
        """
        self._connect_type = connect_type

    @property
    def headers(self):
        """Gets the headers of this ContentInfo.

        请求头

        :return: The headers of this ContentInfo.
        :rtype: list[:class:`huaweicloudsdkcpts.v1.ContentHeader`]
        """
        return self._headers

    @headers.setter
    def headers(self, headers):
        """Sets the headers of this ContentInfo.

        请求头

        :param headers: The headers of this ContentInfo.
        :type headers: list[:class:`huaweicloudsdkcpts.v1.ContentHeader`]
        """
        self._headers = headers

    @property
    def http_version(self):
        """Gets the http_version of this ContentInfo.

        HTTP版本

        :return: The http_version of this ContentInfo.
        :rtype: str
        """
        return self._http_version

    @http_version.setter
    def http_version(self, http_version):
        """Sets the http_version of this ContentInfo.

        HTTP版本

        :param http_version: The http_version of this ContentInfo.
        :type http_version: str
        """
        self._http_version = http_version

    @property
    def method(self):
        """Gets the method of this ContentInfo.

        HTTP方法

        :return: The method of this ContentInfo.
        :rtype: str
        """
        return self._method

    @method.setter
    def method(self, method):
        """Sets the method of this ContentInfo.

        HTTP方法

        :param method: The method of this ContentInfo.
        :type method: str
        """
        self._method = method

    @property
    def name(self):
        """Gets the name of this ContentInfo.

        用例名称

        :return: The name of this ContentInfo.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ContentInfo.

        用例名称

        :param name: The name of this ContentInfo.
        :type name: str
        """
        self._name = name

    @property
    def protocol_type(self):
        """Gets the protocol_type of this ContentInfo.

        协议类型（1：HTTP；2：HTTPS；3：TCP；4：UDP；7：HLS/RTMP；9：WebSocket；10：HTTP-FLV）

        :return: The protocol_type of this ContentInfo.
        :rtype: int
        """
        return self._protocol_type

    @protocol_type.setter
    def protocol_type(self, protocol_type):
        """Sets the protocol_type of this ContentInfo.

        协议类型（1：HTTP；2：HTTPS；3：TCP；4：UDP；7：HLS/RTMP；9：WebSocket；10：HTTP-FLV）

        :param protocol_type: The protocol_type of this ContentInfo.
        :type protocol_type: int
        """
        self._protocol_type = protocol_type

    @property
    def return_timeout(self):
        """Gets the return_timeout of this ContentInfo.

        响应超时

        :return: The return_timeout of this ContentInfo.
        :rtype: int
        """
        return self._return_timeout

    @return_timeout.setter
    def return_timeout(self, return_timeout):
        """Sets the return_timeout of this ContentInfo.

        响应超时

        :param return_timeout: The return_timeout of this ContentInfo.
        :type return_timeout: int
        """
        self._return_timeout = return_timeout

    @property
    def return_timeout_param(self):
        """Gets the return_timeout_param of this ContentInfo.

        响应超时参数

        :return: The return_timeout_param of this ContentInfo.
        :rtype: str
        """
        return self._return_timeout_param

    @return_timeout_param.setter
    def return_timeout_param(self, return_timeout_param):
        """Sets the return_timeout_param of this ContentInfo.

        响应超时参数

        :param return_timeout_param: The return_timeout_param of this ContentInfo.
        :type return_timeout_param: str
        """
        self._return_timeout_param = return_timeout_param

    @property
    def url(self):
        """Gets the url of this ContentInfo.

        请求地址

        :return: The url of this ContentInfo.
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this ContentInfo.

        请求地址

        :param url: The url of this ContentInfo.
        :type url: str
        """
        self._url = url

    @property
    def rtmp_url(self):
        """Gets the rtmp_url of this ContentInfo.

        rtmp地址

        :return: The rtmp_url of this ContentInfo.
        :rtype: str
        """
        return self._rtmp_url

    @rtmp_url.setter
    def rtmp_url(self, rtmp_url):
        """Sets the rtmp_url of this ContentInfo.

        rtmp地址

        :param rtmp_url: The rtmp_url of this ContentInfo.
        :type rtmp_url: str
        """
        self._rtmp_url = rtmp_url

    @property
    def flv_url(self):
        """Gets the flv_url of this ContentInfo.

        flv地址

        :return: The flv_url of this ContentInfo.
        :rtype: str
        """
        return self._flv_url

    @flv_url.setter
    def flv_url(self, flv_url):
        """Sets the flv_url of this ContentInfo.

        flv地址

        :param flv_url: The flv_url of this ContentInfo.
        :type flv_url: str
        """
        self._flv_url = flv_url

    @property
    def bitrate_type(self):
        """Gets the bitrate_type of this ContentInfo.

        分辨率策略

        :return: The bitrate_type of this ContentInfo.
        :rtype: int
        """
        return self._bitrate_type

    @bitrate_type.setter
    def bitrate_type(self, bitrate_type):
        """Sets the bitrate_type of this ContentInfo.

        分辨率策略

        :param bitrate_type: The bitrate_type of this ContentInfo.
        :type bitrate_type: int
        """
        self._bitrate_type = bitrate_type

    @property
    def duration(self):
        """Gets the duration of this ContentInfo.

        持续时间

        :return: The duration of this ContentInfo.
        :rtype: int
        """
        return self._duration

    @duration.setter
    def duration(self, duration):
        """Sets the duration of this ContentInfo.

        持续时间

        :param duration: The duration of this ContentInfo.
        :type duration: int
        """
        self._duration = duration

    @property
    def retry_delay(self):
        """Gets the retry_delay of this ContentInfo.

        HLS重试延迟时间

        :return: The retry_delay of this ContentInfo.
        :rtype: int
        """
        return self._retry_delay

    @retry_delay.setter
    def retry_delay(self, retry_delay):
        """Sets the retry_delay of this ContentInfo.

        HLS重试延迟时间

        :param retry_delay: The retry_delay of this ContentInfo.
        :type retry_delay: int
        """
        self._retry_delay = retry_delay

    @property
    def retry_time(self):
        """Gets the retry_time of this ContentInfo.

        HLS重试次数

        :return: The retry_time of this ContentInfo.
        :rtype: int
        """
        return self._retry_time

    @retry_time.setter
    def retry_time(self, retry_time):
        """Sets the retry_time of this ContentInfo.

        HLS重试次数

        :param retry_time: The retry_time of this ContentInfo.
        :type retry_time: int
        """
        self._retry_time = retry_time

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
        if not isinstance(other, ContentInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

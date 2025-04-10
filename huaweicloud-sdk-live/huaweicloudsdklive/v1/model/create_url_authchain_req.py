# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateUrlAuthchainReq:

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
        'domain_type': 'str',
        'stream': 'str',
        'app': 'str',
        'check_level': 'int',
        'start_time': 'str'
    }

    attribute_map = {
        'domain': 'domain',
        'domain_type': 'domain_type',
        'stream': 'stream',
        'app': 'app',
        'check_level': 'check_level',
        'start_time': 'start_time'
    }

    def __init__(self, domain=None, domain_type=None, stream=None, app=None, check_level=None, start_time=None):
        r"""CreateUrlAuthchainReq

        The model defined in huaweicloud sdk

        :param domain: 播放域名或推流域名
        :type domain: str
        :param domain_type: 域名类型
        :type domain_type: str
        :param stream: 流名称，与推流或播放地址中的StreamName一致。
        :type stream: str
        :param app: 应用名称，与推流或播放地址中的AppName一致。
        :type app: str
        :param check_level: 鉴权方式C必选。 检查级别。LiveID由AppName和StreamName组成,即\&quot;&lt;app_name&gt;/&lt;stream_name&gt;\&quot;。 包含如下取值： - 3：只检查LiveID是否匹配，不检查鉴权URL是否过期。 - 5：检查LiveID是否匹配，Timestamp是否超时。 
        :type check_level: int
        :param start_time: 用户定义的有效访问时间起始点；例如：2006-01-02T15:04:05Z07:00 不传或为空表示当前时间
        :type start_time: str
        """
        
        

        self._domain = None
        self._domain_type = None
        self._stream = None
        self._app = None
        self._check_level = None
        self._start_time = None
        self.discriminator = None

        self.domain = domain
        self.domain_type = domain_type
        self.stream = stream
        self.app = app
        if check_level is not None:
            self.check_level = check_level
        if start_time is not None:
            self.start_time = start_time

    @property
    def domain(self):
        r"""Gets the domain of this CreateUrlAuthchainReq.

        播放域名或推流域名

        :return: The domain of this CreateUrlAuthchainReq.
        :rtype: str
        """
        return self._domain

    @domain.setter
    def domain(self, domain):
        r"""Sets the domain of this CreateUrlAuthchainReq.

        播放域名或推流域名

        :param domain: The domain of this CreateUrlAuthchainReq.
        :type domain: str
        """
        self._domain = domain

    @property
    def domain_type(self):
        r"""Gets the domain_type of this CreateUrlAuthchainReq.

        域名类型

        :return: The domain_type of this CreateUrlAuthchainReq.
        :rtype: str
        """
        return self._domain_type

    @domain_type.setter
    def domain_type(self, domain_type):
        r"""Sets the domain_type of this CreateUrlAuthchainReq.

        域名类型

        :param domain_type: The domain_type of this CreateUrlAuthchainReq.
        :type domain_type: str
        """
        self._domain_type = domain_type

    @property
    def stream(self):
        r"""Gets the stream of this CreateUrlAuthchainReq.

        流名称，与推流或播放地址中的StreamName一致。

        :return: The stream of this CreateUrlAuthchainReq.
        :rtype: str
        """
        return self._stream

    @stream.setter
    def stream(self, stream):
        r"""Sets the stream of this CreateUrlAuthchainReq.

        流名称，与推流或播放地址中的StreamName一致。

        :param stream: The stream of this CreateUrlAuthchainReq.
        :type stream: str
        """
        self._stream = stream

    @property
    def app(self):
        r"""Gets the app of this CreateUrlAuthchainReq.

        应用名称，与推流或播放地址中的AppName一致。

        :return: The app of this CreateUrlAuthchainReq.
        :rtype: str
        """
        return self._app

    @app.setter
    def app(self, app):
        r"""Sets the app of this CreateUrlAuthchainReq.

        应用名称，与推流或播放地址中的AppName一致。

        :param app: The app of this CreateUrlAuthchainReq.
        :type app: str
        """
        self._app = app

    @property
    def check_level(self):
        r"""Gets the check_level of this CreateUrlAuthchainReq.

        鉴权方式C必选。 检查级别。LiveID由AppName和StreamName组成,即\"<app_name>/<stream_name>\"。 包含如下取值： - 3：只检查LiveID是否匹配，不检查鉴权URL是否过期。 - 5：检查LiveID是否匹配，Timestamp是否超时。 

        :return: The check_level of this CreateUrlAuthchainReq.
        :rtype: int
        """
        return self._check_level

    @check_level.setter
    def check_level(self, check_level):
        r"""Sets the check_level of this CreateUrlAuthchainReq.

        鉴权方式C必选。 检查级别。LiveID由AppName和StreamName组成,即\"<app_name>/<stream_name>\"。 包含如下取值： - 3：只检查LiveID是否匹配，不检查鉴权URL是否过期。 - 5：检查LiveID是否匹配，Timestamp是否超时。 

        :param check_level: The check_level of this CreateUrlAuthchainReq.
        :type check_level: int
        """
        self._check_level = check_level

    @property
    def start_time(self):
        r"""Gets the start_time of this CreateUrlAuthchainReq.

        用户定义的有效访问时间起始点；例如：2006-01-02T15:04:05Z07:00 不传或为空表示当前时间

        :return: The start_time of this CreateUrlAuthchainReq.
        :rtype: str
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        r"""Sets the start_time of this CreateUrlAuthchainReq.

        用户定义的有效访问时间起始点；例如：2006-01-02T15:04:05Z07:00 不传或为空表示当前时间

        :param start_time: The start_time of this CreateUrlAuthchainReq.
        :type start_time: str
        """
        self._start_time = start_time

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
        if not isinstance(other, CreateUrlAuthchainReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

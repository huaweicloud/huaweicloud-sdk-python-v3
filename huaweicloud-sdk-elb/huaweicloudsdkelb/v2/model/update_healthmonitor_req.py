# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateHealthmonitorReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'name': 'str',
        'admin_state_up': 'bool',
        'monitor_port': 'int',
        'timeout': 'int',
        'expected_codes': 'str',
        'domain_name': 'str',
        'url_path': 'str',
        'http_method': 'str',
        'delay': 'int',
        'max_retries': 'int',
        'type': 'str'
    }

    attribute_map = {
        'name': 'name',
        'admin_state_up': 'admin_state_up',
        'monitor_port': 'monitor_port',
        'timeout': 'timeout',
        'expected_codes': 'expected_codes',
        'domain_name': 'domain_name',
        'url_path': 'url_path',
        'http_method': 'http_method',
        'delay': 'delay',
        'max_retries': 'max_retries',
        'type': 'type'
    }

    def __init__(self, name=None, admin_state_up=None, monitor_port=None, timeout=None, expected_codes=None, domain_name=None, url_path=None, http_method=None, delay=None, max_retries=None, type=None):
        """UpdateHealthmonitorReq

        The model defined in huaweicloud sdk

        :param name: 健康检查名称。
        :type name: str
        :param admin_state_up: 健康检查的管理状态；该字段虽然支持创建、更新，但实际取值决定于后端云服务器对应的弹性云服务器是否存在。若存在，该值为true，否则，该值为false。
        :type admin_state_up: bool
        :param monitor_port: 健康检查端口号。默认为空，表示使用后端云服务器组的端口。
        :type monitor_port: int
        :param timeout: 健康检查的超时时间。建议该值小于delay的值。
        :type timeout: int
        :param expected_codes: 期望HTTP响应状态码，指定下列值：单值，例如200；列表，例如200，202；区间，例如200-204。仅当type为HTTP时生效。该字段为预留字段，暂未启用。
        :type expected_codes: str
        :param domain_name: 功能说明：健康检查测试member健康状态时，发送的http请求的域名。仅当type为HTTP时生效。使用说明：默认为空，表示使用负载均衡器的vip作为http请求的目的地址。以数字或字母开头，只能包含数字、字母、’-’、’.’。
        :type domain_name: str
        :param url_path: 健康检查请求的请求路径。以\&quot;/\&quot;开头，默认为\&quot;/\&quot;。 支持使用字母、数字和短划线（-）、正斜线（/）、半角句号（.）、百分号（%）、半角问号（?）、井号（#）和and（&amp;）以及扩展字符集_;~!()*[]@$^:&#39;,+  使用说明：当type为HTTP/HTTPS时生效。
        :type url_path: str
        :param http_method: HTTP方法，可以为GET、HEAD、POST、PUT、DELETE、TRACE、OPTIONS、CONNECT、PATCH。仅当type为HTTP时生效。该字段为预留字段，暂未启用。
        :type http_method: str
        :param delay: 健康检查间隔
        :type delay: int
        :param max_retries: 最大重试次数
        :type max_retries: int
        :param type: 健康检查的类型。  取值范围：TCP、UDP_CONNECT、HTTP。
        :type type: str
        """
        
        

        self._name = None
        self._admin_state_up = None
        self._monitor_port = None
        self._timeout = None
        self._expected_codes = None
        self._domain_name = None
        self._url_path = None
        self._http_method = None
        self._delay = None
        self._max_retries = None
        self._type = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if admin_state_up is not None:
            self.admin_state_up = admin_state_up
        if monitor_port is not None:
            self.monitor_port = monitor_port
        if timeout is not None:
            self.timeout = timeout
        if expected_codes is not None:
            self.expected_codes = expected_codes
        if domain_name is not None:
            self.domain_name = domain_name
        if url_path is not None:
            self.url_path = url_path
        if http_method is not None:
            self.http_method = http_method
        if delay is not None:
            self.delay = delay
        if max_retries is not None:
            self.max_retries = max_retries
        if type is not None:
            self.type = type

    @property
    def name(self):
        """Gets the name of this UpdateHealthmonitorReq.

        健康检查名称。

        :return: The name of this UpdateHealthmonitorReq.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this UpdateHealthmonitorReq.

        健康检查名称。

        :param name: The name of this UpdateHealthmonitorReq.
        :type name: str
        """
        self._name = name

    @property
    def admin_state_up(self):
        """Gets the admin_state_up of this UpdateHealthmonitorReq.

        健康检查的管理状态；该字段虽然支持创建、更新，但实际取值决定于后端云服务器对应的弹性云服务器是否存在。若存在，该值为true，否则，该值为false。

        :return: The admin_state_up of this UpdateHealthmonitorReq.
        :rtype: bool
        """
        return self._admin_state_up

    @admin_state_up.setter
    def admin_state_up(self, admin_state_up):
        """Sets the admin_state_up of this UpdateHealthmonitorReq.

        健康检查的管理状态；该字段虽然支持创建、更新，但实际取值决定于后端云服务器对应的弹性云服务器是否存在。若存在，该值为true，否则，该值为false。

        :param admin_state_up: The admin_state_up of this UpdateHealthmonitorReq.
        :type admin_state_up: bool
        """
        self._admin_state_up = admin_state_up

    @property
    def monitor_port(self):
        """Gets the monitor_port of this UpdateHealthmonitorReq.

        健康检查端口号。默认为空，表示使用后端云服务器组的端口。

        :return: The monitor_port of this UpdateHealthmonitorReq.
        :rtype: int
        """
        return self._monitor_port

    @monitor_port.setter
    def monitor_port(self, monitor_port):
        """Sets the monitor_port of this UpdateHealthmonitorReq.

        健康检查端口号。默认为空，表示使用后端云服务器组的端口。

        :param monitor_port: The monitor_port of this UpdateHealthmonitorReq.
        :type monitor_port: int
        """
        self._monitor_port = monitor_port

    @property
    def timeout(self):
        """Gets the timeout of this UpdateHealthmonitorReq.

        健康检查的超时时间。建议该值小于delay的值。

        :return: The timeout of this UpdateHealthmonitorReq.
        :rtype: int
        """
        return self._timeout

    @timeout.setter
    def timeout(self, timeout):
        """Sets the timeout of this UpdateHealthmonitorReq.

        健康检查的超时时间。建议该值小于delay的值。

        :param timeout: The timeout of this UpdateHealthmonitorReq.
        :type timeout: int
        """
        self._timeout = timeout

    @property
    def expected_codes(self):
        """Gets the expected_codes of this UpdateHealthmonitorReq.

        期望HTTP响应状态码，指定下列值：单值，例如200；列表，例如200，202；区间，例如200-204。仅当type为HTTP时生效。该字段为预留字段，暂未启用。

        :return: The expected_codes of this UpdateHealthmonitorReq.
        :rtype: str
        """
        return self._expected_codes

    @expected_codes.setter
    def expected_codes(self, expected_codes):
        """Sets the expected_codes of this UpdateHealthmonitorReq.

        期望HTTP响应状态码，指定下列值：单值，例如200；列表，例如200，202；区间，例如200-204。仅当type为HTTP时生效。该字段为预留字段，暂未启用。

        :param expected_codes: The expected_codes of this UpdateHealthmonitorReq.
        :type expected_codes: str
        """
        self._expected_codes = expected_codes

    @property
    def domain_name(self):
        """Gets the domain_name of this UpdateHealthmonitorReq.

        功能说明：健康检查测试member健康状态时，发送的http请求的域名。仅当type为HTTP时生效。使用说明：默认为空，表示使用负载均衡器的vip作为http请求的目的地址。以数字或字母开头，只能包含数字、字母、’-’、’.’。

        :return: The domain_name of this UpdateHealthmonitorReq.
        :rtype: str
        """
        return self._domain_name

    @domain_name.setter
    def domain_name(self, domain_name):
        """Sets the domain_name of this UpdateHealthmonitorReq.

        功能说明：健康检查测试member健康状态时，发送的http请求的域名。仅当type为HTTP时生效。使用说明：默认为空，表示使用负载均衡器的vip作为http请求的目的地址。以数字或字母开头，只能包含数字、字母、’-’、’.’。

        :param domain_name: The domain_name of this UpdateHealthmonitorReq.
        :type domain_name: str
        """
        self._domain_name = domain_name

    @property
    def url_path(self):
        """Gets the url_path of this UpdateHealthmonitorReq.

        健康检查请求的请求路径。以\"/\"开头，默认为\"/\"。 支持使用字母、数字和短划线（-）、正斜线（/）、半角句号（.）、百分号（%）、半角问号（?）、井号（#）和and（&）以及扩展字符集_;~!()*[]@$^:',+  使用说明：当type为HTTP/HTTPS时生效。

        :return: The url_path of this UpdateHealthmonitorReq.
        :rtype: str
        """
        return self._url_path

    @url_path.setter
    def url_path(self, url_path):
        """Sets the url_path of this UpdateHealthmonitorReq.

        健康检查请求的请求路径。以\"/\"开头，默认为\"/\"。 支持使用字母、数字和短划线（-）、正斜线（/）、半角句号（.）、百分号（%）、半角问号（?）、井号（#）和and（&）以及扩展字符集_;~!()*[]@$^:',+  使用说明：当type为HTTP/HTTPS时生效。

        :param url_path: The url_path of this UpdateHealthmonitorReq.
        :type url_path: str
        """
        self._url_path = url_path

    @property
    def http_method(self):
        """Gets the http_method of this UpdateHealthmonitorReq.

        HTTP方法，可以为GET、HEAD、POST、PUT、DELETE、TRACE、OPTIONS、CONNECT、PATCH。仅当type为HTTP时生效。该字段为预留字段，暂未启用。

        :return: The http_method of this UpdateHealthmonitorReq.
        :rtype: str
        """
        return self._http_method

    @http_method.setter
    def http_method(self, http_method):
        """Sets the http_method of this UpdateHealthmonitorReq.

        HTTP方法，可以为GET、HEAD、POST、PUT、DELETE、TRACE、OPTIONS、CONNECT、PATCH。仅当type为HTTP时生效。该字段为预留字段，暂未启用。

        :param http_method: The http_method of this UpdateHealthmonitorReq.
        :type http_method: str
        """
        self._http_method = http_method

    @property
    def delay(self):
        """Gets the delay of this UpdateHealthmonitorReq.

        健康检查间隔

        :return: The delay of this UpdateHealthmonitorReq.
        :rtype: int
        """
        return self._delay

    @delay.setter
    def delay(self, delay):
        """Sets the delay of this UpdateHealthmonitorReq.

        健康检查间隔

        :param delay: The delay of this UpdateHealthmonitorReq.
        :type delay: int
        """
        self._delay = delay

    @property
    def max_retries(self):
        """Gets the max_retries of this UpdateHealthmonitorReq.

        最大重试次数

        :return: The max_retries of this UpdateHealthmonitorReq.
        :rtype: int
        """
        return self._max_retries

    @max_retries.setter
    def max_retries(self, max_retries):
        """Sets the max_retries of this UpdateHealthmonitorReq.

        最大重试次数

        :param max_retries: The max_retries of this UpdateHealthmonitorReq.
        :type max_retries: int
        """
        self._max_retries = max_retries

    @property
    def type(self):
        """Gets the type of this UpdateHealthmonitorReq.

        健康检查的类型。  取值范围：TCP、UDP_CONNECT、HTTP。

        :return: The type of this UpdateHealthmonitorReq.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this UpdateHealthmonitorReq.

        健康检查的类型。  取值范围：TCP、UDP_CONNECT、HTTP。

        :param type: The type of this UpdateHealthmonitorReq.
        :type type: str
        """
        self._type = type

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
        if not isinstance(other, UpdateHealthmonitorReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

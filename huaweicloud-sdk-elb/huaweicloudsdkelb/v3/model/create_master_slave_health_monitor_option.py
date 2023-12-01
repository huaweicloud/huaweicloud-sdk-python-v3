# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateMasterSlaveHealthMonitorOption:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'delay': 'int',
        'domain_name': 'str',
        'expected_codes': 'str',
        'http_method': 'str',
        'max_retries': 'int',
        'max_retries_down': 'int',
        'monitor_port': 'int',
        'name': 'str',
        'timeout': 'int',
        'type': 'str',
        'url_path': 'str'
    }

    attribute_map = {
        'delay': 'delay',
        'domain_name': 'domain_name',
        'expected_codes': 'expected_codes',
        'http_method': 'http_method',
        'max_retries': 'max_retries',
        'max_retries_down': 'max_retries_down',
        'monitor_port': 'monitor_port',
        'name': 'name',
        'timeout': 'timeout',
        'type': 'type',
        'url_path': 'url_path'
    }

    def __init__(self, delay=None, domain_name=None, expected_codes=None, http_method=None, max_retries=None, max_retries_down=None, monitor_port=None, name=None, timeout=None, type=None, url_path=None):
        """CreateMasterSlaveHealthMonitorOption

        The model defined in huaweicloud sdk

        :param delay: 健康检查间隔。取值：1-50s。
        :type delay: int
        :param domain_name: 发送健康检查请求的域名。  取值：以数字或字母开头，只能包含数字、字母、’-’、’.’。 默认为空，表示使用负载均衡器的vip作为http请求的目的地址。  使用说明：当type为HTTP/HTTPS时生效。
        :type domain_name: str
        :param expected_codes: 期望响应状态码。  取值： - 单值：单个返回码，例如200。 - 列表：多个特定返回码，例如200，202。 - 区间：一个返回码区间，例如200-204。  默认值：200。  仅支持HTTP/HTTPS设置该字段，其他协议设置不会生效。
        :type expected_codes: str
        :param http_method: HTTP请求方法。  取值：GET、HEAD、POST、PUT、DELETE、TRACE、OPTIONS、CONNECT、PATCH，默认GET。  使用说明：当type为HTTP/HTTPS时生效。  不支持该字段，请勿使用。
        :type http_method: str
        :param max_retries: 健康检查连续成功多少次后，将后端服务器的健康检查状态由OFFLINE判定为ONLINE。取值范围：1-10。
        :type max_retries: int
        :param max_retries_down: 健康检查连续失败多少次后，将后端服务器的健康检查状态由ONLINE判定为OFFLINE。取值范围：1-10，默认3。
        :type max_retries_down: int
        :param monitor_port: 健康检查端口号。取值：1-65535，默认为空，表示使用后端云服务器端口号。
        :type monitor_port: int
        :param name: 健康检查名称。
        :type name: str
        :param timeout: 一次健康检查请求的超时时间。  建议该值小于delay的值。
        :type timeout: int
        :param type: 健康检查请求协议。  取值：TCP、UDP_CONNECT、HTTP、HTTPS。  使用说明： - 若pool的protocol为QUIC，则type只能是UDP_CONNECT。 - 若pool的protocol为UDP，则type只能UDP_CONNECT。 - 若pool的protocol为TCP，则type可以是TCP、HTTP、HTTPS。 - 若pool的protocol为HTTP，则type可以是TCP、HTTP、HTTPS。 - 若pool的protocol为HTTPS，则type可以是TCP、HTTP、HTTPS。  [不支持QUIC。](tag:tm,hws_eu,g42,hk_g42,hcso_dt)  [荷兰region不支持QUIC。](tag:dt,dt_test)
        :type type: str
        :param url_path: 健康检查请求的请求路径。以\&quot;/\&quot;开头，默认为\&quot;/\&quot;。  支持使用字母、数字和短划线（-）、正斜线（/）、半角句号（.）、百分号（%）、半角问号（?）、井号（#）和and（&amp;）以及扩展字符集_;~!()*[]@$^:&#39;,+   使用说明：当type为HTTP/HTTPS时生效。
        :type url_path: str
        """
        
        

        self._delay = None
        self._domain_name = None
        self._expected_codes = None
        self._http_method = None
        self._max_retries = None
        self._max_retries_down = None
        self._monitor_port = None
        self._name = None
        self._timeout = None
        self._type = None
        self._url_path = None
        self.discriminator = None

        self.delay = delay
        if domain_name is not None:
            self.domain_name = domain_name
        if expected_codes is not None:
            self.expected_codes = expected_codes
        if http_method is not None:
            self.http_method = http_method
        self.max_retries = max_retries
        if max_retries_down is not None:
            self.max_retries_down = max_retries_down
        if monitor_port is not None:
            self.monitor_port = monitor_port
        if name is not None:
            self.name = name
        self.timeout = timeout
        self.type = type
        if url_path is not None:
            self.url_path = url_path

    @property
    def delay(self):
        """Gets the delay of this CreateMasterSlaveHealthMonitorOption.

        健康检查间隔。取值：1-50s。

        :return: The delay of this CreateMasterSlaveHealthMonitorOption.
        :rtype: int
        """
        return self._delay

    @delay.setter
    def delay(self, delay):
        """Sets the delay of this CreateMasterSlaveHealthMonitorOption.

        健康检查间隔。取值：1-50s。

        :param delay: The delay of this CreateMasterSlaveHealthMonitorOption.
        :type delay: int
        """
        self._delay = delay

    @property
    def domain_name(self):
        """Gets the domain_name of this CreateMasterSlaveHealthMonitorOption.

        发送健康检查请求的域名。  取值：以数字或字母开头，只能包含数字、字母、’-’、’.’。 默认为空，表示使用负载均衡器的vip作为http请求的目的地址。  使用说明：当type为HTTP/HTTPS时生效。

        :return: The domain_name of this CreateMasterSlaveHealthMonitorOption.
        :rtype: str
        """
        return self._domain_name

    @domain_name.setter
    def domain_name(self, domain_name):
        """Sets the domain_name of this CreateMasterSlaveHealthMonitorOption.

        发送健康检查请求的域名。  取值：以数字或字母开头，只能包含数字、字母、’-’、’.’。 默认为空，表示使用负载均衡器的vip作为http请求的目的地址。  使用说明：当type为HTTP/HTTPS时生效。

        :param domain_name: The domain_name of this CreateMasterSlaveHealthMonitorOption.
        :type domain_name: str
        """
        self._domain_name = domain_name

    @property
    def expected_codes(self):
        """Gets the expected_codes of this CreateMasterSlaveHealthMonitorOption.

        期望响应状态码。  取值： - 单值：单个返回码，例如200。 - 列表：多个特定返回码，例如200，202。 - 区间：一个返回码区间，例如200-204。  默认值：200。  仅支持HTTP/HTTPS设置该字段，其他协议设置不会生效。

        :return: The expected_codes of this CreateMasterSlaveHealthMonitorOption.
        :rtype: str
        """
        return self._expected_codes

    @expected_codes.setter
    def expected_codes(self, expected_codes):
        """Sets the expected_codes of this CreateMasterSlaveHealthMonitorOption.

        期望响应状态码。  取值： - 单值：单个返回码，例如200。 - 列表：多个特定返回码，例如200，202。 - 区间：一个返回码区间，例如200-204。  默认值：200。  仅支持HTTP/HTTPS设置该字段，其他协议设置不会生效。

        :param expected_codes: The expected_codes of this CreateMasterSlaveHealthMonitorOption.
        :type expected_codes: str
        """
        self._expected_codes = expected_codes

    @property
    def http_method(self):
        """Gets the http_method of this CreateMasterSlaveHealthMonitorOption.

        HTTP请求方法。  取值：GET、HEAD、POST、PUT、DELETE、TRACE、OPTIONS、CONNECT、PATCH，默认GET。  使用说明：当type为HTTP/HTTPS时生效。  不支持该字段，请勿使用。

        :return: The http_method of this CreateMasterSlaveHealthMonitorOption.
        :rtype: str
        """
        return self._http_method

    @http_method.setter
    def http_method(self, http_method):
        """Sets the http_method of this CreateMasterSlaveHealthMonitorOption.

        HTTP请求方法。  取值：GET、HEAD、POST、PUT、DELETE、TRACE、OPTIONS、CONNECT、PATCH，默认GET。  使用说明：当type为HTTP/HTTPS时生效。  不支持该字段，请勿使用。

        :param http_method: The http_method of this CreateMasterSlaveHealthMonitorOption.
        :type http_method: str
        """
        self._http_method = http_method

    @property
    def max_retries(self):
        """Gets the max_retries of this CreateMasterSlaveHealthMonitorOption.

        健康检查连续成功多少次后，将后端服务器的健康检查状态由OFFLINE判定为ONLINE。取值范围：1-10。

        :return: The max_retries of this CreateMasterSlaveHealthMonitorOption.
        :rtype: int
        """
        return self._max_retries

    @max_retries.setter
    def max_retries(self, max_retries):
        """Sets the max_retries of this CreateMasterSlaveHealthMonitorOption.

        健康检查连续成功多少次后，将后端服务器的健康检查状态由OFFLINE判定为ONLINE。取值范围：1-10。

        :param max_retries: The max_retries of this CreateMasterSlaveHealthMonitorOption.
        :type max_retries: int
        """
        self._max_retries = max_retries

    @property
    def max_retries_down(self):
        """Gets the max_retries_down of this CreateMasterSlaveHealthMonitorOption.

        健康检查连续失败多少次后，将后端服务器的健康检查状态由ONLINE判定为OFFLINE。取值范围：1-10，默认3。

        :return: The max_retries_down of this CreateMasterSlaveHealthMonitorOption.
        :rtype: int
        """
        return self._max_retries_down

    @max_retries_down.setter
    def max_retries_down(self, max_retries_down):
        """Sets the max_retries_down of this CreateMasterSlaveHealthMonitorOption.

        健康检查连续失败多少次后，将后端服务器的健康检查状态由ONLINE判定为OFFLINE。取值范围：1-10，默认3。

        :param max_retries_down: The max_retries_down of this CreateMasterSlaveHealthMonitorOption.
        :type max_retries_down: int
        """
        self._max_retries_down = max_retries_down

    @property
    def monitor_port(self):
        """Gets the monitor_port of this CreateMasterSlaveHealthMonitorOption.

        健康检查端口号。取值：1-65535，默认为空，表示使用后端云服务器端口号。

        :return: The monitor_port of this CreateMasterSlaveHealthMonitorOption.
        :rtype: int
        """
        return self._monitor_port

    @monitor_port.setter
    def monitor_port(self, monitor_port):
        """Sets the monitor_port of this CreateMasterSlaveHealthMonitorOption.

        健康检查端口号。取值：1-65535，默认为空，表示使用后端云服务器端口号。

        :param monitor_port: The monitor_port of this CreateMasterSlaveHealthMonitorOption.
        :type monitor_port: int
        """
        self._monitor_port = monitor_port

    @property
    def name(self):
        """Gets the name of this CreateMasterSlaveHealthMonitorOption.

        健康检查名称。

        :return: The name of this CreateMasterSlaveHealthMonitorOption.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CreateMasterSlaveHealthMonitorOption.

        健康检查名称。

        :param name: The name of this CreateMasterSlaveHealthMonitorOption.
        :type name: str
        """
        self._name = name

    @property
    def timeout(self):
        """Gets the timeout of this CreateMasterSlaveHealthMonitorOption.

        一次健康检查请求的超时时间。  建议该值小于delay的值。

        :return: The timeout of this CreateMasterSlaveHealthMonitorOption.
        :rtype: int
        """
        return self._timeout

    @timeout.setter
    def timeout(self, timeout):
        """Sets the timeout of this CreateMasterSlaveHealthMonitorOption.

        一次健康检查请求的超时时间。  建议该值小于delay的值。

        :param timeout: The timeout of this CreateMasterSlaveHealthMonitorOption.
        :type timeout: int
        """
        self._timeout = timeout

    @property
    def type(self):
        """Gets the type of this CreateMasterSlaveHealthMonitorOption.

        健康检查请求协议。  取值：TCP、UDP_CONNECT、HTTP、HTTPS。  使用说明： - 若pool的protocol为QUIC，则type只能是UDP_CONNECT。 - 若pool的protocol为UDP，则type只能UDP_CONNECT。 - 若pool的protocol为TCP，则type可以是TCP、HTTP、HTTPS。 - 若pool的protocol为HTTP，则type可以是TCP、HTTP、HTTPS。 - 若pool的protocol为HTTPS，则type可以是TCP、HTTP、HTTPS。  [不支持QUIC。](tag:tm,hws_eu,g42,hk_g42,hcso_dt)  [荷兰region不支持QUIC。](tag:dt,dt_test)

        :return: The type of this CreateMasterSlaveHealthMonitorOption.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this CreateMasterSlaveHealthMonitorOption.

        健康检查请求协议。  取值：TCP、UDP_CONNECT、HTTP、HTTPS。  使用说明： - 若pool的protocol为QUIC，则type只能是UDP_CONNECT。 - 若pool的protocol为UDP，则type只能UDP_CONNECT。 - 若pool的protocol为TCP，则type可以是TCP、HTTP、HTTPS。 - 若pool的protocol为HTTP，则type可以是TCP、HTTP、HTTPS。 - 若pool的protocol为HTTPS，则type可以是TCP、HTTP、HTTPS。  [不支持QUIC。](tag:tm,hws_eu,g42,hk_g42,hcso_dt)  [荷兰region不支持QUIC。](tag:dt,dt_test)

        :param type: The type of this CreateMasterSlaveHealthMonitorOption.
        :type type: str
        """
        self._type = type

    @property
    def url_path(self):
        """Gets the url_path of this CreateMasterSlaveHealthMonitorOption.

        健康检查请求的请求路径。以\"/\"开头，默认为\"/\"。  支持使用字母、数字和短划线（-）、正斜线（/）、半角句号（.）、百分号（%）、半角问号（?）、井号（#）和and（&）以及扩展字符集_;~!()*[]@$^:',+   使用说明：当type为HTTP/HTTPS时生效。

        :return: The url_path of this CreateMasterSlaveHealthMonitorOption.
        :rtype: str
        """
        return self._url_path

    @url_path.setter
    def url_path(self, url_path):
        """Sets the url_path of this CreateMasterSlaveHealthMonitorOption.

        健康检查请求的请求路径。以\"/\"开头，默认为\"/\"。  支持使用字母、数字和短划线（-）、正斜线（/）、半角句号（.）、百分号（%）、半角问号（?）、井号（#）和and（&）以及扩展字符集_;~!()*[]@$^:',+   使用说明：当type为HTTP/HTTPS时生效。

        :param url_path: The url_path of this CreateMasterSlaveHealthMonitorOption.
        :type url_path: str
        """
        self._url_path = url_path

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
        if not isinstance(other, CreateMasterSlaveHealthMonitorOption):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

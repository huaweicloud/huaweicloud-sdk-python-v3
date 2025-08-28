# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class MasterSlaveHealthMonitor:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'admin_state_up': 'bool',
        'delay': 'int',
        'domain_name': 'str',
        'expected_codes': 'str',
        'http_method': 'str',
        'id': 'str',
        'max_retries': 'int',
        'max_retries_down': 'int',
        'monitor_port': 'int',
        'name': 'str',
        'timeout': 'int',
        'type': 'str',
        'url_path': 'str'
    }

    attribute_map = {
        'admin_state_up': 'admin_state_up',
        'delay': 'delay',
        'domain_name': 'domain_name',
        'expected_codes': 'expected_codes',
        'http_method': 'http_method',
        'id': 'id',
        'max_retries': 'max_retries',
        'max_retries_down': 'max_retries_down',
        'monitor_port': 'monitor_port',
        'name': 'name',
        'timeout': 'timeout',
        'type': 'type',
        'url_path': 'url_path'
    }

    def __init__(self, admin_state_up=None, delay=None, domain_name=None, expected_codes=None, http_method=None, id=None, max_retries=None, max_retries_down=None, monitor_port=None, name=None, timeout=None, type=None, url_path=None):
        r"""MasterSlaveHealthMonitor

        The model defined in huaweicloud sdk

        :param admin_state_up: **参数解释**：健康检查的管理状态。  **取值范围**： - true：表示开启健康检查。 - false表示关闭健康检查。
        :type admin_state_up: bool
        :param delay: **参数解释**：健康检查间隔。  **取值范围**：1-50，单位：秒。
        :type delay: int
        :param domain_name: **参数解释**：发送健康检查请求的域名。  **取值范围**：以数字或字母开头，只能包含数字、字母、’-’、’.’。
        :type domain_name: str
        :param expected_codes: **参数解释**：期望响应状态码。  **取值范围**： - 单值：单个返回码，例如200。 - 列表：多个特定返回码，例如200，202。 - 区间：一个返回码区间，例如200-204。
        :type expected_codes: str
        :param http_method: **约束限制**：HTTP请求方法。  **取值范围**：GET、HEAD、POST
        :type http_method: str
        :param id: **参数解释**：健康检查ID  **取值范围**：不涉及
        :type id: str
        :param max_retries: **参数解释**：健康检查连续成功多少次后，将后端服务器的健康检查状态由OFFLINE判定为ONLINE。  **取值范围**：1-10
        :type max_retries: int
        :param max_retries_down: **参数解释**：健康检查连续失败多少次后，将后端服务器的健康检查状态由ONLINE判定为OFFLINE。  **取值范围**：1-10
        :type max_retries_down: int
        :param monitor_port: **参数解释**：健康检查端口号。  **取值范围**：1-65535
        :type monitor_port: int
        :param name: **参数解释**：健康检查名称。  **取值范围**：不涉及
        :type name: str
        :param timeout: **参数解释**：一次健康检查请求的超时时间。  **取值范围**：不涉及
        :type timeout: int
        :param type: **参数解释**：健康检查请求协议。  **取值范围**：TCP、UDP_CONNECT、HTTP、HTTPS。
        :type type: str
        :param url_path: **参数解释**：健康检查请求的请求路径。以\&quot;/\&quot;开头，默认为\&quot;/\&quot;。  **取值范围**：支持使用字母、数字和短划线（-）、正斜线（/）、半角句号（.）、百分号（%）、半角问号（?）、井号（#）和and（&amp;）以及扩展字符集_;~!()*[]@$^:&#39;,+
        :type url_path: str
        """
        
        

        self._admin_state_up = None
        self._delay = None
        self._domain_name = None
        self._expected_codes = None
        self._http_method = None
        self._id = None
        self._max_retries = None
        self._max_retries_down = None
        self._monitor_port = None
        self._name = None
        self._timeout = None
        self._type = None
        self._url_path = None
        self.discriminator = None

        self.admin_state_up = admin_state_up
        self.delay = delay
        self.domain_name = domain_name
        self.expected_codes = expected_codes
        self.http_method = http_method
        self.id = id
        self.max_retries = max_retries
        self.max_retries_down = max_retries_down
        self.monitor_port = monitor_port
        self.name = name
        self.timeout = timeout
        self.type = type
        self.url_path = url_path

    @property
    def admin_state_up(self):
        r"""Gets the admin_state_up of this MasterSlaveHealthMonitor.

        **参数解释**：健康检查的管理状态。  **取值范围**： - true：表示开启健康检查。 - false表示关闭健康检查。

        :return: The admin_state_up of this MasterSlaveHealthMonitor.
        :rtype: bool
        """
        return self._admin_state_up

    @admin_state_up.setter
    def admin_state_up(self, admin_state_up):
        r"""Sets the admin_state_up of this MasterSlaveHealthMonitor.

        **参数解释**：健康检查的管理状态。  **取值范围**： - true：表示开启健康检查。 - false表示关闭健康检查。

        :param admin_state_up: The admin_state_up of this MasterSlaveHealthMonitor.
        :type admin_state_up: bool
        """
        self._admin_state_up = admin_state_up

    @property
    def delay(self):
        r"""Gets the delay of this MasterSlaveHealthMonitor.

        **参数解释**：健康检查间隔。  **取值范围**：1-50，单位：秒。

        :return: The delay of this MasterSlaveHealthMonitor.
        :rtype: int
        """
        return self._delay

    @delay.setter
    def delay(self, delay):
        r"""Sets the delay of this MasterSlaveHealthMonitor.

        **参数解释**：健康检查间隔。  **取值范围**：1-50，单位：秒。

        :param delay: The delay of this MasterSlaveHealthMonitor.
        :type delay: int
        """
        self._delay = delay

    @property
    def domain_name(self):
        r"""Gets the domain_name of this MasterSlaveHealthMonitor.

        **参数解释**：发送健康检查请求的域名。  **取值范围**：以数字或字母开头，只能包含数字、字母、’-’、’.’。

        :return: The domain_name of this MasterSlaveHealthMonitor.
        :rtype: str
        """
        return self._domain_name

    @domain_name.setter
    def domain_name(self, domain_name):
        r"""Sets the domain_name of this MasterSlaveHealthMonitor.

        **参数解释**：发送健康检查请求的域名。  **取值范围**：以数字或字母开头，只能包含数字、字母、’-’、’.’。

        :param domain_name: The domain_name of this MasterSlaveHealthMonitor.
        :type domain_name: str
        """
        self._domain_name = domain_name

    @property
    def expected_codes(self):
        r"""Gets the expected_codes of this MasterSlaveHealthMonitor.

        **参数解释**：期望响应状态码。  **取值范围**： - 单值：单个返回码，例如200。 - 列表：多个特定返回码，例如200，202。 - 区间：一个返回码区间，例如200-204。

        :return: The expected_codes of this MasterSlaveHealthMonitor.
        :rtype: str
        """
        return self._expected_codes

    @expected_codes.setter
    def expected_codes(self, expected_codes):
        r"""Sets the expected_codes of this MasterSlaveHealthMonitor.

        **参数解释**：期望响应状态码。  **取值范围**： - 单值：单个返回码，例如200。 - 列表：多个特定返回码，例如200，202。 - 区间：一个返回码区间，例如200-204。

        :param expected_codes: The expected_codes of this MasterSlaveHealthMonitor.
        :type expected_codes: str
        """
        self._expected_codes = expected_codes

    @property
    def http_method(self):
        r"""Gets the http_method of this MasterSlaveHealthMonitor.

        **约束限制**：HTTP请求方法。  **取值范围**：GET、HEAD、POST

        :return: The http_method of this MasterSlaveHealthMonitor.
        :rtype: str
        """
        return self._http_method

    @http_method.setter
    def http_method(self, http_method):
        r"""Sets the http_method of this MasterSlaveHealthMonitor.

        **约束限制**：HTTP请求方法。  **取值范围**：GET、HEAD、POST

        :param http_method: The http_method of this MasterSlaveHealthMonitor.
        :type http_method: str
        """
        self._http_method = http_method

    @property
    def id(self):
        r"""Gets the id of this MasterSlaveHealthMonitor.

        **参数解释**：健康检查ID  **取值范围**：不涉及

        :return: The id of this MasterSlaveHealthMonitor.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this MasterSlaveHealthMonitor.

        **参数解释**：健康检查ID  **取值范围**：不涉及

        :param id: The id of this MasterSlaveHealthMonitor.
        :type id: str
        """
        self._id = id

    @property
    def max_retries(self):
        r"""Gets the max_retries of this MasterSlaveHealthMonitor.

        **参数解释**：健康检查连续成功多少次后，将后端服务器的健康检查状态由OFFLINE判定为ONLINE。  **取值范围**：1-10

        :return: The max_retries of this MasterSlaveHealthMonitor.
        :rtype: int
        """
        return self._max_retries

    @max_retries.setter
    def max_retries(self, max_retries):
        r"""Sets the max_retries of this MasterSlaveHealthMonitor.

        **参数解释**：健康检查连续成功多少次后，将后端服务器的健康检查状态由OFFLINE判定为ONLINE。  **取值范围**：1-10

        :param max_retries: The max_retries of this MasterSlaveHealthMonitor.
        :type max_retries: int
        """
        self._max_retries = max_retries

    @property
    def max_retries_down(self):
        r"""Gets the max_retries_down of this MasterSlaveHealthMonitor.

        **参数解释**：健康检查连续失败多少次后，将后端服务器的健康检查状态由ONLINE判定为OFFLINE。  **取值范围**：1-10

        :return: The max_retries_down of this MasterSlaveHealthMonitor.
        :rtype: int
        """
        return self._max_retries_down

    @max_retries_down.setter
    def max_retries_down(self, max_retries_down):
        r"""Sets the max_retries_down of this MasterSlaveHealthMonitor.

        **参数解释**：健康检查连续失败多少次后，将后端服务器的健康检查状态由ONLINE判定为OFFLINE。  **取值范围**：1-10

        :param max_retries_down: The max_retries_down of this MasterSlaveHealthMonitor.
        :type max_retries_down: int
        """
        self._max_retries_down = max_retries_down

    @property
    def monitor_port(self):
        r"""Gets the monitor_port of this MasterSlaveHealthMonitor.

        **参数解释**：健康检查端口号。  **取值范围**：1-65535

        :return: The monitor_port of this MasterSlaveHealthMonitor.
        :rtype: int
        """
        return self._monitor_port

    @monitor_port.setter
    def monitor_port(self, monitor_port):
        r"""Sets the monitor_port of this MasterSlaveHealthMonitor.

        **参数解释**：健康检查端口号。  **取值范围**：1-65535

        :param monitor_port: The monitor_port of this MasterSlaveHealthMonitor.
        :type monitor_port: int
        """
        self._monitor_port = monitor_port

    @property
    def name(self):
        r"""Gets the name of this MasterSlaveHealthMonitor.

        **参数解释**：健康检查名称。  **取值范围**：不涉及

        :return: The name of this MasterSlaveHealthMonitor.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this MasterSlaveHealthMonitor.

        **参数解释**：健康检查名称。  **取值范围**：不涉及

        :param name: The name of this MasterSlaveHealthMonitor.
        :type name: str
        """
        self._name = name

    @property
    def timeout(self):
        r"""Gets the timeout of this MasterSlaveHealthMonitor.

        **参数解释**：一次健康检查请求的超时时间。  **取值范围**：不涉及

        :return: The timeout of this MasterSlaveHealthMonitor.
        :rtype: int
        """
        return self._timeout

    @timeout.setter
    def timeout(self, timeout):
        r"""Sets the timeout of this MasterSlaveHealthMonitor.

        **参数解释**：一次健康检查请求的超时时间。  **取值范围**：不涉及

        :param timeout: The timeout of this MasterSlaveHealthMonitor.
        :type timeout: int
        """
        self._timeout = timeout

    @property
    def type(self):
        r"""Gets the type of this MasterSlaveHealthMonitor.

        **参数解释**：健康检查请求协议。  **取值范围**：TCP、UDP_CONNECT、HTTP、HTTPS。

        :return: The type of this MasterSlaveHealthMonitor.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this MasterSlaveHealthMonitor.

        **参数解释**：健康检查请求协议。  **取值范围**：TCP、UDP_CONNECT、HTTP、HTTPS。

        :param type: The type of this MasterSlaveHealthMonitor.
        :type type: str
        """
        self._type = type

    @property
    def url_path(self):
        r"""Gets the url_path of this MasterSlaveHealthMonitor.

        **参数解释**：健康检查请求的请求路径。以\"/\"开头，默认为\"/\"。  **取值范围**：支持使用字母、数字和短划线（-）、正斜线（/）、半角句号（.）、百分号（%）、半角问号（?）、井号（#）和and（&）以及扩展字符集_;~!()*[]@$^:',+

        :return: The url_path of this MasterSlaveHealthMonitor.
        :rtype: str
        """
        return self._url_path

    @url_path.setter
    def url_path(self, url_path):
        r"""Sets the url_path of this MasterSlaveHealthMonitor.

        **参数解释**：健康检查请求的请求路径。以\"/\"开头，默认为\"/\"。  **取值范围**：支持使用字母、数字和短划线（-）、正斜线（/）、半角句号（.）、百分号（%）、半角问号（?）、井号（#）和and（&）以及扩展字符集_;~!()*[]@$^:',+

        :param url_path: The url_path of this MasterSlaveHealthMonitor.
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
        if not isinstance(other, MasterSlaveHealthMonitor):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

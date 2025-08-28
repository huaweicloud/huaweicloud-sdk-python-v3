# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateHealthMonitorOption:

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
        'max_retries': 'int',
        'max_retries_down': 'int',
        'monitor_port': 'int',
        'name': 'str',
        'timeout': 'int',
        'url_path': 'str',
        'type': 'str'
    }

    attribute_map = {
        'admin_state_up': 'admin_state_up',
        'delay': 'delay',
        'domain_name': 'domain_name',
        'expected_codes': 'expected_codes',
        'http_method': 'http_method',
        'max_retries': 'max_retries',
        'max_retries_down': 'max_retries_down',
        'monitor_port': 'monitor_port',
        'name': 'name',
        'timeout': 'timeout',
        'url_path': 'url_path',
        'type': 'type'
    }

    def __init__(self, admin_state_up=None, delay=None, domain_name=None, expected_codes=None, http_method=None, max_retries=None, max_retries_down=None, monitor_port=None, name=None, timeout=None, url_path=None, type=None):
        r"""UpdateHealthMonitorOption

        The model defined in huaweicloud sdk

        :param admin_state_up: **参数解释**：健康检查的管理状态。  **约束限制**：不涉及  **取值范围**： - true：表示开启健康检查。 - false：表示关闭健康检查。  **默认取值**：不涉及
        :type admin_state_up: bool
        :param delay: **参数解释**：健康检查间隔。健康检查间隔。  **约束限制**：不涉及  **取值范围**：1-50，单位：秒。  **默认取值**：不涉及
        :type delay: int
        :param domain_name: **参数解释**：发送健康检查请求的域名。  **约束限制**：当type为HTTP/HTTPS时生效。  **取值范围**：以数字或字母开头，只能包含数字、字母、’-’、’.’。 不能传空，但可传null或不传，表示使用负载均衡器的vip作为http请求的目的地址。  **默认取值**：不涉及
        :type domain_name: str
        :param expected_codes: **参数解释**：期望响应状态码。  **约束限制**：该字段仅在HTTP/HTTPS/GRPC协议下有效，其他协议可以设置但不会生效。  **取值范围**： - 单值：单个返回码，例如200。 - 列表：多个特定返回码，例如200，202。 - 区间：一个返回码区间，例如200-204。  **默认取值**：不涉及
        :type expected_codes: str
        :param http_method: **参数解释**：HTTP请求方法。  **约束限制**：当type为HTTP/HTTPS时生效。  **取值范围**：GET、HEAD、POST  **默认取值**：不涉及
        :type http_method: str
        :param max_retries: **参数解释**：健康检查连续成功多少次后，将后端服务器的健康检查状态由OFFLINE判定为ONLINE。  **约束限制**：不涉及  **取值范围**：1-10  **默认取值**：不涉及
        :type max_retries: int
        :param max_retries_down: **参数解释**：健康检查连续失败多少次后，将后端服务器的健康检查状态由ONLINE判定为OFFLINE。  **约束限制**：不涉及  **取值范围**：1-10  **默认取值**：不涉及
        :type max_retries_down: int
        :param monitor_port: **参数解释**：健康检查端口号。  [**约束限制**：不涉及](tag:hws,hws_hk,hws_eu_wb,hws_test,fcs,dt,hcso_dt,ctc,cmcc,tm,sbc,hk_sbc,hk_tm,hk_vdf,srg,g42,hk_g42) [**约束限制**：当pool协议为IP时，monitor_port必须指定为非0值。](tag:hws_eu)  **取值范围**：1-65535和null，传null表示使用后端服务器端口号。  **默认取值**：不涉及
        :type monitor_port: int
        :param name: **参数解释**：健康检查名称。  **约束限制**：不涉及  **取值范围**：不涉及  **默认取值**：不涉及
        :type name: str
        :param timeout: **参数解释**：一次健康检查请求的超时时间。  **约束限制**：不涉及  **取值范围**：建议该值小于delay的值。  **默认取值**：不涉及
        :type timeout: int
        :param url_path: **参数解释**：健康检查请求的请求路径。以\&quot;/\&quot;开头，默认为\&quot;/\&quot;。  **约束限制**：当type为HTTP/HTTPS时生效。  **取值范围**：支持使用字母、数字和短划线（-）、正斜线（/）、半角句号（.）、百分号（%）、半角问号（?）、井号（#）和and（&amp;）以及扩展字符集_;~!()*[]@$^:&#39;,+  **默认取值**：不涉及
        :type url_path: str
        :param type: **参数解释**：健康检查请求协议。  **约束限制**： - 若pool的protocol为QUIC，则type只能是UDP_CONNECT。 - 若pool的protocol为UDP，则type只能UDP_CONNECT。 - 若pool的protocol为TCP，则type可以是TCP、HTTP、HTTPS。 [- 若pool的protocol为IP，则type可以是TCP、HTTP、HTTPS。](tag:hws_eu) - 若pool的protocol为HTTP，则type可以是TCP、HTTP、HTTPS、TLS、GRPC。 - 若pool的protocol为HTTPS，则type可以是TCP、HTTP、HTTPS、TLS、GRPC。 - 若pool的protocol为GRPC，则type可以是TCP、HTTP、HTTPS、TLS、GRPC。 - 若pool的protocol为TLS，则type可以是TCP、HTTP、HTTPS、TLS、GRPC。 [- 不支持QUIC。](tag:tm,hws_eu,g42,hk_g42,hcso_dt) [- 荷兰region不支持QUIC。](tag:dt)  **取值范围**：TCP、UDP_CONNECT、HTTP、HTTPS、TLS和GRPC。  **默认取值**：不涉及
        :type type: str
        """
        
        

        self._admin_state_up = None
        self._delay = None
        self._domain_name = None
        self._expected_codes = None
        self._http_method = None
        self._max_retries = None
        self._max_retries_down = None
        self._monitor_port = None
        self._name = None
        self._timeout = None
        self._url_path = None
        self._type = None
        self.discriminator = None

        if admin_state_up is not None:
            self.admin_state_up = admin_state_up
        if delay is not None:
            self.delay = delay
        if domain_name is not None:
            self.domain_name = domain_name
        if expected_codes is not None:
            self.expected_codes = expected_codes
        if http_method is not None:
            self.http_method = http_method
        if max_retries is not None:
            self.max_retries = max_retries
        if max_retries_down is not None:
            self.max_retries_down = max_retries_down
        if monitor_port is not None:
            self.monitor_port = monitor_port
        if name is not None:
            self.name = name
        if timeout is not None:
            self.timeout = timeout
        if url_path is not None:
            self.url_path = url_path
        if type is not None:
            self.type = type

    @property
    def admin_state_up(self):
        r"""Gets the admin_state_up of this UpdateHealthMonitorOption.

        **参数解释**：健康检查的管理状态。  **约束限制**：不涉及  **取值范围**： - true：表示开启健康检查。 - false：表示关闭健康检查。  **默认取值**：不涉及

        :return: The admin_state_up of this UpdateHealthMonitorOption.
        :rtype: bool
        """
        return self._admin_state_up

    @admin_state_up.setter
    def admin_state_up(self, admin_state_up):
        r"""Sets the admin_state_up of this UpdateHealthMonitorOption.

        **参数解释**：健康检查的管理状态。  **约束限制**：不涉及  **取值范围**： - true：表示开启健康检查。 - false：表示关闭健康检查。  **默认取值**：不涉及

        :param admin_state_up: The admin_state_up of this UpdateHealthMonitorOption.
        :type admin_state_up: bool
        """
        self._admin_state_up = admin_state_up

    @property
    def delay(self):
        r"""Gets the delay of this UpdateHealthMonitorOption.

        **参数解释**：健康检查间隔。健康检查间隔。  **约束限制**：不涉及  **取值范围**：1-50，单位：秒。  **默认取值**：不涉及

        :return: The delay of this UpdateHealthMonitorOption.
        :rtype: int
        """
        return self._delay

    @delay.setter
    def delay(self, delay):
        r"""Sets the delay of this UpdateHealthMonitorOption.

        **参数解释**：健康检查间隔。健康检查间隔。  **约束限制**：不涉及  **取值范围**：1-50，单位：秒。  **默认取值**：不涉及

        :param delay: The delay of this UpdateHealthMonitorOption.
        :type delay: int
        """
        self._delay = delay

    @property
    def domain_name(self):
        r"""Gets the domain_name of this UpdateHealthMonitorOption.

        **参数解释**：发送健康检查请求的域名。  **约束限制**：当type为HTTP/HTTPS时生效。  **取值范围**：以数字或字母开头，只能包含数字、字母、’-’、’.’。 不能传空，但可传null或不传，表示使用负载均衡器的vip作为http请求的目的地址。  **默认取值**：不涉及

        :return: The domain_name of this UpdateHealthMonitorOption.
        :rtype: str
        """
        return self._domain_name

    @domain_name.setter
    def domain_name(self, domain_name):
        r"""Sets the domain_name of this UpdateHealthMonitorOption.

        **参数解释**：发送健康检查请求的域名。  **约束限制**：当type为HTTP/HTTPS时生效。  **取值范围**：以数字或字母开头，只能包含数字、字母、’-’、’.’。 不能传空，但可传null或不传，表示使用负载均衡器的vip作为http请求的目的地址。  **默认取值**：不涉及

        :param domain_name: The domain_name of this UpdateHealthMonitorOption.
        :type domain_name: str
        """
        self._domain_name = domain_name

    @property
    def expected_codes(self):
        r"""Gets the expected_codes of this UpdateHealthMonitorOption.

        **参数解释**：期望响应状态码。  **约束限制**：该字段仅在HTTP/HTTPS/GRPC协议下有效，其他协议可以设置但不会生效。  **取值范围**： - 单值：单个返回码，例如200。 - 列表：多个特定返回码，例如200，202。 - 区间：一个返回码区间，例如200-204。  **默认取值**：不涉及

        :return: The expected_codes of this UpdateHealthMonitorOption.
        :rtype: str
        """
        return self._expected_codes

    @expected_codes.setter
    def expected_codes(self, expected_codes):
        r"""Sets the expected_codes of this UpdateHealthMonitorOption.

        **参数解释**：期望响应状态码。  **约束限制**：该字段仅在HTTP/HTTPS/GRPC协议下有效，其他协议可以设置但不会生效。  **取值范围**： - 单值：单个返回码，例如200。 - 列表：多个特定返回码，例如200，202。 - 区间：一个返回码区间，例如200-204。  **默认取值**：不涉及

        :param expected_codes: The expected_codes of this UpdateHealthMonitorOption.
        :type expected_codes: str
        """
        self._expected_codes = expected_codes

    @property
    def http_method(self):
        r"""Gets the http_method of this UpdateHealthMonitorOption.

        **参数解释**：HTTP请求方法。  **约束限制**：当type为HTTP/HTTPS时生效。  **取值范围**：GET、HEAD、POST  **默认取值**：不涉及

        :return: The http_method of this UpdateHealthMonitorOption.
        :rtype: str
        """
        return self._http_method

    @http_method.setter
    def http_method(self, http_method):
        r"""Sets the http_method of this UpdateHealthMonitorOption.

        **参数解释**：HTTP请求方法。  **约束限制**：当type为HTTP/HTTPS时生效。  **取值范围**：GET、HEAD、POST  **默认取值**：不涉及

        :param http_method: The http_method of this UpdateHealthMonitorOption.
        :type http_method: str
        """
        self._http_method = http_method

    @property
    def max_retries(self):
        r"""Gets the max_retries of this UpdateHealthMonitorOption.

        **参数解释**：健康检查连续成功多少次后，将后端服务器的健康检查状态由OFFLINE判定为ONLINE。  **约束限制**：不涉及  **取值范围**：1-10  **默认取值**：不涉及

        :return: The max_retries of this UpdateHealthMonitorOption.
        :rtype: int
        """
        return self._max_retries

    @max_retries.setter
    def max_retries(self, max_retries):
        r"""Sets the max_retries of this UpdateHealthMonitorOption.

        **参数解释**：健康检查连续成功多少次后，将后端服务器的健康检查状态由OFFLINE判定为ONLINE。  **约束限制**：不涉及  **取值范围**：1-10  **默认取值**：不涉及

        :param max_retries: The max_retries of this UpdateHealthMonitorOption.
        :type max_retries: int
        """
        self._max_retries = max_retries

    @property
    def max_retries_down(self):
        r"""Gets the max_retries_down of this UpdateHealthMonitorOption.

        **参数解释**：健康检查连续失败多少次后，将后端服务器的健康检查状态由ONLINE判定为OFFLINE。  **约束限制**：不涉及  **取值范围**：1-10  **默认取值**：不涉及

        :return: The max_retries_down of this UpdateHealthMonitorOption.
        :rtype: int
        """
        return self._max_retries_down

    @max_retries_down.setter
    def max_retries_down(self, max_retries_down):
        r"""Sets the max_retries_down of this UpdateHealthMonitorOption.

        **参数解释**：健康检查连续失败多少次后，将后端服务器的健康检查状态由ONLINE判定为OFFLINE。  **约束限制**：不涉及  **取值范围**：1-10  **默认取值**：不涉及

        :param max_retries_down: The max_retries_down of this UpdateHealthMonitorOption.
        :type max_retries_down: int
        """
        self._max_retries_down = max_retries_down

    @property
    def monitor_port(self):
        r"""Gets the monitor_port of this UpdateHealthMonitorOption.

        **参数解释**：健康检查端口号。  [**约束限制**：不涉及](tag:hws,hws_hk,hws_eu_wb,hws_test,fcs,dt,hcso_dt,ctc,cmcc,tm,sbc,hk_sbc,hk_tm,hk_vdf,srg,g42,hk_g42) [**约束限制**：当pool协议为IP时，monitor_port必须指定为非0值。](tag:hws_eu)  **取值范围**：1-65535和null，传null表示使用后端服务器端口号。  **默认取值**：不涉及

        :return: The monitor_port of this UpdateHealthMonitorOption.
        :rtype: int
        """
        return self._monitor_port

    @monitor_port.setter
    def monitor_port(self, monitor_port):
        r"""Sets the monitor_port of this UpdateHealthMonitorOption.

        **参数解释**：健康检查端口号。  [**约束限制**：不涉及](tag:hws,hws_hk,hws_eu_wb,hws_test,fcs,dt,hcso_dt,ctc,cmcc,tm,sbc,hk_sbc,hk_tm,hk_vdf,srg,g42,hk_g42) [**约束限制**：当pool协议为IP时，monitor_port必须指定为非0值。](tag:hws_eu)  **取值范围**：1-65535和null，传null表示使用后端服务器端口号。  **默认取值**：不涉及

        :param monitor_port: The monitor_port of this UpdateHealthMonitorOption.
        :type monitor_port: int
        """
        self._monitor_port = monitor_port

    @property
    def name(self):
        r"""Gets the name of this UpdateHealthMonitorOption.

        **参数解释**：健康检查名称。  **约束限制**：不涉及  **取值范围**：不涉及  **默认取值**：不涉及

        :return: The name of this UpdateHealthMonitorOption.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this UpdateHealthMonitorOption.

        **参数解释**：健康检查名称。  **约束限制**：不涉及  **取值范围**：不涉及  **默认取值**：不涉及

        :param name: The name of this UpdateHealthMonitorOption.
        :type name: str
        """
        self._name = name

    @property
    def timeout(self):
        r"""Gets the timeout of this UpdateHealthMonitorOption.

        **参数解释**：一次健康检查请求的超时时间。  **约束限制**：不涉及  **取值范围**：建议该值小于delay的值。  **默认取值**：不涉及

        :return: The timeout of this UpdateHealthMonitorOption.
        :rtype: int
        """
        return self._timeout

    @timeout.setter
    def timeout(self, timeout):
        r"""Sets the timeout of this UpdateHealthMonitorOption.

        **参数解释**：一次健康检查请求的超时时间。  **约束限制**：不涉及  **取值范围**：建议该值小于delay的值。  **默认取值**：不涉及

        :param timeout: The timeout of this UpdateHealthMonitorOption.
        :type timeout: int
        """
        self._timeout = timeout

    @property
    def url_path(self):
        r"""Gets the url_path of this UpdateHealthMonitorOption.

        **参数解释**：健康检查请求的请求路径。以\"/\"开头，默认为\"/\"。  **约束限制**：当type为HTTP/HTTPS时生效。  **取值范围**：支持使用字母、数字和短划线（-）、正斜线（/）、半角句号（.）、百分号（%）、半角问号（?）、井号（#）和and（&）以及扩展字符集_;~!()*[]@$^:',+  **默认取值**：不涉及

        :return: The url_path of this UpdateHealthMonitorOption.
        :rtype: str
        """
        return self._url_path

    @url_path.setter
    def url_path(self, url_path):
        r"""Sets the url_path of this UpdateHealthMonitorOption.

        **参数解释**：健康检查请求的请求路径。以\"/\"开头，默认为\"/\"。  **约束限制**：当type为HTTP/HTTPS时生效。  **取值范围**：支持使用字母、数字和短划线（-）、正斜线（/）、半角句号（.）、百分号（%）、半角问号（?）、井号（#）和and（&）以及扩展字符集_;~!()*[]@$^:',+  **默认取值**：不涉及

        :param url_path: The url_path of this UpdateHealthMonitorOption.
        :type url_path: str
        """
        self._url_path = url_path

    @property
    def type(self):
        r"""Gets the type of this UpdateHealthMonitorOption.

        **参数解释**：健康检查请求协议。  **约束限制**： - 若pool的protocol为QUIC，则type只能是UDP_CONNECT。 - 若pool的protocol为UDP，则type只能UDP_CONNECT。 - 若pool的protocol为TCP，则type可以是TCP、HTTP、HTTPS。 [- 若pool的protocol为IP，则type可以是TCP、HTTP、HTTPS。](tag:hws_eu) - 若pool的protocol为HTTP，则type可以是TCP、HTTP、HTTPS、TLS、GRPC。 - 若pool的protocol为HTTPS，则type可以是TCP、HTTP、HTTPS、TLS、GRPC。 - 若pool的protocol为GRPC，则type可以是TCP、HTTP、HTTPS、TLS、GRPC。 - 若pool的protocol为TLS，则type可以是TCP、HTTP、HTTPS、TLS、GRPC。 [- 不支持QUIC。](tag:tm,hws_eu,g42,hk_g42,hcso_dt) [- 荷兰region不支持QUIC。](tag:dt)  **取值范围**：TCP、UDP_CONNECT、HTTP、HTTPS、TLS和GRPC。  **默认取值**：不涉及

        :return: The type of this UpdateHealthMonitorOption.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this UpdateHealthMonitorOption.

        **参数解释**：健康检查请求协议。  **约束限制**： - 若pool的protocol为QUIC，则type只能是UDP_CONNECT。 - 若pool的protocol为UDP，则type只能UDP_CONNECT。 - 若pool的protocol为TCP，则type可以是TCP、HTTP、HTTPS。 [- 若pool的protocol为IP，则type可以是TCP、HTTP、HTTPS。](tag:hws_eu) - 若pool的protocol为HTTP，则type可以是TCP、HTTP、HTTPS、TLS、GRPC。 - 若pool的protocol为HTTPS，则type可以是TCP、HTTP、HTTPS、TLS、GRPC。 - 若pool的protocol为GRPC，则type可以是TCP、HTTP、HTTPS、TLS、GRPC。 - 若pool的protocol为TLS，则type可以是TCP、HTTP、HTTPS、TLS、GRPC。 [- 不支持QUIC。](tag:tm,hws_eu,g42,hk_g42,hcso_dt) [- 荷兰region不支持QUIC。](tag:dt)  **取值范围**：TCP、UDP_CONNECT、HTTP、HTTPS、TLS和GRPC。  **默认取值**：不涉及

        :param type: The type of this UpdateHealthMonitorOption.
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
        if not isinstance(other, UpdateHealthMonitorOption):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

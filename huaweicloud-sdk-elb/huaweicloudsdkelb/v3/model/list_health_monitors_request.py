# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListHealthMonitorsRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'marker': 'str',
        'limit': 'int',
        'page_reverse': 'bool',
        'id': 'list[str]',
        'monitor_port': 'list[int]',
        'domain_name': 'list[str]',
        'name': 'list[str]',
        'delay': 'list[int]',
        'max_retries': 'list[int]',
        'admin_state_up': 'bool',
        'max_retries_down': 'list[int]',
        'timeout': 'int',
        'type': 'list[str]',
        'expected_codes': 'list[str]',
        'url_path': 'list[str]',
        'http_method': 'list[str]',
        'enterprise_project_id': 'list[str]'
    }

    attribute_map = {
        'marker': 'marker',
        'limit': 'limit',
        'page_reverse': 'page_reverse',
        'id': 'id',
        'monitor_port': 'monitor_port',
        'domain_name': 'domain_name',
        'name': 'name',
        'delay': 'delay',
        'max_retries': 'max_retries',
        'admin_state_up': 'admin_state_up',
        'max_retries_down': 'max_retries_down',
        'timeout': 'timeout',
        'type': 'type',
        'expected_codes': 'expected_codes',
        'url_path': 'url_path',
        'http_method': 'http_method',
        'enterprise_project_id': 'enterprise_project_id'
    }

    def __init__(self, marker=None, limit=None, page_reverse=None, id=None, monitor_port=None, domain_name=None, name=None, delay=None, max_retries=None, admin_state_up=None, max_retries_down=None, timeout=None, type=None, expected_codes=None, url_path=None, http_method=None, enterprise_project_id=None):
        r"""ListHealthMonitorsRequest

        The model defined in huaweicloud sdk

        :param marker: **参数解释**：上一页最后一条记录的ID。  **约束限制**： - 必须与limit一起使用。 - 不指定时表示查询第一页。 - 该字段不允许为空或无效的ID。  **取值范围**：不涉及  **默认取值**：不涉及
        :type marker: str
        :param limit: **参数解释**：每页返回的个数。  **约束限制**：不涉及  **取值范围**：0-2000  **默认取值**：2000
        :type limit: int
        :param page_reverse: **参数解释**：是否反向查询。  **约束限制**： - 必须与limit一起使用。 - 当page_reverse&#x3D;true时，若要查询上一页，marker取值为当前页返回值的previous_marker。  **取值范围**： - true：查询上一页。 - false：查询下一页。  **默认取值**：false
        :type page_reverse: bool
        :param id: **参数解释**：健康检查ID。 支持多值查询，查询条件格式：*id&#x3D;xxx&amp;id&#x3D;xxx****。  **约束限制**：不涉及  **取值范围**：不涉及  **默认取值**：不涉及
        :type id: list[str]
        :param monitor_port: **参数解释**：健康检查端口号。 支持多值查询，查询条件格式：***monitor_port&#x3D;xxx&amp;monitor_port&#x3D;xxx***。  **约束限制**：不涉及  **取值范围**：不涉及  **默认取值**：不涉及
        :type monitor_port: list[int]
        :param domain_name: **参数解释**：发送健康检查请求的域名。 支持多值查询，查询条件格式：**domain_name&#x3D;xxx&amp;domain_name&#x3D;xxx**。  **约束限制**：不涉及  **取值范围**：以数字或字母开头，只能包含数字、字母、’-’、’.’。  **默认取值**：不涉及
        :type domain_name: list[str]
        :param name: **参数解释**：健康检查名称。 支持多值查询，查询条件格式：*name&#x3D;xxx&amp;name&#x3D;xxx*。  **约束限制**：不涉及  **取值范围**：不涉及  **默认取值**：不涉及
        :type name: list[str]
        :param delay: **参数解释**：健康检查间隔。 支持多值查询，查询条件格式：*delay&#x3D;xxx&amp;delay&#x3D;xxx*。  **约束限制**：不涉及  **取值范围**：1-50，单位：秒。  **默认取值**：不涉及
        :type delay: list[int]
        :param max_retries: **参数解释**：健康检查连续成功多少次后，将后端服务器的健康检查状态由OFFLINE判定为ONLINE。 支持多值查询，查询条件格式：*******max_retries&#x3D;xxx&amp;max_retries&#x3D;xxx*******。  **约束限制**：不涉及  **取值范围**：1-10  **默认取值**：不涉及
        :type max_retries: list[int]
        :param admin_state_up: **参数解释**：健康检查的管理状态。  **约束限制**：不涉及  **取值范围**： - true：表示开启健康检查。 - false表示关闭健康检查。  **默认取值**：不涉及
        :type admin_state_up: bool
        :param max_retries_down: **参数解释**：健康检查连续失败多少次后，将后端服务器的健康检查状态由ONLINE判定为OFFLINE。 支持多值查询，查询条件格式：******max_retries_down&#x3D;xxx&amp;max_retries_down&#x3D;xxx******。  **约束限制**：不涉及  **取值范围**：1-10  **默认取值**：不涉及
        :type max_retries_down: list[int]
        :param timeout: **参数解释**：一次健康检查请求的超时时间。  **约束限制**：不涉及  **取值范围**：不涉及  **默认取值**：不涉及
        :type timeout: int
        :param type: **参数解释**：健康检查请求协议。 支持多值查询，查询条件格式：*****type&#x3D;xxx&amp;type&#x3D;xxx*****。  **约束限制**：不涉及  **取值范围**：TCP、UDP_CONNECT、HTTP、HTTPS、TLS和GRPC。  **默认取值**：不涉及
        :type type: list[str]
        :param expected_codes: **参数解释**：期望响应状态码。 支持多值查询，查询条件格式：****expected_codes&#x3D;xxx&amp;expected_codes&#x3D;xxx****。  **约束限制**： - 单值：单个返回码，例如200。 - 列表：多个特定返回码，例如200，202。 - 区间：一个返回码区间，例如200-204。  **取值范围**：不涉及  **默认取值**：不涉及
        :type expected_codes: list[str]
        :param url_path: **参数解释**：健康检查测试member健康时发送的http请求路径。 支持多值查询，查询条件格式：***url_path&#x3D;xxx&amp;url_path&#x3D;xxx***。  **约束限制**：不涉及  **取值范围**：不涉及  **默认取值**：不涉及
        :type url_path: list[str]
        :param http_method: **参数解释**：HTTP请求方法。 支持多值查询，查询条件格式：**http_method&#x3D;xxx&amp;http_method&#x3D;xxx**。  **约束限制**：不涉及  **取值范围**：GET、HEAD、POST  **默认取值**：不涉及
        :type http_method: list[str]
        :param enterprise_project_id: **参数解释**：资源所属的企业项目ID。 支持多值查询，查询条件格式：*enterprise_project_id&#x3D;xxx&amp;enterprise_project_id&#x3D;xxx*。  **约束限制**： - 如果enterprise_project_id不传值，默认查询所有企业项目下的资源，鉴权按照细粒度权限鉴权，必须在用户组下分配elb:healthmonitors:list权限。 - 如果enterprise_project_id传值，鉴权按照企业项目权限鉴权，分为传入具体eps_id和all_granted_eps两种场景，前者查询指定eps_id的eps下的资源，后者查询的是所有有list权限的eps下的资源。  **取值范围**：不涉及  **默认取值**：不涉及  [不支持该字段，请勿使用。](tag:dt,hcso_dt)
        :type enterprise_project_id: list[str]
        """
        
        

        self._marker = None
        self._limit = None
        self._page_reverse = None
        self._id = None
        self._monitor_port = None
        self._domain_name = None
        self._name = None
        self._delay = None
        self._max_retries = None
        self._admin_state_up = None
        self._max_retries_down = None
        self._timeout = None
        self._type = None
        self._expected_codes = None
        self._url_path = None
        self._http_method = None
        self._enterprise_project_id = None
        self.discriminator = None

        if marker is not None:
            self.marker = marker
        if limit is not None:
            self.limit = limit
        if page_reverse is not None:
            self.page_reverse = page_reverse
        if id is not None:
            self.id = id
        if monitor_port is not None:
            self.monitor_port = monitor_port
        if domain_name is not None:
            self.domain_name = domain_name
        if name is not None:
            self.name = name
        if delay is not None:
            self.delay = delay
        if max_retries is not None:
            self.max_retries = max_retries
        if admin_state_up is not None:
            self.admin_state_up = admin_state_up
        if max_retries_down is not None:
            self.max_retries_down = max_retries_down
        if timeout is not None:
            self.timeout = timeout
        if type is not None:
            self.type = type
        if expected_codes is not None:
            self.expected_codes = expected_codes
        if url_path is not None:
            self.url_path = url_path
        if http_method is not None:
            self.http_method = http_method
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id

    @property
    def marker(self):
        r"""Gets the marker of this ListHealthMonitorsRequest.

        **参数解释**：上一页最后一条记录的ID。  **约束限制**： - 必须与limit一起使用。 - 不指定时表示查询第一页。 - 该字段不允许为空或无效的ID。  **取值范围**：不涉及  **默认取值**：不涉及

        :return: The marker of this ListHealthMonitorsRequest.
        :rtype: str
        """
        return self._marker

    @marker.setter
    def marker(self, marker):
        r"""Sets the marker of this ListHealthMonitorsRequest.

        **参数解释**：上一页最后一条记录的ID。  **约束限制**： - 必须与limit一起使用。 - 不指定时表示查询第一页。 - 该字段不允许为空或无效的ID。  **取值范围**：不涉及  **默认取值**：不涉及

        :param marker: The marker of this ListHealthMonitorsRequest.
        :type marker: str
        """
        self._marker = marker

    @property
    def limit(self):
        r"""Gets the limit of this ListHealthMonitorsRequest.

        **参数解释**：每页返回的个数。  **约束限制**：不涉及  **取值范围**：0-2000  **默认取值**：2000

        :return: The limit of this ListHealthMonitorsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListHealthMonitorsRequest.

        **参数解释**：每页返回的个数。  **约束限制**：不涉及  **取值范围**：0-2000  **默认取值**：2000

        :param limit: The limit of this ListHealthMonitorsRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def page_reverse(self):
        r"""Gets the page_reverse of this ListHealthMonitorsRequest.

        **参数解释**：是否反向查询。  **约束限制**： - 必须与limit一起使用。 - 当page_reverse=true时，若要查询上一页，marker取值为当前页返回值的previous_marker。  **取值范围**： - true：查询上一页。 - false：查询下一页。  **默认取值**：false

        :return: The page_reverse of this ListHealthMonitorsRequest.
        :rtype: bool
        """
        return self._page_reverse

    @page_reverse.setter
    def page_reverse(self, page_reverse):
        r"""Sets the page_reverse of this ListHealthMonitorsRequest.

        **参数解释**：是否反向查询。  **约束限制**： - 必须与limit一起使用。 - 当page_reverse=true时，若要查询上一页，marker取值为当前页返回值的previous_marker。  **取值范围**： - true：查询上一页。 - false：查询下一页。  **默认取值**：false

        :param page_reverse: The page_reverse of this ListHealthMonitorsRequest.
        :type page_reverse: bool
        """
        self._page_reverse = page_reverse

    @property
    def id(self):
        r"""Gets the id of this ListHealthMonitorsRequest.

        **参数解释**：健康检查ID。 支持多值查询，查询条件格式：*id=xxx&id=xxx****。  **约束限制**：不涉及  **取值范围**：不涉及  **默认取值**：不涉及

        :return: The id of this ListHealthMonitorsRequest.
        :rtype: list[str]
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this ListHealthMonitorsRequest.

        **参数解释**：健康检查ID。 支持多值查询，查询条件格式：*id=xxx&id=xxx****。  **约束限制**：不涉及  **取值范围**：不涉及  **默认取值**：不涉及

        :param id: The id of this ListHealthMonitorsRequest.
        :type id: list[str]
        """
        self._id = id

    @property
    def monitor_port(self):
        r"""Gets the monitor_port of this ListHealthMonitorsRequest.

        **参数解释**：健康检查端口号。 支持多值查询，查询条件格式：***monitor_port=xxx&monitor_port=xxx***。  **约束限制**：不涉及  **取值范围**：不涉及  **默认取值**：不涉及

        :return: The monitor_port of this ListHealthMonitorsRequest.
        :rtype: list[int]
        """
        return self._monitor_port

    @monitor_port.setter
    def monitor_port(self, monitor_port):
        r"""Sets the monitor_port of this ListHealthMonitorsRequest.

        **参数解释**：健康检查端口号。 支持多值查询，查询条件格式：***monitor_port=xxx&monitor_port=xxx***。  **约束限制**：不涉及  **取值范围**：不涉及  **默认取值**：不涉及

        :param monitor_port: The monitor_port of this ListHealthMonitorsRequest.
        :type monitor_port: list[int]
        """
        self._monitor_port = monitor_port

    @property
    def domain_name(self):
        r"""Gets the domain_name of this ListHealthMonitorsRequest.

        **参数解释**：发送健康检查请求的域名。 支持多值查询，查询条件格式：**domain_name=xxx&domain_name=xxx**。  **约束限制**：不涉及  **取值范围**：以数字或字母开头，只能包含数字、字母、’-’、’.’。  **默认取值**：不涉及

        :return: The domain_name of this ListHealthMonitorsRequest.
        :rtype: list[str]
        """
        return self._domain_name

    @domain_name.setter
    def domain_name(self, domain_name):
        r"""Sets the domain_name of this ListHealthMonitorsRequest.

        **参数解释**：发送健康检查请求的域名。 支持多值查询，查询条件格式：**domain_name=xxx&domain_name=xxx**。  **约束限制**：不涉及  **取值范围**：以数字或字母开头，只能包含数字、字母、’-’、’.’。  **默认取值**：不涉及

        :param domain_name: The domain_name of this ListHealthMonitorsRequest.
        :type domain_name: list[str]
        """
        self._domain_name = domain_name

    @property
    def name(self):
        r"""Gets the name of this ListHealthMonitorsRequest.

        **参数解释**：健康检查名称。 支持多值查询，查询条件格式：*name=xxx&name=xxx*。  **约束限制**：不涉及  **取值范围**：不涉及  **默认取值**：不涉及

        :return: The name of this ListHealthMonitorsRequest.
        :rtype: list[str]
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this ListHealthMonitorsRequest.

        **参数解释**：健康检查名称。 支持多值查询，查询条件格式：*name=xxx&name=xxx*。  **约束限制**：不涉及  **取值范围**：不涉及  **默认取值**：不涉及

        :param name: The name of this ListHealthMonitorsRequest.
        :type name: list[str]
        """
        self._name = name

    @property
    def delay(self):
        r"""Gets the delay of this ListHealthMonitorsRequest.

        **参数解释**：健康检查间隔。 支持多值查询，查询条件格式：*delay=xxx&delay=xxx*。  **约束限制**：不涉及  **取值范围**：1-50，单位：秒。  **默认取值**：不涉及

        :return: The delay of this ListHealthMonitorsRequest.
        :rtype: list[int]
        """
        return self._delay

    @delay.setter
    def delay(self, delay):
        r"""Sets the delay of this ListHealthMonitorsRequest.

        **参数解释**：健康检查间隔。 支持多值查询，查询条件格式：*delay=xxx&delay=xxx*。  **约束限制**：不涉及  **取值范围**：1-50，单位：秒。  **默认取值**：不涉及

        :param delay: The delay of this ListHealthMonitorsRequest.
        :type delay: list[int]
        """
        self._delay = delay

    @property
    def max_retries(self):
        r"""Gets the max_retries of this ListHealthMonitorsRequest.

        **参数解释**：健康检查连续成功多少次后，将后端服务器的健康检查状态由OFFLINE判定为ONLINE。 支持多值查询，查询条件格式：*******max_retries=xxx&max_retries=xxx*******。  **约束限制**：不涉及  **取值范围**：1-10  **默认取值**：不涉及

        :return: The max_retries of this ListHealthMonitorsRequest.
        :rtype: list[int]
        """
        return self._max_retries

    @max_retries.setter
    def max_retries(self, max_retries):
        r"""Sets the max_retries of this ListHealthMonitorsRequest.

        **参数解释**：健康检查连续成功多少次后，将后端服务器的健康检查状态由OFFLINE判定为ONLINE。 支持多值查询，查询条件格式：*******max_retries=xxx&max_retries=xxx*******。  **约束限制**：不涉及  **取值范围**：1-10  **默认取值**：不涉及

        :param max_retries: The max_retries of this ListHealthMonitorsRequest.
        :type max_retries: list[int]
        """
        self._max_retries = max_retries

    @property
    def admin_state_up(self):
        r"""Gets the admin_state_up of this ListHealthMonitorsRequest.

        **参数解释**：健康检查的管理状态。  **约束限制**：不涉及  **取值范围**： - true：表示开启健康检查。 - false表示关闭健康检查。  **默认取值**：不涉及

        :return: The admin_state_up of this ListHealthMonitorsRequest.
        :rtype: bool
        """
        return self._admin_state_up

    @admin_state_up.setter
    def admin_state_up(self, admin_state_up):
        r"""Sets the admin_state_up of this ListHealthMonitorsRequest.

        **参数解释**：健康检查的管理状态。  **约束限制**：不涉及  **取值范围**： - true：表示开启健康检查。 - false表示关闭健康检查。  **默认取值**：不涉及

        :param admin_state_up: The admin_state_up of this ListHealthMonitorsRequest.
        :type admin_state_up: bool
        """
        self._admin_state_up = admin_state_up

    @property
    def max_retries_down(self):
        r"""Gets the max_retries_down of this ListHealthMonitorsRequest.

        **参数解释**：健康检查连续失败多少次后，将后端服务器的健康检查状态由ONLINE判定为OFFLINE。 支持多值查询，查询条件格式：******max_retries_down=xxx&max_retries_down=xxx******。  **约束限制**：不涉及  **取值范围**：1-10  **默认取值**：不涉及

        :return: The max_retries_down of this ListHealthMonitorsRequest.
        :rtype: list[int]
        """
        return self._max_retries_down

    @max_retries_down.setter
    def max_retries_down(self, max_retries_down):
        r"""Sets the max_retries_down of this ListHealthMonitorsRequest.

        **参数解释**：健康检查连续失败多少次后，将后端服务器的健康检查状态由ONLINE判定为OFFLINE。 支持多值查询，查询条件格式：******max_retries_down=xxx&max_retries_down=xxx******。  **约束限制**：不涉及  **取值范围**：1-10  **默认取值**：不涉及

        :param max_retries_down: The max_retries_down of this ListHealthMonitorsRequest.
        :type max_retries_down: list[int]
        """
        self._max_retries_down = max_retries_down

    @property
    def timeout(self):
        r"""Gets the timeout of this ListHealthMonitorsRequest.

        **参数解释**：一次健康检查请求的超时时间。  **约束限制**：不涉及  **取值范围**：不涉及  **默认取值**：不涉及

        :return: The timeout of this ListHealthMonitorsRequest.
        :rtype: int
        """
        return self._timeout

    @timeout.setter
    def timeout(self, timeout):
        r"""Sets the timeout of this ListHealthMonitorsRequest.

        **参数解释**：一次健康检查请求的超时时间。  **约束限制**：不涉及  **取值范围**：不涉及  **默认取值**：不涉及

        :param timeout: The timeout of this ListHealthMonitorsRequest.
        :type timeout: int
        """
        self._timeout = timeout

    @property
    def type(self):
        r"""Gets the type of this ListHealthMonitorsRequest.

        **参数解释**：健康检查请求协议。 支持多值查询，查询条件格式：*****type=xxx&type=xxx*****。  **约束限制**：不涉及  **取值范围**：TCP、UDP_CONNECT、HTTP、HTTPS、TLS和GRPC。  **默认取值**：不涉及

        :return: The type of this ListHealthMonitorsRequest.
        :rtype: list[str]
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this ListHealthMonitorsRequest.

        **参数解释**：健康检查请求协议。 支持多值查询，查询条件格式：*****type=xxx&type=xxx*****。  **约束限制**：不涉及  **取值范围**：TCP、UDP_CONNECT、HTTP、HTTPS、TLS和GRPC。  **默认取值**：不涉及

        :param type: The type of this ListHealthMonitorsRequest.
        :type type: list[str]
        """
        self._type = type

    @property
    def expected_codes(self):
        r"""Gets the expected_codes of this ListHealthMonitorsRequest.

        **参数解释**：期望响应状态码。 支持多值查询，查询条件格式：****expected_codes=xxx&expected_codes=xxx****。  **约束限制**： - 单值：单个返回码，例如200。 - 列表：多个特定返回码，例如200，202。 - 区间：一个返回码区间，例如200-204。  **取值范围**：不涉及  **默认取值**：不涉及

        :return: The expected_codes of this ListHealthMonitorsRequest.
        :rtype: list[str]
        """
        return self._expected_codes

    @expected_codes.setter
    def expected_codes(self, expected_codes):
        r"""Sets the expected_codes of this ListHealthMonitorsRequest.

        **参数解释**：期望响应状态码。 支持多值查询，查询条件格式：****expected_codes=xxx&expected_codes=xxx****。  **约束限制**： - 单值：单个返回码，例如200。 - 列表：多个特定返回码，例如200，202。 - 区间：一个返回码区间，例如200-204。  **取值范围**：不涉及  **默认取值**：不涉及

        :param expected_codes: The expected_codes of this ListHealthMonitorsRequest.
        :type expected_codes: list[str]
        """
        self._expected_codes = expected_codes

    @property
    def url_path(self):
        r"""Gets the url_path of this ListHealthMonitorsRequest.

        **参数解释**：健康检查测试member健康时发送的http请求路径。 支持多值查询，查询条件格式：***url_path=xxx&url_path=xxx***。  **约束限制**：不涉及  **取值范围**：不涉及  **默认取值**：不涉及

        :return: The url_path of this ListHealthMonitorsRequest.
        :rtype: list[str]
        """
        return self._url_path

    @url_path.setter
    def url_path(self, url_path):
        r"""Sets the url_path of this ListHealthMonitorsRequest.

        **参数解释**：健康检查测试member健康时发送的http请求路径。 支持多值查询，查询条件格式：***url_path=xxx&url_path=xxx***。  **约束限制**：不涉及  **取值范围**：不涉及  **默认取值**：不涉及

        :param url_path: The url_path of this ListHealthMonitorsRequest.
        :type url_path: list[str]
        """
        self._url_path = url_path

    @property
    def http_method(self):
        r"""Gets the http_method of this ListHealthMonitorsRequest.

        **参数解释**：HTTP请求方法。 支持多值查询，查询条件格式：**http_method=xxx&http_method=xxx**。  **约束限制**：不涉及  **取值范围**：GET、HEAD、POST  **默认取值**：不涉及

        :return: The http_method of this ListHealthMonitorsRequest.
        :rtype: list[str]
        """
        return self._http_method

    @http_method.setter
    def http_method(self, http_method):
        r"""Sets the http_method of this ListHealthMonitorsRequest.

        **参数解释**：HTTP请求方法。 支持多值查询，查询条件格式：**http_method=xxx&http_method=xxx**。  **约束限制**：不涉及  **取值范围**：GET、HEAD、POST  **默认取值**：不涉及

        :param http_method: The http_method of this ListHealthMonitorsRequest.
        :type http_method: list[str]
        """
        self._http_method = http_method

    @property
    def enterprise_project_id(self):
        r"""Gets the enterprise_project_id of this ListHealthMonitorsRequest.

        **参数解释**：资源所属的企业项目ID。 支持多值查询，查询条件格式：*enterprise_project_id=xxx&enterprise_project_id=xxx*。  **约束限制**： - 如果enterprise_project_id不传值，默认查询所有企业项目下的资源，鉴权按照细粒度权限鉴权，必须在用户组下分配elb:healthmonitors:list权限。 - 如果enterprise_project_id传值，鉴权按照企业项目权限鉴权，分为传入具体eps_id和all_granted_eps两种场景，前者查询指定eps_id的eps下的资源，后者查询的是所有有list权限的eps下的资源。  **取值范围**：不涉及  **默认取值**：不涉及  [不支持该字段，请勿使用。](tag:dt,hcso_dt)

        :return: The enterprise_project_id of this ListHealthMonitorsRequest.
        :rtype: list[str]
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        r"""Sets the enterprise_project_id of this ListHealthMonitorsRequest.

        **参数解释**：资源所属的企业项目ID。 支持多值查询，查询条件格式：*enterprise_project_id=xxx&enterprise_project_id=xxx*。  **约束限制**： - 如果enterprise_project_id不传值，默认查询所有企业项目下的资源，鉴权按照细粒度权限鉴权，必须在用户组下分配elb:healthmonitors:list权限。 - 如果enterprise_project_id传值，鉴权按照企业项目权限鉴权，分为传入具体eps_id和all_granted_eps两种场景，前者查询指定eps_id的eps下的资源，后者查询的是所有有list权限的eps下的资源。  **取值范围**：不涉及  **默认取值**：不涉及  [不支持该字段，请勿使用。](tag:dt,hcso_dt)

        :param enterprise_project_id: The enterprise_project_id of this ListHealthMonitorsRequest.
        :type enterprise_project_id: list[str]
        """
        self._enterprise_project_id = enterprise_project_id

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
        if not isinstance(other, ListHealthMonitorsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

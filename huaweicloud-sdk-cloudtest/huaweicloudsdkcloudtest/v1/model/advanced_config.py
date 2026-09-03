# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AdvancedConfig:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'block_enable': 'str',
        'case_timeout': 'int',
        'enable_cookie': 'str',
        'header_default': 'str',
        'http_timeout': 'int',
        'octopus_image': 'str',
        'parallel_number': 'int',
        'proxy_auth_name': 'str',
        'proxy_auth_password': 'str',
        'proxy_host_name': 'str',
        'proxy_port': 'str',
        'serial_run': 'str',
        'task_stop_time': 'datetime',
        'task_timeout': 'int'
    }

    attribute_map = {
        'block_enable': 'blockEnable',
        'case_timeout': 'caseTimeout',
        'enable_cookie': 'enableCookie',
        'header_default': 'headerDefault',
        'http_timeout': 'httpTimeout',
        'octopus_image': 'octopusImage',
        'parallel_number': 'parallelNumber',
        'proxy_auth_name': 'proxyAuthName',
        'proxy_auth_password': 'proxyAuthPassword',
        'proxy_host_name': 'proxyHostName',
        'proxy_port': 'proxyPort',
        'serial_run': 'serialRun',
        'task_stop_time': 'taskStopTime',
        'task_timeout': 'taskTimeout'
    }

    def __init__(self, block_enable=None, case_timeout=None, enable_cookie=None, header_default=None, http_timeout=None, octopus_image=None, parallel_number=None, proxy_auth_name=None, proxy_auth_password=None, proxy_host_name=None, proxy_port=None, serial_run=None, task_stop_time=None, task_timeout=None):
        r"""AdvancedConfig

        The model defined in huaweicloud sdk

        :param block_enable: 分块开关 1:打开 0：关闭，默认：打开
        :type block_enable: str
        :param case_timeout: 用例超时时间
        :type case_timeout: int
        :param enable_cookie: httpClient报存cookie配置：1 保存 0 不保存
        :type enable_cookie: str
        :param header_default: 关闭默认添加content-type和accept请求头配置：1 打开 0 关闭
        :type header_default: str
        :param http_timeout: http请求超时时间
        :type http_timeout: int
        :param octopus_image: 八爪鱼镜像地址
        :type octopus_image: str
        :param parallel_number: 并行用例个数
        :type parallel_number: int
        :param proxy_auth_name: 代理用户名
        :type proxy_auth_name: str
        :param proxy_auth_password: 代理密码
        :type proxy_auth_password: str
        :param proxy_host_name: 代理服务配置
        :type proxy_host_name: str
        :param proxy_port: 代理服务配置
        :type proxy_port: str
        :param serial_run: 串行配置
        :type serial_run: str
        :param task_stop_time: 任务停止时间
        :type task_stop_time: datetime
        :param task_timeout: 任务超时时间
        :type task_timeout: int
        """
        
        

        self._block_enable = None
        self._case_timeout = None
        self._enable_cookie = None
        self._header_default = None
        self._http_timeout = None
        self._octopus_image = None
        self._parallel_number = None
        self._proxy_auth_name = None
        self._proxy_auth_password = None
        self._proxy_host_name = None
        self._proxy_port = None
        self._serial_run = None
        self._task_stop_time = None
        self._task_timeout = None
        self.discriminator = None

        if block_enable is not None:
            self.block_enable = block_enable
        if case_timeout is not None:
            self.case_timeout = case_timeout
        if enable_cookie is not None:
            self.enable_cookie = enable_cookie
        if header_default is not None:
            self.header_default = header_default
        if http_timeout is not None:
            self.http_timeout = http_timeout
        if octopus_image is not None:
            self.octopus_image = octopus_image
        if parallel_number is not None:
            self.parallel_number = parallel_number
        if proxy_auth_name is not None:
            self.proxy_auth_name = proxy_auth_name
        if proxy_auth_password is not None:
            self.proxy_auth_password = proxy_auth_password
        if proxy_host_name is not None:
            self.proxy_host_name = proxy_host_name
        if proxy_port is not None:
            self.proxy_port = proxy_port
        if serial_run is not None:
            self.serial_run = serial_run
        if task_stop_time is not None:
            self.task_stop_time = task_stop_time
        if task_timeout is not None:
            self.task_timeout = task_timeout

    @property
    def block_enable(self):
        r"""Gets the block_enable of this AdvancedConfig.

        分块开关 1:打开 0：关闭，默认：打开

        :return: The block_enable of this AdvancedConfig.
        :rtype: str
        """
        return self._block_enable

    @block_enable.setter
    def block_enable(self, block_enable):
        r"""Sets the block_enable of this AdvancedConfig.

        分块开关 1:打开 0：关闭，默认：打开

        :param block_enable: The block_enable of this AdvancedConfig.
        :type block_enable: str
        """
        self._block_enable = block_enable

    @property
    def case_timeout(self):
        r"""Gets the case_timeout of this AdvancedConfig.

        用例超时时间

        :return: The case_timeout of this AdvancedConfig.
        :rtype: int
        """
        return self._case_timeout

    @case_timeout.setter
    def case_timeout(self, case_timeout):
        r"""Sets the case_timeout of this AdvancedConfig.

        用例超时时间

        :param case_timeout: The case_timeout of this AdvancedConfig.
        :type case_timeout: int
        """
        self._case_timeout = case_timeout

    @property
    def enable_cookie(self):
        r"""Gets the enable_cookie of this AdvancedConfig.

        httpClient报存cookie配置：1 保存 0 不保存

        :return: The enable_cookie of this AdvancedConfig.
        :rtype: str
        """
        return self._enable_cookie

    @enable_cookie.setter
    def enable_cookie(self, enable_cookie):
        r"""Sets the enable_cookie of this AdvancedConfig.

        httpClient报存cookie配置：1 保存 0 不保存

        :param enable_cookie: The enable_cookie of this AdvancedConfig.
        :type enable_cookie: str
        """
        self._enable_cookie = enable_cookie

    @property
    def header_default(self):
        r"""Gets the header_default of this AdvancedConfig.

        关闭默认添加content-type和accept请求头配置：1 打开 0 关闭

        :return: The header_default of this AdvancedConfig.
        :rtype: str
        """
        return self._header_default

    @header_default.setter
    def header_default(self, header_default):
        r"""Sets the header_default of this AdvancedConfig.

        关闭默认添加content-type和accept请求头配置：1 打开 0 关闭

        :param header_default: The header_default of this AdvancedConfig.
        :type header_default: str
        """
        self._header_default = header_default

    @property
    def http_timeout(self):
        r"""Gets the http_timeout of this AdvancedConfig.

        http请求超时时间

        :return: The http_timeout of this AdvancedConfig.
        :rtype: int
        """
        return self._http_timeout

    @http_timeout.setter
    def http_timeout(self, http_timeout):
        r"""Sets the http_timeout of this AdvancedConfig.

        http请求超时时间

        :param http_timeout: The http_timeout of this AdvancedConfig.
        :type http_timeout: int
        """
        self._http_timeout = http_timeout

    @property
    def octopus_image(self):
        r"""Gets the octopus_image of this AdvancedConfig.

        八爪鱼镜像地址

        :return: The octopus_image of this AdvancedConfig.
        :rtype: str
        """
        return self._octopus_image

    @octopus_image.setter
    def octopus_image(self, octopus_image):
        r"""Sets the octopus_image of this AdvancedConfig.

        八爪鱼镜像地址

        :param octopus_image: The octopus_image of this AdvancedConfig.
        :type octopus_image: str
        """
        self._octopus_image = octopus_image

    @property
    def parallel_number(self):
        r"""Gets the parallel_number of this AdvancedConfig.

        并行用例个数

        :return: The parallel_number of this AdvancedConfig.
        :rtype: int
        """
        return self._parallel_number

    @parallel_number.setter
    def parallel_number(self, parallel_number):
        r"""Sets the parallel_number of this AdvancedConfig.

        并行用例个数

        :param parallel_number: The parallel_number of this AdvancedConfig.
        :type parallel_number: int
        """
        self._parallel_number = parallel_number

    @property
    def proxy_auth_name(self):
        r"""Gets the proxy_auth_name of this AdvancedConfig.

        代理用户名

        :return: The proxy_auth_name of this AdvancedConfig.
        :rtype: str
        """
        return self._proxy_auth_name

    @proxy_auth_name.setter
    def proxy_auth_name(self, proxy_auth_name):
        r"""Sets the proxy_auth_name of this AdvancedConfig.

        代理用户名

        :param proxy_auth_name: The proxy_auth_name of this AdvancedConfig.
        :type proxy_auth_name: str
        """
        self._proxy_auth_name = proxy_auth_name

    @property
    def proxy_auth_password(self):
        r"""Gets the proxy_auth_password of this AdvancedConfig.

        代理密码

        :return: The proxy_auth_password of this AdvancedConfig.
        :rtype: str
        """
        return self._proxy_auth_password

    @proxy_auth_password.setter
    def proxy_auth_password(self, proxy_auth_password):
        r"""Sets the proxy_auth_password of this AdvancedConfig.

        代理密码

        :param proxy_auth_password: The proxy_auth_password of this AdvancedConfig.
        :type proxy_auth_password: str
        """
        self._proxy_auth_password = proxy_auth_password

    @property
    def proxy_host_name(self):
        r"""Gets the proxy_host_name of this AdvancedConfig.

        代理服务配置

        :return: The proxy_host_name of this AdvancedConfig.
        :rtype: str
        """
        return self._proxy_host_name

    @proxy_host_name.setter
    def proxy_host_name(self, proxy_host_name):
        r"""Sets the proxy_host_name of this AdvancedConfig.

        代理服务配置

        :param proxy_host_name: The proxy_host_name of this AdvancedConfig.
        :type proxy_host_name: str
        """
        self._proxy_host_name = proxy_host_name

    @property
    def proxy_port(self):
        r"""Gets the proxy_port of this AdvancedConfig.

        代理服务配置

        :return: The proxy_port of this AdvancedConfig.
        :rtype: str
        """
        return self._proxy_port

    @proxy_port.setter
    def proxy_port(self, proxy_port):
        r"""Sets the proxy_port of this AdvancedConfig.

        代理服务配置

        :param proxy_port: The proxy_port of this AdvancedConfig.
        :type proxy_port: str
        """
        self._proxy_port = proxy_port

    @property
    def serial_run(self):
        r"""Gets the serial_run of this AdvancedConfig.

        串行配置

        :return: The serial_run of this AdvancedConfig.
        :rtype: str
        """
        return self._serial_run

    @serial_run.setter
    def serial_run(self, serial_run):
        r"""Sets the serial_run of this AdvancedConfig.

        串行配置

        :param serial_run: The serial_run of this AdvancedConfig.
        :type serial_run: str
        """
        self._serial_run = serial_run

    @property
    def task_stop_time(self):
        r"""Gets the task_stop_time of this AdvancedConfig.

        任务停止时间

        :return: The task_stop_time of this AdvancedConfig.
        :rtype: datetime
        """
        return self._task_stop_time

    @task_stop_time.setter
    def task_stop_time(self, task_stop_time):
        r"""Sets the task_stop_time of this AdvancedConfig.

        任务停止时间

        :param task_stop_time: The task_stop_time of this AdvancedConfig.
        :type task_stop_time: datetime
        """
        self._task_stop_time = task_stop_time

    @property
    def task_timeout(self):
        r"""Gets the task_timeout of this AdvancedConfig.

        任务超时时间

        :return: The task_timeout of this AdvancedConfig.
        :rtype: int
        """
        return self._task_timeout

    @task_timeout.setter
    def task_timeout(self, task_timeout):
        r"""Sets the task_timeout of this AdvancedConfig.

        任务超时时间

        :param task_timeout: The task_timeout of this AdvancedConfig.
        :type task_timeout: int
        """
        self._task_timeout = task_timeout

    def to_dict(self):
        result = {}

        for attr, _ in self.openapi_types.items():
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
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, AdvancedConfig):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

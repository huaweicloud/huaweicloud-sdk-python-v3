# coding: utf-8

import pprint
import re

import six





class HealthmonitorResp:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'id': 'str',
        'project_id': 'str',
        'tenant_id': 'str',
        'name': 'str',
        'admin_state_up': 'bool',
        'monitor_port': 'int',
        'timeout': 'int',
        'type': 'str',
        'expected_codes': 'str',
        'domain_name': 'str',
        'url_path': 'str',
        'http_method': 'str',
        'delay': 'int',
        'max_retries': 'int',
        'pools': 'list[ResourceList]'
    }

    attribute_map = {
        'id': 'id',
        'project_id': 'project_id',
        'tenant_id': 'tenant_id',
        'name': 'name',
        'admin_state_up': 'admin_state_up',
        'monitor_port': 'monitor_port',
        'timeout': 'timeout',
        'type': 'type',
        'expected_codes': 'expected_codes',
        'domain_name': 'domain_name',
        'url_path': 'url_path',
        'http_method': 'http_method',
        'delay': 'delay',
        'max_retries': 'max_retries',
        'pools': 'pools'
    }

    def __init__(self, id=None, project_id=None, tenant_id=None, name=None, admin_state_up=None, monitor_port=None, timeout=None, type=None, expected_codes=None, domain_name=None, url_path=None, http_method=None, delay=None, max_retries=None, pools=None):
        """HealthmonitorResp - a model defined in huaweicloud sdk"""
        
        

        self._id = None
        self._project_id = None
        self._tenant_id = None
        self._name = None
        self._admin_state_up = None
        self._monitor_port = None
        self._timeout = None
        self._type = None
        self._expected_codes = None
        self._domain_name = None
        self._url_path = None
        self._http_method = None
        self._delay = None
        self._max_retries = None
        self._pools = None
        self.discriminator = None

        self.id = id
        self.project_id = project_id
        self.tenant_id = tenant_id
        self.name = name
        self.admin_state_up = admin_state_up
        self.monitor_port = monitor_port
        self.timeout = timeout
        self.type = type
        self.expected_codes = expected_codes
        self.domain_name = domain_name
        self.url_path = url_path
        self.http_method = http_method
        self.delay = delay
        self.max_retries = max_retries
        self.pools = pools

    @property
    def id(self):
        """Gets the id of this HealthmonitorResp.

        健康检查ID

        :return: The id of this HealthmonitorResp.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this HealthmonitorResp.

        健康检查ID

        :param id: The id of this HealthmonitorResp.
        :type: str
        """
        self._id = id

    @property
    def project_id(self):
        """Gets the project_id of this HealthmonitorResp.

        健康检查所在的项目ID。

        :return: The project_id of this HealthmonitorResp.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """Sets the project_id of this HealthmonitorResp.

        健康检查所在的项目ID。

        :param project_id: The project_id of this HealthmonitorResp.
        :type: str
        """
        self._project_id = project_id

    @property
    def tenant_id(self):
        """Gets the tenant_id of this HealthmonitorResp.

        健康检查所在的项目ID。

        :return: The tenant_id of this HealthmonitorResp.
        :rtype: str
        """
        return self._tenant_id

    @tenant_id.setter
    def tenant_id(self, tenant_id):
        """Sets the tenant_id of this HealthmonitorResp.

        健康检查所在的项目ID。

        :param tenant_id: The tenant_id of this HealthmonitorResp.
        :type: str
        """
        self._tenant_id = tenant_id

    @property
    def name(self):
        """Gets the name of this HealthmonitorResp.

        健康检查名称。

        :return: The name of this HealthmonitorResp.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this HealthmonitorResp.

        健康检查名称。

        :param name: The name of this HealthmonitorResp.
        :type: str
        """
        self._name = name

    @property
    def admin_state_up(self):
        """Gets the admin_state_up of this HealthmonitorResp.

        健康检查的管理状态；该字段虽然支持创建、更新，但实际取值决定于后端云服务器对应的弹性云服务器是否存在。该字段虽然支持创建、更新，但实际取值决定于member对应的弹性云服务器是否存在。若存在，该值为true，否则，该值为false。

        :return: The admin_state_up of this HealthmonitorResp.
        :rtype: bool
        """
        return self._admin_state_up

    @admin_state_up.setter
    def admin_state_up(self, admin_state_up):
        """Sets the admin_state_up of this HealthmonitorResp.

        健康检查的管理状态；该字段虽然支持创建、更新，但实际取值决定于后端云服务器对应的弹性云服务器是否存在。该字段虽然支持创建、更新，但实际取值决定于member对应的弹性云服务器是否存在。若存在，该值为true，否则，该值为false。

        :param admin_state_up: The admin_state_up of this HealthmonitorResp.
        :type: bool
        """
        self._admin_state_up = admin_state_up

    @property
    def monitor_port(self):
        """Gets the monitor_port of this HealthmonitorResp.

        健康检查端口号。默认为空，表示使用后端云服务器组的端口。

        :return: The monitor_port of this HealthmonitorResp.
        :rtype: int
        """
        return self._monitor_port

    @monitor_port.setter
    def monitor_port(self, monitor_port):
        """Sets the monitor_port of this HealthmonitorResp.

        健康检查端口号。默认为空，表示使用后端云服务器组的端口。

        :param monitor_port: The monitor_port of this HealthmonitorResp.
        :type: int
        """
        self._monitor_port = monitor_port

    @property
    def timeout(self):
        """Gets the timeout of this HealthmonitorResp.

        健康检查的超时时间。建议该值小于delay的值。

        :return: The timeout of this HealthmonitorResp.
        :rtype: int
        """
        return self._timeout

    @timeout.setter
    def timeout(self, timeout):
        """Sets the timeout of this HealthmonitorResp.

        健康检查的超时时间。建议该值小于delay的值。

        :param timeout: The timeout of this HealthmonitorResp.
        :type: int
        """
        self._timeout = timeout

    @property
    def type(self):
        """Gets the type of this HealthmonitorResp.

        健康检查类型

        :return: The type of this HealthmonitorResp.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this HealthmonitorResp.

        健康检查类型

        :param type: The type of this HealthmonitorResp.
        :type: str
        """
        self._type = type

    @property
    def expected_codes(self):
        """Gets the expected_codes of this HealthmonitorResp.

        期望HTTP响应状态码，指定下列值：单值，例如200；列表，例如200，202；区间，例如200-204。仅当type为HTTP时生效。该字段为预留字段，暂未启用。

        :return: The expected_codes of this HealthmonitorResp.
        :rtype: str
        """
        return self._expected_codes

    @expected_codes.setter
    def expected_codes(self, expected_codes):
        """Sets the expected_codes of this HealthmonitorResp.

        期望HTTP响应状态码，指定下列值：单值，例如200；列表，例如200，202；区间，例如200-204。仅当type为HTTP时生效。该字段为预留字段，暂未启用。

        :param expected_codes: The expected_codes of this HealthmonitorResp.
        :type: str
        """
        self._expected_codes = expected_codes

    @property
    def domain_name(self):
        """Gets the domain_name of this HealthmonitorResp.

        功能说明：健康检查测试member健康状态时，发送的http请求的域名。仅当type为HTTP时生效。使用说明：默认为空，表示使用负载均衡器的vip作为http请求的目的地址。以数字或字母开头，只能包含数字、字母、’-’、’.’。

        :return: The domain_name of this HealthmonitorResp.
        :rtype: str
        """
        return self._domain_name

    @domain_name.setter
    def domain_name(self, domain_name):
        """Sets the domain_name of this HealthmonitorResp.

        功能说明：健康检查测试member健康状态时，发送的http请求的域名。仅当type为HTTP时生效。使用说明：默认为空，表示使用负载均衡器的vip作为http请求的目的地址。以数字或字母开头，只能包含数字、字母、’-’、’.’。

        :param domain_name: The domain_name of this HealthmonitorResp.
        :type: str
        """
        self._domain_name = domain_name

    @property
    def url_path(self):
        """Gets the url_path of this HealthmonitorResp.

        HTTP方法，可以为GET、HEAD、POST、PUT、DELETE、TRACE、OPTIONS、CONNECT、PATCH。仅当type为HTTP时生效。该字段为预留字段，暂未启用。

        :return: The url_path of this HealthmonitorResp.
        :rtype: str
        """
        return self._url_path

    @url_path.setter
    def url_path(self, url_path):
        """Sets the url_path of this HealthmonitorResp.

        HTTP方法，可以为GET、HEAD、POST、PUT、DELETE、TRACE、OPTIONS、CONNECT、PATCH。仅当type为HTTP时生效。该字段为预留字段，暂未启用。

        :param url_path: The url_path of this HealthmonitorResp.
        :type: str
        """
        self._url_path = url_path

    @property
    def http_method(self):
        """Gets the http_method of this HealthmonitorResp.

        HTTP方法，可以为GET、HEAD、POST、PUT、DELETE、TRACE、OPTIONS、CONNECT、PATCH。仅当type为HTTP时生效。该字段为预留字段，暂未启用。

        :return: The http_method of this HealthmonitorResp.
        :rtype: str
        """
        return self._http_method

    @http_method.setter
    def http_method(self, http_method):
        """Sets the http_method of this HealthmonitorResp.

        HTTP方法，可以为GET、HEAD、POST、PUT、DELETE、TRACE、OPTIONS、CONNECT、PATCH。仅当type为HTTP时生效。该字段为预留字段，暂未启用。

        :param http_method: The http_method of this HealthmonitorResp.
        :type: str
        """
        self._http_method = http_method

    @property
    def delay(self):
        """Gets the delay of this HealthmonitorResp.

        健康检查间隔，单位秒

        :return: The delay of this HealthmonitorResp.
        :rtype: int
        """
        return self._delay

    @delay.setter
    def delay(self, delay):
        """Sets the delay of this HealthmonitorResp.

        健康检查间隔，单位秒

        :param delay: The delay of this HealthmonitorResp.
        :type: int
        """
        self._delay = delay

    @property
    def max_retries(self):
        """Gets the max_retries of this HealthmonitorResp.

        最大重试次数

        :return: The max_retries of this HealthmonitorResp.
        :rtype: int
        """
        return self._max_retries

    @max_retries.setter
    def max_retries(self, max_retries):
        """Sets the max_retries of this HealthmonitorResp.

        最大重试次数

        :param max_retries: The max_retries of this HealthmonitorResp.
        :type: int
        """
        self._max_retries = max_retries

    @property
    def pools(self):
        """Gets the pools of this HealthmonitorResp.

        健康检查关联的后端云服务器组列表

        :return: The pools of this HealthmonitorResp.
        :rtype: list[ResourceList]
        """
        return self._pools

    @pools.setter
    def pools(self, pools):
        """Sets the pools of this HealthmonitorResp.

        健康检查关联的后端云服务器组列表

        :param pools: The pools of this HealthmonitorResp.
        :type: list[ResourceList]
        """
        self._pools = pools

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
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, HealthmonitorResp):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

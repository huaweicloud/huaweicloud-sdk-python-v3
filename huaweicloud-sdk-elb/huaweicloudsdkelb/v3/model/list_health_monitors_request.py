# coding: utf-8

import pprint
import re

import six





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
        'admin_state_up': 'bool',
        'delay': 'list[int]',
        'domain_name': 'list[str]',
        'enterprise_project_id': 'list[str]',
        'expected_codes': 'list[str]',
        'http_method': 'list[str]',
        'id': 'list[str]',
        'limit': 'int',
        'marker': 'str',
        'max_retries': 'list[int]',
        'max_retries_down': 'list[int]',
        'monitor_port': 'list[int]',
        'name': 'list[str]',
        'page_reverse': 'bool',
        'timeout': 'int',
        'type': 'list[str]',
        'url_path': 'list[str]'
    }

    attribute_map = {
        'admin_state_up': 'admin_state_up',
        'delay': 'delay',
        'domain_name': 'domain_name',
        'enterprise_project_id': 'enterprise_project_id',
        'expected_codes': 'expected_codes',
        'http_method': 'http_method',
        'id': 'id',
        'limit': 'limit',
        'marker': 'marker',
        'max_retries': 'max_retries',
        'max_retries_down': 'max_retries_down',
        'monitor_port': 'monitor_port',
        'name': 'name',
        'page_reverse': 'page_reverse',
        'timeout': 'timeout',
        'type': 'type',
        'url_path': 'url_path'
    }

    def __init__(self, admin_state_up=None, delay=None, domain_name=None, enterprise_project_id=None, expected_codes=None, http_method=None, id=None, limit=None, marker=None, max_retries=None, max_retries_down=None, monitor_port=None, name=None, page_reverse=None, timeout=None, type=None, url_path=None):
        """ListHealthMonitorsRequest - a model defined in huaweicloud sdk"""
        
        

        self._admin_state_up = None
        self._delay = None
        self._domain_name = None
        self._enterprise_project_id = None
        self._expected_codes = None
        self._http_method = None
        self._id = None
        self._limit = None
        self._marker = None
        self._max_retries = None
        self._max_retries_down = None
        self._monitor_port = None
        self._name = None
        self._page_reverse = None
        self._timeout = None
        self._type = None
        self._url_path = None
        self.discriminator = None

        if admin_state_up is not None:
            self.admin_state_up = admin_state_up
        if delay is not None:
            self.delay = delay
        if domain_name is not None:
            self.domain_name = domain_name
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        if expected_codes is not None:
            self.expected_codes = expected_codes
        if http_method is not None:
            self.http_method = http_method
        if id is not None:
            self.id = id
        if limit is not None:
            self.limit = limit
        if marker is not None:
            self.marker = marker
        if max_retries is not None:
            self.max_retries = max_retries
        if max_retries_down is not None:
            self.max_retries_down = max_retries_down
        if monitor_port is not None:
            self.monitor_port = monitor_port
        if name is not None:
            self.name = name
        if page_reverse is not None:
            self.page_reverse = page_reverse
        if timeout is not None:
            self.timeout = timeout
        if type is not None:
            self.type = type
        if url_path is not None:
            self.url_path = url_path

    @property
    def admin_state_up(self):
        """Gets the admin_state_up of this ListHealthMonitorsRequest.

        健康检查的管理状态；该字段虽然支持创建、更新，但实际取值决定于后端云服务器对应的弹性云服务器是否存在。该字段虽然支持创建、更新，但实际取值决定于member对应的弹性云服务器是否存在。若存在，该值为true，否则，该值为false。

        :return: The admin_state_up of this ListHealthMonitorsRequest.
        :rtype: bool
        """
        return self._admin_state_up

    @admin_state_up.setter
    def admin_state_up(self, admin_state_up):
        """Sets the admin_state_up of this ListHealthMonitorsRequest.

        健康检查的管理状态；该字段虽然支持创建、更新，但实际取值决定于后端云服务器对应的弹性云服务器是否存在。该字段虽然支持创建、更新，但实际取值决定于member对应的弹性云服务器是否存在。若存在，该值为true，否则，该值为false。

        :param admin_state_up: The admin_state_up of this ListHealthMonitorsRequest.
        :type: bool
        """
        self._admin_state_up = admin_state_up

    @property
    def delay(self):
        """Gets the delay of this ListHealthMonitorsRequest.

        健康检查间隔。

        :return: The delay of this ListHealthMonitorsRequest.
        :rtype: list[int]
        """
        return self._delay

    @delay.setter
    def delay(self, delay):
        """Sets the delay of this ListHealthMonitorsRequest.

        健康检查间隔。

        :param delay: The delay of this ListHealthMonitorsRequest.
        :type: list[int]
        """
        self._delay = delay

    @property
    def domain_name(self):
        """Gets the domain_name of this ListHealthMonitorsRequest.

        功能说明：健康检查测试member健康状态时，发送的http请求的域名。仅当type为HTTP时生效。使用说明：默认为空，表示使用负载均衡器的vip作为http请求的目的地址。以数字或字母开头，只能包含数字、字母、’-’、’.’。

        :return: The domain_name of this ListHealthMonitorsRequest.
        :rtype: list[str]
        """
        return self._domain_name

    @domain_name.setter
    def domain_name(self, domain_name):
        """Sets the domain_name of this ListHealthMonitorsRequest.

        功能说明：健康检查测试member健康状态时，发送的http请求的域名。仅当type为HTTP时生效。使用说明：默认为空，表示使用负载均衡器的vip作为http请求的目的地址。以数字或字母开头，只能包含数字、字母、’-’、’.’。

        :param domain_name: The domain_name of this ListHealthMonitorsRequest.
        :type: list[str]
        """
        self._domain_name = domain_name

    @property
    def enterprise_project_id(self):
        """Gets the enterprise_project_id of this ListHealthMonitorsRequest.

        企业项目ID。

        :return: The enterprise_project_id of this ListHealthMonitorsRequest.
        :rtype: list[str]
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        """Sets the enterprise_project_id of this ListHealthMonitorsRequest.

        企业项目ID。

        :param enterprise_project_id: The enterprise_project_id of this ListHealthMonitorsRequest.
        :type: list[str]
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def expected_codes(self):
        """Gets the expected_codes of this ListHealthMonitorsRequest.

        期望HTTP响应状态码，指定下列值：单值，例如200；列表，例如200，202；区间，例如200-204。仅当type为HTTP时生效。该字段为预留字段，暂未启用。

        :return: The expected_codes of this ListHealthMonitorsRequest.
        :rtype: list[str]
        """
        return self._expected_codes

    @expected_codes.setter
    def expected_codes(self, expected_codes):
        """Sets the expected_codes of this ListHealthMonitorsRequest.

        期望HTTP响应状态码，指定下列值：单值，例如200；列表，例如200，202；区间，例如200-204。仅当type为HTTP时生效。该字段为预留字段，暂未启用。

        :param expected_codes: The expected_codes of this ListHealthMonitorsRequest.
        :type: list[str]
        """
        self._expected_codes = expected_codes

    @property
    def http_method(self):
        """Gets the http_method of this ListHealthMonitorsRequest.

        HTTP方法，可以为GET、HEAD、POST、PUT、DELETE、TRACE、OPTIONS、CONNECT、PATCH。仅当type为HTTP时生效。该字段为预留字段，暂未启用。

        :return: The http_method of this ListHealthMonitorsRequest.
        :rtype: list[str]
        """
        return self._http_method

    @http_method.setter
    def http_method(self, http_method):
        """Sets the http_method of this ListHealthMonitorsRequest.

        HTTP方法，可以为GET、HEAD、POST、PUT、DELETE、TRACE、OPTIONS、CONNECT、PATCH。仅当type为HTTP时生效。该字段为预留字段，暂未启用。

        :param http_method: The http_method of this ListHealthMonitorsRequest.
        :type: list[str]
        """
        self._http_method = http_method

    @property
    def id(self):
        """Gets the id of this ListHealthMonitorsRequest.

        健康检查ID。

        :return: The id of this ListHealthMonitorsRequest.
        :rtype: list[str]
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ListHealthMonitorsRequest.

        健康检查ID。

        :param id: The id of this ListHealthMonitorsRequest.
        :type: list[str]
        """
        self._id = id

    @property
    def limit(self):
        """Gets the limit of this ListHealthMonitorsRequest.

        每页返回的个数。

        :return: The limit of this ListHealthMonitorsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListHealthMonitorsRequest.

        每页返回的个数。

        :param limit: The limit of this ListHealthMonitorsRequest.
        :type: int
        """
        self._limit = limit

    @property
    def marker(self):
        """Gets the marker of this ListHealthMonitorsRequest.

        上一页最后一条记录的ID。  使用说明：  - 必须与limit一起使用。 - 不指定时表示查询第一页。 - 该字段不允许为空或无效的ID。

        :return: The marker of this ListHealthMonitorsRequest.
        :rtype: str
        """
        return self._marker

    @marker.setter
    def marker(self, marker):
        """Sets the marker of this ListHealthMonitorsRequest.

        上一页最后一条记录的ID。  使用说明：  - 必须与limit一起使用。 - 不指定时表示查询第一页。 - 该字段不允许为空或无效的ID。

        :param marker: The marker of this ListHealthMonitorsRequest.
        :type: str
        """
        self._marker = marker

    @property
    def max_retries(self):
        """Gets the max_retries of this ListHealthMonitorsRequest.

        最大重试次数。

        :return: The max_retries of this ListHealthMonitorsRequest.
        :rtype: list[int]
        """
        return self._max_retries

    @max_retries.setter
    def max_retries(self, max_retries):
        """Sets the max_retries of this ListHealthMonitorsRequest.

        最大重试次数。

        :param max_retries: The max_retries of this ListHealthMonitorsRequest.
        :type: list[int]
        """
        self._max_retries = max_retries

    @property
    def max_retries_down(self):
        """Gets the max_retries_down of this ListHealthMonitorsRequest.

        健康检查连续成功多少次后，将后端服务器的健康检查状态由ONLINE判定为OFFLINE，取值范围[1，10]。

        :return: The max_retries_down of this ListHealthMonitorsRequest.
        :rtype: list[int]
        """
        return self._max_retries_down

    @max_retries_down.setter
    def max_retries_down(self, max_retries_down):
        """Sets the max_retries_down of this ListHealthMonitorsRequest.

        健康检查连续成功多少次后，将后端服务器的健康检查状态由ONLINE判定为OFFLINE，取值范围[1，10]。

        :param max_retries_down: The max_retries_down of this ListHealthMonitorsRequest.
        :type: list[int]
        """
        self._max_retries_down = max_retries_down

    @property
    def monitor_port(self):
        """Gets the monitor_port of this ListHealthMonitorsRequest.

        健康检查端口号。

        :return: The monitor_port of this ListHealthMonitorsRequest.
        :rtype: list[int]
        """
        return self._monitor_port

    @monitor_port.setter
    def monitor_port(self, monitor_port):
        """Sets the monitor_port of this ListHealthMonitorsRequest.

        健康检查端口号。

        :param monitor_port: The monitor_port of this ListHealthMonitorsRequest.
        :type: list[int]
        """
        self._monitor_port = monitor_port

    @property
    def name(self):
        """Gets the name of this ListHealthMonitorsRequest.

        健康检查名称。

        :return: The name of this ListHealthMonitorsRequest.
        :rtype: list[str]
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ListHealthMonitorsRequest.

        健康检查名称。

        :param name: The name of this ListHealthMonitorsRequest.
        :type: list[str]
        """
        self._name = name

    @property
    def page_reverse(self):
        """Gets the page_reverse of this ListHealthMonitorsRequest.

        分页的顺序，true表示从后往前分页，false表示从前往后分页，默认为false。 使用说明：必须与limit一起使用。

        :return: The page_reverse of this ListHealthMonitorsRequest.
        :rtype: bool
        """
        return self._page_reverse

    @page_reverse.setter
    def page_reverse(self, page_reverse):
        """Sets the page_reverse of this ListHealthMonitorsRequest.

        分页的顺序，true表示从后往前分页，false表示从前往后分页，默认为false。 使用说明：必须与limit一起使用。

        :param page_reverse: The page_reverse of this ListHealthMonitorsRequest.
        :type: bool
        """
        self._page_reverse = page_reverse

    @property
    def timeout(self):
        """Gets the timeout of this ListHealthMonitorsRequest.

        健康检查的超时时间。建议该值小于delay的值。

        :return: The timeout of this ListHealthMonitorsRequest.
        :rtype: int
        """
        return self._timeout

    @timeout.setter
    def timeout(self, timeout):
        """Sets the timeout of this ListHealthMonitorsRequest.

        健康检查的超时时间。建议该值小于delay的值。

        :param timeout: The timeout of this ListHealthMonitorsRequest.
        :type: int
        """
        self._timeout = timeout

    @property
    def type(self):
        """Gets the type of this ListHealthMonitorsRequest.

        健康检查类型。

        :return: The type of this ListHealthMonitorsRequest.
        :rtype: list[str]
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this ListHealthMonitorsRequest.

        健康检查类型。

        :param type: The type of this ListHealthMonitorsRequest.
        :type: list[str]
        """
        self._type = type

    @property
    def url_path(self):
        """Gets the url_path of this ListHealthMonitorsRequest.

        功能说明：健康检查测试member健康时发送的http请求路径。默认为“/”。使用说明：以“/”开头。仅当type为HTTP时生效。

        :return: The url_path of this ListHealthMonitorsRequest.
        :rtype: list[str]
        """
        return self._url_path

    @url_path.setter
    def url_path(self, url_path):
        """Sets the url_path of this ListHealthMonitorsRequest.

        功能说明：健康检查测试member健康时发送的http请求路径。默认为“/”。使用说明：以“/”开头。仅当type为HTTP时生效。

        :param url_path: The url_path of this ListHealthMonitorsRequest.
        :type: list[str]
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
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ListHealthMonitorsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

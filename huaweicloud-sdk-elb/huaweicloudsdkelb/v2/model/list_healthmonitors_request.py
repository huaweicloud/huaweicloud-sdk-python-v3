# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListHealthmonitorsRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'limit': 'int',
        'marker': 'str',
        'page_reverse': 'bool',
        'id': 'str',
        'name': 'str',
        'delay': 'int',
        'max_retries': 'int',
        'admin_state_up': 'bool',
        'timeout': 'int',
        'type': 'str',
        'monitor_port': 'int',
        'expected_codes': 'str',
        'domain_name': 'str',
        'url_path': 'str',
        'http_method': 'str'
    }

    attribute_map = {
        'limit': 'limit',
        'marker': 'marker',
        'page_reverse': 'page_reverse',
        'id': 'id',
        'name': 'name',
        'delay': 'delay',
        'max_retries': 'max_retries',
        'admin_state_up': 'admin_state_up',
        'timeout': 'timeout',
        'type': 'type',
        'monitor_port': 'monitor_port',
        'expected_codes': 'expected_codes',
        'domain_name': 'domain_name',
        'url_path': 'url_path',
        'http_method': 'http_method'
    }

    def __init__(self, limit=None, marker=None, page_reverse=None, id=None, name=None, delay=None, max_retries=None, admin_state_up=None, timeout=None, type=None, monitor_port=None, expected_codes=None, domain_name=None, url_path=None, http_method=None):
        """ListHealthmonitorsRequest

        The model defined in huaweicloud sdk

        :param limit: 分页查询中每页的健康检查个数
        :type limit: int
        :param marker: 分页查询的起始的资源id，表示上一页最后一条查询记录的健康检查的id。不指定时表示查询第一页。
        :type marker: str
        :param page_reverse: 分页的顺序，true表示从后往前分页，false表示从前往后分页，默认为false。
        :type page_reverse: bool
        :param id: 健康检查ID。
        :type id: str
        :param name: 健康检查名称。
        :type name: str
        :param delay: 健康检查间隔，单位秒，取值范围[1，50]。
        :type delay: int
        :param max_retries: 健康检查最大重试次数，取值范围[1，10]。
        :type max_retries: int
        :param admin_state_up: 健康检查的管理状态。取值范围：true/false。默认为true；true表示开启健康检查；false表示关闭健康检查。
        :type admin_state_up: bool
        :param timeout: 健康检查超时时间，单位秒，取值范围[1，50]。 建议该值小于delay的值。
        :type timeout: int
        :param type: 健康检查的类型。取值范围：TCP、UDP_CONNECT、HTTP。
        :type type: str
        :param monitor_port: 健康检查端口号]。默认为空，表示使用后端云服务器的protocol_port作为健康检查的检查端口。
        :type monitor_port: int
        :param expected_codes: 期望HTTP响应状态码；默认值：“200”。取值范围：单值，例如200；列表，例如200，202；区间，例如200-204。仅当type为HTTP时生效。 该字段为预留字段，暂未启用。
        :type expected_codes: str
        :param domain_name: 健康检查时，发送的http请求的域名。仅当type为HTTP时生效。默认为空，表示使用负载均衡器的vip_address作为http请求的目的地址。以数字或字母开头，只能包含数字、字母、’-’、’.’。例如：www.huaweitest.com
        :type domain_name: str
        :param url_path: 健康检查时发送的http请求路径。默认为“/”。以“/”开头。仅当type为HTTP时生效。例如：“/test”
        :type url_path: str
        :param http_method: HTTP请求的方法；默认值：GET取值范围：GET、HEAD、POST、PUT、DELETE、TRACE、OPTIONS、CONNECT、PATCH。仅当type为HTTP时生效。
        :type http_method: str
        """
        
        

        self._limit = None
        self._marker = None
        self._page_reverse = None
        self._id = None
        self._name = None
        self._delay = None
        self._max_retries = None
        self._admin_state_up = None
        self._timeout = None
        self._type = None
        self._monitor_port = None
        self._expected_codes = None
        self._domain_name = None
        self._url_path = None
        self._http_method = None
        self.discriminator = None

        if limit is not None:
            self.limit = limit
        if marker is not None:
            self.marker = marker
        if page_reverse is not None:
            self.page_reverse = page_reverse
        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if delay is not None:
            self.delay = delay
        if max_retries is not None:
            self.max_retries = max_retries
        if admin_state_up is not None:
            self.admin_state_up = admin_state_up
        if timeout is not None:
            self.timeout = timeout
        if type is not None:
            self.type = type
        if monitor_port is not None:
            self.monitor_port = monitor_port
        if expected_codes is not None:
            self.expected_codes = expected_codes
        if domain_name is not None:
            self.domain_name = domain_name
        if url_path is not None:
            self.url_path = url_path
        if http_method is not None:
            self.http_method = http_method

    @property
    def limit(self):
        """Gets the limit of this ListHealthmonitorsRequest.

        分页查询中每页的健康检查个数

        :return: The limit of this ListHealthmonitorsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListHealthmonitorsRequest.

        分页查询中每页的健康检查个数

        :param limit: The limit of this ListHealthmonitorsRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def marker(self):
        """Gets the marker of this ListHealthmonitorsRequest.

        分页查询的起始的资源id，表示上一页最后一条查询记录的健康检查的id。不指定时表示查询第一页。

        :return: The marker of this ListHealthmonitorsRequest.
        :rtype: str
        """
        return self._marker

    @marker.setter
    def marker(self, marker):
        """Sets the marker of this ListHealthmonitorsRequest.

        分页查询的起始的资源id，表示上一页最后一条查询记录的健康检查的id。不指定时表示查询第一页。

        :param marker: The marker of this ListHealthmonitorsRequest.
        :type marker: str
        """
        self._marker = marker

    @property
    def page_reverse(self):
        """Gets the page_reverse of this ListHealthmonitorsRequest.

        分页的顺序，true表示从后往前分页，false表示从前往后分页，默认为false。

        :return: The page_reverse of this ListHealthmonitorsRequest.
        :rtype: bool
        """
        return self._page_reverse

    @page_reverse.setter
    def page_reverse(self, page_reverse):
        """Sets the page_reverse of this ListHealthmonitorsRequest.

        分页的顺序，true表示从后往前分页，false表示从前往后分页，默认为false。

        :param page_reverse: The page_reverse of this ListHealthmonitorsRequest.
        :type page_reverse: bool
        """
        self._page_reverse = page_reverse

    @property
    def id(self):
        """Gets the id of this ListHealthmonitorsRequest.

        健康检查ID。

        :return: The id of this ListHealthmonitorsRequest.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ListHealthmonitorsRequest.

        健康检查ID。

        :param id: The id of this ListHealthmonitorsRequest.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        """Gets the name of this ListHealthmonitorsRequest.

        健康检查名称。

        :return: The name of this ListHealthmonitorsRequest.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ListHealthmonitorsRequest.

        健康检查名称。

        :param name: The name of this ListHealthmonitorsRequest.
        :type name: str
        """
        self._name = name

    @property
    def delay(self):
        """Gets the delay of this ListHealthmonitorsRequest.

        健康检查间隔，单位秒，取值范围[1，50]。

        :return: The delay of this ListHealthmonitorsRequest.
        :rtype: int
        """
        return self._delay

    @delay.setter
    def delay(self, delay):
        """Sets the delay of this ListHealthmonitorsRequest.

        健康检查间隔，单位秒，取值范围[1，50]。

        :param delay: The delay of this ListHealthmonitorsRequest.
        :type delay: int
        """
        self._delay = delay

    @property
    def max_retries(self):
        """Gets the max_retries of this ListHealthmonitorsRequest.

        健康检查最大重试次数，取值范围[1，10]。

        :return: The max_retries of this ListHealthmonitorsRequest.
        :rtype: int
        """
        return self._max_retries

    @max_retries.setter
    def max_retries(self, max_retries):
        """Sets the max_retries of this ListHealthmonitorsRequest.

        健康检查最大重试次数，取值范围[1，10]。

        :param max_retries: The max_retries of this ListHealthmonitorsRequest.
        :type max_retries: int
        """
        self._max_retries = max_retries

    @property
    def admin_state_up(self):
        """Gets the admin_state_up of this ListHealthmonitorsRequest.

        健康检查的管理状态。取值范围：true/false。默认为true；true表示开启健康检查；false表示关闭健康检查。

        :return: The admin_state_up of this ListHealthmonitorsRequest.
        :rtype: bool
        """
        return self._admin_state_up

    @admin_state_up.setter
    def admin_state_up(self, admin_state_up):
        """Sets the admin_state_up of this ListHealthmonitorsRequest.

        健康检查的管理状态。取值范围：true/false。默认为true；true表示开启健康检查；false表示关闭健康检查。

        :param admin_state_up: The admin_state_up of this ListHealthmonitorsRequest.
        :type admin_state_up: bool
        """
        self._admin_state_up = admin_state_up

    @property
    def timeout(self):
        """Gets the timeout of this ListHealthmonitorsRequest.

        健康检查超时时间，单位秒，取值范围[1，50]。 建议该值小于delay的值。

        :return: The timeout of this ListHealthmonitorsRequest.
        :rtype: int
        """
        return self._timeout

    @timeout.setter
    def timeout(self, timeout):
        """Sets the timeout of this ListHealthmonitorsRequest.

        健康检查超时时间，单位秒，取值范围[1，50]。 建议该值小于delay的值。

        :param timeout: The timeout of this ListHealthmonitorsRequest.
        :type timeout: int
        """
        self._timeout = timeout

    @property
    def type(self):
        """Gets the type of this ListHealthmonitorsRequest.

        健康检查的类型。取值范围：TCP、UDP_CONNECT、HTTP。

        :return: The type of this ListHealthmonitorsRequest.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this ListHealthmonitorsRequest.

        健康检查的类型。取值范围：TCP、UDP_CONNECT、HTTP。

        :param type: The type of this ListHealthmonitorsRequest.
        :type type: str
        """
        self._type = type

    @property
    def monitor_port(self):
        """Gets the monitor_port of this ListHealthmonitorsRequest.

        健康检查端口号]。默认为空，表示使用后端云服务器的protocol_port作为健康检查的检查端口。

        :return: The monitor_port of this ListHealthmonitorsRequest.
        :rtype: int
        """
        return self._monitor_port

    @monitor_port.setter
    def monitor_port(self, monitor_port):
        """Sets the monitor_port of this ListHealthmonitorsRequest.

        健康检查端口号]。默认为空，表示使用后端云服务器的protocol_port作为健康检查的检查端口。

        :param monitor_port: The monitor_port of this ListHealthmonitorsRequest.
        :type monitor_port: int
        """
        self._monitor_port = monitor_port

    @property
    def expected_codes(self):
        """Gets the expected_codes of this ListHealthmonitorsRequest.

        期望HTTP响应状态码；默认值：“200”。取值范围：单值，例如200；列表，例如200，202；区间，例如200-204。仅当type为HTTP时生效。 该字段为预留字段，暂未启用。

        :return: The expected_codes of this ListHealthmonitorsRequest.
        :rtype: str
        """
        return self._expected_codes

    @expected_codes.setter
    def expected_codes(self, expected_codes):
        """Sets the expected_codes of this ListHealthmonitorsRequest.

        期望HTTP响应状态码；默认值：“200”。取值范围：单值，例如200；列表，例如200，202；区间，例如200-204。仅当type为HTTP时生效。 该字段为预留字段，暂未启用。

        :param expected_codes: The expected_codes of this ListHealthmonitorsRequest.
        :type expected_codes: str
        """
        self._expected_codes = expected_codes

    @property
    def domain_name(self):
        """Gets the domain_name of this ListHealthmonitorsRequest.

        健康检查时，发送的http请求的域名。仅当type为HTTP时生效。默认为空，表示使用负载均衡器的vip_address作为http请求的目的地址。以数字或字母开头，只能包含数字、字母、’-’、’.’。例如：www.huaweitest.com

        :return: The domain_name of this ListHealthmonitorsRequest.
        :rtype: str
        """
        return self._domain_name

    @domain_name.setter
    def domain_name(self, domain_name):
        """Sets the domain_name of this ListHealthmonitorsRequest.

        健康检查时，发送的http请求的域名。仅当type为HTTP时生效。默认为空，表示使用负载均衡器的vip_address作为http请求的目的地址。以数字或字母开头，只能包含数字、字母、’-’、’.’。例如：www.huaweitest.com

        :param domain_name: The domain_name of this ListHealthmonitorsRequest.
        :type domain_name: str
        """
        self._domain_name = domain_name

    @property
    def url_path(self):
        """Gets the url_path of this ListHealthmonitorsRequest.

        健康检查时发送的http请求路径。默认为“/”。以“/”开头。仅当type为HTTP时生效。例如：“/test”

        :return: The url_path of this ListHealthmonitorsRequest.
        :rtype: str
        """
        return self._url_path

    @url_path.setter
    def url_path(self, url_path):
        """Sets the url_path of this ListHealthmonitorsRequest.

        健康检查时发送的http请求路径。默认为“/”。以“/”开头。仅当type为HTTP时生效。例如：“/test”

        :param url_path: The url_path of this ListHealthmonitorsRequest.
        :type url_path: str
        """
        self._url_path = url_path

    @property
    def http_method(self):
        """Gets the http_method of this ListHealthmonitorsRequest.

        HTTP请求的方法；默认值：GET取值范围：GET、HEAD、POST、PUT、DELETE、TRACE、OPTIONS、CONNECT、PATCH。仅当type为HTTP时生效。

        :return: The http_method of this ListHealthmonitorsRequest.
        :rtype: str
        """
        return self._http_method

    @http_method.setter
    def http_method(self, http_method):
        """Sets the http_method of this ListHealthmonitorsRequest.

        HTTP请求的方法；默认值：GET取值范围：GET、HEAD、POST、PUT、DELETE、TRACE、OPTIONS、CONNECT、PATCH。仅当type为HTTP时生效。

        :param http_method: The http_method of this ListHealthmonitorsRequest.
        :type http_method: str
        """
        self._http_method = http_method

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
        if not isinstance(other, ListHealthmonitorsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

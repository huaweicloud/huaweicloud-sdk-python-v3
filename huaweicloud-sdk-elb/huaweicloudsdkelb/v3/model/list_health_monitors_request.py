# coding: utf-8

import re
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
        """ListHealthMonitorsRequest

        The model defined in huaweicloud sdk

        :param marker: 上一页最后一条记录的ID。  使用说明： - 必须与limit一起使用。 - 不指定时表示查询第一页。 - 该字段不允许为空或无效的ID。
        :type marker: str
        :param limit: 每页返回的个数。
        :type limit: int
        :param page_reverse: 是否反向查询。  取值： - true：查询上一页。 - false：查询下一页，默认。  使用说明： - 必须与limit一起使用。 - 当page_reverse&#x3D;true时，若要查询上一页，marker取值为当前页返回值的previous_marker。
        :type page_reverse: bool
        :param id: 健康检查ID。  支持多值查询，查询条件格式：*id&#x3D;xxx&amp;id&#x3D;xxx****。
        :type id: list[str]
        :param monitor_port: 健康检查端口号。  支持多值查询，查询条件格式：***monitor_port&#x3D;xxx&amp;monitor_port&#x3D;xxx***。
        :type monitor_port: list[int]
        :param domain_name: 发送健康检查请求的域名。  取值：以数字或字母开头，只能包含数字、字母、’-’、’.’。  支持多值查询，查询条件格式：**domain_name&#x3D;xxx&amp;domain_name&#x3D;xxx**。
        :type domain_name: list[str]
        :param name: 健康检查名称。  支持多值查询，查询条件格式：*name&#x3D;xxx&amp;name&#x3D;xxx*。
        :type name: list[str]
        :param delay: 健康检查间隔。  取值：1-50s。  支持多值查询，查询条件格式：*delay&#x3D;xxx&amp;delay&#x3D;xxx*。
        :type delay: list[int]
        :param max_retries: 健康检查连续成功多少次后，将后端服务器的健康检查状态由OFFLINE判定为ONLINE。取值范围：1-10。  支持多值查询，查询条件格式：*******max_retries&#x3D;xxx&amp;max_retries&#x3D;xxx*******。
        :type max_retries: list[int]
        :param admin_state_up: 健康检查的管理状态。  取值： - true：表示开启健康检查，默认为true。 - false表示关闭健康检查。
        :type admin_state_up: bool
        :param max_retries_down: 健康检查连续失败多少次后，将后端服务器的健康检查状态由ONLINE判定为OFFLINE。取值范围：1-10。  支持多值查询，查询条件格式：******max_retries_down&#x3D;xxx&amp;max_retries_down&#x3D;xxx******。
        :type max_retries_down: list[int]
        :param timeout: 一次健康检查请求的超时时间。
        :type timeout: int
        :param type: 健康检查请求协议。  取值：TCP、UDP_CONNECT、HTTP、HTTPS。  支持多值查询，查询条件格式：*****type&#x3D;xxx&amp;type&#x3D;xxx*****。
        :type type: list[str]
        :param expected_codes: 期望响应状态码。  取值： - 单值：单个返回码，例如200。 - 列表：多个特定返回码，例如200，202。 - 区间：一个返回码区间，例如200-204。   默认值：200。  仅支持HTTP/HTTPS设置该字段，其他协议设置不会生效。  支持多值查询，查询条件格式：****expected_codes&#x3D;xxx&amp;expected_codes&#x3D;xxx****。
        :type expected_codes: list[str]
        :param url_path: 健康检查测试member健康时发送的http请求路径。默认为“/”。  使用说明：以“/”开头。当type为HTTP/HTTPS时生效。  支持多值查询，查询条件格式：***url_path&#x3D;xxx&amp;url_path&#x3D;xxx***。
        :type url_path: list[str]
        :param http_method: HTTP请求方法。  取值：GET、HEAD、POST、PUT、DELETE、TRACE、OPTIONS、CONNECT、PATCH。  支持多值查询，查询条件格式：**http_method&#x3D;xxx&amp;http_method&#x3D;xxx**。  不支持该字段，请勿使用。
        :type http_method: list[str]
        :param enterprise_project_id: 企业项目ID。不传时查询default企业项目\&quot;0\&quot;下的资源，鉴权按照default企业项目鉴权； 如果传值，则传已存在的企业项目ID或all_granted_eps（表示查询所有企业项目）进行查询。  支持多值查询，查询条件格式： *enterprise_project_id&#x3D;xxx&amp;enterprise_project_id&#x3D;xxx*。  [不支持该字段，请勿使用。](tag:dt,dt_test,hcso_dt)
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
        """Gets the marker of this ListHealthMonitorsRequest.

        上一页最后一条记录的ID。  使用说明： - 必须与limit一起使用。 - 不指定时表示查询第一页。 - 该字段不允许为空或无效的ID。

        :return: The marker of this ListHealthMonitorsRequest.
        :rtype: str
        """
        return self._marker

    @marker.setter
    def marker(self, marker):
        """Sets the marker of this ListHealthMonitorsRequest.

        上一页最后一条记录的ID。  使用说明： - 必须与limit一起使用。 - 不指定时表示查询第一页。 - 该字段不允许为空或无效的ID。

        :param marker: The marker of this ListHealthMonitorsRequest.
        :type marker: str
        """
        self._marker = marker

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
        :type limit: int
        """
        self._limit = limit

    @property
    def page_reverse(self):
        """Gets the page_reverse of this ListHealthMonitorsRequest.

        是否反向查询。  取值： - true：查询上一页。 - false：查询下一页，默认。  使用说明： - 必须与limit一起使用。 - 当page_reverse=true时，若要查询上一页，marker取值为当前页返回值的previous_marker。

        :return: The page_reverse of this ListHealthMonitorsRequest.
        :rtype: bool
        """
        return self._page_reverse

    @page_reverse.setter
    def page_reverse(self, page_reverse):
        """Sets the page_reverse of this ListHealthMonitorsRequest.

        是否反向查询。  取值： - true：查询上一页。 - false：查询下一页，默认。  使用说明： - 必须与limit一起使用。 - 当page_reverse=true时，若要查询上一页，marker取值为当前页返回值的previous_marker。

        :param page_reverse: The page_reverse of this ListHealthMonitorsRequest.
        :type page_reverse: bool
        """
        self._page_reverse = page_reverse

    @property
    def id(self):
        """Gets the id of this ListHealthMonitorsRequest.

        健康检查ID。  支持多值查询，查询条件格式：*id=xxx&id=xxx****。

        :return: The id of this ListHealthMonitorsRequest.
        :rtype: list[str]
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ListHealthMonitorsRequest.

        健康检查ID。  支持多值查询，查询条件格式：*id=xxx&id=xxx****。

        :param id: The id of this ListHealthMonitorsRequest.
        :type id: list[str]
        """
        self._id = id

    @property
    def monitor_port(self):
        """Gets the monitor_port of this ListHealthMonitorsRequest.

        健康检查端口号。  支持多值查询，查询条件格式：***monitor_port=xxx&monitor_port=xxx***。

        :return: The monitor_port of this ListHealthMonitorsRequest.
        :rtype: list[int]
        """
        return self._monitor_port

    @monitor_port.setter
    def monitor_port(self, monitor_port):
        """Sets the monitor_port of this ListHealthMonitorsRequest.

        健康检查端口号。  支持多值查询，查询条件格式：***monitor_port=xxx&monitor_port=xxx***。

        :param monitor_port: The monitor_port of this ListHealthMonitorsRequest.
        :type monitor_port: list[int]
        """
        self._monitor_port = monitor_port

    @property
    def domain_name(self):
        """Gets the domain_name of this ListHealthMonitorsRequest.

        发送健康检查请求的域名。  取值：以数字或字母开头，只能包含数字、字母、’-’、’.’。  支持多值查询，查询条件格式：**domain_name=xxx&domain_name=xxx**。

        :return: The domain_name of this ListHealthMonitorsRequest.
        :rtype: list[str]
        """
        return self._domain_name

    @domain_name.setter
    def domain_name(self, domain_name):
        """Sets the domain_name of this ListHealthMonitorsRequest.

        发送健康检查请求的域名。  取值：以数字或字母开头，只能包含数字、字母、’-’、’.’。  支持多值查询，查询条件格式：**domain_name=xxx&domain_name=xxx**。

        :param domain_name: The domain_name of this ListHealthMonitorsRequest.
        :type domain_name: list[str]
        """
        self._domain_name = domain_name

    @property
    def name(self):
        """Gets the name of this ListHealthMonitorsRequest.

        健康检查名称。  支持多值查询，查询条件格式：*name=xxx&name=xxx*。

        :return: The name of this ListHealthMonitorsRequest.
        :rtype: list[str]
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ListHealthMonitorsRequest.

        健康检查名称。  支持多值查询，查询条件格式：*name=xxx&name=xxx*。

        :param name: The name of this ListHealthMonitorsRequest.
        :type name: list[str]
        """
        self._name = name

    @property
    def delay(self):
        """Gets the delay of this ListHealthMonitorsRequest.

        健康检查间隔。  取值：1-50s。  支持多值查询，查询条件格式：*delay=xxx&delay=xxx*。

        :return: The delay of this ListHealthMonitorsRequest.
        :rtype: list[int]
        """
        return self._delay

    @delay.setter
    def delay(self, delay):
        """Sets the delay of this ListHealthMonitorsRequest.

        健康检查间隔。  取值：1-50s。  支持多值查询，查询条件格式：*delay=xxx&delay=xxx*。

        :param delay: The delay of this ListHealthMonitorsRequest.
        :type delay: list[int]
        """
        self._delay = delay

    @property
    def max_retries(self):
        """Gets the max_retries of this ListHealthMonitorsRequest.

        健康检查连续成功多少次后，将后端服务器的健康检查状态由OFFLINE判定为ONLINE。取值范围：1-10。  支持多值查询，查询条件格式：*******max_retries=xxx&max_retries=xxx*******。

        :return: The max_retries of this ListHealthMonitorsRequest.
        :rtype: list[int]
        """
        return self._max_retries

    @max_retries.setter
    def max_retries(self, max_retries):
        """Sets the max_retries of this ListHealthMonitorsRequest.

        健康检查连续成功多少次后，将后端服务器的健康检查状态由OFFLINE判定为ONLINE。取值范围：1-10。  支持多值查询，查询条件格式：*******max_retries=xxx&max_retries=xxx*******。

        :param max_retries: The max_retries of this ListHealthMonitorsRequest.
        :type max_retries: list[int]
        """
        self._max_retries = max_retries

    @property
    def admin_state_up(self):
        """Gets the admin_state_up of this ListHealthMonitorsRequest.

        健康检查的管理状态。  取值： - true：表示开启健康检查，默认为true。 - false表示关闭健康检查。

        :return: The admin_state_up of this ListHealthMonitorsRequest.
        :rtype: bool
        """
        return self._admin_state_up

    @admin_state_up.setter
    def admin_state_up(self, admin_state_up):
        """Sets the admin_state_up of this ListHealthMonitorsRequest.

        健康检查的管理状态。  取值： - true：表示开启健康检查，默认为true。 - false表示关闭健康检查。

        :param admin_state_up: The admin_state_up of this ListHealthMonitorsRequest.
        :type admin_state_up: bool
        """
        self._admin_state_up = admin_state_up

    @property
    def max_retries_down(self):
        """Gets the max_retries_down of this ListHealthMonitorsRequest.

        健康检查连续失败多少次后，将后端服务器的健康检查状态由ONLINE判定为OFFLINE。取值范围：1-10。  支持多值查询，查询条件格式：******max_retries_down=xxx&max_retries_down=xxx******。

        :return: The max_retries_down of this ListHealthMonitorsRequest.
        :rtype: list[int]
        """
        return self._max_retries_down

    @max_retries_down.setter
    def max_retries_down(self, max_retries_down):
        """Sets the max_retries_down of this ListHealthMonitorsRequest.

        健康检查连续失败多少次后，将后端服务器的健康检查状态由ONLINE判定为OFFLINE。取值范围：1-10。  支持多值查询，查询条件格式：******max_retries_down=xxx&max_retries_down=xxx******。

        :param max_retries_down: The max_retries_down of this ListHealthMonitorsRequest.
        :type max_retries_down: list[int]
        """
        self._max_retries_down = max_retries_down

    @property
    def timeout(self):
        """Gets the timeout of this ListHealthMonitorsRequest.

        一次健康检查请求的超时时间。

        :return: The timeout of this ListHealthMonitorsRequest.
        :rtype: int
        """
        return self._timeout

    @timeout.setter
    def timeout(self, timeout):
        """Sets the timeout of this ListHealthMonitorsRequest.

        一次健康检查请求的超时时间。

        :param timeout: The timeout of this ListHealthMonitorsRequest.
        :type timeout: int
        """
        self._timeout = timeout

    @property
    def type(self):
        """Gets the type of this ListHealthMonitorsRequest.

        健康检查请求协议。  取值：TCP、UDP_CONNECT、HTTP、HTTPS。  支持多值查询，查询条件格式：*****type=xxx&type=xxx*****。

        :return: The type of this ListHealthMonitorsRequest.
        :rtype: list[str]
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this ListHealthMonitorsRequest.

        健康检查请求协议。  取值：TCP、UDP_CONNECT、HTTP、HTTPS。  支持多值查询，查询条件格式：*****type=xxx&type=xxx*****。

        :param type: The type of this ListHealthMonitorsRequest.
        :type type: list[str]
        """
        self._type = type

    @property
    def expected_codes(self):
        """Gets the expected_codes of this ListHealthMonitorsRequest.

        期望响应状态码。  取值： - 单值：单个返回码，例如200。 - 列表：多个特定返回码，例如200，202。 - 区间：一个返回码区间，例如200-204。   默认值：200。  仅支持HTTP/HTTPS设置该字段，其他协议设置不会生效。  支持多值查询，查询条件格式：****expected_codes=xxx&expected_codes=xxx****。

        :return: The expected_codes of this ListHealthMonitorsRequest.
        :rtype: list[str]
        """
        return self._expected_codes

    @expected_codes.setter
    def expected_codes(self, expected_codes):
        """Sets the expected_codes of this ListHealthMonitorsRequest.

        期望响应状态码。  取值： - 单值：单个返回码，例如200。 - 列表：多个特定返回码，例如200，202。 - 区间：一个返回码区间，例如200-204。   默认值：200。  仅支持HTTP/HTTPS设置该字段，其他协议设置不会生效。  支持多值查询，查询条件格式：****expected_codes=xxx&expected_codes=xxx****。

        :param expected_codes: The expected_codes of this ListHealthMonitorsRequest.
        :type expected_codes: list[str]
        """
        self._expected_codes = expected_codes

    @property
    def url_path(self):
        """Gets the url_path of this ListHealthMonitorsRequest.

        健康检查测试member健康时发送的http请求路径。默认为“/”。  使用说明：以“/”开头。当type为HTTP/HTTPS时生效。  支持多值查询，查询条件格式：***url_path=xxx&url_path=xxx***。

        :return: The url_path of this ListHealthMonitorsRequest.
        :rtype: list[str]
        """
        return self._url_path

    @url_path.setter
    def url_path(self, url_path):
        """Sets the url_path of this ListHealthMonitorsRequest.

        健康检查测试member健康时发送的http请求路径。默认为“/”。  使用说明：以“/”开头。当type为HTTP/HTTPS时生效。  支持多值查询，查询条件格式：***url_path=xxx&url_path=xxx***。

        :param url_path: The url_path of this ListHealthMonitorsRequest.
        :type url_path: list[str]
        """
        self._url_path = url_path

    @property
    def http_method(self):
        """Gets the http_method of this ListHealthMonitorsRequest.

        HTTP请求方法。  取值：GET、HEAD、POST、PUT、DELETE、TRACE、OPTIONS、CONNECT、PATCH。  支持多值查询，查询条件格式：**http_method=xxx&http_method=xxx**。  不支持该字段，请勿使用。

        :return: The http_method of this ListHealthMonitorsRequest.
        :rtype: list[str]
        """
        return self._http_method

    @http_method.setter
    def http_method(self, http_method):
        """Sets the http_method of this ListHealthMonitorsRequest.

        HTTP请求方法。  取值：GET、HEAD、POST、PUT、DELETE、TRACE、OPTIONS、CONNECT、PATCH。  支持多值查询，查询条件格式：**http_method=xxx&http_method=xxx**。  不支持该字段，请勿使用。

        :param http_method: The http_method of this ListHealthMonitorsRequest.
        :type http_method: list[str]
        """
        self._http_method = http_method

    @property
    def enterprise_project_id(self):
        """Gets the enterprise_project_id of this ListHealthMonitorsRequest.

        企业项目ID。不传时查询default企业项目\"0\"下的资源，鉴权按照default企业项目鉴权； 如果传值，则传已存在的企业项目ID或all_granted_eps（表示查询所有企业项目）进行查询。  支持多值查询，查询条件格式： *enterprise_project_id=xxx&enterprise_project_id=xxx*。  [不支持该字段，请勿使用。](tag:dt,dt_test,hcso_dt)

        :return: The enterprise_project_id of this ListHealthMonitorsRequest.
        :rtype: list[str]
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        """Sets the enterprise_project_id of this ListHealthMonitorsRequest.

        企业项目ID。不传时查询default企业项目\"0\"下的资源，鉴权按照default企业项目鉴权； 如果传值，则传已存在的企业项目ID或all_granted_eps（表示查询所有企业项目）进行查询。  支持多值查询，查询条件格式： *enterprise_project_id=xxx&enterprise_project_id=xxx*。  [不支持该字段，请勿使用。](tag:dt,dt_test,hcso_dt)

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

# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class HealthMonitor:

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
        'pools': 'list[PoolRef]',
        'project_id': 'str',
        'timeout': 'int',
        'type': 'str',
        'url_path': 'str',
        'created_at': 'str',
        'updated_at': 'str'
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
        'pools': 'pools',
        'project_id': 'project_id',
        'timeout': 'timeout',
        'type': 'type',
        'url_path': 'url_path',
        'created_at': 'created_at',
        'updated_at': 'updated_at'
    }

    def __init__(self, admin_state_up=None, delay=None, domain_name=None, expected_codes=None, http_method=None, id=None, max_retries=None, max_retries_down=None, monitor_port=None, name=None, pools=None, project_id=None, timeout=None, type=None, url_path=None, created_at=None, updated_at=None):
        """HealthMonitor

        The model defined in huaweicloud sdk

        :param admin_state_up: 健康检查的管理状态。  取值： - true：表示开启健康检查，默认为true。 - false表示关闭健康检查。
        :type admin_state_up: bool
        :param delay: 健康检查间隔。取值：1-50s。
        :type delay: int
        :param domain_name: 发送健康检查请求的域名。  取值：以数字或字母开头，只能包含数字、字母、’-’、’.’。 默认为空，表示使用负载均衡器的vip作为http请求的目的地址。  使用说明：当type为HTTP/HTTPS时生效。
        :type domain_name: str
        :param expected_codes: 期望响应状态码。  取值： - 单值：单个返回码，例如200。 - 列表：多个特定返回码，例如200，202。 - 区间：一个返回码区间，例如200-204。   默认值：200。  仅支持HTTP/HTTPS设置该字段，其他协议设置不会生效。
        :type expected_codes: str
        :param http_method: HTTP请求方法。  取值：GET、HEAD、POST、PUT、DELETE、TRACE、OPTIONS、CONNECT、PATCH，默认GET。  使用说明：当type为HTTP/HTTPS时生效。  不支持该字段，请勿使用。
        :type http_method: str
        :param id: 健康检查ID
        :type id: str
        :param max_retries: 健康检查连续成功多少次后，将后端服务器的健康检查状态由OFFLINE判定为ONLINE。取值范围：1-10。
        :type max_retries: int
        :param max_retries_down: 健康检查连续失败多少次后，将后端服务器的健康检查状态由ONLINE判定为OFFLINE。取值范围：1-10，默认3。
        :type max_retries_down: int
        :param monitor_port: 健康检查端口号。取值：1-65535，默认为空，表示使用后端云服务器端口号。
        :type monitor_port: int
        :param name: 健康检查名称。
        :type name: str
        :param pools: 健康检查所在的后端云服务器组ID列表。实际只会有一个后端云服务器组ID。
        :type pools: list[:class:`huaweicloudsdkelb.v3.PoolRef`]
        :param project_id: 健康检查所在的项目ID。
        :type project_id: str
        :param timeout: 一次健康检查请求的超时时间。  建议该值小于delay的值。
        :type timeout: int
        :param type: 健康检查请求协议。  取值：TCP、UDP_CONNECT、HTTP、HTTPS。  使用说明： - 若pool的protocol为QUIC，则type只能是UDP_CONNECT。 - 若pool的protocol为UDP，则type只能UDP_CONNECT。 - 若pool的protocol为TCP，则type可以是TCP、HTTP、HTTPS。 - 若pool的protocol为HTTP，则type可以是TCP、HTTP、HTTPS。 - 若pool的protocol为HTTPS，则type可以是TCP、HTTP、HTTPS。
        :type type: str
        :param url_path: 健康检查请求的请求路径。以\&quot;/\&quot;开头，默认为\&quot;/\&quot;。  使用说明：当type为HTTP/HTTPS时生效。
        :type url_path: str
        :param created_at: 创建时间。格式：yyyy-MM-dd&#39;T&#39;HH:mm:ss&#39;Z&#39;，UTC时区。  [注意：独享型实例的历史数据以及共享型实例下的资源，不返回该字段。 ](tag:hws,hws_hk,ocb,ctc,g42,tm,cmcc,hk_g42,hws_ocb,fcs,dt,hk_tm)
        :type created_at: str
        :param updated_at: 更新时间。格式：yyyy-MM-dd&#39;T&#39;HH:mm:ss&#39;Z&#39;，UTC时区。  [注意：独享型实例的历史数据以及共享型实例下的资源，不返回该字段。 ](tag:hws,hws_hk,ocb,ctc,g42,tm,cmcc,hk_g42,hws_ocb,fcs,dt,hk_tm)
        :type updated_at: str
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
        self._pools = None
        self._project_id = None
        self._timeout = None
        self._type = None
        self._url_path = None
        self._created_at = None
        self._updated_at = None
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
        self.pools = pools
        self.project_id = project_id
        self.timeout = timeout
        self.type = type
        self.url_path = url_path
        if created_at is not None:
            self.created_at = created_at
        if updated_at is not None:
            self.updated_at = updated_at

    @property
    def admin_state_up(self):
        """Gets the admin_state_up of this HealthMonitor.

        健康检查的管理状态。  取值： - true：表示开启健康检查，默认为true。 - false表示关闭健康检查。

        :return: The admin_state_up of this HealthMonitor.
        :rtype: bool
        """
        return self._admin_state_up

    @admin_state_up.setter
    def admin_state_up(self, admin_state_up):
        """Sets the admin_state_up of this HealthMonitor.

        健康检查的管理状态。  取值： - true：表示开启健康检查，默认为true。 - false表示关闭健康检查。

        :param admin_state_up: The admin_state_up of this HealthMonitor.
        :type admin_state_up: bool
        """
        self._admin_state_up = admin_state_up

    @property
    def delay(self):
        """Gets the delay of this HealthMonitor.

        健康检查间隔。取值：1-50s。

        :return: The delay of this HealthMonitor.
        :rtype: int
        """
        return self._delay

    @delay.setter
    def delay(self, delay):
        """Sets the delay of this HealthMonitor.

        健康检查间隔。取值：1-50s。

        :param delay: The delay of this HealthMonitor.
        :type delay: int
        """
        self._delay = delay

    @property
    def domain_name(self):
        """Gets the domain_name of this HealthMonitor.

        发送健康检查请求的域名。  取值：以数字或字母开头，只能包含数字、字母、’-’、’.’。 默认为空，表示使用负载均衡器的vip作为http请求的目的地址。  使用说明：当type为HTTP/HTTPS时生效。

        :return: The domain_name of this HealthMonitor.
        :rtype: str
        """
        return self._domain_name

    @domain_name.setter
    def domain_name(self, domain_name):
        """Sets the domain_name of this HealthMonitor.

        发送健康检查请求的域名。  取值：以数字或字母开头，只能包含数字、字母、’-’、’.’。 默认为空，表示使用负载均衡器的vip作为http请求的目的地址。  使用说明：当type为HTTP/HTTPS时生效。

        :param domain_name: The domain_name of this HealthMonitor.
        :type domain_name: str
        """
        self._domain_name = domain_name

    @property
    def expected_codes(self):
        """Gets the expected_codes of this HealthMonitor.

        期望响应状态码。  取值： - 单值：单个返回码，例如200。 - 列表：多个特定返回码，例如200，202。 - 区间：一个返回码区间，例如200-204。   默认值：200。  仅支持HTTP/HTTPS设置该字段，其他协议设置不会生效。

        :return: The expected_codes of this HealthMonitor.
        :rtype: str
        """
        return self._expected_codes

    @expected_codes.setter
    def expected_codes(self, expected_codes):
        """Sets the expected_codes of this HealthMonitor.

        期望响应状态码。  取值： - 单值：单个返回码，例如200。 - 列表：多个特定返回码，例如200，202。 - 区间：一个返回码区间，例如200-204。   默认值：200。  仅支持HTTP/HTTPS设置该字段，其他协议设置不会生效。

        :param expected_codes: The expected_codes of this HealthMonitor.
        :type expected_codes: str
        """
        self._expected_codes = expected_codes

    @property
    def http_method(self):
        """Gets the http_method of this HealthMonitor.

        HTTP请求方法。  取值：GET、HEAD、POST、PUT、DELETE、TRACE、OPTIONS、CONNECT、PATCH，默认GET。  使用说明：当type为HTTP/HTTPS时生效。  不支持该字段，请勿使用。

        :return: The http_method of this HealthMonitor.
        :rtype: str
        """
        return self._http_method

    @http_method.setter
    def http_method(self, http_method):
        """Sets the http_method of this HealthMonitor.

        HTTP请求方法。  取值：GET、HEAD、POST、PUT、DELETE、TRACE、OPTIONS、CONNECT、PATCH，默认GET。  使用说明：当type为HTTP/HTTPS时生效。  不支持该字段，请勿使用。

        :param http_method: The http_method of this HealthMonitor.
        :type http_method: str
        """
        self._http_method = http_method

    @property
    def id(self):
        """Gets the id of this HealthMonitor.

        健康检查ID

        :return: The id of this HealthMonitor.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this HealthMonitor.

        健康检查ID

        :param id: The id of this HealthMonitor.
        :type id: str
        """
        self._id = id

    @property
    def max_retries(self):
        """Gets the max_retries of this HealthMonitor.

        健康检查连续成功多少次后，将后端服务器的健康检查状态由OFFLINE判定为ONLINE。取值范围：1-10。

        :return: The max_retries of this HealthMonitor.
        :rtype: int
        """
        return self._max_retries

    @max_retries.setter
    def max_retries(self, max_retries):
        """Sets the max_retries of this HealthMonitor.

        健康检查连续成功多少次后，将后端服务器的健康检查状态由OFFLINE判定为ONLINE。取值范围：1-10。

        :param max_retries: The max_retries of this HealthMonitor.
        :type max_retries: int
        """
        self._max_retries = max_retries

    @property
    def max_retries_down(self):
        """Gets the max_retries_down of this HealthMonitor.

        健康检查连续失败多少次后，将后端服务器的健康检查状态由ONLINE判定为OFFLINE。取值范围：1-10，默认3。

        :return: The max_retries_down of this HealthMonitor.
        :rtype: int
        """
        return self._max_retries_down

    @max_retries_down.setter
    def max_retries_down(self, max_retries_down):
        """Sets the max_retries_down of this HealthMonitor.

        健康检查连续失败多少次后，将后端服务器的健康检查状态由ONLINE判定为OFFLINE。取值范围：1-10，默认3。

        :param max_retries_down: The max_retries_down of this HealthMonitor.
        :type max_retries_down: int
        """
        self._max_retries_down = max_retries_down

    @property
    def monitor_port(self):
        """Gets the monitor_port of this HealthMonitor.

        健康检查端口号。取值：1-65535，默认为空，表示使用后端云服务器端口号。

        :return: The monitor_port of this HealthMonitor.
        :rtype: int
        """
        return self._monitor_port

    @monitor_port.setter
    def monitor_port(self, monitor_port):
        """Sets the monitor_port of this HealthMonitor.

        健康检查端口号。取值：1-65535，默认为空，表示使用后端云服务器端口号。

        :param monitor_port: The monitor_port of this HealthMonitor.
        :type monitor_port: int
        """
        self._monitor_port = monitor_port

    @property
    def name(self):
        """Gets the name of this HealthMonitor.

        健康检查名称。

        :return: The name of this HealthMonitor.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this HealthMonitor.

        健康检查名称。

        :param name: The name of this HealthMonitor.
        :type name: str
        """
        self._name = name

    @property
    def pools(self):
        """Gets the pools of this HealthMonitor.

        健康检查所在的后端云服务器组ID列表。实际只会有一个后端云服务器组ID。

        :return: The pools of this HealthMonitor.
        :rtype: list[:class:`huaweicloudsdkelb.v3.PoolRef`]
        """
        return self._pools

    @pools.setter
    def pools(self, pools):
        """Sets the pools of this HealthMonitor.

        健康检查所在的后端云服务器组ID列表。实际只会有一个后端云服务器组ID。

        :param pools: The pools of this HealthMonitor.
        :type pools: list[:class:`huaweicloudsdkelb.v3.PoolRef`]
        """
        self._pools = pools

    @property
    def project_id(self):
        """Gets the project_id of this HealthMonitor.

        健康检查所在的项目ID。

        :return: The project_id of this HealthMonitor.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """Sets the project_id of this HealthMonitor.

        健康检查所在的项目ID。

        :param project_id: The project_id of this HealthMonitor.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def timeout(self):
        """Gets the timeout of this HealthMonitor.

        一次健康检查请求的超时时间。  建议该值小于delay的值。

        :return: The timeout of this HealthMonitor.
        :rtype: int
        """
        return self._timeout

    @timeout.setter
    def timeout(self, timeout):
        """Sets the timeout of this HealthMonitor.

        一次健康检查请求的超时时间。  建议该值小于delay的值。

        :param timeout: The timeout of this HealthMonitor.
        :type timeout: int
        """
        self._timeout = timeout

    @property
    def type(self):
        """Gets the type of this HealthMonitor.

        健康检查请求协议。  取值：TCP、UDP_CONNECT、HTTP、HTTPS。  使用说明： - 若pool的protocol为QUIC，则type只能是UDP_CONNECT。 - 若pool的protocol为UDP，则type只能UDP_CONNECT。 - 若pool的protocol为TCP，则type可以是TCP、HTTP、HTTPS。 - 若pool的protocol为HTTP，则type可以是TCP、HTTP、HTTPS。 - 若pool的protocol为HTTPS，则type可以是TCP、HTTP、HTTPS。

        :return: The type of this HealthMonitor.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this HealthMonitor.

        健康检查请求协议。  取值：TCP、UDP_CONNECT、HTTP、HTTPS。  使用说明： - 若pool的protocol为QUIC，则type只能是UDP_CONNECT。 - 若pool的protocol为UDP，则type只能UDP_CONNECT。 - 若pool的protocol为TCP，则type可以是TCP、HTTP、HTTPS。 - 若pool的protocol为HTTP，则type可以是TCP、HTTP、HTTPS。 - 若pool的protocol为HTTPS，则type可以是TCP、HTTP、HTTPS。

        :param type: The type of this HealthMonitor.
        :type type: str
        """
        self._type = type

    @property
    def url_path(self):
        """Gets the url_path of this HealthMonitor.

        健康检查请求的请求路径。以\"/\"开头，默认为\"/\"。  使用说明：当type为HTTP/HTTPS时生效。

        :return: The url_path of this HealthMonitor.
        :rtype: str
        """
        return self._url_path

    @url_path.setter
    def url_path(self, url_path):
        """Sets the url_path of this HealthMonitor.

        健康检查请求的请求路径。以\"/\"开头，默认为\"/\"。  使用说明：当type为HTTP/HTTPS时生效。

        :param url_path: The url_path of this HealthMonitor.
        :type url_path: str
        """
        self._url_path = url_path

    @property
    def created_at(self):
        """Gets the created_at of this HealthMonitor.

        创建时间。格式：yyyy-MM-dd'T'HH:mm:ss'Z'，UTC时区。  [注意：独享型实例的历史数据以及共享型实例下的资源，不返回该字段。 ](tag:hws,hws_hk,ocb,ctc,g42,tm,cmcc,hk_g42,hws_ocb,fcs,dt,hk_tm)

        :return: The created_at of this HealthMonitor.
        :rtype: str
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this HealthMonitor.

        创建时间。格式：yyyy-MM-dd'T'HH:mm:ss'Z'，UTC时区。  [注意：独享型实例的历史数据以及共享型实例下的资源，不返回该字段。 ](tag:hws,hws_hk,ocb,ctc,g42,tm,cmcc,hk_g42,hws_ocb,fcs,dt,hk_tm)

        :param created_at: The created_at of this HealthMonitor.
        :type created_at: str
        """
        self._created_at = created_at

    @property
    def updated_at(self):
        """Gets the updated_at of this HealthMonitor.

        更新时间。格式：yyyy-MM-dd'T'HH:mm:ss'Z'，UTC时区。  [注意：独享型实例的历史数据以及共享型实例下的资源，不返回该字段。 ](tag:hws,hws_hk,ocb,ctc,g42,tm,cmcc,hk_g42,hws_ocb,fcs,dt,hk_tm)

        :return: The updated_at of this HealthMonitor.
        :rtype: str
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this HealthMonitor.

        更新时间。格式：yyyy-MM-dd'T'HH:mm:ss'Z'，UTC时区。  [注意：独享型实例的历史数据以及共享型实例下的资源，不返回该字段。 ](tag:hws,hws_hk,ocb,ctc,g42,tm,cmcc,hk_g42,hws_ocb,fcs,dt,hk_tm)

        :param updated_at: The updated_at of this HealthMonitor.
        :type updated_at: str
        """
        self._updated_at = updated_at

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
        if not isinstance(other, HealthMonitor):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

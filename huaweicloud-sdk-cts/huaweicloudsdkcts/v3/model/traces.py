# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Traces:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'resource_id': 'str',
        'trace_name': 'str',
        'trace_rating': 'str',
        'trace_type': 'str',
        'request': 'str',
        'response': 'str',
        'code': 'str',
        'api_version': 'str',
        'message': 'str',
        'record_time': 'int',
        'trace_id': 'str',
        'time': 'int',
        'user': 'UserInfo',
        'service_type': 'str',
        'resource_type': 'str',
        'source_ip': 'str',
        'resource_name': 'str',
        'request_id': 'str',
        'location_info': 'str',
        'endpoint': 'str',
        'resource_url': 'str',
        'enterprise_project_id': 'str',
        'resource_account_id': 'str',
        'read_only': 'bool',
        'operation_id': 'str'
    }

    attribute_map = {
        'resource_id': 'resource_id',
        'trace_name': 'trace_name',
        'trace_rating': 'trace_rating',
        'trace_type': 'trace_type',
        'request': 'request',
        'response': 'response',
        'code': 'code',
        'api_version': 'api_version',
        'message': 'message',
        'record_time': 'record_time',
        'trace_id': 'trace_id',
        'time': 'time',
        'user': 'user',
        'service_type': 'service_type',
        'resource_type': 'resource_type',
        'source_ip': 'source_ip',
        'resource_name': 'resource_name',
        'request_id': 'request_id',
        'location_info': 'location_info',
        'endpoint': 'endpoint',
        'resource_url': 'resource_url',
        'enterprise_project_id': 'enterprise_project_id',
        'resource_account_id': 'resource_account_id',
        'read_only': 'read_only',
        'operation_id': 'operation_id'
    }

    def __init__(self, resource_id=None, trace_name=None, trace_rating=None, trace_type=None, request=None, response=None, code=None, api_version=None, message=None, record_time=None, trace_id=None, time=None, user=None, service_type=None, resource_type=None, source_ip=None, resource_name=None, request_id=None, location_info=None, endpoint=None, resource_url=None, enterprise_project_id=None, resource_account_id=None, read_only=None, operation_id=None):
        r"""Traces

        The model defined in huaweicloud sdk

        :param resource_id: 标识事件对应的云服务资源ID。
        :type resource_id: str
        :param trace_name: 标识查询事件列表对应的事件名称。由0-9,a-z,A-Z,&#39;-&#39;,&#39;.&#39;,&#39;_&#39;,组成，长度为1～64个字符，且以首字符必须为字母。
        :type trace_name: str
        :param trace_rating: 标识事件等级，目前有三种：正常（normal），警告（warning），事故（incident）。
        :type trace_rating: str
        :param trace_type: 标识事件发生源头类型，管理类事件主要包括API调用（ApiCall），Console页面调用（ConsoleAction）和系统间调用（SystemAction）。 数据类事件主要包括ObsSDK，ObsAPI。
        :type trace_type: str
        :param request: 标识事件对应接口请求内容，即资源操作请求体。
        :type request: str
        :param response: 记录用户请求的响应，标识事件对应接口响应内容，即资源操作结果返回体。
        :type response: str
        :param code: 记录用户请求的响应，标识事件对应接口返回的HTTP状态码。
        :type code: str
        :param api_version: 标识事件对应的云服务接口版本。
        :type api_version: str
        :param message: 标识其他云服务为此条事件添加的备注信息。
        :type message: str
        :param record_time: 标识云审计服务记录本次事件的时间戳。
        :type record_time: int
        :param trace_id: 标识事件的ID，由系统生成的UUID。
        :type trace_id: str
        :param time: 标识事件产生的时间戳。
        :type time: int
        :param user: 
        :type user: :class:`huaweicloudsdkcts.v3.UserInfo`
        :param service_type: 标识查询事件列表对应的云服务类型。必须为已对接CTS的云服务的英文缩写，且服务类型一般为大写字母。
        :type service_type: str
        :param resource_type: 查询事件列表对应的资源类型。
        :type resource_type: str
        :param source_ip: 标识触发事件的租户IP。
        :type source_ip: str
        :param resource_name: 标识事件对应的资源名称。
        :type resource_name: str
        :param request_id: 记录本次请求的request id
        :type request_id: str
        :param location_info: 记录本次请求出错后，问题定位所需要的辅助信息。
        :type location_info: str
        :param endpoint: 云资源的详情页面
        :type endpoint: str
        :param resource_url: 云资源的详情页面的访问链接（不含endpoint）
        :type resource_url: str
        :param enterprise_project_id: 标识资源所在的企业项目ID。
        :type enterprise_project_id: str
        :param resource_account_id: 标识资源所在的账号ID。仅在跨租户操作资源时有值。
        :type resource_account_id: str
        :param read_only: 标识用户请求是不是只读。
        :type read_only: bool
        :param operation_id: 记录事件对应的操作ID。
        :type operation_id: str
        """
        
        

        self._resource_id = None
        self._trace_name = None
        self._trace_rating = None
        self._trace_type = None
        self._request = None
        self._response = None
        self._code = None
        self._api_version = None
        self._message = None
        self._record_time = None
        self._trace_id = None
        self._time = None
        self._user = None
        self._service_type = None
        self._resource_type = None
        self._source_ip = None
        self._resource_name = None
        self._request_id = None
        self._location_info = None
        self._endpoint = None
        self._resource_url = None
        self._enterprise_project_id = None
        self._resource_account_id = None
        self._read_only = None
        self._operation_id = None
        self.discriminator = None

        if resource_id is not None:
            self.resource_id = resource_id
        if trace_name is not None:
            self.trace_name = trace_name
        if trace_rating is not None:
            self.trace_rating = trace_rating
        if trace_type is not None:
            self.trace_type = trace_type
        if request is not None:
            self.request = request
        if response is not None:
            self.response = response
        if code is not None:
            self.code = code
        if api_version is not None:
            self.api_version = api_version
        if message is not None:
            self.message = message
        if record_time is not None:
            self.record_time = record_time
        if trace_id is not None:
            self.trace_id = trace_id
        if time is not None:
            self.time = time
        if user is not None:
            self.user = user
        if service_type is not None:
            self.service_type = service_type
        if resource_type is not None:
            self.resource_type = resource_type
        if source_ip is not None:
            self.source_ip = source_ip
        if resource_name is not None:
            self.resource_name = resource_name
        if request_id is not None:
            self.request_id = request_id
        if location_info is not None:
            self.location_info = location_info
        if endpoint is not None:
            self.endpoint = endpoint
        if resource_url is not None:
            self.resource_url = resource_url
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        if resource_account_id is not None:
            self.resource_account_id = resource_account_id
        if read_only is not None:
            self.read_only = read_only
        if operation_id is not None:
            self.operation_id = operation_id

    @property
    def resource_id(self):
        r"""Gets the resource_id of this Traces.

        标识事件对应的云服务资源ID。

        :return: The resource_id of this Traces.
        :rtype: str
        """
        return self._resource_id

    @resource_id.setter
    def resource_id(self, resource_id):
        r"""Sets the resource_id of this Traces.

        标识事件对应的云服务资源ID。

        :param resource_id: The resource_id of this Traces.
        :type resource_id: str
        """
        self._resource_id = resource_id

    @property
    def trace_name(self):
        r"""Gets the trace_name of this Traces.

        标识查询事件列表对应的事件名称。由0-9,a-z,A-Z,'-','.','_',组成，长度为1～64个字符，且以首字符必须为字母。

        :return: The trace_name of this Traces.
        :rtype: str
        """
        return self._trace_name

    @trace_name.setter
    def trace_name(self, trace_name):
        r"""Sets the trace_name of this Traces.

        标识查询事件列表对应的事件名称。由0-9,a-z,A-Z,'-','.','_',组成，长度为1～64个字符，且以首字符必须为字母。

        :param trace_name: The trace_name of this Traces.
        :type trace_name: str
        """
        self._trace_name = trace_name

    @property
    def trace_rating(self):
        r"""Gets the trace_rating of this Traces.

        标识事件等级，目前有三种：正常（normal），警告（warning），事故（incident）。

        :return: The trace_rating of this Traces.
        :rtype: str
        """
        return self._trace_rating

    @trace_rating.setter
    def trace_rating(self, trace_rating):
        r"""Sets the trace_rating of this Traces.

        标识事件等级，目前有三种：正常（normal），警告（warning），事故（incident）。

        :param trace_rating: The trace_rating of this Traces.
        :type trace_rating: str
        """
        self._trace_rating = trace_rating

    @property
    def trace_type(self):
        r"""Gets the trace_type of this Traces.

        标识事件发生源头类型，管理类事件主要包括API调用（ApiCall），Console页面调用（ConsoleAction）和系统间调用（SystemAction）。 数据类事件主要包括ObsSDK，ObsAPI。

        :return: The trace_type of this Traces.
        :rtype: str
        """
        return self._trace_type

    @trace_type.setter
    def trace_type(self, trace_type):
        r"""Sets the trace_type of this Traces.

        标识事件发生源头类型，管理类事件主要包括API调用（ApiCall），Console页面调用（ConsoleAction）和系统间调用（SystemAction）。 数据类事件主要包括ObsSDK，ObsAPI。

        :param trace_type: The trace_type of this Traces.
        :type trace_type: str
        """
        self._trace_type = trace_type

    @property
    def request(self):
        r"""Gets the request of this Traces.

        标识事件对应接口请求内容，即资源操作请求体。

        :return: The request of this Traces.
        :rtype: str
        """
        return self._request

    @request.setter
    def request(self, request):
        r"""Sets the request of this Traces.

        标识事件对应接口请求内容，即资源操作请求体。

        :param request: The request of this Traces.
        :type request: str
        """
        self._request = request

    @property
    def response(self):
        r"""Gets the response of this Traces.

        记录用户请求的响应，标识事件对应接口响应内容，即资源操作结果返回体。

        :return: The response of this Traces.
        :rtype: str
        """
        return self._response

    @response.setter
    def response(self, response):
        r"""Sets the response of this Traces.

        记录用户请求的响应，标识事件对应接口响应内容，即资源操作结果返回体。

        :param response: The response of this Traces.
        :type response: str
        """
        self._response = response

    @property
    def code(self):
        r"""Gets the code of this Traces.

        记录用户请求的响应，标识事件对应接口返回的HTTP状态码。

        :return: The code of this Traces.
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code):
        r"""Sets the code of this Traces.

        记录用户请求的响应，标识事件对应接口返回的HTTP状态码。

        :param code: The code of this Traces.
        :type code: str
        """
        self._code = code

    @property
    def api_version(self):
        r"""Gets the api_version of this Traces.

        标识事件对应的云服务接口版本。

        :return: The api_version of this Traces.
        :rtype: str
        """
        return self._api_version

    @api_version.setter
    def api_version(self, api_version):
        r"""Sets the api_version of this Traces.

        标识事件对应的云服务接口版本。

        :param api_version: The api_version of this Traces.
        :type api_version: str
        """
        self._api_version = api_version

    @property
    def message(self):
        r"""Gets the message of this Traces.

        标识其他云服务为此条事件添加的备注信息。

        :return: The message of this Traces.
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        r"""Sets the message of this Traces.

        标识其他云服务为此条事件添加的备注信息。

        :param message: The message of this Traces.
        :type message: str
        """
        self._message = message

    @property
    def record_time(self):
        r"""Gets the record_time of this Traces.

        标识云审计服务记录本次事件的时间戳。

        :return: The record_time of this Traces.
        :rtype: int
        """
        return self._record_time

    @record_time.setter
    def record_time(self, record_time):
        r"""Sets the record_time of this Traces.

        标识云审计服务记录本次事件的时间戳。

        :param record_time: The record_time of this Traces.
        :type record_time: int
        """
        self._record_time = record_time

    @property
    def trace_id(self):
        r"""Gets the trace_id of this Traces.

        标识事件的ID，由系统生成的UUID。

        :return: The trace_id of this Traces.
        :rtype: str
        """
        return self._trace_id

    @trace_id.setter
    def trace_id(self, trace_id):
        r"""Sets the trace_id of this Traces.

        标识事件的ID，由系统生成的UUID。

        :param trace_id: The trace_id of this Traces.
        :type trace_id: str
        """
        self._trace_id = trace_id

    @property
    def time(self):
        r"""Gets the time of this Traces.

        标识事件产生的时间戳。

        :return: The time of this Traces.
        :rtype: int
        """
        return self._time

    @time.setter
    def time(self, time):
        r"""Sets the time of this Traces.

        标识事件产生的时间戳。

        :param time: The time of this Traces.
        :type time: int
        """
        self._time = time

    @property
    def user(self):
        r"""Gets the user of this Traces.

        :return: The user of this Traces.
        :rtype: :class:`huaweicloudsdkcts.v3.UserInfo`
        """
        return self._user

    @user.setter
    def user(self, user):
        r"""Sets the user of this Traces.

        :param user: The user of this Traces.
        :type user: :class:`huaweicloudsdkcts.v3.UserInfo`
        """
        self._user = user

    @property
    def service_type(self):
        r"""Gets the service_type of this Traces.

        标识查询事件列表对应的云服务类型。必须为已对接CTS的云服务的英文缩写，且服务类型一般为大写字母。

        :return: The service_type of this Traces.
        :rtype: str
        """
        return self._service_type

    @service_type.setter
    def service_type(self, service_type):
        r"""Sets the service_type of this Traces.

        标识查询事件列表对应的云服务类型。必须为已对接CTS的云服务的英文缩写，且服务类型一般为大写字母。

        :param service_type: The service_type of this Traces.
        :type service_type: str
        """
        self._service_type = service_type

    @property
    def resource_type(self):
        r"""Gets the resource_type of this Traces.

        查询事件列表对应的资源类型。

        :return: The resource_type of this Traces.
        :rtype: str
        """
        return self._resource_type

    @resource_type.setter
    def resource_type(self, resource_type):
        r"""Sets the resource_type of this Traces.

        查询事件列表对应的资源类型。

        :param resource_type: The resource_type of this Traces.
        :type resource_type: str
        """
        self._resource_type = resource_type

    @property
    def source_ip(self):
        r"""Gets the source_ip of this Traces.

        标识触发事件的租户IP。

        :return: The source_ip of this Traces.
        :rtype: str
        """
        return self._source_ip

    @source_ip.setter
    def source_ip(self, source_ip):
        r"""Sets the source_ip of this Traces.

        标识触发事件的租户IP。

        :param source_ip: The source_ip of this Traces.
        :type source_ip: str
        """
        self._source_ip = source_ip

    @property
    def resource_name(self):
        r"""Gets the resource_name of this Traces.

        标识事件对应的资源名称。

        :return: The resource_name of this Traces.
        :rtype: str
        """
        return self._resource_name

    @resource_name.setter
    def resource_name(self, resource_name):
        r"""Sets the resource_name of this Traces.

        标识事件对应的资源名称。

        :param resource_name: The resource_name of this Traces.
        :type resource_name: str
        """
        self._resource_name = resource_name

    @property
    def request_id(self):
        r"""Gets the request_id of this Traces.

        记录本次请求的request id

        :return: The request_id of this Traces.
        :rtype: str
        """
        return self._request_id

    @request_id.setter
    def request_id(self, request_id):
        r"""Sets the request_id of this Traces.

        记录本次请求的request id

        :param request_id: The request_id of this Traces.
        :type request_id: str
        """
        self._request_id = request_id

    @property
    def location_info(self):
        r"""Gets the location_info of this Traces.

        记录本次请求出错后，问题定位所需要的辅助信息。

        :return: The location_info of this Traces.
        :rtype: str
        """
        return self._location_info

    @location_info.setter
    def location_info(self, location_info):
        r"""Sets the location_info of this Traces.

        记录本次请求出错后，问题定位所需要的辅助信息。

        :param location_info: The location_info of this Traces.
        :type location_info: str
        """
        self._location_info = location_info

    @property
    def endpoint(self):
        r"""Gets the endpoint of this Traces.

        云资源的详情页面

        :return: The endpoint of this Traces.
        :rtype: str
        """
        return self._endpoint

    @endpoint.setter
    def endpoint(self, endpoint):
        r"""Sets the endpoint of this Traces.

        云资源的详情页面

        :param endpoint: The endpoint of this Traces.
        :type endpoint: str
        """
        self._endpoint = endpoint

    @property
    def resource_url(self):
        r"""Gets the resource_url of this Traces.

        云资源的详情页面的访问链接（不含endpoint）

        :return: The resource_url of this Traces.
        :rtype: str
        """
        return self._resource_url

    @resource_url.setter
    def resource_url(self, resource_url):
        r"""Sets the resource_url of this Traces.

        云资源的详情页面的访问链接（不含endpoint）

        :param resource_url: The resource_url of this Traces.
        :type resource_url: str
        """
        self._resource_url = resource_url

    @property
    def enterprise_project_id(self):
        r"""Gets the enterprise_project_id of this Traces.

        标识资源所在的企业项目ID。

        :return: The enterprise_project_id of this Traces.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        r"""Sets the enterprise_project_id of this Traces.

        标识资源所在的企业项目ID。

        :param enterprise_project_id: The enterprise_project_id of this Traces.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def resource_account_id(self):
        r"""Gets the resource_account_id of this Traces.

        标识资源所在的账号ID。仅在跨租户操作资源时有值。

        :return: The resource_account_id of this Traces.
        :rtype: str
        """
        return self._resource_account_id

    @resource_account_id.setter
    def resource_account_id(self, resource_account_id):
        r"""Sets the resource_account_id of this Traces.

        标识资源所在的账号ID。仅在跨租户操作资源时有值。

        :param resource_account_id: The resource_account_id of this Traces.
        :type resource_account_id: str
        """
        self._resource_account_id = resource_account_id

    @property
    def read_only(self):
        r"""Gets the read_only of this Traces.

        标识用户请求是不是只读。

        :return: The read_only of this Traces.
        :rtype: bool
        """
        return self._read_only

    @read_only.setter
    def read_only(self, read_only):
        r"""Sets the read_only of this Traces.

        标识用户请求是不是只读。

        :param read_only: The read_only of this Traces.
        :type read_only: bool
        """
        self._read_only = read_only

    @property
    def operation_id(self):
        r"""Gets the operation_id of this Traces.

        记录事件对应的操作ID。

        :return: The operation_id of this Traces.
        :rtype: str
        """
        return self._operation_id

    @operation_id.setter
    def operation_id(self, operation_id):
        r"""Sets the operation_id of this Traces.

        记录事件对应的操作ID。

        :param operation_id: The operation_id of this Traces.
        :type operation_id: str
        """
        self._operation_id = operation_id

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
        if not isinstance(other, Traces):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

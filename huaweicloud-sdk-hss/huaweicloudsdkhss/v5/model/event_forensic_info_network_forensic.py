# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class EventForensicInfoNetworkForensic:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'local_address': 'str',
        'local_port': 'int',
        'src_ip': 'str',
        'remote_address': 'str',
        'remote_port': 'int',
        'protocol': 'str',
        'app_protocol': 'str',
        'flow_direction': 'str',
        'count': 'int',
        'first_time': 'int',
        'last_time': 'int',
        'request_method': 'str',
        'request_url': 'str',
        'query_string': 'str',
        'request_params': 'str',
        'request_header': 'str'
    }

    attribute_map = {
        'local_address': 'local_address',
        'local_port': 'local_port',
        'src_ip': 'src_ip',
        'remote_address': 'remote_address',
        'remote_port': 'remote_port',
        'protocol': 'protocol',
        'app_protocol': 'app_protocol',
        'flow_direction': 'flow_direction',
        'count': 'count',
        'first_time': 'first_time',
        'last_time': 'last_time',
        'request_method': 'request_method',
        'request_url': 'request_url',
        'query_string': 'query_string',
        'request_params': 'request_params',
        'request_header': 'request_header'
    }

    def __init__(self, local_address=None, local_port=None, src_ip=None, remote_address=None, remote_port=None, protocol=None, app_protocol=None, flow_direction=None, count=None, first_time=None, last_time=None, request_method=None, request_url=None, query_string=None, request_params=None, request_header=None):
        r"""EventForensicInfoNetworkForensic

        The model defined in huaweicloud sdk

        :param local_address: **参数解释**： 本地ip地址 **取值范围**： 不涉及
        :type local_address: str
        :param local_port: **参数解释**： 本地端口 **取值范围**： 不涉及
        :type local_port: int
        :param src_ip: **参数解释**： 源ip **取值范围**： 不涉及
        :type src_ip: str
        :param remote_address: **参数解释**： 远端ip地址(攻击者ip) **取值范围**： 不涉及
        :type remote_address: str
        :param remote_port: **参数解释**： 远程端口 **取值范围**： 不涉及
        :type remote_port: int
        :param protocol: **参数解释**： 协议 **取值范围**： 不涉及
        :type protocol: str
        :param app_protocol: **参数解释**： 应用层协议 **取值范围**： 不涉及
        :type app_protocol: str
        :param flow_direction: **参数解释**： 流量方向 **取值范围**： 不涉及
        :type flow_direction: str
        :param count: **参数解释**： 连接次数 **取值范围**： 不涉及
        :type count: int
        :param first_time: **参数解释**： 首次连接时间(毫秒) **取值范围**： 不涉及
        :type first_time: int
        :param last_time: **参数解释**： 最后一连接时间(毫秒) **取值范围**： 不涉及
        :type last_time: int
        :param request_method: **参数解释**： 请求方法 **取值范围**： 不涉及
        :type request_method: str
        :param request_url: **参数解释**： 请求地址 **取值范围**： 不涉及
        :type request_url: str
        :param query_string: **参数解释**： 查询字符串 **取值范围**： 不涉及
        :type query_string: str
        :param request_params: **参数解释**： 请求参数 **取值范围**： 不涉及
        :type request_params: str
        :param request_header: **参数解释**： 请求头信息 **取值范围**： 不涉及
        :type request_header: str
        """
        
        

        self._local_address = None
        self._local_port = None
        self._src_ip = None
        self._remote_address = None
        self._remote_port = None
        self._protocol = None
        self._app_protocol = None
        self._flow_direction = None
        self._count = None
        self._first_time = None
        self._last_time = None
        self._request_method = None
        self._request_url = None
        self._query_string = None
        self._request_params = None
        self._request_header = None
        self.discriminator = None

        if local_address is not None:
            self.local_address = local_address
        if local_port is not None:
            self.local_port = local_port
        if src_ip is not None:
            self.src_ip = src_ip
        if remote_address is not None:
            self.remote_address = remote_address
        if remote_port is not None:
            self.remote_port = remote_port
        if protocol is not None:
            self.protocol = protocol
        if app_protocol is not None:
            self.app_protocol = app_protocol
        if flow_direction is not None:
            self.flow_direction = flow_direction
        if count is not None:
            self.count = count
        if first_time is not None:
            self.first_time = first_time
        if last_time is not None:
            self.last_time = last_time
        if request_method is not None:
            self.request_method = request_method
        if request_url is not None:
            self.request_url = request_url
        if query_string is not None:
            self.query_string = query_string
        if request_params is not None:
            self.request_params = request_params
        if request_header is not None:
            self.request_header = request_header

    @property
    def local_address(self):
        r"""Gets the local_address of this EventForensicInfoNetworkForensic.

        **参数解释**： 本地ip地址 **取值范围**： 不涉及

        :return: The local_address of this EventForensicInfoNetworkForensic.
        :rtype: str
        """
        return self._local_address

    @local_address.setter
    def local_address(self, local_address):
        r"""Sets the local_address of this EventForensicInfoNetworkForensic.

        **参数解释**： 本地ip地址 **取值范围**： 不涉及

        :param local_address: The local_address of this EventForensicInfoNetworkForensic.
        :type local_address: str
        """
        self._local_address = local_address

    @property
    def local_port(self):
        r"""Gets the local_port of this EventForensicInfoNetworkForensic.

        **参数解释**： 本地端口 **取值范围**： 不涉及

        :return: The local_port of this EventForensicInfoNetworkForensic.
        :rtype: int
        """
        return self._local_port

    @local_port.setter
    def local_port(self, local_port):
        r"""Sets the local_port of this EventForensicInfoNetworkForensic.

        **参数解释**： 本地端口 **取值范围**： 不涉及

        :param local_port: The local_port of this EventForensicInfoNetworkForensic.
        :type local_port: int
        """
        self._local_port = local_port

    @property
    def src_ip(self):
        r"""Gets the src_ip of this EventForensicInfoNetworkForensic.

        **参数解释**： 源ip **取值范围**： 不涉及

        :return: The src_ip of this EventForensicInfoNetworkForensic.
        :rtype: str
        """
        return self._src_ip

    @src_ip.setter
    def src_ip(self, src_ip):
        r"""Sets the src_ip of this EventForensicInfoNetworkForensic.

        **参数解释**： 源ip **取值范围**： 不涉及

        :param src_ip: The src_ip of this EventForensicInfoNetworkForensic.
        :type src_ip: str
        """
        self._src_ip = src_ip

    @property
    def remote_address(self):
        r"""Gets the remote_address of this EventForensicInfoNetworkForensic.

        **参数解释**： 远端ip地址(攻击者ip) **取值范围**： 不涉及

        :return: The remote_address of this EventForensicInfoNetworkForensic.
        :rtype: str
        """
        return self._remote_address

    @remote_address.setter
    def remote_address(self, remote_address):
        r"""Sets the remote_address of this EventForensicInfoNetworkForensic.

        **参数解释**： 远端ip地址(攻击者ip) **取值范围**： 不涉及

        :param remote_address: The remote_address of this EventForensicInfoNetworkForensic.
        :type remote_address: str
        """
        self._remote_address = remote_address

    @property
    def remote_port(self):
        r"""Gets the remote_port of this EventForensicInfoNetworkForensic.

        **参数解释**： 远程端口 **取值范围**： 不涉及

        :return: The remote_port of this EventForensicInfoNetworkForensic.
        :rtype: int
        """
        return self._remote_port

    @remote_port.setter
    def remote_port(self, remote_port):
        r"""Sets the remote_port of this EventForensicInfoNetworkForensic.

        **参数解释**： 远程端口 **取值范围**： 不涉及

        :param remote_port: The remote_port of this EventForensicInfoNetworkForensic.
        :type remote_port: int
        """
        self._remote_port = remote_port

    @property
    def protocol(self):
        r"""Gets the protocol of this EventForensicInfoNetworkForensic.

        **参数解释**： 协议 **取值范围**： 不涉及

        :return: The protocol of this EventForensicInfoNetworkForensic.
        :rtype: str
        """
        return self._protocol

    @protocol.setter
    def protocol(self, protocol):
        r"""Sets the protocol of this EventForensicInfoNetworkForensic.

        **参数解释**： 协议 **取值范围**： 不涉及

        :param protocol: The protocol of this EventForensicInfoNetworkForensic.
        :type protocol: str
        """
        self._protocol = protocol

    @property
    def app_protocol(self):
        r"""Gets the app_protocol of this EventForensicInfoNetworkForensic.

        **参数解释**： 应用层协议 **取值范围**： 不涉及

        :return: The app_protocol of this EventForensicInfoNetworkForensic.
        :rtype: str
        """
        return self._app_protocol

    @app_protocol.setter
    def app_protocol(self, app_protocol):
        r"""Sets the app_protocol of this EventForensicInfoNetworkForensic.

        **参数解释**： 应用层协议 **取值范围**： 不涉及

        :param app_protocol: The app_protocol of this EventForensicInfoNetworkForensic.
        :type app_protocol: str
        """
        self._app_protocol = app_protocol

    @property
    def flow_direction(self):
        r"""Gets the flow_direction of this EventForensicInfoNetworkForensic.

        **参数解释**： 流量方向 **取值范围**： 不涉及

        :return: The flow_direction of this EventForensicInfoNetworkForensic.
        :rtype: str
        """
        return self._flow_direction

    @flow_direction.setter
    def flow_direction(self, flow_direction):
        r"""Sets the flow_direction of this EventForensicInfoNetworkForensic.

        **参数解释**： 流量方向 **取值范围**： 不涉及

        :param flow_direction: The flow_direction of this EventForensicInfoNetworkForensic.
        :type flow_direction: str
        """
        self._flow_direction = flow_direction

    @property
    def count(self):
        r"""Gets the count of this EventForensicInfoNetworkForensic.

        **参数解释**： 连接次数 **取值范围**： 不涉及

        :return: The count of this EventForensicInfoNetworkForensic.
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        r"""Sets the count of this EventForensicInfoNetworkForensic.

        **参数解释**： 连接次数 **取值范围**： 不涉及

        :param count: The count of this EventForensicInfoNetworkForensic.
        :type count: int
        """
        self._count = count

    @property
    def first_time(self):
        r"""Gets the first_time of this EventForensicInfoNetworkForensic.

        **参数解释**： 首次连接时间(毫秒) **取值范围**： 不涉及

        :return: The first_time of this EventForensicInfoNetworkForensic.
        :rtype: int
        """
        return self._first_time

    @first_time.setter
    def first_time(self, first_time):
        r"""Sets the first_time of this EventForensicInfoNetworkForensic.

        **参数解释**： 首次连接时间(毫秒) **取值范围**： 不涉及

        :param first_time: The first_time of this EventForensicInfoNetworkForensic.
        :type first_time: int
        """
        self._first_time = first_time

    @property
    def last_time(self):
        r"""Gets the last_time of this EventForensicInfoNetworkForensic.

        **参数解释**： 最后一连接时间(毫秒) **取值范围**： 不涉及

        :return: The last_time of this EventForensicInfoNetworkForensic.
        :rtype: int
        """
        return self._last_time

    @last_time.setter
    def last_time(self, last_time):
        r"""Sets the last_time of this EventForensicInfoNetworkForensic.

        **参数解释**： 最后一连接时间(毫秒) **取值范围**： 不涉及

        :param last_time: The last_time of this EventForensicInfoNetworkForensic.
        :type last_time: int
        """
        self._last_time = last_time

    @property
    def request_method(self):
        r"""Gets the request_method of this EventForensicInfoNetworkForensic.

        **参数解释**： 请求方法 **取值范围**： 不涉及

        :return: The request_method of this EventForensicInfoNetworkForensic.
        :rtype: str
        """
        return self._request_method

    @request_method.setter
    def request_method(self, request_method):
        r"""Sets the request_method of this EventForensicInfoNetworkForensic.

        **参数解释**： 请求方法 **取值范围**： 不涉及

        :param request_method: The request_method of this EventForensicInfoNetworkForensic.
        :type request_method: str
        """
        self._request_method = request_method

    @property
    def request_url(self):
        r"""Gets the request_url of this EventForensicInfoNetworkForensic.

        **参数解释**： 请求地址 **取值范围**： 不涉及

        :return: The request_url of this EventForensicInfoNetworkForensic.
        :rtype: str
        """
        return self._request_url

    @request_url.setter
    def request_url(self, request_url):
        r"""Sets the request_url of this EventForensicInfoNetworkForensic.

        **参数解释**： 请求地址 **取值范围**： 不涉及

        :param request_url: The request_url of this EventForensicInfoNetworkForensic.
        :type request_url: str
        """
        self._request_url = request_url

    @property
    def query_string(self):
        r"""Gets the query_string of this EventForensicInfoNetworkForensic.

        **参数解释**： 查询字符串 **取值范围**： 不涉及

        :return: The query_string of this EventForensicInfoNetworkForensic.
        :rtype: str
        """
        return self._query_string

    @query_string.setter
    def query_string(self, query_string):
        r"""Sets the query_string of this EventForensicInfoNetworkForensic.

        **参数解释**： 查询字符串 **取值范围**： 不涉及

        :param query_string: The query_string of this EventForensicInfoNetworkForensic.
        :type query_string: str
        """
        self._query_string = query_string

    @property
    def request_params(self):
        r"""Gets the request_params of this EventForensicInfoNetworkForensic.

        **参数解释**： 请求参数 **取值范围**： 不涉及

        :return: The request_params of this EventForensicInfoNetworkForensic.
        :rtype: str
        """
        return self._request_params

    @request_params.setter
    def request_params(self, request_params):
        r"""Sets the request_params of this EventForensicInfoNetworkForensic.

        **参数解释**： 请求参数 **取值范围**： 不涉及

        :param request_params: The request_params of this EventForensicInfoNetworkForensic.
        :type request_params: str
        """
        self._request_params = request_params

    @property
    def request_header(self):
        r"""Gets the request_header of this EventForensicInfoNetworkForensic.

        **参数解释**： 请求头信息 **取值范围**： 不涉及

        :return: The request_header of this EventForensicInfoNetworkForensic.
        :rtype: str
        """
        return self._request_header

    @request_header.setter
    def request_header(self, request_header):
        r"""Sets the request_header of this EventForensicInfoNetworkForensic.

        **参数解释**： 请求头信息 **取值范围**： 不涉及

        :param request_header: The request_header of this EventForensicInfoNetworkForensic.
        :type request_header: str
        """
        self._request_header = request_header

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
        if not isinstance(other, EventForensicInfoNetworkForensic):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

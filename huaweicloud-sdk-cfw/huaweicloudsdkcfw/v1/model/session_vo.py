# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SessionVO:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'app': 'str',
        'bytes': 'float',
        'dst_associate_instance_type': 'str',
        'dst_device_name': 'str',
        'dst_ip': 'str',
        'dst_port': 'str',
        'dst_host': 'str',
        'dst_region_id': 'str',
        'dst_region_name': 'str',
        'end_time': 'int',
        'protocol': 'str',
        'request_byte': 'float',
        'response_byte': 'float',
        'sessions': 'int',
        'src_associate_instance_type': 'str',
        'src_device_name': 'str',
        'src_ip': 'str',
        'src_region_id': 'str',
        'src_region_name': 'str',
        'start_time': 'int'
    }

    attribute_map = {
        'app': 'app',
        'bytes': 'bytes',
        'dst_associate_instance_type': 'dst_associate_instance_type',
        'dst_device_name': 'dst_device_name',
        'dst_ip': 'dst_ip',
        'dst_port': 'dst_port',
        'dst_host': 'dst_host',
        'dst_region_id': 'dst_region_id',
        'dst_region_name': 'dst_region_name',
        'end_time': 'end_time',
        'protocol': 'protocol',
        'request_byte': 'request_byte',
        'response_byte': 'response_byte',
        'sessions': 'sessions',
        'src_associate_instance_type': 'src_associate_instance_type',
        'src_device_name': 'src_device_name',
        'src_ip': 'src_ip',
        'src_region_id': 'src_region_id',
        'src_region_name': 'src_region_name',
        'start_time': 'start_time'
    }

    def __init__(self, app=None, bytes=None, dst_associate_instance_type=None, dst_device_name=None, dst_ip=None, dst_port=None, dst_host=None, dst_region_id=None, dst_region_name=None, end_time=None, protocol=None, request_byte=None, response_byte=None, sessions=None, src_associate_instance_type=None, src_device_name=None, src_ip=None, src_region_id=None, src_region_name=None, start_time=None):
        r"""SessionVO

        The model defined in huaweicloud sdk

        :param app: **参数解释**： 应用 **取值范围**： 不涉及
        :type app: str
        :param bytes: **参数解释**： 字节数 **取值范围**： 不涉及
        :type bytes: float
        :param dst_associate_instance_type: **参数解释**： 目的IP关联资产类型 **取值范围**： 不涉及
        :type dst_associate_instance_type: str
        :param dst_device_name: **参数解释**： 目的IP关联资产名称 **取值范围**： 不涉及
        :type dst_device_name: str
        :param dst_ip: **参数解释**： 目的IP **取值范围**： 不涉及
        :type dst_ip: str
        :param dst_port: **参数解释**： 目的端口 **取值范围**： 不涉及
        :type dst_port: str
        :param dst_host: **参数解释**： 目的域名 **取值范围**： 不涉及
        :type dst_host: str
        :param dst_region_id: **参数解释**： 目的regionID **取值范围**： 不涉及
        :type dst_region_id: str
        :param dst_region_name: **参数解释**： 目的地区 **取值范围**： 不涉及
        :type dst_region_name: str
        :param end_time: **参数解释**： 结束时间 **取值范围**： 不涉及
        :type end_time: int
        :param protocol: **参数解释**： 协议 **取值范围**： 不涉及
        :type protocol: str
        :param request_byte: **参数解释**： 请求字节数 **取值范围**： 不涉及
        :type request_byte: float
        :param response_byte: **参数解释**： 响应字节数 **取值范围**： 不涉及
        :type response_byte: float
        :param sessions: **参数解释**： 会话数量 **取值范围**： 不涉及
        :type sessions: int
        :param src_associate_instance_type: **参数解释**： 源IP关联资产类型 **取值范围**： 不涉及
        :type src_associate_instance_type: str
        :param src_device_name: **参数解释**： 源IP关联资产名称 **取值范围**： 不涉及
        :type src_device_name: str
        :param src_ip: **参数解释**： 源IP **取值范围**： 不涉及
        :type src_ip: str
        :param src_region_id: **参数解释**： 源地区 ID **取值范围**： 不涉及
        :type src_region_id: str
        :param src_region_name: **参数解释**： 源地区 **取值范围**： 不涉及
        :type src_region_name: str
        :param start_time: **参数解释**： 会话开始时间 **取值范围**： 不涉及
        :type start_time: int
        """
        
        

        self._app = None
        self._bytes = None
        self._dst_associate_instance_type = None
        self._dst_device_name = None
        self._dst_ip = None
        self._dst_port = None
        self._dst_host = None
        self._dst_region_id = None
        self._dst_region_name = None
        self._end_time = None
        self._protocol = None
        self._request_byte = None
        self._response_byte = None
        self._sessions = None
        self._src_associate_instance_type = None
        self._src_device_name = None
        self._src_ip = None
        self._src_region_id = None
        self._src_region_name = None
        self._start_time = None
        self.discriminator = None

        if app is not None:
            self.app = app
        if bytes is not None:
            self.bytes = bytes
        if dst_associate_instance_type is not None:
            self.dst_associate_instance_type = dst_associate_instance_type
        if dst_device_name is not None:
            self.dst_device_name = dst_device_name
        if dst_ip is not None:
            self.dst_ip = dst_ip
        if dst_port is not None:
            self.dst_port = dst_port
        if dst_host is not None:
            self.dst_host = dst_host
        if dst_region_id is not None:
            self.dst_region_id = dst_region_id
        if dst_region_name is not None:
            self.dst_region_name = dst_region_name
        if end_time is not None:
            self.end_time = end_time
        if protocol is not None:
            self.protocol = protocol
        if request_byte is not None:
            self.request_byte = request_byte
        if response_byte is not None:
            self.response_byte = response_byte
        if sessions is not None:
            self.sessions = sessions
        if src_associate_instance_type is not None:
            self.src_associate_instance_type = src_associate_instance_type
        if src_device_name is not None:
            self.src_device_name = src_device_name
        if src_ip is not None:
            self.src_ip = src_ip
        if src_region_id is not None:
            self.src_region_id = src_region_id
        if src_region_name is not None:
            self.src_region_name = src_region_name
        if start_time is not None:
            self.start_time = start_time

    @property
    def app(self):
        r"""Gets the app of this SessionVO.

        **参数解释**： 应用 **取值范围**： 不涉及

        :return: The app of this SessionVO.
        :rtype: str
        """
        return self._app

    @app.setter
    def app(self, app):
        r"""Sets the app of this SessionVO.

        **参数解释**： 应用 **取值范围**： 不涉及

        :param app: The app of this SessionVO.
        :type app: str
        """
        self._app = app

    @property
    def bytes(self):
        r"""Gets the bytes of this SessionVO.

        **参数解释**： 字节数 **取值范围**： 不涉及

        :return: The bytes of this SessionVO.
        :rtype: float
        """
        return self._bytes

    @bytes.setter
    def bytes(self, bytes):
        r"""Sets the bytes of this SessionVO.

        **参数解释**： 字节数 **取值范围**： 不涉及

        :param bytes: The bytes of this SessionVO.
        :type bytes: float
        """
        self._bytes = bytes

    @property
    def dst_associate_instance_type(self):
        r"""Gets the dst_associate_instance_type of this SessionVO.

        **参数解释**： 目的IP关联资产类型 **取值范围**： 不涉及

        :return: The dst_associate_instance_type of this SessionVO.
        :rtype: str
        """
        return self._dst_associate_instance_type

    @dst_associate_instance_type.setter
    def dst_associate_instance_type(self, dst_associate_instance_type):
        r"""Sets the dst_associate_instance_type of this SessionVO.

        **参数解释**： 目的IP关联资产类型 **取值范围**： 不涉及

        :param dst_associate_instance_type: The dst_associate_instance_type of this SessionVO.
        :type dst_associate_instance_type: str
        """
        self._dst_associate_instance_type = dst_associate_instance_type

    @property
    def dst_device_name(self):
        r"""Gets the dst_device_name of this SessionVO.

        **参数解释**： 目的IP关联资产名称 **取值范围**： 不涉及

        :return: The dst_device_name of this SessionVO.
        :rtype: str
        """
        return self._dst_device_name

    @dst_device_name.setter
    def dst_device_name(self, dst_device_name):
        r"""Sets the dst_device_name of this SessionVO.

        **参数解释**： 目的IP关联资产名称 **取值范围**： 不涉及

        :param dst_device_name: The dst_device_name of this SessionVO.
        :type dst_device_name: str
        """
        self._dst_device_name = dst_device_name

    @property
    def dst_ip(self):
        r"""Gets the dst_ip of this SessionVO.

        **参数解释**： 目的IP **取值范围**： 不涉及

        :return: The dst_ip of this SessionVO.
        :rtype: str
        """
        return self._dst_ip

    @dst_ip.setter
    def dst_ip(self, dst_ip):
        r"""Sets the dst_ip of this SessionVO.

        **参数解释**： 目的IP **取值范围**： 不涉及

        :param dst_ip: The dst_ip of this SessionVO.
        :type dst_ip: str
        """
        self._dst_ip = dst_ip

    @property
    def dst_port(self):
        r"""Gets the dst_port of this SessionVO.

        **参数解释**： 目的端口 **取值范围**： 不涉及

        :return: The dst_port of this SessionVO.
        :rtype: str
        """
        return self._dst_port

    @dst_port.setter
    def dst_port(self, dst_port):
        r"""Sets the dst_port of this SessionVO.

        **参数解释**： 目的端口 **取值范围**： 不涉及

        :param dst_port: The dst_port of this SessionVO.
        :type dst_port: str
        """
        self._dst_port = dst_port

    @property
    def dst_host(self):
        r"""Gets the dst_host of this SessionVO.

        **参数解释**： 目的域名 **取值范围**： 不涉及

        :return: The dst_host of this SessionVO.
        :rtype: str
        """
        return self._dst_host

    @dst_host.setter
    def dst_host(self, dst_host):
        r"""Sets the dst_host of this SessionVO.

        **参数解释**： 目的域名 **取值范围**： 不涉及

        :param dst_host: The dst_host of this SessionVO.
        :type dst_host: str
        """
        self._dst_host = dst_host

    @property
    def dst_region_id(self):
        r"""Gets the dst_region_id of this SessionVO.

        **参数解释**： 目的regionID **取值范围**： 不涉及

        :return: The dst_region_id of this SessionVO.
        :rtype: str
        """
        return self._dst_region_id

    @dst_region_id.setter
    def dst_region_id(self, dst_region_id):
        r"""Sets the dst_region_id of this SessionVO.

        **参数解释**： 目的regionID **取值范围**： 不涉及

        :param dst_region_id: The dst_region_id of this SessionVO.
        :type dst_region_id: str
        """
        self._dst_region_id = dst_region_id

    @property
    def dst_region_name(self):
        r"""Gets the dst_region_name of this SessionVO.

        **参数解释**： 目的地区 **取值范围**： 不涉及

        :return: The dst_region_name of this SessionVO.
        :rtype: str
        """
        return self._dst_region_name

    @dst_region_name.setter
    def dst_region_name(self, dst_region_name):
        r"""Sets the dst_region_name of this SessionVO.

        **参数解释**： 目的地区 **取值范围**： 不涉及

        :param dst_region_name: The dst_region_name of this SessionVO.
        :type dst_region_name: str
        """
        self._dst_region_name = dst_region_name

    @property
    def end_time(self):
        r"""Gets the end_time of this SessionVO.

        **参数解释**： 结束时间 **取值范围**： 不涉及

        :return: The end_time of this SessionVO.
        :rtype: int
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        r"""Sets the end_time of this SessionVO.

        **参数解释**： 结束时间 **取值范围**： 不涉及

        :param end_time: The end_time of this SessionVO.
        :type end_time: int
        """
        self._end_time = end_time

    @property
    def protocol(self):
        r"""Gets the protocol of this SessionVO.

        **参数解释**： 协议 **取值范围**： 不涉及

        :return: The protocol of this SessionVO.
        :rtype: str
        """
        return self._protocol

    @protocol.setter
    def protocol(self, protocol):
        r"""Sets the protocol of this SessionVO.

        **参数解释**： 协议 **取值范围**： 不涉及

        :param protocol: The protocol of this SessionVO.
        :type protocol: str
        """
        self._protocol = protocol

    @property
    def request_byte(self):
        r"""Gets the request_byte of this SessionVO.

        **参数解释**： 请求字节数 **取值范围**： 不涉及

        :return: The request_byte of this SessionVO.
        :rtype: float
        """
        return self._request_byte

    @request_byte.setter
    def request_byte(self, request_byte):
        r"""Sets the request_byte of this SessionVO.

        **参数解释**： 请求字节数 **取值范围**： 不涉及

        :param request_byte: The request_byte of this SessionVO.
        :type request_byte: float
        """
        self._request_byte = request_byte

    @property
    def response_byte(self):
        r"""Gets the response_byte of this SessionVO.

        **参数解释**： 响应字节数 **取值范围**： 不涉及

        :return: The response_byte of this SessionVO.
        :rtype: float
        """
        return self._response_byte

    @response_byte.setter
    def response_byte(self, response_byte):
        r"""Sets the response_byte of this SessionVO.

        **参数解释**： 响应字节数 **取值范围**： 不涉及

        :param response_byte: The response_byte of this SessionVO.
        :type response_byte: float
        """
        self._response_byte = response_byte

    @property
    def sessions(self):
        r"""Gets the sessions of this SessionVO.

        **参数解释**： 会话数量 **取值范围**： 不涉及

        :return: The sessions of this SessionVO.
        :rtype: int
        """
        return self._sessions

    @sessions.setter
    def sessions(self, sessions):
        r"""Sets the sessions of this SessionVO.

        **参数解释**： 会话数量 **取值范围**： 不涉及

        :param sessions: The sessions of this SessionVO.
        :type sessions: int
        """
        self._sessions = sessions

    @property
    def src_associate_instance_type(self):
        r"""Gets the src_associate_instance_type of this SessionVO.

        **参数解释**： 源IP关联资产类型 **取值范围**： 不涉及

        :return: The src_associate_instance_type of this SessionVO.
        :rtype: str
        """
        return self._src_associate_instance_type

    @src_associate_instance_type.setter
    def src_associate_instance_type(self, src_associate_instance_type):
        r"""Sets the src_associate_instance_type of this SessionVO.

        **参数解释**： 源IP关联资产类型 **取值范围**： 不涉及

        :param src_associate_instance_type: The src_associate_instance_type of this SessionVO.
        :type src_associate_instance_type: str
        """
        self._src_associate_instance_type = src_associate_instance_type

    @property
    def src_device_name(self):
        r"""Gets the src_device_name of this SessionVO.

        **参数解释**： 源IP关联资产名称 **取值范围**： 不涉及

        :return: The src_device_name of this SessionVO.
        :rtype: str
        """
        return self._src_device_name

    @src_device_name.setter
    def src_device_name(self, src_device_name):
        r"""Sets the src_device_name of this SessionVO.

        **参数解释**： 源IP关联资产名称 **取值范围**： 不涉及

        :param src_device_name: The src_device_name of this SessionVO.
        :type src_device_name: str
        """
        self._src_device_name = src_device_name

    @property
    def src_ip(self):
        r"""Gets the src_ip of this SessionVO.

        **参数解释**： 源IP **取值范围**： 不涉及

        :return: The src_ip of this SessionVO.
        :rtype: str
        """
        return self._src_ip

    @src_ip.setter
    def src_ip(self, src_ip):
        r"""Sets the src_ip of this SessionVO.

        **参数解释**： 源IP **取值范围**： 不涉及

        :param src_ip: The src_ip of this SessionVO.
        :type src_ip: str
        """
        self._src_ip = src_ip

    @property
    def src_region_id(self):
        r"""Gets the src_region_id of this SessionVO.

        **参数解释**： 源地区 ID **取值范围**： 不涉及

        :return: The src_region_id of this SessionVO.
        :rtype: str
        """
        return self._src_region_id

    @src_region_id.setter
    def src_region_id(self, src_region_id):
        r"""Sets the src_region_id of this SessionVO.

        **参数解释**： 源地区 ID **取值范围**： 不涉及

        :param src_region_id: The src_region_id of this SessionVO.
        :type src_region_id: str
        """
        self._src_region_id = src_region_id

    @property
    def src_region_name(self):
        r"""Gets the src_region_name of this SessionVO.

        **参数解释**： 源地区 **取值范围**： 不涉及

        :return: The src_region_name of this SessionVO.
        :rtype: str
        """
        return self._src_region_name

    @src_region_name.setter
    def src_region_name(self, src_region_name):
        r"""Sets the src_region_name of this SessionVO.

        **参数解释**： 源地区 **取值范围**： 不涉及

        :param src_region_name: The src_region_name of this SessionVO.
        :type src_region_name: str
        """
        self._src_region_name = src_region_name

    @property
    def start_time(self):
        r"""Gets the start_time of this SessionVO.

        **参数解释**： 会话开始时间 **取值范围**： 不涉及

        :return: The start_time of this SessionVO.
        :rtype: int
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        r"""Sets the start_time of this SessionVO.

        **参数解释**： 会话开始时间 **取值范围**： 不涉及

        :param start_time: The start_time of this SessionVO.
        :type start_time: int
        """
        self._start_time = start_time

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
        if not isinstance(other, SessionVO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

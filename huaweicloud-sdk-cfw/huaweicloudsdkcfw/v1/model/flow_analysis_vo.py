# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class FlowAnalysisVO:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'app_count': 'int',
        'bytes': 'float',
        'dst_ip_count': 'int',
        'dst_port_count': 'int',
        'end_time': 'int',
        'records': 'list[SessionVO]',
        'request_byte': 'float',
        'response_byte': 'float',
        'sessions': 'int',
        'src_ip_count': 'int',
        'start_time': 'int'
    }

    attribute_map = {
        'app_count': 'app_count',
        'bytes': 'bytes',
        'dst_ip_count': 'dst_ip_count',
        'dst_port_count': 'dst_port_count',
        'end_time': 'end_time',
        'records': 'records',
        'request_byte': 'request_byte',
        'response_byte': 'response_byte',
        'sessions': 'sessions',
        'src_ip_count': 'src_ip_count',
        'start_time': 'start_time'
    }

    def __init__(self, app_count=None, bytes=None, dst_ip_count=None, dst_port_count=None, end_time=None, records=None, request_byte=None, response_byte=None, sessions=None, src_ip_count=None, start_time=None):
        r"""FlowAnalysisVO

        The model defined in huaweicloud sdk

        :param app_count: **参数解释**： 应用统计 **取值范围**： 不涉及
        :type app_count: int
        :param bytes: **参数解释**： 字节数 **取值范围**： 不涉及
        :type bytes: float
        :param dst_ip_count: **参数解释**： 目的IP计数 **取值范围**： 不涉及
        :type dst_ip_count: int
        :param dst_port_count: **参数**： 目的端口计数 **取值范围**： 不涉及
        :type dst_port_count: int
        :param end_time: **参数解释**： 结束时间 **取值范围**： 不涉及
        :type end_time: int
        :param records: **参数解释**： TOP会话详情 **取值范围**： 不涉及
        :type records: list[:class:`huaweicloudsdkcfw.v1.SessionVO`]
        :param request_byte: **参数解释**： 请求字节数 **取值范围**： 不涉及
        :type request_byte: float
        :param response_byte: **参数解释**： 响应字节数 **取值范围**： 不涉及
        :type response_byte: float
        :param sessions: **参数解释**： 会话次数 **取值范围**： 不涉及
        :type sessions: int
        :param src_ip_count: **参数解释**： 源IP计数 **取值范围**： 不涉及
        :type src_ip_count: int
        :param start_time: **参数解释**： 开始时间 **取值范围**： 不涉及
        :type start_time: int
        """
        
        

        self._app_count = None
        self._bytes = None
        self._dst_ip_count = None
        self._dst_port_count = None
        self._end_time = None
        self._records = None
        self._request_byte = None
        self._response_byte = None
        self._sessions = None
        self._src_ip_count = None
        self._start_time = None
        self.discriminator = None

        if app_count is not None:
            self.app_count = app_count
        if bytes is not None:
            self.bytes = bytes
        if dst_ip_count is not None:
            self.dst_ip_count = dst_ip_count
        if dst_port_count is not None:
            self.dst_port_count = dst_port_count
        if end_time is not None:
            self.end_time = end_time
        if records is not None:
            self.records = records
        if request_byte is not None:
            self.request_byte = request_byte
        if response_byte is not None:
            self.response_byte = response_byte
        if sessions is not None:
            self.sessions = sessions
        if src_ip_count is not None:
            self.src_ip_count = src_ip_count
        if start_time is not None:
            self.start_time = start_time

    @property
    def app_count(self):
        r"""Gets the app_count of this FlowAnalysisVO.

        **参数解释**： 应用统计 **取值范围**： 不涉及

        :return: The app_count of this FlowAnalysisVO.
        :rtype: int
        """
        return self._app_count

    @app_count.setter
    def app_count(self, app_count):
        r"""Sets the app_count of this FlowAnalysisVO.

        **参数解释**： 应用统计 **取值范围**： 不涉及

        :param app_count: The app_count of this FlowAnalysisVO.
        :type app_count: int
        """
        self._app_count = app_count

    @property
    def bytes(self):
        r"""Gets the bytes of this FlowAnalysisVO.

        **参数解释**： 字节数 **取值范围**： 不涉及

        :return: The bytes of this FlowAnalysisVO.
        :rtype: float
        """
        return self._bytes

    @bytes.setter
    def bytes(self, bytes):
        r"""Sets the bytes of this FlowAnalysisVO.

        **参数解释**： 字节数 **取值范围**： 不涉及

        :param bytes: The bytes of this FlowAnalysisVO.
        :type bytes: float
        """
        self._bytes = bytes

    @property
    def dst_ip_count(self):
        r"""Gets the dst_ip_count of this FlowAnalysisVO.

        **参数解释**： 目的IP计数 **取值范围**： 不涉及

        :return: The dst_ip_count of this FlowAnalysisVO.
        :rtype: int
        """
        return self._dst_ip_count

    @dst_ip_count.setter
    def dst_ip_count(self, dst_ip_count):
        r"""Sets the dst_ip_count of this FlowAnalysisVO.

        **参数解释**： 目的IP计数 **取值范围**： 不涉及

        :param dst_ip_count: The dst_ip_count of this FlowAnalysisVO.
        :type dst_ip_count: int
        """
        self._dst_ip_count = dst_ip_count

    @property
    def dst_port_count(self):
        r"""Gets the dst_port_count of this FlowAnalysisVO.

        **参数**： 目的端口计数 **取值范围**： 不涉及

        :return: The dst_port_count of this FlowAnalysisVO.
        :rtype: int
        """
        return self._dst_port_count

    @dst_port_count.setter
    def dst_port_count(self, dst_port_count):
        r"""Sets the dst_port_count of this FlowAnalysisVO.

        **参数**： 目的端口计数 **取值范围**： 不涉及

        :param dst_port_count: The dst_port_count of this FlowAnalysisVO.
        :type dst_port_count: int
        """
        self._dst_port_count = dst_port_count

    @property
    def end_time(self):
        r"""Gets the end_time of this FlowAnalysisVO.

        **参数解释**： 结束时间 **取值范围**： 不涉及

        :return: The end_time of this FlowAnalysisVO.
        :rtype: int
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        r"""Sets the end_time of this FlowAnalysisVO.

        **参数解释**： 结束时间 **取值范围**： 不涉及

        :param end_time: The end_time of this FlowAnalysisVO.
        :type end_time: int
        """
        self._end_time = end_time

    @property
    def records(self):
        r"""Gets the records of this FlowAnalysisVO.

        **参数解释**： TOP会话详情 **取值范围**： 不涉及

        :return: The records of this FlowAnalysisVO.
        :rtype: list[:class:`huaweicloudsdkcfw.v1.SessionVO`]
        """
        return self._records

    @records.setter
    def records(self, records):
        r"""Sets the records of this FlowAnalysisVO.

        **参数解释**： TOP会话详情 **取值范围**： 不涉及

        :param records: The records of this FlowAnalysisVO.
        :type records: list[:class:`huaweicloudsdkcfw.v1.SessionVO`]
        """
        self._records = records

    @property
    def request_byte(self):
        r"""Gets the request_byte of this FlowAnalysisVO.

        **参数解释**： 请求字节数 **取值范围**： 不涉及

        :return: The request_byte of this FlowAnalysisVO.
        :rtype: float
        """
        return self._request_byte

    @request_byte.setter
    def request_byte(self, request_byte):
        r"""Sets the request_byte of this FlowAnalysisVO.

        **参数解释**： 请求字节数 **取值范围**： 不涉及

        :param request_byte: The request_byte of this FlowAnalysisVO.
        :type request_byte: float
        """
        self._request_byte = request_byte

    @property
    def response_byte(self):
        r"""Gets the response_byte of this FlowAnalysisVO.

        **参数解释**： 响应字节数 **取值范围**： 不涉及

        :return: The response_byte of this FlowAnalysisVO.
        :rtype: float
        """
        return self._response_byte

    @response_byte.setter
    def response_byte(self, response_byte):
        r"""Sets the response_byte of this FlowAnalysisVO.

        **参数解释**： 响应字节数 **取值范围**： 不涉及

        :param response_byte: The response_byte of this FlowAnalysisVO.
        :type response_byte: float
        """
        self._response_byte = response_byte

    @property
    def sessions(self):
        r"""Gets the sessions of this FlowAnalysisVO.

        **参数解释**： 会话次数 **取值范围**： 不涉及

        :return: The sessions of this FlowAnalysisVO.
        :rtype: int
        """
        return self._sessions

    @sessions.setter
    def sessions(self, sessions):
        r"""Sets the sessions of this FlowAnalysisVO.

        **参数解释**： 会话次数 **取值范围**： 不涉及

        :param sessions: The sessions of this FlowAnalysisVO.
        :type sessions: int
        """
        self._sessions = sessions

    @property
    def src_ip_count(self):
        r"""Gets the src_ip_count of this FlowAnalysisVO.

        **参数解释**： 源IP计数 **取值范围**： 不涉及

        :return: The src_ip_count of this FlowAnalysisVO.
        :rtype: int
        """
        return self._src_ip_count

    @src_ip_count.setter
    def src_ip_count(self, src_ip_count):
        r"""Sets the src_ip_count of this FlowAnalysisVO.

        **参数解释**： 源IP计数 **取值范围**： 不涉及

        :param src_ip_count: The src_ip_count of this FlowAnalysisVO.
        :type src_ip_count: int
        """
        self._src_ip_count = src_ip_count

    @property
    def start_time(self):
        r"""Gets the start_time of this FlowAnalysisVO.

        **参数解释**： 开始时间 **取值范围**： 不涉及

        :return: The start_time of this FlowAnalysisVO.
        :rtype: int
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        r"""Sets the start_time of this FlowAnalysisVO.

        **参数解释**： 开始时间 **取值范围**： 不涉及

        :param start_time: The start_time of this FlowAnalysisVO.
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
        if not isinstance(other, FlowAnalysisVO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

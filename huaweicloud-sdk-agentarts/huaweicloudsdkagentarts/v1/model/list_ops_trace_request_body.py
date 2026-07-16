# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListOpsTraceRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'start_time': 'int',
        'end_time': 'int',
        'resource_id': 'str',
        'resource_type': 'str',
        'trace_id': 'str',
        'status_code': 'str',
        'session_id': 'str',
        'span_type': 'str',
        'input': 'str',
        'output': 'str',
        'like': 'int',
        'label': 'dict(str, str)',
        'page_no': 'int',
        'page_size': 'int',
        'filter_sign': 'str',
        'label_filter': 'list[FilterParam]',
        'filter': 'list[ListFilterParam]'
    }

    attribute_map = {
        'start_time': 'start_time',
        'end_time': 'end_time',
        'resource_id': 'resource_id',
        'resource_type': 'resource_type',
        'trace_id': 'trace_id',
        'status_code': 'status_code',
        'session_id': 'session_id',
        'span_type': 'span_type',
        'input': 'input',
        'output': 'output',
        'like': 'like',
        'label': 'label',
        'page_no': 'page_no',
        'page_size': 'page_size',
        'filter_sign': 'filter_sign',
        'label_filter': 'label_filter',
        'filter': 'filter'
    }

    def __init__(self, start_time=None, end_time=None, resource_id=None, resource_type=None, trace_id=None, status_code=None, session_id=None, span_type=None, input=None, output=None, like=None, label=None, page_no=None, page_size=None, filter_sign=None, label_filter=None, filter=None):
        r"""ListOpsTraceRequestBody

        The model defined in huaweicloud sdk

        :param start_time: 起始时间
        :type start_time: int
        :param end_time: 结束时间
        :type end_time: int
        :param resource_id: agent id
        :type resource_id: str
        :param resource_type: 资源类型
        :type resource_type: str
        :param trace_id: 调用链id
        :type trace_id: str
        :param status_code: 状态码
        :type status_code: str
        :param session_id: 会话id
        :type session_id: str
        :param span_type: span类型
        :type span_type: str
        :param input: 输入过滤词
        :type input: str
        :param output: 输出过滤词
        :type output: str
        :param like: 评价
        :type like: int
        :param label: 标注的过滤条件
        :type label: dict(str, str)
        :param page_no: 页码
        :type page_no: int
        :param page_size: 每页条数
        :type page_size: int
        :param filter_sign: 连接标识
        :type filter_sign: str
        :param label_filter: 标签过滤条件
        :type label_filter: list[:class:`huaweicloudsdkagentarts.v1.FilterParam`]
        :param filter: 过滤条件
        :type filter: list[:class:`huaweicloudsdkagentarts.v1.ListFilterParam`]
        """
        
        

        self._start_time = None
        self._end_time = None
        self._resource_id = None
        self._resource_type = None
        self._trace_id = None
        self._status_code = None
        self._session_id = None
        self._span_type = None
        self._input = None
        self._output = None
        self._like = None
        self._label = None
        self._page_no = None
        self._page_size = None
        self._filter_sign = None
        self._label_filter = None
        self._filter = None
        self.discriminator = None

        if start_time is not None:
            self.start_time = start_time
        if end_time is not None:
            self.end_time = end_time
        if resource_id is not None:
            self.resource_id = resource_id
        if resource_type is not None:
            self.resource_type = resource_type
        if trace_id is not None:
            self.trace_id = trace_id
        if status_code is not None:
            self.status_code = status_code
        if session_id is not None:
            self.session_id = session_id
        if span_type is not None:
            self.span_type = span_type
        if input is not None:
            self.input = input
        if output is not None:
            self.output = output
        if like is not None:
            self.like = like
        if label is not None:
            self.label = label
        if page_no is not None:
            self.page_no = page_no
        if page_size is not None:
            self.page_size = page_size
        if filter_sign is not None:
            self.filter_sign = filter_sign
        if label_filter is not None:
            self.label_filter = label_filter
        if filter is not None:
            self.filter = filter

    @property
    def start_time(self):
        r"""Gets the start_time of this ListOpsTraceRequestBody.

        起始时间

        :return: The start_time of this ListOpsTraceRequestBody.
        :rtype: int
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        r"""Sets the start_time of this ListOpsTraceRequestBody.

        起始时间

        :param start_time: The start_time of this ListOpsTraceRequestBody.
        :type start_time: int
        """
        self._start_time = start_time

    @property
    def end_time(self):
        r"""Gets the end_time of this ListOpsTraceRequestBody.

        结束时间

        :return: The end_time of this ListOpsTraceRequestBody.
        :rtype: int
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        r"""Sets the end_time of this ListOpsTraceRequestBody.

        结束时间

        :param end_time: The end_time of this ListOpsTraceRequestBody.
        :type end_time: int
        """
        self._end_time = end_time

    @property
    def resource_id(self):
        r"""Gets the resource_id of this ListOpsTraceRequestBody.

        agent id

        :return: The resource_id of this ListOpsTraceRequestBody.
        :rtype: str
        """
        return self._resource_id

    @resource_id.setter
    def resource_id(self, resource_id):
        r"""Sets the resource_id of this ListOpsTraceRequestBody.

        agent id

        :param resource_id: The resource_id of this ListOpsTraceRequestBody.
        :type resource_id: str
        """
        self._resource_id = resource_id

    @property
    def resource_type(self):
        r"""Gets the resource_type of this ListOpsTraceRequestBody.

        资源类型

        :return: The resource_type of this ListOpsTraceRequestBody.
        :rtype: str
        """
        return self._resource_type

    @resource_type.setter
    def resource_type(self, resource_type):
        r"""Sets the resource_type of this ListOpsTraceRequestBody.

        资源类型

        :param resource_type: The resource_type of this ListOpsTraceRequestBody.
        :type resource_type: str
        """
        self._resource_type = resource_type

    @property
    def trace_id(self):
        r"""Gets the trace_id of this ListOpsTraceRequestBody.

        调用链id

        :return: The trace_id of this ListOpsTraceRequestBody.
        :rtype: str
        """
        return self._trace_id

    @trace_id.setter
    def trace_id(self, trace_id):
        r"""Sets the trace_id of this ListOpsTraceRequestBody.

        调用链id

        :param trace_id: The trace_id of this ListOpsTraceRequestBody.
        :type trace_id: str
        """
        self._trace_id = trace_id

    @property
    def status_code(self):
        r"""Gets the status_code of this ListOpsTraceRequestBody.

        状态码

        :return: The status_code of this ListOpsTraceRequestBody.
        :rtype: str
        """
        return self._status_code

    @status_code.setter
    def status_code(self, status_code):
        r"""Sets the status_code of this ListOpsTraceRequestBody.

        状态码

        :param status_code: The status_code of this ListOpsTraceRequestBody.
        :type status_code: str
        """
        self._status_code = status_code

    @property
    def session_id(self):
        r"""Gets the session_id of this ListOpsTraceRequestBody.

        会话id

        :return: The session_id of this ListOpsTraceRequestBody.
        :rtype: str
        """
        return self._session_id

    @session_id.setter
    def session_id(self, session_id):
        r"""Sets the session_id of this ListOpsTraceRequestBody.

        会话id

        :param session_id: The session_id of this ListOpsTraceRequestBody.
        :type session_id: str
        """
        self._session_id = session_id

    @property
    def span_type(self):
        r"""Gets the span_type of this ListOpsTraceRequestBody.

        span类型

        :return: The span_type of this ListOpsTraceRequestBody.
        :rtype: str
        """
        return self._span_type

    @span_type.setter
    def span_type(self, span_type):
        r"""Sets the span_type of this ListOpsTraceRequestBody.

        span类型

        :param span_type: The span_type of this ListOpsTraceRequestBody.
        :type span_type: str
        """
        self._span_type = span_type

    @property
    def input(self):
        r"""Gets the input of this ListOpsTraceRequestBody.

        输入过滤词

        :return: The input of this ListOpsTraceRequestBody.
        :rtype: str
        """
        return self._input

    @input.setter
    def input(self, input):
        r"""Sets the input of this ListOpsTraceRequestBody.

        输入过滤词

        :param input: The input of this ListOpsTraceRequestBody.
        :type input: str
        """
        self._input = input

    @property
    def output(self):
        r"""Gets the output of this ListOpsTraceRequestBody.

        输出过滤词

        :return: The output of this ListOpsTraceRequestBody.
        :rtype: str
        """
        return self._output

    @output.setter
    def output(self, output):
        r"""Sets the output of this ListOpsTraceRequestBody.

        输出过滤词

        :param output: The output of this ListOpsTraceRequestBody.
        :type output: str
        """
        self._output = output

    @property
    def like(self):
        r"""Gets the like of this ListOpsTraceRequestBody.

        评价

        :return: The like of this ListOpsTraceRequestBody.
        :rtype: int
        """
        return self._like

    @like.setter
    def like(self, like):
        r"""Sets the like of this ListOpsTraceRequestBody.

        评价

        :param like: The like of this ListOpsTraceRequestBody.
        :type like: int
        """
        self._like = like

    @property
    def label(self):
        r"""Gets the label of this ListOpsTraceRequestBody.

        标注的过滤条件

        :return: The label of this ListOpsTraceRequestBody.
        :rtype: dict(str, str)
        """
        return self._label

    @label.setter
    def label(self, label):
        r"""Sets the label of this ListOpsTraceRequestBody.

        标注的过滤条件

        :param label: The label of this ListOpsTraceRequestBody.
        :type label: dict(str, str)
        """
        self._label = label

    @property
    def page_no(self):
        r"""Gets the page_no of this ListOpsTraceRequestBody.

        页码

        :return: The page_no of this ListOpsTraceRequestBody.
        :rtype: int
        """
        return self._page_no

    @page_no.setter
    def page_no(self, page_no):
        r"""Sets the page_no of this ListOpsTraceRequestBody.

        页码

        :param page_no: The page_no of this ListOpsTraceRequestBody.
        :type page_no: int
        """
        self._page_no = page_no

    @property
    def page_size(self):
        r"""Gets the page_size of this ListOpsTraceRequestBody.

        每页条数

        :return: The page_size of this ListOpsTraceRequestBody.
        :rtype: int
        """
        return self._page_size

    @page_size.setter
    def page_size(self, page_size):
        r"""Sets the page_size of this ListOpsTraceRequestBody.

        每页条数

        :param page_size: The page_size of this ListOpsTraceRequestBody.
        :type page_size: int
        """
        self._page_size = page_size

    @property
    def filter_sign(self):
        r"""Gets the filter_sign of this ListOpsTraceRequestBody.

        连接标识

        :return: The filter_sign of this ListOpsTraceRequestBody.
        :rtype: str
        """
        return self._filter_sign

    @filter_sign.setter
    def filter_sign(self, filter_sign):
        r"""Sets the filter_sign of this ListOpsTraceRequestBody.

        连接标识

        :param filter_sign: The filter_sign of this ListOpsTraceRequestBody.
        :type filter_sign: str
        """
        self._filter_sign = filter_sign

    @property
    def label_filter(self):
        r"""Gets the label_filter of this ListOpsTraceRequestBody.

        标签过滤条件

        :return: The label_filter of this ListOpsTraceRequestBody.
        :rtype: list[:class:`huaweicloudsdkagentarts.v1.FilterParam`]
        """
        return self._label_filter

    @label_filter.setter
    def label_filter(self, label_filter):
        r"""Sets the label_filter of this ListOpsTraceRequestBody.

        标签过滤条件

        :param label_filter: The label_filter of this ListOpsTraceRequestBody.
        :type label_filter: list[:class:`huaweicloudsdkagentarts.v1.FilterParam`]
        """
        self._label_filter = label_filter

    @property
    def filter(self):
        r"""Gets the filter of this ListOpsTraceRequestBody.

        过滤条件

        :return: The filter of this ListOpsTraceRequestBody.
        :rtype: list[:class:`huaweicloudsdkagentarts.v1.ListFilterParam`]
        """
        return self._filter

    @filter.setter
    def filter(self, filter):
        r"""Sets the filter of this ListOpsTraceRequestBody.

        过滤条件

        :param filter: The filter of this ListOpsTraceRequestBody.
        :type filter: list[:class:`huaweicloudsdkagentarts.v1.ListFilterParam`]
        """
        self._filter = filter

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
        if not isinstance(other, ListOpsTraceRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

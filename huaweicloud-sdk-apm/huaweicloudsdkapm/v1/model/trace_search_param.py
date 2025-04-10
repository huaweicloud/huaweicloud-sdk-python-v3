# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class TraceSearchParam:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'region': 'str',
        'order_param': 'OrderParam',
        'real_source_full_match': 'bool',
        'source_full_match': 'bool',
        'tags_content': 'str',
        'start_time_string': 'str',
        'end_time_string': 'str',
        'time_used_min': 'int',
        'time_used_max': 'str',
        'contain_tags_content': 'bool',
        'page_size': 'int',
        'page': 'int',
        'parameters': 'str',
        'codes': 'list[int]',
        'global_trace_id': 'str',
        'global_path': 'str',
        'trace_id': 'str',
        'span_id': 'str',
        'env_id': 'int',
        'instance_id': 'int',
        'app_id': 'int',
        'biz_id': 'int',
        'domain_id': 'int',
        'source': 'str',
        'real_source': 'str',
        'start_time': 'int',
        'time_used': 'int',
        'code': 'int',
        'class_name': 'str',
        'is_async': 'bool',
        'tags': 'dict(str, str)',
        'has_error': 'bool',
        'error_reasons': 'str',
        'type': 'str',
        'http_method': 'str',
        'biz_code': 'str'
    }

    attribute_map = {
        'region': 'region',
        'order_param': 'order_param',
        'real_source_full_match': 'real_source_full_match',
        'source_full_match': 'source_full_match',
        'tags_content': 'tags_content',
        'start_time_string': 'start_time_string',
        'end_time_string': 'end_time_string',
        'time_used_min': 'time_used_min',
        'time_used_max': 'time_used_max',
        'contain_tags_content': 'contain_tags_content',
        'page_size': 'page_size',
        'page': 'page',
        'parameters': 'parameters',
        'codes': 'codes',
        'global_trace_id': 'global_trace_id',
        'global_path': 'global_path',
        'trace_id': 'trace_id',
        'span_id': 'span_id',
        'env_id': 'env_id',
        'instance_id': 'instance_id',
        'app_id': 'app_id',
        'biz_id': 'biz_id',
        'domain_id': 'domain_id',
        'source': 'source',
        'real_source': 'real_source',
        'start_time': 'start_time',
        'time_used': 'time_used',
        'code': 'code',
        'class_name': 'class_name',
        'is_async': 'is_async',
        'tags': 'tags',
        'has_error': 'has_error',
        'error_reasons': 'error_reasons',
        'type': 'type',
        'http_method': 'http_method',
        'biz_code': 'biz_code'
    }

    def __init__(self, region=None, order_param=None, real_source_full_match=None, source_full_match=None, tags_content=None, start_time_string=None, end_time_string=None, time_used_min=None, time_used_max=None, contain_tags_content=None, page_size=None, page=None, parameters=None, codes=None, global_trace_id=None, global_path=None, trace_id=None, span_id=None, env_id=None, instance_id=None, app_id=None, biz_id=None, domain_id=None, source=None, real_source=None, start_time=None, time_used=None, code=None, class_name=None, is_async=None, tags=None, has_error=None, error_reasons=None, type=None, http_method=None, biz_code=None):
        r"""TraceSearchParam

        The model defined in huaweicloud sdk

        :param region: region名称。
        :type region: str
        :param order_param: 
        :type order_param: :class:`huaweicloudsdkapm.v1.OrderParam`
        :param real_source_full_match: 是否为精确搜索。
        :type real_source_full_match: bool
        :param source_full_match: 全匹配搜索。
        :type source_full_match: bool
        :param tags_content: header或body体，或自定义参数，或其他tags里字段的关键词搜索。
        :type tags_content: str
        :param start_time_string: 开始时间。
        :type start_time_string: str
        :param end_time_string: 结束时间。
        :type end_time_string: str
        :param time_used_min: 最小耗时。
        :type time_used_min: int
        :param time_used_max: 最大耗时。
        :type time_used_max: str
        :param contain_tags_content: 搜索结果是否包含tags内容详情。
        :type contain_tags_content: bool
        :param page_size: 每一页返回的行数。
        :type page_size: int
        :param page: 查询第几页的数据,默认查询第一页。
        :type page: int
        :param parameters: 参数。
        :type parameters: str
        :param codes: 字符串格式的的状态码，用于支持多个状态码查询。
        :type codes: list[int]
        :param global_trace_id: vTraceId，虚拟traceId，一个vTraceId对应多个实际的traceId， vTraceId会从开始一直往下应用传输。
        :type global_trace_id: str
        :param global_path: 虚拟traceId经过的path路径。
        :type global_path: str
        :param trace_id: 在root的span调用产生的全局id，以此往后透传。
        :type trace_id: str
        :param span_id: 代表一次rpc的调用的id，对于root的调用，值为字符串1，对于当前span调用的下一个spanId编号为1-1,1-2等格式，以此往后类推。
        :type span_id: str
        :param env_id: 环境id。
        :type env_id: int
        :param instance_id: 实例id。
        :type instance_id: int
        :param app_id: 组件id。
        :type app_id: int
        :param biz_id: 应用id。
        :type biz_id: int
        :param domain_id: 租户id。
        :type domain_id: int
        :param source: 只有是根event也就是span的时候有值。
        :type source: str
        :param real_source: 根event 的时候存在，实际调用的url。
        :type real_source: str
        :param start_time: 开始时间。
        :type start_time: int
        :param time_used: 耗时。
        :type time_used: int
        :param code: 状态码，针对http的调用有效。
        :type code: int
        :param class_name: 类名。
        :type class_name: str
        :param is_async: 是否异步的event。
        :type is_async: bool
        :param tags: 包含用户自定义参数，header或body体里的内容，httpMethod, bizCode，以及后续可能新增参数。
        :type tags: dict(str, str)
        :param has_error: 是否有错误。
        :type has_error: bool
        :param error_reasons: 错误类型。
        :type error_reasons: str
        :param type: 类型。
        :type type: str
        :param http_method: 这里的method实际上是tags里面的http_method，只有url监控项才有。
        :type http_method: str
        :param biz_code: 业务状态码的采集。
        :type biz_code: str
        """
        
        

        self._region = None
        self._order_param = None
        self._real_source_full_match = None
        self._source_full_match = None
        self._tags_content = None
        self._start_time_string = None
        self._end_time_string = None
        self._time_used_min = None
        self._time_used_max = None
        self._contain_tags_content = None
        self._page_size = None
        self._page = None
        self._parameters = None
        self._codes = None
        self._global_trace_id = None
        self._global_path = None
        self._trace_id = None
        self._span_id = None
        self._env_id = None
        self._instance_id = None
        self._app_id = None
        self._biz_id = None
        self._domain_id = None
        self._source = None
        self._real_source = None
        self._start_time = None
        self._time_used = None
        self._code = None
        self._class_name = None
        self._is_async = None
        self._tags = None
        self._has_error = None
        self._error_reasons = None
        self._type = None
        self._http_method = None
        self._biz_code = None
        self.discriminator = None

        self.region = region
        if order_param is not None:
            self.order_param = order_param
        if real_source_full_match is not None:
            self.real_source_full_match = real_source_full_match
        if source_full_match is not None:
            self.source_full_match = source_full_match
        if tags_content is not None:
            self.tags_content = tags_content
        if start_time_string is not None:
            self.start_time_string = start_time_string
        if end_time_string is not None:
            self.end_time_string = end_time_string
        if time_used_min is not None:
            self.time_used_min = time_used_min
        if time_used_max is not None:
            self.time_used_max = time_used_max
        if contain_tags_content is not None:
            self.contain_tags_content = contain_tags_content
        if page_size is not None:
            self.page_size = page_size
        if page is not None:
            self.page = page
        if parameters is not None:
            self.parameters = parameters
        if codes is not None:
            self.codes = codes
        if global_trace_id is not None:
            self.global_trace_id = global_trace_id
        if global_path is not None:
            self.global_path = global_path
        if trace_id is not None:
            self.trace_id = trace_id
        if span_id is not None:
            self.span_id = span_id
        if env_id is not None:
            self.env_id = env_id
        if instance_id is not None:
            self.instance_id = instance_id
        if app_id is not None:
            self.app_id = app_id
        self.biz_id = biz_id
        if domain_id is not None:
            self.domain_id = domain_id
        if source is not None:
            self.source = source
        if real_source is not None:
            self.real_source = real_source
        if start_time is not None:
            self.start_time = start_time
        if time_used is not None:
            self.time_used = time_used
        if code is not None:
            self.code = code
        if class_name is not None:
            self.class_name = class_name
        if is_async is not None:
            self.is_async = is_async
        if tags is not None:
            self.tags = tags
        if has_error is not None:
            self.has_error = has_error
        if error_reasons is not None:
            self.error_reasons = error_reasons
        if type is not None:
            self.type = type
        if http_method is not None:
            self.http_method = http_method
        if biz_code is not None:
            self.biz_code = biz_code

    @property
    def region(self):
        r"""Gets the region of this TraceSearchParam.

        region名称。

        :return: The region of this TraceSearchParam.
        :rtype: str
        """
        return self._region

    @region.setter
    def region(self, region):
        r"""Sets the region of this TraceSearchParam.

        region名称。

        :param region: The region of this TraceSearchParam.
        :type region: str
        """
        self._region = region

    @property
    def order_param(self):
        r"""Gets the order_param of this TraceSearchParam.

        :return: The order_param of this TraceSearchParam.
        :rtype: :class:`huaweicloudsdkapm.v1.OrderParam`
        """
        return self._order_param

    @order_param.setter
    def order_param(self, order_param):
        r"""Sets the order_param of this TraceSearchParam.

        :param order_param: The order_param of this TraceSearchParam.
        :type order_param: :class:`huaweicloudsdkapm.v1.OrderParam`
        """
        self._order_param = order_param

    @property
    def real_source_full_match(self):
        r"""Gets the real_source_full_match of this TraceSearchParam.

        是否为精确搜索。

        :return: The real_source_full_match of this TraceSearchParam.
        :rtype: bool
        """
        return self._real_source_full_match

    @real_source_full_match.setter
    def real_source_full_match(self, real_source_full_match):
        r"""Sets the real_source_full_match of this TraceSearchParam.

        是否为精确搜索。

        :param real_source_full_match: The real_source_full_match of this TraceSearchParam.
        :type real_source_full_match: bool
        """
        self._real_source_full_match = real_source_full_match

    @property
    def source_full_match(self):
        r"""Gets the source_full_match of this TraceSearchParam.

        全匹配搜索。

        :return: The source_full_match of this TraceSearchParam.
        :rtype: bool
        """
        return self._source_full_match

    @source_full_match.setter
    def source_full_match(self, source_full_match):
        r"""Sets the source_full_match of this TraceSearchParam.

        全匹配搜索。

        :param source_full_match: The source_full_match of this TraceSearchParam.
        :type source_full_match: bool
        """
        self._source_full_match = source_full_match

    @property
    def tags_content(self):
        r"""Gets the tags_content of this TraceSearchParam.

        header或body体，或自定义参数，或其他tags里字段的关键词搜索。

        :return: The tags_content of this TraceSearchParam.
        :rtype: str
        """
        return self._tags_content

    @tags_content.setter
    def tags_content(self, tags_content):
        r"""Sets the tags_content of this TraceSearchParam.

        header或body体，或自定义参数，或其他tags里字段的关键词搜索。

        :param tags_content: The tags_content of this TraceSearchParam.
        :type tags_content: str
        """
        self._tags_content = tags_content

    @property
    def start_time_string(self):
        r"""Gets the start_time_string of this TraceSearchParam.

        开始时间。

        :return: The start_time_string of this TraceSearchParam.
        :rtype: str
        """
        return self._start_time_string

    @start_time_string.setter
    def start_time_string(self, start_time_string):
        r"""Sets the start_time_string of this TraceSearchParam.

        开始时间。

        :param start_time_string: The start_time_string of this TraceSearchParam.
        :type start_time_string: str
        """
        self._start_time_string = start_time_string

    @property
    def end_time_string(self):
        r"""Gets the end_time_string of this TraceSearchParam.

        结束时间。

        :return: The end_time_string of this TraceSearchParam.
        :rtype: str
        """
        return self._end_time_string

    @end_time_string.setter
    def end_time_string(self, end_time_string):
        r"""Sets the end_time_string of this TraceSearchParam.

        结束时间。

        :param end_time_string: The end_time_string of this TraceSearchParam.
        :type end_time_string: str
        """
        self._end_time_string = end_time_string

    @property
    def time_used_min(self):
        r"""Gets the time_used_min of this TraceSearchParam.

        最小耗时。

        :return: The time_used_min of this TraceSearchParam.
        :rtype: int
        """
        return self._time_used_min

    @time_used_min.setter
    def time_used_min(self, time_used_min):
        r"""Sets the time_used_min of this TraceSearchParam.

        最小耗时。

        :param time_used_min: The time_used_min of this TraceSearchParam.
        :type time_used_min: int
        """
        self._time_used_min = time_used_min

    @property
    def time_used_max(self):
        r"""Gets the time_used_max of this TraceSearchParam.

        最大耗时。

        :return: The time_used_max of this TraceSearchParam.
        :rtype: str
        """
        return self._time_used_max

    @time_used_max.setter
    def time_used_max(self, time_used_max):
        r"""Sets the time_used_max of this TraceSearchParam.

        最大耗时。

        :param time_used_max: The time_used_max of this TraceSearchParam.
        :type time_used_max: str
        """
        self._time_used_max = time_used_max

    @property
    def contain_tags_content(self):
        r"""Gets the contain_tags_content of this TraceSearchParam.

        搜索结果是否包含tags内容详情。

        :return: The contain_tags_content of this TraceSearchParam.
        :rtype: bool
        """
        return self._contain_tags_content

    @contain_tags_content.setter
    def contain_tags_content(self, contain_tags_content):
        r"""Sets the contain_tags_content of this TraceSearchParam.

        搜索结果是否包含tags内容详情。

        :param contain_tags_content: The contain_tags_content of this TraceSearchParam.
        :type contain_tags_content: bool
        """
        self._contain_tags_content = contain_tags_content

    @property
    def page_size(self):
        r"""Gets the page_size of this TraceSearchParam.

        每一页返回的行数。

        :return: The page_size of this TraceSearchParam.
        :rtype: int
        """
        return self._page_size

    @page_size.setter
    def page_size(self, page_size):
        r"""Sets the page_size of this TraceSearchParam.

        每一页返回的行数。

        :param page_size: The page_size of this TraceSearchParam.
        :type page_size: int
        """
        self._page_size = page_size

    @property
    def page(self):
        r"""Gets the page of this TraceSearchParam.

        查询第几页的数据,默认查询第一页。

        :return: The page of this TraceSearchParam.
        :rtype: int
        """
        return self._page

    @page.setter
    def page(self, page):
        r"""Sets the page of this TraceSearchParam.

        查询第几页的数据,默认查询第一页。

        :param page: The page of this TraceSearchParam.
        :type page: int
        """
        self._page = page

    @property
    def parameters(self):
        r"""Gets the parameters of this TraceSearchParam.

        参数。

        :return: The parameters of this TraceSearchParam.
        :rtype: str
        """
        return self._parameters

    @parameters.setter
    def parameters(self, parameters):
        r"""Sets the parameters of this TraceSearchParam.

        参数。

        :param parameters: The parameters of this TraceSearchParam.
        :type parameters: str
        """
        self._parameters = parameters

    @property
    def codes(self):
        r"""Gets the codes of this TraceSearchParam.

        字符串格式的的状态码，用于支持多个状态码查询。

        :return: The codes of this TraceSearchParam.
        :rtype: list[int]
        """
        return self._codes

    @codes.setter
    def codes(self, codes):
        r"""Sets the codes of this TraceSearchParam.

        字符串格式的的状态码，用于支持多个状态码查询。

        :param codes: The codes of this TraceSearchParam.
        :type codes: list[int]
        """
        self._codes = codes

    @property
    def global_trace_id(self):
        r"""Gets the global_trace_id of this TraceSearchParam.

        vTraceId，虚拟traceId，一个vTraceId对应多个实际的traceId， vTraceId会从开始一直往下应用传输。

        :return: The global_trace_id of this TraceSearchParam.
        :rtype: str
        """
        return self._global_trace_id

    @global_trace_id.setter
    def global_trace_id(self, global_trace_id):
        r"""Sets the global_trace_id of this TraceSearchParam.

        vTraceId，虚拟traceId，一个vTraceId对应多个实际的traceId， vTraceId会从开始一直往下应用传输。

        :param global_trace_id: The global_trace_id of this TraceSearchParam.
        :type global_trace_id: str
        """
        self._global_trace_id = global_trace_id

    @property
    def global_path(self):
        r"""Gets the global_path of this TraceSearchParam.

        虚拟traceId经过的path路径。

        :return: The global_path of this TraceSearchParam.
        :rtype: str
        """
        return self._global_path

    @global_path.setter
    def global_path(self, global_path):
        r"""Sets the global_path of this TraceSearchParam.

        虚拟traceId经过的path路径。

        :param global_path: The global_path of this TraceSearchParam.
        :type global_path: str
        """
        self._global_path = global_path

    @property
    def trace_id(self):
        r"""Gets the trace_id of this TraceSearchParam.

        在root的span调用产生的全局id，以此往后透传。

        :return: The trace_id of this TraceSearchParam.
        :rtype: str
        """
        return self._trace_id

    @trace_id.setter
    def trace_id(self, trace_id):
        r"""Sets the trace_id of this TraceSearchParam.

        在root的span调用产生的全局id，以此往后透传。

        :param trace_id: The trace_id of this TraceSearchParam.
        :type trace_id: str
        """
        self._trace_id = trace_id

    @property
    def span_id(self):
        r"""Gets the span_id of this TraceSearchParam.

        代表一次rpc的调用的id，对于root的调用，值为字符串1，对于当前span调用的下一个spanId编号为1-1,1-2等格式，以此往后类推。

        :return: The span_id of this TraceSearchParam.
        :rtype: str
        """
        return self._span_id

    @span_id.setter
    def span_id(self, span_id):
        r"""Sets the span_id of this TraceSearchParam.

        代表一次rpc的调用的id，对于root的调用，值为字符串1，对于当前span调用的下一个spanId编号为1-1,1-2等格式，以此往后类推。

        :param span_id: The span_id of this TraceSearchParam.
        :type span_id: str
        """
        self._span_id = span_id

    @property
    def env_id(self):
        r"""Gets the env_id of this TraceSearchParam.

        环境id。

        :return: The env_id of this TraceSearchParam.
        :rtype: int
        """
        return self._env_id

    @env_id.setter
    def env_id(self, env_id):
        r"""Sets the env_id of this TraceSearchParam.

        环境id。

        :param env_id: The env_id of this TraceSearchParam.
        :type env_id: int
        """
        self._env_id = env_id

    @property
    def instance_id(self):
        r"""Gets the instance_id of this TraceSearchParam.

        实例id。

        :return: The instance_id of this TraceSearchParam.
        :rtype: int
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        r"""Sets the instance_id of this TraceSearchParam.

        实例id。

        :param instance_id: The instance_id of this TraceSearchParam.
        :type instance_id: int
        """
        self._instance_id = instance_id

    @property
    def app_id(self):
        r"""Gets the app_id of this TraceSearchParam.

        组件id。

        :return: The app_id of this TraceSearchParam.
        :rtype: int
        """
        return self._app_id

    @app_id.setter
    def app_id(self, app_id):
        r"""Sets the app_id of this TraceSearchParam.

        组件id。

        :param app_id: The app_id of this TraceSearchParam.
        :type app_id: int
        """
        self._app_id = app_id

    @property
    def biz_id(self):
        r"""Gets the biz_id of this TraceSearchParam.

        应用id。

        :return: The biz_id of this TraceSearchParam.
        :rtype: int
        """
        return self._biz_id

    @biz_id.setter
    def biz_id(self, biz_id):
        r"""Sets the biz_id of this TraceSearchParam.

        应用id。

        :param biz_id: The biz_id of this TraceSearchParam.
        :type biz_id: int
        """
        self._biz_id = biz_id

    @property
    def domain_id(self):
        r"""Gets the domain_id of this TraceSearchParam.

        租户id。

        :return: The domain_id of this TraceSearchParam.
        :rtype: int
        """
        return self._domain_id

    @domain_id.setter
    def domain_id(self, domain_id):
        r"""Sets the domain_id of this TraceSearchParam.

        租户id。

        :param domain_id: The domain_id of this TraceSearchParam.
        :type domain_id: int
        """
        self._domain_id = domain_id

    @property
    def source(self):
        r"""Gets the source of this TraceSearchParam.

        只有是根event也就是span的时候有值。

        :return: The source of this TraceSearchParam.
        :rtype: str
        """
        return self._source

    @source.setter
    def source(self, source):
        r"""Sets the source of this TraceSearchParam.

        只有是根event也就是span的时候有值。

        :param source: The source of this TraceSearchParam.
        :type source: str
        """
        self._source = source

    @property
    def real_source(self):
        r"""Gets the real_source of this TraceSearchParam.

        根event 的时候存在，实际调用的url。

        :return: The real_source of this TraceSearchParam.
        :rtype: str
        """
        return self._real_source

    @real_source.setter
    def real_source(self, real_source):
        r"""Sets the real_source of this TraceSearchParam.

        根event 的时候存在，实际调用的url。

        :param real_source: The real_source of this TraceSearchParam.
        :type real_source: str
        """
        self._real_source = real_source

    @property
    def start_time(self):
        r"""Gets the start_time of this TraceSearchParam.

        开始时间。

        :return: The start_time of this TraceSearchParam.
        :rtype: int
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        r"""Sets the start_time of this TraceSearchParam.

        开始时间。

        :param start_time: The start_time of this TraceSearchParam.
        :type start_time: int
        """
        self._start_time = start_time

    @property
    def time_used(self):
        r"""Gets the time_used of this TraceSearchParam.

        耗时。

        :return: The time_used of this TraceSearchParam.
        :rtype: int
        """
        return self._time_used

    @time_used.setter
    def time_used(self, time_used):
        r"""Sets the time_used of this TraceSearchParam.

        耗时。

        :param time_used: The time_used of this TraceSearchParam.
        :type time_used: int
        """
        self._time_used = time_used

    @property
    def code(self):
        r"""Gets the code of this TraceSearchParam.

        状态码，针对http的调用有效。

        :return: The code of this TraceSearchParam.
        :rtype: int
        """
        return self._code

    @code.setter
    def code(self, code):
        r"""Sets the code of this TraceSearchParam.

        状态码，针对http的调用有效。

        :param code: The code of this TraceSearchParam.
        :type code: int
        """
        self._code = code

    @property
    def class_name(self):
        r"""Gets the class_name of this TraceSearchParam.

        类名。

        :return: The class_name of this TraceSearchParam.
        :rtype: str
        """
        return self._class_name

    @class_name.setter
    def class_name(self, class_name):
        r"""Sets the class_name of this TraceSearchParam.

        类名。

        :param class_name: The class_name of this TraceSearchParam.
        :type class_name: str
        """
        self._class_name = class_name

    @property
    def is_async(self):
        r"""Gets the is_async of this TraceSearchParam.

        是否异步的event。

        :return: The is_async of this TraceSearchParam.
        :rtype: bool
        """
        return self._is_async

    @is_async.setter
    def is_async(self, is_async):
        r"""Sets the is_async of this TraceSearchParam.

        是否异步的event。

        :param is_async: The is_async of this TraceSearchParam.
        :type is_async: bool
        """
        self._is_async = is_async

    @property
    def tags(self):
        r"""Gets the tags of this TraceSearchParam.

        包含用户自定义参数，header或body体里的内容，httpMethod, bizCode，以及后续可能新增参数。

        :return: The tags of this TraceSearchParam.
        :rtype: dict(str, str)
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        r"""Sets the tags of this TraceSearchParam.

        包含用户自定义参数，header或body体里的内容，httpMethod, bizCode，以及后续可能新增参数。

        :param tags: The tags of this TraceSearchParam.
        :type tags: dict(str, str)
        """
        self._tags = tags

    @property
    def has_error(self):
        r"""Gets the has_error of this TraceSearchParam.

        是否有错误。

        :return: The has_error of this TraceSearchParam.
        :rtype: bool
        """
        return self._has_error

    @has_error.setter
    def has_error(self, has_error):
        r"""Sets the has_error of this TraceSearchParam.

        是否有错误。

        :param has_error: The has_error of this TraceSearchParam.
        :type has_error: bool
        """
        self._has_error = has_error

    @property
    def error_reasons(self):
        r"""Gets the error_reasons of this TraceSearchParam.

        错误类型。

        :return: The error_reasons of this TraceSearchParam.
        :rtype: str
        """
        return self._error_reasons

    @error_reasons.setter
    def error_reasons(self, error_reasons):
        r"""Sets the error_reasons of this TraceSearchParam.

        错误类型。

        :param error_reasons: The error_reasons of this TraceSearchParam.
        :type error_reasons: str
        """
        self._error_reasons = error_reasons

    @property
    def type(self):
        r"""Gets the type of this TraceSearchParam.

        类型。

        :return: The type of this TraceSearchParam.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this TraceSearchParam.

        类型。

        :param type: The type of this TraceSearchParam.
        :type type: str
        """
        self._type = type

    @property
    def http_method(self):
        r"""Gets the http_method of this TraceSearchParam.

        这里的method实际上是tags里面的http_method，只有url监控项才有。

        :return: The http_method of this TraceSearchParam.
        :rtype: str
        """
        return self._http_method

    @http_method.setter
    def http_method(self, http_method):
        r"""Sets the http_method of this TraceSearchParam.

        这里的method实际上是tags里面的http_method，只有url监控项才有。

        :param http_method: The http_method of this TraceSearchParam.
        :type http_method: str
        """
        self._http_method = http_method

    @property
    def biz_code(self):
        r"""Gets the biz_code of this TraceSearchParam.

        业务状态码的采集。

        :return: The biz_code of this TraceSearchParam.
        :rtype: str
        """
        return self._biz_code

    @biz_code.setter
    def biz_code(self, biz_code):
        r"""Sets the biz_code of this TraceSearchParam.

        业务状态码的采集。

        :param biz_code: The biz_code of this TraceSearchParam.
        :type biz_code: str
        """
        self._biz_code = biz_code

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
        if not isinstance(other, TraceSearchParam):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

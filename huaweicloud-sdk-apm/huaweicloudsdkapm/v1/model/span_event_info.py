# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SpanEventInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'env_name': 'str',
        'app_name': 'str',
        'indent': 'int',
        'region': 'str',
        'host_name': 'str',
        'ip_address': 'str',
        'instance_name': 'str',
        'event_id': 'str',
        'next_span_id': 'str',
        'source_event_id': 'str',
        'method': 'str',
        'children_event_count': 'int',
        'discard': 'list[DiscardInfo]',
        'argument': 'str',
        'attachment': 'dict(str, str)',
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
        'biz_code': 'str',
        'id': 'str'
    }

    attribute_map = {
        'env_name': 'env_name',
        'app_name': 'app_name',
        'indent': 'indent',
        'region': 'region',
        'host_name': 'host_name',
        'ip_address': 'ip_address',
        'instance_name': 'instance_name',
        'event_id': 'event_id',
        'next_span_id': 'next_spanId',
        'source_event_id': 'source_event_id',
        'method': 'method',
        'children_event_count': 'children_event_count',
        'discard': 'discard',
        'argument': 'argument',
        'attachment': 'attachment',
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
        'biz_code': 'biz_code',
        'id': 'id'
    }

    def __init__(self, env_name=None, app_name=None, indent=None, region=None, host_name=None, ip_address=None, instance_name=None, event_id=None, next_span_id=None, source_event_id=None, method=None, children_event_count=None, discard=None, argument=None, attachment=None, global_trace_id=None, global_path=None, trace_id=None, span_id=None, env_id=None, instance_id=None, app_id=None, biz_id=None, domain_id=None, source=None, real_source=None, start_time=None, time_used=None, code=None, class_name=None, is_async=None, tags=None, has_error=None, error_reasons=None, type=None, http_method=None, biz_code=None, id=None):
        r"""SpanEventInfo

        The model defined in huaweicloud sdk

        :param env_name: 环境名称。
        :type env_name: str
        :param app_name: 组件名称。
        :type app_name: str
        :param indent: 缩进。
        :type indent: int
        :param region: 区域。
        :type region: str
        :param host_name: 主机名称。
        :type host_name: str
        :param ip_address: ip地址。
        :type ip_address: str
        :param instance_name: 实例名称。
        :type instance_name: str
        :param event_id: event的ID，在一个具体的span下面event的编号，一般是1-1-2这种格式。
        :type event_id: str
        :param next_span_id: 产生下一个span的源的eventId。
        :type next_span_id: str
        :param source_event_id: 调用方的eventid。
        :type source_event_id: str
        :param method: 方法名。
        :type method: str
        :param children_event_count: 子event的个数。
        :type children_event_count: int
        :param discard: 丢弃的子event个数，key是类型。
        :type discard: list[:class:`huaweicloudsdkapm.v1.DiscardInfo`]
        :param argument: 界面展示的参数，每个类型的event自己来实现。
        :type argument: str
        :param attachment: 注册信息里面的attachment。
        :type attachment: dict(str, str)
        :param global_trace_id: vTraceId，虚拟traceId。
        :type global_trace_id: str
        :param global_path: 虚拟traceId经过的path路径。
        :type global_path: str
        :param trace_id: traceId。
        :type trace_id: str
        :param span_id: span id。
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
        :param real_source: 根event的时候存在，实际调用的url。
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
        :param has_error: 是否有错误，主要用在span的场景。
        :type has_error: bool
        :param error_reasons: 错误原因。
        :type error_reasons: str
        :param type: 类型，mysql，kafka等。
        :type type: str
        :param http_method: 这里的method实际上是tags里面的http_method，只有url监控项才有。
        :type http_method: str
        :param biz_code: 业务状态码的采集。
        :type biz_code: str
        :param id: spanId。
        :type id: str
        """
        
        

        self._env_name = None
        self._app_name = None
        self._indent = None
        self._region = None
        self._host_name = None
        self._ip_address = None
        self._instance_name = None
        self._event_id = None
        self._next_span_id = None
        self._source_event_id = None
        self._method = None
        self._children_event_count = None
        self._discard = None
        self._argument = None
        self._attachment = None
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
        self._id = None
        self.discriminator = None

        if env_name is not None:
            self.env_name = env_name
        if app_name is not None:
            self.app_name = app_name
        if indent is not None:
            self.indent = indent
        if region is not None:
            self.region = region
        if host_name is not None:
            self.host_name = host_name
        if ip_address is not None:
            self.ip_address = ip_address
        if instance_name is not None:
            self.instance_name = instance_name
        if event_id is not None:
            self.event_id = event_id
        if next_span_id is not None:
            self.next_span_id = next_span_id
        if source_event_id is not None:
            self.source_event_id = source_event_id
        if method is not None:
            self.method = method
        if children_event_count is not None:
            self.children_event_count = children_event_count
        if discard is not None:
            self.discard = discard
        if argument is not None:
            self.argument = argument
        if attachment is not None:
            self.attachment = attachment
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
        if biz_id is not None:
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
        if id is not None:
            self.id = id

    @property
    def env_name(self):
        r"""Gets the env_name of this SpanEventInfo.

        环境名称。

        :return: The env_name of this SpanEventInfo.
        :rtype: str
        """
        return self._env_name

    @env_name.setter
    def env_name(self, env_name):
        r"""Sets the env_name of this SpanEventInfo.

        环境名称。

        :param env_name: The env_name of this SpanEventInfo.
        :type env_name: str
        """
        self._env_name = env_name

    @property
    def app_name(self):
        r"""Gets the app_name of this SpanEventInfo.

        组件名称。

        :return: The app_name of this SpanEventInfo.
        :rtype: str
        """
        return self._app_name

    @app_name.setter
    def app_name(self, app_name):
        r"""Sets the app_name of this SpanEventInfo.

        组件名称。

        :param app_name: The app_name of this SpanEventInfo.
        :type app_name: str
        """
        self._app_name = app_name

    @property
    def indent(self):
        r"""Gets the indent of this SpanEventInfo.

        缩进。

        :return: The indent of this SpanEventInfo.
        :rtype: int
        """
        return self._indent

    @indent.setter
    def indent(self, indent):
        r"""Sets the indent of this SpanEventInfo.

        缩进。

        :param indent: The indent of this SpanEventInfo.
        :type indent: int
        """
        self._indent = indent

    @property
    def region(self):
        r"""Gets the region of this SpanEventInfo.

        区域。

        :return: The region of this SpanEventInfo.
        :rtype: str
        """
        return self._region

    @region.setter
    def region(self, region):
        r"""Sets the region of this SpanEventInfo.

        区域。

        :param region: The region of this SpanEventInfo.
        :type region: str
        """
        self._region = region

    @property
    def host_name(self):
        r"""Gets the host_name of this SpanEventInfo.

        主机名称。

        :return: The host_name of this SpanEventInfo.
        :rtype: str
        """
        return self._host_name

    @host_name.setter
    def host_name(self, host_name):
        r"""Sets the host_name of this SpanEventInfo.

        主机名称。

        :param host_name: The host_name of this SpanEventInfo.
        :type host_name: str
        """
        self._host_name = host_name

    @property
    def ip_address(self):
        r"""Gets the ip_address of this SpanEventInfo.

        ip地址。

        :return: The ip_address of this SpanEventInfo.
        :rtype: str
        """
        return self._ip_address

    @ip_address.setter
    def ip_address(self, ip_address):
        r"""Sets the ip_address of this SpanEventInfo.

        ip地址。

        :param ip_address: The ip_address of this SpanEventInfo.
        :type ip_address: str
        """
        self._ip_address = ip_address

    @property
    def instance_name(self):
        r"""Gets the instance_name of this SpanEventInfo.

        实例名称。

        :return: The instance_name of this SpanEventInfo.
        :rtype: str
        """
        return self._instance_name

    @instance_name.setter
    def instance_name(self, instance_name):
        r"""Sets the instance_name of this SpanEventInfo.

        实例名称。

        :param instance_name: The instance_name of this SpanEventInfo.
        :type instance_name: str
        """
        self._instance_name = instance_name

    @property
    def event_id(self):
        r"""Gets the event_id of this SpanEventInfo.

        event的ID，在一个具体的span下面event的编号，一般是1-1-2这种格式。

        :return: The event_id of this SpanEventInfo.
        :rtype: str
        """
        return self._event_id

    @event_id.setter
    def event_id(self, event_id):
        r"""Sets the event_id of this SpanEventInfo.

        event的ID，在一个具体的span下面event的编号，一般是1-1-2这种格式。

        :param event_id: The event_id of this SpanEventInfo.
        :type event_id: str
        """
        self._event_id = event_id

    @property
    def next_span_id(self):
        r"""Gets the next_span_id of this SpanEventInfo.

        产生下一个span的源的eventId。

        :return: The next_span_id of this SpanEventInfo.
        :rtype: str
        """
        return self._next_span_id

    @next_span_id.setter
    def next_span_id(self, next_span_id):
        r"""Sets the next_span_id of this SpanEventInfo.

        产生下一个span的源的eventId。

        :param next_span_id: The next_span_id of this SpanEventInfo.
        :type next_span_id: str
        """
        self._next_span_id = next_span_id

    @property
    def source_event_id(self):
        r"""Gets the source_event_id of this SpanEventInfo.

        调用方的eventid。

        :return: The source_event_id of this SpanEventInfo.
        :rtype: str
        """
        return self._source_event_id

    @source_event_id.setter
    def source_event_id(self, source_event_id):
        r"""Sets the source_event_id of this SpanEventInfo.

        调用方的eventid。

        :param source_event_id: The source_event_id of this SpanEventInfo.
        :type source_event_id: str
        """
        self._source_event_id = source_event_id

    @property
    def method(self):
        r"""Gets the method of this SpanEventInfo.

        方法名。

        :return: The method of this SpanEventInfo.
        :rtype: str
        """
        return self._method

    @method.setter
    def method(self, method):
        r"""Sets the method of this SpanEventInfo.

        方法名。

        :param method: The method of this SpanEventInfo.
        :type method: str
        """
        self._method = method

    @property
    def children_event_count(self):
        r"""Gets the children_event_count of this SpanEventInfo.

        子event的个数。

        :return: The children_event_count of this SpanEventInfo.
        :rtype: int
        """
        return self._children_event_count

    @children_event_count.setter
    def children_event_count(self, children_event_count):
        r"""Sets the children_event_count of this SpanEventInfo.

        子event的个数。

        :param children_event_count: The children_event_count of this SpanEventInfo.
        :type children_event_count: int
        """
        self._children_event_count = children_event_count

    @property
    def discard(self):
        r"""Gets the discard of this SpanEventInfo.

        丢弃的子event个数，key是类型。

        :return: The discard of this SpanEventInfo.
        :rtype: list[:class:`huaweicloudsdkapm.v1.DiscardInfo`]
        """
        return self._discard

    @discard.setter
    def discard(self, discard):
        r"""Sets the discard of this SpanEventInfo.

        丢弃的子event个数，key是类型。

        :param discard: The discard of this SpanEventInfo.
        :type discard: list[:class:`huaweicloudsdkapm.v1.DiscardInfo`]
        """
        self._discard = discard

    @property
    def argument(self):
        r"""Gets the argument of this SpanEventInfo.

        界面展示的参数，每个类型的event自己来实现。

        :return: The argument of this SpanEventInfo.
        :rtype: str
        """
        return self._argument

    @argument.setter
    def argument(self, argument):
        r"""Sets the argument of this SpanEventInfo.

        界面展示的参数，每个类型的event自己来实现。

        :param argument: The argument of this SpanEventInfo.
        :type argument: str
        """
        self._argument = argument

    @property
    def attachment(self):
        r"""Gets the attachment of this SpanEventInfo.

        注册信息里面的attachment。

        :return: The attachment of this SpanEventInfo.
        :rtype: dict(str, str)
        """
        return self._attachment

    @attachment.setter
    def attachment(self, attachment):
        r"""Sets the attachment of this SpanEventInfo.

        注册信息里面的attachment。

        :param attachment: The attachment of this SpanEventInfo.
        :type attachment: dict(str, str)
        """
        self._attachment = attachment

    @property
    def global_trace_id(self):
        r"""Gets the global_trace_id of this SpanEventInfo.

        vTraceId，虚拟traceId。

        :return: The global_trace_id of this SpanEventInfo.
        :rtype: str
        """
        return self._global_trace_id

    @global_trace_id.setter
    def global_trace_id(self, global_trace_id):
        r"""Sets the global_trace_id of this SpanEventInfo.

        vTraceId，虚拟traceId。

        :param global_trace_id: The global_trace_id of this SpanEventInfo.
        :type global_trace_id: str
        """
        self._global_trace_id = global_trace_id

    @property
    def global_path(self):
        r"""Gets the global_path of this SpanEventInfo.

        虚拟traceId经过的path路径。

        :return: The global_path of this SpanEventInfo.
        :rtype: str
        """
        return self._global_path

    @global_path.setter
    def global_path(self, global_path):
        r"""Sets the global_path of this SpanEventInfo.

        虚拟traceId经过的path路径。

        :param global_path: The global_path of this SpanEventInfo.
        :type global_path: str
        """
        self._global_path = global_path

    @property
    def trace_id(self):
        r"""Gets the trace_id of this SpanEventInfo.

        traceId。

        :return: The trace_id of this SpanEventInfo.
        :rtype: str
        """
        return self._trace_id

    @trace_id.setter
    def trace_id(self, trace_id):
        r"""Sets the trace_id of this SpanEventInfo.

        traceId。

        :param trace_id: The trace_id of this SpanEventInfo.
        :type trace_id: str
        """
        self._trace_id = trace_id

    @property
    def span_id(self):
        r"""Gets the span_id of this SpanEventInfo.

        span id。

        :return: The span_id of this SpanEventInfo.
        :rtype: str
        """
        return self._span_id

    @span_id.setter
    def span_id(self, span_id):
        r"""Sets the span_id of this SpanEventInfo.

        span id。

        :param span_id: The span_id of this SpanEventInfo.
        :type span_id: str
        """
        self._span_id = span_id

    @property
    def env_id(self):
        r"""Gets the env_id of this SpanEventInfo.

        环境id。

        :return: The env_id of this SpanEventInfo.
        :rtype: int
        """
        return self._env_id

    @env_id.setter
    def env_id(self, env_id):
        r"""Sets the env_id of this SpanEventInfo.

        环境id。

        :param env_id: The env_id of this SpanEventInfo.
        :type env_id: int
        """
        self._env_id = env_id

    @property
    def instance_id(self):
        r"""Gets the instance_id of this SpanEventInfo.

        实例id。

        :return: The instance_id of this SpanEventInfo.
        :rtype: int
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        r"""Sets the instance_id of this SpanEventInfo.

        实例id。

        :param instance_id: The instance_id of this SpanEventInfo.
        :type instance_id: int
        """
        self._instance_id = instance_id

    @property
    def app_id(self):
        r"""Gets the app_id of this SpanEventInfo.

        组件id。

        :return: The app_id of this SpanEventInfo.
        :rtype: int
        """
        return self._app_id

    @app_id.setter
    def app_id(self, app_id):
        r"""Sets the app_id of this SpanEventInfo.

        组件id。

        :param app_id: The app_id of this SpanEventInfo.
        :type app_id: int
        """
        self._app_id = app_id

    @property
    def biz_id(self):
        r"""Gets the biz_id of this SpanEventInfo.

        应用id。

        :return: The biz_id of this SpanEventInfo.
        :rtype: int
        """
        return self._biz_id

    @biz_id.setter
    def biz_id(self, biz_id):
        r"""Sets the biz_id of this SpanEventInfo.

        应用id。

        :param biz_id: The biz_id of this SpanEventInfo.
        :type biz_id: int
        """
        self._biz_id = biz_id

    @property
    def domain_id(self):
        r"""Gets the domain_id of this SpanEventInfo.

        租户id。

        :return: The domain_id of this SpanEventInfo.
        :rtype: int
        """
        return self._domain_id

    @domain_id.setter
    def domain_id(self, domain_id):
        r"""Sets the domain_id of this SpanEventInfo.

        租户id。

        :param domain_id: The domain_id of this SpanEventInfo.
        :type domain_id: int
        """
        self._domain_id = domain_id

    @property
    def source(self):
        r"""Gets the source of this SpanEventInfo.

        只有是根event也就是span的时候有值。

        :return: The source of this SpanEventInfo.
        :rtype: str
        """
        return self._source

    @source.setter
    def source(self, source):
        r"""Sets the source of this SpanEventInfo.

        只有是根event也就是span的时候有值。

        :param source: The source of this SpanEventInfo.
        :type source: str
        """
        self._source = source

    @property
    def real_source(self):
        r"""Gets the real_source of this SpanEventInfo.

        根event的时候存在，实际调用的url。

        :return: The real_source of this SpanEventInfo.
        :rtype: str
        """
        return self._real_source

    @real_source.setter
    def real_source(self, real_source):
        r"""Sets the real_source of this SpanEventInfo.

        根event的时候存在，实际调用的url。

        :param real_source: The real_source of this SpanEventInfo.
        :type real_source: str
        """
        self._real_source = real_source

    @property
    def start_time(self):
        r"""Gets the start_time of this SpanEventInfo.

        开始时间。

        :return: The start_time of this SpanEventInfo.
        :rtype: int
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        r"""Sets the start_time of this SpanEventInfo.

        开始时间。

        :param start_time: The start_time of this SpanEventInfo.
        :type start_time: int
        """
        self._start_time = start_time

    @property
    def time_used(self):
        r"""Gets the time_used of this SpanEventInfo.

        耗时。

        :return: The time_used of this SpanEventInfo.
        :rtype: int
        """
        return self._time_used

    @time_used.setter
    def time_used(self, time_used):
        r"""Sets the time_used of this SpanEventInfo.

        耗时。

        :param time_used: The time_used of this SpanEventInfo.
        :type time_used: int
        """
        self._time_used = time_used

    @property
    def code(self):
        r"""Gets the code of this SpanEventInfo.

        状态码，针对http的调用有效。

        :return: The code of this SpanEventInfo.
        :rtype: int
        """
        return self._code

    @code.setter
    def code(self, code):
        r"""Sets the code of this SpanEventInfo.

        状态码，针对http的调用有效。

        :param code: The code of this SpanEventInfo.
        :type code: int
        """
        self._code = code

    @property
    def class_name(self):
        r"""Gets the class_name of this SpanEventInfo.

        类名。

        :return: The class_name of this SpanEventInfo.
        :rtype: str
        """
        return self._class_name

    @class_name.setter
    def class_name(self, class_name):
        r"""Sets the class_name of this SpanEventInfo.

        类名。

        :param class_name: The class_name of this SpanEventInfo.
        :type class_name: str
        """
        self._class_name = class_name

    @property
    def is_async(self):
        r"""Gets the is_async of this SpanEventInfo.

        是否异步的event。

        :return: The is_async of this SpanEventInfo.
        :rtype: bool
        """
        return self._is_async

    @is_async.setter
    def is_async(self, is_async):
        r"""Sets the is_async of this SpanEventInfo.

        是否异步的event。

        :param is_async: The is_async of this SpanEventInfo.
        :type is_async: bool
        """
        self._is_async = is_async

    @property
    def tags(self):
        r"""Gets the tags of this SpanEventInfo.

        包含用户自定义参数，header或body体里的内容，httpMethod, bizCode，以及后续可能新增参数。

        :return: The tags of this SpanEventInfo.
        :rtype: dict(str, str)
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        r"""Sets the tags of this SpanEventInfo.

        包含用户自定义参数，header或body体里的内容，httpMethod, bizCode，以及后续可能新增参数。

        :param tags: The tags of this SpanEventInfo.
        :type tags: dict(str, str)
        """
        self._tags = tags

    @property
    def has_error(self):
        r"""Gets the has_error of this SpanEventInfo.

        是否有错误，主要用在span的场景。

        :return: The has_error of this SpanEventInfo.
        :rtype: bool
        """
        return self._has_error

    @has_error.setter
    def has_error(self, has_error):
        r"""Sets the has_error of this SpanEventInfo.

        是否有错误，主要用在span的场景。

        :param has_error: The has_error of this SpanEventInfo.
        :type has_error: bool
        """
        self._has_error = has_error

    @property
    def error_reasons(self):
        r"""Gets the error_reasons of this SpanEventInfo.

        错误原因。

        :return: The error_reasons of this SpanEventInfo.
        :rtype: str
        """
        return self._error_reasons

    @error_reasons.setter
    def error_reasons(self, error_reasons):
        r"""Sets the error_reasons of this SpanEventInfo.

        错误原因。

        :param error_reasons: The error_reasons of this SpanEventInfo.
        :type error_reasons: str
        """
        self._error_reasons = error_reasons

    @property
    def type(self):
        r"""Gets the type of this SpanEventInfo.

        类型，mysql，kafka等。

        :return: The type of this SpanEventInfo.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this SpanEventInfo.

        类型，mysql，kafka等。

        :param type: The type of this SpanEventInfo.
        :type type: str
        """
        self._type = type

    @property
    def http_method(self):
        r"""Gets the http_method of this SpanEventInfo.

        这里的method实际上是tags里面的http_method，只有url监控项才有。

        :return: The http_method of this SpanEventInfo.
        :rtype: str
        """
        return self._http_method

    @http_method.setter
    def http_method(self, http_method):
        r"""Sets the http_method of this SpanEventInfo.

        这里的method实际上是tags里面的http_method，只有url监控项才有。

        :param http_method: The http_method of this SpanEventInfo.
        :type http_method: str
        """
        self._http_method = http_method

    @property
    def biz_code(self):
        r"""Gets the biz_code of this SpanEventInfo.

        业务状态码的采集。

        :return: The biz_code of this SpanEventInfo.
        :rtype: str
        """
        return self._biz_code

    @biz_code.setter
    def biz_code(self, biz_code):
        r"""Sets the biz_code of this SpanEventInfo.

        业务状态码的采集。

        :param biz_code: The biz_code of this SpanEventInfo.
        :type biz_code: str
        """
        self._biz_code = biz_code

    @property
    def id(self):
        r"""Gets the id of this SpanEventInfo.

        spanId。

        :return: The id of this SpanEventInfo.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this SpanEventInfo.

        spanId。

        :param id: The id of this SpanEventInfo.
        :type id: str
        """
        self._id = id

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
        if not isinstance(other, SpanEventInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

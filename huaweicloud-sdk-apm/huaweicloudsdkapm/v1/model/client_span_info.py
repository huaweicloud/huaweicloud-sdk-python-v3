# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ClientSpanInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
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

    def __init__(self, global_trace_id=None, global_path=None, trace_id=None, span_id=None, env_id=None, instance_id=None, app_id=None, biz_id=None, domain_id=None, source=None, real_source=None, start_time=None, time_used=None, code=None, class_name=None, is_async=None, tags=None, has_error=None, error_reasons=None, type=None, http_method=None, biz_code=None):
        """ClientSpanInfo

        The model defined in huaweicloud sdk

        :param global_trace_id: vTraceId，虚拟traceI
        :type global_trace_id: str
        :param global_path: 
        :type global_path: str
        :param trace_id: 
        :type trace_id: str
        :param span_id: 
        :type span_id: str
        :param env_id: 
        :type env_id: int
        :param instance_id: 
        :type instance_id: int
        :param app_id: 
        :type app_id: int
        :param biz_id: 
        :type biz_id: int
        :param domain_id: 
        :type domain_id: int
        :param source: 
        :type source: str
        :param real_source: 
        :type real_source: str
        :param start_time: 
        :type start_time: int
        :param time_used: 
        :type time_used: int
        :param code: 
        :type code: int
        :param class_name: 
        :type class_name: str
        :param is_async: 
        :type is_async: bool
        :param tags: 
        :type tags: dict(str, str)
        :param has_error: 
        :type has_error: bool
        :param error_reasons: 
        :type error_reasons: str
        :param type: 类型，mysql，kafka等
        :type type: str
        :param http_method: 这里的method实际上是tags里面的http_method，只有url监控项才有
        :type http_method: str
        :param biz_code: 业务状态码的采集
        :type biz_code: str
        """
        
        

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

    @property
    def global_trace_id(self):
        """Gets the global_trace_id of this ClientSpanInfo.

        vTraceId，虚拟traceI

        :return: The global_trace_id of this ClientSpanInfo.
        :rtype: str
        """
        return self._global_trace_id

    @global_trace_id.setter
    def global_trace_id(self, global_trace_id):
        """Sets the global_trace_id of this ClientSpanInfo.

        vTraceId，虚拟traceI

        :param global_trace_id: The global_trace_id of this ClientSpanInfo.
        :type global_trace_id: str
        """
        self._global_trace_id = global_trace_id

    @property
    def global_path(self):
        """Gets the global_path of this ClientSpanInfo.


        :return: The global_path of this ClientSpanInfo.
        :rtype: str
        """
        return self._global_path

    @global_path.setter
    def global_path(self, global_path):
        """Sets the global_path of this ClientSpanInfo.


        :param global_path: The global_path of this ClientSpanInfo.
        :type global_path: str
        """
        self._global_path = global_path

    @property
    def trace_id(self):
        """Gets the trace_id of this ClientSpanInfo.


        :return: The trace_id of this ClientSpanInfo.
        :rtype: str
        """
        return self._trace_id

    @trace_id.setter
    def trace_id(self, trace_id):
        """Sets the trace_id of this ClientSpanInfo.


        :param trace_id: The trace_id of this ClientSpanInfo.
        :type trace_id: str
        """
        self._trace_id = trace_id

    @property
    def span_id(self):
        """Gets the span_id of this ClientSpanInfo.


        :return: The span_id of this ClientSpanInfo.
        :rtype: str
        """
        return self._span_id

    @span_id.setter
    def span_id(self, span_id):
        """Sets the span_id of this ClientSpanInfo.


        :param span_id: The span_id of this ClientSpanInfo.
        :type span_id: str
        """
        self._span_id = span_id

    @property
    def env_id(self):
        """Gets the env_id of this ClientSpanInfo.


        :return: The env_id of this ClientSpanInfo.
        :rtype: int
        """
        return self._env_id

    @env_id.setter
    def env_id(self, env_id):
        """Sets the env_id of this ClientSpanInfo.


        :param env_id: The env_id of this ClientSpanInfo.
        :type env_id: int
        """
        self._env_id = env_id

    @property
    def instance_id(self):
        """Gets the instance_id of this ClientSpanInfo.


        :return: The instance_id of this ClientSpanInfo.
        :rtype: int
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        """Sets the instance_id of this ClientSpanInfo.


        :param instance_id: The instance_id of this ClientSpanInfo.
        :type instance_id: int
        """
        self._instance_id = instance_id

    @property
    def app_id(self):
        """Gets the app_id of this ClientSpanInfo.


        :return: The app_id of this ClientSpanInfo.
        :rtype: int
        """
        return self._app_id

    @app_id.setter
    def app_id(self, app_id):
        """Sets the app_id of this ClientSpanInfo.


        :param app_id: The app_id of this ClientSpanInfo.
        :type app_id: int
        """
        self._app_id = app_id

    @property
    def biz_id(self):
        """Gets the biz_id of this ClientSpanInfo.


        :return: The biz_id of this ClientSpanInfo.
        :rtype: int
        """
        return self._biz_id

    @biz_id.setter
    def biz_id(self, biz_id):
        """Sets the biz_id of this ClientSpanInfo.


        :param biz_id: The biz_id of this ClientSpanInfo.
        :type biz_id: int
        """
        self._biz_id = biz_id

    @property
    def domain_id(self):
        """Gets the domain_id of this ClientSpanInfo.


        :return: The domain_id of this ClientSpanInfo.
        :rtype: int
        """
        return self._domain_id

    @domain_id.setter
    def domain_id(self, domain_id):
        """Sets the domain_id of this ClientSpanInfo.


        :param domain_id: The domain_id of this ClientSpanInfo.
        :type domain_id: int
        """
        self._domain_id = domain_id

    @property
    def source(self):
        """Gets the source of this ClientSpanInfo.


        :return: The source of this ClientSpanInfo.
        :rtype: str
        """
        return self._source

    @source.setter
    def source(self, source):
        """Sets the source of this ClientSpanInfo.


        :param source: The source of this ClientSpanInfo.
        :type source: str
        """
        self._source = source

    @property
    def real_source(self):
        """Gets the real_source of this ClientSpanInfo.


        :return: The real_source of this ClientSpanInfo.
        :rtype: str
        """
        return self._real_source

    @real_source.setter
    def real_source(self, real_source):
        """Sets the real_source of this ClientSpanInfo.


        :param real_source: The real_source of this ClientSpanInfo.
        :type real_source: str
        """
        self._real_source = real_source

    @property
    def start_time(self):
        """Gets the start_time of this ClientSpanInfo.


        :return: The start_time of this ClientSpanInfo.
        :rtype: int
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        """Sets the start_time of this ClientSpanInfo.


        :param start_time: The start_time of this ClientSpanInfo.
        :type start_time: int
        """
        self._start_time = start_time

    @property
    def time_used(self):
        """Gets the time_used of this ClientSpanInfo.


        :return: The time_used of this ClientSpanInfo.
        :rtype: int
        """
        return self._time_used

    @time_used.setter
    def time_used(self, time_used):
        """Sets the time_used of this ClientSpanInfo.


        :param time_used: The time_used of this ClientSpanInfo.
        :type time_used: int
        """
        self._time_used = time_used

    @property
    def code(self):
        """Gets the code of this ClientSpanInfo.


        :return: The code of this ClientSpanInfo.
        :rtype: int
        """
        return self._code

    @code.setter
    def code(self, code):
        """Sets the code of this ClientSpanInfo.


        :param code: The code of this ClientSpanInfo.
        :type code: int
        """
        self._code = code

    @property
    def class_name(self):
        """Gets the class_name of this ClientSpanInfo.


        :return: The class_name of this ClientSpanInfo.
        :rtype: str
        """
        return self._class_name

    @class_name.setter
    def class_name(self, class_name):
        """Sets the class_name of this ClientSpanInfo.


        :param class_name: The class_name of this ClientSpanInfo.
        :type class_name: str
        """
        self._class_name = class_name

    @property
    def is_async(self):
        """Gets the is_async of this ClientSpanInfo.


        :return: The is_async of this ClientSpanInfo.
        :rtype: bool
        """
        return self._is_async

    @is_async.setter
    def is_async(self, is_async):
        """Sets the is_async of this ClientSpanInfo.


        :param is_async: The is_async of this ClientSpanInfo.
        :type is_async: bool
        """
        self._is_async = is_async

    @property
    def tags(self):
        """Gets the tags of this ClientSpanInfo.


        :return: The tags of this ClientSpanInfo.
        :rtype: dict(str, str)
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this ClientSpanInfo.


        :param tags: The tags of this ClientSpanInfo.
        :type tags: dict(str, str)
        """
        self._tags = tags

    @property
    def has_error(self):
        """Gets the has_error of this ClientSpanInfo.


        :return: The has_error of this ClientSpanInfo.
        :rtype: bool
        """
        return self._has_error

    @has_error.setter
    def has_error(self, has_error):
        """Sets the has_error of this ClientSpanInfo.


        :param has_error: The has_error of this ClientSpanInfo.
        :type has_error: bool
        """
        self._has_error = has_error

    @property
    def error_reasons(self):
        """Gets the error_reasons of this ClientSpanInfo.


        :return: The error_reasons of this ClientSpanInfo.
        :rtype: str
        """
        return self._error_reasons

    @error_reasons.setter
    def error_reasons(self, error_reasons):
        """Sets the error_reasons of this ClientSpanInfo.


        :param error_reasons: The error_reasons of this ClientSpanInfo.
        :type error_reasons: str
        """
        self._error_reasons = error_reasons

    @property
    def type(self):
        """Gets the type of this ClientSpanInfo.

        类型，mysql，kafka等

        :return: The type of this ClientSpanInfo.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this ClientSpanInfo.

        类型，mysql，kafka等

        :param type: The type of this ClientSpanInfo.
        :type type: str
        """
        self._type = type

    @property
    def http_method(self):
        """Gets the http_method of this ClientSpanInfo.

        这里的method实际上是tags里面的http_method，只有url监控项才有

        :return: The http_method of this ClientSpanInfo.
        :rtype: str
        """
        return self._http_method

    @http_method.setter
    def http_method(self, http_method):
        """Sets the http_method of this ClientSpanInfo.

        这里的method实际上是tags里面的http_method，只有url监控项才有

        :param http_method: The http_method of this ClientSpanInfo.
        :type http_method: str
        """
        self._http_method = http_method

    @property
    def biz_code(self):
        """Gets the biz_code of this ClientSpanInfo.

        业务状态码的采集

        :return: The biz_code of this ClientSpanInfo.
        :rtype: str
        """
        return self._biz_code

    @biz_code.setter
    def biz_code(self, biz_code):
        """Sets the biz_code of this ClientSpanInfo.

        业务状态码的采集

        :param biz_code: The biz_code of this ClientSpanInfo.
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
        if not isinstance(other, ClientSpanInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

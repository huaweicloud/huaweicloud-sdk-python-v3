# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class StatisticsGroup:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'max_latency': 'int',
        'avg_latency': 'float',
        'req_count': 'int',
        'req_count2xx': 'int',
        'req_count4xx': 'int',
        'req_count5xx': 'int',
        'req_count_error': 'int',
        'output_throughput': 'int',
        'input_throughput': 'int',
        'current_minute': 'int',
        'group_id': 'str',
        'provider': 'str',
        'req_time': 'datetime',
        'register_time': 'datetime'
    }

    attribute_map = {
        'max_latency': 'max_latency',
        'avg_latency': 'avg_latency',
        'req_count': 'req_count',
        'req_count2xx': 'req_count2xx',
        'req_count4xx': 'req_count4xx',
        'req_count5xx': 'req_count5xx',
        'req_count_error': 'req_count_error',
        'output_throughput': 'output_throughput',
        'input_throughput': 'input_throughput',
        'current_minute': 'current_minute',
        'group_id': 'group_id',
        'provider': 'provider',
        'req_time': 'req_time',
        'register_time': 'register_time'
    }

    def __init__(self, max_latency=None, avg_latency=None, req_count=None, req_count2xx=None, req_count4xx=None, req_count5xx=None, req_count_error=None, output_throughput=None, input_throughput=None, current_minute=None, group_id=None, provider=None, req_time=None, register_time=None):
        """StatisticsGroup

        The model defined in huaweicloud sdk

        :param max_latency: 最大延时  单位：ms
        :type max_latency: int
        :param avg_latency: 平均延时  单位：ms
        :type avg_latency: float
        :param req_count: 请求总次数
        :type req_count: int
        :param req_count2xx: 2xx响应码总次数
        :type req_count2xx: int
        :param req_count4xx: 4xx响应码总次数
        :type req_count4xx: int
        :param req_count5xx: 5xx响应码总次数
        :type req_count5xx: int
        :param req_count_error: 错误次数
        :type req_count_error: int
        :param output_throughput: 下行吞吐量（byte）
        :type output_throughput: int
        :param input_throughput: 上行吞吐量（byte）
        :type input_throughput: int
        :param current_minute: API访问的UTC时间戳
        :type current_minute: int
        :param group_id: API分组编号
        :type group_id: str
        :param provider: API拥有者
        :type provider: str
        :param req_time: API请求时间
        :type req_time: datetime
        :param register_time: 记录时间
        :type register_time: datetime
        """
        
        

        self._max_latency = None
        self._avg_latency = None
        self._req_count = None
        self._req_count2xx = None
        self._req_count4xx = None
        self._req_count5xx = None
        self._req_count_error = None
        self._output_throughput = None
        self._input_throughput = None
        self._current_minute = None
        self._group_id = None
        self._provider = None
        self._req_time = None
        self._register_time = None
        self.discriminator = None

        if max_latency is not None:
            self.max_latency = max_latency
        if avg_latency is not None:
            self.avg_latency = avg_latency
        if req_count is not None:
            self.req_count = req_count
        if req_count2xx is not None:
            self.req_count2xx = req_count2xx
        if req_count4xx is not None:
            self.req_count4xx = req_count4xx
        if req_count5xx is not None:
            self.req_count5xx = req_count5xx
        if req_count_error is not None:
            self.req_count_error = req_count_error
        if output_throughput is not None:
            self.output_throughput = output_throughput
        if input_throughput is not None:
            self.input_throughput = input_throughput
        if current_minute is not None:
            self.current_minute = current_minute
        if group_id is not None:
            self.group_id = group_id
        if provider is not None:
            self.provider = provider
        if req_time is not None:
            self.req_time = req_time
        if register_time is not None:
            self.register_time = register_time

    @property
    def max_latency(self):
        """Gets the max_latency of this StatisticsGroup.

        最大延时  单位：ms

        :return: The max_latency of this StatisticsGroup.
        :rtype: int
        """
        return self._max_latency

    @max_latency.setter
    def max_latency(self, max_latency):
        """Sets the max_latency of this StatisticsGroup.

        最大延时  单位：ms

        :param max_latency: The max_latency of this StatisticsGroup.
        :type max_latency: int
        """
        self._max_latency = max_latency

    @property
    def avg_latency(self):
        """Gets the avg_latency of this StatisticsGroup.

        平均延时  单位：ms

        :return: The avg_latency of this StatisticsGroup.
        :rtype: float
        """
        return self._avg_latency

    @avg_latency.setter
    def avg_latency(self, avg_latency):
        """Sets the avg_latency of this StatisticsGroup.

        平均延时  单位：ms

        :param avg_latency: The avg_latency of this StatisticsGroup.
        :type avg_latency: float
        """
        self._avg_latency = avg_latency

    @property
    def req_count(self):
        """Gets the req_count of this StatisticsGroup.

        请求总次数

        :return: The req_count of this StatisticsGroup.
        :rtype: int
        """
        return self._req_count

    @req_count.setter
    def req_count(self, req_count):
        """Sets the req_count of this StatisticsGroup.

        请求总次数

        :param req_count: The req_count of this StatisticsGroup.
        :type req_count: int
        """
        self._req_count = req_count

    @property
    def req_count2xx(self):
        """Gets the req_count2xx of this StatisticsGroup.

        2xx响应码总次数

        :return: The req_count2xx of this StatisticsGroup.
        :rtype: int
        """
        return self._req_count2xx

    @req_count2xx.setter
    def req_count2xx(self, req_count2xx):
        """Sets the req_count2xx of this StatisticsGroup.

        2xx响应码总次数

        :param req_count2xx: The req_count2xx of this StatisticsGroup.
        :type req_count2xx: int
        """
        self._req_count2xx = req_count2xx

    @property
    def req_count4xx(self):
        """Gets the req_count4xx of this StatisticsGroup.

        4xx响应码总次数

        :return: The req_count4xx of this StatisticsGroup.
        :rtype: int
        """
        return self._req_count4xx

    @req_count4xx.setter
    def req_count4xx(self, req_count4xx):
        """Sets the req_count4xx of this StatisticsGroup.

        4xx响应码总次数

        :param req_count4xx: The req_count4xx of this StatisticsGroup.
        :type req_count4xx: int
        """
        self._req_count4xx = req_count4xx

    @property
    def req_count5xx(self):
        """Gets the req_count5xx of this StatisticsGroup.

        5xx响应码总次数

        :return: The req_count5xx of this StatisticsGroup.
        :rtype: int
        """
        return self._req_count5xx

    @req_count5xx.setter
    def req_count5xx(self, req_count5xx):
        """Sets the req_count5xx of this StatisticsGroup.

        5xx响应码总次数

        :param req_count5xx: The req_count5xx of this StatisticsGroup.
        :type req_count5xx: int
        """
        self._req_count5xx = req_count5xx

    @property
    def req_count_error(self):
        """Gets the req_count_error of this StatisticsGroup.

        错误次数

        :return: The req_count_error of this StatisticsGroup.
        :rtype: int
        """
        return self._req_count_error

    @req_count_error.setter
    def req_count_error(self, req_count_error):
        """Sets the req_count_error of this StatisticsGroup.

        错误次数

        :param req_count_error: The req_count_error of this StatisticsGroup.
        :type req_count_error: int
        """
        self._req_count_error = req_count_error

    @property
    def output_throughput(self):
        """Gets the output_throughput of this StatisticsGroup.

        下行吞吐量（byte）

        :return: The output_throughput of this StatisticsGroup.
        :rtype: int
        """
        return self._output_throughput

    @output_throughput.setter
    def output_throughput(self, output_throughput):
        """Sets the output_throughput of this StatisticsGroup.

        下行吞吐量（byte）

        :param output_throughput: The output_throughput of this StatisticsGroup.
        :type output_throughput: int
        """
        self._output_throughput = output_throughput

    @property
    def input_throughput(self):
        """Gets the input_throughput of this StatisticsGroup.

        上行吞吐量（byte）

        :return: The input_throughput of this StatisticsGroup.
        :rtype: int
        """
        return self._input_throughput

    @input_throughput.setter
    def input_throughput(self, input_throughput):
        """Sets the input_throughput of this StatisticsGroup.

        上行吞吐量（byte）

        :param input_throughput: The input_throughput of this StatisticsGroup.
        :type input_throughput: int
        """
        self._input_throughput = input_throughput

    @property
    def current_minute(self):
        """Gets the current_minute of this StatisticsGroup.

        API访问的UTC时间戳

        :return: The current_minute of this StatisticsGroup.
        :rtype: int
        """
        return self._current_minute

    @current_minute.setter
    def current_minute(self, current_minute):
        """Sets the current_minute of this StatisticsGroup.

        API访问的UTC时间戳

        :param current_minute: The current_minute of this StatisticsGroup.
        :type current_minute: int
        """
        self._current_minute = current_minute

    @property
    def group_id(self):
        """Gets the group_id of this StatisticsGroup.

        API分组编号

        :return: The group_id of this StatisticsGroup.
        :rtype: str
        """
        return self._group_id

    @group_id.setter
    def group_id(self, group_id):
        """Sets the group_id of this StatisticsGroup.

        API分组编号

        :param group_id: The group_id of this StatisticsGroup.
        :type group_id: str
        """
        self._group_id = group_id

    @property
    def provider(self):
        """Gets the provider of this StatisticsGroup.

        API拥有者

        :return: The provider of this StatisticsGroup.
        :rtype: str
        """
        return self._provider

    @provider.setter
    def provider(self, provider):
        """Sets the provider of this StatisticsGroup.

        API拥有者

        :param provider: The provider of this StatisticsGroup.
        :type provider: str
        """
        self._provider = provider

    @property
    def req_time(self):
        """Gets the req_time of this StatisticsGroup.

        API请求时间

        :return: The req_time of this StatisticsGroup.
        :rtype: datetime
        """
        return self._req_time

    @req_time.setter
    def req_time(self, req_time):
        """Sets the req_time of this StatisticsGroup.

        API请求时间

        :param req_time: The req_time of this StatisticsGroup.
        :type req_time: datetime
        """
        self._req_time = req_time

    @property
    def register_time(self):
        """Gets the register_time of this StatisticsGroup.

        记录时间

        :return: The register_time of this StatisticsGroup.
        :rtype: datetime
        """
        return self._register_time

    @register_time.setter
    def register_time(self, register_time):
        """Sets the register_time of this StatisticsGroup.

        记录时间

        :param register_time: The register_time of this StatisticsGroup.
        :type register_time: datetime
        """
        self._register_time = register_time

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
        if not isinstance(other, StatisticsGroup):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

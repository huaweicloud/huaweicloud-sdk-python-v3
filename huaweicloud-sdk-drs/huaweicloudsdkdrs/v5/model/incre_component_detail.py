# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class IncreComponentDetail:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'type': 'str',
        'status': 'str',
        'start_time': 'str',
        'start_point': 'str',
        'current_point': 'str',
        'resolution_time': 'str',
        'delay': 'str'
    }

    attribute_map = {
        'type': 'type',
        'status': 'status',
        'start_time': 'start_time',
        'start_point': 'start_point',
        'current_point': 'current_point',
        'resolution_time': 'resolution_time',
        'delay': 'delay'
    }

    def __init__(self, type=None, status=None, start_time=None, start_point=None, current_point=None, resolution_time=None, delay=None):
        r"""IncreComponentDetail

        The model defined in huaweicloud sdk

        :param type: 组件类型 - capture：抓取 - apply：回放
        :type type: str
        :param status: 状态。 - STOPPED：停止 - STARTED：运行中 - STOPPING：停止中 - STARTING：启动中
        :type status: str
        :param start_time: 启动时间
        :type start_time: str
        :param start_point: 启动位点
        :type start_point: str
        :param current_point: 当前位点
        :type current_point: str
        :param resolution_time: 解析时间
        :type resolution_time: str
        :param delay: 时延，单位：秒
        :type delay: str
        """
        
        

        self._type = None
        self._status = None
        self._start_time = None
        self._start_point = None
        self._current_point = None
        self._resolution_time = None
        self._delay = None
        self.discriminator = None

        if type is not None:
            self.type = type
        if status is not None:
            self.status = status
        if start_time is not None:
            self.start_time = start_time
        if start_point is not None:
            self.start_point = start_point
        if current_point is not None:
            self.current_point = current_point
        if resolution_time is not None:
            self.resolution_time = resolution_time
        if delay is not None:
            self.delay = delay

    @property
    def type(self):
        r"""Gets the type of this IncreComponentDetail.

        组件类型 - capture：抓取 - apply：回放

        :return: The type of this IncreComponentDetail.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this IncreComponentDetail.

        组件类型 - capture：抓取 - apply：回放

        :param type: The type of this IncreComponentDetail.
        :type type: str
        """
        self._type = type

    @property
    def status(self):
        r"""Gets the status of this IncreComponentDetail.

        状态。 - STOPPED：停止 - STARTED：运行中 - STOPPING：停止中 - STARTING：启动中

        :return: The status of this IncreComponentDetail.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this IncreComponentDetail.

        状态。 - STOPPED：停止 - STARTED：运行中 - STOPPING：停止中 - STARTING：启动中

        :param status: The status of this IncreComponentDetail.
        :type status: str
        """
        self._status = status

    @property
    def start_time(self):
        r"""Gets the start_time of this IncreComponentDetail.

        启动时间

        :return: The start_time of this IncreComponentDetail.
        :rtype: str
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        r"""Sets the start_time of this IncreComponentDetail.

        启动时间

        :param start_time: The start_time of this IncreComponentDetail.
        :type start_time: str
        """
        self._start_time = start_time

    @property
    def start_point(self):
        r"""Gets the start_point of this IncreComponentDetail.

        启动位点

        :return: The start_point of this IncreComponentDetail.
        :rtype: str
        """
        return self._start_point

    @start_point.setter
    def start_point(self, start_point):
        r"""Sets the start_point of this IncreComponentDetail.

        启动位点

        :param start_point: The start_point of this IncreComponentDetail.
        :type start_point: str
        """
        self._start_point = start_point

    @property
    def current_point(self):
        r"""Gets the current_point of this IncreComponentDetail.

        当前位点

        :return: The current_point of this IncreComponentDetail.
        :rtype: str
        """
        return self._current_point

    @current_point.setter
    def current_point(self, current_point):
        r"""Sets the current_point of this IncreComponentDetail.

        当前位点

        :param current_point: The current_point of this IncreComponentDetail.
        :type current_point: str
        """
        self._current_point = current_point

    @property
    def resolution_time(self):
        r"""Gets the resolution_time of this IncreComponentDetail.

        解析时间

        :return: The resolution_time of this IncreComponentDetail.
        :rtype: str
        """
        return self._resolution_time

    @resolution_time.setter
    def resolution_time(self, resolution_time):
        r"""Sets the resolution_time of this IncreComponentDetail.

        解析时间

        :param resolution_time: The resolution_time of this IncreComponentDetail.
        :type resolution_time: str
        """
        self._resolution_time = resolution_time

    @property
    def delay(self):
        r"""Gets the delay of this IncreComponentDetail.

        时延，单位：秒

        :return: The delay of this IncreComponentDetail.
        :rtype: str
        """
        return self._delay

    @delay.setter
    def delay(self, delay):
        r"""Sets the delay of this IncreComponentDetail.

        时延，单位：秒

        :param delay: The delay of this IncreComponentDetail.
        :type delay: str
        """
        self._delay = delay

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
        if not isinstance(other, IncreComponentDetail):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

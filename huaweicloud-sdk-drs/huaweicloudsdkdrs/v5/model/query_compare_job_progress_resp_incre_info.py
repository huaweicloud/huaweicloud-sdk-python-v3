# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class QueryCompareJobProgressRespIncreInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'delay': 'float',
        'src_speed': 'str',
        'rps': 'int',
        'log_point': 'str',
        'recheck_entities': 'int'
    }

    attribute_map = {
        'delay': 'delay',
        'src_speed': 'src_speed',
        'rps': 'rps',
        'log_point': 'log_point',
        'recheck_entities': 'recheck_entities'
    }

    def __init__(self, delay=None, src_speed=None, rps=None, log_point=None, recheck_entities=None):
        r"""QueryCompareJobProgressRespIncreInfo

        The model defined in huaweicloud sdk

        :param delay: 增量对比时延，若时延为0表示所有增量数据都已对比完成。
        :type delay: float
        :param src_speed: 增量数据对比速率。
        :type src_speed: str
        :param rps: 每秒对比行数。
        :type rps: int
        :param log_point: 增量位点。
        :type log_point: str
        :param recheck_entities: 差异待复查行数。
        :type recheck_entities: int
        """
        
        

        self._delay = None
        self._src_speed = None
        self._rps = None
        self._log_point = None
        self._recheck_entities = None
        self.discriminator = None

        if delay is not None:
            self.delay = delay
        if src_speed is not None:
            self.src_speed = src_speed
        if rps is not None:
            self.rps = rps
        if log_point is not None:
            self.log_point = log_point
        if recheck_entities is not None:
            self.recheck_entities = recheck_entities

    @property
    def delay(self):
        r"""Gets the delay of this QueryCompareJobProgressRespIncreInfo.

        增量对比时延，若时延为0表示所有增量数据都已对比完成。

        :return: The delay of this QueryCompareJobProgressRespIncreInfo.
        :rtype: float
        """
        return self._delay

    @delay.setter
    def delay(self, delay):
        r"""Sets the delay of this QueryCompareJobProgressRespIncreInfo.

        增量对比时延，若时延为0表示所有增量数据都已对比完成。

        :param delay: The delay of this QueryCompareJobProgressRespIncreInfo.
        :type delay: float
        """
        self._delay = delay

    @property
    def src_speed(self):
        r"""Gets the src_speed of this QueryCompareJobProgressRespIncreInfo.

        增量数据对比速率。

        :return: The src_speed of this QueryCompareJobProgressRespIncreInfo.
        :rtype: str
        """
        return self._src_speed

    @src_speed.setter
    def src_speed(self, src_speed):
        r"""Sets the src_speed of this QueryCompareJobProgressRespIncreInfo.

        增量数据对比速率。

        :param src_speed: The src_speed of this QueryCompareJobProgressRespIncreInfo.
        :type src_speed: str
        """
        self._src_speed = src_speed

    @property
    def rps(self):
        r"""Gets the rps of this QueryCompareJobProgressRespIncreInfo.

        每秒对比行数。

        :return: The rps of this QueryCompareJobProgressRespIncreInfo.
        :rtype: int
        """
        return self._rps

    @rps.setter
    def rps(self, rps):
        r"""Sets the rps of this QueryCompareJobProgressRespIncreInfo.

        每秒对比行数。

        :param rps: The rps of this QueryCompareJobProgressRespIncreInfo.
        :type rps: int
        """
        self._rps = rps

    @property
    def log_point(self):
        r"""Gets the log_point of this QueryCompareJobProgressRespIncreInfo.

        增量位点。

        :return: The log_point of this QueryCompareJobProgressRespIncreInfo.
        :rtype: str
        """
        return self._log_point

    @log_point.setter
    def log_point(self, log_point):
        r"""Sets the log_point of this QueryCompareJobProgressRespIncreInfo.

        增量位点。

        :param log_point: The log_point of this QueryCompareJobProgressRespIncreInfo.
        :type log_point: str
        """
        self._log_point = log_point

    @property
    def recheck_entities(self):
        r"""Gets the recheck_entities of this QueryCompareJobProgressRespIncreInfo.

        差异待复查行数。

        :return: The recheck_entities of this QueryCompareJobProgressRespIncreInfo.
        :rtype: int
        """
        return self._recheck_entities

    @recheck_entities.setter
    def recheck_entities(self, recheck_entities):
        r"""Sets the recheck_entities of this QueryCompareJobProgressRespIncreInfo.

        差异待复查行数。

        :param recheck_entities: The recheck_entities of this QueryCompareJobProgressRespIncreInfo.
        :type recheck_entities: int
        """
        self._recheck_entities = recheck_entities

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
        if not isinstance(other, QueryCompareJobProgressRespIncreInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

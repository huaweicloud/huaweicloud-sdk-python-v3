# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CircuitBreaker:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'switch': 'bool',
        'dead_num': 'int',
        'dead_ratio': 'float',
        'block_time': 'int',
        'superposition_num': 'int',
        'suspend_num': 'int',
        'sus_block_time': 'int'
    }

    attribute_map = {
        'switch': 'switch',
        'dead_num': 'dead_num',
        'dead_ratio': 'dead_ratio',
        'block_time': 'block_time',
        'superposition_num': 'superposition_num',
        'suspend_num': 'suspend_num',
        'sus_block_time': 'sus_block_time'
    }

    def __init__(self, switch=None, dead_num=None, dead_ratio=None, block_time=None, superposition_num=None, suspend_num=None, sus_block_time=None):
        """CircuitBreaker

        The model defined in huaweicloud sdk

        :param switch: 熔断开关，是否开启连接保护   - true：开启连接保护   - false: 关闭连接保护 
        :type switch: bool
        :param dead_num: 502/504数量阈值，每30s累加的502/504数量阈值
        :type dead_num: int
        :param dead_ratio: 502/504数量占比(%)，总请求数量中502/504数量占比达到所设定值，并且与数量阈值同时满足时触发宕机保护
        :type dead_ratio: float
        :param block_time: 初次触发宕机的保护时间，即WAF将停止转发用户请求的时间。
        :type block_time: int
        :param superposition_num: 连续触发时，保护时间延长最大倍数，叠加周期为3600s。例如，“初次保护时间”设置为180s，“连续触发叠加系数”设置为3。   - 当触发次数为2（即小于3）时，保护时间为360s。   - 当次数大于等于3时，保护时间为540s。   - 当累计保护时间超过1小时（3600s），叠加次数会从头计数。
        :type superposition_num: int
        :param suspend_num: 读等待URL请求数量阈值，读等待URL请求数量到达设定值即触发连接保护
        :type suspend_num: int
        :param sus_block_time: 读等待URL请求数量超过阈值后的熔断时间，达到数量阈值所触发的保护时间，即WAF将停止转发用户请求的时间。
        :type sus_block_time: int
        """
        
        

        self._switch = None
        self._dead_num = None
        self._dead_ratio = None
        self._block_time = None
        self._superposition_num = None
        self._suspend_num = None
        self._sus_block_time = None
        self.discriminator = None

        if switch is not None:
            self.switch = switch
        if dead_num is not None:
            self.dead_num = dead_num
        if dead_ratio is not None:
            self.dead_ratio = dead_ratio
        if block_time is not None:
            self.block_time = block_time
        if superposition_num is not None:
            self.superposition_num = superposition_num
        if suspend_num is not None:
            self.suspend_num = suspend_num
        if sus_block_time is not None:
            self.sus_block_time = sus_block_time

    @property
    def switch(self):
        """Gets the switch of this CircuitBreaker.

        熔断开关，是否开启连接保护   - true：开启连接保护   - false: 关闭连接保护 

        :return: The switch of this CircuitBreaker.
        :rtype: bool
        """
        return self._switch

    @switch.setter
    def switch(self, switch):
        """Sets the switch of this CircuitBreaker.

        熔断开关，是否开启连接保护   - true：开启连接保护   - false: 关闭连接保护 

        :param switch: The switch of this CircuitBreaker.
        :type switch: bool
        """
        self._switch = switch

    @property
    def dead_num(self):
        """Gets the dead_num of this CircuitBreaker.

        502/504数量阈值，每30s累加的502/504数量阈值

        :return: The dead_num of this CircuitBreaker.
        :rtype: int
        """
        return self._dead_num

    @dead_num.setter
    def dead_num(self, dead_num):
        """Sets the dead_num of this CircuitBreaker.

        502/504数量阈值，每30s累加的502/504数量阈值

        :param dead_num: The dead_num of this CircuitBreaker.
        :type dead_num: int
        """
        self._dead_num = dead_num

    @property
    def dead_ratio(self):
        """Gets the dead_ratio of this CircuitBreaker.

        502/504数量占比(%)，总请求数量中502/504数量占比达到所设定值，并且与数量阈值同时满足时触发宕机保护

        :return: The dead_ratio of this CircuitBreaker.
        :rtype: float
        """
        return self._dead_ratio

    @dead_ratio.setter
    def dead_ratio(self, dead_ratio):
        """Sets the dead_ratio of this CircuitBreaker.

        502/504数量占比(%)，总请求数量中502/504数量占比达到所设定值，并且与数量阈值同时满足时触发宕机保护

        :param dead_ratio: The dead_ratio of this CircuitBreaker.
        :type dead_ratio: float
        """
        self._dead_ratio = dead_ratio

    @property
    def block_time(self):
        """Gets the block_time of this CircuitBreaker.

        初次触发宕机的保护时间，即WAF将停止转发用户请求的时间。

        :return: The block_time of this CircuitBreaker.
        :rtype: int
        """
        return self._block_time

    @block_time.setter
    def block_time(self, block_time):
        """Sets the block_time of this CircuitBreaker.

        初次触发宕机的保护时间，即WAF将停止转发用户请求的时间。

        :param block_time: The block_time of this CircuitBreaker.
        :type block_time: int
        """
        self._block_time = block_time

    @property
    def superposition_num(self):
        """Gets the superposition_num of this CircuitBreaker.

        连续触发时，保护时间延长最大倍数，叠加周期为3600s。例如，“初次保护时间”设置为180s，“连续触发叠加系数”设置为3。   - 当触发次数为2（即小于3）时，保护时间为360s。   - 当次数大于等于3时，保护时间为540s。   - 当累计保护时间超过1小时（3600s），叠加次数会从头计数。

        :return: The superposition_num of this CircuitBreaker.
        :rtype: int
        """
        return self._superposition_num

    @superposition_num.setter
    def superposition_num(self, superposition_num):
        """Sets the superposition_num of this CircuitBreaker.

        连续触发时，保护时间延长最大倍数，叠加周期为3600s。例如，“初次保护时间”设置为180s，“连续触发叠加系数”设置为3。   - 当触发次数为2（即小于3）时，保护时间为360s。   - 当次数大于等于3时，保护时间为540s。   - 当累计保护时间超过1小时（3600s），叠加次数会从头计数。

        :param superposition_num: The superposition_num of this CircuitBreaker.
        :type superposition_num: int
        """
        self._superposition_num = superposition_num

    @property
    def suspend_num(self):
        """Gets the suspend_num of this CircuitBreaker.

        读等待URL请求数量阈值，读等待URL请求数量到达设定值即触发连接保护

        :return: The suspend_num of this CircuitBreaker.
        :rtype: int
        """
        return self._suspend_num

    @suspend_num.setter
    def suspend_num(self, suspend_num):
        """Sets the suspend_num of this CircuitBreaker.

        读等待URL请求数量阈值，读等待URL请求数量到达设定值即触发连接保护

        :param suspend_num: The suspend_num of this CircuitBreaker.
        :type suspend_num: int
        """
        self._suspend_num = suspend_num

    @property
    def sus_block_time(self):
        """Gets the sus_block_time of this CircuitBreaker.

        读等待URL请求数量超过阈值后的熔断时间，达到数量阈值所触发的保护时间，即WAF将停止转发用户请求的时间。

        :return: The sus_block_time of this CircuitBreaker.
        :rtype: int
        """
        return self._sus_block_time

    @sus_block_time.setter
    def sus_block_time(self, sus_block_time):
        """Sets the sus_block_time of this CircuitBreaker.

        读等待URL请求数量超过阈值后的熔断时间，达到数量阈值所触发的保护时间，即WAF将停止转发用户请求的时间。

        :param sus_block_time: The sus_block_time of this CircuitBreaker.
        :type sus_block_time: int
        """
        self._sus_block_time = sus_block_time

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
        if not isinstance(other, CircuitBreaker):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

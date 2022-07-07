# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class FlavorInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'connection': 'int',
        'cps': 'int',
        'qps': 'int',
        'bandwidth': 'int',
        'lcu': 'int',
        'https_cps': 'int'
    }

    attribute_map = {
        'connection': 'connection',
        'cps': 'cps',
        'qps': 'qps',
        'bandwidth': 'bandwidth',
        'lcu': 'lcu',
        'https_cps': 'https_cps'
    }

    def __init__(self, connection=None, cps=None, qps=None, bandwidth=None, lcu=None, https_cps=None):
        """FlavorInfo

        The model defined in huaweicloud sdk

        :param connection: 并发数。单位：个
        :type connection: int
        :param cps: 新建数。单位：个
        :type cps: int
        :param qps: 7层每秒查询数。单位：个
        :type qps: int
        :param bandwidth: 带宽。单位：Mbit/s
        :type bandwidth: int
        :param lcu: 当前flavor对应的lcu数量。 LCU是用来衡量独享型ELB处理性能综合指标，LCU值越大，性能越好。单位：个
        :type lcu: int
        :param https_cps: https新建连接数。单位：个
        :type https_cps: int
        """
        
        

        self._connection = None
        self._cps = None
        self._qps = None
        self._bandwidth = None
        self._lcu = None
        self._https_cps = None
        self.discriminator = None

        self.connection = connection
        self.cps = cps
        if qps is not None:
            self.qps = qps
        if bandwidth is not None:
            self.bandwidth = bandwidth
        if lcu is not None:
            self.lcu = lcu
        if https_cps is not None:
            self.https_cps = https_cps

    @property
    def connection(self):
        """Gets the connection of this FlavorInfo.

        并发数。单位：个

        :return: The connection of this FlavorInfo.
        :rtype: int
        """
        return self._connection

    @connection.setter
    def connection(self, connection):
        """Sets the connection of this FlavorInfo.

        并发数。单位：个

        :param connection: The connection of this FlavorInfo.
        :type connection: int
        """
        self._connection = connection

    @property
    def cps(self):
        """Gets the cps of this FlavorInfo.

        新建数。单位：个

        :return: The cps of this FlavorInfo.
        :rtype: int
        """
        return self._cps

    @cps.setter
    def cps(self, cps):
        """Sets the cps of this FlavorInfo.

        新建数。单位：个

        :param cps: The cps of this FlavorInfo.
        :type cps: int
        """
        self._cps = cps

    @property
    def qps(self):
        """Gets the qps of this FlavorInfo.

        7层每秒查询数。单位：个

        :return: The qps of this FlavorInfo.
        :rtype: int
        """
        return self._qps

    @qps.setter
    def qps(self, qps):
        """Sets the qps of this FlavorInfo.

        7层每秒查询数。单位：个

        :param qps: The qps of this FlavorInfo.
        :type qps: int
        """
        self._qps = qps

    @property
    def bandwidth(self):
        """Gets the bandwidth of this FlavorInfo.

        带宽。单位：Mbit/s

        :return: The bandwidth of this FlavorInfo.
        :rtype: int
        """
        return self._bandwidth

    @bandwidth.setter
    def bandwidth(self, bandwidth):
        """Sets the bandwidth of this FlavorInfo.

        带宽。单位：Mbit/s

        :param bandwidth: The bandwidth of this FlavorInfo.
        :type bandwidth: int
        """
        self._bandwidth = bandwidth

    @property
    def lcu(self):
        """Gets the lcu of this FlavorInfo.

        当前flavor对应的lcu数量。 LCU是用来衡量独享型ELB处理性能综合指标，LCU值越大，性能越好。单位：个

        :return: The lcu of this FlavorInfo.
        :rtype: int
        """
        return self._lcu

    @lcu.setter
    def lcu(self, lcu):
        """Sets the lcu of this FlavorInfo.

        当前flavor对应的lcu数量。 LCU是用来衡量独享型ELB处理性能综合指标，LCU值越大，性能越好。单位：个

        :param lcu: The lcu of this FlavorInfo.
        :type lcu: int
        """
        self._lcu = lcu

    @property
    def https_cps(self):
        """Gets the https_cps of this FlavorInfo.

        https新建连接数。单位：个

        :return: The https_cps of this FlavorInfo.
        :rtype: int
        """
        return self._https_cps

    @https_cps.setter
    def https_cps(self, https_cps):
        """Sets the https_cps of this FlavorInfo.

        https新建连接数。单位：个

        :param https_cps: The https_cps of this FlavorInfo.
        :type https_cps: int
        """
        self._https_cps = https_cps

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
        if not isinstance(other, FlavorInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

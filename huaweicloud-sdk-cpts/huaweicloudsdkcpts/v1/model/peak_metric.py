# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PeakMetric:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'vuser': 'int',
        'rps': 'float',
        'avg_rt': 'float',
        'success_rate': 'float',
        'peak_time': 'str'
    }

    attribute_map = {
        'vuser': 'vuser',
        'rps': 'rps',
        'avg_rt': 'avgRT',
        'success_rate': 'successRate',
        'peak_time': 'peakTime'
    }

    def __init__(self, vuser=None, rps=None, avg_rt=None, success_rate=None, peak_time=None):
        """PeakMetric

        The model defined in huaweicloud sdk

        :param vuser: vusers
        :type vuser: int
        :param rps: tps
        :type rps: float
        :param avg_rt: avgRT
        :type avg_rt: float
        :param success_rate: 成功率
        :type success_rate: float
        :param peak_time: 峰值时间
        :type peak_time: str
        """
        
        

        self._vuser = None
        self._rps = None
        self._avg_rt = None
        self._success_rate = None
        self._peak_time = None
        self.discriminator = None

        if vuser is not None:
            self.vuser = vuser
        if rps is not None:
            self.rps = rps
        if avg_rt is not None:
            self.avg_rt = avg_rt
        if success_rate is not None:
            self.success_rate = success_rate
        if peak_time is not None:
            self.peak_time = peak_time

    @property
    def vuser(self):
        """Gets the vuser of this PeakMetric.

        vusers

        :return: The vuser of this PeakMetric.
        :rtype: int
        """
        return self._vuser

    @vuser.setter
    def vuser(self, vuser):
        """Sets the vuser of this PeakMetric.

        vusers

        :param vuser: The vuser of this PeakMetric.
        :type vuser: int
        """
        self._vuser = vuser

    @property
    def rps(self):
        """Gets the rps of this PeakMetric.

        tps

        :return: The rps of this PeakMetric.
        :rtype: float
        """
        return self._rps

    @rps.setter
    def rps(self, rps):
        """Sets the rps of this PeakMetric.

        tps

        :param rps: The rps of this PeakMetric.
        :type rps: float
        """
        self._rps = rps

    @property
    def avg_rt(self):
        """Gets the avg_rt of this PeakMetric.

        avgRT

        :return: The avg_rt of this PeakMetric.
        :rtype: float
        """
        return self._avg_rt

    @avg_rt.setter
    def avg_rt(self, avg_rt):
        """Sets the avg_rt of this PeakMetric.

        avgRT

        :param avg_rt: The avg_rt of this PeakMetric.
        :type avg_rt: float
        """
        self._avg_rt = avg_rt

    @property
    def success_rate(self):
        """Gets the success_rate of this PeakMetric.

        成功率

        :return: The success_rate of this PeakMetric.
        :rtype: float
        """
        return self._success_rate

    @success_rate.setter
    def success_rate(self, success_rate):
        """Sets the success_rate of this PeakMetric.

        成功率

        :param success_rate: The success_rate of this PeakMetric.
        :type success_rate: float
        """
        self._success_rate = success_rate

    @property
    def peak_time(self):
        """Gets the peak_time of this PeakMetric.

        峰值时间

        :return: The peak_time of this PeakMetric.
        :rtype: str
        """
        return self._peak_time

    @peak_time.setter
    def peak_time(self, peak_time):
        """Sets the peak_time of this PeakMetric.

        峰值时间

        :param peak_time: The peak_time of this PeakMetric.
        :type peak_time: str
        """
        self._peak_time = peak_time

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
        if not isinstance(other, PeakMetric):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CPUThresholdData:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'cpu': 'int',
        'cpu_default': 'int'
    }

    attribute_map = {
        'cpu': 'cpu',
        'cpu_default': 'cpuDefault'
    }

    def __init__(self, cpu=None, cpu_default=None):
        r"""CPUThresholdData

        The model defined in huaweicloud sdk

        :param cpu: 自定义的cpu阈值，单位为百分比(%)
        :type cpu: int
        :param cpu_default: cpu阈值默认值，单位为百分比(%)
        :type cpu_default: int
        """
        
        

        self._cpu = None
        self._cpu_default = None
        self.discriminator = None

        if cpu is not None:
            self.cpu = cpu
        if cpu_default is not None:
            self.cpu_default = cpu_default

    @property
    def cpu(self):
        r"""Gets the cpu of this CPUThresholdData.

        自定义的cpu阈值，单位为百分比(%)

        :return: The cpu of this CPUThresholdData.
        :rtype: int
        """
        return self._cpu

    @cpu.setter
    def cpu(self, cpu):
        r"""Sets the cpu of this CPUThresholdData.

        自定义的cpu阈值，单位为百分比(%)

        :param cpu: The cpu of this CPUThresholdData.
        :type cpu: int
        """
        self._cpu = cpu

    @property
    def cpu_default(self):
        r"""Gets the cpu_default of this CPUThresholdData.

        cpu阈值默认值，单位为百分比(%)

        :return: The cpu_default of this CPUThresholdData.
        :rtype: int
        """
        return self._cpu_default

    @cpu_default.setter
    def cpu_default(self, cpu_default):
        r"""Sets the cpu_default of this CPUThresholdData.

        cpu阈值默认值，单位为百分比(%)

        :param cpu_default: The cpu_default of this CPUThresholdData.
        :type cpu_default: int
        """
        self._cpu_default = cpu_default

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
        if not isinstance(other, CPUThresholdData):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

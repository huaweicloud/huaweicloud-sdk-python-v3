# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class StatUsageInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'stat_time': 'str',
        'guaranteed_band_width': 'str',
        'usage': 'str',
        'measure_id': 'int'
    }

    attribute_map = {
        'stat_time': 'stat_time',
        'guaranteed_band_width': 'guaranteed_band_width',
        'usage': 'usage',
        'measure_id': 'measure_id'
    }

    def __init__(self, stat_time=None, guaranteed_band_width=None, usage=None, measure_id=None):
        """StatUsageInfo

        The model defined in huaweicloud sdk

        :param stat_time: 统计时间点，UTC时间，格式为YYYY-MM-DDTHH:MM:SSZ。
        :type stat_time: str
        :param guaranteed_band_width: 保底带宽。  说明： 该字段为预留值，当前始终为空；当场景为95增强时才返回数值。
        :type guaranteed_band_width: str
        :param usage: 用量。
        :type usage: str
        :param measure_id: 单位，您可以调用查询度量单位列表接口获取。带宽和用量使用相同的计量单位。
        :type measure_id: int
        """
        
        

        self._stat_time = None
        self._guaranteed_band_width = None
        self._usage = None
        self._measure_id = None
        self.discriminator = None

        if stat_time is not None:
            self.stat_time = stat_time
        if guaranteed_band_width is not None:
            self.guaranteed_band_width = guaranteed_band_width
        if usage is not None:
            self.usage = usage
        if measure_id is not None:
            self.measure_id = measure_id

    @property
    def stat_time(self):
        """Gets the stat_time of this StatUsageInfo.

        统计时间点，UTC时间，格式为YYYY-MM-DDTHH:MM:SSZ。

        :return: The stat_time of this StatUsageInfo.
        :rtype: str
        """
        return self._stat_time

    @stat_time.setter
    def stat_time(self, stat_time):
        """Sets the stat_time of this StatUsageInfo.

        统计时间点，UTC时间，格式为YYYY-MM-DDTHH:MM:SSZ。

        :param stat_time: The stat_time of this StatUsageInfo.
        :type stat_time: str
        """
        self._stat_time = stat_time

    @property
    def guaranteed_band_width(self):
        """Gets the guaranteed_band_width of this StatUsageInfo.

        保底带宽。  说明： 该字段为预留值，当前始终为空；当场景为95增强时才返回数值。

        :return: The guaranteed_band_width of this StatUsageInfo.
        :rtype: str
        """
        return self._guaranteed_band_width

    @guaranteed_band_width.setter
    def guaranteed_band_width(self, guaranteed_band_width):
        """Sets the guaranteed_band_width of this StatUsageInfo.

        保底带宽。  说明： 该字段为预留值，当前始终为空；当场景为95增强时才返回数值。

        :param guaranteed_band_width: The guaranteed_band_width of this StatUsageInfo.
        :type guaranteed_band_width: str
        """
        self._guaranteed_band_width = guaranteed_band_width

    @property
    def usage(self):
        """Gets the usage of this StatUsageInfo.

        用量。

        :return: The usage of this StatUsageInfo.
        :rtype: str
        """
        return self._usage

    @usage.setter
    def usage(self, usage):
        """Sets the usage of this StatUsageInfo.

        用量。

        :param usage: The usage of this StatUsageInfo.
        :type usage: str
        """
        self._usage = usage

    @property
    def measure_id(self):
        """Gets the measure_id of this StatUsageInfo.

        单位，您可以调用查询度量单位列表接口获取。带宽和用量使用相同的计量单位。

        :return: The measure_id of this StatUsageInfo.
        :rtype: int
        """
        return self._measure_id

    @measure_id.setter
    def measure_id(self, measure_id):
        """Sets the measure_id of this StatUsageInfo.

        单位，您可以调用查询度量单位列表接口获取。带宽和用量使用相同的计量单位。

        :param measure_id: The measure_id of this StatUsageInfo.
        :type measure_id: int
        """
        self._measure_id = measure_id

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
        if not isinstance(other, StatUsageInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

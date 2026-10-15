# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class KeyTrendData:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'name': 'str',
        'stat_type': 'str',
        'interval': 'int',
        'trend_list': 'list[TrendPoint]'
    }

    attribute_map = {
        'name': 'name',
        'stat_type': 'stat_type',
        'interval': 'interval',
        'trend_list': 'trend_list'
    }

    def __init__(self, name=None, stat_type=None, interval=None, trend_list=None):
        r"""KeyTrendData

        The model defined in huaweicloud sdk

        :param name: key名称
        :type name: str
        :param stat_type: 统计维度。size/storage/qps/traffic
        :type stat_type: str
        :param interval: 时间粒度（毫秒）
        :type interval: int
        :param trend_list: 趋势数据点列表
        :type trend_list: list[:class:`huaweicloudsdkdas.v3.TrendPoint`]
        """
        
        

        self._name = None
        self._stat_type = None
        self._interval = None
        self._trend_list = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if stat_type is not None:
            self.stat_type = stat_type
        if interval is not None:
            self.interval = interval
        if trend_list is not None:
            self.trend_list = trend_list

    @property
    def name(self):
        r"""Gets the name of this KeyTrendData.

        key名称

        :return: The name of this KeyTrendData.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this KeyTrendData.

        key名称

        :param name: The name of this KeyTrendData.
        :type name: str
        """
        self._name = name

    @property
    def stat_type(self):
        r"""Gets the stat_type of this KeyTrendData.

        统计维度。size/storage/qps/traffic

        :return: The stat_type of this KeyTrendData.
        :rtype: str
        """
        return self._stat_type

    @stat_type.setter
    def stat_type(self, stat_type):
        r"""Sets the stat_type of this KeyTrendData.

        统计维度。size/storage/qps/traffic

        :param stat_type: The stat_type of this KeyTrendData.
        :type stat_type: str
        """
        self._stat_type = stat_type

    @property
    def interval(self):
        r"""Gets the interval of this KeyTrendData.

        时间粒度（毫秒）

        :return: The interval of this KeyTrendData.
        :rtype: int
        """
        return self._interval

    @interval.setter
    def interval(self, interval):
        r"""Sets the interval of this KeyTrendData.

        时间粒度（毫秒）

        :param interval: The interval of this KeyTrendData.
        :type interval: int
        """
        self._interval = interval

    @property
    def trend_list(self):
        r"""Gets the trend_list of this KeyTrendData.

        趋势数据点列表

        :return: The trend_list of this KeyTrendData.
        :rtype: list[:class:`huaweicloudsdkdas.v3.TrendPoint`]
        """
        return self._trend_list

    @trend_list.setter
    def trend_list(self, trend_list):
        r"""Sets the trend_list of this KeyTrendData.

        趋势数据点列表

        :param trend_list: The trend_list of this KeyTrendData.
        :type trend_list: list[:class:`huaweicloudsdkdas.v3.TrendPoint`]
        """
        self._trend_list = trend_list

    def to_dict(self):
        result = {}

        for attr, _ in self.openapi_types.items():
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
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, KeyTrendData):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

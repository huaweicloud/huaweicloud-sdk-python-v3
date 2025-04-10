# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class NumFeatureReport:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'avg': 'float',
        'min': 'float',
        'max': 'float',
        'median': 'float',
        'percents_agg': 'str',
        'name': 'str',
        'data_type': 'str'
    }

    attribute_map = {
        'avg': 'avg',
        'min': 'min',
        'max': 'max',
        'median': 'median',
        'percents_agg': 'percents_agg',
        'name': 'name',
        'data_type': 'data_type'
    }

    def __init__(self, avg=None, min=None, max=None, median=None, percents_agg=None, name=None, data_type=None):
        r"""NumFeatureReport

        The model defined in huaweicloud sdk

        :param avg: 平均值。
        :type avg: float
        :param min: 最小值。
        :type min: float
        :param max: 最大值。
        :type max: float
        :param median: 中位数。
        :type median: float
        :param percents_agg: 百分位统计。
        :type percents_agg: str
        :param name: 特征名。
        :type name: str
        :param data_type: 特征类型。
        :type data_type: str
        """
        
        

        self._avg = None
        self._min = None
        self._max = None
        self._median = None
        self._percents_agg = None
        self._name = None
        self._data_type = None
        self.discriminator = None

        if avg is not None:
            self.avg = avg
        if min is not None:
            self.min = min
        if max is not None:
            self.max = max
        if median is not None:
            self.median = median
        if percents_agg is not None:
            self.percents_agg = percents_agg
        if name is not None:
            self.name = name
        if data_type is not None:
            self.data_type = data_type

    @property
    def avg(self):
        r"""Gets the avg of this NumFeatureReport.

        平均值。

        :return: The avg of this NumFeatureReport.
        :rtype: float
        """
        return self._avg

    @avg.setter
    def avg(self, avg):
        r"""Sets the avg of this NumFeatureReport.

        平均值。

        :param avg: The avg of this NumFeatureReport.
        :type avg: float
        """
        self._avg = avg

    @property
    def min(self):
        r"""Gets the min of this NumFeatureReport.

        最小值。

        :return: The min of this NumFeatureReport.
        :rtype: float
        """
        return self._min

    @min.setter
    def min(self, min):
        r"""Sets the min of this NumFeatureReport.

        最小值。

        :param min: The min of this NumFeatureReport.
        :type min: float
        """
        self._min = min

    @property
    def max(self):
        r"""Gets the max of this NumFeatureReport.

        最大值。

        :return: The max of this NumFeatureReport.
        :rtype: float
        """
        return self._max

    @max.setter
    def max(self, max):
        r"""Sets the max of this NumFeatureReport.

        最大值。

        :param max: The max of this NumFeatureReport.
        :type max: float
        """
        self._max = max

    @property
    def median(self):
        r"""Gets the median of this NumFeatureReport.

        中位数。

        :return: The median of this NumFeatureReport.
        :rtype: float
        """
        return self._median

    @median.setter
    def median(self, median):
        r"""Sets the median of this NumFeatureReport.

        中位数。

        :param median: The median of this NumFeatureReport.
        :type median: float
        """
        self._median = median

    @property
    def percents_agg(self):
        r"""Gets the percents_agg of this NumFeatureReport.

        百分位统计。

        :return: The percents_agg of this NumFeatureReport.
        :rtype: str
        """
        return self._percents_agg

    @percents_agg.setter
    def percents_agg(self, percents_agg):
        r"""Sets the percents_agg of this NumFeatureReport.

        百分位统计。

        :param percents_agg: The percents_agg of this NumFeatureReport.
        :type percents_agg: str
        """
        self._percents_agg = percents_agg

    @property
    def name(self):
        r"""Gets the name of this NumFeatureReport.

        特征名。

        :return: The name of this NumFeatureReport.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this NumFeatureReport.

        特征名。

        :param name: The name of this NumFeatureReport.
        :type name: str
        """
        self._name = name

    @property
    def data_type(self):
        r"""Gets the data_type of this NumFeatureReport.

        特征类型。

        :return: The data_type of this NumFeatureReport.
        :rtype: str
        """
        return self._data_type

    @data_type.setter
    def data_type(self, data_type):
        r"""Sets the data_type of this NumFeatureReport.

        特征类型。

        :param data_type: The data_type of this NumFeatureReport.
        :type data_type: str
        """
        self._data_type = data_type

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
        if not isinstance(other, NumFeatureReport):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

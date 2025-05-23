# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SeriesAPIQueryItemParam:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'series': 'list[QuerySeriesOptionParam]'
    }

    attribute_map = {
        'series': 'series'
    }

    def __init__(self, series=None):
        r"""SeriesAPIQueryItemParam

        The model defined in huaweicloud sdk

        :param series: 通过该数组传递的参数信息进行时间序列查询。
        :type series: list[:class:`huaweicloudsdkaom.v2.QuerySeriesOptionParam`]
        """
        
        

        self._series = None
        self.discriminator = None

        self.series = series

    @property
    def series(self):
        r"""Gets the series of this SeriesAPIQueryItemParam.

        通过该数组传递的参数信息进行时间序列查询。

        :return: The series of this SeriesAPIQueryItemParam.
        :rtype: list[:class:`huaweicloudsdkaom.v2.QuerySeriesOptionParam`]
        """
        return self._series

    @series.setter
    def series(self, series):
        r"""Sets the series of this SeriesAPIQueryItemParam.

        通过该数组传递的参数信息进行时间序列查询。

        :param series: The series of this SeriesAPIQueryItemParam.
        :type series: list[:class:`huaweicloudsdkaom.v2.QuerySeriesOptionParam`]
        """
        self._series = series

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
        if not isinstance(other, SeriesAPIQueryItemParam):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class QueryRiskItemsItems:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'metric_code': 'str',
        'threshold': 'float',
        'unit': 'str'
    }

    attribute_map = {
        'metric_code': 'metric_code',
        'threshold': 'threshold',
        'unit': 'unit'
    }

    def __init__(self, metric_code=None, threshold=None, unit=None):
        r"""QueryRiskItemsItems

        The model defined in huaweicloud sdk

        :param metric_code: 指标码
        :type metric_code: str
        :param threshold: 阈值
        :type threshold: float
        :param unit: 单位
        :type unit: str
        """
        
        

        self._metric_code = None
        self._threshold = None
        self._unit = None
        self.discriminator = None

        if metric_code is not None:
            self.metric_code = metric_code
        if threshold is not None:
            self.threshold = threshold
        if unit is not None:
            self.unit = unit

    @property
    def metric_code(self):
        r"""Gets the metric_code of this QueryRiskItemsItems.

        指标码

        :return: The metric_code of this QueryRiskItemsItems.
        :rtype: str
        """
        return self._metric_code

    @metric_code.setter
    def metric_code(self, metric_code):
        r"""Sets the metric_code of this QueryRiskItemsItems.

        指标码

        :param metric_code: The metric_code of this QueryRiskItemsItems.
        :type metric_code: str
        """
        self._metric_code = metric_code

    @property
    def threshold(self):
        r"""Gets the threshold of this QueryRiskItemsItems.

        阈值

        :return: The threshold of this QueryRiskItemsItems.
        :rtype: float
        """
        return self._threshold

    @threshold.setter
    def threshold(self, threshold):
        r"""Sets the threshold of this QueryRiskItemsItems.

        阈值

        :param threshold: The threshold of this QueryRiskItemsItems.
        :type threshold: float
        """
        self._threshold = threshold

    @property
    def unit(self):
        r"""Gets the unit of this QueryRiskItemsItems.

        单位

        :return: The unit of this QueryRiskItemsItems.
        :rtype: str
        """
        return self._unit

    @unit.setter
    def unit(self, unit):
        r"""Sets the unit of this QueryRiskItemsItems.

        单位

        :param unit: The unit of this QueryRiskItemsItems.
        :type unit: str
        """
        self._unit = unit

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
        if not isinstance(other, QueryRiskItemsItems):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

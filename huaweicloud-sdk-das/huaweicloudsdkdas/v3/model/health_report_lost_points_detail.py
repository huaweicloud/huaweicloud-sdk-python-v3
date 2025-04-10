# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class HealthReportLostPointsDetail:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'metric': 'str',
        'lost_points': 'float',
        'risk_level': 'str'
    }

    attribute_map = {
        'metric': 'metric',
        'lost_points': 'lost_points',
        'risk_level': 'risk_level'
    }

    def __init__(self, metric=None, lost_points=None, risk_level=None):
        r"""HealthReportLostPointsDetail

        The model defined in huaweicloud sdk

        :param metric: 扣分项。
        :type metric: str
        :param lost_points: 所扣分数。
        :type lost_points: float
        :param risk_level: 事件等级。
        :type risk_level: str
        """
        
        

        self._metric = None
        self._lost_points = None
        self._risk_level = None
        self.discriminator = None

        self.metric = metric
        self.lost_points = lost_points
        self.risk_level = risk_level

    @property
    def metric(self):
        r"""Gets the metric of this HealthReportLostPointsDetail.

        扣分项。

        :return: The metric of this HealthReportLostPointsDetail.
        :rtype: str
        """
        return self._metric

    @metric.setter
    def metric(self, metric):
        r"""Sets the metric of this HealthReportLostPointsDetail.

        扣分项。

        :param metric: The metric of this HealthReportLostPointsDetail.
        :type metric: str
        """
        self._metric = metric

    @property
    def lost_points(self):
        r"""Gets the lost_points of this HealthReportLostPointsDetail.

        所扣分数。

        :return: The lost_points of this HealthReportLostPointsDetail.
        :rtype: float
        """
        return self._lost_points

    @lost_points.setter
    def lost_points(self, lost_points):
        r"""Sets the lost_points of this HealthReportLostPointsDetail.

        所扣分数。

        :param lost_points: The lost_points of this HealthReportLostPointsDetail.
        :type lost_points: float
        """
        self._lost_points = lost_points

    @property
    def risk_level(self):
        r"""Gets the risk_level of this HealthReportLostPointsDetail.

        事件等级。

        :return: The risk_level of this HealthReportLostPointsDetail.
        :rtype: str
        """
        return self._risk_level

    @risk_level.setter
    def risk_level(self, risk_level):
        r"""Sets the risk_level of this HealthReportLostPointsDetail.

        事件等级。

        :param risk_level: The risk_level of this HealthReportLostPointsDetail.
        :type risk_level: str
        """
        self._risk_level = risk_level

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
        if not isinstance(other, HealthReportLostPointsDetail):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

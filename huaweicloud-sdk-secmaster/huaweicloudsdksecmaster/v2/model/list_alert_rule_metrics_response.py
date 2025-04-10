# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListAlertRuleMetricsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'category': 'str',
        'metric': 'dict(str, float)',
        'x_request_id': 'str'
    }

    attribute_map = {
        'category': 'category',
        'metric': 'metric',
        'x_request_id': 'X-request-id'
    }

    def __init__(self, category=None, metric=None, x_request_id=None):
        r"""ListAlertRuleMetricsResponse

        The model defined in huaweicloud sdk

        :param category: 指标类型，分组数量。Metric category. GROUP_COUNT.
        :type category: str
        :param metric: 指标值。Metric value.
        :type metric: dict(str, float)
        :param x_request_id: 
        :type x_request_id: str
        """
        
        super(ListAlertRuleMetricsResponse, self).__init__()

        self._category = None
        self._metric = None
        self._x_request_id = None
        self.discriminator = None

        if category is not None:
            self.category = category
        if metric is not None:
            self.metric = metric
        if x_request_id is not None:
            self.x_request_id = x_request_id

    @property
    def category(self):
        r"""Gets the category of this ListAlertRuleMetricsResponse.

        指标类型，分组数量。Metric category. GROUP_COUNT.

        :return: The category of this ListAlertRuleMetricsResponse.
        :rtype: str
        """
        return self._category

    @category.setter
    def category(self, category):
        r"""Sets the category of this ListAlertRuleMetricsResponse.

        指标类型，分组数量。Metric category. GROUP_COUNT.

        :param category: The category of this ListAlertRuleMetricsResponse.
        :type category: str
        """
        self._category = category

    @property
    def metric(self):
        r"""Gets the metric of this ListAlertRuleMetricsResponse.

        指标值。Metric value.

        :return: The metric of this ListAlertRuleMetricsResponse.
        :rtype: dict(str, float)
        """
        return self._metric

    @metric.setter
    def metric(self, metric):
        r"""Sets the metric of this ListAlertRuleMetricsResponse.

        指标值。Metric value.

        :param metric: The metric of this ListAlertRuleMetricsResponse.
        :type metric: dict(str, float)
        """
        self._metric = metric

    @property
    def x_request_id(self):
        r"""Gets the x_request_id of this ListAlertRuleMetricsResponse.

        :return: The x_request_id of this ListAlertRuleMetricsResponse.
        :rtype: str
        """
        return self._x_request_id

    @x_request_id.setter
    def x_request_id(self, x_request_id):
        r"""Sets the x_request_id of this ListAlertRuleMetricsResponse.

        :param x_request_id: The x_request_id of this ListAlertRuleMetricsResponse.
        :type x_request_id: str
        """
        self._x_request_id = x_request_id

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
        if not isinstance(other, ListAlertRuleMetricsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

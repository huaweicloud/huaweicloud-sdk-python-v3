# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListRiskTrendResponse(SdkResponse):

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
        'metric': 'QueryRiskTrendMetric'
    }

    attribute_map = {
        'metric_code': 'metric_code',
        'metric': 'metric'
    }

    def __init__(self, metric_code=None, metric=None):
        r"""ListRiskTrendResponse

        The model defined in huaweicloud sdk

        :param metric_code: 指标码
        :type metric_code: str
        :param metric: 
        :type metric: :class:`huaweicloudsdkdas.v3.QueryRiskTrendMetric`
        """
        
        super(ListRiskTrendResponse, self).__init__()

        self._metric_code = None
        self._metric = None
        self.discriminator = None

        if metric_code is not None:
            self.metric_code = metric_code
        if metric is not None:
            self.metric = metric

    @property
    def metric_code(self):
        r"""Gets the metric_code of this ListRiskTrendResponse.

        指标码

        :return: The metric_code of this ListRiskTrendResponse.
        :rtype: str
        """
        return self._metric_code

    @metric_code.setter
    def metric_code(self, metric_code):
        r"""Sets the metric_code of this ListRiskTrendResponse.

        指标码

        :param metric_code: The metric_code of this ListRiskTrendResponse.
        :type metric_code: str
        """
        self._metric_code = metric_code

    @property
    def metric(self):
        r"""Gets the metric of this ListRiskTrendResponse.

        :return: The metric of this ListRiskTrendResponse.
        :rtype: :class:`huaweicloudsdkdas.v3.QueryRiskTrendMetric`
        """
        return self._metric

    @metric.setter
    def metric(self, metric):
        r"""Sets the metric of this ListRiskTrendResponse.

        :param metric: The metric of this ListRiskTrendResponse.
        :type metric: :class:`huaweicloudsdkdas.v3.QueryRiskTrendMetric`
        """
        self._metric = metric

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
        if not isinstance(other, ListRiskTrendResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

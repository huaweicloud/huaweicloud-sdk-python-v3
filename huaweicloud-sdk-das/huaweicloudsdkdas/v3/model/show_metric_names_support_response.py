# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowMetricNamesSupportResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'support_metric_names': 'list[SupportMetricNameListSupportMetricNames]'
    }

    attribute_map = {
        'support_metric_names': 'support_metric_names'
    }

    def __init__(self, support_metric_names=None):
        r"""ShowMetricNamesSupportResponse

        The model defined in huaweicloud sdk

        :param support_metric_names: 支持指标名称列表
        :type support_metric_names: list[:class:`huaweicloudsdkdas.v3.SupportMetricNameListSupportMetricNames`]
        """
        
        super(ShowMetricNamesSupportResponse, self).__init__()

        self._support_metric_names = None
        self.discriminator = None

        if support_metric_names is not None:
            self.support_metric_names = support_metric_names

    @property
    def support_metric_names(self):
        r"""Gets the support_metric_names of this ShowMetricNamesSupportResponse.

        支持指标名称列表

        :return: The support_metric_names of this ShowMetricNamesSupportResponse.
        :rtype: list[:class:`huaweicloudsdkdas.v3.SupportMetricNameListSupportMetricNames`]
        """
        return self._support_metric_names

    @support_metric_names.setter
    def support_metric_names(self, support_metric_names):
        r"""Sets the support_metric_names of this ShowMetricNamesSupportResponse.

        支持指标名称列表

        :param support_metric_names: The support_metric_names of this ShowMetricNamesSupportResponse.
        :type support_metric_names: list[:class:`huaweicloudsdkdas.v3.SupportMetricNameListSupportMetricNames`]
        """
        self._support_metric_names = support_metric_names

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
        if not isinstance(other, ShowMetricNamesSupportResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

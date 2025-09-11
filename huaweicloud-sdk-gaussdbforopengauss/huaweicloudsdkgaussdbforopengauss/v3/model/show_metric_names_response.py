# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowMetricNamesResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'group_name': 'str',
        'metric_names': 'list[MetricNameResult]'
    }

    attribute_map = {
        'group_name': 'group_name',
        'metric_names': 'metric_names'
    }

    def __init__(self, group_name=None, metric_names=None):
        r"""ShowMetricNamesResponse

        The model defined in huaweicloud sdk

        :param group_name: **参数解释**: 指标组名。 **取值范围**: 不涉及。
        :type group_name: str
        :param metric_names: **参数解释**: 指标分组名称信息。
        :type metric_names: list[:class:`huaweicloudsdkgaussdbforopengauss.v3.MetricNameResult`]
        """
        
        super(ShowMetricNamesResponse, self).__init__()

        self._group_name = None
        self._metric_names = None
        self.discriminator = None

        if group_name is not None:
            self.group_name = group_name
        if metric_names is not None:
            self.metric_names = metric_names

    @property
    def group_name(self):
        r"""Gets the group_name of this ShowMetricNamesResponse.

        **参数解释**: 指标组名。 **取值范围**: 不涉及。

        :return: The group_name of this ShowMetricNamesResponse.
        :rtype: str
        """
        return self._group_name

    @group_name.setter
    def group_name(self, group_name):
        r"""Sets the group_name of this ShowMetricNamesResponse.

        **参数解释**: 指标组名。 **取值范围**: 不涉及。

        :param group_name: The group_name of this ShowMetricNamesResponse.
        :type group_name: str
        """
        self._group_name = group_name

    @property
    def metric_names(self):
        r"""Gets the metric_names of this ShowMetricNamesResponse.

        **参数解释**: 指标分组名称信息。

        :return: The metric_names of this ShowMetricNamesResponse.
        :rtype: list[:class:`huaweicloudsdkgaussdbforopengauss.v3.MetricNameResult`]
        """
        return self._metric_names

    @metric_names.setter
    def metric_names(self, metric_names):
        r"""Sets the metric_names of this ShowMetricNamesResponse.

        **参数解释**: 指标分组名称信息。

        :param metric_names: The metric_names of this ShowMetricNamesResponse.
        :type metric_names: list[:class:`huaweicloudsdkgaussdbforopengauss.v3.MetricNameResult`]
        """
        self._metric_names = metric_names

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
        if not isinstance(other, ShowMetricNamesResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

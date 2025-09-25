# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowInstanceMetricDataResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'instance_id': 'str',
        'metrics': 'list[MetricDataResult]'
    }

    attribute_map = {
        'instance_id': 'instance_id',
        'metrics': 'metrics'
    }

    def __init__(self, instance_id=None, metrics=None):
        r"""ShowInstanceMetricDataResponse

        The model defined in huaweicloud sdk

        :param instance_id: **参数解释**: 实例ID。 **取值范围**: 只能由英文字母、数字组成，且长度为36个字符。
        :type instance_id: str
        :param metrics: **参数解释**: 指标数据集合。
        :type metrics: list[:class:`huaweicloudsdkgaussdbforopengauss.v3.MetricDataResult`]
        """
        
        super(ShowInstanceMetricDataResponse, self).__init__()

        self._instance_id = None
        self._metrics = None
        self.discriminator = None

        if instance_id is not None:
            self.instance_id = instance_id
        if metrics is not None:
            self.metrics = metrics

    @property
    def instance_id(self):
        r"""Gets the instance_id of this ShowInstanceMetricDataResponse.

        **参数解释**: 实例ID。 **取值范围**: 只能由英文字母、数字组成，且长度为36个字符。

        :return: The instance_id of this ShowInstanceMetricDataResponse.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        r"""Sets the instance_id of this ShowInstanceMetricDataResponse.

        **参数解释**: 实例ID。 **取值范围**: 只能由英文字母、数字组成，且长度为36个字符。

        :param instance_id: The instance_id of this ShowInstanceMetricDataResponse.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def metrics(self):
        r"""Gets the metrics of this ShowInstanceMetricDataResponse.

        **参数解释**: 指标数据集合。

        :return: The metrics of this ShowInstanceMetricDataResponse.
        :rtype: list[:class:`huaweicloudsdkgaussdbforopengauss.v3.MetricDataResult`]
        """
        return self._metrics

    @metrics.setter
    def metrics(self, metrics):
        r"""Sets the metrics of this ShowInstanceMetricDataResponse.

        **参数解释**: 指标数据集合。

        :param metrics: The metrics of this ShowInstanceMetricDataResponse.
        :type metrics: list[:class:`huaweicloudsdkgaussdbforopengauss.v3.MetricDataResult`]
        """
        self._metrics = metrics

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
        if not isinstance(other, ShowInstanceMetricDataResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowGrowthRateRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'grow_period': 'str',
        'metric_name': 'str',
        'dim': 'str'
    }

    attribute_map = {
        'grow_period': 'grow_period',
        'metric_name': 'metric_name',
        'dim': 'dim'
    }

    def __init__(self, grow_period=None, metric_name=None, dim=None):
        r"""ShowGrowthRateRequest

        The model defined in huaweicloud sdk

        :param grow_period: 环比周期 | DAY - 天 MONTH - 月。
        :type grow_period: str
        :param metric_name: 指标名称。
        :type metric_name: str
        :param dim: 指标维度 | 目前最大支持3个维度，必须从0开始；维度格式为dim.{i}&#x3D;key,value，key的最大长度32，value的最大长度为256。 单维度：dim.0&#x3D;instance_id,6f3c6f91-4b24-4e1b-b7d1-a94ac1cb011d 多维度：dim.0&#x3D;key,value&amp;dim.1&#x3D;key,value。
        :type dim: str
        """
        
        

        self._grow_period = None
        self._metric_name = None
        self._dim = None
        self.discriminator = None

        if grow_period is not None:
            self.grow_period = grow_period
        self.metric_name = metric_name
        if dim is not None:
            self.dim = dim

    @property
    def grow_period(self):
        r"""Gets the grow_period of this ShowGrowthRateRequest.

        环比周期 | DAY - 天 MONTH - 月。

        :return: The grow_period of this ShowGrowthRateRequest.
        :rtype: str
        """
        return self._grow_period

    @grow_period.setter
    def grow_period(self, grow_period):
        r"""Sets the grow_period of this ShowGrowthRateRequest.

        环比周期 | DAY - 天 MONTH - 月。

        :param grow_period: The grow_period of this ShowGrowthRateRequest.
        :type grow_period: str
        """
        self._grow_period = grow_period

    @property
    def metric_name(self):
        r"""Gets the metric_name of this ShowGrowthRateRequest.

        指标名称。

        :return: The metric_name of this ShowGrowthRateRequest.
        :rtype: str
        """
        return self._metric_name

    @metric_name.setter
    def metric_name(self, metric_name):
        r"""Sets the metric_name of this ShowGrowthRateRequest.

        指标名称。

        :param metric_name: The metric_name of this ShowGrowthRateRequest.
        :type metric_name: str
        """
        self._metric_name = metric_name

    @property
    def dim(self):
        r"""Gets the dim of this ShowGrowthRateRequest.

        指标维度 | 目前最大支持3个维度，必须从0开始；维度格式为dim.{i}=key,value，key的最大长度32，value的最大长度为256。 单维度：dim.0=instance_id,6f3c6f91-4b24-4e1b-b7d1-a94ac1cb011d 多维度：dim.0=key,value&dim.1=key,value。

        :return: The dim of this ShowGrowthRateRequest.
        :rtype: str
        """
        return self._dim

    @dim.setter
    def dim(self, dim):
        r"""Sets the dim of this ShowGrowthRateRequest.

        指标维度 | 目前最大支持3个维度，必须从0开始；维度格式为dim.{i}=key,value，key的最大长度32，value的最大长度为256。 单维度：dim.0=instance_id,6f3c6f91-4b24-4e1b-b7d1-a94ac1cb011d 多维度：dim.0=key,value&dim.1=key,value。

        :param dim: The dim of this ShowGrowthRateRequest.
        :type dim: str
        """
        self._dim = dim

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
        if not isinstance(other, ShowGrowthRateRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

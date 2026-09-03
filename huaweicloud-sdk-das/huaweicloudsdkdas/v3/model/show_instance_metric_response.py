# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowInstanceMetricResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'das_metric_infos': 'list[DasMetricInfo]'
    }

    attribute_map = {
        'das_metric_infos': 'das_metric_infos'
    }

    def __init__(self, das_metric_infos=None):
        r"""ShowInstanceMetricResponse

        The model defined in huaweicloud sdk

        :param das_metric_infos: 实例指标信息列表
        :type das_metric_infos: list[:class:`huaweicloudsdkdas.v3.DasMetricInfo`]
        """
        
        super().__init__()

        self._das_metric_infos = None
        self.discriminator = None

        if das_metric_infos is not None:
            self.das_metric_infos = das_metric_infos

    @property
    def das_metric_infos(self):
        r"""Gets the das_metric_infos of this ShowInstanceMetricResponse.

        实例指标信息列表

        :return: The das_metric_infos of this ShowInstanceMetricResponse.
        :rtype: list[:class:`huaweicloudsdkdas.v3.DasMetricInfo`]
        """
        return self._das_metric_infos

    @das_metric_infos.setter
    def das_metric_infos(self, das_metric_infos):
        r"""Sets the das_metric_infos of this ShowInstanceMetricResponse.

        实例指标信息列表

        :param das_metric_infos: The das_metric_infos of this ShowInstanceMetricResponse.
        :type das_metric_infos: list[:class:`huaweicloudsdkdas.v3.DasMetricInfo`]
        """
        self._das_metric_infos = das_metric_infos

    def to_dict(self):
        import warnings
        warnings.warn("ShowInstanceMetricResponse.to_dict() is deprecated and no longer maintained, "
                      "use to_json_object() to get the response content.", DeprecationWarning)
        result = {}

        for attr, _ in self.openapi_types.items():
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
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ShowInstanceMetricResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

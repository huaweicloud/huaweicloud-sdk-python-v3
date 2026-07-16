# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowOpsAgentMetricGaugeResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'original_value': 'str',
        'day_compare_data': 'str'
    }

    attribute_map = {
        'original_value': 'original_value',
        'day_compare_data': 'day_compare_data'
    }

    def __init__(self, original_value=None, day_compare_data=None):
        r"""ShowOpsAgentMetricGaugeResponse

        The model defined in huaweicloud sdk

        :param original_value: 当前区间的值
        :type original_value: str
        :param day_compare_data: 日环比、今日新增
        :type day_compare_data: str
        """
        
        super().__init__()

        self._original_value = None
        self._day_compare_data = None
        self.discriminator = None

        if original_value is not None:
            self.original_value = original_value
        if day_compare_data is not None:
            self.day_compare_data = day_compare_data

    @property
    def original_value(self):
        r"""Gets the original_value of this ShowOpsAgentMetricGaugeResponse.

        当前区间的值

        :return: The original_value of this ShowOpsAgentMetricGaugeResponse.
        :rtype: str
        """
        return self._original_value

    @original_value.setter
    def original_value(self, original_value):
        r"""Sets the original_value of this ShowOpsAgentMetricGaugeResponse.

        当前区间的值

        :param original_value: The original_value of this ShowOpsAgentMetricGaugeResponse.
        :type original_value: str
        """
        self._original_value = original_value

    @property
    def day_compare_data(self):
        r"""Gets the day_compare_data of this ShowOpsAgentMetricGaugeResponse.

        日环比、今日新增

        :return: The day_compare_data of this ShowOpsAgentMetricGaugeResponse.
        :rtype: str
        """
        return self._day_compare_data

    @day_compare_data.setter
    def day_compare_data(self, day_compare_data):
        r"""Sets the day_compare_data of this ShowOpsAgentMetricGaugeResponse.

        日环比、今日新增

        :param day_compare_data: The day_compare_data of this ShowOpsAgentMetricGaugeResponse.
        :type day_compare_data: str
        """
        self._day_compare_data = day_compare_data

    def to_dict(self):
        import warnings
        warnings.warn("ShowOpsAgentMetricGaugeResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, ShowOpsAgentMetricGaugeResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

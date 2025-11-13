# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowDrugJobStatisticsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'quantity_statistics': 'list[QuantityStatistics]',
        'usage_statistics': 'list[UsageStatistics]'
    }

    attribute_map = {
        'quantity_statistics': 'quantity_statistics',
        'usage_statistics': 'usage_statistics'
    }

    def __init__(self, quantity_statistics=None, usage_statistics=None):
        r"""ShowDrugJobStatisticsResponse

        The model defined in huaweicloud sdk

        :param quantity_statistics: **参数解释**： 药物设计作业数量统计结果。 **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及 
        :type quantity_statistics: list[:class:`huaweicloudsdkeihealth.v2.QuantityStatistics`]
        :param usage_statistics: **参数解释**： 药物设计作业使用量统计结果。 **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及 
        :type usage_statistics: list[:class:`huaweicloudsdkeihealth.v2.UsageStatistics`]
        """
        
        super().__init__()

        self._quantity_statistics = None
        self._usage_statistics = None
        self.discriminator = None

        if quantity_statistics is not None:
            self.quantity_statistics = quantity_statistics
        if usage_statistics is not None:
            self.usage_statistics = usage_statistics

    @property
    def quantity_statistics(self):
        r"""Gets the quantity_statistics of this ShowDrugJobStatisticsResponse.

        **参数解释**： 药物设计作业数量统计结果。 **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及 

        :return: The quantity_statistics of this ShowDrugJobStatisticsResponse.
        :rtype: list[:class:`huaweicloudsdkeihealth.v2.QuantityStatistics`]
        """
        return self._quantity_statistics

    @quantity_statistics.setter
    def quantity_statistics(self, quantity_statistics):
        r"""Sets the quantity_statistics of this ShowDrugJobStatisticsResponse.

        **参数解释**： 药物设计作业数量统计结果。 **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及 

        :param quantity_statistics: The quantity_statistics of this ShowDrugJobStatisticsResponse.
        :type quantity_statistics: list[:class:`huaweicloudsdkeihealth.v2.QuantityStatistics`]
        """
        self._quantity_statistics = quantity_statistics

    @property
    def usage_statistics(self):
        r"""Gets the usage_statistics of this ShowDrugJobStatisticsResponse.

        **参数解释**： 药物设计作业使用量统计结果。 **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及 

        :return: The usage_statistics of this ShowDrugJobStatisticsResponse.
        :rtype: list[:class:`huaweicloudsdkeihealth.v2.UsageStatistics`]
        """
        return self._usage_statistics

    @usage_statistics.setter
    def usage_statistics(self, usage_statistics):
        r"""Sets the usage_statistics of this ShowDrugJobStatisticsResponse.

        **参数解释**： 药物设计作业使用量统计结果。 **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及 

        :param usage_statistics: The usage_statistics of this ShowDrugJobStatisticsResponse.
        :type usage_statistics: list[:class:`huaweicloudsdkeihealth.v2.UsageStatistics`]
        """
        self._usage_statistics = usage_statistics

    def to_dict(self):
        import warnings
        warnings.warn("ShowDrugJobStatisticsResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, ShowDrugJobStatisticsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowPoolStatisticsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'statistics': 'PoolStatisticsStatistics',
        'operation_time': 'str'
    }

    attribute_map = {
        'statistics': 'statistics',
        'operation_time': 'operationTime'
    }

    def __init__(self, statistics=None, operation_time=None):
        r"""ShowPoolStatisticsResponse

        The model defined in huaweicloud sdk

        :param statistics: 
        :type statistics: :class:`huaweicloudsdkmodelarts.v1.PoolStatisticsStatistics`
        :param operation_time: **参数描述**： 统计的时间。 **取值范围**： 不涉及。
        :type operation_time: str
        """
        
        super().__init__()

        self._statistics = None
        self._operation_time = None
        self.discriminator = None

        if statistics is not None:
            self.statistics = statistics
        if operation_time is not None:
            self.operation_time = operation_time

    @property
    def statistics(self):
        r"""Gets the statistics of this ShowPoolStatisticsResponse.

        :return: The statistics of this ShowPoolStatisticsResponse.
        :rtype: :class:`huaweicloudsdkmodelarts.v1.PoolStatisticsStatistics`
        """
        return self._statistics

    @statistics.setter
    def statistics(self, statistics):
        r"""Sets the statistics of this ShowPoolStatisticsResponse.

        :param statistics: The statistics of this ShowPoolStatisticsResponse.
        :type statistics: :class:`huaweicloudsdkmodelarts.v1.PoolStatisticsStatistics`
        """
        self._statistics = statistics

    @property
    def operation_time(self):
        r"""Gets the operation_time of this ShowPoolStatisticsResponse.

        **参数描述**： 统计的时间。 **取值范围**： 不涉及。

        :return: The operation_time of this ShowPoolStatisticsResponse.
        :rtype: str
        """
        return self._operation_time

    @operation_time.setter
    def operation_time(self, operation_time):
        r"""Sets the operation_time of this ShowPoolStatisticsResponse.

        **参数描述**： 统计的时间。 **取值范围**： 不涉及。

        :param operation_time: The operation_time of this ShowPoolStatisticsResponse.
        :type operation_time: str
        """
        self._operation_time = operation_time

    def to_dict(self):
        import warnings
        warnings.warn("ShowPoolStatisticsResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, ShowPoolStatisticsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

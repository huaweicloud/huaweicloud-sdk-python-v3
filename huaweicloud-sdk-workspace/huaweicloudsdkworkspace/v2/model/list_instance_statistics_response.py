# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListInstanceStatisticsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'total_count': 'int',
        'unconfigured_model_count': 'int',
        'unconfigured_channel_count': 'int',
        'risk_count': 'int'
    }

    attribute_map = {
        'total_count': 'total_count',
        'unconfigured_model_count': 'unconfigured_model_count',
        'unconfigured_channel_count': 'unconfigured_channel_count',
        'risk_count': 'risk_count'
    }

    def __init__(self, total_count=None, unconfigured_model_count=None, unconfigured_channel_count=None, risk_count=None):
        r"""ListInstanceStatisticsResponse

        The model defined in huaweicloud sdk

        :param total_count: 桌面总数
        :type total_count: int
        :param unconfigured_model_count: 未配置模型桌面数
        :type unconfigured_model_count: int
        :param unconfigured_channel_count: 未配置通道桌面数
        :type unconfigured_channel_count: int
        :param risk_count: 存在风险桌面数
        :type risk_count: int
        """
        
        super().__init__()

        self._total_count = None
        self._unconfigured_model_count = None
        self._unconfigured_channel_count = None
        self._risk_count = None
        self.discriminator = None

        if total_count is not None:
            self.total_count = total_count
        if unconfigured_model_count is not None:
            self.unconfigured_model_count = unconfigured_model_count
        if unconfigured_channel_count is not None:
            self.unconfigured_channel_count = unconfigured_channel_count
        if risk_count is not None:
            self.risk_count = risk_count

    @property
    def total_count(self):
        r"""Gets the total_count of this ListInstanceStatisticsResponse.

        桌面总数

        :return: The total_count of this ListInstanceStatisticsResponse.
        :rtype: int
        """
        return self._total_count

    @total_count.setter
    def total_count(self, total_count):
        r"""Sets the total_count of this ListInstanceStatisticsResponse.

        桌面总数

        :param total_count: The total_count of this ListInstanceStatisticsResponse.
        :type total_count: int
        """
        self._total_count = total_count

    @property
    def unconfigured_model_count(self):
        r"""Gets the unconfigured_model_count of this ListInstanceStatisticsResponse.

        未配置模型桌面数

        :return: The unconfigured_model_count of this ListInstanceStatisticsResponse.
        :rtype: int
        """
        return self._unconfigured_model_count

    @unconfigured_model_count.setter
    def unconfigured_model_count(self, unconfigured_model_count):
        r"""Sets the unconfigured_model_count of this ListInstanceStatisticsResponse.

        未配置模型桌面数

        :param unconfigured_model_count: The unconfigured_model_count of this ListInstanceStatisticsResponse.
        :type unconfigured_model_count: int
        """
        self._unconfigured_model_count = unconfigured_model_count

    @property
    def unconfigured_channel_count(self):
        r"""Gets the unconfigured_channel_count of this ListInstanceStatisticsResponse.

        未配置通道桌面数

        :return: The unconfigured_channel_count of this ListInstanceStatisticsResponse.
        :rtype: int
        """
        return self._unconfigured_channel_count

    @unconfigured_channel_count.setter
    def unconfigured_channel_count(self, unconfigured_channel_count):
        r"""Sets the unconfigured_channel_count of this ListInstanceStatisticsResponse.

        未配置通道桌面数

        :param unconfigured_channel_count: The unconfigured_channel_count of this ListInstanceStatisticsResponse.
        :type unconfigured_channel_count: int
        """
        self._unconfigured_channel_count = unconfigured_channel_count

    @property
    def risk_count(self):
        r"""Gets the risk_count of this ListInstanceStatisticsResponse.

        存在风险桌面数

        :return: The risk_count of this ListInstanceStatisticsResponse.
        :rtype: int
        """
        return self._risk_count

    @risk_count.setter
    def risk_count(self, risk_count):
        r"""Sets the risk_count of this ListInstanceStatisticsResponse.

        存在风险桌面数

        :param risk_count: The risk_count of this ListInstanceStatisticsResponse.
        :type risk_count: int
        """
        self._risk_count = risk_count

    def to_dict(self):
        import warnings
        warnings.warn("ListInstanceStatisticsResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, ListInstanceStatisticsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

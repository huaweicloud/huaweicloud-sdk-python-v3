# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowQuotaHostStatisticsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'host_total_num': 'int',
        'data_list': 'list[QuotaHostStatistics]'
    }

    attribute_map = {
        'host_total_num': 'host_total_num',
        'data_list': 'data_list'
    }

    def __init__(self, host_total_num=None, data_list=None):
        r"""ShowQuotaHostStatisticsResponse

        The model defined in huaweicloud sdk

        :param host_total_num: **参数解释**: 主机总数量 **取值范围**: 最小值0，最大值2147483647 
        :type host_total_num: int
        :param data_list: **参数解释**: 配额信息列表，包含各版本的配额统计 **取值范围**: 0-200个QuotaHostStatistics对象 
        :type data_list: list[:class:`huaweicloudsdkhss.v5.QuotaHostStatistics`]
        """
        
        super().__init__()

        self._host_total_num = None
        self._data_list = None
        self.discriminator = None

        if host_total_num is not None:
            self.host_total_num = host_total_num
        if data_list is not None:
            self.data_list = data_list

    @property
    def host_total_num(self):
        r"""Gets the host_total_num of this ShowQuotaHostStatisticsResponse.

        **参数解释**: 主机总数量 **取值范围**: 最小值0，最大值2147483647 

        :return: The host_total_num of this ShowQuotaHostStatisticsResponse.
        :rtype: int
        """
        return self._host_total_num

    @host_total_num.setter
    def host_total_num(self, host_total_num):
        r"""Sets the host_total_num of this ShowQuotaHostStatisticsResponse.

        **参数解释**: 主机总数量 **取值范围**: 最小值0，最大值2147483647 

        :param host_total_num: The host_total_num of this ShowQuotaHostStatisticsResponse.
        :type host_total_num: int
        """
        self._host_total_num = host_total_num

    @property
    def data_list(self):
        r"""Gets the data_list of this ShowQuotaHostStatisticsResponse.

        **参数解释**: 配额信息列表，包含各版本的配额统计 **取值范围**: 0-200个QuotaHostStatistics对象 

        :return: The data_list of this ShowQuotaHostStatisticsResponse.
        :rtype: list[:class:`huaweicloudsdkhss.v5.QuotaHostStatistics`]
        """
        return self._data_list

    @data_list.setter
    def data_list(self, data_list):
        r"""Sets the data_list of this ShowQuotaHostStatisticsResponse.

        **参数解释**: 配额信息列表，包含各版本的配额统计 **取值范围**: 0-200个QuotaHostStatistics对象 

        :param data_list: The data_list of this ShowQuotaHostStatisticsResponse.
        :type data_list: list[:class:`huaweicloudsdkhss.v5.QuotaHostStatistics`]
        """
        self._data_list = data_list

    def to_dict(self):
        import warnings
        warnings.warn("ShowQuotaHostStatisticsResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, ShowQuotaHostStatisticsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowSecurityRiskResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'host_risk_info': 'HostRiskInfo',
        'container_risk_info': 'ContainerRiskInfo',
        'trend_data_list': 'list[TrendRiskInfo]'
    }

    attribute_map = {
        'host_risk_info': 'host_risk_info',
        'container_risk_info': 'container_risk_info',
        'trend_data_list': 'trend_data_list'
    }

    def __init__(self, host_risk_info=None, container_risk_info=None, trend_data_list=None):
        r"""ShowSecurityRiskResponse

        The model defined in huaweicloud sdk

        :param host_risk_info: 
        :type host_risk_info: :class:`huaweicloudsdkhss.v5.HostRiskInfo`
        :param container_risk_info: 
        :type container_risk_info: :class:`huaweicloudsdkhss.v5.ContainerRiskInfo`
        :param trend_data_list: **参数解释**: 安全风险趋势 **取值范围**: 取值0-30个TrendRiskInfo对象 
        :type trend_data_list: list[:class:`huaweicloudsdkhss.v5.TrendRiskInfo`]
        """
        
        super().__init__()

        self._host_risk_info = None
        self._container_risk_info = None
        self._trend_data_list = None
        self.discriminator = None

        if host_risk_info is not None:
            self.host_risk_info = host_risk_info
        if container_risk_info is not None:
            self.container_risk_info = container_risk_info
        if trend_data_list is not None:
            self.trend_data_list = trend_data_list

    @property
    def host_risk_info(self):
        r"""Gets the host_risk_info of this ShowSecurityRiskResponse.

        :return: The host_risk_info of this ShowSecurityRiskResponse.
        :rtype: :class:`huaweicloudsdkhss.v5.HostRiskInfo`
        """
        return self._host_risk_info

    @host_risk_info.setter
    def host_risk_info(self, host_risk_info):
        r"""Sets the host_risk_info of this ShowSecurityRiskResponse.

        :param host_risk_info: The host_risk_info of this ShowSecurityRiskResponse.
        :type host_risk_info: :class:`huaweicloudsdkhss.v5.HostRiskInfo`
        """
        self._host_risk_info = host_risk_info

    @property
    def container_risk_info(self):
        r"""Gets the container_risk_info of this ShowSecurityRiskResponse.

        :return: The container_risk_info of this ShowSecurityRiskResponse.
        :rtype: :class:`huaweicloudsdkhss.v5.ContainerRiskInfo`
        """
        return self._container_risk_info

    @container_risk_info.setter
    def container_risk_info(self, container_risk_info):
        r"""Sets the container_risk_info of this ShowSecurityRiskResponse.

        :param container_risk_info: The container_risk_info of this ShowSecurityRiskResponse.
        :type container_risk_info: :class:`huaweicloudsdkhss.v5.ContainerRiskInfo`
        """
        self._container_risk_info = container_risk_info

    @property
    def trend_data_list(self):
        r"""Gets the trend_data_list of this ShowSecurityRiskResponse.

        **参数解释**: 安全风险趋势 **取值范围**: 取值0-30个TrendRiskInfo对象 

        :return: The trend_data_list of this ShowSecurityRiskResponse.
        :rtype: list[:class:`huaweicloudsdkhss.v5.TrendRiskInfo`]
        """
        return self._trend_data_list

    @trend_data_list.setter
    def trend_data_list(self, trend_data_list):
        r"""Sets the trend_data_list of this ShowSecurityRiskResponse.

        **参数解释**: 安全风险趋势 **取值范围**: 取值0-30个TrendRiskInfo对象 

        :param trend_data_list: The trend_data_list of this ShowSecurityRiskResponse.
        :type trend_data_list: list[:class:`huaweicloudsdkhss.v5.TrendRiskInfo`]
        """
        self._trend_data_list = trend_data_list

    def to_dict(self):
        import warnings
        warnings.warn("ShowSecurityRiskResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, ShowSecurityRiskResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowProtectionStatusStatisticsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'vul_scan_time': 'int',
        'av_upgrade_time': 'int',
        'protection_enabled_list': 'list[ProtectionEnabledTypes]',
        'data_list': 'list[ProtectStatusStatistics]'
    }

    attribute_map = {
        'vul_scan_time': 'vul_scan_time',
        'av_upgrade_time': 'av_upgrade_time',
        'protection_enabled_list': 'protection_enabled_list',
        'data_list': 'data_list'
    }

    def __init__(self, vul_scan_time=None, av_upgrade_time=None, protection_enabled_list=None, data_list=None):
        r"""ShowProtectionStatusStatisticsResponse

        The model defined in huaweicloud sdk

        :param vul_scan_time: **参数解释**: 漏洞扫描时间，Unix时间戳格式，单位为毫秒 **取值范围**: 最小值0，最大值9223372036854775807 
        :type vul_scan_time: int
        :param av_upgrade_time: **参数解释**: 病毒库更新时间，Unix时间戳格式，单位为毫秒 **取值范围**: 最小值0，最大值9223372036854775807 
        :type av_upgrade_time: int
        :param protection_enabled_list: **参数解释**: 已开启防护的类型列表 **取值范围**: 0-200个ProtectionEnabledTypes对象 
        :type protection_enabled_list: list[:class:`huaweicloudsdkhss.v5.ProtectionEnabledTypes`]
        :param data_list: **参数解释**: 防护状态统计列表 **取值范围**: 0-200个ProtectStatusStatistics对象 
        :type data_list: list[:class:`huaweicloudsdkhss.v5.ProtectStatusStatistics`]
        """
        
        super().__init__()

        self._vul_scan_time = None
        self._av_upgrade_time = None
        self._protection_enabled_list = None
        self._data_list = None
        self.discriminator = None

        if vul_scan_time is not None:
            self.vul_scan_time = vul_scan_time
        if av_upgrade_time is not None:
            self.av_upgrade_time = av_upgrade_time
        if protection_enabled_list is not None:
            self.protection_enabled_list = protection_enabled_list
        if data_list is not None:
            self.data_list = data_list

    @property
    def vul_scan_time(self):
        r"""Gets the vul_scan_time of this ShowProtectionStatusStatisticsResponse.

        **参数解释**: 漏洞扫描时间，Unix时间戳格式，单位为毫秒 **取值范围**: 最小值0，最大值9223372036854775807 

        :return: The vul_scan_time of this ShowProtectionStatusStatisticsResponse.
        :rtype: int
        """
        return self._vul_scan_time

    @vul_scan_time.setter
    def vul_scan_time(self, vul_scan_time):
        r"""Sets the vul_scan_time of this ShowProtectionStatusStatisticsResponse.

        **参数解释**: 漏洞扫描时间，Unix时间戳格式，单位为毫秒 **取值范围**: 最小值0，最大值9223372036854775807 

        :param vul_scan_time: The vul_scan_time of this ShowProtectionStatusStatisticsResponse.
        :type vul_scan_time: int
        """
        self._vul_scan_time = vul_scan_time

    @property
    def av_upgrade_time(self):
        r"""Gets the av_upgrade_time of this ShowProtectionStatusStatisticsResponse.

        **参数解释**: 病毒库更新时间，Unix时间戳格式，单位为毫秒 **取值范围**: 最小值0，最大值9223372036854775807 

        :return: The av_upgrade_time of this ShowProtectionStatusStatisticsResponse.
        :rtype: int
        """
        return self._av_upgrade_time

    @av_upgrade_time.setter
    def av_upgrade_time(self, av_upgrade_time):
        r"""Sets the av_upgrade_time of this ShowProtectionStatusStatisticsResponse.

        **参数解释**: 病毒库更新时间，Unix时间戳格式，单位为毫秒 **取值范围**: 最小值0，最大值9223372036854775807 

        :param av_upgrade_time: The av_upgrade_time of this ShowProtectionStatusStatisticsResponse.
        :type av_upgrade_time: int
        """
        self._av_upgrade_time = av_upgrade_time

    @property
    def protection_enabled_list(self):
        r"""Gets the protection_enabled_list of this ShowProtectionStatusStatisticsResponse.

        **参数解释**: 已开启防护的类型列表 **取值范围**: 0-200个ProtectionEnabledTypes对象 

        :return: The protection_enabled_list of this ShowProtectionStatusStatisticsResponse.
        :rtype: list[:class:`huaweicloudsdkhss.v5.ProtectionEnabledTypes`]
        """
        return self._protection_enabled_list

    @protection_enabled_list.setter
    def protection_enabled_list(self, protection_enabled_list):
        r"""Sets the protection_enabled_list of this ShowProtectionStatusStatisticsResponse.

        **参数解释**: 已开启防护的类型列表 **取值范围**: 0-200个ProtectionEnabledTypes对象 

        :param protection_enabled_list: The protection_enabled_list of this ShowProtectionStatusStatisticsResponse.
        :type protection_enabled_list: list[:class:`huaweicloudsdkhss.v5.ProtectionEnabledTypes`]
        """
        self._protection_enabled_list = protection_enabled_list

    @property
    def data_list(self):
        r"""Gets the data_list of this ShowProtectionStatusStatisticsResponse.

        **参数解释**: 防护状态统计列表 **取值范围**: 0-200个ProtectStatusStatistics对象 

        :return: The data_list of this ShowProtectionStatusStatisticsResponse.
        :rtype: list[:class:`huaweicloudsdkhss.v5.ProtectStatusStatistics`]
        """
        return self._data_list

    @data_list.setter
    def data_list(self, data_list):
        r"""Sets the data_list of this ShowProtectionStatusStatisticsResponse.

        **参数解释**: 防护状态统计列表 **取值范围**: 0-200个ProtectStatusStatistics对象 

        :param data_list: The data_list of this ShowProtectionStatusStatisticsResponse.
        :type data_list: list[:class:`huaweicloudsdkhss.v5.ProtectStatusStatistics`]
        """
        self._data_list = data_list

    def to_dict(self):
        import warnings
        warnings.warn("ShowProtectionStatusStatisticsResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, ShowProtectionStatusStatisticsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

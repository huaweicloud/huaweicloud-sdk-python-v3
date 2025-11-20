# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowVulScanTaskEstimatedTimeRequestInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'manual_scan_type': 'list[str]',
        'range_type': 'str',
        'agent_ids': 'list[str]'
    }

    attribute_map = {
        'manual_scan_type': 'manual_scan_type',
        'range_type': 'range_type',
        'agent_ids': 'agent_ids'
    }

    def __init__(self, manual_scan_type=None, range_type=None, agent_ids=None):
        r"""ShowVulScanTaskEstimatedTimeRequestInfo

        The model defined in huaweicloud sdk

        :param manual_scan_type: **参数解释**: 漏洞手动检测类型 **约束限制**: 不涉及 **取值范围**: - linux_vul：linux漏洞 - windows_vul：windows漏洞 - web_cms：Web-CMS漏洞 - app_vul：应用漏洞 - urgent_vul：紧急漏洞  **默认取值**: 不涉及 
        :type manual_scan_type: list[str]
        :param range_type: **参数解释**: 检测的主机范围 **约束限制**: 不涉及 **取值范围**: - all_host：全部主机 - specific_host：部分主机  **默认取值**: 不涉及 
        :type range_type: str
        :param agent_ids: **参数解释**: 待检测的agent列表 **约束限制**: 不涉及 **取值范围**: 字符长度0-256位 **默认取值**: 不涉及 
        :type agent_ids: list[str]
        """
        
        

        self._manual_scan_type = None
        self._range_type = None
        self._agent_ids = None
        self.discriminator = None

        if manual_scan_type is not None:
            self.manual_scan_type = manual_scan_type
        if range_type is not None:
            self.range_type = range_type
        if agent_ids is not None:
            self.agent_ids = agent_ids

    @property
    def manual_scan_type(self):
        r"""Gets the manual_scan_type of this ShowVulScanTaskEstimatedTimeRequestInfo.

        **参数解释**: 漏洞手动检测类型 **约束限制**: 不涉及 **取值范围**: - linux_vul：linux漏洞 - windows_vul：windows漏洞 - web_cms：Web-CMS漏洞 - app_vul：应用漏洞 - urgent_vul：紧急漏洞  **默认取值**: 不涉及 

        :return: The manual_scan_type of this ShowVulScanTaskEstimatedTimeRequestInfo.
        :rtype: list[str]
        """
        return self._manual_scan_type

    @manual_scan_type.setter
    def manual_scan_type(self, manual_scan_type):
        r"""Sets the manual_scan_type of this ShowVulScanTaskEstimatedTimeRequestInfo.

        **参数解释**: 漏洞手动检测类型 **约束限制**: 不涉及 **取值范围**: - linux_vul：linux漏洞 - windows_vul：windows漏洞 - web_cms：Web-CMS漏洞 - app_vul：应用漏洞 - urgent_vul：紧急漏洞  **默认取值**: 不涉及 

        :param manual_scan_type: The manual_scan_type of this ShowVulScanTaskEstimatedTimeRequestInfo.
        :type manual_scan_type: list[str]
        """
        self._manual_scan_type = manual_scan_type

    @property
    def range_type(self):
        r"""Gets the range_type of this ShowVulScanTaskEstimatedTimeRequestInfo.

        **参数解释**: 检测的主机范围 **约束限制**: 不涉及 **取值范围**: - all_host：全部主机 - specific_host：部分主机  **默认取值**: 不涉及 

        :return: The range_type of this ShowVulScanTaskEstimatedTimeRequestInfo.
        :rtype: str
        """
        return self._range_type

    @range_type.setter
    def range_type(self, range_type):
        r"""Sets the range_type of this ShowVulScanTaskEstimatedTimeRequestInfo.

        **参数解释**: 检测的主机范围 **约束限制**: 不涉及 **取值范围**: - all_host：全部主机 - specific_host：部分主机  **默认取值**: 不涉及 

        :param range_type: The range_type of this ShowVulScanTaskEstimatedTimeRequestInfo.
        :type range_type: str
        """
        self._range_type = range_type

    @property
    def agent_ids(self):
        r"""Gets the agent_ids of this ShowVulScanTaskEstimatedTimeRequestInfo.

        **参数解释**: 待检测的agent列表 **约束限制**: 不涉及 **取值范围**: 字符长度0-256位 **默认取值**: 不涉及 

        :return: The agent_ids of this ShowVulScanTaskEstimatedTimeRequestInfo.
        :rtype: list[str]
        """
        return self._agent_ids

    @agent_ids.setter
    def agent_ids(self, agent_ids):
        r"""Sets the agent_ids of this ShowVulScanTaskEstimatedTimeRequestInfo.

        **参数解释**: 待检测的agent列表 **约束限制**: 不涉及 **取值范围**: 字符长度0-256位 **默认取值**: 不涉及 

        :param agent_ids: The agent_ids of this ShowVulScanTaskEstimatedTimeRequestInfo.
        :type agent_ids: list[str]
        """
        self._agent_ids = agent_ids

    def to_dict(self):
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
        if not isinstance(other, ShowVulScanTaskEstimatedTimeRequestInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

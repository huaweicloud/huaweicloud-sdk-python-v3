# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class RescanVulScanTaskRequestInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'range_type': 'str',
        'host_ids': 'list[str]'
    }

    attribute_map = {
        'range_type': 'range_type',
        'host_ids': 'host_ids'
    }

    def __init__(self, range_type=None, host_ids=None):
        r"""RescanVulScanTaskRequestInfo

        The model defined in huaweicloud sdk

        :param range_type: **参数解释**: 重新扫描的主机范围 **约束限制**: 不涉及 **取值范围**: - all_failed_host：当前任务下所有扫描失败的主机 - specific_host：指定主机  **默认取值**: 不涉及 
        :type range_type: str
        :param host_ids: **参数解释**: 主机ID列表 **约束限制**: range_type值为“specific_host”时有效 **取值范围**: 最少1条，最多1000条  **默认取值**: 不涉及 
        :type host_ids: list[str]
        """
        
        

        self._range_type = None
        self._host_ids = None
        self.discriminator = None

        self.range_type = range_type
        if host_ids is not None:
            self.host_ids = host_ids

    @property
    def range_type(self):
        r"""Gets the range_type of this RescanVulScanTaskRequestInfo.

        **参数解释**: 重新扫描的主机范围 **约束限制**: 不涉及 **取值范围**: - all_failed_host：当前任务下所有扫描失败的主机 - specific_host：指定主机  **默认取值**: 不涉及 

        :return: The range_type of this RescanVulScanTaskRequestInfo.
        :rtype: str
        """
        return self._range_type

    @range_type.setter
    def range_type(self, range_type):
        r"""Sets the range_type of this RescanVulScanTaskRequestInfo.

        **参数解释**: 重新扫描的主机范围 **约束限制**: 不涉及 **取值范围**: - all_failed_host：当前任务下所有扫描失败的主机 - specific_host：指定主机  **默认取值**: 不涉及 

        :param range_type: The range_type of this RescanVulScanTaskRequestInfo.
        :type range_type: str
        """
        self._range_type = range_type

    @property
    def host_ids(self):
        r"""Gets the host_ids of this RescanVulScanTaskRequestInfo.

        **参数解释**: 主机ID列表 **约束限制**: range_type值为“specific_host”时有效 **取值范围**: 最少1条，最多1000条  **默认取值**: 不涉及 

        :return: The host_ids of this RescanVulScanTaskRequestInfo.
        :rtype: list[str]
        """
        return self._host_ids

    @host_ids.setter
    def host_ids(self, host_ids):
        r"""Sets the host_ids of this RescanVulScanTaskRequestInfo.

        **参数解释**: 主机ID列表 **约束限制**: range_type值为“specific_host”时有效 **取值范围**: 最少1条，最多1000条  **默认取值**: 不涉及 

        :param host_ids: The host_ids of this RescanVulScanTaskRequestInfo.
        :type host_ids: list[str]
        """
        self._host_ids = host_ids

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
        if not isinstance(other, RescanVulScanTaskRequestInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

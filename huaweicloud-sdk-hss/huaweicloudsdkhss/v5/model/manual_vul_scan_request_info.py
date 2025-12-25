# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ManualVulScanRequestInfo:

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
        'batch_flag': 'bool',
        'range_type': 'str',
        'agent_id_list': 'list[str]',
        'urgent_vul_id_list': 'list[str]'
    }

    attribute_map = {
        'manual_scan_type': 'manual_scan_type',
        'batch_flag': 'batch_flag',
        'range_type': 'range_type',
        'agent_id_list': 'agent_id_list',
        'urgent_vul_id_list': 'urgent_vul_id_list'
    }

    def __init__(self, manual_scan_type=None, batch_flag=None, range_type=None, agent_id_list=None, urgent_vul_id_list=None):
        r"""ManualVulScanRequestInfo

        The model defined in huaweicloud sdk

        :param manual_scan_type: **参数解释**: 扫描的漏洞类型列表 **约束限制**: 不涉及 **取值范围**: 最小值1，最大值200 **默认取值**: 不涉及 
        :type manual_scan_type: list[str]
        :param batch_flag: **参数解释**: 是否为批量扫描操作 **约束限制**: 不涉及 **取值范围**:   - true：是批量扫描操作   - false：不是批量扫描操作  **默认取值**: 不涉及 
        :type batch_flag: bool
        :param range_type: **参数解释**: 扫描主机的范围 **约束限制**: 不涉及 **取值范围**:   - all_host：扫描全部主机，此类型不需要填写agent_id_list   - specific_host：扫描指定主机  **默认取值**: 不涉及 
        :type range_type: str
        :param agent_id_list: **参数解释**: 需要扫描主机的agent id列表 **约束限制**: range_type值为specific_host时有效 **取值范围**: 最小值1，最大值200 **默认取值**: 不涉及 
        :type agent_id_list: list[str]
        :param urgent_vul_id_list: **参数解释**: 扫描的应急漏洞id列表，该字段不传值则扫描所有应急漏洞 **约束限制**: manual_scan_type字段的值中包含“urgent_vul”时有效 **取值范围**: 最小值1，最大值200 **默认取值**: 不涉及 
        :type urgent_vul_id_list: list[str]
        """
        
        

        self._manual_scan_type = None
        self._batch_flag = None
        self._range_type = None
        self._agent_id_list = None
        self._urgent_vul_id_list = None
        self.discriminator = None

        if manual_scan_type is not None:
            self.manual_scan_type = manual_scan_type
        if batch_flag is not None:
            self.batch_flag = batch_flag
        if range_type is not None:
            self.range_type = range_type
        if agent_id_list is not None:
            self.agent_id_list = agent_id_list
        if urgent_vul_id_list is not None:
            self.urgent_vul_id_list = urgent_vul_id_list

    @property
    def manual_scan_type(self):
        r"""Gets the manual_scan_type of this ManualVulScanRequestInfo.

        **参数解释**: 扫描的漏洞类型列表 **约束限制**: 不涉及 **取值范围**: 最小值1，最大值200 **默认取值**: 不涉及 

        :return: The manual_scan_type of this ManualVulScanRequestInfo.
        :rtype: list[str]
        """
        return self._manual_scan_type

    @manual_scan_type.setter
    def manual_scan_type(self, manual_scan_type):
        r"""Sets the manual_scan_type of this ManualVulScanRequestInfo.

        **参数解释**: 扫描的漏洞类型列表 **约束限制**: 不涉及 **取值范围**: 最小值1，最大值200 **默认取值**: 不涉及 

        :param manual_scan_type: The manual_scan_type of this ManualVulScanRequestInfo.
        :type manual_scan_type: list[str]
        """
        self._manual_scan_type = manual_scan_type

    @property
    def batch_flag(self):
        r"""Gets the batch_flag of this ManualVulScanRequestInfo.

        **参数解释**: 是否为批量扫描操作 **约束限制**: 不涉及 **取值范围**:   - true：是批量扫描操作   - false：不是批量扫描操作  **默认取值**: 不涉及 

        :return: The batch_flag of this ManualVulScanRequestInfo.
        :rtype: bool
        """
        return self._batch_flag

    @batch_flag.setter
    def batch_flag(self, batch_flag):
        r"""Sets the batch_flag of this ManualVulScanRequestInfo.

        **参数解释**: 是否为批量扫描操作 **约束限制**: 不涉及 **取值范围**:   - true：是批量扫描操作   - false：不是批量扫描操作  **默认取值**: 不涉及 

        :param batch_flag: The batch_flag of this ManualVulScanRequestInfo.
        :type batch_flag: bool
        """
        self._batch_flag = batch_flag

    @property
    def range_type(self):
        r"""Gets the range_type of this ManualVulScanRequestInfo.

        **参数解释**: 扫描主机的范围 **约束限制**: 不涉及 **取值范围**:   - all_host：扫描全部主机，此类型不需要填写agent_id_list   - specific_host：扫描指定主机  **默认取值**: 不涉及 

        :return: The range_type of this ManualVulScanRequestInfo.
        :rtype: str
        """
        return self._range_type

    @range_type.setter
    def range_type(self, range_type):
        r"""Sets the range_type of this ManualVulScanRequestInfo.

        **参数解释**: 扫描主机的范围 **约束限制**: 不涉及 **取值范围**:   - all_host：扫描全部主机，此类型不需要填写agent_id_list   - specific_host：扫描指定主机  **默认取值**: 不涉及 

        :param range_type: The range_type of this ManualVulScanRequestInfo.
        :type range_type: str
        """
        self._range_type = range_type

    @property
    def agent_id_list(self):
        r"""Gets the agent_id_list of this ManualVulScanRequestInfo.

        **参数解释**: 需要扫描主机的agent id列表 **约束限制**: range_type值为specific_host时有效 **取值范围**: 最小值1，最大值200 **默认取值**: 不涉及 

        :return: The agent_id_list of this ManualVulScanRequestInfo.
        :rtype: list[str]
        """
        return self._agent_id_list

    @agent_id_list.setter
    def agent_id_list(self, agent_id_list):
        r"""Sets the agent_id_list of this ManualVulScanRequestInfo.

        **参数解释**: 需要扫描主机的agent id列表 **约束限制**: range_type值为specific_host时有效 **取值范围**: 最小值1，最大值200 **默认取值**: 不涉及 

        :param agent_id_list: The agent_id_list of this ManualVulScanRequestInfo.
        :type agent_id_list: list[str]
        """
        self._agent_id_list = agent_id_list

    @property
    def urgent_vul_id_list(self):
        r"""Gets the urgent_vul_id_list of this ManualVulScanRequestInfo.

        **参数解释**: 扫描的应急漏洞id列表，该字段不传值则扫描所有应急漏洞 **约束限制**: manual_scan_type字段的值中包含“urgent_vul”时有效 **取值范围**: 最小值1，最大值200 **默认取值**: 不涉及 

        :return: The urgent_vul_id_list of this ManualVulScanRequestInfo.
        :rtype: list[str]
        """
        return self._urgent_vul_id_list

    @urgent_vul_id_list.setter
    def urgent_vul_id_list(self, urgent_vul_id_list):
        r"""Sets the urgent_vul_id_list of this ManualVulScanRequestInfo.

        **参数解释**: 扫描的应急漏洞id列表，该字段不传值则扫描所有应急漏洞 **约束限制**: manual_scan_type字段的值中包含“urgent_vul”时有效 **取值范围**: 最小值1，最大值200 **默认取值**: 不涉及 

        :param urgent_vul_id_list: The urgent_vul_id_list of this ManualVulScanRequestInfo.
        :type urgent_vul_id_list: list[str]
        """
        self._urgent_vul_id_list = urgent_vul_id_list

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
        if not isinstance(other, ManualVulScanRequestInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

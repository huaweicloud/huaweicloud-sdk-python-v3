# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class VulHostHostsResponseInfoVulNumWithRepairPriorityList:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'repair_priority': 'str',
        'vul_num': 'int'
    }

    attribute_map = {
        'repair_priority': 'repair_priority',
        'vul_num': 'vul_num'
    }

    def __init__(self, repair_priority=None, vul_num=None):
        r"""VulHostHostsResponseInfoVulNumWithRepairPriorityList

        The model defined in huaweicloud sdk

        :param repair_priority: **参数解释**: 漏洞修复优先级 **取值范围**: 字符长度0-64位 
        :type repair_priority: str
        :param vul_num: **参数解释**: 该优先级下的漏洞数量 **取值范围**: 最小值0，最大值2147483647 
        :type vul_num: int
        """
        
        

        self._repair_priority = None
        self._vul_num = None
        self.discriminator = None

        if repair_priority is not None:
            self.repair_priority = repair_priority
        if vul_num is not None:
            self.vul_num = vul_num

    @property
    def repair_priority(self):
        r"""Gets the repair_priority of this VulHostHostsResponseInfoVulNumWithRepairPriorityList.

        **参数解释**: 漏洞修复优先级 **取值范围**: 字符长度0-64位 

        :return: The repair_priority of this VulHostHostsResponseInfoVulNumWithRepairPriorityList.
        :rtype: str
        """
        return self._repair_priority

    @repair_priority.setter
    def repair_priority(self, repair_priority):
        r"""Sets the repair_priority of this VulHostHostsResponseInfoVulNumWithRepairPriorityList.

        **参数解释**: 漏洞修复优先级 **取值范围**: 字符长度0-64位 

        :param repair_priority: The repair_priority of this VulHostHostsResponseInfoVulNumWithRepairPriorityList.
        :type repair_priority: str
        """
        self._repair_priority = repair_priority

    @property
    def vul_num(self):
        r"""Gets the vul_num of this VulHostHostsResponseInfoVulNumWithRepairPriorityList.

        **参数解释**: 该优先级下的漏洞数量 **取值范围**: 最小值0，最大值2147483647 

        :return: The vul_num of this VulHostHostsResponseInfoVulNumWithRepairPriorityList.
        :rtype: int
        """
        return self._vul_num

    @vul_num.setter
    def vul_num(self, vul_num):
        r"""Sets the vul_num of this VulHostHostsResponseInfoVulNumWithRepairPriorityList.

        **参数解释**: 该优先级下的漏洞数量 **取值范围**: 最小值0，最大值2147483647 

        :param vul_num: The vul_num of this VulHostHostsResponseInfoVulNumWithRepairPriorityList.
        :type vul_num: int
        """
        self._vul_num = vul_num

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
        if not isinstance(other, VulHostHostsResponseInfoVulNumWithRepairPriorityList):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

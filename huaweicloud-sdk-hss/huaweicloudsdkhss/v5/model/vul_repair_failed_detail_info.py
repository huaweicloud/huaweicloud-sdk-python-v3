# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class VulRepairFailedDetailInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'software': 'str',
        'reason': 'str',
        'reason_describtion': 'str',
        'reason_solution': 'str'
    }

    attribute_map = {
        'software': 'software',
        'reason': 'reason',
        'reason_describtion': 'reason_describtion',
        'reason_solution': 'reason_solution'
    }

    def __init__(self, software=None, reason=None, reason_describtion=None, reason_solution=None):
        r"""VulRepairFailedDetailInfo

        The model defined in huaweicloud sdk

        :param software: **参数解释**: 软件名称 **取值范围**: 字符长度1-512位 
        :type software: str
        :param reason: **参数解释**: 漏洞修复失败原因详情 **取值范围**: 字符长度0-65535位 
        :type reason: str
        :param reason_describtion: **参数解释**: 漏洞修复失败原因解释说明 **取值范围**: 字符长度0-256位 
        :type reason_describtion: str
        :param reason_solution: **参数解释**: 解决方式说明 **取值范围**: 字符长度0-65535位 
        :type reason_solution: str
        """
        
        

        self._software = None
        self._reason = None
        self._reason_describtion = None
        self._reason_solution = None
        self.discriminator = None

        if software is not None:
            self.software = software
        if reason is not None:
            self.reason = reason
        if reason_describtion is not None:
            self.reason_describtion = reason_describtion
        if reason_solution is not None:
            self.reason_solution = reason_solution

    @property
    def software(self):
        r"""Gets the software of this VulRepairFailedDetailInfo.

        **参数解释**: 软件名称 **取值范围**: 字符长度1-512位 

        :return: The software of this VulRepairFailedDetailInfo.
        :rtype: str
        """
        return self._software

    @software.setter
    def software(self, software):
        r"""Sets the software of this VulRepairFailedDetailInfo.

        **参数解释**: 软件名称 **取值范围**: 字符长度1-512位 

        :param software: The software of this VulRepairFailedDetailInfo.
        :type software: str
        """
        self._software = software

    @property
    def reason(self):
        r"""Gets the reason of this VulRepairFailedDetailInfo.

        **参数解释**: 漏洞修复失败原因详情 **取值范围**: 字符长度0-65535位 

        :return: The reason of this VulRepairFailedDetailInfo.
        :rtype: str
        """
        return self._reason

    @reason.setter
    def reason(self, reason):
        r"""Sets the reason of this VulRepairFailedDetailInfo.

        **参数解释**: 漏洞修复失败原因详情 **取值范围**: 字符长度0-65535位 

        :param reason: The reason of this VulRepairFailedDetailInfo.
        :type reason: str
        """
        self._reason = reason

    @property
    def reason_describtion(self):
        r"""Gets the reason_describtion of this VulRepairFailedDetailInfo.

        **参数解释**: 漏洞修复失败原因解释说明 **取值范围**: 字符长度0-256位 

        :return: The reason_describtion of this VulRepairFailedDetailInfo.
        :rtype: str
        """
        return self._reason_describtion

    @reason_describtion.setter
    def reason_describtion(self, reason_describtion):
        r"""Sets the reason_describtion of this VulRepairFailedDetailInfo.

        **参数解释**: 漏洞修复失败原因解释说明 **取值范围**: 字符长度0-256位 

        :param reason_describtion: The reason_describtion of this VulRepairFailedDetailInfo.
        :type reason_describtion: str
        """
        self._reason_describtion = reason_describtion

    @property
    def reason_solution(self):
        r"""Gets the reason_solution of this VulRepairFailedDetailInfo.

        **参数解释**: 解决方式说明 **取值范围**: 字符长度0-65535位 

        :return: The reason_solution of this VulRepairFailedDetailInfo.
        :rtype: str
        """
        return self._reason_solution

    @reason_solution.setter
    def reason_solution(self, reason_solution):
        r"""Sets the reason_solution of this VulRepairFailedDetailInfo.

        **参数解释**: 解决方式说明 **取值范围**: 字符长度0-65535位 

        :param reason_solution: The reason_solution of this VulRepairFailedDetailInfo.
        :type reason_solution: str
        """
        self._reason_solution = reason_solution

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
        if not isinstance(other, VulRepairFailedDetailInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

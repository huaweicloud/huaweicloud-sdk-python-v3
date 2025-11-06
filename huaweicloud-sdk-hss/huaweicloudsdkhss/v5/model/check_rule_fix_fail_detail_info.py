# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CheckRuleFixFailDetailInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'fix_fail_reason': 'str',
        'host_name': 'str'
    }

    attribute_map = {
        'fix_fail_reason': 'fix_fail_reason',
        'host_name': 'host_name'
    }

    def __init__(self, fix_fail_reason=None, host_name=None):
        r"""CheckRuleFixFailDetailInfo

        The model defined in huaweicloud sdk

        :param fix_fail_reason: **参数解释**: 修复失败原因 **取值范围**: 字符长度0-65534位 
        :type fix_fail_reason: str
        :param host_name: **参数解释**: 服务器名称 **取值范围**: 字符长度1-256位 
        :type host_name: str
        """
        
        

        self._fix_fail_reason = None
        self._host_name = None
        self.discriminator = None

        if fix_fail_reason is not None:
            self.fix_fail_reason = fix_fail_reason
        if host_name is not None:
            self.host_name = host_name

    @property
    def fix_fail_reason(self):
        r"""Gets the fix_fail_reason of this CheckRuleFixFailDetailInfo.

        **参数解释**: 修复失败原因 **取值范围**: 字符长度0-65534位 

        :return: The fix_fail_reason of this CheckRuleFixFailDetailInfo.
        :rtype: str
        """
        return self._fix_fail_reason

    @fix_fail_reason.setter
    def fix_fail_reason(self, fix_fail_reason):
        r"""Sets the fix_fail_reason of this CheckRuleFixFailDetailInfo.

        **参数解释**: 修复失败原因 **取值范围**: 字符长度0-65534位 

        :param fix_fail_reason: The fix_fail_reason of this CheckRuleFixFailDetailInfo.
        :type fix_fail_reason: str
        """
        self._fix_fail_reason = fix_fail_reason

    @property
    def host_name(self):
        r"""Gets the host_name of this CheckRuleFixFailDetailInfo.

        **参数解释**: 服务器名称 **取值范围**: 字符长度1-256位 

        :return: The host_name of this CheckRuleFixFailDetailInfo.
        :rtype: str
        """
        return self._host_name

    @host_name.setter
    def host_name(self, host_name):
        r"""Sets the host_name of this CheckRuleFixFailDetailInfo.

        **参数解释**: 服务器名称 **取值范围**: 字符长度1-256位 

        :param host_name: The host_name of this CheckRuleFixFailDetailInfo.
        :type host_name: str
        """
        self._host_name = host_name

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
        if not isinstance(other, CheckRuleFixFailDetailInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

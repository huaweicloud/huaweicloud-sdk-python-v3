# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class HostVulInfoDisabledOperateTypes:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'operate_type': 'str',
        'reason': 'str'
    }

    attribute_map = {
        'operate_type': 'operate_type',
        'reason': 'reason'
    }

    def __init__(self, operate_type=None, reason=None):
        r"""HostVulInfoDisabledOperateTypes

        The model defined in huaweicloud sdk

        :param operate_type: **参数解释**: 操作类型 **取值范围**: - ignore           : 忽略 - not_ignore       : 取消忽略 - immediate_repair : 修复 - manual_repair    : 人工修复 - verify           : 验证 - add_to_whitelist : 加入白名单 
        :type operate_type: str
        :param reason: **参数解释**: 不可进行操作的原因 **取值范围**: 字符范围0-512位 
        :type reason: str
        """
        
        

        self._operate_type = None
        self._reason = None
        self.discriminator = None

        if operate_type is not None:
            self.operate_type = operate_type
        if reason is not None:
            self.reason = reason

    @property
    def operate_type(self):
        r"""Gets the operate_type of this HostVulInfoDisabledOperateTypes.

        **参数解释**: 操作类型 **取值范围**: - ignore           : 忽略 - not_ignore       : 取消忽略 - immediate_repair : 修复 - manual_repair    : 人工修复 - verify           : 验证 - add_to_whitelist : 加入白名单 

        :return: The operate_type of this HostVulInfoDisabledOperateTypes.
        :rtype: str
        """
        return self._operate_type

    @operate_type.setter
    def operate_type(self, operate_type):
        r"""Sets the operate_type of this HostVulInfoDisabledOperateTypes.

        **参数解释**: 操作类型 **取值范围**: - ignore           : 忽略 - not_ignore       : 取消忽略 - immediate_repair : 修复 - manual_repair    : 人工修复 - verify           : 验证 - add_to_whitelist : 加入白名单 

        :param operate_type: The operate_type of this HostVulInfoDisabledOperateTypes.
        :type operate_type: str
        """
        self._operate_type = operate_type

    @property
    def reason(self):
        r"""Gets the reason of this HostVulInfoDisabledOperateTypes.

        **参数解释**: 不可进行操作的原因 **取值范围**: 字符范围0-512位 

        :return: The reason of this HostVulInfoDisabledOperateTypes.
        :rtype: str
        """
        return self._reason

    @reason.setter
    def reason(self, reason):
        r"""Sets the reason of this HostVulInfoDisabledOperateTypes.

        **参数解释**: 不可进行操作的原因 **取值范围**: 字符范围0-512位 

        :param reason: The reason of this HostVulInfoDisabledOperateTypes.
        :type reason: str
        """
        self._reason = reason

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
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
        if six.PY2:
            import sys
            reload(sys)
            sys.setdefaultencoding("utf-8")
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, HostVulInfoDisabledOperateTypes):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

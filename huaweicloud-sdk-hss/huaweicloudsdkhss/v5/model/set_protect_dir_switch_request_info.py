# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SetProtectDirSwitchRequestInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'protect_dir_list': 'list[str]',
        'enable_protect': 'bool'
    }

    attribute_map = {
        'protect_dir_list': 'protect_dir_list',
        'enable_protect': 'enable_protect'
    }

    def __init__(self, protect_dir_list=None, enable_protect=None):
        r"""SetProtectDirSwitchRequestInfo

        The model defined in huaweicloud sdk

        :param protect_dir_list: **参数解释**: 需要暂停或恢复的防护目录列表 **约束限制**: 不涉及 **取值范围**: 不超过50条 **默认取值**: 不涉及 
        :type protect_dir_list: list[str]
        :param enable_protect: **参数解释**: 暂停或恢复防护目录的防护状态 **约束限制**: 不涉及 **取值范围**: - true ：恢复防护。 - false ：暂停防护。  **默认取值**: false 
        :type enable_protect: bool
        """
        
        

        self._protect_dir_list = None
        self._enable_protect = None
        self.discriminator = None

        self.protect_dir_list = protect_dir_list
        self.enable_protect = enable_protect

    @property
    def protect_dir_list(self):
        r"""Gets the protect_dir_list of this SetProtectDirSwitchRequestInfo.

        **参数解释**: 需要暂停或恢复的防护目录列表 **约束限制**: 不涉及 **取值范围**: 不超过50条 **默认取值**: 不涉及 

        :return: The protect_dir_list of this SetProtectDirSwitchRequestInfo.
        :rtype: list[str]
        """
        return self._protect_dir_list

    @protect_dir_list.setter
    def protect_dir_list(self, protect_dir_list):
        r"""Sets the protect_dir_list of this SetProtectDirSwitchRequestInfo.

        **参数解释**: 需要暂停或恢复的防护目录列表 **约束限制**: 不涉及 **取值范围**: 不超过50条 **默认取值**: 不涉及 

        :param protect_dir_list: The protect_dir_list of this SetProtectDirSwitchRequestInfo.
        :type protect_dir_list: list[str]
        """
        self._protect_dir_list = protect_dir_list

    @property
    def enable_protect(self):
        r"""Gets the enable_protect of this SetProtectDirSwitchRequestInfo.

        **参数解释**: 暂停或恢复防护目录的防护状态 **约束限制**: 不涉及 **取值范围**: - true ：恢复防护。 - false ：暂停防护。  **默认取值**: false 

        :return: The enable_protect of this SetProtectDirSwitchRequestInfo.
        :rtype: bool
        """
        return self._enable_protect

    @enable_protect.setter
    def enable_protect(self, enable_protect):
        r"""Sets the enable_protect of this SetProtectDirSwitchRequestInfo.

        **参数解释**: 暂停或恢复防护目录的防护状态 **约束限制**: 不涉及 **取值范围**: - true ：恢复防护。 - false ：暂停防护。  **默认取值**: false 

        :param enable_protect: The enable_protect of this SetProtectDirSwitchRequestInfo.
        :type enable_protect: bool
        """
        self._enable_protect = enable_protect

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
        if not isinstance(other, SetProtectDirSwitchRequestInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

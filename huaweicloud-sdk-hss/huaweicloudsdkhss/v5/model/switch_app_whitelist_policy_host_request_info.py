# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SwitchAppWhitelistPolicyHostRequestInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'enable_app_whitelist': 'bool',
        'policy_info_list': 'list[AppPolicyInfoList]'
    }

    attribute_map = {
        'enable_app_whitelist': 'enable_app_whitelist',
        'policy_info_list': 'policy_info_list'
    }

    def __init__(self, enable_app_whitelist=None, policy_info_list=None):
        r"""SwitchAppWhitelistPolicyHostRequestInfo

        The model defined in huaweicloud sdk

        :param enable_app_whitelist: 是否开启/关闭白名单策略防护
        :type enable_app_whitelist: bool
        :param policy_info_list: 策略关联主机列表
        :type policy_info_list: list[:class:`huaweicloudsdkhss.v5.AppPolicyInfoList`]
        """
        
        

        self._enable_app_whitelist = None
        self._policy_info_list = None
        self.discriminator = None

        self.enable_app_whitelist = enable_app_whitelist
        self.policy_info_list = policy_info_list

    @property
    def enable_app_whitelist(self):
        r"""Gets the enable_app_whitelist of this SwitchAppWhitelistPolicyHostRequestInfo.

        是否开启/关闭白名单策略防护

        :return: The enable_app_whitelist of this SwitchAppWhitelistPolicyHostRequestInfo.
        :rtype: bool
        """
        return self._enable_app_whitelist

    @enable_app_whitelist.setter
    def enable_app_whitelist(self, enable_app_whitelist):
        r"""Sets the enable_app_whitelist of this SwitchAppWhitelistPolicyHostRequestInfo.

        是否开启/关闭白名单策略防护

        :param enable_app_whitelist: The enable_app_whitelist of this SwitchAppWhitelistPolicyHostRequestInfo.
        :type enable_app_whitelist: bool
        """
        self._enable_app_whitelist = enable_app_whitelist

    @property
    def policy_info_list(self):
        r"""Gets the policy_info_list of this SwitchAppWhitelistPolicyHostRequestInfo.

        策略关联主机列表

        :return: The policy_info_list of this SwitchAppWhitelistPolicyHostRequestInfo.
        :rtype: list[:class:`huaweicloudsdkhss.v5.AppPolicyInfoList`]
        """
        return self._policy_info_list

    @policy_info_list.setter
    def policy_info_list(self, policy_info_list):
        r"""Sets the policy_info_list of this SwitchAppWhitelistPolicyHostRequestInfo.

        策略关联主机列表

        :param policy_info_list: The policy_info_list of this SwitchAppWhitelistPolicyHostRequestInfo.
        :type policy_info_list: list[:class:`huaweicloudsdkhss.v5.AppPolicyInfoList`]
        """
        self._policy_info_list = policy_info_list

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
        if not isinstance(other, SwitchAppWhitelistPolicyHostRequestInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

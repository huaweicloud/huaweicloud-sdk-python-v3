# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateSecurityRuleEnableStatusResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'rule_id': 'str',
        'rule_name': 'str',
        'enabled': 'bool'
    }

    attribute_map = {
        'rule_id': 'rule_id',
        'rule_name': 'rule_name',
        'enabled': 'enabled'
    }

    def __init__(self, rule_id=None, rule_name=None, enabled=None):
        r"""UpdateSecurityRuleEnableStatusResponse

        The model defined in huaweicloud sdk

        :param rule_id: 识别规则id
        :type rule_id: str
        :param rule_name: 识别规则名称
        :type rule_name: str
        :param enabled: 识别规则是否开启
        :type enabled: bool
        """
        
        super(UpdateSecurityRuleEnableStatusResponse, self).__init__()

        self._rule_id = None
        self._rule_name = None
        self._enabled = None
        self.discriminator = None

        if rule_id is not None:
            self.rule_id = rule_id
        if rule_name is not None:
            self.rule_name = rule_name
        if enabled is not None:
            self.enabled = enabled

    @property
    def rule_id(self):
        r"""Gets the rule_id of this UpdateSecurityRuleEnableStatusResponse.

        识别规则id

        :return: The rule_id of this UpdateSecurityRuleEnableStatusResponse.
        :rtype: str
        """
        return self._rule_id

    @rule_id.setter
    def rule_id(self, rule_id):
        r"""Sets the rule_id of this UpdateSecurityRuleEnableStatusResponse.

        识别规则id

        :param rule_id: The rule_id of this UpdateSecurityRuleEnableStatusResponse.
        :type rule_id: str
        """
        self._rule_id = rule_id

    @property
    def rule_name(self):
        r"""Gets the rule_name of this UpdateSecurityRuleEnableStatusResponse.

        识别规则名称

        :return: The rule_name of this UpdateSecurityRuleEnableStatusResponse.
        :rtype: str
        """
        return self._rule_name

    @rule_name.setter
    def rule_name(self, rule_name):
        r"""Sets the rule_name of this UpdateSecurityRuleEnableStatusResponse.

        识别规则名称

        :param rule_name: The rule_name of this UpdateSecurityRuleEnableStatusResponse.
        :type rule_name: str
        """
        self._rule_name = rule_name

    @property
    def enabled(self):
        r"""Gets the enabled of this UpdateSecurityRuleEnableStatusResponse.

        识别规则是否开启

        :return: The enabled of this UpdateSecurityRuleEnableStatusResponse.
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        r"""Sets the enabled of this UpdateSecurityRuleEnableStatusResponse.

        识别规则是否开启

        :param enabled: The enabled of this UpdateSecurityRuleEnableStatusResponse.
        :type enabled: bool
        """
        self._enabled = enabled

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
        if not isinstance(other, UpdateSecurityRuleEnableStatusResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

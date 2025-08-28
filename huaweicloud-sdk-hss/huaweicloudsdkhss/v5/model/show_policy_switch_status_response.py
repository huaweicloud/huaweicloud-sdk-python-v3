# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowPolicySwitchStatusResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'policy_name': 'str',
        'enable': 'bool'
    }

    attribute_map = {
        'policy_name': 'policy_name',
        'enable': 'enable'
    }

    def __init__(self, policy_name=None, enable=None):
        r"""ShowPolicySwitchStatusResponse

        The model defined in huaweicloud sdk

        :param policy_name: **参数解释**： 策略名称 **取值范围**： 字符长度1-128位 
        :type policy_name: str
        :param enable: **参数解释**： 策略总开关是否开启 **取值范围**： - true：是。 - false：否。 
        :type enable: bool
        """
        
        super(ShowPolicySwitchStatusResponse, self).__init__()

        self._policy_name = None
        self._enable = None
        self.discriminator = None

        if policy_name is not None:
            self.policy_name = policy_name
        if enable is not None:
            self.enable = enable

    @property
    def policy_name(self):
        r"""Gets the policy_name of this ShowPolicySwitchStatusResponse.

        **参数解释**： 策略名称 **取值范围**： 字符长度1-128位 

        :return: The policy_name of this ShowPolicySwitchStatusResponse.
        :rtype: str
        """
        return self._policy_name

    @policy_name.setter
    def policy_name(self, policy_name):
        r"""Sets the policy_name of this ShowPolicySwitchStatusResponse.

        **参数解释**： 策略名称 **取值范围**： 字符长度1-128位 

        :param policy_name: The policy_name of this ShowPolicySwitchStatusResponse.
        :type policy_name: str
        """
        self._policy_name = policy_name

    @property
    def enable(self):
        r"""Gets the enable of this ShowPolicySwitchStatusResponse.

        **参数解释**： 策略总开关是否开启 **取值范围**： - true：是。 - false：否。 

        :return: The enable of this ShowPolicySwitchStatusResponse.
        :rtype: bool
        """
        return self._enable

    @enable.setter
    def enable(self, enable):
        r"""Sets the enable of this ShowPolicySwitchStatusResponse.

        **参数解释**： 策略总开关是否开启 **取值范围**： - true：是。 - false：否。 

        :param enable: The enable of this ShowPolicySwitchStatusResponse.
        :type enable: bool
        """
        self._enable = enable

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
        if not isinstance(other, ShowPolicySwitchStatusResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

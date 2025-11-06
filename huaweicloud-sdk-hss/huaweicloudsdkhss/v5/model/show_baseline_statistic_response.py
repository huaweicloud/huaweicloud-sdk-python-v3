# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowBaselineStatisticResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'host_weak_pwd': 'int',
        'pwd_policy': 'int',
        'security_check': 'int'
    }

    attribute_map = {
        'host_weak_pwd': 'host_weak_pwd',
        'pwd_policy': 'pwd_policy',
        'security_check': 'security_check'
    }

    def __init__(self, host_weak_pwd=None, pwd_policy=None, security_check=None):
        r"""ShowBaselineStatisticResponse

        The model defined in huaweicloud sdk

        :param host_weak_pwd: **参数解释**: 弱口令检测数量 **取值范围**: 取值0-9223372036854775807 
        :type host_weak_pwd: int
        :param pwd_policy: **参数解释**: 口令复杂度策略检测数量 **取值范围**: 取值0-9223372036854775807 
        :type pwd_policy: int
        :param security_check: **参数解释**: 服务器配置检测数量 **取值范围**: 取值0-9223372036854775807 
        :type security_check: int
        """
        
        super().__init__()

        self._host_weak_pwd = None
        self._pwd_policy = None
        self._security_check = None
        self.discriminator = None

        if host_weak_pwd is not None:
            self.host_weak_pwd = host_weak_pwd
        if pwd_policy is not None:
            self.pwd_policy = pwd_policy
        if security_check is not None:
            self.security_check = security_check

    @property
    def host_weak_pwd(self):
        r"""Gets the host_weak_pwd of this ShowBaselineStatisticResponse.

        **参数解释**: 弱口令检测数量 **取值范围**: 取值0-9223372036854775807 

        :return: The host_weak_pwd of this ShowBaselineStatisticResponse.
        :rtype: int
        """
        return self._host_weak_pwd

    @host_weak_pwd.setter
    def host_weak_pwd(self, host_weak_pwd):
        r"""Sets the host_weak_pwd of this ShowBaselineStatisticResponse.

        **参数解释**: 弱口令检测数量 **取值范围**: 取值0-9223372036854775807 

        :param host_weak_pwd: The host_weak_pwd of this ShowBaselineStatisticResponse.
        :type host_weak_pwd: int
        """
        self._host_weak_pwd = host_weak_pwd

    @property
    def pwd_policy(self):
        r"""Gets the pwd_policy of this ShowBaselineStatisticResponse.

        **参数解释**: 口令复杂度策略检测数量 **取值范围**: 取值0-9223372036854775807 

        :return: The pwd_policy of this ShowBaselineStatisticResponse.
        :rtype: int
        """
        return self._pwd_policy

    @pwd_policy.setter
    def pwd_policy(self, pwd_policy):
        r"""Sets the pwd_policy of this ShowBaselineStatisticResponse.

        **参数解释**: 口令复杂度策略检测数量 **取值范围**: 取值0-9223372036854775807 

        :param pwd_policy: The pwd_policy of this ShowBaselineStatisticResponse.
        :type pwd_policy: int
        """
        self._pwd_policy = pwd_policy

    @property
    def security_check(self):
        r"""Gets the security_check of this ShowBaselineStatisticResponse.

        **参数解释**: 服务器配置检测数量 **取值范围**: 取值0-9223372036854775807 

        :return: The security_check of this ShowBaselineStatisticResponse.
        :rtype: int
        """
        return self._security_check

    @security_check.setter
    def security_check(self, security_check):
        r"""Sets the security_check of this ShowBaselineStatisticResponse.

        **参数解释**: 服务器配置检测数量 **取值范围**: 取值0-9223372036854775807 

        :param security_check: The security_check of this ShowBaselineStatisticResponse.
        :type security_check: int
        """
        self._security_check = security_check

    def to_dict(self):
        import warnings
        warnings.warn("ShowBaselineStatisticResponse.to_dict() is deprecated and no longer maintained, "
                      "use to_json_object() to get the response content.", DeprecationWarning)
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
        if not isinstance(other, ShowBaselineStatisticResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

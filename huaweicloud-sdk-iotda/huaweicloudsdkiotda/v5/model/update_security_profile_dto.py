# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateSecurityProfileDTO:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'alarm_level': 'str',
        'security_level': 'str',
        'enable': 'bool',
        'profile': 'list[SecurityProfile]',
        'profile_targets': 'SecurityTarget'
    }

    attribute_map = {
        'alarm_level': 'alarm_level',
        'security_level': 'security_level',
        'enable': 'enable',
        'profile': 'profile',
        'profile_targets': 'profile_targets'
    }

    def __init__(self, alarm_level=None, security_level=None, enable=None, profile=None, profile_targets=None):
        r"""UpdateSecurityProfileDTO

        The model defined in huaweicloud sdk

        :param alarm_level: 安全态势感知告警级别，CRITICAL：严重告警，MAJOR：重要告警，MINOR：一般告警
        :type alarm_level: str
        :param security_level: 安全态势感知项所属安全风险级别；BASIC_SECURITY：基础安全，ADVANCE_SECURITY：高级安全，ULTIMATE_SECURITY：极致安全
        :type security_level: str
        :param enable: 安全态势感知项是否开启
        :type enable: bool
        :param profile: 安全态势感知项配置结构体，用于设备侧检测项下发给设备
        :type profile: list[:class:`huaweicloudsdkiotda.v5.SecurityProfile`]
        :param profile_targets: 
        :type profile_targets: :class:`huaweicloudsdkiotda.v5.SecurityTarget`
        """
        
        

        self._alarm_level = None
        self._security_level = None
        self._enable = None
        self._profile = None
        self._profile_targets = None
        self.discriminator = None

        if alarm_level is not None:
            self.alarm_level = alarm_level
        if security_level is not None:
            self.security_level = security_level
        if enable is not None:
            self.enable = enable
        if profile is not None:
            self.profile = profile
        if profile_targets is not None:
            self.profile_targets = profile_targets

    @property
    def alarm_level(self):
        r"""Gets the alarm_level of this UpdateSecurityProfileDTO.

        安全态势感知告警级别，CRITICAL：严重告警，MAJOR：重要告警，MINOR：一般告警

        :return: The alarm_level of this UpdateSecurityProfileDTO.
        :rtype: str
        """
        return self._alarm_level

    @alarm_level.setter
    def alarm_level(self, alarm_level):
        r"""Sets the alarm_level of this UpdateSecurityProfileDTO.

        安全态势感知告警级别，CRITICAL：严重告警，MAJOR：重要告警，MINOR：一般告警

        :param alarm_level: The alarm_level of this UpdateSecurityProfileDTO.
        :type alarm_level: str
        """
        self._alarm_level = alarm_level

    @property
    def security_level(self):
        r"""Gets the security_level of this UpdateSecurityProfileDTO.

        安全态势感知项所属安全风险级别；BASIC_SECURITY：基础安全，ADVANCE_SECURITY：高级安全，ULTIMATE_SECURITY：极致安全

        :return: The security_level of this UpdateSecurityProfileDTO.
        :rtype: str
        """
        return self._security_level

    @security_level.setter
    def security_level(self, security_level):
        r"""Sets the security_level of this UpdateSecurityProfileDTO.

        安全态势感知项所属安全风险级别；BASIC_SECURITY：基础安全，ADVANCE_SECURITY：高级安全，ULTIMATE_SECURITY：极致安全

        :param security_level: The security_level of this UpdateSecurityProfileDTO.
        :type security_level: str
        """
        self._security_level = security_level

    @property
    def enable(self):
        r"""Gets the enable of this UpdateSecurityProfileDTO.

        安全态势感知项是否开启

        :return: The enable of this UpdateSecurityProfileDTO.
        :rtype: bool
        """
        return self._enable

    @enable.setter
    def enable(self, enable):
        r"""Sets the enable of this UpdateSecurityProfileDTO.

        安全态势感知项是否开启

        :param enable: The enable of this UpdateSecurityProfileDTO.
        :type enable: bool
        """
        self._enable = enable

    @property
    def profile(self):
        r"""Gets the profile of this UpdateSecurityProfileDTO.

        安全态势感知项配置结构体，用于设备侧检测项下发给设备

        :return: The profile of this UpdateSecurityProfileDTO.
        :rtype: list[:class:`huaweicloudsdkiotda.v5.SecurityProfile`]
        """
        return self._profile

    @profile.setter
    def profile(self, profile):
        r"""Sets the profile of this UpdateSecurityProfileDTO.

        安全态势感知项配置结构体，用于设备侧检测项下发给设备

        :param profile: The profile of this UpdateSecurityProfileDTO.
        :type profile: list[:class:`huaweicloudsdkiotda.v5.SecurityProfile`]
        """
        self._profile = profile

    @property
    def profile_targets(self):
        r"""Gets the profile_targets of this UpdateSecurityProfileDTO.

        :return: The profile_targets of this UpdateSecurityProfileDTO.
        :rtype: :class:`huaweicloudsdkiotda.v5.SecurityTarget`
        """
        return self._profile_targets

    @profile_targets.setter
    def profile_targets(self, profile_targets):
        r"""Sets the profile_targets of this UpdateSecurityProfileDTO.

        :param profile_targets: The profile_targets of this UpdateSecurityProfileDTO.
        :type profile_targets: :class:`huaweicloudsdkiotda.v5.SecurityTarget`
        """
        self._profile_targets = profile_targets

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
        if not isinstance(other, UpdateSecurityProfileDTO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

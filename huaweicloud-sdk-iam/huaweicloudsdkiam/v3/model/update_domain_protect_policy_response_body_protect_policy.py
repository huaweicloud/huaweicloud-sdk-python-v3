# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateDomainProtectPolicyResponseBodyProtectPolicy:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'allow_user': 'AllowUserBody',
        'operation_protection': 'bool',
        'admin_check': 'str',
        'scene': 'str'
    }

    attribute_map = {
        'allow_user': 'allow_user',
        'operation_protection': 'operation_protection',
        'admin_check': 'admin_check',
        'scene': 'scene'
    }

    def __init__(self, allow_user=None, operation_protection=None, admin_check=None, scene=None):
        """UpdateDomainProtectPolicyResponseBodyProtectPolicy

        The model defined in huaweicloud sdk

        :param allow_user: 
        :type allow_user: :class:`huaweicloudsdkiam.v3.AllowUserBody`
        :param operation_protection: 是否开启操作保护，取值范围true或false。
        :type operation_protection: bool
        :param admin_check: 是否指定人员验证。on为指定人员验证，必须填写scene参数。off为操作员验证。
        :type admin_check: str
        :param scene: 操作保护指定人员验证方式，admin_check为on时，必须填写。包括mobile、email。
        :type scene: str
        """
        
        

        self._allow_user = None
        self._operation_protection = None
        self._admin_check = None
        self._scene = None
        self.discriminator = None

        self.allow_user = allow_user
        self.operation_protection = operation_protection
        self.admin_check = admin_check
        self.scene = scene

    @property
    def allow_user(self):
        """Gets the allow_user of this UpdateDomainProtectPolicyResponseBodyProtectPolicy.

        :return: The allow_user of this UpdateDomainProtectPolicyResponseBodyProtectPolicy.
        :rtype: :class:`huaweicloudsdkiam.v3.AllowUserBody`
        """
        return self._allow_user

    @allow_user.setter
    def allow_user(self, allow_user):
        """Sets the allow_user of this UpdateDomainProtectPolicyResponseBodyProtectPolicy.

        :param allow_user: The allow_user of this UpdateDomainProtectPolicyResponseBodyProtectPolicy.
        :type allow_user: :class:`huaweicloudsdkiam.v3.AllowUserBody`
        """
        self._allow_user = allow_user

    @property
    def operation_protection(self):
        """Gets the operation_protection of this UpdateDomainProtectPolicyResponseBodyProtectPolicy.

        是否开启操作保护，取值范围true或false。

        :return: The operation_protection of this UpdateDomainProtectPolicyResponseBodyProtectPolicy.
        :rtype: bool
        """
        return self._operation_protection

    @operation_protection.setter
    def operation_protection(self, operation_protection):
        """Sets the operation_protection of this UpdateDomainProtectPolicyResponseBodyProtectPolicy.

        是否开启操作保护，取值范围true或false。

        :param operation_protection: The operation_protection of this UpdateDomainProtectPolicyResponseBodyProtectPolicy.
        :type operation_protection: bool
        """
        self._operation_protection = operation_protection

    @property
    def admin_check(self):
        """Gets the admin_check of this UpdateDomainProtectPolicyResponseBodyProtectPolicy.

        是否指定人员验证。on为指定人员验证，必须填写scene参数。off为操作员验证。

        :return: The admin_check of this UpdateDomainProtectPolicyResponseBodyProtectPolicy.
        :rtype: str
        """
        return self._admin_check

    @admin_check.setter
    def admin_check(self, admin_check):
        """Sets the admin_check of this UpdateDomainProtectPolicyResponseBodyProtectPolicy.

        是否指定人员验证。on为指定人员验证，必须填写scene参数。off为操作员验证。

        :param admin_check: The admin_check of this UpdateDomainProtectPolicyResponseBodyProtectPolicy.
        :type admin_check: str
        """
        self._admin_check = admin_check

    @property
    def scene(self):
        """Gets the scene of this UpdateDomainProtectPolicyResponseBodyProtectPolicy.

        操作保护指定人员验证方式，admin_check为on时，必须填写。包括mobile、email。

        :return: The scene of this UpdateDomainProtectPolicyResponseBodyProtectPolicy.
        :rtype: str
        """
        return self._scene

    @scene.setter
    def scene(self, scene):
        """Sets the scene of this UpdateDomainProtectPolicyResponseBodyProtectPolicy.

        操作保护指定人员验证方式，admin_check为on时，必须填写。包括mobile、email。

        :param scene: The scene of this UpdateDomainProtectPolicyResponseBodyProtectPolicy.
        :type scene: str
        """
        self._scene = scene

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
        if not isinstance(other, UpdateDomainProtectPolicyResponseBodyProtectPolicy):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

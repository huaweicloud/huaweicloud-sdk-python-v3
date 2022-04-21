# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class IdentityproviderOption:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'sso_type': 'str',
        'description': 'str',
        'enabled': 'bool'
    }

    attribute_map = {
        'sso_type': 'sso_type',
        'description': 'description',
        'enabled': 'enabled'
    }

    def __init__(self, sso_type=None, description=None, enabled=None):
        """IdentityproviderOption

        The model defined in huaweicloud sdk

        :param sso_type: 身份提供商类型。当前支持virtual_user_sso和iam_user_sso两种，缺省配置默认为virtual_user_sso类型。
        :type sso_type: str
        :param description: 身份提供商描述信息。
        :type description: str
        :param enabled: 身份提供商是否启用，true为启用，false为停用，默认为false。
        :type enabled: bool
        """
        
        

        self._sso_type = None
        self._description = None
        self._enabled = None
        self.discriminator = None

        if sso_type is not None:
            self.sso_type = sso_type
        if description is not None:
            self.description = description
        if enabled is not None:
            self.enabled = enabled

    @property
    def sso_type(self):
        """Gets the sso_type of this IdentityproviderOption.

        身份提供商类型。当前支持virtual_user_sso和iam_user_sso两种，缺省配置默认为virtual_user_sso类型。

        :return: The sso_type of this IdentityproviderOption.
        :rtype: str
        """
        return self._sso_type

    @sso_type.setter
    def sso_type(self, sso_type):
        """Sets the sso_type of this IdentityproviderOption.

        身份提供商类型。当前支持virtual_user_sso和iam_user_sso两种，缺省配置默认为virtual_user_sso类型。

        :param sso_type: The sso_type of this IdentityproviderOption.
        :type sso_type: str
        """
        self._sso_type = sso_type

    @property
    def description(self):
        """Gets the description of this IdentityproviderOption.

        身份提供商描述信息。

        :return: The description of this IdentityproviderOption.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this IdentityproviderOption.

        身份提供商描述信息。

        :param description: The description of this IdentityproviderOption.
        :type description: str
        """
        self._description = description

    @property
    def enabled(self):
        """Gets the enabled of this IdentityproviderOption.

        身份提供商是否启用，true为启用，false为停用，默认为false。

        :return: The enabled of this IdentityproviderOption.
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        """Sets the enabled of this IdentityproviderOption.

        身份提供商是否启用，true为启用，false为停用，默认为false。

        :param enabled: The enabled of this IdentityproviderOption.
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
        if not isinstance(other, IdentityproviderOption):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

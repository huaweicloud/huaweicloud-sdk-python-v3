# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateTokenPolicyReqBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'token_enabled': 'bool'
    }

    attribute_map = {
        'token_enabled': 'token_enabled'
    }

    def __init__(self, token_enabled=None):
        r"""UpdateTokenPolicyReqBody

        The model defined in huaweicloud sdk

        :param token_enabled: 是否允许获取Token，默认为true，设置为false后将不允许获取账号下所有身份类型（IAM用户、委托、联邦用户）的Token（联邦认证获取的unscoped token不受Token策略影响）。
        :type token_enabled: bool
        """
        
        

        self._token_enabled = None
        self.discriminator = None

        if token_enabled is not None:
            self.token_enabled = token_enabled

    @property
    def token_enabled(self):
        r"""Gets the token_enabled of this UpdateTokenPolicyReqBody.

        是否允许获取Token，默认为true，设置为false后将不允许获取账号下所有身份类型（IAM用户、委托、联邦用户）的Token（联邦认证获取的unscoped token不受Token策略影响）。

        :return: The token_enabled of this UpdateTokenPolicyReqBody.
        :rtype: bool
        """
        return self._token_enabled

    @token_enabled.setter
    def token_enabled(self, token_enabled):
        r"""Sets the token_enabled of this UpdateTokenPolicyReqBody.

        是否允许获取Token，默认为true，设置为false后将不允许获取账号下所有身份类型（IAM用户、委托、联邦用户）的Token（联邦认证获取的unscoped token不受Token策略影响）。

        :param token_enabled: The token_enabled of this UpdateTokenPolicyReqBody.
        :type token_enabled: bool
        """
        self._token_enabled = token_enabled

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
        if not isinstance(other, UpdateTokenPolicyReqBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

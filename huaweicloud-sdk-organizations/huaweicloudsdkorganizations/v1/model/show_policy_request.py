# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowPolicyRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []
    sensitive_list.append('x_security_token')

    openapi_types = {
        'x_security_token': 'str',
        'policy_id': 'str',
        'x_language': 'str'
    }

    attribute_map = {
        'x_security_token': 'X-Security-Token',
        'policy_id': 'policy_id',
        'x_language': 'X-Language'
    }

    def __init__(self, x_security_token=None, policy_id=None, x_language=None):
        r"""ShowPolicyRequest

        The model defined in huaweicloud sdk

        :param x_security_token: 如果正在使用临时安全凭据，则此header是必需的，该值是临时安全凭据的安全令牌（会话令牌）。
        :type x_security_token: str
        :param policy_id: 策略的唯一标识符（ID）。
        :type policy_id: str
        :param x_language: 选择接口返回的信息的语言
        :type x_language: str
        """
        
        

        self._x_security_token = None
        self._policy_id = None
        self._x_language = None
        self.discriminator = None

        if x_security_token is not None:
            self.x_security_token = x_security_token
        self.policy_id = policy_id
        if x_language is not None:
            self.x_language = x_language

    @property
    def x_security_token(self):
        r"""Gets the x_security_token of this ShowPolicyRequest.

        如果正在使用临时安全凭据，则此header是必需的，该值是临时安全凭据的安全令牌（会话令牌）。

        :return: The x_security_token of this ShowPolicyRequest.
        :rtype: str
        """
        return self._x_security_token

    @x_security_token.setter
    def x_security_token(self, x_security_token):
        r"""Sets the x_security_token of this ShowPolicyRequest.

        如果正在使用临时安全凭据，则此header是必需的，该值是临时安全凭据的安全令牌（会话令牌）。

        :param x_security_token: The x_security_token of this ShowPolicyRequest.
        :type x_security_token: str
        """
        self._x_security_token = x_security_token

    @property
    def policy_id(self):
        r"""Gets the policy_id of this ShowPolicyRequest.

        策略的唯一标识符（ID）。

        :return: The policy_id of this ShowPolicyRequest.
        :rtype: str
        """
        return self._policy_id

    @policy_id.setter
    def policy_id(self, policy_id):
        r"""Sets the policy_id of this ShowPolicyRequest.

        策略的唯一标识符（ID）。

        :param policy_id: The policy_id of this ShowPolicyRequest.
        :type policy_id: str
        """
        self._policy_id = policy_id

    @property
    def x_language(self):
        r"""Gets the x_language of this ShowPolicyRequest.

        选择接口返回的信息的语言

        :return: The x_language of this ShowPolicyRequest.
        :rtype: str
        """
        return self._x_language

    @x_language.setter
    def x_language(self, x_language):
        r"""Sets the x_language of this ShowPolicyRequest.

        选择接口返回的信息的语言

        :param x_language: The x_language of this ShowPolicyRequest.
        :type x_language: str
        """
        self._x_language = x_language

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
        if not isinstance(other, ShowPolicyRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowEffectivePoliciesRequest:

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
        'entity_id': 'str',
        'policy_type': 'str'
    }

    attribute_map = {
        'x_security_token': 'X-Security-Token',
        'entity_id': 'entity_id',
        'policy_type': 'policy_type'
    }

    def __init__(self, x_security_token=None, entity_id=None, policy_type=None):
        r"""ShowEffectivePoliciesRequest

        The model defined in huaweicloud sdk

        :param x_security_token: 如果正在使用临时安全凭据，则此header是必需的，该值是临时安全凭据的安全令牌（会话令牌）。
        :type x_security_token: str
        :param entity_id: 账号的唯一标识符（ID）。当前还不支持指定根、组织单元。
        :type entity_id: str
        :param policy_type: 策略类型的名称，tag_policy标签策略。
        :type policy_type: str
        """
        
        

        self._x_security_token = None
        self._entity_id = None
        self._policy_type = None
        self.discriminator = None

        if x_security_token is not None:
            self.x_security_token = x_security_token
        self.entity_id = entity_id
        self.policy_type = policy_type

    @property
    def x_security_token(self):
        r"""Gets the x_security_token of this ShowEffectivePoliciesRequest.

        如果正在使用临时安全凭据，则此header是必需的，该值是临时安全凭据的安全令牌（会话令牌）。

        :return: The x_security_token of this ShowEffectivePoliciesRequest.
        :rtype: str
        """
        return self._x_security_token

    @x_security_token.setter
    def x_security_token(self, x_security_token):
        r"""Sets the x_security_token of this ShowEffectivePoliciesRequest.

        如果正在使用临时安全凭据，则此header是必需的，该值是临时安全凭据的安全令牌（会话令牌）。

        :param x_security_token: The x_security_token of this ShowEffectivePoliciesRequest.
        :type x_security_token: str
        """
        self._x_security_token = x_security_token

    @property
    def entity_id(self):
        r"""Gets the entity_id of this ShowEffectivePoliciesRequest.

        账号的唯一标识符（ID）。当前还不支持指定根、组织单元。

        :return: The entity_id of this ShowEffectivePoliciesRequest.
        :rtype: str
        """
        return self._entity_id

    @entity_id.setter
    def entity_id(self, entity_id):
        r"""Sets the entity_id of this ShowEffectivePoliciesRequest.

        账号的唯一标识符（ID）。当前还不支持指定根、组织单元。

        :param entity_id: The entity_id of this ShowEffectivePoliciesRequest.
        :type entity_id: str
        """
        self._entity_id = entity_id

    @property
    def policy_type(self):
        r"""Gets the policy_type of this ShowEffectivePoliciesRequest.

        策略类型的名称，tag_policy标签策略。

        :return: The policy_type of this ShowEffectivePoliciesRequest.
        :rtype: str
        """
        return self._policy_type

    @policy_type.setter
    def policy_type(self, policy_type):
        r"""Sets the policy_type of this ShowEffectivePoliciesRequest.

        策略类型的名称，tag_policy标签策略。

        :param policy_type: The policy_type of this ShowEffectivePoliciesRequest.
        :type policy_type: str
        """
        self._policy_type = policy_type

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
        if not isinstance(other, ShowEffectivePoliciesRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

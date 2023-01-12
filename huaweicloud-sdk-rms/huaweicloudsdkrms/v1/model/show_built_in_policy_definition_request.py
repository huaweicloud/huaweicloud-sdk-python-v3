# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowBuiltInPolicyDefinitionRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []
    sensitive_list.append('x_auth_token')

    openapi_types = {
        'x_auth_token': 'str',
        'policy_definition_id': 'str',
        'x_language': 'str'
    }

    attribute_map = {
        'x_auth_token': 'X-Auth-Token',
        'policy_definition_id': 'policy_definition_id',
        'x_language': 'X-Language'
    }

    def __init__(self, x_auth_token=None, policy_definition_id=None, x_language=None):
        """ShowBuiltInPolicyDefinitionRequest

        The model defined in huaweicloud sdk

        :param x_auth_token: 用户Token。 获取Token，请参考《统一身份认证服务API参考》的“获取用户Token”章节。请求响应成功后在响应消息头中包含的“X-Subject-Token”的值即为Token值。
        :type x_auth_token: str
        :param policy_definition_id: 策略ID
        :type policy_definition_id: str
        :param x_language: 选择接口返回的信息的语言，默认为\&quot;zh-cn\&quot;中文
        :type x_language: str
        """
        
        

        self._x_auth_token = None
        self._policy_definition_id = None
        self._x_language = None
        self.discriminator = None

        self.x_auth_token = x_auth_token
        self.policy_definition_id = policy_definition_id
        if x_language is not None:
            self.x_language = x_language

    @property
    def x_auth_token(self):
        """Gets the x_auth_token of this ShowBuiltInPolicyDefinitionRequest.

        用户Token。 获取Token，请参考《统一身份认证服务API参考》的“获取用户Token”章节。请求响应成功后在响应消息头中包含的“X-Subject-Token”的值即为Token值。

        :return: The x_auth_token of this ShowBuiltInPolicyDefinitionRequest.
        :rtype: str
        """
        return self._x_auth_token

    @x_auth_token.setter
    def x_auth_token(self, x_auth_token):
        """Sets the x_auth_token of this ShowBuiltInPolicyDefinitionRequest.

        用户Token。 获取Token，请参考《统一身份认证服务API参考》的“获取用户Token”章节。请求响应成功后在响应消息头中包含的“X-Subject-Token”的值即为Token值。

        :param x_auth_token: The x_auth_token of this ShowBuiltInPolicyDefinitionRequest.
        :type x_auth_token: str
        """
        self._x_auth_token = x_auth_token

    @property
    def policy_definition_id(self):
        """Gets the policy_definition_id of this ShowBuiltInPolicyDefinitionRequest.

        策略ID

        :return: The policy_definition_id of this ShowBuiltInPolicyDefinitionRequest.
        :rtype: str
        """
        return self._policy_definition_id

    @policy_definition_id.setter
    def policy_definition_id(self, policy_definition_id):
        """Sets the policy_definition_id of this ShowBuiltInPolicyDefinitionRequest.

        策略ID

        :param policy_definition_id: The policy_definition_id of this ShowBuiltInPolicyDefinitionRequest.
        :type policy_definition_id: str
        """
        self._policy_definition_id = policy_definition_id

    @property
    def x_language(self):
        """Gets the x_language of this ShowBuiltInPolicyDefinitionRequest.

        选择接口返回的信息的语言，默认为\"zh-cn\"中文

        :return: The x_language of this ShowBuiltInPolicyDefinitionRequest.
        :rtype: str
        """
        return self._x_language

    @x_language.setter
    def x_language(self, x_language):
        """Sets the x_language of this ShowBuiltInPolicyDefinitionRequest.

        选择接口返回的信息的语言，默认为\"zh-cn\"中文

        :param x_language: The x_language of this ShowBuiltInPolicyDefinitionRequest.
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
        if not isinstance(other, ShowBuiltInPolicyDefinitionRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

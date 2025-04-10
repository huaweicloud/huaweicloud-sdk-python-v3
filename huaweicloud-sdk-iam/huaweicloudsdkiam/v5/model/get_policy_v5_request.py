# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class GetPolicyV5Request:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'policy_id': 'str',
        'x_language': 'str'
    }

    attribute_map = {
        'policy_id': 'policy_id',
        'x_language': 'X-Language'
    }

    def __init__(self, policy_id=None, x_language=None):
        r"""GetPolicyV5Request

        The model defined in huaweicloud sdk

        :param policy_id: 身份策略ID，长度为1到64个字符，只包含字母、数字和\&quot;-\&quot;的字符串。
        :type policy_id: str
        :param x_language: 选择接口返回的信息的语言，可以为中文（\&quot;zh-cn\&quot;）或英文（\&quot;en-us\&quot;），默认为中文。
        :type x_language: str
        """
        
        

        self._policy_id = None
        self._x_language = None
        self.discriminator = None

        self.policy_id = policy_id
        if x_language is not None:
            self.x_language = x_language

    @property
    def policy_id(self):
        r"""Gets the policy_id of this GetPolicyV5Request.

        身份策略ID，长度为1到64个字符，只包含字母、数字和\"-\"的字符串。

        :return: The policy_id of this GetPolicyV5Request.
        :rtype: str
        """
        return self._policy_id

    @policy_id.setter
    def policy_id(self, policy_id):
        r"""Sets the policy_id of this GetPolicyV5Request.

        身份策略ID，长度为1到64个字符，只包含字母、数字和\"-\"的字符串。

        :param policy_id: The policy_id of this GetPolicyV5Request.
        :type policy_id: str
        """
        self._policy_id = policy_id

    @property
    def x_language(self):
        r"""Gets the x_language of this GetPolicyV5Request.

        选择接口返回的信息的语言，可以为中文（\"zh-cn\"）或英文（\"en-us\"），默认为中文。

        :return: The x_language of this GetPolicyV5Request.
        :rtype: str
        """
        return self._x_language

    @x_language.setter
    def x_language(self, x_language):
        r"""Sets the x_language of this GetPolicyV5Request.

        选择接口返回的信息的语言，可以为中文（\"zh-cn\"）或英文（\"en-us\"），默认为中文。

        :param x_language: The x_language of this GetPolicyV5Request.
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
        if not isinstance(other, GetPolicyV5Request):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SetDefaultPolicyVersionV5Request:

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
        'version_id': 'str'
    }

    attribute_map = {
        'policy_id': 'policy_id',
        'version_id': 'version_id'
    }

    def __init__(self, policy_id=None, version_id=None):
        """SetDefaultPolicyVersionV5Request

        The model defined in huaweicloud sdk

        :param policy_id: 身份策略ID，长度为1到64个字符，只包含字母、数字和\&quot;-\&quot;的字符串。
        :type policy_id: str
        :param version_id: 身份策略版本号，以\&quot;v\&quot;开头后跟数字的字符串，例如\&quot;v5\&quot;。
        :type version_id: str
        """
        
        

        self._policy_id = None
        self._version_id = None
        self.discriminator = None

        self.policy_id = policy_id
        self.version_id = version_id

    @property
    def policy_id(self):
        """Gets the policy_id of this SetDefaultPolicyVersionV5Request.

        身份策略ID，长度为1到64个字符，只包含字母、数字和\"-\"的字符串。

        :return: The policy_id of this SetDefaultPolicyVersionV5Request.
        :rtype: str
        """
        return self._policy_id

    @policy_id.setter
    def policy_id(self, policy_id):
        """Sets the policy_id of this SetDefaultPolicyVersionV5Request.

        身份策略ID，长度为1到64个字符，只包含字母、数字和\"-\"的字符串。

        :param policy_id: The policy_id of this SetDefaultPolicyVersionV5Request.
        :type policy_id: str
        """
        self._policy_id = policy_id

    @property
    def version_id(self):
        """Gets the version_id of this SetDefaultPolicyVersionV5Request.

        身份策略版本号，以\"v\"开头后跟数字的字符串，例如\"v5\"。

        :return: The version_id of this SetDefaultPolicyVersionV5Request.
        :rtype: str
        """
        return self._version_id

    @version_id.setter
    def version_id(self, version_id):
        """Sets the version_id of this SetDefaultPolicyVersionV5Request.

        身份策略版本号，以\"v\"开头后跟数字的字符串，例如\"v5\"。

        :param version_id: The version_id of this SetDefaultPolicyVersionV5Request.
        :type version_id: str
        """
        self._version_id = version_id

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
        if not isinstance(other, SetDefaultPolicyVersionV5Request):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

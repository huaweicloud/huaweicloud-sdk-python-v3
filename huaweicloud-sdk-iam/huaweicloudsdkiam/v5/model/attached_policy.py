# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AttachedPolicy:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'policy_name': 'str',
        'policy_id': 'str',
        'urn': 'str',
        'attached_at': 'datetime'
    }

    attribute_map = {
        'policy_name': 'policy_name',
        'policy_id': 'policy_id',
        'urn': 'urn',
        'attached_at': 'attached_at'
    }

    def __init__(self, policy_name=None, policy_id=None, urn=None, attached_at=None):
        r"""AttachedPolicy

        The model defined in huaweicloud sdk

        :param policy_name: 身份策略名称，长度为1到128个字符，只包含字母、数字、\&quot;_\&quot;、\&quot;+\&quot;、\&quot;&#x3D;\&quot;、\&quot;.\&quot;、\&quot;@\&quot;和\&quot;-\&quot;的字符串。
        :type policy_name: str
        :param policy_id: 身份策略ID，长度为1到64个字符，只包含字母、数字和\&quot;-\&quot;的字符串。
        :type policy_id: str
        :param urn: 统一资源名称。
        :type urn: str
        :param attached_at: 身份策略的附加时间。
        :type attached_at: datetime
        """
        
        

        self._policy_name = None
        self._policy_id = None
        self._urn = None
        self._attached_at = None
        self.discriminator = None

        self.policy_name = policy_name
        self.policy_id = policy_id
        self.urn = urn
        self.attached_at = attached_at

    @property
    def policy_name(self):
        r"""Gets the policy_name of this AttachedPolicy.

        身份策略名称，长度为1到128个字符，只包含字母、数字、\"_\"、\"+\"、\"=\"、\".\"、\"@\"和\"-\"的字符串。

        :return: The policy_name of this AttachedPolicy.
        :rtype: str
        """
        return self._policy_name

    @policy_name.setter
    def policy_name(self, policy_name):
        r"""Sets the policy_name of this AttachedPolicy.

        身份策略名称，长度为1到128个字符，只包含字母、数字、\"_\"、\"+\"、\"=\"、\".\"、\"@\"和\"-\"的字符串。

        :param policy_name: The policy_name of this AttachedPolicy.
        :type policy_name: str
        """
        self._policy_name = policy_name

    @property
    def policy_id(self):
        r"""Gets the policy_id of this AttachedPolicy.

        身份策略ID，长度为1到64个字符，只包含字母、数字和\"-\"的字符串。

        :return: The policy_id of this AttachedPolicy.
        :rtype: str
        """
        return self._policy_id

    @policy_id.setter
    def policy_id(self, policy_id):
        r"""Sets the policy_id of this AttachedPolicy.

        身份策略ID，长度为1到64个字符，只包含字母、数字和\"-\"的字符串。

        :param policy_id: The policy_id of this AttachedPolicy.
        :type policy_id: str
        """
        self._policy_id = policy_id

    @property
    def urn(self):
        r"""Gets the urn of this AttachedPolicy.

        统一资源名称。

        :return: The urn of this AttachedPolicy.
        :rtype: str
        """
        return self._urn

    @urn.setter
    def urn(self, urn):
        r"""Sets the urn of this AttachedPolicy.

        统一资源名称。

        :param urn: The urn of this AttachedPolicy.
        :type urn: str
        """
        self._urn = urn

    @property
    def attached_at(self):
        r"""Gets the attached_at of this AttachedPolicy.

        身份策略的附加时间。

        :return: The attached_at of this AttachedPolicy.
        :rtype: datetime
        """
        return self._attached_at

    @attached_at.setter
    def attached_at(self, attached_at):
        r"""Sets the attached_at of this AttachedPolicy.

        身份策略的附加时间。

        :param attached_at: The attached_at of this AttachedPolicy.
        :type attached_at: datetime
        """
        self._attached_at = attached_at

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
        if not isinstance(other, AttachedPolicy):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

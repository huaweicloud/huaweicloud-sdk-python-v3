# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AttachAgencyPolicyV5Request:

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
        'body': 'AttachAgencyPolicyReqBody'
    }

    attribute_map = {
        'policy_id': 'policy_id',
        'body': 'body'
    }

    def __init__(self, policy_id=None, body=None):
        r"""AttachAgencyPolicyV5Request

        The model defined in huaweicloud sdk

        :param policy_id: 身份策略ID，长度为1到64个字符，只包含字母、数字和\&quot;-\&quot;的字符串。
        :type policy_id: str
        :param body: Body of the AttachAgencyPolicyV5Request
        :type body: :class:`huaweicloudsdkiam.v5.AttachAgencyPolicyReqBody`
        """
        
        

        self._policy_id = None
        self._body = None
        self.discriminator = None

        self.policy_id = policy_id
        if body is not None:
            self.body = body

    @property
    def policy_id(self):
        r"""Gets the policy_id of this AttachAgencyPolicyV5Request.

        身份策略ID，长度为1到64个字符，只包含字母、数字和\"-\"的字符串。

        :return: The policy_id of this AttachAgencyPolicyV5Request.
        :rtype: str
        """
        return self._policy_id

    @policy_id.setter
    def policy_id(self, policy_id):
        r"""Sets the policy_id of this AttachAgencyPolicyV5Request.

        身份策略ID，长度为1到64个字符，只包含字母、数字和\"-\"的字符串。

        :param policy_id: The policy_id of this AttachAgencyPolicyV5Request.
        :type policy_id: str
        """
        self._policy_id = policy_id

    @property
    def body(self):
        r"""Gets the body of this AttachAgencyPolicyV5Request.

        :return: The body of this AttachAgencyPolicyV5Request.
        :rtype: :class:`huaweicloudsdkiam.v5.AttachAgencyPolicyReqBody`
        """
        return self._body

    @body.setter
    def body(self, body):
        r"""Sets the body of this AttachAgencyPolicyV5Request.

        :param body: The body of this AttachAgencyPolicyV5Request.
        :type body: :class:`huaweicloudsdkiam.v5.AttachAgencyPolicyReqBody`
        """
        self._body = body

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
        if not isinstance(other, AttachAgencyPolicyV5Request):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

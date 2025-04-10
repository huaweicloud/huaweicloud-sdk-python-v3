# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PrivatePolicyBodyPrimitiveTypeHolder:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'policy_body': 'str'
    }

    attribute_map = {
        'policy_body': 'policy_body'
    }

    def __init__(self, policy_body=None):
        r"""PrivatePolicyBodyPrimitiveTypeHolder

        The model defined in huaweicloud sdk

        :param policy_body: 策略内容。仅支持OPA开源引擎识别的，以Rego（https://www.openpolicyagent.org/docs/latest/policy-language/）语言编写的策略模板。  policy_body和policy_uri 必须有且只有一个存在
        :type policy_body: str
        """
        
        

        self._policy_body = None
        self.discriminator = None

        if policy_body is not None:
            self.policy_body = policy_body

    @property
    def policy_body(self):
        r"""Gets the policy_body of this PrivatePolicyBodyPrimitiveTypeHolder.

        策略内容。仅支持OPA开源引擎识别的，以Rego（https://www.openpolicyagent.org/docs/latest/policy-language/）语言编写的策略模板。  policy_body和policy_uri 必须有且只有一个存在

        :return: The policy_body of this PrivatePolicyBodyPrimitiveTypeHolder.
        :rtype: str
        """
        return self._policy_body

    @policy_body.setter
    def policy_body(self, policy_body):
        r"""Sets the policy_body of this PrivatePolicyBodyPrimitiveTypeHolder.

        策略内容。仅支持OPA开源引擎识别的，以Rego（https://www.openpolicyagent.org/docs/latest/policy-language/）语言编写的策略模板。  policy_body和policy_uri 必须有且只有一个存在

        :param policy_body: The policy_body of this PrivatePolicyBodyPrimitiveTypeHolder.
        :type policy_body: str
        """
        self._policy_body = policy_body

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
        if not isinstance(other, PrivatePolicyBodyPrimitiveTypeHolder):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

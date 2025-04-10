# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PolicyDelta:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'policy': 'Policy',
        'change_type': 'int'
    }

    attribute_map = {
        'policy': 'policy',
        'change_type': 'change_type'
    }

    def __init__(self, policy=None, change_type=None):
        r"""PolicyDelta

        The model defined in huaweicloud sdk

        :param policy: 
        :type policy: :class:`huaweicloudsdklakeformation.v1.Policy`
        :param change_type: 变更类型
        :type change_type: int
        """
        
        

        self._policy = None
        self._change_type = None
        self.discriminator = None

        if policy is not None:
            self.policy = policy
        if change_type is not None:
            self.change_type = change_type

    @property
    def policy(self):
        r"""Gets the policy of this PolicyDelta.

        :return: The policy of this PolicyDelta.
        :rtype: :class:`huaweicloudsdklakeformation.v1.Policy`
        """
        return self._policy

    @policy.setter
    def policy(self, policy):
        r"""Sets the policy of this PolicyDelta.

        :param policy: The policy of this PolicyDelta.
        :type policy: :class:`huaweicloudsdklakeformation.v1.Policy`
        """
        self._policy = policy

    @property
    def change_type(self):
        r"""Gets the change_type of this PolicyDelta.

        变更类型

        :return: The change_type of this PolicyDelta.
        :rtype: int
        """
        return self._change_type

    @change_type.setter
    def change_type(self, change_type):
        r"""Sets the change_type of this PolicyDelta.

        变更类型

        :param change_type: The change_type of this PolicyDelta.
        :type change_type: int
        """
        self._change_type = change_type

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
        if not isinstance(other, PolicyDelta):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

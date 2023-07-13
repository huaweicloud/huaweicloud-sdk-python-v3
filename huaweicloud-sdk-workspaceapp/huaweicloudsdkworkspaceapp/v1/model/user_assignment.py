# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UserAssignment:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'attach': 'str',
        'policy_statement_id': 'str'
    }

    attribute_map = {
        'attach': 'attach',
        'policy_statement_id': 'policy_statement_id'
    }

    def __init__(self, attach=None, policy_statement_id=None):
        """UserAssignment

        The model defined in huaweicloud sdk

        :param attach: 目标用户
        :type attach: str
        :param policy_statement_id: 策略ID
        :type policy_statement_id: str
        """
        
        

        self._attach = None
        self._policy_statement_id = None
        self.discriminator = None

        self.attach = attach
        self.policy_statement_id = policy_statement_id

    @property
    def attach(self):
        """Gets the attach of this UserAssignment.

        目标用户

        :return: The attach of this UserAssignment.
        :rtype: str
        """
        return self._attach

    @attach.setter
    def attach(self, attach):
        """Sets the attach of this UserAssignment.

        目标用户

        :param attach: The attach of this UserAssignment.
        :type attach: str
        """
        self._attach = attach

    @property
    def policy_statement_id(self):
        """Gets the policy_statement_id of this UserAssignment.

        策略ID

        :return: The policy_statement_id of this UserAssignment.
        :rtype: str
        """
        return self._policy_statement_id

    @policy_statement_id.setter
    def policy_statement_id(self, policy_statement_id):
        """Sets the policy_statement_id of this UserAssignment.

        策略ID

        :param policy_statement_id: The policy_statement_id of this UserAssignment.
        :type policy_statement_id: str
        """
        self._policy_statement_id = policy_statement_id

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
        if not isinstance(other, UserAssignment):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

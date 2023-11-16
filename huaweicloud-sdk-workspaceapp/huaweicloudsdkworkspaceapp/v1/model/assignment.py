# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Assignment:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'policy_statement_id': 'str',
        'attach': 'str',
        'attach_type': 'AttachType'
    }

    attribute_map = {
        'policy_statement_id': 'policy_statement_id',
        'attach': 'attach',
        'attach_type': 'attach_type'
    }

    def __init__(self, policy_statement_id=None, attach=None, attach_type=None):
        """Assignment

        The model defined in huaweicloud sdk

        :param policy_statement_id: 策略ID
        :type policy_statement_id: str
        :param attach: 目标
        :type attach: str
        :param attach_type: 
        :type attach_type: :class:`huaweicloudsdkworkspaceapp.v1.AttachType`
        """
        
        

        self._policy_statement_id = None
        self._attach = None
        self._attach_type = None
        self.discriminator = None

        self.policy_statement_id = policy_statement_id
        self.attach = attach
        self.attach_type = attach_type

    @property
    def policy_statement_id(self):
        """Gets the policy_statement_id of this Assignment.

        策略ID

        :return: The policy_statement_id of this Assignment.
        :rtype: str
        """
        return self._policy_statement_id

    @policy_statement_id.setter
    def policy_statement_id(self, policy_statement_id):
        """Sets the policy_statement_id of this Assignment.

        策略ID

        :param policy_statement_id: The policy_statement_id of this Assignment.
        :type policy_statement_id: str
        """
        self._policy_statement_id = policy_statement_id

    @property
    def attach(self):
        """Gets the attach of this Assignment.

        目标

        :return: The attach of this Assignment.
        :rtype: str
        """
        return self._attach

    @attach.setter
    def attach(self, attach):
        """Sets the attach of this Assignment.

        目标

        :param attach: The attach of this Assignment.
        :type attach: str
        """
        self._attach = attach

    @property
    def attach_type(self):
        """Gets the attach_type of this Assignment.

        :return: The attach_type of this Assignment.
        :rtype: :class:`huaweicloudsdkworkspaceapp.v1.AttachType`
        """
        return self._attach_type

    @attach_type.setter
    def attach_type(self, attach_type):
        """Sets the attach_type of this Assignment.

        :param attach_type: The attach_type of this Assignment.
        :type attach_type: :class:`huaweicloudsdkworkspaceapp.v1.AttachType`
        """
        self._attach_type = attach_type

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
        if not isinstance(other, Assignment):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
